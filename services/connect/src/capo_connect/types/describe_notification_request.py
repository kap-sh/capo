"""Generated from Smithy shape ``com.amazonaws.connect#DescribeNotificationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.notification_id


class DescribeNotificationRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    notification_id: "capo_connect.types.notification_id.NotificationId"
    """<p>The unique identifier for the notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeNotificationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeNotificationRequest:
    out: DescribeNotificationRequest = {}  # type: ignore[typeddict-item]
    return out
