"""Generated from Smithy shape ``com.amazonaws.medialive#MediaPackageV2CaptionLanguageSetting``."""

from typing import Literal, TypeAlias, cast

"""Media Package V2 Caption Language Setting"""
MediaPackageV2CaptionLanguageSetting: TypeAlias = Literal[
    "AUTO",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MediaPackageV2CaptionLanguageSetting) -> str:
    return value


def deserialize_json(data: str) -> MediaPackageV2CaptionLanguageSetting:
    return cast(MediaPackageV2CaptionLanguageSetting, data)
