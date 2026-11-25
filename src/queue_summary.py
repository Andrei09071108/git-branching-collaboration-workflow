"""Count tickets that still need attention."""
ACTIVE = ('open', 'waiting', 'reopened')

def count_active(tickets):
    return sum(status in ACTIVE for status in tickets)
