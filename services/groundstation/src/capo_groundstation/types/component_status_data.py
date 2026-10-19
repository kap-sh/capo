"""Generated from Smithy shape ``com.amazonaws.groundstation#ComponentStatusData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_groundstation.types.agent_status
    import capo_groundstation.types.capability_arn
    import capo_groundstation.types.component_type_string
    import capo_groundstation.types.uuid


class ComponentStatusData(TypedDict, closed=True):
    component_type: "capo_groundstation.types.component_type_string.ComponentTypeString"
    """<p>The Component type.</p>"""
    capability_arn: "capo_groundstation.types.capability_arn.CapabilityArn"
    """<p>Capability ARN of the component.</p>"""
    status: "capo_groundstation.types.agent_status.AgentStatus"
    """<p>Component status.</p>"""
    bytes_sent: NotRequired["int"]
    """<p>Bytes sent by the component.</p>"""
    bytes_received: NotRequired["int"]
    """<p>Bytes received by the component.</p>"""
    packets_dropped: NotRequired["int"]
    """<p>Packets dropped by component.</p>"""
    dataflow_id: "capo_groundstation.types.uuid.Uuid"
    """<p>Dataflow UUID associated with the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentStatusData) -> dict:
    out: dict = {}
    out["componentType"] = value["component_type"]
    out["capabilityArn"] = value["capability_arn"]
    import capo_groundstation.types.agent_status

    out["status"] = capo_groundstation.types.agent_status.serialize_json(
        value["status"]
    )
    if "bytes_sent" in value:
        out["bytesSent"] = value["bytes_sent"]
    if "bytes_received" in value:
        out["bytesReceived"] = value["bytes_received"]
    if "packets_dropped" in value:
        out["packetsDropped"] = value["packets_dropped"]
    out["dataflowId"] = value["dataflow_id"]
    return out


def deserialize_json(data: dict) -> ComponentStatusData:
    out: ComponentStatusData = {}  # type: ignore[typeddict-item]
    if data.get("componentType") is not None:
        out["component_type"] = data["componentType"]
    else:
        out["component_type"] = ""
    if data.get("capabilityArn") is not None:
        out["capability_arn"] = data["capabilityArn"]
    else:
        out["capability_arn"] = ""
    if data.get("status") is not None:
        import capo_groundstation.types.agent_status

        out["status"] = capo_groundstation.types.agent_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_groundstation.types.agent_status.AgentStatus", ""
        )
    if data.get("bytesSent") is not None:
        out["bytes_sent"] = data["bytesSent"]
    if data.get("bytesReceived") is not None:
        out["bytes_received"] = data["bytesReceived"]
    if data.get("packetsDropped") is not None:
        out["packets_dropped"] = data["packetsDropped"]
    if data.get("dataflowId") is not None:
        out["dataflow_id"] = data["dataflowId"]
    else:
        out["dataflow_id"] = ""
    return out
