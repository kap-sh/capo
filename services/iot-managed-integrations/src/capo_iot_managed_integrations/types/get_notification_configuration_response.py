"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#GetNotificationConfigurationResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.event_type
    import capo_iot_managed_integrations.types.notification_configuration_created_at
    import capo_iot_managed_integrations.types.notification_configuration_updated_at
    import capo_iot_managed_integrations.types.tags_map


class GetNotificationConfigurationResponse(TypedDict, closed=True):
    event_type: NotRequired["capo_iot_managed_integrations.types.event_type.EventType"]
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""
    destination_name: NotRequired[
        "capo_iot_managed_integrations.types.destination_name.DestinationName"
    ]
    """<p>The name of the destination for the notification configuration.</p>"""
    created_at: NotRequired[
        "capo_iot_managed_integrations.types.notification_configuration_created_at.NotificationConfigurationCreatedAt"
    ]
    """<p>The timestamp value of when the notification configuration was created.</p>"""
    updated_at: NotRequired[
        "capo_iot_managed_integrations.types.notification_configuration_updated_at.NotificationConfigurationUpdatedAt"
    ]
    """<p>The timestamp value of when the notification configuration was last updated.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotificationConfigurationResponse) -> dict:
    out: dict = {}
    if "event_type" in value:
        import capo_iot_managed_integrations.types.event_type

        out["EventType"] = (
            capo_iot_managed_integrations.types.event_type.serialize_json(
                value["event_type"]
            )
        )
    if "destination_name" in value:
        out["DestinationName"] = value["destination_name"]
    if "created_at" in value:
        import capo_iot_managed_integrations.types.notification_configuration_created_at

        out["CreatedAt"] = (
            capo_iot_managed_integrations.types.notification_configuration_created_at.serialize_json(
                value["created_at"]
            )
        )
    if "updated_at" in value:
        import capo_iot_managed_integrations.types.notification_configuration_updated_at

        out["UpdatedAt"] = (
            capo_iot_managed_integrations.types.notification_configuration_updated_at.serialize_json(
                value["updated_at"]
            )
        )
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> GetNotificationConfigurationResponse:
    out: GetNotificationConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("EventType") is not None:
        import capo_iot_managed_integrations.types.event_type

        out["event_type"] = (
            capo_iot_managed_integrations.types.event_type.deserialize_json(
                data["EventType"]
            )
        )
    if data.get("DestinationName") is not None:
        out["destination_name"] = data["DestinationName"]
    if data.get("CreatedAt") is not None:
        import capo_iot_managed_integrations.types.notification_configuration_created_at

        out["created_at"] = (
            capo_iot_managed_integrations.types.notification_configuration_created_at.deserialize_json(
                data["CreatedAt"]
            )
        )
    if data.get("UpdatedAt") is not None:
        import capo_iot_managed_integrations.types.notification_configuration_updated_at

        out["updated_at"] = (
            capo_iot_managed_integrations.types.notification_configuration_updated_at.deserialize_json(
                data["UpdatedAt"]
            )
        )
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: GetNotificationConfigurationResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
