"""Score classification and report completeness, not semantic correctness."""
import argparse
import json
from pathlib import Path


def score(expectations, mapping, results):
    valid_categories = {f'S{i:02}' for i in range(1, 24)}
    if len({item['id'] for item in expectations}) != len(expectations):
        raise ValueError('Duplicate expectation ids')
    if len({item['case'] for item in mapping}) != len(mapping):
        raise ValueError('Duplicate mapping aliases')
    expected = {item['id']: item for item in expectations}
    aliases = {item['case']: item['id'] for item in mapping}
    seen = set()
    checks = []
    for result in results:
        case = result['case']
        if case in seen or case not in aliases:
            raise ValueError(f'Duplicate or unknown case: {case}')
        seen.add(case)
        item = expected[aliases[case]]
        findings = result.get('findings', [])
        uncertain = result.get('uncertain', [])
        exclusions = result.get('exclusions', [])
        for collection in [findings, uncertain, exclusions]:
            if not isinstance(collection, list):
                raise ValueError(f'{case}: expected a list')
            for entry in collection:
                if entry.get('category') not in valid_categories:
                    raise ValueError(f'{case}: unknown category')
                if not isinstance(entry.get('related_categories', []), list):
                    raise ValueError(f'{case}: related categories must be a list')
                if any(label not in valid_categories
                       for label in entry.get('related_categories', [])):
                    raise ValueError(f'{case}: unknown related category')
        if any(not entry.get('missing') for entry in uncertain):
            raise ValueError(f'{case}: uncertainty needs a concrete evidence gap')
        primary_labels = {entry['category'] for entry in findings}
        primary_uncertain = {entry['category'] for entry in uncertain}
        labels = primary_labels | {label for entry in findings
                                   for label in entry.get('related_categories', [])}
        uncertain_labels = primary_uncertain | {label for entry in uncertain
                                                for label in entry.get('related_categories', [])}
        target = item['target']
        if item['expected'] == 'finding':
            passed = target in labels
            primary_pass = target in primary_labels
        elif item['expected'] == 'exclude':
            passed = target not in labels and target not in uncertain_labels
            primary_pass = target not in primary_labels and target not in primary_uncertain
        else:
            passed = target not in labels and target in uncertain_labels
            primary_pass = target not in primary_labels and target in primary_uncertain
        complete = all(all(entry.get(field) for field in
                           ['location', 'evidence', 'impact', 'suggestion'])
                       for entry in findings)
        checks.append({'case': case, 'id': item['id'],
                       'expected': item['expected'], 'target': target,
                       'classification_pass': passed,
                       'primary_label_pass': primary_pass,
                       'finding_fields_complete': complete,
                       'other_finding_labels': sorted(labels - {target})})
    if seen != set(aliases):
        raise ValueError(f'Missing cases: {sorted(set(aliases) - seen)}')
    return {'cases': len(checks),
            'classification_passes': sum(x['classification_pass'] for x in checks),
            'primary_label_passes': sum(x['primary_label_pass'] for x in checks),
            'by_outcome': {outcome: {
                'total': sum(x['expected'] == outcome for x in checks),
                'passed': sum(x['expected'] == outcome and x['classification_pass']
                              for x in checks)}
                for outcome in ['finding', 'exclude', 'uncertain']},
            'complete_finding_fields': all(x['finding_fields_complete'] for x in checks),
            'checks': checks,
            'limitation': 'Target-label and field checks require independent semantic review.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expectations', type=Path, required=True)
    parser.add_argument('--mapping', type=Path, required=True)
    parser.add_argument('--results', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    report = score(*(json.loads(path.read_text()) for path in
                     [args.expectations, args.mapping, args.results]))
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(f"{report['classification_passes']}/{report['cases']} target classifications passed")
