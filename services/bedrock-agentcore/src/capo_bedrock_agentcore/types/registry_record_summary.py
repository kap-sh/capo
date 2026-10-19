"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RegistryRecordSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.date_timestamp
    import capo_bedrock_agentcore.types.description
    import capo_bedrock_agentcore.types.descriptor_type
    import capo_bedrock_agentcore.types.descriptors
    import capo_bedrock_agentcore.types.registry_arn
    import capo_bedrock_agentcore.types.registry_record_arn
    import capo_bedrock_agentcore.types.registry_record_id
    import capo_bedrock_agentcore.types.registry_record_name
    import capo_bedrock_agentcore.types.registry_record_status
    import capo_bedrock_agentcore.types.registry_record_version


class RegistryRecordSummary(TypedDict, closed=True):
    registry_arn: "capo_bedrock_agentcore.types.registry_arn.RegistryArn"
    """<p> The Amazon Resource Name (ARN) of the registry that this record belongs to.</p>"""
    record_arn: "capo_bedrock_agentcore.types.registry_record_arn.RegistryRecordArn"
    """<p> The Amazon Resource Name (ARN) of the registry record.</p>"""
    record_id: "capo_bedrock_agentcore.types.registry_record_id.RegistryRecordId"
    """<p> The unique identifier of the registry record.</p>"""
    name: "capo_bedrock_agentcore.types.registry_record_name.RegistryRecordName"
    """<p> The name of the registry record.</p>"""
    description: NotRequired["capo_bedrock_agentcore.types.description.Description"]
    """<p> A description of the registry record.</p>"""
    descriptor_type: "capo_bedrock_agentcore.types.descriptor_type.DescriptorType"
    """<p> The type of descriptor associated with this registry record.</p>"""
    descriptors: "capo_bedrock_agentcore.types.descriptors.Descriptors"
    """<p> The descriptor configurations for this registry record.</p>"""
    version: (
        "capo_bedrock_agentcore.types.registry_record_version.RegistryRecordVersion"
    )
    """<p> The version of the registry record.</p>"""
    status: "capo_bedrock_agentcore.types.registry_record_status.RegistryRecordStatus"
    """<p> The current status of the registry record.</p>"""
    created_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p> The date and time when the registry record was created.</p>"""
    updated_at: "capo_bedrock_agentcore.types.date_timestamp.DateTimestamp"
    """<p> The date and time when the registry record was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegistryRecordSummary) -> dict:
    out: dict = {}
    out["registryArn"] = value["registry_arn"]
    out["recordArn"] = value["record_arn"]
    out["recordId"] = value["record_id"]
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agentcore.types.descriptor_type

    out["descriptorType"] = capo_bedrock_agentcore.types.descriptor_type.serialize_json(
        value["descriptor_type"]
    )
    import capo_bedrock_agentcore.types.descriptors

    out["descriptors"] = capo_bedrock_agentcore.types.descriptors.serialize_json(
        value["descriptors"]
    )
    out["version"] = value["version"]
    import capo_bedrock_agentcore.types.registry_record_status

    out["status"] = capo_bedrock_agentcore.types.registry_record_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["createdAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import capo_bedrock_agentcore.types.date_timestamp

    out["updatedAt"] = capo_bedrock_agentcore.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> RegistryRecordSummary:
    out: RegistryRecordSummary = {}  # type: ignore[typeddict-item]
    if data.get("registryArn") is not None:
        out["registry_arn"] = data["registryArn"]
    else:
        out["registry_arn"] = ""
    if data.get("recordArn") is not None:
        out["record_arn"] = data["recordArn"]
    else:
        out["record_arn"] = ""
    if data.get("recordId") is not None:
        out["record_id"] = data["recordId"]
    else:
        out["record_id"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("descriptorType") is not None:
        import capo_bedrock_agentcore.types.descriptor_type

        out["descriptor_type"] = (
            capo_bedrock_agentcore.types.descriptor_type.deserialize_json(
                data["descriptorType"]
            )
        )
    else:
        import typing

        out["descriptor_type"] = typing.cast(
            "capo_bedrock_agentcore.types.descriptor_type.DescriptorType", ""
        )
    if data.get("descriptors") is not None:
        import capo_bedrock_agentcore.types.descriptors

        out["descriptors"] = capo_bedrock_agentcore.types.descriptors.deserialize_json(
            data["descriptors"]
        )
    else:
        raise DeserializationError("RegistryRecordSummary.descriptors required")
    if data.get("version") is not None:
        out["version"] = data["version"]
    else:
        out["version"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore.types.registry_record_status

        out["status"] = (
            capo_bedrock_agentcore.types.registry_record_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore.types.registry_record_status.RegistryRecordStatus",
            "",
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out


def redact_sensitive(value: RegistryRecordSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "description" in value:
        out["description"] = "*** Sensitive Data Redacted ***"
    return out
