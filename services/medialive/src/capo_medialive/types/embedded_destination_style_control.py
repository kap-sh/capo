"""Generated from Smithy shape ``com.amazonaws.medialive#EmbeddedDestinationStyleControl``."""

from typing import Literal, TypeAlias, cast

"""Controls the source of position and style information for embedded outputs. - "passthrough": Carry the caption position and style from the source captions. When the source captions are embedded, SCTE-20, or ancillary, the position and style are preserved exactly. When the source captions are another format, the position and any supported style are carried over. - "manual": Use the position specified in the destination's position field."""
EmbeddedDestinationStyleControl: TypeAlias = Literal[
    "MANUAL",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: EmbeddedDestinationStyleControl) -> str:
    return value


def deserialize_json(data: str) -> EmbeddedDestinationStyleControl:
    return cast(EmbeddedDestinationStyleControl, data)
