"""Generated from Smithy shape ``com.amazonaws.lambdacore#ComputeResourceType``."""

from typing import Literal, TypeAlias, cast

ComputeResourceType: TypeAlias = Literal["MicroVm",]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeResourceType) -> str:
    return value


def deserialize_json(data: str) -> ComputeResourceType:
    return cast(ComputeResourceType, data)
