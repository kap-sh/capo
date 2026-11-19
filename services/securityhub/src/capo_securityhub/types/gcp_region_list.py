"""Generated from Smithy shape ``com.amazonaws.securityhub#GcpRegionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.non_empty_string

GcpRegionList: TypeAlias = list[
    "capo_securityhub.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: GcpRegionList) -> list:
    return list(value)


def deserialize_json(data: list) -> GcpRegionList:
    return [item for item in data if item is not None]
