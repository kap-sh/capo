"""Generated from Smithy shape ``com.amazonaws.fms#ListThirdPartyFirewallFirewallPoliciesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.pagination_max_results
    import capo_fms.types.pagination_token
    import capo_fms.types.third_party_firewall


class ListThirdPartyFirewallFirewallPoliciesRequest(TypedDict, closed=True):
    third_party_firewall: "capo_fms.types.third_party_firewall.ThirdPartyFirewall"
    """<p>The name of the third-party firewall vendor.</p>"""
    next_token: NotRequired["capo_fms.types.pagination_token.PaginationToken"]
    """<p>If the previous response included a <code>NextToken</code> element, the specified third-party firewall vendor is associated with more third-party firewall policies. To get more third-party firewall policies, submit another <code>ListThirdPartyFirewallFirewallPoliciesRequest</code> request.</p> <p> For the value of <code>NextToken</code>, specify the value of <code>NextToken</code> from the previous response. If the previous response didn't include a <code>NextToken</code> element, there are no more third-party firewall policies to get. </p>"""
    max_results: "capo_fms.types.pagination_max_results.PaginationMaxResults"
    """<p>The maximum number of third-party firewall policies that you want Firewall Manager to return. If the specified third-party firewall vendor is associated with more than <code>MaxResults</code> firewall policies, the response includes a <code>NextToken</code> element. <code>NextToken</code> contains an encrypted token that identifies the first third-party firewall policies that Firewall Manager will return if you submit another request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListThirdPartyFirewallFirewallPoliciesRequest,
) -> dict:
    out: dict = {}
    import capo_fms.types.third_party_firewall

    out["ThirdPartyFirewall"] = (
        capo_fms.types.third_party_firewall.serialize_aws_json_1_1(
            value["third_party_firewall"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["MaxResults"] = value["max_results"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListThirdPartyFirewallFirewallPoliciesRequest:
    out: ListThirdPartyFirewallFirewallPoliciesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ThirdPartyFirewall") is not None:
        import capo_fms.types.third_party_firewall

        out["third_party_firewall"] = (
            capo_fms.types.third_party_firewall.deserialize_aws_json_1_1(
                data["ThirdPartyFirewall"]
            )
        )
    else:
        import typing

        out["third_party_firewall"] = typing.cast(
            "capo_fms.types.third_party_firewall.ThirdPartyFirewall", ""
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 0
    return out
