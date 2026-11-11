"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchCreateRelatedItemErrorEntryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.batch_create_related_item_error_entry

BatchCreateRelatedItemErrorEntryList: TypeAlias = list[
    "capo_connectcases.types.batch_create_related_item_error_entry.BatchCreateRelatedItemErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRelatedItemErrorEntryList) -> list:
    import capo_connectcases.types.batch_create_related_item_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.batch_create_related_item_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateRelatedItemErrorEntryList:
    import capo_connectcases.types.batch_create_related_item_error_entry

    out: BatchCreateRelatedItemErrorEntryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcases.types.batch_create_related_item_error_entry.deserialize_json(
                item
            )
        )
    return out
