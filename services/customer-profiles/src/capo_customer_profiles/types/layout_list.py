"""Generated from Smithy shape ``com.amazonaws.customerprofiles#LayoutList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.layout_item

LayoutList: TypeAlias = list["capo_customer_profiles.types.layout_item.LayoutItem"]


# --- restJson1 ser/de ---
def serialize_json(value: LayoutList) -> list:
    import capo_customer_profiles.types.layout_item

    out: list = []
    for item in value:
        out.append(capo_customer_profiles.types.layout_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> LayoutList:
    import capo_customer_profiles.types.layout_item

    out: LayoutList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_customer_profiles.types.layout_item.deserialize_json(item))
    return out


def redact_sensitive(value: LayoutList) -> list[Any]:
    import capo_customer_profiles.types.layout_item

    return [
        capo_customer_profiles.types.layout_item.redact_sensitive(item)
        for item in value
    ]
