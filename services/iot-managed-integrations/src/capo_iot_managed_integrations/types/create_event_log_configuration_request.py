"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CreateEventLogConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.client_token
    import capo_iot_managed_integrations.types.log_level
    import capo_iot_managed_integrations.types.smart_home_resource_id
    import capo_iot_managed_integrations.types.smart_home_resource_type


class CreateEventLogConfigurationRequest(TypedDict, closed=True):
    resource_type: "capo_iot_managed_integrations.types.smart_home_resource_type.SmartHomeResourceType"
    """<p>The type of resource for the event log configuration.</p>"""
    resource_id: NotRequired[
        "capo_iot_managed_integrations.types.smart_home_resource_id.SmartHomeResourceId"
    ]
    """<p>The identifier of the resource for the event log configuration.</p>"""
    event_log_level: "capo_iot_managed_integrations.types.log_level.LogLevel"
    """<p>The logging level for the event log configuration.</p>"""
    client_token: NotRequired[
        "capo_iot_managed_integrations.types.client_token.ClientToken"
    ]
    """<p>An idempotency token. If you retry a request that completed successfully initially using the same client token and parameters, then the retry attempt will succeed without performing any further actions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventLogConfigurationRequest) -> dict:
    out: dict = {}
    out["ResourceType"] = value["resource_type"]
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    import capo_iot_managed_integrations.types.log_level

    out["EventLogLevel"] = capo_iot_managed_integrations.types.log_level.serialize_json(
        value["event_log_level"]
    )
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CreateEventLogConfigurationRequest:
    out: CreateEventLogConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceType") is not None:
        out["resource_type"] = data["ResourceType"]
    else:
        out["resource_type"] = ""
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("EventLogLevel") is not None:
        import capo_iot_managed_integrations.types.log_level

        out["event_log_level"] = (
            capo_iot_managed_integrations.types.log_level.deserialize_json(
                data["EventLogLevel"]
            )
        )
    else:
        import typing

        out["event_log_level"] = typing.cast(
            "capo_iot_managed_integrations.types.log_level.LogLevel", ""
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
