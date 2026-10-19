"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListResolverEndpointIpAddressesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.max_results
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.resource_id


class ListResolverEndpointIpAddressesRequest(TypedDict, closed=True):
    resolver_endpoint_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the Resolver endpoint that you want to get IP addresses for.</p>"""
    max_results: NotRequired["capo_route53resolver.types.max_results.MaxResults"]
    """<p>The maximum number of IP addresses that you want to return in the response to a <code>ListResolverEndpointIpAddresses</code> request. If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 IP addresses. </p>"""
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>For the first <code>ListResolverEndpointIpAddresses</code> request, omit this value.</p> <p>If the specified Resolver endpoint has more than <code>MaxResults</code> IP addresses, you can submit another <code>ListResolverEndpointIpAddresses</code> request to get the next group of IP addresses. In the next request, specify the value of <code>NextToken</code> from the previous response. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListResolverEndpointIpAddressesRequest) -> dict:
    out: dict = {}
    out["ResolverEndpointId"] = value["resolver_endpoint_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListResolverEndpointIpAddressesRequest:
    out: ListResolverEndpointIpAddressesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResolverEndpointId") is not None:
        out["resolver_endpoint_id"] = data["ResolverEndpointId"]
    else:
        out["resolver_endpoint_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
