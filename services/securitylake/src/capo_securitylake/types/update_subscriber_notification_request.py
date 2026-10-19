"""Generated from Smithy shape ``com.amazonaws.securitylake#UpdateSubscriberNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_securitylake.types.notification_configuration
    import capo_securitylake.types.uuid


class UpdateSubscriberNotificationRequest(TypedDict, closed=True):
    subscriber_id: "capo_securitylake.types.uuid.UUID"
    """<p>The subscription ID for which the subscription notification is specified.</p>"""
    configuration: (
        "capo_securitylake.types.notification_configuration.NotificationConfiguration"
    )
    """<p>The configuration for subscriber notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateSubscriberNotificationRequest) -> dict:
    out: dict = {}
    import capo_securitylake.types.notification_configuration

    out["configuration"] = (
        capo_securitylake.types.notification_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateSubscriberNotificationRequest:
    out: UpdateSubscriberNotificationRequest = {}  # type: ignore[typeddict-item]
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
