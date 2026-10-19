"""Generated from Smithy shape ``com.amazonaws.backup#ListBackupAccessPointsByRecoveryPointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_backup.types.list_backup_access_points_by_recovery_point_request_max_results_integer
    import capo_backup.types.recovery_point_arn


class ListBackupAccessPointsByRecoveryPointRequest(TypedDict, closed=True):
    max_results: NotRequired[
        "capo_backup.types.list_backup_access_points_by_recovery_point_request_max_results_integer.ListBackupAccessPointsByRecoveryPointRequestMaxResultsInteger"
    ]
    """<p>The maximum number of items to be returned.</p>"""
    next_token: NotRequired["str"]
    """<p>The next item following a partial list of returned items. For example, if a request is made to return <code>MaxResults</code> number of items, <code>NextToken</code> allows you to return more items in your list starting at the location pointed to by the next token.</p>"""
    recovery_point_arn: "capo_backup.types.recovery_point_arn.RecoveryPointArn"
    """<p>The Amazon Resource Name (ARN) of the recovery point whose backup access points you want to list.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListBackupAccessPointsByRecoveryPointRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListBackupAccessPointsByRecoveryPointRequest:
    out: ListBackupAccessPointsByRecoveryPointRequest = {}  # type: ignore[typeddict-item]
    return out
