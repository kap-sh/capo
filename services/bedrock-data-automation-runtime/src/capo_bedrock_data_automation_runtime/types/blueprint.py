"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#Blueprint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation_runtime.types.blueprint_arn
    import capo_bedrock_data_automation_runtime.types.blueprint_stage
    import capo_bedrock_data_automation_runtime.types.blueprint_version


class Blueprint(TypedDict, closed=True):
    blueprint_arn: (
        "capo_bedrock_data_automation_runtime.types.blueprint_arn.BlueprintArn"
    )
    """Arn of blueprint."""
    version: NotRequired[
        "capo_bedrock_data_automation_runtime.types.blueprint_version.BlueprintVersion"
    ]
    """Version of blueprint."""
    stage: NotRequired[
        "capo_bedrock_data_automation_runtime.types.blueprint_stage.BlueprintStage"
    ]
    """Stage of blueprint."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Blueprint) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    if "version" in value:
        out["version"] = value["version"]
    if "stage" in value:
        import capo_bedrock_data_automation_runtime.types.blueprint_stage

        out["stage"] = (
            capo_bedrock_data_automation_runtime.types.blueprint_stage.serialize_aws_json_1_1(
                value["stage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Blueprint:
    out: Blueprint = {}  # type: ignore[typeddict-item]
    if data.get("blueprintArn") is not None:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        out["blueprint_arn"] = ""
    if data.get("version") is not None:
        out["version"] = data["version"]
    if data.get("stage") is not None:
        import capo_bedrock_data_automation_runtime.types.blueprint_stage

        out["stage"] = (
            capo_bedrock_data_automation_runtime.types.blueprint_stage.deserialize_aws_json_1_1(
                data["stage"]
            )
        )
    return out
