"""Generated from Smithy shape ``com.amazonaws.medialive#PerceptualFilterStrength``."""

from typing import Literal, TypeAlias, cast

"""Perceptual Filter Strength"""
PerceptualFilterStrength: TypeAlias = Literal[
    "STRENGTH_1",
    "STRENGTH_2",
]


# --- restJson1 ser/de ---
def serialize_json(value: PerceptualFilterStrength) -> str:
    return value


def deserialize_json(data: str) -> PerceptualFilterStrength:
    return cast(PerceptualFilterStrength, data)
