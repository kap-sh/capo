"""Generated from Smithy shape ``com.amazonaws.iot#ListAuditTasksRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_task_status
    import capo_iot.types.audit_task_type
    import capo_iot.types.max_results
    import capo_iot.types.next_token
    import capo_iot.types.timestamp


class ListAuditTasksRequest(TypedDict, closed=True):
    start_time: "capo_iot.types.timestamp.Timestamp"
    """<p>The beginning of the time period. Audit information is retained for a limited time (90 days). Requesting a start time prior to what is retained results in an "InvalidRequestException".</p>"""
    end_time: "capo_iot.types.timestamp.Timestamp"
    """<p>The end of the time period.</p>"""
    task_type: NotRequired["capo_iot.types.audit_task_type.AuditTaskType"]
    """<p>A filter to limit the output to the specified type of audit: can be one of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED__AUDIT_TASK".</p>"""
    task_status: NotRequired["capo_iot.types.audit_task_status.AuditTaskStatus"]
    """<p>A filter to limit the output to audits with the specified completion status: can be one of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".</p>"""
    next_token: NotRequired["capo_iot.types.next_token.NextToken"]
    """<p>The token for the next set of results.</p>"""
    max_results: NotRequired["capo_iot.types.max_results.MaxResults"]
    """<p>The maximum number of results to return at one time. The default is 25.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAuditTasksRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAuditTasksRequest:
    out: ListAuditTasksRequest = {}  # type: ignore[typeddict-item]
    return out
