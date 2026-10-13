"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailChecksContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_checks_text_content


class _GuardrailChecksContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_runtime.types.guardrail_checks_text_content.GuardrailChecksTextContent"


GuardrailChecksContentBlock: TypeAlias = _GuardrailChecksContentBlock_text


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailChecksContentBlock) -> dict:
    if "text" in value:
        return {"text": value["text"]}
    else:
        raise SerializationError("GuardrailChecksContentBlock: no variant present")


def deserialize_json(data: dict) -> GuardrailChecksContentBlock:
    if data.get("text") is not None:
        return {"text": data["text"]}
    else:
        raise DeserializationError(
            "GuardrailChecksContentBlock: no recognized variant key"
        )


def redact_sensitive(value: GuardrailChecksContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "text" in value:
        out["text"] = "*** Sensitive Data Redacted ***"
    return out
