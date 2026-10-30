"""Generated from Smithy shape ``com.amazonaws.imagebuilder#ImageScanningType``."""

from typing import Literal, TypeAlias, cast

ImageScanningType: TypeAlias = Literal[
    "TEST_INSTANCE_CVE",
    "ON_DEMAND_AMI_CVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ImageScanningType) -> str:
    return value


def deserialize_json(data: str) -> ImageScanningType:
    return cast(ImageScanningType, data)
