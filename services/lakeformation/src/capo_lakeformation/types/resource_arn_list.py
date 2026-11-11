"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceArnList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.resource_arn_string

ResourceArnList: TypeAlias = list[
    "capo_lakeformation.types.resource_arn_string.ResourceArnString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceArnList) -> list:
    return list(value)


def deserialize_json(data: list) -> ResourceArnList:
    return [item for item in data if item is not None]
