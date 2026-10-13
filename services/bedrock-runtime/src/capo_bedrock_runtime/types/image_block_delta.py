"""Generated from Smithy shape ``com.amazonaws.bedrockruntime#ImageBlockDelta``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_runtime.types.error_block
    import capo_bedrock_runtime.types.image_source


class ImageBlockDelta(TypedDict, closed=True):
    source: NotRequired["capo_bedrock_runtime.types.image_source.ImageSource"]
    """<p>The incremental image source data for this delta event.</p>"""
    error: NotRequired["capo_bedrock_runtime.types.error_block.ErrorBlock"]
    """<p>Error information if this image delta could not be processed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageBlockDelta) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_bedrock_runtime.types.image_source

        out["source"] = capo_bedrock_runtime.types.image_source.serialize_json(
            value["source"]
        )
    if "error" in value:
        import capo_bedrock_runtime.types.error_block

        out["error"] = capo_bedrock_runtime.types.error_block.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> ImageBlockDelta:
    out: ImageBlockDelta = {}  # type: ignore[typeddict-item]
    if data.get("source") is not None:
        import capo_bedrock_runtime.types.image_source

        out["source"] = capo_bedrock_runtime.types.image_source.deserialize_json(
            data["source"]
        )
    if data.get("error") is not None:
        import capo_bedrock_runtime.types.error_block

        out["error"] = capo_bedrock_runtime.types.error_block.deserialize_json(
            data["error"]
        )
    return out


def redact_sensitive(value: ImageBlockDelta) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "source" in value:
        out["source"] = "*** Sensitive Data Redacted ***"
    if "error" in value:
        out["error"] = "*** Sensitive Data Redacted ***"
    return out
