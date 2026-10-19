"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CopyBlueprintStageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.client_token


class CopyBlueprintStageRequest(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """Blueprint to be copied"""
    source_stage: "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    """Source stage to copy from"""
    target_stage: "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    """Target stage to copy to"""
    client_token: NotRequired[
        "capo_bedrock_data_automation.types.client_token.ClientToken"
    ]
    """Client token for idempotency"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyBlueprintStageRequest) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.blueprint_stage

    out["sourceStage"] = (
        capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
            value["source_stage"]
        )
    )
    import capo_bedrock_data_automation.types.blueprint_stage

    out["targetStage"] = (
        capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
            value["target_stage"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CopyBlueprintStageRequest:
    out: CopyBlueprintStageRequest = {}  # type: ignore[typeddict-item]
    if data.get("sourceStage") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["source_stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["sourceStage"]
            )
        )
    else:
        import typing

        out["source_stage"] = typing.cast(
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage", ""
        )
    if data.get("targetStage") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["target_stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["targetStage"]
            )
        )
    else:
        import typing

        out["target_stage"] = typing.cast(
            "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage", ""
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
