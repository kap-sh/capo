"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseContentBlock``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock_runtime.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_converse_image_block
    import capo_bedrock_runtime.types.guardrail_converse_text_block


class _GuardrailConverseContentBlock_text(TypedDict, closed=True):
    text: "capo_bedrock_runtime.types.guardrail_converse_text_block.GuardrailConverseTextBlock"


class _GuardrailConverseContentBlock_image(TypedDict, closed=True):
    image: "capo_bedrock_runtime.types.guardrail_converse_image_block.GuardrailConverseImageBlock"


GuardrailConverseContentBlock: TypeAlias = (
    _GuardrailConverseContentBlock_text | _GuardrailConverseContentBlock_image
)


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseContentBlock) -> dict:
    if "text" in value:
        import capo_bedrock_runtime.types.guardrail_converse_text_block

        return {
            "text": capo_bedrock_runtime.types.guardrail_converse_text_block.serialize_json(
                value["text"]
            )
        }
    elif "image" in value:
        import capo_bedrock_runtime.types.guardrail_converse_image_block

        return {
            "image": capo_bedrock_runtime.types.guardrail_converse_image_block.serialize_json(
                value["image"]
            )
        }
    else:
        raise SerializationError("GuardrailConverseContentBlock: no variant present")


def deserialize_json(data: dict) -> GuardrailConverseContentBlock:
    if data.get("text") is not None:
        import capo_bedrock_runtime.types.guardrail_converse_text_block

        return {
            "text": capo_bedrock_runtime.types.guardrail_converse_text_block.deserialize_json(
                data["text"]
            )
        }
    elif data.get("image") is not None:
        import capo_bedrock_runtime.types.guardrail_converse_image_block

        return {
            "image": capo_bedrock_runtime.types.guardrail_converse_image_block.deserialize_json(
                data["image"]
            )
        }
    else:
        raise DeserializationError(
            "GuardrailConverseContentBlock: no recognized variant key"
        )


def redact_sensitive(value: GuardrailConverseContentBlock) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "image" in value:
        out["image"] = "*** Sensitive Data Redacted ***"
    return out
