"""Generated from Smithy shape ``com.amazonaws.networkmonitor#ProbeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkmonitor.types.arn
    import capo_networkmonitor.types.destination
    import capo_networkmonitor.types.packet_size
    import capo_networkmonitor.types.port
    import capo_networkmonitor.types.protocol
    import capo_networkmonitor.types.tag_map


class ProbeInput(TypedDict, closed=True):
    source_arn: "capo_networkmonitor.types.arn.Arn"
    """<p>The ARN of the subnet.</p>"""
    destination: "capo_networkmonitor.types.destination.Destination"
    """<p>The destination IP address. This must be either <code>IPV4</code> or <code>IPV6</code>.</p>"""
    destination_port: NotRequired["capo_networkmonitor.types.port.Port"]
    """<p>The port associated with the <code>destination</code>. This is required only if the <code>protocol</code> is <code>TCP</code> and must be a number between <code>1</code> and <code>65536</code>.</p>"""
    protocol: "capo_networkmonitor.types.protocol.Protocol"
    """<p>The protocol used for the network traffic between the <code>source</code> and <code>destination</code>. This must be either <code>TCP</code> or <code>ICMP</code>.</p>"""
    packet_size: NotRequired["capo_networkmonitor.types.packet_size.PacketSize"]
    """<p>The size of the packets sent between the source and destination. This must be a number between <code>56</code> and <code>8500</code>.</p>"""
    tags: NotRequired["capo_networkmonitor.types.tag_map.TagMap"]
    """<p>The list of key-value pairs created and assigned to the monitor.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProbeInput) -> dict:
    out: dict = {}
    out["sourceArn"] = value["source_arn"]
    out["destination"] = value["destination"]
    if "destination_port" in value:
        out["destinationPort"] = value["destination_port"]
    import capo_networkmonitor.types.protocol

    out["protocol"] = capo_networkmonitor.types.protocol.serialize_json(
        value["protocol"]
    )
    if "packet_size" in value:
        out["packetSize"] = value["packet_size"]
    if "tags" in value:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> ProbeInput:
    out: ProbeInput = {}  # type: ignore[typeddict-item]
    if data.get("sourceArn") is not None:
        out["source_arn"] = data["sourceArn"]
    else:
        out["source_arn"] = ""
    if data.get("destination") is not None:
        out["destination"] = data["destination"]
    else:
        out["destination"] = ""
    if data.get("destinationPort") is not None:
        out["destination_port"] = data["destinationPort"]
    if data.get("protocol") is not None:
        import capo_networkmonitor.types.protocol

        out["protocol"] = capo_networkmonitor.types.protocol.deserialize_json(
            data["protocol"]
        )
    else:
        import typing

        out["protocol"] = typing.cast("capo_networkmonitor.types.protocol.Protocol", "")
    if data.get("packetSize") is not None:
        out["packet_size"] = data["packetSize"]
    if data.get("tags") is not None:
        import capo_networkmonitor.types.tag_map

        out["tags"] = capo_networkmonitor.types.tag_map.deserialize_json(data["tags"])
    return out
