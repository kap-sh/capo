"""Generated from Smithy shape ``com.amazonaws.iotmanagedintegrations#CommandEndpoint``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot_managed_integrations.types.command_capabilities
    import capo_iot_managed_integrations.types.endpoint_id


class CommandEndpoint(TypedDict, closed=True):
    endpoint_id: "capo_iot_managed_integrations.types.endpoint_id.EndpointId"
    """<p>The id of the endpoint for a managed thing.</p>"""
    capabilities: (
        "capo_iot_managed_integrations.types.command_capabilities.CommandCapabilities"
    )
    """<p>Describe the endpoint with an id, a name, and the relevant capabilities for sending commands.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommandEndpoint) -> dict:
    out: dict = {}
    out["endpointId"] = value["endpoint_id"]
    import capo_iot_managed_integrations.types.command_capabilities

    out["capabilities"] = (
        capo_iot_managed_integrations.types.command_capabilities.serialize_json(
            value["capabilities"]
        )
    )
    return out


def deserialize_json(data: dict) -> CommandEndpoint:
    out: CommandEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("endpointId") is not None:
        out["endpoint_id"] = data["endpointId"]
    else:
        out["endpoint_id"] = ""
    if data.get("capabilities") is not None:
        import capo_iot_managed_integrations.types.command_capabilities

        out["capabilities"] = (
            capo_iot_managed_integrations.types.command_capabilities.deserialize_json(
                data["capabilities"]
            )
        )
    else:
        out["capabilities"] = []
    return out


def redact_sensitive(value: CommandEndpoint) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "capabilities" in value:
        import capo_iot_managed_integrations.types.command_capabilities

        out["capabilities"] = (
            capo_iot_managed_integrations.types.command_capabilities.redact_sensitive(
                value["capabilities"]
            )
        )
    return out
