"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_directory_service_data.types.group

GroupList: TypeAlias = list["capo_directory_service_data.types.group.Group"]


# --- restJson1 ser/de ---
def serialize_json(value: GroupList) -> list:
    import capo_directory_service_data.types.group

    out: list = []
    for item in value:
        out.append(capo_directory_service_data.types.group.serialize_json(item))
    return out


def deserialize_json(data: list) -> GroupList:
    import capo_directory_service_data.types.group

    out: GroupList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_directory_service_data.types.group.deserialize_json(item))
    return out


def redact_sensitive(value: GroupList) -> list[Any]:
    import capo_directory_service_data.types.group

    return [
        capo_directory_service_data.types.group.redact_sensitive(item) for item in value
    ]
