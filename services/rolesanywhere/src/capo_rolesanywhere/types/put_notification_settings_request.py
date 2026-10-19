"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#PutNotificationSettingsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_rolesanywhere.types.notification_settings
    import capo_rolesanywhere.types.uuid


class PutNotificationSettingsRequest(TypedDict, closed=True):
    trust_anchor_id: "capo_rolesanywhere.types.uuid.Uuid"
    """<p>The unique identifier of the trust anchor.</p>"""
    notification_settings: (
        "capo_rolesanywhere.types.notification_settings.NotificationSettings"
    )
    """<p>A list of notification settings to be associated to the trust anchor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutNotificationSettingsRequest) -> dict:
    out: dict = {}
    out["trustAnchorId"] = value["trust_anchor_id"]
    import capo_rolesanywhere.types.notification_settings

    out["notificationSettings"] = (
        capo_rolesanywhere.types.notification_settings.serialize_json(
            value["notification_settings"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutNotificationSettingsRequest:
    out: PutNotificationSettingsRequest = {}  # type: ignore[typeddict-item]
    if data.get("trustAnchorId") is not None:
        out["trust_anchor_id"] = data["trustAnchorId"]
    else:
        out["trust_anchor_id"] = ""
    if data.get("notificationSettings") is not None:
        import capo_rolesanywhere.types.notification_settings

        out["notification_settings"] = (
            capo_rolesanywhere.types.notification_settings.deserialize_json(
                data["notificationSettings"]
            )
        )
    else:
        out["notification_settings"] = []
    return out
