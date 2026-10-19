"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageBlockStart``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.image_format


class ImageBlockStart(TypedDict, closed=True):
    format: "capo_bedrock_runtime.types.image_format.ImageFormat"
    """<p>The format of the image data that will be streamed in subsequent delta events.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageBlockStart) -> dict:
    out: dict = {}
    import capo_bedrock_runtime.types.image_format

    out["format"] = capo_bedrock_runtime.types.image_format.serialize_json(
        value["format"]
    )
    return out


def deserialize_json(data: dict) -> ImageBlockStart:
    out: ImageBlockStart = {}  # type: ignore[typeddict-item]
    if data.get("format") is not None:
        import capo_bedrock_runtime.types.image_format

        out["format"] = capo_bedrock_runtime.types.image_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_bedrock_runtime.types.image_format.ImageFormat", ""
        )
    return out
