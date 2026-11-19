"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TagFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_observabilityadmin.types.tag_filter_value

TagFilterValues: TypeAlias = list[
    "capo_observabilityadmin.types.tag_filter_value.TagFilterValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: TagFilterValues) -> list:
    return list(value)


def deserialize_json(data: list) -> TagFilterValues:
    return [item for item in data if item is not None]
