"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#UtcDate``."""

from typing import TypeAlias

"""A UTC calendar date, `YYYY-MM-DD`. <p>A date and not a `timestamp` on purpose. The values this carries — a campaign's run window, an asset's send date — are calendar dates a partner picks in a wizard, with no meaningful time-of-day; modelling them as an instant invited callers to send one, which then had to be parsed back out and truncated. The pattern is the whole contract, so an invalid date is rejected at the edge rather than surfacing later as a malformed schedule."""
UtcDate: TypeAlias = str
