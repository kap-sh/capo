"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListFirewallPoliciesV2Response``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.firewall_policies_v2
    import capo_network_firewall.types.pagination_token


class ListFirewallPoliciesV2Response(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    firewall_policies_v2: (
        "capo_network_firewall.types.firewall_policies_v2.FirewallPoliciesV2"
    )
    """<p>The metadata for the Next Generation policies. Depending on your setting for max results and the number of firewall policies that you have, this might not be the full list.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListFirewallPoliciesV2Response) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    import capo_network_firewall.types.firewall_policies_v2

    out["FirewallPoliciesV2"] = (
        capo_network_firewall.types.firewall_policies_v2.serialize_aws_json_1_0(
            value["firewall_policies_v2"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListFirewallPoliciesV2Response:
    out: ListFirewallPoliciesV2Response = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("FirewallPoliciesV2") is not None:
        import capo_network_firewall.types.firewall_policies_v2

        out["firewall_policies_v2"] = (
            capo_network_firewall.types.firewall_policies_v2.deserialize_aws_json_1_0(
                data["FirewallPoliciesV2"]
            )
        )
    else:
        out["firewall_policies_v2"] = []
    return out
