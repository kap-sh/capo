"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateNotificationConfigurationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_iot_managed_integrations.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.destination_name
    import capo_iot_managed_integrations.types.event_type
    import capo_iot_managed_integrations.types.tags_map


class CreateNotificationConfigurationRequest(TypedDict, closed=True):
    event_type: "capo_iot_managed_integrations.types.event_type.EventType"
    """<p>The type of event triggering a device notification to the customer-managed destination.</p>"""
    destination_name: (
        "capo_iot_managed_integrations.types.destination_name.DestinationName"
    )
    """<p>The name of the destination for the notification configuration.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""
    tags: NotRequired["capo_iot_managed_integrations.types.tags_map.TagsMap"]
    """<p>A set of key/value pairs that are used to manage the notification configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateNotificationConfigurationRequest) -> dict:
    out: dict = {}
    import capo_iot_managed_integrations.types.event_type

    out["EventType"] = capo_iot_managed_integrations.types.event_type.serialize_json(
        value["event_type"]
    )
    out["DestinationName"] = value["destination_name"]
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    if "tags" in value:
        import capo_iot_managed_integrations.types.tags_map

        out["Tags"] = capo_iot_managed_integrations.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateNotificationConfigurationRequest:
    out: CreateNotificationConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventType") is not None:
        import capo_iot_managed_integrations.types.event_type

        out["event_type"] = (
            capo_iot_managed_integrations.types.event_type.deserialize_json(
                data["EventType"]
            )
        )
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationRequest.event_type required"
        )
    if data.get("DestinationName") is not None:
        out["destination_name"] = data["DestinationName"]
    else:
        raise DeserializationError(
            "CreateNotificationConfigurationRequest.destination_name required"
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    if data.get("Tags") is not None:
        import capo_iot_managed_integrations.types.tags_map

        out["tags"] = capo_iot_managed_integrations.types.tags_map.deserialize_json(
            data["Tags"]
        )
    return out


def redact_sensitive(value: CreateNotificationConfigurationRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tags" in value:
        out["tags"] = "*** Sensitive Data Redacted ***"
    return out
