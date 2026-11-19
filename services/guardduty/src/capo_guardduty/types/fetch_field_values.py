"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchFieldValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_field_value

FetchFieldValues: TypeAlias = list[
    "capo_guardduty.types.fetch_field_value.FetchFieldValue"
]


# --- restJson1 ser/de ---
def serialize_json(value: FetchFieldValues) -> list:
    return list(value)


def deserialize_json(data: list) -> FetchFieldValues:
    return [item for item in data if item is not None]
