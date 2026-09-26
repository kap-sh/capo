"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#PolicySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.date_timestamp
    import capo_network_security_manager.types.entity_status
    import capo_network_security_manager.types.entity_version
    import capo_network_security_manager.types.has_published_version
    import capo_network_security_manager.types.policy_arn
    import capo_network_security_manager.types.policy_firewall_type
    import capo_network_security_manager.types.policy_id
    import capo_network_security_manager.types.policy_name
    import capo_network_security_manager.types.priority


class PolicySummary(TypedDict, closed=True):
    policy_id: "capo_network_security_manager.types.policy_id.PolicyId"
    """<p>The service-generated id of the policy.</p>"""
    policy_arn: "capo_network_security_manager.types.policy_arn.PolicyArn"
    """<p>The Amazon Resource Name (ARN) of the policy.</p>"""
    policy_name: NotRequired[
        "capo_network_security_manager.types.policy_name.PolicyName"
    ]
    """<p>The name of the policy.</p>"""
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
    firewall_type: NotRequired[
        "capo_network_security_manager.types.policy_firewall_type.PolicyFirewallType"
    ]
    """<p>The firewall type associated with the resource.</p>"""
    priority: NotRequired["capo_network_security_manager.types.priority.Priority"]
    """<p>The priority of the resource. A lower number indicates a higher priority.</p>"""
    updated_at: NotRequired[
        "capo_network_security_manager.types.date_timestamp.DateTimestamp"
    ]
    """<p>The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolicySummary) -> dict:
    out: dict = {}
    out["policyId"] = value["policy_id"]
    out["policyArn"] = value["policy_arn"]
    if "policy_name" in value:
        out["policyName"] = value["policy_name"]
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
    if "firewall_type" in value:
        import capo_network_security_manager.types.policy_firewall_type

        out["firewallType"] = (
            capo_network_security_manager.types.policy_firewall_type.serialize_json(
                value["firewall_type"]
            )
        )
    if "priority" in value:
        out["priority"] = value["priority"]
    if "updated_at" in value:
        import capo_network_security_manager.types.date_timestamp

        out["updatedAt"] = (
            capo_network_security_manager.types.date_timestamp.serialize_json(
                value["updated_at"]
            )
        )
    return out


def deserialize_json(data: dict) -> PolicySummary:
    out: PolicySummary = {}  # type: ignore[typeddict-item]
    if data.get("policyId") is not None:
        out["policy_id"] = data["policyId"]
    else:
        raise DeserializationError("PolicySummary.policy_id required")
    if data.get("policyArn") is not None:
        out["policy_arn"] = data["policyArn"]
    else:
        raise DeserializationError("PolicySummary.policy_arn required")
    if data.get("policyName") is not None:
        out["policy_name"] = data["policyName"]
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
    if data.get("firewallType") is not None:
        import capo_network_security_manager.types.policy_firewall_type

        out["firewall_type"] = (
            capo_network_security_manager.types.policy_firewall_type.deserialize_json(
                data["firewallType"]
            )
        )
    if data.get("priority") is not None:
        out["priority"] = data["priority"]
    if data.get("updatedAt") is not None:
        import capo_network_security_manager.types.date_timestamp

        out["updated_at"] = (
            capo_network_security_manager.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    return out
