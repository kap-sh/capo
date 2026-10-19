"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSystemContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)
from capo_bedrock_agentcore_control.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.sensitive_text


class _HarnessSystemContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_agentcore_control.types.sensitive_text.SensitiveText"


HarnessSystemContentBlock: TypeAlias = (
    _HarnessSystemContentBlock_text | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSystemContentBlock) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"HarnessSystemContentBlock: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("HarnessSystemContentBlock: no variant present")


def deserialize_json(data: dict) -> HarnessSystemContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "HarnessSystemContentBlock: no recognized variant key"
        )


def redact_sensitive(
    value: HarnessSystemContentBlock,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
