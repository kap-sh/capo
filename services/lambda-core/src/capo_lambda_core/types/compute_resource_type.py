"""Generated from Smithy shape ``com.amazonaws.lambdacore#ComputeResourceType``."""

from typing import Literal, TypeAlias, cast

"""<p>The type of Lambda compute resource that can use a network connector.</p>"""
ComputeResourceType: TypeAlias = Literal[
    "MicroVm",
    "WebFunction",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComputeResourceType) -> str:
    return value


def deserialize_json(data: str) -> ComputeResourceType:
    return cast(ComputeResourceType, data)
