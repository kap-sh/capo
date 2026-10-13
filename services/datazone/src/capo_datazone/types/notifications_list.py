"""Generated from Smithy shape ``com.amazonaws.datazone#NotificationsList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_datazone.types.notification_output

NotificationsList: TypeAlias = list[
    "capo_datazone.types.notification_output.NotificationOutput"
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationsList) -> list:
    import capo_datazone.types.notification_output

    out: list = []
    for item in value:
        out.append(capo_datazone.types.notification_output.serialize_json(item))
    return out


def deserialize_json(data: list) -> NotificationsList:
    import capo_datazone.types.notification_output

    out: NotificationsList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_datazone.types.notification_output.deserialize_json(item))
    return out


def redact_sensitive(value: NotificationsList) -> list[Any]:
    import capo_datazone.types.notification_output

    return [
        capo_datazone.types.notification_output.redact_sensitive(item) for item in value
    ]
