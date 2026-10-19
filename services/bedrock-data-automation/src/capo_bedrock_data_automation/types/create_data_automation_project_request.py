"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateDataAutomationProjectRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.custom_output_configuration
    import capo_bedrock_data_automation.types.data_automation_library_configuration
    import capo_bedrock_data_automation.types.data_automation_project_description
    import capo_bedrock_data_automation.types.data_automation_project_name
    import capo_bedrock_data_automation.types.data_automation_project_stage
    import capo_bedrock_data_automation.types.data_automation_project_type
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.override_configuration
    import capo_bedrock_data_automation.types.standard_output_configuration
    import capo_bedrock_data_automation.types.tag_list


class CreateDataAutomationProjectRequest(TypedDict, closed=True):
    project_name: "capo_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName"
    project_description: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_description.DataAutomationProjectDescription"
    ]
    project_stage: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_type: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
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
    client_token: NotRequired[
        "capo_bedrock_data_automation.types.client_token.ClientToken"
    ]
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]
    tags: NotRequired["capo_bedrock_data_automation.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAutomationProjectRequest) -> dict:
    out: dict = {}
    out["projectName"] = value["project_name"]
    if "project_description" in value:
        out["projectDescription"] = value["project_description"]
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
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "encryption_configuration" in value:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateDataAutomationProjectRequest:
    out: CreateDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
    else:
        out["project_name"] = ""
    if data.get("projectDescription") is not None:
        out["project_description"] = data["projectDescription"]
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
    if data.get("standardOutputConfiguration") is not None:
        import capo_bedrock_data_automation.types.standard_output_configuration

        out["standard_output_configuration"] = (
            capo_bedrock_data_automation.types.standard_output_configuration.deserialize_json(
                data["standardOutputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "CreateDataAutomationProjectRequest.standard_output_configuration required"
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
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("encryptionConfiguration") is not None:
        import capo_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if data.get("tags") is not None:
        import capo_bedrock_data_automation.types.tag_list

        out["tags"] = capo_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateDataAutomationProjectRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "project_name" in value:
        out["project_name"] = "*** Sensitive Data Redacted ***"
    if "project_description" in value:
        out["project_description"] = "*** Sensitive Data Redacted ***"
    return out
