"""Generated from Smithy shape ``com.amazonaws.ecs#ServiceRegistry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string


class ServiceRegistry(TypedDict, closed=True):
    registry_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the service registry. The currently supported service registry is Cloud Map. For more information, see <a href="https://docs.aws.amazon.com/cloud-map/latest/api/API_CreateService.html">CreateService</a>.</p>"""
    port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port value used if your service discovery service specified an SRV record. This field might be used if both the <code>awsvpc</code> network mode and SRV records are used.</p>"""
    container_name: NotRequired["capo_ecs.types.string.String"]
    """<p>The container name value to be used for your service discovery service. It's already specified in the task definition. If the task definition that your service task specifies uses the <code>bridge</code> or <code>host</code> network mode, you must specify a <code>containerName</code> and <code>containerPort</code> combination from the task definition. If the task definition that your service task specifies uses the <code>awsvpc</code> network mode and a type SRV DNS record is used, you must specify either a <code>containerName</code> and <code>containerPort</code> combination or a <code>port</code> value. However, you can't specify both.</p>"""
    container_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port value to be used for your service discovery service. It's already specified in the task definition. If the task definition your service task specifies uses the <code>bridge</code> or <code>host</code> network mode, you must specify a <code>containerName</code> and <code>containerPort</code> combination from the task definition. If the task definition your service task specifies uses the <code>awsvpc</code> network mode and a type SRV DNS record is used, you must specify either a <code>containerName</code> and <code>containerPort</code> combination or a <code>port</code> value. However, you can't specify both.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ServiceRegistry) -> dict:
    out: dict = {}
    if "registry_arn" in value:
        out["registryArn"] = value["registry_arn"]
    if "port" in value:
        out["port"] = value["port"]
    if "container_name" in value:
        out["containerName"] = value["container_name"]
    if "container_port" in value:
        out["containerPort"] = value["container_port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ServiceRegistry:
    out: ServiceRegistry = {}  # type: ignore[typeddict-item]
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    if data.get("port") is not None:
        out["port"] = data["port"]
    if data.get("containerName") is not None:
        out["container_name"] = data["containerName"]
    if data.get("containerPort") is not None:
        out["container_port"] = data["containerPort"]
    return out
