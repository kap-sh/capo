"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#DataAutomationConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.data_automation_arn
    import capo_bedrock_data_automation_runtime.types.data_automation_stage


class DataAutomationConfiguration(TypedDict, closed=True):
    data_automation_project_arn: "capo_bedrock_data_automation_runtime.types.data_automation_arn.DataAutomationArn"
    """Data automation project arn."""
    stage: NotRequired[
        "capo_bedrock_data_automation_runtime.types.data_automation_stage.DataAutomationStage"
    ]
    """Data automation stage."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataAutomationConfiguration) -> dict:
    out: dict = {}
    out["dataAutomationProjectArn"] = value["data_automation_project_arn"]
    if "stage" in value:
        import capo_bedrock_data_automation_runtime.types.data_automation_stage

        out["stage"] = (
            capo_bedrock_data_automation_runtime.types.data_automation_stage.serialize_aws_json_1_1(
                value["stage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataAutomationConfiguration:
    out: DataAutomationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("dataAutomationProjectArn") is not None:
        out["data_automation_project_arn"] = data["dataAutomationProjectArn"]
    else:
        out["data_automation_project_arn"] = ""
    if data.get("stage") is not None:
        import capo_bedrock_data_automation_runtime.types.data_automation_stage

        out["stage"] = (
            capo_bedrock_data_automation_runtime.types.data_automation_stage.deserialize_aws_json_1_1(
                data["stage"]
            )
        )
    return out
