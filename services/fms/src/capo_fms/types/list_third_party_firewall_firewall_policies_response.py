"""Generated from Smithy shape ``com.amazonaws.fms#ListThirdPartyFirewallFirewallPoliciesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.pagination_token
    import capo_fms.types.third_party_firewall_firewall_policies


class ListThirdPartyFirewallFirewallPoliciesResponse(TypedDict, closed=True):
    third_party_firewall_firewall_policies: NotRequired[
        "capo_fms.types.third_party_firewall_firewall_policies.ThirdPartyFirewallFirewallPolicies"
    ]
    """<p>A list that contains one <code>ThirdPartyFirewallFirewallPolicies</code> element for each third-party firewall policies that the specified third-party firewall vendor is associated with. Each <code>ThirdPartyFirewallFirewallPolicies</code> element contains the firewall policy name and ID.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>The value that you will use for <code>NextToken</code> in the next <code>ListThirdPartyFirewallFirewallPolicies</code> request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListThirdPartyFirewallFirewallPoliciesResponse,
) -> dict:
    out: dict = {}
    if "third_party_firewall_firewall_policies" in value:
        import capo_fms.types.third_party_firewall_firewall_policies

        out["ThirdPartyFirewallFirewallPolicies"] = (
            capo_fms.types.third_party_firewall_firewall_policies.serialize_aws_json_1_1(
                value["third_party_firewall_firewall_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListThirdPartyFirewallFirewallPoliciesResponse:
    out: ListThirdPartyFirewallFirewallPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallFirewallPolicies") is not None:
        import capo_fms.types.third_party_firewall_firewall_policies

        out["third_party_firewall_firewall_policies"] = (
            capo_fms.types.third_party_firewall_firewall_policies.deserialize_aws_json_1_1(
                data["ThirdPartyFirewallFirewallPolicies"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListThirdPartyFirewallFirewallPoliciesResponse) -> dict:
    out: dict = {}
    if "third_party_firewall_firewall_policies" in value:
        import capo_fms.types.third_party_firewall_firewall_policies

        out["ThirdPartyFirewallFirewallPolicies"] = (
            capo_fms.types.third_party_firewall_firewall_policies.serialize_cbor(
                value["third_party_firewall_firewall_policies"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> ListThirdPartyFirewallFirewallPoliciesResponse:
    out: ListThirdPartyFirewallFirewallPoliciesResponse = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewallFirewallPolicies") is not None:
        import capo_fms.types.third_party_firewall_firewall_policies

        out["third_party_firewall_firewall_policies"] = (
            capo_fms.types.third_party_firewall_firewall_policies.deserialize_cbor(
                data["ThirdPartyFirewallFirewallPolicies"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
