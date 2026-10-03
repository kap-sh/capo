"""Generated from Smithy shape ``com.amazonaws.medialive#IFrameOnlyPlaylistType``."""

from typing import Literal, TypeAlias, cast

"""When set to "standard", an I-Frame only playlist will be written out for each video output in the output group. This I-Frame only playlist will contain byte range offsets pointing to the I-frame(s) in each segment."""
IFrameOnlyPlaylistType: TypeAlias = Literal[
    "DISABLED",
    "STANDARD",
]


# --- restJson1 ser/de ---
def serialize_json(value: IFrameOnlyPlaylistType) -> str:
    return value


def deserialize_json(data: str) -> IFrameOnlyPlaylistType:
    return cast(IFrameOnlyPlaylistType, data)
