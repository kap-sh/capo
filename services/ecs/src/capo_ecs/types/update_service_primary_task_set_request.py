"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateServicePrimaryTaskSetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class UpdateServicePrimaryTaskSetRequest(TypedDict, closed=True):
    cluster: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the service that the task set exists in.</p>"""
    service: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the service that the task set exists in.</p>"""
    primary_task_set: "capo_ecs.types.string.String"
    """<p>The short name or full Amazon Resource Name (ARN) of the task set to set as the primary task set in the deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateServicePrimaryTaskSetRequest) -> dict:
    out: dict = {}
    out["cluster"] = value["cluster"]
    out["service"] = value["service"]
    out["primaryTaskSet"] = value["primary_task_set"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateServicePrimaryTaskSetRequest:
    out: UpdateServicePrimaryTaskSetRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    else:
        out["cluster"] = ""
    if data.get("service") is not None:
        out["service"] = data["service"]
    else:
        out["service"] = ""
    if data.get("primaryTaskSet") is not None:
        out["primary_task_set"] = data["primaryTaskSet"]
    else:
        out["primary_task_set"] = ""
    return out
