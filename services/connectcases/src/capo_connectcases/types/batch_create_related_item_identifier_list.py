"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchCreateRelatedItemIdentifierList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.batch_create_related_item_identifier

BatchCreateRelatedItemIdentifierList: TypeAlias = list[
    "capo_connectcases.types.batch_create_related_item_identifier.BatchCreateRelatedItemIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchCreateRelatedItemIdentifierList) -> list:
    import capo_connectcases.types.batch_create_related_item_identifier

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.batch_create_related_item_identifier.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchCreateRelatedItemIdentifierList:
    import capo_connectcases.types.batch_create_related_item_identifier

    out: BatchCreateRelatedItemIdentifierList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcases.types.batch_create_related_item_identifier.deserialize_json(
                item
            )
        )
    return out
