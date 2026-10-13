"""Generated from Smithy shape ``com.amazonaws.appfabric#UserAccessResultsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_appfabric.types.user_access_result_item

UserAccessResultsList: TypeAlias = list[
    "capo_appfabric.types.user_access_result_item.UserAccessResultItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: UserAccessResultsList) -> list:
    import capo_appfabric.types.user_access_result_item

    out: list = []
    for item in value:
        out.append(capo_appfabric.types.user_access_result_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserAccessResultsList:
    import capo_appfabric.types.user_access_result_item

    out: UserAccessResultsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_appfabric.types.user_access_result_item.deserialize_json(item))
    return out


def redact_sensitive(value: UserAccessResultsList) -> list[Any]:
    import capo_appfabric.types.user_access_result_item

    return [
        capo_appfabric.types.user_access_result_item.redact_sensitive(item)
        for item in value
    ]
