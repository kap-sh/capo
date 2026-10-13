"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InputImage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.byte_content_blob
    import capo_bedrock_agent_runtime.types.input_image_format


class InputImage(TypedDict, closed=True):
    format: "capo_bedrock_agent_runtime.types.input_image_format.InputImageFormat"
    """<p>The format of the input image. Supported formats include png, gif, jpeg, and webp.</p>"""
    inline_content: "capo_bedrock_agent_runtime.types.byte_content_blob.ByteContentBlob"
    """<p>The base64-encoded image data for inline image content. Maximum size is 5MB.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InputImage) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.input_image_format

    out["format"] = capo_bedrock_agent_runtime.types.input_image_format.serialize_json(
        value["format"]
    )
    import capo_bedrock_agent_runtime.types.byte_content_blob

    out["inlineContent"] = (
        capo_bedrock_agent_runtime.types.byte_content_blob.serialize_json(
            value["inline_content"]
        )
    )
    return out


def deserialize_json(data: dict) -> InputImage:
    out: InputImage = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_agent_runtime.types.input_image_format

        out["format"] = (
            capo_bedrock_agent_runtime.types.input_image_format.deserialize_json(
                data["format"]
            )
        )
    else:
        raise DeserializationError("InputImage.format required")
    if data.get("inlineContent") is not None:
        import capo_bedrock_agent_runtime.types.byte_content_blob

        out["inline_content"] = (
            capo_bedrock_agent_runtime.types.byte_content_blob.deserialize_json(
                data["inlineContent"]
            )
        )
    else:
        raise DeserializationError("InputImage.inline_content required")
    return out


def redact_sensitive(value: InputImage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline_content" in value:
        out["inline_content"] = "*** Sensitive Data Redacted ***"
    return out
