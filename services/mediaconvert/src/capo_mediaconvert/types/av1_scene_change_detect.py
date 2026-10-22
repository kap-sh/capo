"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1SceneChangeDetect``."""

from typing import Literal, TypeAlias, cast

"""Optional. Use this setting to have the service insert I-frames at scene changes that it automatically detects. For AV1, scene change detection is disabled by default. Choose Enabled to insert I-frames at detected scene changes, which can improve video quality. If this output uses QVBR, you can instead choose Transition detection for further video quality improvement. For more information about QVBR, see https://docs.aws.amazon.com/console/mediaconvert/cbr-vbr-qvbr."""
Av1SceneChangeDetect: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "TRANSITION_DETECTION",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1SceneChangeDetect) -> str:
    return value


def deserialize_json(data: str) -> Av1SceneChangeDetect:
    return cast(Av1SceneChangeDetect, data)
