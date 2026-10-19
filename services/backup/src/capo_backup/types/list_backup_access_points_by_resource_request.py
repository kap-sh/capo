"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupAccessPointsByResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.list_backup_access_points_by_resource_request_max_results_integer
    import capo_backup.types.resource_arn


class ListBackupAccessPointsByResourceRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_backup.types.list_backup_access_points_by_resource_request_max_results_integer.ListBackupAccessPointsByResourceRequestMaxResultsInteger"
    ]
    """<p>The maximum number of items to be returned.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    resource_arn: "capo_backup.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the resource whose backup access points you want to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupAccessPointsByResourceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBackupAccessPointsByResourceRequest:
    out: ListBackupAccessPointsByResourceRequest = {}  # type: ignore[typeddict-item]
    return out
