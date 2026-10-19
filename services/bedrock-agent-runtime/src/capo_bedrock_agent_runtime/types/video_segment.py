"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#VideoSegment``."""

from typing_extensions import NotRequired, TypedDict


class VideoSegment(TypedDict, closed=True):
    s3_uri: "str"
    """<p>The S3 URI where this specific video segment is stored in the multimodal storage destination.</p>"""
    summary: NotRequired["str"]
    """<p>A text summary describing the content of the video segment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoSegment) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "summary" in value:
        out["summary"] = value["summary"]
    return out


def deserialize_json(data: dict) -> VideoSegment:
    out: VideoSegment = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("summary") is not None:
        out["summary"] = data["summary"]
    return out
