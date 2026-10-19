"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupAccessPointsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.list_backup_access_points_request_max_results_integer


class ListBackupAccessPointsRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_backup.types.list_backup_access_points_request_max_results_integer.ListBackupAccessPointsRequestMaxResultsInteger"
    ]
    """<p>The maximum number of items to be returned.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupAccessPointsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBackupAccessPointsRequest:
    out: ListBackupAccessPointsRequest = {}  # type: ignore[typeddict-item]
    return out
