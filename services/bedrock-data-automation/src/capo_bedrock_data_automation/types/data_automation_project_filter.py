"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_stage


class DataAutomationProjectFilter(TypedDict, closed=True):
    project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    project_stage: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectFilter) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "project_stage" in value:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataAutomationProjectFilter:
    out: DataAutomationProjectFilter = {}  # type: ignore[typeddict-item]
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
    return out
