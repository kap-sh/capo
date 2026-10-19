"""Generated from Smithy shape ``com.amazonaws.connect#CreateNotificationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.notification_id


class CreateNotificationResponse(TypedDict, closed=True):
    notification_id: "capo_connect.types.notification_id.NotificationId"
    """<p>The unique identifier assigned to the created notification.</p>"""
    notification_arn: "capo_connect.types.arn.ARN"
    """<p>The Amazon Resource Name (ARN) of the created notification.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationResponse) -> dict:
    out: dict = {}
    out["NotificationId"] = value["notification_id"]
    out["NotificationArn"] = value["notification_arn"]
    return out


def deserialize_json(data: dict) -> CreateNotificationResponse:
    out: CreateNotificationResponse = {}  # type: ignore[typeddict-item]
    if data.get("NotificationId") is not None:
        out["notification_id"] = data["NotificationId"]
    else:
        out["notification_id"] = ""
    if data.get("NotificationArn") is not None:
        out["notification_arn"] = data["NotificationArn"]
    else:
        out["notification_arn"] = ""
    return out
