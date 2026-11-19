"""Generated from Smithy shape ``com.amazonaws.networkfirewall#ListRuleGroupsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.pagination_token
    import capo_network_firewall.types.rule_groups


class ListRuleGroupsResponse(TypedDict, closed=True):
    next_token: NotRequired[
        "capo_network_firewall.types.pagination_token.PaginationToken"
    ]
    """<p>When you request a list of objects with a <code>MaxResults</code> setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Network Firewall returns a <code>NextToken</code> value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.</p>"""
    rule_groups: NotRequired["capo_network_firewall.types.rule_groups.RuleGroups"]
    """<p>The rule group metadata objects that you've defined. Depending on your setting for max results and the number of rule groups, this might not be the full list. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "rule_groups" in value:
        import capo_network_firewall.types.rule_groups

        out["RuleGroups"] = (
            capo_network_firewall.types.rule_groups.serialize_aws_json_1_0(
                value["rule_groups"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListRuleGroupsResponse:
    out: ListRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RuleGroups") is not None:
        import capo_network_firewall.types.rule_groups

        out["rule_groups"] = (
            capo_network_firewall.types.rule_groups.deserialize_aws_json_1_0(
                data["RuleGroups"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ListRuleGroupsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "rule_groups" in value:
        import capo_network_firewall.types.rule_groups

        out["RuleGroups"] = capo_network_firewall.types.rule_groups.serialize_cbor(
            value["rule_groups"]
        )
    return out


def deserialize_cbor(data: dict) -> ListRuleGroupsResponse:
    out: ListRuleGroupsResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("RuleGroups") is not None:
        import capo_network_firewall.types.rule_groups

        out["rule_groups"] = capo_network_firewall.types.rule_groups.deserialize_cbor(
            data["RuleGroups"]
        )
    return out
