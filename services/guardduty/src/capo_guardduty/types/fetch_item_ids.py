"""Generated from Smithy shape ``com.amazonaws.guardduty#FetchItemIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.fetch_item_id

FetchItemIds: TypeAlias = list["capo_guardduty.types.fetch_item_id.FetchItemId"]


# --- restJson1 ser/de ---
def serialize_json(value: FetchItemIds) -> list:
    return list(value)


def deserialize_json(data: list) -> FetchItemIds:
    return [item for item in data if item is not None]
