"""Generated from Smithy shape ``com.amazonaws.billingconductor#CustomLineItemVersionList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_billingconductor.types.custom_line_item_version_list_element

CustomLineItemVersionList: TypeAlias = list[
    "capo_billingconductor.types.custom_line_item_version_list_element.CustomLineItemVersionListElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: CustomLineItemVersionList) -> list:
    import capo_billingconductor.types.custom_line_item_version_list_element

    out: list = []
    for item in value:
        out.append(
            capo_billingconductor.types.custom_line_item_version_list_element.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CustomLineItemVersionList:
    import capo_billingconductor.types.custom_line_item_version_list_element

    out: CustomLineItemVersionList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_billingconductor.types.custom_line_item_version_list_element.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: CustomLineItemVersionList) -> list[Any]:
    import capo_billingconductor.types.custom_line_item_version_list_element

    return [
        capo_billingconductor.types.custom_line_item_version_list_element.redact_sensitive(
            item
        )
        for item in value
    ]
