"""Generated from Smithy shape ``com.amazonaws.amplify#Apps``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.app

Apps: TypeAlias = list["capo_amplify.types.app.App"]


# --- restJson1 ser/de ---
def serialize_json(value: Apps) -> list:
    import capo_amplify.types.app

    out: list = []
    for item in value:
        out.append(capo_amplify.types.app.serialize_json(item))
    return out


def deserialize_json(data: list) -> Apps:
    import capo_amplify.types.app

    out: Apps = []
    for item in data:
        if item is None:
            continue
        out.append(capo_amplify.types.app.deserialize_json(item))
    return out


def redact_sensitive(value: Apps) -> list[Any]:
    import capo_amplify.types.app

    return [capo_amplify.types.app.redact_sensitive(item) for item in value]
