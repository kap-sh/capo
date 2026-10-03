"""Generated from Smithy shape ``com.amazonaws.iot#CancelAuditTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_task_id


class CancelAuditTaskRequest(TypedDict, closed=True):
    task_id: "capo_iot.types.audit_task_id.AuditTaskId"
    """<p>The ID of the audit you want to cancel. You can only cancel an audit that is "IN_PROGRESS".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CancelAuditTaskRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelAuditTaskRequest:
    out: CancelAuditTaskRequest = {}  # type: ignore[typeddict-item]
    return out
