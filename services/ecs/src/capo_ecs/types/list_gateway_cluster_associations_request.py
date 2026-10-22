"""Generated from Smithy shape ``com.amazonaws.ecs#ListGatewayClusterAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.gateway_cluster_association_status_list
    import capo_ecs.types.string


class ListGatewayClusterAssociationsRequest(TypedDict, closed=True):
    gateway: NotRequired["capo_ecs.types.string.String"]
    """<p>The name or Amazon Resource Name (ARN) of a gateway to filter the results by.</p>"""
    cluster: NotRequired["capo_ecs.types.string.String"]
    """<p>The name or Amazon Resource Name (ARN) of a cluster to filter the results by.</p>"""
    status: NotRequired[
        "capo_ecs.types.gateway_cluster_association_status_list.GatewayClusterAssociationStatusList"
    ]
    """<p>The association status to filter the results by.</p>"""
    max_results: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The maximum number of results that the operation returns in a single page. The default is 100.</p>"""
    next_token: NotRequired["capo_ecs.types.string.String"]
    """<p>The <code>nextToken</code> value returned from a previous paginated request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListGatewayClusterAssociationsRequest) -> dict:
    out: dict = {}
    if "gateway" in value:
        out["gateway"] = value["gateway"]
    if "cluster" in value:
        out["cluster"] = value["cluster"]
    if "status" in value:
        import capo_ecs.types.gateway_cluster_association_status_list

        out["status"] = (
            capo_ecs.types.gateway_cluster_association_status_list.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListGatewayClusterAssociationsRequest:
    out: ListGatewayClusterAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("gateway") is not None:
        out["gateway"] = data["gateway"]
    if data.get("cluster") is not None:
        out["cluster"] = data["cluster"]
    if data.get("status") is not None:
        import capo_ecs.types.gateway_cluster_association_status_list

        out["status"] = (
            capo_ecs.types.gateway_cluster_association_status_list.deserialize_aws_json_1_1(
                data["status"]
            )
        )
    if data.get("maxResults") is not None:
        out["max_results"] = data["maxResults"]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
