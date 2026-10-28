"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ToolChoice``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.any_tool_choice
    import capo_bedrock_runtime.types.auto_tool_choice
    import capo_bedrock_runtime.types.specific_tool_choice


class ToolChoiceAutoMember(TypedDict, closed=True):
    auto: "capo_bedrock_runtime.types.auto_tool_choice.AutoToolChoice"


class ToolChoiceAnyMember(TypedDict, closed=True):
    any: "capo_bedrock_runtime.types.any_tool_choice.AnyToolChoice"


class ToolChoiceToolMember(TypedDict, closed=True):
    tool: "capo_bedrock_runtime.types.specific_tool_choice.SpecificToolChoice"


ToolChoice: TypeAlias = (
    ToolChoiceAutoMember
    | ToolChoiceAnyMember
    | ToolChoiceToolMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ToolChoice) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ToolChoice: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "auto" in value:
        import capo_bedrock_runtime.types.auto_tool_choice

        return {
            "auto": capo_bedrock_runtime.types.auto_tool_choice.serialize_json(
                value["auto"]
            )
        }
    elif "any" in value:
        import capo_bedrock_runtime.types.any_tool_choice

        return {
            "any": capo_bedrock_runtime.types.any_tool_choice.serialize_json(
                value["any"]
            )
        }
    elif "tool" in value:
        import capo_bedrock_runtime.types.specific_tool_choice

        return {
            "tool": capo_bedrock_runtime.types.specific_tool_choice.serialize_json(
                value["tool"]
            )
        }
    else:
        raise SerializationError("ToolChoice: no variant present")


def deserialize_json(data: dict) -> ToolChoice:
    if data.get("auto") is not None:
        import capo_bedrock_runtime.types.auto_tool_choice

        return {
            "auto": capo_bedrock_runtime.types.auto_tool_choice.deserialize_json(
                data["auto"]
            )
        }
    elif data.get("any") is not None:
        import capo_bedrock_runtime.types.any_tool_choice

        return {
            "any": capo_bedrock_runtime.types.any_tool_choice.deserialize_json(
                data["any"]
            )
        }
    elif data.get("tool") is not None:
        import capo_bedrock_runtime.types.specific_tool_choice

        return {
            "tool": capo_bedrock_runtime.types.specific_tool_choice.deserialize_json(
                data["tool"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ToolChoice: no recognized variant key")
