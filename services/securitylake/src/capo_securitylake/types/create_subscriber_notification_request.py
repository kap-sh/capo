"""Generated from Smithy shape ``com.amazonaws.securitylake#CreateSubscriberNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.notification_configuration
    import capo_securitylake.types.uuid


class CreateSubscriberNotificationRequest(TypedDict, closed=True):
    subscriber_id: "capo_securitylake.types.uuid.UUID"
    """<p>The subscriber ID for the notification subscription.</p>"""
    configuration: (
        "capo_securitylake.types.notification_configuration.NotificationConfiguration"
    )
    """<p>Specify the configuration using which you want to create the subscriber notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSubscriberNotificationRequest) -> dict:
    out: dict = {}
    import capo_securitylake.types.notification_configuration

    out["configuration"] = (
        capo_securitylake.types.notification_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> CreateSubscriberNotificationRequest:
    out: CreateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("configuration") is not None:
        import capo_securitylake.types.notification_configuration

        out["configuration"] = (
            capo_securitylake.types.notification_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        import capo_securitylake.types._unknown

        out["configuration"] = capo_securitylake.types._unknown.UnknownUnionMember("")
    return out
