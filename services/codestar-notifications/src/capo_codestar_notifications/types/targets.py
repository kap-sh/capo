"""Generated from Smithy shape ``com.amazonaws.codestarnotifications#Targets``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_codestar_notifications.types.target

Targets: TypeAlias = list["capo_codestar_notifications.types.target.Target"]


# --- restJson1 ser/de ---
def serialize_json(value: Targets) -> list:
    import capo_codestar_notifications.types.target

    out: list = []
    for item in value:
        out.append(capo_codestar_notifications.types.target.serialize_json(item))
    return out


def deserialize_json(data: list) -> Targets:
    import capo_codestar_notifications.types.target

    out: Targets = []
    for item in data:
        if item is None:
            continue
        out.append(capo_codestar_notifications.types.target.deserialize_json(item))
    return out


def redact_sensitive(value: Targets) -> list[Any]:
    import capo_codestar_notifications.types.target

    return [
        capo_codestar_notifications.types.target.redact_sensitive(item)
        for item in value
    ]
