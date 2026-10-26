"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError
from capo_bedrock_runtime.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_image_block
    import capo_bedrock_runtime.types.guardrail_text_block


class _GuardrailContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_runtime.types.guardrail_text_block.GuardrailTextBlock"


class _GuardrailContentBlock_image(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.guardrail_image_block.GuardrailImageBlock"


GuardrailContentBlock: TypeAlias = (
    _GuardrailContentBlock_text | _GuardrailContentBlock_image | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailContentBlock) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"GuardrailContentBlock: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "text" in value:
        import capo_bedrock_runtime.types.guardrail_text_block

        return {
            "text": capo_bedrock_runtime.types.guardrail_text_block.serialize_json(
                value["text"]
            )
        }
    elif "image" in value:
        import capo_bedrock_runtime.types.guardrail_image_block

        return {
            "image": capo_bedrock_runtime.types.guardrail_image_block.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("GuardrailContentBlock: no variant present")


def deserialize_json(data: dict) -> GuardrailContentBlock:
    if data.get("text") is not None:
        import capo_bedrock_runtime.types.guardrail_text_block

        return {
            "text": capo_bedrock_runtime.types.guardrail_text_block.deserialize_json(
                data["text"]
            )
        }
    elif data.get("image") is not None:
        import capo_bedrock_runtime.types.guardrail_image_block

        return {
            "image": capo_bedrock_runtime.types.guardrail_image_block.deserialize_json(
                data["image"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("GuardrailContentBlock: no recognized variant key")


def redact_sensitive(value: GuardrailContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image" in value:
        out["image"] = "*** Sensitive Data Redacted ***"
    return out
