"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateBlueprintRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_schema
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.encryption_configuration


class UpdateBlueprintRequest(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """ARN generated at the server side when a Blueprint is created"""
    schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema"
    blueprint_stage: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBlueprintRequest) -> dict:
    out: dict = {}
    out["schema"] = value["schema"]
    if "blueprint_stage" in value:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
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


def deserialize_json(data: dict) -> UpdateBlueprintRequest:
    out: UpdateBlueprintRequest = {}  # type: ignore[typeddict-item]
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        out["schema"] = ""
    if data.get("blueprintStage") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
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


def redact_sensitive(value: UpdateBlueprintRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "schema" in value:
        out["schema"] = "*** Sensitive Data Redacted ***"
    return out
