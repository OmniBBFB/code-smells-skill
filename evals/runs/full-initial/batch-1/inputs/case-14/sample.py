class Subscription:
    """Owns entitlement rules, including grace-period billing eligibility."""
    def __init__(self, active, grace_days, overdue_days):
        self.active = active
        self.grace_days = grace_days
        self.overdue_days = overdue_days

class InvoiceRenderer:
    def render(self, subscription):
        eligible = subscription.active or (
            subscription.overdue_days <= subscription.grace_days
        )
        return "billable" if eligible else "paused"
