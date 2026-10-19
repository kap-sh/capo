"""Generated from Smithy shape ``com.amazonaws.networkfirewall#DescribeProxyRuleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name


class DescribeProxyRuleRequest(TypedDict, closed=True):
    proxy_rule_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the proxy rule. You can't change the name of a proxy rule after you create it.</p>"""
    proxy_rule_group_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy rule group. You can't change the name of a proxy rule group after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_rule_group_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy rule group.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeProxyRuleRequest) -> dict:
    out: dict = {}
    out["ProxyRuleName"] = value["proxy_rule_name"]
    if "proxy_rule_group_name" in value:
        out["ProxyRuleGroupName"] = value["proxy_rule_group_name"]
    if "proxy_rule_group_arn" in value:
        out["ProxyRuleGroupArn"] = value["proxy_rule_group_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeProxyRuleRequest:
    out: DescribeProxyRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyRuleName") is not None:
        out["proxy_rule_name"] = data["ProxyRuleName"]
    else:
        out["proxy_rule_name"] = ""
    if data.get("ProxyRuleGroupName") is not None:
        out["proxy_rule_group_name"] = data["ProxyRuleGroupName"]
    if data.get("ProxyRuleGroupArn") is not None:
        out["proxy_rule_group_arn"] = data["ProxyRuleGroupArn"]
    return out
