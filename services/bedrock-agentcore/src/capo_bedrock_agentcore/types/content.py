"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#Content``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_string


class _Content_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_string.SensitiveString"


Content: TypeAlias = _Content_text


# --- restJson1 ser/de ---
def serialize_json(value: Content) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("Content: no variant present")


def deserialize_json(data: dict) -> Content:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        raise DeserializationError("Content: no recognized variant key")


def redact_sensitive(value: Content) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
