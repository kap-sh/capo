"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRulePrioritiesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule_priority_list
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.rule_group_request_phase
    import capo_network_firewall.types.update_token


class UpdateProxyRulePrioritiesRequest(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_group_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_group_request_phase: (
        "capo_network_firewall.types.rule_group_request_phase.RuleGroupRequestPhase"
    )
    """<p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p>"""
    rules: "capo_network_firewall.types.proxy_rule_priority_list.ProxyRulePriorityList"
    """<p>proxy rule resources to update to new positions. </p>"""
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule group. The token marks the state of the proxy rule group resource at the time of the request. </p> <p>To make changes to the proxy rule group, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule group hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule group again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRulePrioritiesRequest) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    import capo_network_firewall.types.rule_group_request_phase

    out["RuleGroupRequestPhase"] = (
        capo_network_firewall.types.rule_group_request_phase.serialize_aws_json_1_0(
            value["rule_group_request_phase"]
        )
    )
    import capo_network_firewall.types.proxy_rule_priority_list

    out["Rules"] = (
        capo_network_firewall.types.proxy_rule_priority_list.serialize_aws_json_1_0(
            value["rules"]
        )
    )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRulePrioritiesRequest:
    out: UpdateProxyRulePrioritiesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyRuleGroupName") is not None:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if data.get("ProxyRuleGroupArn") is not None:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if data.get("RuleGroupRequestPhase") is not None:
        import capo_network_firewall.types.rule_group_request_phase

        out["rule_group_request_phase"] = (
            capo_network_firewall.types.rule_group_request_phase.deserialize_aws_json_1_0(
                data["RuleGroupRequestPhase"]
            )
        )
    else:
        import typing

        out["rule_group_request_phase"] = typing.cast(
            "capo_network_firewall.types.rule_group_request_phase.RuleGroupRequestPhase",
            "",
        )
    if data.get("Rules") is not None:
        import capo_network_firewall.types.proxy_rule_priority_list

        out["rules"] = (
            capo_network_firewall.types.proxy_rule_priority_list.deserialize_aws_json_1_0(
                data["Rules"]
            )
        )
    else:
        out["rules"] = []
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    return out
