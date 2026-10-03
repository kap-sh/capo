"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265CodecProfile``."""

from typing import Literal, TypeAlias, cast

"""Represents the Profile and Tier, per the HEVC (H.265) specification. Selections are grouped as [Profile] / [Tier], so "Main/High" represents Main Profile with High Tier. 4:2:2 profiles are only available with the HEVC 4:2:2 License."""
H265CodecProfile: TypeAlias = Literal[
    "MAIN_MAIN",
    "MAIN_HIGH",
    "MAIN10_MAIN",
    "MAIN10_HIGH",
    "MAIN_422_8BIT_MAIN",
    "MAIN_422_8BIT_HIGH",
    "MAIN_422_10BIT_MAIN",
    "MAIN_422_10BIT_HIGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265CodecProfile) -> str:
    return value


def deserialize_json(data: str) -> H265CodecProfile:
    return cast(H265CodecProfile, data)
