"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessSystemContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_text


class _HarnessSystemContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"


HarnessSystemContentBlock: TypeAlias = _HarnessSystemContentBlock_text


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSystemContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("HarnessSystemContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessSystemContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        raise DeserializationError(
            "HarnessSystemContentBlock: no recognized variant key"
        )


def redact_sensitive(value: HarnessSystemContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
