"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionSource``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.tool_description_configuration_bundle
    import capo_bedrock_agentcore.types.tool_description_text_input


class _ToolDescriptionSource_toolDescriptionText(TypedDict, closed=True):
    toolDescriptionText: "capo_bedrock_agentcore.types.tool_description_text_input.ToolDescriptionTextInput"


class _ToolDescriptionSource_configurationBundle(TypedDict, closed=True):
    configurationBundle: "capo_bedrock_agentcore.types.tool_description_configuration_bundle.ToolDescriptionConfigurationBundle"


ToolDescriptionSource: TypeAlias = (
    _ToolDescriptionSource_toolDescriptionText
    | _ToolDescriptionSource_configurationBundle
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionSource) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ToolDescriptionSource: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "toolDescriptionText" in value:
        import capo_bedrock_agentcore.types.tool_description_text_input

        return {
            "toolDescriptionText": capo_bedrock_agentcore.types.tool_description_text_input.serialize_json(
                value["toolDescriptionText"]
            )
        }
    elif "configurationBundle" in value:
        import capo_bedrock_agentcore.types.tool_description_configuration_bundle

        return {
            "configurationBundle": capo_bedrock_agentcore.types.tool_description_configuration_bundle.serialize_json(
                value["configurationBundle"]
            )
        }
    else:
        raise SerializationError("ToolDescriptionSource: no variant present")


def deserialize_json(data: dict) -> ToolDescriptionSource:
    if data.get("toolDescriptionText") is not None:
        import capo_bedrock_agentcore.types.tool_description_text_input

        return {
            "toolDescriptionText": capo_bedrock_agentcore.types.tool_description_text_input.deserialize_json(
                data["toolDescriptionText"]
            )
        }
    elif data.get("configurationBundle") is not None:
        import capo_bedrock_agentcore.types.tool_description_configuration_bundle

        return {
            "configurationBundle": capo_bedrock_agentcore.types.tool_description_configuration_bundle.deserialize_json(
                data["configurationBundle"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ToolDescriptionSource: no recognized variant key")


def redact_sensitive(value: ToolDescriptionSource) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "toolDescriptionText" in value:
        import capo_bedrock_agentcore.types.tool_description_text_input

        out["toolDescriptionText"] = (
            capo_bedrock_agentcore.types.tool_description_text_input.redact_sensitive(
                value["toolDescriptionText"]
            )
        )
    return out
