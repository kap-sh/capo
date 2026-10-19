"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateDataAutomationProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_stage
    import capo_bedrock_data_automation.types.data_automation_project_status


class UpdateDataAutomationProjectResponse(TypedDict, closed=True):
    project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    project_stage: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    status: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_status.DataAutomationProjectStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateDataAutomationProjectResponse) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "project_stage" in value:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    if "status" in value:
        import capo_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            capo_bedrock_data_automation.types.data_automation_project_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateDataAutomationProjectResponse:
    out: UpdateDataAutomationProjectResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("status") is not None:
        import capo_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            capo_bedrock_data_automation.types.data_automation_project_status.deserialize_json(
                data["status"]
            )
        )
    return out
