"""Generated from Smithy shape ``com.amazonaws.iotsitewise#DescribeGatewayCapabilityConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_iotsitewise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsitewise.types.capability_configuration
    import capo_iotsitewise.types.capability_namespace
    import capo_iotsitewise.types.capability_sync_status
    import capo_iotsitewise.types.id


class DescribeGatewayCapabilityConfigurationResponse(TypedDict, closed=True):
    gateway_id: "capo_iotsitewise.types.id.ID"
    """<p>The ID of the gateway that defines the capability configuration.</p>"""
    capability_namespace: (
        "capo_iotsitewise.types.capability_namespace.CapabilityNamespace"
    )
    """<p>The namespace of the gateway capability.</p>"""
    capability_configuration: (
        "capo_iotsitewise.types.capability_configuration.CapabilityConfiguration"
    )
    """<p>The JSON document that defines the gateway capability's configuration. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html#configure-source-cli">Configuring data sources (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>"""
    capability_sync_status: (
        "capo_iotsitewise.types.capability_sync_status.CapabilitySyncStatus"
    )
    """<p>The synchronization status of the gateway capability configuration. The sync status can be one of the following:</p> <ul> <li> <p> <code>IN_SYNC</code> - The gateway is running with the latest configuration.</p> </li> <li> <p> <code>OUT_OF_SYNC</code> - The gateway hasn't received the latest configuration.</p> </li> <li> <p> <code>SYNC_FAILED</code> - The gateway rejected the latest configuration.</p> </li> <li> <p> <code>UNKNOWN</code> - The gateway hasn't reported its sync status.</p> </li> <li> <p> <code>NOT_APPLICABLE</code> - The gateway doesn't support this capability. This is most common when integrating partner data sources, because the data integration is handled externally by the partner.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeGatewayCapabilityConfigurationResponse) -> dict:
    out: dict = {}
    out["gatewayId"] = value["gateway_id"]
    out["capabilityNamespace"] = value["capability_namespace"]
    out["capabilityConfiguration"] = value["capability_configuration"]
    import capo_iotsitewise.types.capability_sync_status

    out["capabilitySyncStatus"] = (
        capo_iotsitewise.types.capability_sync_status.serialize_json(
            value["capability_sync_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> DescribeGatewayCapabilityConfigurationResponse:
    out: DescribeGatewayCapabilityConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("gatewayId") is not None:
        out["gateway_id"] = data["gatewayId"]
    else:
        raise DeserializationError(
            "DescribeGatewayCapabilityConfigurationResponse.gateway_id required"
        )
    if data.get("capabilityNamespace") is not None:
        out["capability_namespace"] = data["capabilityNamespace"]
    else:
        raise DeserializationError(
            "DescribeGatewayCapabilityConfigurationResponse.capability_namespace required"
        )
    if data.get("capabilityConfiguration") is not None:
        out["capability_configuration"] = data["capabilityConfiguration"]
    else:
        raise DeserializationError(
            "DescribeGatewayCapabilityConfigurationResponse.capability_configuration required"
        )
    if data.get("capabilitySyncStatus") is not None:
        import capo_iotsitewise.types.capability_sync_status

        out["capability_sync_status"] = (
            capo_iotsitewise.types.capability_sync_status.deserialize_json(
                data["capabilitySyncStatus"]
            )
        )
    else:
        raise DeserializationError(
            "DescribeGatewayCapabilityConfigurationResponse.capability_sync_status required"
        )
    return out
