"""Generated from Smithy shape ``com.amazonaws.iotevents#NotificationAction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iot_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_events.types.email_configurations
    import capo_iot_events.types.notification_target_actions
    import capo_iot_events.types.sms_configurations


class NotificationAction(TypedDict, closed=True):
    action: (
        "capo_iot_events.types.notification_target_actions.NotificationTargetActions"
    )
    """<p>Specifies an AWS Lambda function to manage alarm notifications. You can create one or use the <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html">AWS Lambda function provided by AWS IoT Events</a>.</p>"""
    sms_configurations: NotRequired[
        "capo_iot_events.types.sms_configurations.SMSConfigurations"
    ]
    """<p>Contains the configuration information of SMS notifications.</p>"""
    email_configurations: NotRequired[
        "capo_iot_events.types.email_configurations.EmailConfigurations"
    ]
    """<p>Contains the configuration information of email notifications.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NotificationAction) -> dict:
    out: dict = {}
    import capo_iot_events.types.notification_target_actions

    out["action"] = capo_iot_events.types.notification_target_actions.serialize_json(
        value["action"]
    )
    if "sms_configurations" in value:
        import capo_iot_events.types.sms_configurations

        out["smsConfigurations"] = (
            capo_iot_events.types.sms_configurations.serialize_json(
                value["sms_configurations"]
            )
        )
    if "email_configurations" in value:
        import capo_iot_events.types.email_configurations

        out["emailConfigurations"] = (
            capo_iot_events.types.email_configurations.serialize_json(
                value["email_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> NotificationAction:
    out: NotificationAction = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_iot_events.types.notification_target_actions

        out["action"] = (
            capo_iot_events.types.notification_target_actions.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError("NotificationAction.action required")
    if data.get("smsConfigurations") is not None:
        import capo_iot_events.types.sms_configurations

        out["sms_configurations"] = (
            capo_iot_events.types.sms_configurations.deserialize_json(
                data["smsConfigurations"]
            )
        )
    if data.get("emailConfigurations") is not None:
        import capo_iot_events.types.email_configurations

        out["email_configurations"] = (
            capo_iot_events.types.email_configurations.deserialize_json(
                data["emailConfigurations"]
            )
        )
    return out
