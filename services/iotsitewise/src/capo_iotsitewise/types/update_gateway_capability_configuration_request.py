"""Generated from Smithy shape ``com.amazonaws.iotsitewise#UpdateGatewayCapabilityConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.capability_configuration
    import capo_iotsitewise.types.capability_namespace
    import capo_iotsitewise.types.id


class UpdateGatewayCapabilityConfigurationRequest(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway to be updated.</p>"""
    capability_namespace: (
        "capo_iotsitewise.types.capability_namespace.CapabilityNamespace"
    )
    """<p>The namespace of the gateway capability configuration to be updated. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:3</code>.</p>"""
    capability_configuration: (
        "capo_iotsitewise.types.capability_configuration.CapabilityConfiguration"
    )
    """<p>The JSON document that defines the configuration for the gateway capability. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html#configure-source-cli">Configuring data sources (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateGatewayCapabilityConfigurationRequest) -> dict:
    out: dict = {}
    out["capabilityNamespace"] = value["capability_namespace"]
    out["capabilityConfiguration"] = value["capability_configuration"]
    return out


def deserialize_json(data: dict) -> UpdateGatewayCapabilityConfigurationRequest:
    out: UpdateGatewayCapabilityConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("capabilityNamespace") is not None:
        out["capability_namespace"] = data["capabilityNamespace"]
    else:
        raise DeserializationError(
            "UpdateGatewayCapabilityConfigurationRequest.capability_namespace required"
        )
    if data.get("capabilityConfiguration") is not None:
        out["capability_configuration"] = data["capabilityConfiguration"]
    else:
        raise DeserializationError(
            "UpdateGatewayCapabilityConfigurationRequest.capability_configuration required"
        )
    return out
