"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListProjectsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.project_summaries


class ListProjectsResponse(TypedDict, closed=True):
    project_summaries: "capo_iotsitewise.types.project_summaries.ProjectSummaries"
    """<p>A list that summarizes each project in the portal.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.next_token.NextToken"]
    """<p>The token for the next set of results, or null if there are no additional results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListProjectsResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.project_summaries

    out["projectSummaries"] = capo_iotsitewise.types.project_summaries.serialize_json(
        value["project_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListProjectsResponse:
    out: ListProjectsResponse = {}  # type: ignore[typeddict-item]
    if data.get("projectSummaries") is not None:
        import capo_iotsitewise.types.project_summaries

        out["project_summaries"] = (
            capo_iotsitewise.types.project_summaries.deserialize_json(
                data["projectSummaries"]
            )
        )
    else:
        out["project_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
