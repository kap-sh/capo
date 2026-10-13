"""Generated from Smithy shape ``com.amazonaws.connectcases#RelatedItemFilterList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_connectcases.types.related_item_type_filter

RelatedItemFilterList: TypeAlias = list[
    "capo_connectcases.types.related_item_type_filter.RelatedItemTypeFilter"
]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedItemFilterList) -> list:
    import capo_connectcases.types.related_item_type_filter

    out: list = []
    for item in value:
        out.append(
            capo_connectcases.types.related_item_type_filter.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> RelatedItemFilterList:
    import capo_connectcases.types.related_item_type_filter

    out: RelatedItemFilterList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_connectcases.types.related_item_type_filter.deserialize_json(item)
        )
    return out


def redact_sensitive(value: RelatedItemFilterList) -> list[Any]:
    import capo_connectcases.types.related_item_type_filter

    return [
        capo_connectcases.types.related_item_type_filter.redact_sensitive(item)
        for item in value
    ]
