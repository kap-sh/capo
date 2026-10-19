"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintOptimizationObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_stage


class BlueprintOptimizationObject(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """Arn of blueprint."""
    stage: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    """Stage of blueprint."""


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintOptimizationObject) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    if "stage" in value:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["stage"]
            )
        )
    return out


def deserialize_json(data: dict) -> BlueprintOptimizationObject:
    out: BlueprintOptimizationObject = {}  # type: ignore[typeddict-item]
    if data.get("blueprintArn") is not None:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        out["blueprint_arn"] = ""
    if data.get("stage") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["stage"]
            )
        )
    return out
