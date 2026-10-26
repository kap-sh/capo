"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ImageBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.image_format
    import capo_bedrock_agent_runtime.types.image_source


class ImageBlock(TypedDict, closed=True):
    format: "capo_bedrock_agent_runtime.types.image_format.ImageFormat"
    """<p>The format of the image.</p>"""
    source: "capo_bedrock_agent_runtime.types.image_source.ImageSource"
    """<p>The source for the image.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageBlock) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.image_format

    out["format"] = capo_bedrock_agent_runtime.types.image_format.serialize_json(
        value["format"]
    )
    import capo_bedrock_agent_runtime.types.image_source

    out["source"] = capo_bedrock_agent_runtime.types.image_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> ImageBlock:
    out: ImageBlock = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_agent_runtime.types.image_format

        out["format"] = capo_bedrock_agent_runtime.types.image_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bedrock_agent_runtime.types.image_format.ImageFormat", ""
        )
    if data.get("source") is not None:
        import capo_bedrock_agent_runtime.types.image_source

        out["source"] = capo_bedrock_agent_runtime.types.image_source.deserialize_json(
            data["source"]
        )
    else:
        out["source"] = {"$unknown": {"name": ""}}
    return out
