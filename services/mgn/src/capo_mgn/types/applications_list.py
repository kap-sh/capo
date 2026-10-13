"""Generated from Smithy shape ``com.amazonaws.mgn#ApplicationsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_mgn.types.application

ApplicationsList: TypeAlias = list["capo_mgn.types.application.Application"]


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationsList) -> list:
    import capo_mgn.types.application

    out: list = []
    for item in value:
        out.append(capo_mgn.types.application.serialize_json(item))
    return out


def deserialize_json(data: list) -> ApplicationsList:
    import capo_mgn.types.application

    out: ApplicationsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_mgn.types.application.deserialize_json(item))
    return out


def redact_sensitive(value: ApplicationsList) -> list[Any]:
    import capo_mgn.types.application

    return [capo_mgn.types.application.redact_sensitive(item) for item in value]
