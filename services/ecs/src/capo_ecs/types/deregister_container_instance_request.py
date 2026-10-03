"""Generated from Smithy shape ``com.amazonaws.ecs#DeregisterContainerInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.string


class DeregisterContainerInstanceRequest(TypedDict, closed=True):
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The short name or full Amazon Resource Name (ARN) of the cluster that hosts the container instance to deregister. If you do not specify a cluster, the default cluster is assumed.</p>"""
    container_instance: "capo_ecs.types.string.String"
    """<p>The container instance ID or full ARN of the container instance to deregister. For more information about the ARN format, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids">Amazon Resource Name (ARN)</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    force: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Forces the container instance to be deregistered. If you have tasks running on the container instance when you deregister it with the <code>force</code> option, these tasks remain running until you terminate the instance or the tasks stop through some other means, but they're orphaned (no longer monitored or accounted for by Amazon ECS). If an orphaned task on your container instance is part of an Amazon ECS service, then the service scheduler starts another copy of that task, on a different container instance if possible. </p> <p>Any containers in orphaned service tasks that are registered with a Classic Load Balancer or an Application Load Balancer target group are deregistered. They begin connection draining according to the settings on the load balancer or target group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterContainerInstanceRequest) -> dict:
    out: dict = {}
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    out["containerInstance"] = value["container_instance"]
    if "force" in value:
        out["force"] = value["force"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterContainerInstanceRequest:
    out: DeregisterContainerInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("containerInstance") is not None:
        out["container_instance"] = data["containerInstance"]
    else:
        raise DeserializationError(
            "DeregisterContainerInstanceRequest.container_instance required"
        )
    if data.get("force") is not None:
        out["force"] = data["force"]
    return out
