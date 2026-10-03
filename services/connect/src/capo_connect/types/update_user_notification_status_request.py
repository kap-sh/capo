"""Generated from Smithy shape ``com.amazonaws.connect#UpdateUserNotificationStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.notification_id
    import capo_connect.types.notification_status
    import capo_connect.types.region_name
    import capo_connect.types.timestamp
    import capo_connect.types.user_id


class UpdateUserNotificationStatusRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    notification_id: "capo_connect.types.notification_id.NotificationId"
    """<p>The unique identifier for the notification.</p>"""
    user_id: "capo_connect.types.user_id.UserId"
    """<p>The identifier of the user whose notification status is being updated.</p>"""
    status: "capo_connect.types.notification_status.NotificationStatus"
    """<p>The new status for the notification. Valid values are READ, UNREAD, and HIDDEN.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the notification status was last modified. Used for cross-region replication and optimistic locking.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The AWS Region where the notification status was last modified. Used for cross-region replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateUserNotificationStatusRequest) -> dict:
    out: dict = {}
    import capo_connect.types.notification_status

    out["Status"] = capo_connect.types.notification_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> UpdateUserNotificationStatusRequest:
    out: UpdateUserNotificationStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        import capo_connect.types.notification_status

        out["status"] = capo_connect.types.notification_status.deserialize_json(
            data["Status"]
        )
    else:
        raise DeserializationError(
            "UpdateUserNotificationStatusRequest.status required"
        )
    return out
