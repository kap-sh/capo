"""Generated from Smithy shape ``com.amazonaws.agentregistry#RegistryRecordSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry.types.date_timestamp
    import capo_agent_registry.types.description
    import capo_agent_registry.types.descriptors
    import capo_agent_registry.types.record_type
    import capo_agent_registry.types.registry_arn
    import capo_agent_registry.types.registry_record_arn
    import capo_agent_registry.types.registry_record_display_name
    import capo_agent_registry.types.registry_record_id
    import capo_agent_registry.types.registry_record_name
    import capo_agent_registry.types.registry_record_status
    import capo_agent_registry.types.registry_record_version


class RegistryRecordSummary(TypedDict, closed=True):
    registry_arn: "capo_agent_registry.types.registry_arn.RegistryArn"
    """<p> The Amazon Resource Name (ARN) of the parent registry that owns the record.</p>"""
    record_arn: "capo_agent_registry.types.registry_record_arn.RegistryRecordArn"
    """<p> The Amazon Resource Name (ARN) of the registry record.</p>"""
    record_id: "capo_agent_registry.types.registry_record_id.RegistryRecordId"
    """<p> The unique identifier of the registry record.</p>"""
    name: "capo_agent_registry.types.registry_record_name.RegistryRecordName"
    """<p> The name of the registry record. Names are unique within a registry.</p>"""
    description: NotRequired["capo_agent_registry.types.description.Description"]
    """<p> A human-readable description of the registry record. Use this field to explain the record's purpose or content to consumers discovering it in the registry.</p>"""
    display_name: NotRequired[
        "capo_agent_registry.types.registry_record_display_name.RegistryRecordDisplayName"
    ]
    """<p> The human-readable display name of the registry record.</p>"""
    record_type: "capo_agent_registry.types.record_type.RecordType"
    """<p> The type of the registry record. <code>MCP</code> is a Model Context Protocol server record, <code>AGENT</code> is an Agent-to-Agent (A2A) agent card record, <code>SKILL</code> is an agent skills definition record, and <code>CUSTOM</code> is a record with a custom descriptor.</p>"""
    descriptors: "capo_agent_registry.types.descriptors.Descriptors"
    """<p> The protocol-specific descriptors that describe how to connect to and use the record.</p>"""
    record_version: (
        "capo_agent_registry.types.registry_record_version.RegistryRecordVersion"
    )
    """<p> The version identifier of the registry record.</p>"""
    status: "capo_agent_registry.types.registry_record_status.RegistryRecordStatus"
    """<p> The lifecycle status of the registry record. A record is <code>DRAFT</code> before it is submitted, <code>PENDING_APPROVAL</code> while awaiting curator review, and <code>APPROVED</code> once it is approved and discoverable. <code>REJECTED</code> and <code>DEPRECATED</code> records are not discoverable. The <code>CREATING</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, and <code>UPDATE_FAILED</code> values reflect the state of an in-progress or failed asynchronous change.</p>"""
    created_at: "capo_agent_registry.types.date_timestamp.DateTimestamp"
    """<p> The timestamp when the registry record was created.</p>"""
    updated_at: "capo_agent_registry.types.date_timestamp.DateTimestamp"
    """<p> The timestamp when the registry record was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordSummary) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    out["recordArn"] = value["record_arn"]
    out["recordId"] = value["record_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    import capo_agent_registry.types.record_type

    out["recordType"] = capo_agent_registry.types.record_type.serialize_json(
        value["record_type"]
    )
    import capo_agent_registry.types.descriptors

    out["descriptors"] = capo_agent_registry.types.descriptors.serialize_json(
        value["descriptors"]
    )
    out["recordVersion"] = value["record_version"]
    import capo_agent_registry.types.registry_record_status

    out["status"] = capo_agent_registry.types.registry_record_status.serialize_json(
        value["status"]
    )
    import capo_agent_registry.types.date_timestamp

    out["createdAt"] = capo_agent_registry.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_agent_registry.types.date_timestamp

    out["updatedAt"] = capo_agent_registry.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> RegistryRecordSummary:
    out: RegistryRecordSummary = {}  # type: ignore[typeddict-item]
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("RegistryRecordSummary.registry_arn required")
    if data.get("recordArn") is not None:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError("RegistryRecordSummary.record_arn required")
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError("RegistryRecordSummary.record_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("RegistryRecordSummary.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("recordType") is not None:
        import capo_agent_registry.types.record_type

        out["record_type"] = capo_agent_registry.types.record_type.deserialize_json(
            data["recordType"]
        )
    else:
        raise DeserializationError("RegistryRecordSummary.record_type required")
    if data.get("descriptors") is not None:
        import capo_agent_registry.types.descriptors

        out["descriptors"] = capo_agent_registry.types.descriptors.deserialize_json(
            data["descriptors"]
        )
    else:
        raise DeserializationError("RegistryRecordSummary.descriptors required")
    if data.get("recordVersion") is not None:
        out["record_version"] = data["recordVersion"]
    else:
        raise DeserializationError("RegistryRecordSummary.record_version required")
    if data.get("status") is not None:
        import capo_agent_registry.types.registry_record_status

        out["status"] = (
            capo_agent_registry.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("RegistryRecordSummary.status required")
    if data.get("createdAt") is not None:
        import capo_agent_registry.types.date_timestamp

        out["created_at"] = capo_agent_registry.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("RegistryRecordSummary.created_at required")
    if data.get("updatedAt") is not None:
        import capo_agent_registry.types.date_timestamp

        out["updated_at"] = capo_agent_registry.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("RegistryRecordSummary.updated_at required")
    return out
