"""Generated from Smithy shape ``com.amazonaws.ecs#AssociateGatewayWithClusterResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_cluster_association_status
    import capo_ecs.types.string


class AssociateGatewayWithClusterResponse(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the gateway.</p>"""
    cluster_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the cluster.</p>"""
    status: NotRequired[
        "capo_ecs.types.gateway_cluster_association_status.GatewayClusterAssociationStatus"
    ]
    """<p>The status of the association. A new association is <code>ACTIVE</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateGatewayWithClusterResponse) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["gatewayArn"] = value["gateway_arn"]
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "status" in value:
        import capo_ecs.types.gateway_cluster_association_status

        out["status"] = (
            capo_ecs.types.gateway_cluster_association_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateGatewayWithClusterResponse:
    out: AssociateGatewayWithClusterResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayArn") is not None:
        out["gateway_arn"] = data["gatewayArn"]
    if data.get("clusterArn") is not None:
        out["cluster_arn"] = data["clusterArn"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_cluster_association_status

        out["status"] = (
            capo_ecs.types.gateway_cluster_association_status.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    return out
