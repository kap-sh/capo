"""Generated from Smithy shape ``com.amazonaws.s3tables#PartitionDateSource``."""

from typing import Literal, TypeAlias, cast

PartitionDateSource: TypeAlias = Literal[
    "EventTime",
    "DeliveryTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: PartitionDateSource) -> str:
    return value


def deserialize_json(data: str) -> PartitionDateSource:
    return cast(PartitionDateSource, data)
