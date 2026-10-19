"""Generated from Smithy shape ``com.amazonaws.bedrockagent#VideoSegmentationConfiguration``."""

from typing_extensions import TypedDict


class VideoSegmentationConfiguration(TypedDict, closed=True):
    fixed_length_duration: "int"
    """<p>The duration in seconds for each video segment. Video files will be divided into chunks of this length for processing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VideoSegmentationConfiguration) -> dict:
    out: dict = {}
    out["fixedLengthDuration"] = value["fixed_length_duration"]
    return out


def deserialize_json(data: dict) -> VideoSegmentationConfiguration:
    out: VideoSegmentationConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fixedLengthDuration") is not None:
        out["fixed_length_duration"] = data["fixedLengthDuration"]
    else:
        out["fixed_length_duration"] = 0
    return out
