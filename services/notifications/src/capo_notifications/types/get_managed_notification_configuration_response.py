"""Generated from Smithy shape ``com.amazonaws.notifications#GetManagedNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_notifications.types.managed_notification_configuration_description
    import capo_notifications.types.managed_notification_configuration_name
    import capo_notifications.types.managed_notification_configuration_os_arn


class GetManagedNotificationConfigurationResponse(TypedDict, closed=True):
    arn: "capo_notifications.types.managed_notification_configuration_os_arn.ManagedNotificationConfigurationOsArn"
    """<p>The ARN of the <code>ManagedNotificationConfiguration</code> resource.</p>"""
    name: "capo_notifications.types.managed_notification_configuration_name.ManagedNotificationConfigurationName"
    """<p>The name of the <code>ManagedNotificationConfiguration</code>.</p>"""
    description: "capo_notifications.types.managed_notification_configuration_description.ManagedNotificationConfigurationDescription"
    """<p>The description of the <code>ManagedNotificationConfiguration</code>.</p>"""
    category: "str"
    """<p>The category of the <code>ManagedNotificationConfiguration</code>.</p>"""
    sub_category: "str"
    """<p>The subCategory of the <code>ManagedNotificationConfiguration</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetManagedNotificationConfigurationResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["description"] = value["description"]
    out["category"] = value["category"]
    out["subCategory"] = value["sub_category"]
    return out


def deserialize_json(data: dict) -> GetManagedNotificationConfigurationResponse:
    out: GetManagedNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("category") is not None:
        out["category"] = data["category"]
    else:
        out["category"] = ""
    if data.get("subCategory") is not None:
        out["sub_category"] = data["subCategory"]
    else:
        out["sub_category"] = ""
    return out
