"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProject``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.custom_output_configuration
    import capo_bedrock_data_automation.types.data_automation_library_configuration
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_description
    import capo_bedrock_data_automation.types.data_automation_project_name
    import capo_bedrock_data_automation.types.data_automation_project_stage
    import capo_bedrock_data_automation.types.data_automation_project_status
    import capo_bedrock_data_automation.types.data_automation_project_type
    import capo_bedrock_data_automation.types.date_timestamp
    import capo_bedrock_data_automation.types.kms_encryption_context
    import capo_bedrock_data_automation.types.kms_key_id
    import capo_bedrock_data_automation.types.override_configuration
    import capo_bedrock_data_automation.types.standard_output_configuration


class DataAutomationProject(TypedDict, closed=True):
    project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    creation_time: "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    last_modified_time: (
        "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    )
    project_name: "capo_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName"
    project_stage: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_type: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
    ]
    project_description: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
    ]
    standard_output_configuration: NotRequired[
        "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration"
    ]
    custom_output_configuration: NotRequired[
        "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
    ]
    override_configuration: NotRequired[
        "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
    ]
    data_automation_library_configuration: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
    ]
    status: "capo_bedrock_data_automation.types.data_automation_project_status.DataAutomationProjectStatus"
    kms_key_id: NotRequired["capo_bedrock_data_automation.types.kms_key_id.KmsKeyId"]
    kms_encryption_context: NotRequired[
        "capo_bedrock_data_automation.types.kms_encryption_context.KmsEncryptionContext"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProject) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    import capo_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    import capo_bedrock_data_automation.types.date_timestamp

    out["lastModifiedTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["projectName"] = value["project_name"]
    if "project_stage" in value:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    if "project_type" in value:
        import capo_bedrock_data_automation.types.data_automation_project_type

        out["projectType"] = (
            capo_bedrock_data_automation.types.data_automation_project_type.serialize_json(
                value["project_type"]
            )
        )
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
    if "standard_output_configuration" in value:
        import capo_bedrock_data_automation.types.standard_output_configuration

        out["standardOutputConfiguration"] = (
            capo_bedrock_data_automation.types.standard_output_configuration.serialize_json(
                value["standard_output_configuration"]
            )
        )
    if "custom_output_configuration" in value:
        import capo_bedrock_data_automation.types.custom_output_configuration

        out["customOutputConfiguration"] = (
            capo_bedrock_data_automation.types.custom_output_configuration.serialize_json(
                value["custom_output_configuration"]
            )
        )
    if "override_configuration" in value:
        import capo_bedrock_data_automation.types.override_configuration

        out["overrideConfiguration"] = (
            capo_bedrock_data_automation.types.override_configuration.serialize_json(
                value["override_configuration"]
            )
        )
    if "data_automation_library_configuration" in value:
        import capo_bedrock_data_automation.types.data_automation_library_configuration

        out["dataAutomationLibraryConfiguration"] = (
            capo_bedrock_data_automation.types.data_automation_library_configuration.serialize_json(
                value["data_automation_library_configuration"]
            )
        )
    import capo_bedrock_data_automation.types.data_automation_project_status

    out["status"] = (
        capo_bedrock_data_automation.types.data_automation_project_status.serialize_json(
            value["status"]
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


def deserialize_json(data: dict) -> DataAutomationProject:
    out: DataAutomationProject = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        out["project_arn"] = ""
    if data.get("creationTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        import datetime

        out["last_modified_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    if data.get("projectStage") is not None:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
            )
        )
    if data.get("projectType") is not None:
        import capo_bedrock_data_automation.types.data_automation_project_type

        out["project_type"] = (
            capo_bedrock_data_automation.types.data_automation_project_type.deserialize_json(
                data["projectType"]
            )
        )
    if data.get("projectDescription") is not None:
        out["project_description"] = data["projectDescription"]
    if data.get("standardOutputConfiguration") is not None:
        import capo_bedrock_data_automation.types.standard_output_configuration

        out["standard_output_configuration"] = (
            capo_bedrock_data_automation.types.standard_output_configuration.deserialize_json(
                data["standardOutputConfiguration"]
            )
        )
    if data.get("customOutputConfiguration") is not None:
        import capo_bedrock_data_automation.types.custom_output_configuration

        out["custom_output_configuration"] = (
            capo_bedrock_data_automation.types.custom_output_configuration.deserialize_json(
                data["customOutputConfiguration"]
            )
        )
    if data.get("overrideConfiguration") is not None:
        import capo_bedrock_data_automation.types.override_configuration

        out["override_configuration"] = (
            capo_bedrock_data_automation.types.override_configuration.deserialize_json(
                data["overrideConfiguration"]
            )
        )
    if data.get("dataAutomationLibraryConfiguration") is not None:
        import capo_bedrock_data_automation.types.data_automation_library_configuration

        out["data_automation_library_configuration"] = (
            capo_bedrock_data_automation.types.data_automation_library_configuration.deserialize_json(
                data["dataAutomationLibraryConfiguration"]
            )
        )
    if data.get("status") is not None:
        import capo_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            capo_bedrock_data_automation.types.data_automation_project_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_data_automation.types.data_automation_project_status.DataAutomationProjectStatus",
            "",
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


def redact_sensitive(value: DataAutomationProject) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "project_name" in value:
        out["project_name"] = "*** Sensitive Data Redacted ***"
    if "project_description" in value:
        out["project_description"] = "*** Sensitive Data Redacted ***"
    return out
