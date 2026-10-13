"""Generated from Smithy shape ``com.amazonaws.customerprofiles#ProfileObjectList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_customer_profiles.types.list_profile_objects_item

ProfileObjectList: TypeAlias = list[
    "capo_customer_profiles.types.list_profile_objects_item.ListProfileObjectsItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: ProfileObjectList) -> list:
    import capo_customer_profiles.types.list_profile_objects_item

    out: list = []
    for item in value:
        out.append(
            capo_customer_profiles.types.list_profile_objects_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ProfileObjectList:
    import capo_customer_profiles.types.list_profile_objects_item

    out: ProfileObjectList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_customer_profiles.types.list_profile_objects_item.deserialize_json(
                item
            )
        )
    return out


def redact_sensitive(value: ProfileObjectList) -> list[Any]:
    import capo_customer_profiles.types.list_profile_objects_item

    return [
        capo_customer_profiles.types.list_profile_objects_item.redact_sensitive(item)
        for item in value
    ]
