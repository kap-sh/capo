"""Generated from Smithy shape ``com.amazonaws.continuum#ListCodeIssuesOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_continuum.types.code_issue_summaries
    import capo_continuum.types.next_token


class ListCodeIssuesOutput(TypedDict, closed=True):
    items: "capo_continuum.types.code_issue_summaries.CodeIssueSummaries"
    """The issues in the environment, ordered by issueId descending."""
    next_token: NotRequired["capo_continuum.types.next_token.NextToken"]
    """A pagination token to retrieve the next page of results. Absent when there are no more results."""


# --- restJson1 ser/de ---
def serialize_json(value: ListCodeIssuesOutput) -> dict:
    out: dict = {}
    import capo_continuum.types.code_issue_summaries

    out["items"] = capo_continuum.types.code_issue_summaries.serialize_json(
        value["items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListCodeIssuesOutput:
    out: ListCodeIssuesOutput = {}  # type: ignore[typeddict-item]
    if data.get("items") is not None:
        import capo_continuum.types.code_issue_summaries

        out["items"] = capo_continuum.types.code_issue_summaries.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
