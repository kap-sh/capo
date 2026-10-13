"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibrary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_arn
    import capo_bedrock_data_automation.types.data_automation_library_description
    import capo_bedrock_data_automation.types.data_automation_library_name
    import capo_bedrock_data_automation.types.data_automation_library_status
    import capo_bedrock_data_automation.types.date_timestamp
    import capo_bedrock_data_automation.types.entity_type_info_list
    import capo_bedrock_data_automation.types.kms_encryption_context
    import capo_bedrock_data_automation.types.kms_key_id


class DataAutomationLibrary(TypedDict, closed=True):
    library_arn: "capo_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    creation_time: "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    library_name: "capo_bedrock_data_automation.types.data_automation_library_name.DataAutomationLibraryName"
    library_description: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_description.DataAutomationLibraryDescription"
    ]
    status: "capo_bedrock_data_automation.types.data_automation_library_status.DataAutomationLibraryStatus"
    entity_types: NotRequired[
        "capo_bedrock_data_automation.types.entity_type_info_list.EntityTypeInfoList"
    ]
    kms_key_id: NotRequired["capo_bedrock_data_automation.types.kms_key_id.KmsKeyId"]
    kms_encryption_context: NotRequired[
        "capo_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibrary) -> dict:
    out: dict = {}
    out["libraryArn"] = value["library_arn"]
    import capo_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["libraryName"] = value["library_name"]
    if "library_description" in value:
        out["libraryDescription"] = value["library_description"]
    import capo_bedrock_data_automation.types.data_automation_library_status

    out["status"] = (
        capo_bedrock_data_automation.types.data_automation_library_status.serialize_json(
            value["status"]
        )
    )
    if "entity_types" in value:
        import capo_bedrock_data_automation.types.entity_type_info_list

        out["entityTypes"] = (
            capo_bedrock_data_automation.types.entity_type_info_list.serialize_json(
                value["entity_types"]
            )
        )
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "kms_encryption_context" in value:
        import capo_bedrock_data_automation.types.kms_encryption_context

        out["kmsEncryptionContext"] = (
            capo_bedrock_data_automation.types.kms_encryption_context.serialize_json(
                value["kms_encryption_context"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAutomationLibrary:
    out: DataAutomationLibrary = {}  # type: ignore[typeddict-item]
    if data.get("libraryArn") is not None:
        out["library_arn"] = data["libraryArn"]
    else:
        raise DeserializationError("DataAutomationLibrary.library_arn required")
    if data.get("creationTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("DataAutomationLibrary.creation_time required")
    if data.get("libraryName") is not None:
        out["library_name"] = data["libraryName"]
    else:
        raise DeserializationError("DataAutomationLibrary.library_name required")
    if data.get("libraryDescription") is not None:
        out["library_description"] = data["libraryDescription"]
    if data.get("status") is not None:
        import capo_bedrock_data_automation.types.data_automation_library_status

        out["status"] = (
            capo_bedrock_data_automation.types.data_automation_library_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("DataAutomationLibrary.status required")
    if data.get("entityTypes") is not None:
        import capo_bedrock_data_automation.types.entity_type_info_list

        out["entity_types"] = (
            capo_bedrock_data_automation.types.entity_type_info_list.deserialize_json(
                data["entityTypes"]
            )
        )
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("kmsEncryptionContext") is not None:
        import capo_bedrock_data_automation.types.kms_encryption_context

        out["kms_encryption_context"] = (
            capo_bedrock_data_automation.types.kms_encryption_context.deserialize_json(
                data["kmsEncryptionContext"]
            )
        )
    return out


def redact_sensitive(value: DataAutomationLibrary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "library_name" in value:
        out["library_name"] = "*** Sensitive Data Redacted ***"
    if "library_description" in value:
        out["library_description"] = "*** Sensitive Data Redacted ***"
    return out
