"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VideoColorimetry``."""

from typing import Literal, TypeAlias, cast

VideoColorimetry: TypeAlias = Literal[
    "BT709",
    "BT470M",
    "BT470BG",
    "BT601",
    "SMPTE240M",
    "GENERIC_FILM",
    "BT2020",
    "SMPTE428",
    "SMPTE431",
    "SMPTE432",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoColorimetry) -> str:
    return value


def deserialize_json(data: str) -> VideoColorimetry:
    return cast(VideoColorimetry, data)
