"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcDescriptiveVideoServiceFlag``."""

from typing import Literal, TypeAlias, cast

"""Specify whether to flag this audio track as descriptive video service (DVS) in your HLS parent manifest. When you choose Flag, MediaConvert includes the parameter CHARACTERISTICS="public.accessibility.describes-video" in the EXT-X-MEDIA entry for this track. When you keep the default choice, Don't flag, MediaConvert leaves this parameter out. The DVS flag can help with accessibility on Apple devices. For more information, see the Apple documentation."""
CmfcDescriptiveVideoServiceFlag: TypeAlias = Literal[
    "DONT_FLAG",
    "FLAG",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmfcDescriptiveVideoServiceFlag) -> str:
    return value


def deserialize_json(data: str) -> CmfcDescriptiveVideoServiceFlag:
    return cast(CmfcDescriptiveVideoServiceFlag, data)
