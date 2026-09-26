"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreatePolicyInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.idempotency_token
    import capo_network_security_manager.types.is_published
    import capo_network_security_manager.types.policy_configuration
    import capo_network_security_manager.types.policy_firewall_type
    import capo_network_security_manager.types.policy_name
    import capo_network_security_manager.types.priority
    import capo_network_security_manager.types.tag_map
    import capo_network_security_manager.types.template_and_rule_reference_list


class CreatePolicyInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_network_security_manager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive token that you provide to ensure that the operation completes no more than one time. If you retry a request with the same client token and the same parameters, the service returns the result of the original successful request.</p>"""
    policy_name: "capo_network_security_manager.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    policy_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the policy.</p>"""
    priority: "capo_network_security_manager.types.priority.Priority"
    """<p>The priority of the resource. A lower number indicates a higher priority.</p>"""
    associated_template_and_rule_list: NotRequired[
        "capo_network_security_manager.types.template_and_rule_reference_list.TemplateAndRuleReferenceList"
    ]
    """<p>The templates and rules to associate with the policy. For AWS WAF policies, specify 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list must be empty.</p>"""
    firewall_type: (
        "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType"
    )
    """<p>The firewall type associated with the resource.</p>"""
    policy_configuration: (
        "capo_network_security_manager.types.policy_configuration.PolicyConfiguration"
    )
    """<p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>"""
    is_published: "capo_network_security_manager.types.is_published.IsPublished"
    """<p>Specifies whether to publish the resource. When <code>true</code>, the resource is saved in published (<code>ACTIVE</code>) state. When <code>false</code>, it is saved as a draft (<code>DRAFT</code>). Default: <code>true</code>.</p>"""
    tags: NotRequired["capo_network_security_manager.types.tag_map.TagMap"]
    """<p>The tags to add to the resource when it is created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreatePolicyInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["policyName"] = value["policy_name"]
    if "policy_description" in value:
        out["policyDescription"] = value["policy_description"]
    out["priority"] = value["priority"]
    if "associated_template_and_rule_list" in value:
        import capo_network_security_manager.types.template_and_rule_reference_list

        out["associatedTemplateAndRuleList"] = (
            capo_network_security_manager.types.template_and_rule_reference_list.serialize_json(
                value["associated_template_and_rule_list"]
            )
        )
    import capo_network_security_manager.types.policy_firewall_type

    out["firewallType"] = (
        capo_network_security_manager.types.policy_firewall_type.serialize_json(
            value["firewall_type"]
        )
    )
    import capo_network_security_manager.types.policy_configuration

    out["policyConfiguration"] = (
        capo_network_security_manager.types.policy_configuration.serialize_json(
            value["policy_configuration"]
        )
    )
    out["isPublished"] = value.get("is_published", True)
    if "tags" in value:
        import capo_network_security_manager.types.tag_map

        out["tags"] = capo_network_security_manager.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreatePolicyInput:
    out: CreatePolicyInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    else:
        raise DeserializationError("CreatePolicyInput.policy_name required")
    if data.get("policyDescription") is not None:
        out["policy_description"] = data["policyDescription"]
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("CreatePolicyInput.priority required")
    if data.get("associatedTemplateAndRuleList") is not None:
        import capo_network_security_manager.types.template_and_rule_reference_list

        out["associated_template_and_rule_list"] = (
            capo_network_security_manager.types.template_and_rule_reference_list.deserialize_json(
                data["associatedTemplateAndRuleList"]
            )
        )
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.policy_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.policy_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyInput.firewall_type required")
    if data.get("policyConfiguration") is not None:
        import capo_network_security_manager.types.policy_configuration

        out["policy_configuration"] = (
            capo_network_security_manager.types.policy_configuration.deserialize_json(
                data["policyConfiguration"]
            )
        )
    else:
        raise DeserializationError("CreatePolicyInput.policy_configuration required")
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
