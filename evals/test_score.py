import unittest

from score import score


class ScoreTests(unittest.TestCase):
    def evaluate(self, expected, result):
        return score([{'id': 'sample', 'target': 'S02', 'expected': expected}],
                     [{'case': 'case-01', 'id': 'sample'}],
                     [{'case': 'case-01', **result}])

    def finding(self, category='S02', related=None):
        return {'category': category, 'related_categories': related or [],
                'location': 'sample.py:1', 'evidence': 'two responsibility clusters',
                'impact': 'independent rules require one module change',
                'suggestion': 'separate the rule owners'}

    def test_evidence_backed_secondary_label_is_not_a_primary_match(self):
        result = self.evaluate('finding', {
            'findings': [self.finding('S10', ['S02'])]})
        self.assertEqual(result['classification_passes'], 1)
        self.assertEqual(result['primary_label_passes'], 0)

    def test_secondary_false_positive_fails_negative_case(self):
        result = self.evaluate('exclude', {
            'findings': [self.finding('S10', ['S02'])]})
        self.assertEqual(result['classification_passes'], 0)

    def test_uncertainty_is_not_a_confirmed_finding(self):
        result = self.evaluate('uncertain', {
            'findings': [self.finding()],
            'uncertain': [{'category': 'S02', 'missing': 'full class definition'}]})
        self.assertEqual(result['classification_passes'], 0)

    def test_missing_finding_evidence_is_reported(self):
        incomplete = self.finding()
        del incomplete['evidence']
        result = self.evaluate('finding', {'findings': [incomplete]})
        self.assertFalse(result['complete_finding_fields'])

    def test_unknown_related_category_is_rejected(self):
        with self.assertRaises(ValueError):
            self.evaluate('finding', {'findings': [self.finding('S10', ['S99'])]})

    def test_uncertainty_needs_evidence_gap(self):
        with self.assertRaises(ValueError):
            self.evaluate('uncertain', {'uncertain': [{'category': 'S02'}]})

    def test_missing_case_is_rejected(self):
        with self.assertRaises(ValueError):
            score([{'id': 'x', 'target': 'S02', 'expected': 'finding'}],
                  [{'case': 'case-01', 'id': 'x'}], [])

    def test_duplicate_case_is_rejected(self):
        result = {'case': 'case-01', 'findings': []}
        with self.assertRaises(ValueError):
            score([{'id': 'x', 'target': 'S02', 'expected': 'exclude'}],
                  [{'case': 'case-01', 'id': 'x'}], [result, result])


if __name__ == '__main__':
    unittest.main()
