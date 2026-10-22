"""Generated from Smithy shape ``com.amazonaws.mediaconvert#Av1RateControlMode``."""

from typing import Literal, TypeAlias, cast

"""'With AV1 outputs, for rate control mode, MediaConvert supports quality-defined variable bitrate (QVBR) and constant bitrate (CBR). You can''t use VBR.'"""
Av1RateControlMode: TypeAlias = Literal[
    "CBR",
    "QVBR",
]


# --- restJson1 ser/de ---
def serialize_json(value: Av1RateControlMode) -> str:
    return value


def deserialize_json(data: str) -> Av1RateControlMode:
    return cast(Av1RateControlMode, data)
