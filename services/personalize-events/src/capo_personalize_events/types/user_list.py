"""Generated from Smithy shape ``com.amazonaws.personalizeevents#UserList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_personalize_events.types.user

UserList: TypeAlias = list["capo_personalize_events.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: UserList) -> list:
    import capo_personalize_events.types.user

    out: list = []
    for item in value:
        out.append(capo_personalize_events.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> UserList:
    import capo_personalize_events.types.user

    out: UserList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_personalize_events.types.user.deserialize_json(item))
    return out


def redact_sensitive(value: UserList) -> list[Any]:
    import capo_personalize_events.types.user

    return [capo_personalize_events.types.user.redact_sensitive(item) for item in value]
