"""Generated from Smithy shape ``com.amazonaws.networkfirewall#AttachRuleGroupsToProxyConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.proxy_rule_group_attachment_list
    import capo_network_firewall.types.resource_arn
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.update_token


class AttachRuleGroupsToProxyConfigurationRequest(TypedDict, closed=True):
    proxy_configuration_name: NotRequired[
        "capo_network_firewall.types.resource_name.ResourceName"
    ]
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    proxy_configuration_arn: NotRequired[
        "capo_network_firewall.types.resource_arn.ResourceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of a proxy configuration.</p> <p>You must specify the ARN or the name, and you can specify both. </p>"""
    rule_groups: "capo_network_firewall.types.proxy_rule_group_attachment_list.ProxyRuleGroupAttachmentList"
    """<p>The proxy rule group(s) to attach to the proxy configuration</p>"""
    update_token: "capo_network_firewall.types.update_token.UpdateToken"
    """<p>A token used for optimistic locking. Network Firewall returns a token to your requests that access the proxy configuration. The token marks the state of the proxy configuration resource at the time of the request. </p> <p>To make changes to the proxy configuration, you provide the token in your request. Network Firewall uses the token to ensure that the proxy configuration hasn't changed since you last retrieved it. If it has changed, the operation fails with an <code>InvalidTokenException</code>. If this happens, retrieve the proxy configuration again to get a current copy of it with a current token. Reapply your changes as needed, then try the operation again using the new token. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachRuleGroupsToProxyConfigurationRequest) -> dict:
    out: dict = {}
    if "proxy_configuration_name" in value:
        out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "proxy_configuration_arn" in value:
        out["ProxyConfigurationArn"] = value["proxy_configuration_arn"]
    import capo_network_firewall.types.proxy_rule_group_attachment_list

    out["RuleGroups"] = (
        capo_network_firewall.types.proxy_rule_group_attachment_list.serialize_aws_json_1_0(
            value["rule_groups"]
        )
    )
    out["UpdateToken"] = value["update_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AttachRuleGroupsToProxyConfigurationRequest:
    out: AttachRuleGroupsToProxyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyConfigurationName") is not None:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    if data.get("ProxyConfigurationArn") is not None:
        out["proxy_configuration_arn"] = data["ProxyConfigurationArn"]
    if data.get("RuleGroups") is not None:
        import capo_network_firewall.types.proxy_rule_group_attachment_list

        out["rule_groups"] = (
            capo_network_firewall.types.proxy_rule_group_attachment_list.deserialize_aws_json_1_0(
                data["RuleGroups"]
            )
        )
    else:
        out["rule_groups"] = []
    if data.get("UpdateToken") is not None:
        out["update_token"] = data["UpdateToken"]
    else:
        out["update_token"] = ""
    return out
