"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#UpdateRuleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.json_document
    import capo_network_security_manager.types.rule_identifier
    import capo_network_security_manager.types.rule_type
    import capo_network_security_manager.types.update_token


class UpdateRuleInput(TypedDict, closed=True):
    rule_identifier: (
        "capo_network_security_manager.types.rule_identifier.RuleIdentifier"
    )
    """<p>The identifier of the rule. This is the rule's Amazon Resource Name (ARN).</p>"""
    update_token: "capo_network_security_manager.types.update_token.UpdateToken"
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    rule_type: NotRequired["capo_network_security_manager.types.rule_type.RuleType"]
    """<p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>"""
    rule_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the rule.</p>"""
    configuration: NotRequired[
        "capo_network_security_manager.types.json_document.JsonDocument"
    ]
    r"""<p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type. For an AWS WAF <code>INSPECTION</code> rule, provide an AWS WAF rule group. For an AWS WAF <code>CONFIGURATION</code> rule, provide a single web ACL setting, such as <code>DefaultAction</code> or <code>VisibilityConfig</code>; use <code>wafConfigDataType</code> to declare which setting the document contains. For the schema of each setting and complete examples, see <a href=\"https://docs.aws.amazon.com/network-security-manager/latest/devguide/what-is.html\">Writing rule configurations</a> in the <i>AWS Network Security Manager Developer Guide</i>.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>"""
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRuleInput) -> dict:
    out: dict = {}
    out["updateToken"] = value["update_token"]
    if "rule_type" in value:
        import capo_network_security_manager.types.rule_type

        out["ruleType"] = capo_network_security_manager.types.rule_type.serialize_json(
            value["rule_type"]
        )
    if "rule_description" in value:
        out["ruleDescription"] = value["rule_description"]
    if "configuration" in value:
        out["configuration"] = value["configuration"]
    out["isPublished"] = value["is_published"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdateRuleInput:
    out: UpdateRuleInput = {}  # type: ignore[typeddict-item]
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    else:
        raise DeserializationError("UpdateRuleInput.update_token required")
    if data.get("ruleType") is not None:
        import capo_network_security_manager.types.rule_type

        out["rule_type"] = (
            capo_network_security_manager.types.rule_type.deserialize_json(
                data["ruleType"]
            )
        )
    if data.get("ruleDescription") is not None:
        out["rule_description"] = data["ruleDescription"]
    if data.get("configuration") is not None:
        out["configuration"] = data["configuration"]
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        raise DeserializationError("UpdateRuleInput.is_published required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
