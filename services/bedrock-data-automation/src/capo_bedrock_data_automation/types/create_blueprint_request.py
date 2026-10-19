"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateBlueprintRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_name
    import capo_bedrock_data_automation.types.blueprint_schema
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.client_token
    import capo_bedrock_data_automation.types.encryption_configuration
    import capo_bedrock_data_automation.types.tag_list
    import capo_bedrock_data_automation.types.type


class CreateBlueprintRequest(TypedDict, closed=True):
    blueprint_name: "capo_bedrock_data_automation.types.blueprint_name.BlueprintName"
    type: "capo_bedrock_data_automation.types.type.Type"
    blueprint_stage: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    schema: "capo_bedrock_data_automation.types.blueprint_schema.BlueprintSchema"
    client_token: NotRequired[
        "capo_bedrock_data_automation.types.client_token.ClientToken"
    ]
    encryption_configuration: NotRequired[
        "capo_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]
    tags: NotRequired["capo_bedrock_data_automation.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateBlueprintRequest) -> dict:
    out: dict = {}
    out["blueprintName"] = value["blueprint_name"]
    import capo_bedrock_data_automation.types.type

    out["type"] = capo_bedrock_data_automation.types.type.serialize_json(value["type"])
    if "blueprint_stage" in value:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
            )
        )
    out["schema"] = value["schema"]
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


def deserialize_json(data: dict) -> CreateBlueprintRequest:
    out: CreateBlueprintRequest = {}  # type: ignore[typeddict-item]
    if data.get("blueprintName") is not None:
        out["blueprint_name"] = data["blueprintName"]
    else:
        out["blueprint_name"] = ""
    if data.get("type") is not None:
        import capo_bedrock_data_automation.types.type

        out["type"] = capo_bedrock_data_automation.types.type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast("capo_bedrock_data_automation.types.type.Type", "")
    if data.get("blueprintStage") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    if data.get("schema") is not None:
        out["schema"] = data["schema"]
    else:
        out["schema"] = ""
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


def redact_sensitive(value: CreateBlueprintRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "blueprint_name" in value:
        out["blueprint_name"] = "*** Sensitive Data Redacted ***"
    if "schema" in value:
        out["schema"] = "*** Sensitive Data Redacted ***"
    return out
