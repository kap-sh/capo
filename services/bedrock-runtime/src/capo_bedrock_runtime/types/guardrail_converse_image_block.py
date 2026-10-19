"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#GuardrailConverseImageBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.guardrail_converse_image_format
    import capo_bedrock_runtime.types.guardrail_converse_image_source


class GuardrailConverseImageBlock(TypedDict, closed=True):
    format: "capo_bedrock_runtime.types.guardrail_converse_image_format.GuardrailConverseImageFormat"
    """<p>The format details for the image type of the guardrail converse image block.</p>"""
    source: "capo_bedrock_runtime.types.guardrail_converse_image_source.GuardrailConverseImageSource"
    """<p>The image source (image bytes) of the guardrail converse image block.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GuardrailConverseImageBlock) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.guardrail_converse_image_format

    out["format"] = (
        capo_bedrock_runtime.types.guardrail_converse_image_format.serialize_json(
            value["format"]
        )
    )
    import capo_bedrock_runtime.types.guardrail_converse_image_source

    out["source"] = (
        capo_bedrock_runtime.types.guardrail_converse_image_source.serialize_json(
            value["source"]
        )
    )
    return out


def deserialize_json(data: dict) -> GuardrailConverseImageBlock:
    out: GuardrailConverseImageBlock = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_runtime.types.guardrail_converse_image_format

        out["format"] = (
            capo_bedrock_runtime.types.guardrail_converse_image_format.deserialize_json(
                data["format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bedrock_runtime.types.guardrail_converse_image_format.GuardrailConverseImageFormat",
            "",
        )
    if data.get("source") is not None:
        import capo_bedrock_runtime.types.guardrail_converse_image_source

        out["source"] = (
            capo_bedrock_runtime.types.guardrail_converse_image_source.deserialize_json(
                data["source"]
            )
        )
    else:
        import capo_bedrock_runtime.types._unknown

        out["source"] = capo_bedrock_runtime.types._unknown.UnknownUnionMember("")
    return out
