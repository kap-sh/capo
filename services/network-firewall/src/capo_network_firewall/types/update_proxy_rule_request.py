"""Generated from Smithy shape ``com.amazonaws.networkfirewall#UpdateProxyRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.proxy_rule_condition_list
    import capo_network_firewall.types.proxy_rule_phase_action
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.update_token


class UpdateProxyRuleRequest(TypedDict, closed=True):
    proxy_rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_group_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the proxy rule. </p>"""
    action: NotRequired[
        "capo_network_firewall.types.proxy_rule_phase_action.ProxyRulePhaseAction"
    ]
    """<p>Depending on the match action, the proxy either stops the evaluation (if the action is terminal - allow or deny), or continues it (if the action is alert) until it matches a rule with a terminal action. </p>"""
    add_conditions: NotRequired[
        "capo_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
    ]
    """<p>Proxy rule conditions to add. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>"""
    remove_conditions: NotRequired[
        "capo_network_firewall.types.proxy_rule_condition_list.ProxyRuleConditionList"
    ]
    """<p>Proxy rule conditions to remove. Match criteria that specify what traffic attributes to examine. Conditions include operators (StringEquals, StringLike) and values to match against. </p>"""
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy rule. The token marks the state of the proxy rule resource at the time of the request. </p> <p>To make changes to the proxy rule, you provide the token in your request. Network Firewall uses the token to ensure that the proxy rule hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy rule again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateProxyRuleRequest) -> dict:
    out: dict = {}
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    out["ProxyRuleName"] = value["proxy_rule_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "action" in value:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["Action"] = (
            capo_network_firewall.types.proxy_rule_phase_action.serialize_aws_json_1_0(
                value["action"]
            )
        )
    if "add_conditions" in value:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["AddConditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.serialize_aws_json_1_0(
                value["add_conditions"]
            )
        )
    if "remove_conditions" in value:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["RemoveConditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.serialize_aws_json_1_0(
                value["remove_conditions"]
            )
        )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateProxyRuleRequest:
    out: UpdateProxyRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyRuleGroupName") is not None:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if data.get("ProxyRuleGroupArn") is not None:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if data.get("ProxyRuleName") is not None:
        out["proxy_rule_name"] = data["ProxyRuleName"]
    else:
        out["proxy_rule_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Action") is not None:
        import capo_network_firewall.types.proxy_rule_phase_action

        out["action"] = (
            capo_network_firewall.types.proxy_rule_phase_action.deserialize_aws_json_1_0(
                data["Action"]
            )
        )
    if data.get("AddConditions") is not None:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["add_conditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.deserialize_aws_json_1_0(
                data["AddConditions"]
            )
        )
    if data.get("RemoveConditions") is not None:
        import capo_network_firewall.types.proxy_rule_condition_list

        out["remove_conditions"] = (
            capo_network_firewall.types.proxy_rule_condition_list.deserialize_aws_json_1_0(
                data["RemoveConditions"]
            )
        )
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    return out
