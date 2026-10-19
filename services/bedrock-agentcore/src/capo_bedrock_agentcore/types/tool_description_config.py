"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#ToolDescriptionConfig``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.tool_description_text


class _ToolDescriptionConfig_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.tool_description_text.ToolDescriptionText"


ToolDescriptionConfig: TypeAlias = _ToolDescriptionConfig_text | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ToolDescriptionConfig) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"ToolDescriptionConfig: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("ToolDescriptionConfig: no variant present")


def deserialize_json(data: dict) -> ToolDescriptionConfig:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("ToolDescriptionConfig: no recognized variant key")


def redact_sensitive(
    value: ToolDescriptionConfig,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
