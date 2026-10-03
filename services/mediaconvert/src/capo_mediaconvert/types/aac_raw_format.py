"""Generated from Smithy shape ``com.amazonaws.mediaconvert#AacRawFormat``."""

from typing import Literal, TypeAlias, cast

"""Enables LATM/LOAS AAC output. Note that if you use LATM/LOAS AAC in an output, you must choose "No container" for the output container."""
AacRawFormat: TypeAlias = Literal[
    "LATM_LOAS",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: AacRawFormat) -> str:
    return value


def deserialize_json(data: str) -> AacRawFormat:
    return cast(AacRawFormat, data)
