"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VideoMatrixCoefficients``."""

from typing import Literal, TypeAlias, cast

VideoMatrixCoefficients: TypeAlias = Literal[
    "IDENTITY",
    "BT709",
    "FCC",
    "BT470BG",
    "BT601",
    "SMPTE240M",
    "YCGCO",
    "BT2020_NCL",
    "BT2020_CL",
    "SMPTE2085",
    "CHROMATICITY_DERIVED_NCL",
    "CHROMATICITY_DERIVED_CL",
    "BT2100_ICTCP",
    "IPT_C2",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoMatrixCoefficients) -> str:
    return value


def deserialize_json(data: str) -> VideoMatrixCoefficients:
    return cast(VideoMatrixCoefficients, data)
