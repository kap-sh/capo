"""Generated from Smithy shape ``com.amazonaws.continuum#GetCodeIssueInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.environment_id
    import capo_continuum.types.issue_id


class GetCodeIssueInput(TypedDict, closed=True):
    environment_id: "capo_continuum.types.environment_id.EnvironmentId"
    """The environment that owns the issue."""
    issue_id: "capo_continuum.types.issue_id.IssueId"
    """The unique identifier of the issue to retrieve."""


# --- restJson1 ser/de ---
def serialize_json(value: GetCodeIssueInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetCodeIssueInput:
    out: GetCodeIssueInput = {}  # type: ignore[typeddict-item]
    return out
