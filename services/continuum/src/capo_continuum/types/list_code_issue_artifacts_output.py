"""Generated from Smithy shape ``com.amazonaws.continuum#ListCodeIssueArtifactsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.code_issue_artifact_items
    import capo_continuum.types.next_token


class ListCodeIssueArtifactsOutput(TypedDict, closed=True):
    items: "capo_continuum.types.code_issue_artifact_items.CodeIssueArtifactItems"
    """The artifacts attached to the issue, ordered by artifactId descending."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """A pagination token to retrieve the next page of results. Absent when there are no more results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeIssueArtifactsOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.code_issue_artifact_items

    out["items"] = capo_continuum.types.code_issue_artifact_items.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeIssueArtifactsOutput:
    out: ListCodeIssueArtifactsOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_continuum.types.code_issue_artifact_items

        out["items"] = capo_continuum.types.code_issue_artifact_items.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
