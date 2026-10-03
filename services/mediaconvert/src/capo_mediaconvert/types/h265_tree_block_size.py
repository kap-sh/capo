"""Generated from Smithy shape ``com.amazonaws.mediaconvert#H265TreeBlockSize``."""

from typing import Literal, TypeAlias, cast

"""Select the tree block size used for encoding. If you enter "auto", the encoder will pick the best size. If you are setting up the picture as a tile, you must set this to 32x32. In all other configurations, you typically enter "auto"."""
H265TreeBlockSize: TypeAlias = Literal[
    "AUTO",
    "TREE_SIZE_32X32",
]


# --- restJson1 ser/de ---
def serialize_json(value: H265TreeBlockSize) -> str:
    return value


def deserialize_json(data: str) -> H265TreeBlockSize:
    return cast(H265TreeBlockSize, data)
