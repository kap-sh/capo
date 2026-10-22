"""Generated from Smithy shape ``com.amazonaws.ecs#GatewayResources``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_infrastructure_resources
    import capo_ecs.types.string


class GatewayResources(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    resources: NotRequired[
        "capo_ecs.types.gateway_infrastructure_resources.GatewayInfrastructureResources"
    ]
    """<p>The infrastructure resources that the gateway manages.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GatewayResources) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "resources" in value:
        import capo_ecs.types.gateway_infrastructure_resources

        out["resources"] = (
            capo_ecs.types.gateway_infrastructure_resources.serialize_aws_json_1_1(
                value["resources"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GatewayResources:
    out: GatewayResources = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("resources") is not None:
        import capo_ecs.types.gateway_infrastructure_resources

        out["resources"] = (
            capo_ecs.types.gateway_infrastructure_resources.deserialize_aws_json_1_1(
                data["resources"]
            )
        )
    return out
