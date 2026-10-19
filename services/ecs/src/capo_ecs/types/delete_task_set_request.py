"""Generated from Smithy shape ``com.amazonaws.ecs#DeleteTaskSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.string


class DeleteTaskSetRequest(TypedDict, closed=True):
    cluster: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set found in to delete.</p>"""
    service: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that hosts the task set to delete.</p>"""
    task_set: "capo_ecs.types.string.String"
    """<p>The task set ID or full Amazon Resource Name (ARN) of the task set to delete.</p>"""
    force: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>If <code>true</code>, you can delete a task set even if it hasn't been scaled down to zero.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteTaskSetRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    out["taskSet"] = value["task_set"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteTaskSetRequest:
    out: DeleteTaskSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    else:
        out["cluster"] = ""
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("taskSet") is not None:
        out["task_set"] = data["taskSet"]
    else:
        out["task_set"] = ""
    if data.get("force") is not None:
        out["force"] = data["force"]
    return out
