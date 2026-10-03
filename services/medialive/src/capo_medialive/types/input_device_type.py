"""Generated from Smithy shape ``com.amazonaws.medialive#InputDeviceType``."""

from typing import Literal, TypeAlias, cast

"""The type of the input device. For an AWS Elemental Link device that outputs resolutions up to 1080, choose "HD"."""
InputDeviceType: TypeAlias = Literal[
    "HD",
    "UHD",
]


# --- restJson1 ser/de ---
def serialize_json(value: InputDeviceType) -> str:
    return value


def deserialize_json(data: str) -> InputDeviceType:
    return cast(InputDeviceType, data)
