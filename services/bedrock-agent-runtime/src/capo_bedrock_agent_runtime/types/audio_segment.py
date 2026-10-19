"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AudioSegment``."""

from typing_extensions import NotRequired, TypedDict


class AudioSegment(TypedDict, closed=True):
    s3_uri: "str"
    """<p>The S3 URI where this specific audio segment is stored in the multimodal storage destination.</p>"""
    transcription: NotRequired["str"]
    """<p>The text transcription of the audio segment content.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AudioSegment) -> dict:
    out: dict = {}
    out["s3Uri"] = value["s3_uri"]
    if "transcription" in value:
        out["transcription"] = value["transcription"]
    return out


def deserialize_json(data: dict) -> AudioSegment:
    out: AudioSegment = {}  # type: ignore[typeddict-item]
    if data.get("s3Uri") is not None:
        out["s3_uri"] = data["s3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("transcription") is not None:
        out["transcription"] = data["transcription"]
    return out
