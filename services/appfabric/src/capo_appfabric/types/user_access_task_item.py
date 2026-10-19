"""Generated from Smithy shape ``com.amazonaws.appfabric#UserAccessTaskItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.string255
    import capo_appfabric.types.task_error
    import capo_appfabric.types.tenant_identifier
    import capo_appfabric.types.uuid


class UserAccessTaskItem(TypedDict, closed=True):
    app: "capo_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant_id: "capo_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    task_id: NotRequired["capo_appfabric.types.uuid.UUID"]
    """<p>The unique ID of the task.</p>"""
    error: NotRequired["capo_appfabric.types.task_error.TaskError"]
    """<p>Error from the task, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessTaskItem) -> dict:
    out: dict = {}
    out["app"] = value["app"]
    out["tenantId"] = value["tenant_id"]
    if "task_id" in value:
        out["taskId"] = value["task_id"]
    if "error" in value:
        import capo_appfabric.types.task_error

        out["error"] = capo_appfabric.types.task_error.serialize_json(value["error"])
    return out


def deserialize_json(data: dict) -> UserAccessTaskItem:
    out: UserAccessTaskItem = {}  # type: ignore[typeddict-item]
    if data.get("app") is not None:
        out["app"] = data["app"]
    else:
        out["app"] = ""
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    else:
        out["tenant_id"] = ""
    if data.get("taskId") is not None:
        out["task_id"] = data["taskId"]
    if data.get("error") is not None:
        import capo_appfabric.types.task_error

        out["error"] = capo_appfabric.types.task_error.deserialize_json(data["error"])
    return out
