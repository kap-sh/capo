"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.json_document
    import capo_network_security_manager.types.rule_firewall_type
    import capo_network_security_manager.types.rule_name
    import capo_network_security_manager.types.rule_type
    import capo_network_security_manager.types.tag_map


class CreateRuleInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""
    rule_name: "capo_network_security_manager.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    firewall_type: (
        "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType"
    )
    """<p>The firewall type associated with the resource.</p>"""
    rule_type: "capo_network_security_manager.types.rule_type.RuleType"
    """<p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>"""
    rule_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the rule.</p>"""
    configuration: "capo_network_security_manager.types.json_document.JsonDocument"
    r"""<p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>"""
    tags: NotRequired["capo_network_security_manager.types.tag_map.TagMap"]
    """<p>The tags to add to the resource when it is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["ruleName"] = value["rule_name"]
    import capo_network_security_manager.types.rule_firewall_type

    out["firewallType"] = (
        capo_network_security_manager.types.rule_firewall_type.serialize_json(
            value["firewall_type"]
        )
    )
    import capo_network_security_manager.types.rule_type

    out["ruleType"] = capo_network_security_manager.types.rule_type.serialize_json(
        value["rule_type"]
    )
    if "rule_description" in value:
        out["ruleDescription"] = value["rule_description"]
    out["configuration"] = value["configuration"]
    out["isPublished"] = value.get("is_published", True)
    if "tags" in value:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateRuleInput:
    out: CreateRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("CreateRuleInput.rule_name required")
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.rule_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.rule_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    else:
        raise DeserializationError("CreateRuleInput.firewall_type required")
    if data.get("ruleType") is not None:
        import capo_network_security_manager.types.rule_type

        out["rule_type"] = (
            capo_network_security_manager.types.rule_type.deserialize_json(
                data["ruleType"]
            )
        )
    else:
        raise DeserializationError("CreateRuleInput.rule_type required")
    if data.get("ruleDescription") is not None:
        out["rule_description"] = data["ruleDescription"]
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    else:
        raise DeserializationError("CreateRuleInput.configuration required")
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        out["is_published"] = True
    if data.get("tags") is not None:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
