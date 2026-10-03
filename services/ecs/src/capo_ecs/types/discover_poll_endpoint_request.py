"""Generated from Smithy shape ``com.amazonaws.ecs#DiscoverPollEndpointRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.string


class DiscoverPollEndpointRequest(TypedDict, closed=True):
    container_instance: NotRequired["capo_ecs.types.string.String"]
    """<p>The container instance ID or full ARN of the container instance. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that the container instance belongs to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DiscoverPollEndpointRequest) -> dict:
    out: dict = {}
    if "container_instance" in value:
        out["containerInstance"] = value["container_instance"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DiscoverPollEndpointRequest:
    out: DiscoverPollEndpointRequest = {}  # type: ignore[typeddict-item]
    if data.get("containerInstance") is not None:
        out["container_instance"] = data["containerInstance"]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    return out
