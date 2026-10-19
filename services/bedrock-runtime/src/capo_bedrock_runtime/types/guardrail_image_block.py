"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailImageBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_image_format
    import capo_bedrock_runtime.types.guardrail_image_source


class GuardrailImageBlock(TypedDict, closed=True):
    format: "capo_bedrock_runtime.types.guardrail_image_format.GuardrailImageFormat"
    """<p>The format details for the file type of the image blocked by the guardrail.</p>"""
    source: "capo_bedrock_runtime.types.guardrail_image_source.GuardrailImageSource"
    """<p>The image source (image bytes) details of the image blocked by the guardrail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailImageBlock) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_image_format

    out["format"] = capo_bedrock_runtime.types.guardrail_image_format.serialize_json(
        value["format"]
    )
    import capo_bedrock_runtime.types.guardrail_image_source

    out["source"] = capo_bedrock_runtime.types.guardrail_image_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> GuardrailImageBlock:
    out: GuardrailImageBlock = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_runtime.types.guardrail_image_format

        out["format"] = (
            capo_bedrock_runtime.types.guardrail_image_format.deserialize_json(
                data["format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_image_format.GuardrailImageFormat", ""
        )
    if data.get("source") is not None:
        import capo_bedrock_runtime.types.guardrail_image_source

        out["source"] = (
            capo_bedrock_runtime.types.guardrail_image_source.deserialize_json(
                data["source"]
            )
        )
    else:
        import capo_bedrock_runtime.types._unknown

        out["source"] = capo_bedrock_runtime.types._unknown.UnknownUnionMember("")
    return out
