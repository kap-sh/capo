"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateTaskSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.scale
    import capo_ecs.types.string


class UpdateTaskSetRequest(TypedDict, closed=True):
    cluster: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set is found in.</p>"""
    service: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task set is found in.</p>"""
    task_set: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the task set to update.</p>"""
    scale: "capo_ecs.types.scale.Scale"
    """<p>A floating-point percentage of the desired number of tasks to place and keep running in the task set.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateTaskSetRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    out["taskSet"] = value["task_set"]
    import capo_ecs.types.scale

    out["scale"] = capo_ecs.types.scale.serialize_aws_json_1_1(value["scale"])
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateTaskSetRequest:
    out: UpdateTaskSetRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("scale") is not None:
        import capo_ecs.types.scale

        out["scale"] = capo_ecs.types.scale.deserialize_aws_json_1_1(data["scale"])
    else:
        raise DeserializationError("UpdateTaskSetRequest.scale required")
    return out
