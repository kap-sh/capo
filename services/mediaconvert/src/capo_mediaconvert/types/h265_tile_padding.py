"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265TilePadding``."""

from typing import Literal, TypeAlias, cast

"""Set to "padded" to force MediaConvert to add padding to the frame, to obtain a frame that is a whole multiple of the tile size. If you are setting up the picture as a tile, you must enter "padded". In all other configurations, you typically enter "none"."""
H265TilePadding: TypeAlias = Literal[
    "NONE",
    "PADDED",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265TilePadding) -> str:
    return value


def deserialize_json(data: str) -> H265TilePadding:
    return cast(H265TilePadding, data)
