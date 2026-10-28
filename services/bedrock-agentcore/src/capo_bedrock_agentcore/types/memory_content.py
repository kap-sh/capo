"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#MemoryContent``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_string


class MemoryContentTextMember(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_string.SensitiveString"


MemoryContent: TypeAlias = MemoryContentTextMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: MemoryContent) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"MemoryContent: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("MemoryContent: no variant present")


def deserialize_json(data: dict) -> MemoryContent:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("MemoryContent: no recognized variant key")


def redact_sensitive(value: MemoryContent) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
