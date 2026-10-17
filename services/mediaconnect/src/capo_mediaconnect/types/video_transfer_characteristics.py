"""Generated from Smithy shape ``com.amazonaws.mediaconnect#VideoTransferCharacteristics``."""

from typing import Literal, TypeAlias, cast

VideoTransferCharacteristics: TypeAlias = Literal[
    "BT709",
    "BT470M",
    "BT470BG",
    "BT601",
    "SMPTE240M",
    "LINEAR",
    "LOG100",
    "LOG316",
    "IEC61966_2_4",
    "BT1361_ECG",
    "IEC61966_2_1",
    "BT2020_10",
    "BT2020_12",
    "BT2100_PQ",
    "SMPTE428",
    "BT2100_HLG",
]


# --- restJson1 ser/de ---
def serialize_json(value: VideoTransferCharacteristics) -> str:
    return value


def deserialize_json(data: str) -> VideoTransferCharacteristics:
    return cast(VideoTransferCharacteristics, data)
