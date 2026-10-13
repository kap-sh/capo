"""Generated from Smithy shape ``com.amazonaws.wickr#Users``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_wickr.types.user

Users: TypeAlias = list["capo_wickr.types.user.User"]


# --- restJson1 ser/de ---
def serialize_json(value: Users) -> list:
    import capo_wickr.types.user

    out: list = []
    for item in value:
        out.append(capo_wickr.types.user.serialize_json(item))
    return out


def deserialize_json(data: list) -> Users:
    import capo_wickr.types.user

    out: Users = []
    for item in data:
        if item is None:
            continue
        out.append(capo_wickr.types.user.deserialize_json(item))
    return out


def redact_sensitive(value: Users) -> list[Any]:
    import capo_wickr.types.user

    return [capo_wickr.types.user.redact_sensitive(item) for item in value]
