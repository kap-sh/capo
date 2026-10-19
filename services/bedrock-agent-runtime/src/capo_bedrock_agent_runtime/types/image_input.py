"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.image_input_format
    import capo_bedrock_agent_runtime.types.image_input_source


class ImageInput(TypedDict, closed=True):
    format: "capo_bedrock_agent_runtime.types.image_input_format.ImageInputFormat"
    """<p>The type of image in the result.</p>"""
    source: "capo_bedrock_agent_runtime.types.image_input_source.ImageInputSource"
    """<p>The source of the image in the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageInput) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.image_input_format

    out["format"] = capo_bedrock_agent_runtime.types.image_input_format.serialize_json(
        value["format"]
    )
    import capo_bedrock_agent_runtime.types.image_input_source

    out["source"] = capo_bedrock_agent_runtime.types.image_input_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> ImageInput:
    out: ImageInput = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_agent_runtime.types.image_input_format

        out["format"] = (
            capo_bedrock_agent_runtime.types.image_input_format.deserialize_json(
                data["format"]
            )
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bedrock_agent_runtime.types.image_input_format.ImageInputFormat", ""
        )
    if data.get("source") is not None:
        import capo_bedrock_agent_runtime.types.image_input_source

        out["source"] = (
            capo_bedrock_agent_runtime.types.image_input_source.deserialize_json(
                data["source"]
            )
        )
    else:
        import capo_bedrock_agent_runtime.types._unknown

        out["source"] = capo_bedrock_agent_runtime.types._unknown.UnknownUnionMember("")
    return out
