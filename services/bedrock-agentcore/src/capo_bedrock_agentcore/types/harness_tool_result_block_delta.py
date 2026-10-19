"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#HarnessToolResultBlockDelta``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore.errors import DeserializationError, SerializationError
from capo_bedrock_agentcore.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.sensitive_json
    import capo_bedrock_agentcore.types.sensitive_text


class _HarnessToolResultBlockDelta_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore.types.sensitive_text.SensitiveText"


class _HarnessToolResultBlockDelta_json(TypedDict, closed=True):
    json: "capo_bedrock_agentcore.types.sensitive_json.SensitiveJson"


HarnessToolResultBlockDelta: TypeAlias = (
    _HarnessToolResultBlockDelta_text
    | _HarnessToolResultBlockDelta_json
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolResultBlockDelta) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HarnessToolResultBlockDelta: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    elif "json" in value:
        return {"json": value["json"]}
    else:
        raise SerializationError("HarnessToolResultBlockDelta: no variant present")


def deserialize_json(data: dict) -> HarnessToolResultBlockDelta:
    if data.get("text") is not None:
        return {"text": data["text"]}
    elif data.get("json") is not None:
        return {"json": data["json"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "HarnessToolResultBlockDelta: no recognized variant key"
        )


def redact_sensitive(
    value: HarnessToolResultBlockDelta,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    if "json" in value:
        out["json"] = "*** Sensitive Data Redacted ***"
    return out
