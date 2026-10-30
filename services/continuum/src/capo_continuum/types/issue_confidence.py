"""Generated from Smithy shape ``com.amazonaws.continuum#IssueConfidence``."""

from typing import TypeAlias

"""The likelihood that this issue is a true positive, expressed as a percentage (0-100). Distinct from severity, which measures impact rather than likelihood. Continuum sets this value; callers can't set it."""
IssueConfidence: TypeAlias = int
