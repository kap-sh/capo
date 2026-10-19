"""Generated from Smithy shape ``com.amazonaws.networkfirewall#CreateProxyConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.description
    import capo_network_firewall.types.proxy_config_default_rule_phase_actions_request
    import capo_network_firewall.types.resource_arn_list
    import capo_network_firewall.types.resource_name
    import capo_network_firewall.types.resource_name_list
    import capo_network_firewall.types.tag_list


class CreateProxyConfigurationRequest(TypedDict, closed=True):
    proxy_configuration_name: "capo_network_firewall.types.resource_name.ResourceName"
    """<p>The descriptive name of the proxy configuration. You can't change the name of a proxy configuration after you create it.</p>"""
    description: NotRequired["capo_network_firewall.types.description.Description"]
    """<p>A description of the proxy configuration. </p>"""
    rule_group_names: NotRequired[
        "capo_network_firewall.types.resource_name_list.ResourceNameList"
    ]
    """<p>The proxy rule group name(s) to attach to the proxy configuration.</p> <p>You must specify the ARNs or the names, and you can specify both. </p>"""
    rule_group_arns: NotRequired[
        "capo_network_firewall.types.resource_arn_list.ResourceArnList"
    ]
    """<p>The proxy rule group arn(s) to attach to the proxy configuration.</p> <p>You must specify the ARNs or the names, and you can specify both. </p>"""
    default_rule_phase_actions: "capo_network_firewall.types.proxy_config_default_rule_phase_actions_request.ProxyConfigDefaultRulePhaseActionsRequest"
    """<p>Evaluation points in the traffic flow where rules are applied. There are three phases in a traffic where the rule match is applied. </p>"""
    tags: NotRequired["capo_network_firewall.types.tag_list.TagList"]
    """<p>The key:value pairs to associate with the resource.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateProxyConfigurationRequest) -> dict:
    out: dict = {}
    out["ProxyConfigurationName"] = value["proxy_configuration_name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "rule_group_names" in value:
        import capo_network_firewall.types.resource_name_list

        out["RuleGroupNames"] = (
            capo_network_firewall.types.resource_name_list.serialize_aws_json_1_0(
                value["rule_group_names"]
            )
        )
    if "rule_group_arns" in value:
        import capo_network_firewall.types.resource_arn_list

        out["RuleGroupArns"] = (
            capo_network_firewall.types.resource_arn_list.serialize_aws_json_1_0(
                value["rule_group_arns"]
            )
        )
    import capo_network_firewall.types.proxy_config_default_rule_phase_actions_request

    out["DefaultRulePhaseActions"] = (
        capo_network_firewall.types.proxy_config_default_rule_phase_actions_request.serialize_aws_json_1_0(
            value["default_rule_phase_actions"]
        )
    )
    if "tags" in value:
        import capo_network_firewall.types.tag_list

        out["Tags"] = capo_network_firewall.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateProxyConfigurationRequest:
    out: CreateProxyConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ProxyConfigurationName") is not None:
        out["proxy_configuration_name"] = data["ProxyConfigurationName"]
    else:
        out["proxy_configuration_name"] = ""
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("RuleGroupNames") is not None:
        import capo_network_firewall.types.resource_name_list

        out["rule_group_names"] = (
            capo_network_firewall.types.resource_name_list.deserialize_aws_json_1_0(
                data["RuleGroupNames"]
            )
        )
    if data.get("RuleGroupArns") is not None:
        import capo_network_firewall.types.resource_arn_list

        out["rule_group_arns"] = (
            capo_network_firewall.types.resource_arn_list.deserialize_aws_json_1_0(
                data["RuleGroupArns"]
            )
        )
    if data.get("DefaultRulePhaseActions") is not None:
        import capo_network_firewall.types.proxy_config_default_rule_phase_actions_request

        out["default_rule_phase_actions"] = (
            capo_network_firewall.types.proxy_config_default_rule_phase_actions_request.deserialize_aws_json_1_0(
                data["DefaultRulePhaseActions"]
            )
        )
    else:
        raise DeserializationError(
            "CreateProxyConfigurationRequest.default_rule_phase_actions required"
        )
    if data.get("Tags") is not None:
        import capo_network_firewall.types.tag_list

        out["tags"] = capo_network_firewall.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
