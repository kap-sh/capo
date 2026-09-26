"""Generated from Smithy shape ``com.amazonaws.agentregistrycontrol#UpdateRegistryRecordResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_agent_registry_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_agent_registry_control.types.creator_account_id
    import capo_agent_registry_control.types.date_timestamp
    import capo_agent_registry_control.types.description
    import capo_agent_registry_control.types.descriptors
    import capo_agent_registry_control.types.provenance_list
    import capo_agent_registry_control.types.record_type
    import capo_agent_registry_control.types.registry_arn
    import capo_agent_registry_control.types.registry_record_arn
    import capo_agent_registry_control.types.registry_record_display_name
    import capo_agent_registry_control.types.registry_record_id
    import capo_agent_registry_control.types.registry_record_name
    import capo_agent_registry_control.types.registry_record_status
    import capo_agent_registry_control.types.registry_record_version


class UpdateRegistryRecordResponse(TypedDict, closed=True):
    registry_arn: "capo_agent_registry_control.types.registry_arn.RegistryArn"
    """<p>The Amazon Resource Name (ARN) of the parent registry that owns the record.</p>"""
    record_arn: (
        "capo_agent_registry_control.types.registry_record_arn.RegistryRecordArn"
    )
    """<p>The Amazon Resource Name (ARN) of the registry record.</p>"""
    record_id: "capo_agent_registry_control.types.registry_record_id.RegistryRecordId"
    """<p>The unique identifier of the registry record.</p>"""
    name: "capo_agent_registry_control.types.registry_record_name.RegistryRecordName"
    """<p>The name of the registry record. Names are unique within a registry.</p>"""
    display_name: NotRequired[
        "capo_agent_registry_control.types.registry_record_display_name.RegistryRecordDisplayName"
    ]
    """<p>The human-readable display name of the registry record.</p>"""
    description: NotRequired[
        "capo_agent_registry_control.types.description.Description"
    ]
    """<p>A description of the registry record.</p>"""
    record_type: "capo_agent_registry_control.types.record_type.RecordType"
    """<p>The type of the registry record, such as MCP, AGENT, SKILL, or CUSTOM.</p>"""
    descriptors: NotRequired[
        "capo_agent_registry_control.types.descriptors.Descriptors"
    ]
    """<p>The typed descriptors that define the content of the registry record.</p>"""
    record_version: NotRequired[
        "capo_agent_registry_control.types.registry_record_version.RegistryRecordVersion"
    ]
    """<p>The version identifier of the registry record.</p>"""
    status: (
        "capo_agent_registry_control.types.registry_record_status.RegistryRecordStatus"
    )
    """<p>The lifecycle status of the registry record.</p>"""
    created_at: "capo_agent_registry_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry record was created.</p>"""
    updated_at: "capo_agent_registry_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the registry record was last updated.</p>"""
    status_reason: NotRequired["str"]
    """<p>The reason for the current status. Typically populated when the status indicates a failure state.</p>"""
    provenance: NotRequired[
        "capo_agent_registry_control.types.provenance_list.ProvenanceList"
    ]
    created_by_auto_detection: NotRequired["bool"]
    """<p>Specifies whether the registry record was created by auto-detection. <code>true</code> indicates the record was automatically created by the service based on the registry's auto-detection configuration; <code>false</code> indicates the record was created through a control-plane API call.</p>"""
    created_by: NotRequired[
        "capo_agent_registry_control.types.creator_account_id.CreatorAccountId"
    ]
    """<p>The ID of the Amazon Web Services account that created the registry record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRegistryRecordResponse) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    out["recordArn"] = value["record_arn"]
    out["recordId"] = value["record_id"]
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_agent_registry_control.types.record_type

    out["recordType"] = capo_agent_registry_control.types.record_type.serialize_json(
        value["record_type"]
    )
    if "descriptors" in value:
        import capo_agent_registry_control.types.descriptors

        out["descriptors"] = (
            capo_agent_registry_control.types.descriptors.serialize_json(
                value["descriptors"]
            )
        )
    if "record_version" in value:
        out["recordVersion"] = value["record_version"]
    import capo_agent_registry_control.types.registry_record_status

    out["status"] = (
        capo_agent_registry_control.types.registry_record_status.serialize_json(
            value["status"]
        )
    )
    import capo_agent_registry_control.types.date_timestamp

    out["createdAt"] = capo_agent_registry_control.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_agent_registry_control.types.date_timestamp

    out["updatedAt"] = capo_agent_registry_control.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "provenance" in value:
        import capo_agent_registry_control.types.provenance_list

        out["provenance"] = (
            capo_agent_registry_control.types.provenance_list.serialize_json(
                value["provenance"]
            )
        )
    if "created_by_auto_detection" in value:
        out["createdByAutoDetection"] = value["created_by_auto_detection"]
    if "created_by" in value:
        out["createdBy"] = value["created_by"]
    return out


def deserialize_json(data: dict) -> UpdateRegistryRecordResponse:
    out: UpdateRegistryRecordResponse = {}  # type: ignore[typeddict-item]
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.registry_arn required")
    if data.get("recordArn") is not None:
        out["record_arn"] = data["recordArn"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.record_arn required")
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.record_id required")
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.name required")
    if data.get("displayName") is not None:
        out["display_name"] = data["displayName"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("recordType") is not None:
        import capo_agent_registry_control.types.record_type

        out["record_type"] = (
            capo_agent_registry_control.types.record_type.deserialize_json(
                data["recordType"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.record_type required")
    if data.get("descriptors") is not None:
        import capo_agent_registry_control.types.descriptors

        out["descriptors"] = (
            capo_agent_registry_control.types.descriptors.deserialize_json(
                data["descriptors"]
            )
        )
    if data.get("recordVersion") is not None:
        out["record_version"] = data["recordVersion"]
    if data.get("status") is not None:
        import capo_agent_registry_control.types.registry_record_status

        out["status"] = (
            capo_agent_registry_control.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.status required")
    if data.get("createdAt") is not None:
        import capo_agent_registry_control.types.date_timestamp

        out["created_at"] = (
            capo_agent_registry_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.created_at required")
    if data.get("updatedAt") is not None:
        import capo_agent_registry_control.types.date_timestamp

        out["updated_at"] = (
            capo_agent_registry_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("UpdateRegistryRecordResponse.updated_at required")
    if data.get("statusReason") is not None:
        out["status_reason"] = data["statusReason"]
    if data.get("provenance") is not None:
        import capo_agent_registry_control.types.provenance_list

        out["provenance"] = (
            capo_agent_registry_control.types.provenance_list.deserialize_json(
                data["provenance"]
            )
        )
    if data.get("createdByAutoDetection") is not None:
        out["created_by_auto_detection"] = data["createdByAutoDetection"]
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    return out
