"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DeleteProxyRulesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.resource_name_list


class DeleteProxyRulesRequest(TypedDict, closed=True):
    proxy_rule_group_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rules: "capo_network_firewall.types.resource_name_list.ResourceNameList"
    """<p>The proxy rule(s) to remove from the existing proxy rule group. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteProxyRulesRequest) -> dict:
    out: dict = {}
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    import capo_network_firewall.types.resource_name_list

    out["Rules"] = (
        capo_network_firewall.types.resource_name_list.serialize_aws_json_1_0(
            value["rules"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteProxyRulesRequest:
    out: DeleteProxyRulesRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyRuleGroupArn") is not None:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    if data.get("ProxyRuleGroupName") is not None:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if data.get("Rules") is not None:
        import capo_network_firewall.types.resource_name_list

        out["rules"] = (
            capo_network_firewall.types.resource_name_list.deserialize_aws_json_1_0(
                data["Rules"]
            )
        )
    else:
        out["rules"] = []
    return out
