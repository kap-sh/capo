"""Generated from Smithy shape ``com.amazonaws.continuum#IssueArtifactType``."""

from typing import Literal, TypeAlias, cast

"""The category of an artifact attached to an issue, such as evidence, validation evidence, a remediation proposal, a decision, or a patch."""
IssueArtifactType: TypeAlias = Literal[
    "EVIDENCE",
    "AGENT_COMMUNICATION",
    "VALIDATION_EVIDENCE",
    "REMEDIATION_PROPOSAL",
    "DECISION",
    "PATCH",
]


# --- restJson1 ser/de ---
def serialize_json(value: IssueArtifactType) -> str:
    return value


def deserialize_json(data: str) -> IssueArtifactType:
    return cast(IssueArtifactType, data)
