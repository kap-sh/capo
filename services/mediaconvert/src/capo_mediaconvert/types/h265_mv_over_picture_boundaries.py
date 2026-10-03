"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265MvOverPictureBoundaries``."""

from typing import Literal, TypeAlias, cast

"""If you are setting up the picture as a tile, you must set this to "disabled". In all other configurations, you typically enter "enabled"."""
H265MvOverPictureBoundaries: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265MvOverPictureBoundaries) -> str:
    return value


def deserialize_json(data: str) -> H265MvOverPictureBoundaries:
    return cast(H265MvOverPictureBoundaries, data)
