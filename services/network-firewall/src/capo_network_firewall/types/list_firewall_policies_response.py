"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFirewallPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policies
    import capo_network_firewall.types.pagination_token


class ListFirewallPoliciesResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    firewall_policies: NotRequired[
        "capo_network_firewall.types.firewall_policies.FirewallPolicies"
    ]
    """<p>The metadata for the firewall policies. Depending on your setting for max results and the number of firewall policies that you have, this might not be the full list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFirewallPoliciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewall_policies" in value:
        import capo_network_firewall.types.firewall_policies

        out["FirewallPolicies"] = (
            capo_network_firewall.types.firewall_policies.serialize_aws_json_1_0(
                value["firewall_policies"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFirewallPoliciesResponse:
    out: ListFirewallPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("FirewallPolicies") is not None:
        import capo_network_firewall.types.firewall_policies

        out["firewall_policies"] = (
            capo_network_firewall.types.firewall_policies.deserialize_aws_json_1_0(
                data["FirewallPolicies"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListFirewallPoliciesResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "firewall_policies" in value:
        import capo_network_firewall.types.firewall_policies

        out["FirewallPolicies"] = (
            capo_network_firewall.types.firewall_policies.serialize_cbor(
                value["firewall_policies"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ListFirewallPoliciesResponse:
    out: ListFirewallPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("FirewallPolicies") is not None:
        import capo_network_firewall.types.firewall_policies

        out["firewall_policies"] = (
            capo_network_firewall.types.firewall_policies.deserialize_cbor(
                data["FirewallPolicies"]
            )
        )
    return out
