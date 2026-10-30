"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeIssueArtifactInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.issue_artifact_id
    import capo_continuum.types.issue_id


class GetCodeIssueArtifactInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The environment that owns the issue."""
    issue_id: "capo_continuum.types.issue_id.IssueId"
    """The issue the artifact is attached to."""
    artifact_id: "capo_continuum.types.issue_artifact_id.IssueArtifactId"
    """The unique identifier of the artifact to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeIssueArtifactInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeIssueArtifactInput:
    out: GetCodeIssueArtifactInput = {}  # type: ignore[typeddict-item]
    return out
