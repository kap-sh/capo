"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#VideoBlock``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.video_format
    import capo_bedrock_runtime.types.video_source


class VideoBlock(TypedDict, closed=True):
    format: "capo_bedrock_runtime.types.video_format.VideoFormat"
    """<p>The block's format.</p>"""
    source: "capo_bedrock_runtime.types.video_source.VideoSource"
    """<p>The block's source.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoBlock) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.video_format

    out["format"] = capo_bedrock_runtime.types.video_format.serialize_json(
        value["format"]
    )
    import capo_bedrock_runtime.types.video_source

    out["source"] = capo_bedrock_runtime.types.video_source.serialize_json(
        value["source"]
    )
    return out


def deserialize_json(data: dict) -> VideoBlock:
    out: VideoBlock = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_runtime.types.video_format

        out["format"] = capo_bedrock_runtime.types.video_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bedrock_runtime.types.video_format.VideoFormat", ""
        )
    if data.get("source") is not None:
        import capo_bedrock_runtime.types.video_source

        out["source"] = capo_bedrock_runtime.types.video_source.deserialize_json(
            data["source"]
        )
    else:
        import capo_bedrock_runtime.types._unknown

        out["source"] = capo_bedrock_runtime.types._unknown.UnknownUnionMember("")
    return out
