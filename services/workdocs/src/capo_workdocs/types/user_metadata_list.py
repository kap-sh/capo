"""Generated from Smithy shape ``com.amazonaws.workdocs#UserMetadataList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_workdocs.types.user_metadata

UserMetadataList: TypeAlias = list["capo_workdocs.types.user_metadata.UserMetadata"]


# --- restJson1 ser/de ---
def serialize_json(value: UserMetadataList) -> list:
    import capo_workdocs.types.user_metadata

    out: list = []
    for item in value:
        out.append(capo_workdocs.types.user_metadata.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserMetadataList:
    import capo_workdocs.types.user_metadata

    out: UserMetadataList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_workdocs.types.user_metadata.deserialize_json(item))
    return out


def redact_sensitive(value: UserMetadataList) -> list[Any]:
    import capo_workdocs.types.user_metadata

    return [capo_workdocs.types.user_metadata.redact_sensitive(item) for item in value]
