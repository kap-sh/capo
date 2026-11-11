"""Generated from Smithy shape ``com.amazonaws.mediaconvert#ElementalInferenceFeature``."""

from typing import Literal, TypeAlias, cast

"""Elemental Inference feature."""
ElementalInferenceFeature: TypeAlias = Literal[
    "SMART_CROP",
    "SMART_SUBTITLE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ElementalInferenceFeature) -> str:
    return value


def deserialize_json(data: str) -> ElementalInferenceFeature:
    return cast(ElementalInferenceFeature, data)
