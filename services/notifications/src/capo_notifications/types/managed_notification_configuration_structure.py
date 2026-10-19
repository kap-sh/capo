"""Generated from Smithy shape ``com.amazonaws.notifications#ManagedNotificationConfigurationStructure``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_configuration_description
    import capo_notifications.types.managed_notification_configuration_name
    import capo_notifications.types.managed_notification_configuration_os_arn


class ManagedNotificationConfigurationStructure(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The Amazon Resource Name (ARN) of the <code>ManagedNotificationConfiguration</code>.</p>"""
    name: "capo_notifications.types.managed_notification_configuration_name.ManagedNotificationConfigurationName"
    """<p>The name of the <code>ManagedNotificationConfiguration</code>.</p>"""
    description: "capo_notifications.types.managed_notification_configuration_description.ManagedNotificationConfigurationDescription"
    """<p>The description of the <code>ManagedNotificationConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ManagedNotificationConfigurationStructure) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> ManagedNotificationConfigurationStructure:
    out: ManagedNotificationConfigurationStructure = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    else:
        out["description"] = ""
    return out
