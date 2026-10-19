"""Generated from Smithy shape ``com.amazonaws.iotsitewise#GatewayCapabilitySummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.capability_namespace
    import capo_iotsitewise.types.capability_sync_status


class GatewayCapabilitySummary(TypedDict, closed=True):
    capability_namespace: (
        "capo_iotsitewise.types.capability_namespace.CapabilityNamespace"
    )
    """<p>The namespace of the capability configuration. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:3</code>.</p>"""
    capability_sync_status: (
        "capo_iotsitewise.types.capability_sync_status.CapabilitySyncStatus"
    )
    """<p>The synchronization status of the gateway capability configuration. The sync status can be one of the following:</p> <ul> <li> <p> <code>IN_SYNC</code> - The gateway is running with the latest configuration.</p> </li> <li> <p> <code>OUT_OF_SYNC</code> - The gateway hasn't received the latest configuration.</p> </li> <li> <p> <code>SYNC_FAILED</code> - The gateway rejected the latest configuration.</p> </li> <li> <p> <code>UNKNOWN</code> - The gateway hasn't reported its sync status.</p> </li> <li> <p> <code>NOT_APPLICABLE</code> - The gateway doesn't support this capability. This is most common when integrating partner data sources, because the data integration is handled externally by the partner.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GatewayCapabilitySummary) -> dict:
    out: dict = {}
    out["capabilityNamespace"] = value["capability_namespace"]
    import capo_iotsitewise.types.capability_sync_status

    out["capabilitySyncStatus"] = (
        capo_iotsitewise.types.capability_sync_status.serialize_json(
            value["capability_sync_status"]
        )
    )
    return out


def deserialize_json(data: dict) -> GatewayCapabilitySummary:
    out: GatewayCapabilitySummary = {}  # type: ignore[typeddict-item]
    if data.get("capabilityNamespace") is not None:
        out["capability_namespace"] = data["capabilityNamespace"]
    else:
        out["capability_namespace"] = ""
    if data.get("capabilitySyncStatus") is not None:
        import capo_iotsitewise.types.capability_sync_status

        out["capability_sync_status"] = (
            capo_iotsitewise.types.capability_sync_status.deserialize_json(
                data["capabilitySyncStatus"]
            )
        )
    else:
        import typing

        out["capability_sync_status"] = typing.cast(
            "capo_iotsitewise.types.capability_sync_status.CapabilitySyncStatus", ""
        )
    return out
