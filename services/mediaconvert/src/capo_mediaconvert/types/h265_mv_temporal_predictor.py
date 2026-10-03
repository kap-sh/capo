"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265MvTemporalPredictor``."""

from typing import Literal, TypeAlias, cast

"""If you are setting up the picture as a tile, you must set this to "disabled". In other configurations, you typically enter "enabled"."""
H265MvTemporalPredictor: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265MvTemporalPredictor) -> str:
    return value


def deserialize_json(data: str) -> H265MvTemporalPredictor:
    return cast(H265MvTemporalPredictor, data)
