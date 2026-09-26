"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#UpdatePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.policy_configuration
    import capo_network_security_manager.types.policy_identifier
    import capo_network_security_manager.types.priority
    import capo_network_security_manager.types.template_and_rule_reference_list
    import capo_network_security_manager.types.update_token


class UpdatePolicyInput(TypedDict, closed=True):
    policy_identifier: (
        "capo_network_security_manager.types.policy_identifier.PolicyIdentifier"
    )
    """<p>The identifier of the policy. This is the policy's Amazon Resource Name (ARN).</p>"""
    update_token: "capo_network_security_manager.types.update_token.UpdateToken"
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    policy_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the policy.</p>"""
    priority: NotRequired["capo_network_security_manager.types.priority.Priority"]
    """<p>The priority of the resource. A lower number indicates a higher priority.</p>"""
    associated_template_and_rule_list: NotRequired[
        "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
    ]
    """<p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>"""
    policy_configuration: NotRequired[
        "capo_network_security_manager.types.policy_configuration.PolicyConfiguration"
    ]
    """<p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>).</p>"""
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyInput) -> dict:
    out: dict = {}
    out["updateToken"] = value["update_token"]
    if "policy_description" in value:
        out["policyDescription"] = value["policy_description"]
    if "priority" in value:
        out["priority"] = value["priority"]
    if "associated_template_and_rule_list" in value:
        import capo_network_security_manager.types.template_and_rule_reference_list

        out["associatedTemplateAndRuleList"] = (
            capo_network_security_manager.types.template_and_rule_reference_list.serialize_json(
                value["associated_template_and_rule_list"]
            )
        )
    if "policy_configuration" in value:
        import capo_network_security_manager.types.policy_configuration

        out["policyConfiguration"] = (
            capo_network_security_manager.types.policy_configuration.serialize_json(
                value["policy_configuration"]
            )
        )
    out["isPublished"] = value["is_published"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> UpdatePolicyInput:
    out: UpdatePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    else:
        raise DeserializationError("UpdatePolicyInput.update_token required")
    if data.get("policyDescription") is not None:
        out["policy_description"] = data["policyDescription"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("associatedTemplateAndRuleList") is not None:
        import capo_network_security_manager.types.template_and_rule_reference_list

        out["associated_template_and_rule_list"] = (
            capo_network_security_manager.types.template_and_rule_reference_list.deserialize_json(
                data["associatedTemplateAndRuleList"]
            )
        )
    if data.get("policyConfiguration") is not None:
        import capo_network_security_manager.types.policy_configuration

        out["policy_configuration"] = (
            capo_network_security_manager.types.policy_configuration.deserialize_json(
                data["policyConfiguration"]
            )
        )
    if data.get("isPublished") is not None:
        out["is_published"] = data["isPublished"]
    else:
        raise DeserializationError("UpdatePolicyInput.is_published required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
