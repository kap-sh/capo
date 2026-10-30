"""Generated from Smithy shape ``com.amazonaws.continuum#FindingDescription``."""

from typing import TypeAlias

"""Free-form prose about a finding (summary, detailed analysis, rationale, remediation guidance). Capped well below the finding document's own 256 KB limit, since several of these can appear on one finding."""
FindingDescription: TypeAlias = str
