"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ListTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.list_tasks_request_max_results_integer
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.workspace_name


class ListTasksRequest(TypedDict, closed=True):
    workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName"
    """<p>The name of the workspace.</p>"""
    next_token: NotRequired["capo_iotsitewise.types.pagination_token.PaginationToken"]
    """<p>The token to be used for the next set of paginated results.</p>"""
    max_results: NotRequired[
        "capo_iotsitewise.types.list_tasks_request_max_results_integer.ListTasksRequestMaxResultsInteger"
    ]
    """<p>The maximum number of results to return for each paginated request. Default: 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListTasksRequest:
    out: ListTasksRequest = {}  # type: ignore[typeddict-item]
    return out
