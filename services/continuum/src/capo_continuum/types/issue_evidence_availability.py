"""Generated from Smithy shape ``com.amazonaws.continuum#IssueEvidenceAvailability``."""

from typing import Literal, TypeAlias, cast

"""Whether this issue has any evidence (formerly 'artifacts') attached. NONE = no evidence; AVAILABLE = at least one evidence item exists -- call ListCodeIssueArtifacts to retrieve."""
IssueEvidenceAvailability: TypeAlias = Literal[
    "NONE",
    "AVAILABLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssueEvidenceAvailability) -> str:
    return value


def deserialize_json(data: str) -> IssueEvidenceAvailability:
    return cast(IssueEvidenceAvailability, data)
