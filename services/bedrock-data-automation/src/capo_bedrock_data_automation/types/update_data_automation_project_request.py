"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateDataAutomationProjectRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.custom_output_configuration
    import capo_bedrock_data_automation.types.data_automation_library_configuration
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_description
    import capo_bedrock_data_automation.types.data_automation_project_stage
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.override_configuration
    import capo_bedrock_data_automation.types.standard_output_configuration


class UpdateDataAutomationProjectRequest(TypedDict, closed=True):
    project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    """ARN generated at the server side when a DataAutomationProject is created"""
    project_stage: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_description: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
    ]
    standard_output_configuration: "capo_bedrock_data_automation.types.standard_output_configuration.StandardOutputConfiguration"
    custom_output_configuration: NotRequired[
        "capo_bedrock_data_automation.types.custom_output_configuration.CustomOutputConfiguration"
    ]
    override_configuration: NotRequired[
        "capo_bedrock_data_automation.types.override_configuration.OverrideConfiguration"
    ]
    data_automation_library_configuration: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_library_configuration.DataAutomationLibraryConfiguration"
    ]
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataAutomationProjectRequest) -> dict:
    out: dict = {}
    if "project_stage" in value:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
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
    if "encryption_configuration" in value:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDataAutomationProjectRequest:
    out: UpdateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectStage") is not None:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
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
    else:
        raise DeserializationError(
            "UpdateDataAutomationProjectRequest.standard_output_configuration required"
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
    if data.get("encryptionConfiguration") is not None:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out


def redact_sensitive(value: UpdateDataAutomationProjectRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "project_description" in value:
        out["project_description"] = "*** Sensitive Data Redacted ***"
    return out
