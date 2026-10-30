"""Generated from Smithy shape ``com.amazonaws.continuum#CodeIssueArtifactItems``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_continuum.types.issue_artifact_item

CodeIssueArtifactItems: TypeAlias = list[
    "capo_continuum.types.issue_artifact_item.IssueArtifactItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: CodeIssueArtifactItems) -> list:
    import capo_continuum.types.issue_artifact_item

    out: list = []
    for item in value:
        out.append(capo_continuum.types.issue_artifact_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> CodeIssueArtifactItems:
    import capo_continuum.types.issue_artifact_item

    out: CodeIssueArtifactItems = []
    for item in data:
        if item is None:
            continue
        out.append(capo_continuum.types.issue_artifact_item.deserialize_json(item))
    return out
