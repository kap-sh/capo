"""Generated from Smithy shape ``com.amazonaws.notifications#DisassociateChannelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.channel_arn
    import capo_notifications.types.notification_configuration_arn


class DisassociateChannelRequest(TypedDict, closed=True):
    arn: "capo_notifications.types.channel_arn.ChannelArn"
    """<p>The Amazon Resource Name (ARN) of the Channel to disassociate.</p>"""
    notification_configuration_arn: "capo_notifications.types.notification_configuration_arn.NotificationConfigurationArn"
    """<p>The ARN of the <code>NotificationConfiguration</code> to disassociate.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateChannelRequest) -> dict:
    out: dict = {}
    out["notificationConfigurationArn"] = value["notification_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DisassociateChannelRequest:
    out: DisassociateChannelRequest = {}  # type: ignore[typeddict-item]
    if data.get("notificationConfigurationArn") is not None:
        out["notification_configuration_arn"] = data["notificationConfigurationArn"]
    else:
        out["notification_configuration_arn"] = ""
    return out
