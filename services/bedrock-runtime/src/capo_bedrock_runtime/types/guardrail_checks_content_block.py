"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_text_content


class _GuardrailChecksContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_runtime.types.guardrail_checks_text_content.GuardrailChecksTextContent"


GuardrailChecksContentBlock: TypeAlias = (
    _GuardrailChecksContentBlock_text | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentBlock) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"GuardrailChecksContentBlock: cannot serialize unknown variant {value.name!r}"
        )
    elif "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("GuardrailChecksContentBlock: no variant present")


def deserialize_json(data: dict) -> GuardrailChecksContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError(
            "GuardrailChecksContentBlock: no recognized variant key"
        )


def redact_sensitive(
    value: GuardrailChecksContentBlock,
) -> dict[str, Any] | UnknownUnionMember:
    if isinstance(value, UnknownUnionMember):
        return value
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
