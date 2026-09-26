"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#RuleSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.rule_arn
    import capo_network_security_manager.types.rule_firewall_type
    import capo_network_security_manager.types.rule_id
    import capo_network_security_manager.types.rule_name
    import capo_network_security_manager.types.rule_type


class RuleSummary(TypedDict, closed=True):
    rule_id: "capo_network_security_manager.types.rule_id.RuleId"
    """<p>The service-generated id of the rule.</p>"""
    rule_arn: "capo_network_security_manager.types.rule_arn.RuleArn"
    """<p>The Amazon Resource Name (ARN) of the rule.</p>"""
    rule_name: "capo_network_security_manager.types.rule_name.RuleName"
    """<p>The name of the rule.</p>"""
    firewall_type: NotRequired[
        "capo_network_security_manager.types.rule_firewall_type.RuleFirewallType"
    ]
    """<p>The firewall type associated with the resource.</p>"""
    rule_type: NotRequired["capo_network_security_manager.types.rule_type.RuleType"]
    """<p>The type of the rule. <code>CONFIGURATION</code> rules contain firewall settings, and <code>INSPECTION</code> rules contain rule groups.</p>"""
    status: NotRequired[
        "capo_network_security_manager.types.entity_status.EntityStatus"
    ]
    """<p>The current status of the resource: <code>DRAFT</code> (unpublished, editable) or <code>ACTIVE</code> (published, in use).</p>"""
    version: NotRequired[
        "capo_network_security_manager.types.entity_version.EntityVersion"
    ]
    """<p>The version of the resource.</p>"""
    has_published_version: NotRequired[
        "capo_network_security_manager.types.has_published_version.HasPublishedVersion"
    ]
    """<p>Specifies whether a published version of the resource exists.</p>"""
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RuleSummary) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    out["ruleArn"] = value["rule_arn"]
    out["ruleName"] = value["rule_name"]
    if "firewall_type" in value:
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
    if "status" in value:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.serialize_json(
                value["status"]
            )
        )
    if "version" in value:
        out["version"] = value["version"]
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


def deserialize_json(data: dict) -> RuleSummary:
    out: RuleSummary = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        raise DeserializationError("RuleSummary.rule_id required")
    if data.get("ruleArn") is not None:
        out["rule_arn"] = data["ruleArn"]
    else:
        raise DeserializationError("RuleSummary.rule_arn required")
    if data.get("ruleName") is not None:
        out["rule_name"] = data["ruleName"]
    else:
        raise DeserializationError("RuleSummary.rule_name required")
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.rule_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.rule_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    if data.get("ruleType") is not None:
        import capo_network_security_manager.types.rule_type

        out["rule_type"] = (
            capo_network_security_manager.types.rule_type.deserialize_json(
                data["ruleType"]
            )
        )
    if data.get("status") is not None:
        import capo_network_security_manager.types.entity_status

        out["status"] = (
            capo_network_security_manager.types.entity_status.deserialize_json(
                data["status"]
            )
        )
    if data.get("version") is not None:
        out["version"] = data["version"]
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
