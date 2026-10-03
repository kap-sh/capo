"""Generated from Smithy shape ``com.amazonaws.iot#AuditTaskMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.audit_task_id
    import capo_iot.types.audit_task_status
    import capo_iot.types.audit_task_type


class AuditTaskMetadata(TypedDict, closed=True):
    task_id: NotRequired["capo_iot.types.audit_task_id.AuditTaskId"]
    """<p>The ID of this audit.</p>"""
    task_status: NotRequired["capo_iot.types.audit_task_status.AuditTaskStatus"]
    """<p>The status of this audit. One of "IN_PROGRESS", "COMPLETED", "FAILED", or "CANCELED".</p>"""
    task_type: NotRequired["capo_iot.types.audit_task_type.AuditTaskType"]
    """<p>The type of this audit. One of "ON_DEMAND_AUDIT_TASK" or "SCHEDULED_AUDIT_TASK".</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuditTaskMetadata) -> dict:
    out: dict = {}
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "task_status" in value:
        import capo_iot.types.audit_task_status

        out["taskStatus"] = capo_iot.types.audit_task_status.serialize_json(
            value["task_status"]
        )
    if "task_type" in value:
        import capo_iot.types.audit_task_type

        out["taskType"] = capo_iot.types.audit_task_type.serialize_json(
            value["task_type"]
        )
    return out


def deserialize_json(data: dict) -> AuditTaskMetadata:
    out: AuditTaskMetadata = {}  # type: ignore[typeddict-item]
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("taskStatus") is not None:
        import capo_iot.types.audit_task_status

        out["task_status"] = capo_iot.types.audit_task_status.deserialize_json(
            data["taskStatus"]
        )
    if data.get("taskType") is not None:
        import capo_iot.types.audit_task_type

        out["task_type"] = capo_iot.types.audit_task_type.deserialize_json(
            data["taskType"]
        )
    return out
