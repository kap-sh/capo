"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_name
    import capo_bedrock_data_automation.types.data_automation_project_stage
    import capo_bedrock_data_automation.types.data_automation_project_type
    import capo_bedrock_data_automation.types.date_timestamp


class DataAutomationProjectSummary(TypedDict, closed=True):
    project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    project_stage: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_type: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
    ]
    project_name: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName"
    ]
    creation_time: "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectSummary) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
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
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    import capo_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataAutomationProjectSummary:
    out: DataAutomationProjectSummary = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        out["project_arn"] = ""
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
    if data.get("projectName") is not None:
        out["project_name"] = data["projectName"]
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
    return out


def redact_sensitive(value: DataAutomationProjectSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "project_name" in value:
        out["project_name"] = "*** Sensitive Data Redacted ***"
    return out
