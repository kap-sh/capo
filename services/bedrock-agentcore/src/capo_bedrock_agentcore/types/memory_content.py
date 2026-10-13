"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryContent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_string


class _MemoryContent_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_string.SensitiveString"


MemoryContent: TypeAlias = _MemoryContent_text


# --- restJson1 ser/de ---
def serialize_json(value: MemoryContent) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("MemoryContent: no variant present")


def deserialize_json(data: dict) -> MemoryContent:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        raise DeserializationError("MemoryContent: no recognized variant key")


def redact_sensitive(value: MemoryContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
