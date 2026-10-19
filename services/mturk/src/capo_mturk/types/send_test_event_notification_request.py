"""Generated from Smithy shape ``com.amazonaws.mturk#SendTestEventNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mturk.types.event_type
    import capo_mturk.types.notification_specification


class SendTestEventNotificationRequest(TypedDict, closed=True):
    notification: (
        "capo_mturk.types.notification_specification.NotificationSpecification"
    )
    """<p> The notification specification to test. This value is identical to the value you would provide to the UpdateNotificationSettings operation when you establish the notification specification for a HIT type. </p>"""
    test_event_type: "capo_mturk.types.event_type.EventType"
    """<p> The event to simulate to test the notification specification. This event is included in the test message even if the notification specification does not include the event type. The notification specification does not filter out the test event. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SendTestEventNotificationRequest) -> dict:
    out: dict = {}
    import capo_mturk.types.notification_specification

    out["Notification"] = (
        capo_mturk.types.notification_specification.serialize_aws_json_1_1(
            value["notification"]
        )
    )
    import capo_mturk.types.event_type

    out["TestEventType"] = capo_mturk.types.event_type.serialize_aws_json_1_1(
        value["test_event_type"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SendTestEventNotificationRequest:
    out: SendTestEventNotificationRequest = {}  # type: ignore[typeddict-item]
    if data.get("Notification") is not None:
        import capo_mturk.types.notification_specification

        out["notification"] = (
            capo_mturk.types.notification_specification.deserialize_aws_json_1_1(
                data["Notification"]
            )
        )
    else:
        raise DeserializationError(
            "SendTestEventNotificationRequest.notification required"
        )
    if data.get("TestEventType") is not None:
        import capo_mturk.types.event_type

        out["test_event_type"] = capo_mturk.types.event_type.deserialize_aws_json_1_1(
            data["TestEventType"]
        )
    else:
        import typing

        out["test_event_type"] = typing.cast(
            "capo_mturk.types.event_type.EventType", ""
        )
    return out
