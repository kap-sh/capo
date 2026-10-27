"""Generated from Smithy shape ``com.amazonaws.medialive#H264AllowExplicitWeightedPrediction``."""

from typing import Literal, TypeAlias, cast

"""H264 Allow Explicit Weighted Prediction"""
H264AllowExplicitWeightedPrediction: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H264AllowExplicitWeightedPrediction) -> str:
    return value


def deserialize_json(data: str) -> H264AllowExplicitWeightedPrediction:
    return cast(H264AllowExplicitWeightedPrediction, data)
