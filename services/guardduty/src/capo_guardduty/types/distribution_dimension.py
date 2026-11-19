"""Generated from Smithy shape ``com.amazonaws.guardduty#DistributionDimension``."""

from typing import Literal, TypeAlias, cast

DistributionDimension: TypeAlias = Literal[
    "SEVERITY",
    "TYPE",
    "RESOURCE",
    "ATTACK_VECTOR",
    "ARCHIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: DistributionDimension) -> str:
    return value


def deserialize_json(data: str) -> DistributionDimension:
    return cast(DistributionDimension, data)
