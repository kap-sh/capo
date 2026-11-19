"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListVpcEndpointAssociationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.pagination_max_results
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.resource_arn


class ListVpcEndpointAssociationsRequest(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    max_results: NotRequired[
        "capo_network_firewall.types.pagination_max_results.PaginationMaxResults"
    ]
    """<p>The maximum number of objects that you want Network Firewall to return for this request. If more objects are available, in the response, Network Firewall provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p>"""
    firewall_arn: NotRequired["capo_network_firewall.types.resource_arn.ResourceArn"]
    """<p>The Amazon Resource Name (ARN) of the firewall.</p> <p>If you don't specify this, Network Firewall retrieves all VPC endpoint associations that you have defined.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListVpcEndpointAssociationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListVpcEndpointAssociationsRequest:
    out: ListVpcEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListVpcEndpointAssociationsRequest) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "firewall_arn" in value:
        out["FirewallArn"] = value["firewall_arn"]
    return out


def deserialize_cbor(data: dict) -> ListVpcEndpointAssociationsRequest:
    out: ListVpcEndpointAssociationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("FirewallArn") is not None:
        out["firewall_arn"] = data["FirewallArn"]
    return out
