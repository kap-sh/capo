"""Generated from Smithy shape ``com.amazonaws.connectscheduling#DurationValue``."""

from typing import TypeAlias

"""<p>A number of time units, which can be negative. It must stay within 876,000 hours (100 years) of zero: at most 52,560,000 <code>MINUTES</code>, 876,000 <code>HOURS</code>, or 36,500 <code>DAYS</code>.</p>"""
DurationValue: TypeAlias = int
