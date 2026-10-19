"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PropertyNotification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.property_notification_state
    import capo_iotsitewise.types.property_notification_topic


class PropertyNotification(TypedDict, closed=True):
    topic: (
        "capo_iotsitewise.types.property_notification_topic.PropertyNotificationTopic"
    )
    """<p>The MQTT topic to which IoT SiteWise publishes property value update notifications.</p>"""
    state: (
        "capo_iotsitewise.types.property_notification_state.PropertyNotificationState"
    )
    """<p>The current notification state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PropertyNotification) -> dict:
    out: dict = {}
    out["topic"] = value["topic"]
    import capo_iotsitewise.types.property_notification_state

    out["state"] = capo_iotsitewise.types.property_notification_state.serialize_json(
        value["state"]
    )
    return out


def deserialize_json(data: dict) -> PropertyNotification:
    out: PropertyNotification = {}  # type: ignore[typeddict-item]
    if data.get("topic") is not None:
        out["topic"] = data["topic"]
    else:
        out["topic"] = ""
    if data.get("state") is not None:
        import capo_iotsitewise.types.property_notification_state

        out["state"] = (
            capo_iotsitewise.types.property_notification_state.deserialize_json(
                data["state"]
            )
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_iotsitewise.types.property_notification_state.PropertyNotificationState",
            "",
        )
    return out
