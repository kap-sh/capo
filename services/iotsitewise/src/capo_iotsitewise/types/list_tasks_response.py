"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListTasksResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.task_summaries


class ListTasksResponse(TypedDict, closed=True):
    task_summaries: "capo_iotsitewise.types.task_summaries.TaskSummaries"
    """<p>A list that summarizes each task in the workspace.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.pagination_token.PaginationToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTasksResponse) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.task_summaries

    out["taskSummaries"] = capo_iotsitewise.types.task_summaries.serialize_json(
        value["task_summaries"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTasksResponse:
    out: ListTasksResponse = {}  # type: ignore[typeddict-item]
    if data.get("taskSummaries") is not None:
        import capo_iotsitewise.types.task_summaries

        out["task_summaries"] = capo_iotsitewise.types.task_summaries.deserialize_json(
            data["taskSummaries"]
        )
    else:
        out["task_summaries"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
