"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#UpdatePolicyOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.associated_template_and_rule_list
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.is_snapshot
    import capo_network_security_manager.types.policy_arn
    import capo_network_security_manager.types.policy_configuration
    import capo_network_security_manager.types.policy_firewall_type
    import capo_network_security_manager.types.policy_id
    import capo_network_security_manager.types.policy_name
    import capo_network_security_manager.types.priority
    import capo_network_security_manager.types.update_token


class UpdatePolicyOutput(TypedDict, closed=True):
    policy_id: "capo_network_security_manager.types.policy_id.PolicyId"
    """<p>The service-generated id of the policy.</p>"""
    policy_arn: "capo_network_security_manager.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    policy_name: "capo_network_security_manager.types.policy_name.PolicyName"
    """<p>The name of the policy.</p>"""
    policy_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the policy.</p>"""
    status: "capo_network_security_manager.types.entity_status.EntityStatus"
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable) or <code>ACTIVE</code> (published, in use).</p>"""
    priority: "capo_network_security_manager.types.priority.Priority"
    """<p>The priority of the resource. A lower number indicates a higher priority.</p>"""
    associated_template_and_rule_list: "capo_network_security_manager.types.associated_template_and_rule_list.AssociatedTemplateAndRuleList"
    """<p>The templates and rules associated with the policy. For AWS WAF policies, this list contains 1 to 100 templates or rules, of which at most 2 can be templates. For AWS Shield Advanced policies, this list is empty.</p>"""
    version: "capo_network_security_manager.types.entity_version.EntityVersion"
    """<p>The version of the resource.</p>"""
    update_token: NotRequired[
        "capo_network_security_manager.types.update_token.UpdateToken"
    ]
    """<p>A token used for optimistic concurrency control. Each read and write returns an <code>updateToken</code>. Provide the most recent value on your next update to detect and prevent conflicting concurrent modifications.</p>"""
    is_snapshot: NotRequired[
        "capo_network_security_manager.types.is_snapshot.IsSnapshot"
    ]
    """<p>Specifies whether the resource is a snapshot of a published version.</p>"""
    has_published_version: NotRequired[
        "capo_network_security_manager.types.has_published_version.HasPublishedVersion"
    ]
    """<p>Specifies whether a published version of the resource exists.</p>"""
    firewall_type: (
        "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType"
    )
    """<p>The firewall type associated with the resource.</p>"""
    policy_configuration: NotRequired[
        "capo_network_security_manager.types.policy_configuration.PolicyConfiguration"
    ]
    """<p>The configuration settings that control the policy's behavior, including remediation and firewall-type-specific settings.</p>"""
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the resource was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePolicyOutput) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    out["policyArn"] = value["policy_arn"]
    out["policyName"] = value["policy_name"]
    if "policy_description" in value:
        out["policyDescription"] = value["policy_description"]
    import capo_network_security_manager.types.entity_status

    out["status"] = capo_network_security_manager.types.entity_status.serialize_json(
        value["status"]
    )
    out["priority"] = value["priority"]
    import capo_network_security_manager.types.associated_template_and_rule_list

    out["associatedTemplateAndRuleList"] = (
        capo_network_security_manager.types.associated_template_and_rule_list.serialize_json(
            value["associated_template_and_rule_list"]
        )
    )
    out["version"] = value["version"]
    if "update_token" in value:
        out["updateToken"] = value["update_token"]
    if "is_snapshot" in value:
        out["isSnapshot"] = value["is_snapshot"]
    if "has_published_version" in value:
        out["hasPublishedVersion"] = value["has_published_version"]
    import capo_network_security_manager.types.policy_firewall_type

    out["firewallType"] = (
        capo_network_security_manager.types.policy_firewall_type.serialize_json(
            value["firewall_type"]
        )
    )
    if "policy_configuration" in value:
        import capo_network_security_manager.types.policy_configuration

        out["policyConfiguration"] = (
            capo_network_security_manager.types.policy_configuration.serialize_json(
                value["policy_configuration"]
            )
        )
    if "updated_at" in value:
        import capo_network_security_manager.types.date_timestamp

        out["updatedAt"] = (
            capo_network_security_manager.types.date_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePolicyOutput:
    out: UpdatePolicyOutput = {}  # type: ignore[typeddict-item]
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("UpdatePolicyOutput.policy_id required")
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("UpdatePolicyOutput.policy_arn required")
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
    else:
        raise DeserializationError("UpdatePolicyOutput.policy_name required")
    if data.get("policyDescription") is not None:
        out["policy_description"] = data["policyDescription"]
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyOutput.status required")
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    else:
        raise DeserializationError("UpdatePolicyOutput.priority required")
    if data.get("associatedTemplateAndRuleList") is not None:
        import capo_network_security_manager.types.associated_template_and_rule_list

        out["associated_template_and_rule_list"] = (
            capo_network_security_manager.types.associated_template_and_rule_list.deserialize_json(
                data["associatedTemplateAndRuleList"]
            )
        )
    else:
        raise DeserializationError(
            "UpdatePolicyOutput.associated_template_and_rule_list required"
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("UpdatePolicyOutput.version required")
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    if data.get("isSnapshot") is not None:
        out["is_snapshot"] = data["isSnapshot"]
    if data.get("hasPublishedVersion") is not None:
        out["has_published_version"] = data["hasPublishedVersion"]
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.policy_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.policy_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    else:
        raise DeserializationError("UpdatePolicyOutput.firewall_type required")
    if data.get("policyConfiguration") is not None:
        import capo_network_security_manager.types.policy_configuration

        out["policy_configuration"] = (
            capo_network_security_manager.types.policy_configuration.deserialize_json(
                data["policyConfiguration"]
            )
        )
    if data.get("updatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["updated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
