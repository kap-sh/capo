"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#CreateRuleSnapshotOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.description
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.is_snapshot
    import capo_network_security_manager.types.json_document
    import capo_network_security_manager.types.rule_arn
    import capo_network_security_manager.types.rule_firewall_type
    import capo_network_security_manager.types.rule_id
    import capo_network_security_manager.types.rule_name
    import capo_network_security_manager.types.rule_type
    import capo_network_security_manager.types.update_token


class CreateRuleSnapshotOutput(TypedDict, closed=True):
    rule_id: "capo_network_security_manager.types.rule_id.RuleId"
    """<p>The service-generated id of the rule.</p>"""
    rule_arn: "capo_network_security_manager.types.rule_arn.RuleArn"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    rule_name: "capo_network_security_manager.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    firewall_type: (
        "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType"
    )
    """<p>The firewall type associated with the resource.</p>"""
    rule_type: NotRequired["capo_network_security_manager.types.rule_type.RuleType"]
    """<p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>"""
    rule_description: NotRequired[
        "capo_network_security_manager.types.description.Description"
    ]
    """<p>A description of the rule.</p>"""
    configuration: "capo_network_security_manager.types.json_document.JsonDocument"
    """<p>The firewall configuration for the rule, as a JSON document. The structure depends on the rule's firewall type and rule type.</p>"""
    status: "capo_network_security_manager.types.entity_status.EntityStatus"
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable) or <code>ACTIVE</code> (published, in use).</p>"""
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
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the snapshot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRuleSnapshotOutput) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    out["ruleArn"] = value["rule_arn"]
    out["ruleName"] = value["rule_name"]
    import capo_network_security_manager.types.rule_firewall_type

    out["firewallType"] = (
        capo_network_security_manager.types.rule_firewall_type.serialize_json(
            value["firewall_type"]
        )
    )
    if "rule_type" in value:
        import capo_network_security_manager.types.rule_type

        out["ruleType"] = capo_network_security_manager.types.rule_type.serialize_json(
            value["rule_type"]
        )
    if "rule_description" in value:
        out["ruleDescription"] = value["rule_description"]
    out["configuration"] = value["configuration"]
    import capo_network_security_manager.types.entity_status

    out["status"] = capo_network_security_manager.types.entity_status.serialize_json(
        value["status"]
    )
    out["version"] = value["version"]
    if "update_token" in value:
        out["updateToken"] = value["update_token"]
    if "is_snapshot" in value:
        out["isSnapshot"] = value["is_snapshot"]
    if "has_published_version" in value:
        out["hasPublishedVersion"] = value["has_published_version"]
    if "updated_at" in value:
        import capo_network_security_manager.types.date_timestamp

        out["updatedAt"] = (
            capo_network_security_manager.types.date_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRuleSnapshotOutput:
    out: CreateRuleSnapshotOutput = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("CreateRuleSnapshotOutput.rule_id required")
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    else:
        raise DeserializationError("CreateRuleSnapshotOutput.rule_arn required")
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("CreateRuleSnapshotOutput.rule_name required")
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.rule_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.rule_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    else:
        raise DeserializationError("CreateRuleSnapshotOutput.firewall_type required")
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
    else:
        raise DeserializationError("CreateRuleSnapshotOutput.configuration required")
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("CreateRuleSnapshotOutput.status required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        raise DeserializationError("CreateRuleSnapshotOutput.version required")
    if data.get("updateToken") is not None:
        out["update_token"] = data["updateToken"]
    if data.get("isSnapshot") is not None:
        out["is_snapshot"] = data["isSnapshot"]
    if data.get("hasPublishedVersion") is not None:
        out["has_published_version"] = data["hasPublishedVersion"]
    if data.get("updatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["updated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
