"""Generated from Smithy shape ``com.amazonaws.deadline#EbsVolumeType``."""

from typing import Literal, TypeAlias, cast

"""The EBS volume type."""
EbsVolumeType: TypeAlias = Literal["gp3",]


# --- restJson1 ser/de ---
def serialize_json(value: EbsVolumeType) -> str:
    return value


def deserialize_json(data: str) -> EbsVolumeType:
    return cast(EbsVolumeType, data)
