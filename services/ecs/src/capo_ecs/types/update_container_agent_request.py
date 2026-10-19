"""Generated from Smithy shape ``com.amazonaws.ecs#UpdateContainerAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class UpdateContainerAgentRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that your container instance is running on. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container_instance: "capo_ecs.types.string.String"
    """<p>The container instance ID or full ARN entries for the container instance where you would like to update the Amazon ECS container agent.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateContainerAgentRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    out["containerInstance"] = value["container_instance"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateContainerAgentRequest:
    out: UpdateContainerAgentRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("containerInstance") is not None:
        out["container_instance"] = data["containerInstance"]
    else:
        out["container_instance"] = ""
    return out
