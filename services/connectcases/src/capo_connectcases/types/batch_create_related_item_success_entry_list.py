"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchCreateRelatedItemSuccessEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.batch_create_related_item_success_entry

BatchCreateRelatedItemSuccessEntryList: TypeAlias = list[
    "capo_connectcases.types.batch_create_related_item_success_entry.BatchCreateRelatedItemSuccessEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRelatedItemSuccessEntryList) -> list:
    import capo_connectcases.types.batch_create_related_item_success_entry

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.batch_create_related_item_success_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateRelatedItemSuccessEntryList:
    import capo_connectcases.types.batch_create_related_item_success_entry

    out: BatchCreateRelatedItemSuccessEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcases.types.batch_create_related_item_success_entry.deserialize_json(
                item
            )
        )
    return out
