"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFlowOperationResultsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.availability_zone
    import capo_network_firewall.types.flow_operation_id
    import capo_network_firewall.types.pagination_max_results
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.vpc_endpoint_id


class ListFlowOperationResultsRequest(TypedDict, closed=True):
    firewall_arn: "capo_network_firewall.types.resource_arn.ResourceArn"
    """<p>The Amazon Resource Name (ARN) of the firewall.</p>"""
    flow_operation_id: "capo_network_firewall.types.flow_operation_id.FlowOperationId"
    """<p>A unique identifier for the flow operation. This ID is returned in the responses to start and list commands. You provide to describe commands.</p>"""
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    max_results: NotRequired[
        "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    availability_zone: NotRequired[
        "capo_network_firewall.types.availability_zone.AvailabilityZone"
    ]
    """<p>The ID of the Availability Zone where the firewall is located. For example, <code>us-east-2a</code>.</p> <p>Defines the scope a flow operation. You can use up to 20 filters to configure a single flow operation.</p>"""
    vpc_endpoint_id: NotRequired[
        "capo_network_firewall.types.vpc_endpoint_id.VpcEndpointId"
    ]
    """<p>A unique identifier for the primary endpoint associated with a firewall.</p>"""
    vpc_endpoint_association_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a VPC endpoint association.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFlowOperationResultsRequest) -> dict:
    out: dict = {}
    out["FirewallArn"] = value["firewall_arn"]
    out["FlowOperationId"] = value["flow_operation_id"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "availability_zone" in value:
        out["AvailabilityZone"] = value["availability_zone"]
    if "vpc_endpoint_id" in value:
        out["VpcEndpointId"] = value["vpc_endpoint_id"]
    if "vpc_endpoint_association_arn" in value:
        out["VpcEndpointAssociationArn"] = value["vpc_endpoint_association_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFlowOperationResultsRequest:
    out: ListFlowOperationResultsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    else:
        out["firewall_arn"] = ""
    if data.get("FlowOperationId") is not None:
        out["flow_operation_id"] = data["FlowOperationId"]
    else:
        out["flow_operation_id"] = ""
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("AvailabilityZone") is not None:
        out["availability_zone"] = data["AvailabilityZone"]
    if data.get("VpcEndpointId") is not None:
        out["vpc_endpoint_id"] = data["VpcEndpointId"]
    if data.get("VpcEndpointAssociationArn") is not None:
        out["vpc_endpoint_association_arn"] = data["VpcEndpointAssociationArn"]
    return out
