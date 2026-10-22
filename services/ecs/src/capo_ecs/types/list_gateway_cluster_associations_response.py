"""Generated from Smithy shape ``com.amazonaws.ecs#ListGatewayClusterAssociationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.gateway_cluster_association_summary_list
    import capo_ecs.types.string


class ListGatewayClusterAssociationsResponse(TypedDict, closed=True):
    gateway_cluster_associations: NotRequired[
        "capo_ecs.types.gateway_cluster_association_summary_list.GatewayClusterAssociationSummaryList"
    ]
    """<p>The gateway-cluster associations that match the request.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value to include in a future request to retrieve the next page of results. This value is <code>null</code> when there are no more results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewayClusterAssociationsResponse) -> dict:
    out: dict = {}
    if "gateway_cluster_associations" in value:
        import capo_ecs.types.gateway_cluster_association_summary_list

        out["gatewayClusterAssociations"] = (
            capo_ecs.types.gateway_cluster_association_summary_list.serialize_aws_json_1_1(
                value["gateway_cluster_associations"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewayClusterAssociationsResponse:
    out: ListGatewayClusterAssociationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayClusterAssociations") is not None:
        import capo_ecs.types.gateway_cluster_association_summary_list

        out["gateway_cluster_associations"] = (
            capo_ecs.types.gateway_cluster_association_summary_list.deserialize_aws_json_1_1(
                data["gatewayClusterAssociations"]
            )
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
