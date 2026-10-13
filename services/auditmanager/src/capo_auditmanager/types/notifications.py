"""Generated from Smithy shape ``com.amazonaws.auditmanager#Notifications``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_auditmanager.types.notification

Notifications: TypeAlias = list["capo_auditmanager.types.notification.Notification"]


# --- restJson1 ser/de ---
def serialize_json(value: Notifications) -> list:
    import capo_auditmanager.types.notification

    out: list = []
    for item in value:
        out.append(capo_auditmanager.types.notification.serialize_json(item))
    return out


def deserialize_json(data: list) -> Notifications:
    import capo_auditmanager.types.notification

    out: Notifications = []
    for item in data:
        if item is None:
            continue
        out.append(capo_auditmanager.types.notification.deserialize_json(item))
    return out


def redact_sensitive(value: Notifications) -> list[Any]:
    import capo_auditmanager.types.notification

    return [
        capo_auditmanager.types.notification.redact_sensitive(item) for item in value
    ]
