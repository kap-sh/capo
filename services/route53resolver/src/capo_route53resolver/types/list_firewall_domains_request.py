"""Generated from Smithy shape ``com.amazonaws.route53resolver#ListFirewallDomainsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_route53resolver.types.list_domain_max_results
    import capo_route53resolver.types.next_token
    import capo_route53resolver.types.resource_id


class ListFirewallDomainsRequest(TypedDict, closed=True):
    firewall_domain_list_id: "capo_route53resolver.types.resource_id.ResourceId"
    """<p>The ID of the domain list whose domains you want to retrieve. </p>"""
    max_results: NotRequired[
        "capo_route53resolver.types.list_domain_max_results.ListDomainMaxResults"
    ]
    """<p>The maximum number of objects that you want Resolver to return for this request. If more objects are available, in the response, Resolver provides a <code>NextToken</code> value that you can use in a subsequent call to get the next batch of objects.</p> <p>If you don't specify a value for <code>MaxResults</code>, Resolver returns up to 100 objects. </p>"""
    next_token: NotRequired["capo_route53resolver.types.next_token.NextToken"]
    """<p>For the first call to this list request, omit this value.</p> <p>When you request a list of objects, Resolver returns at most the number of objects specified in <code>MaxResults</code>. If more objects are available for retrieval, Resolver returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token that was returned for the prior request in your next request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFirewallDomainsRequest) -> dict:
    out: dict = {}
    out["FirewallDomainListId"] = value["firewall_domain_list_id"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFirewallDomainsRequest:
    out: ListFirewallDomainsRequest = {}  # type: ignore[typeddict-item]
    if data.get("FirewallDomainListId") is not None:
        out["firewall_domain_list_id"] = data["FirewallDomainListId"]
    else:
        out["firewall_domain_list_id"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
