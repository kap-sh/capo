"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Flow``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.address
    import capo_network_firewall.types.age
    import capo_network_firewall.types.byte_count
    import capo_network_firewall.types.packet_count
    import capo_network_firewall.types.port
    import capo_network_firewall.types.protocol_string


class Flow(TypedDict, closed=True):
    source_address: NotRequired["capo_network_firewall.types.address.Address"]
    destination_address: NotRequired["capo_network_firewall.types.address.Address"]
    source_port: NotRequired["capo_network_firewall.types.port.Port"]
    """<p>The source port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    destination_port: NotRequired["capo_network_firewall.types.port.Port"]
    """<p>The destination port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    protocol: NotRequired["capo_network_firewall.types.protocol_string.ProtocolString"]
    """<p>The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.</p>"""
    age: NotRequired["capo_network_firewall.types.age.Age"]
    """<p>Returned as info about age of the flows identified by the flow operation.</p>"""
    packet_count: NotRequired["capo_network_firewall.types.packet_count.PacketCount"]
    """<p>Returns the total number of data packets received or transmitted in a flow.</p>"""
    byte_count: "capo_network_firewall.types.byte_count.ByteCount"
    """<p>Returns the number of bytes received or transmitted in a specific flow.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Flow) -> dict:
    out: dict = {}
    if "source_address" in value:
        import capo_network_firewall.types.address

        out["SourceAddress"] = (
            capo_network_firewall.types.address.serialize_aws_json_1_0(
                value["source_address"]
            )
        )
    if "destination_address" in value:
        import capo_network_firewall.types.address

        out["DestinationAddress"] = (
            capo_network_firewall.types.address.serialize_aws_json_1_0(
                value["destination_address"]
            )
        )
    if "source_port" in value:
        out["SourcePort"] = value["source_port"]
    if "destination_port" in value:
        out["DestinationPort"] = value["destination_port"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "age" in value:
        out["Age"] = value["age"]
    if "packet_count" in value:
        out["PacketCount"] = value["packet_count"]
    out["ByteCount"] = value.get("byte_count", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> Flow:
    out: Flow = {}  # type: ignore[typeddict-item]
    if data.get("SourceAddress") is not None:
        import capo_network_firewall.types.address

        out["source_address"] = (
            capo_network_firewall.types.address.deserialize_aws_json_1_0(
                data["SourceAddress"]
            )
        )
    if data.get("DestinationAddress") is not None:
        import capo_network_firewall.types.address

        out["destination_address"] = (
            capo_network_firewall.types.address.deserialize_aws_json_1_0(
                data["DestinationAddress"]
            )
        )
    if data.get("SourcePort") is not None:
        out["source_port"] = data["SourcePort"]
    if data.get("DestinationPort") is not None:
        out["destination_port"] = data["DestinationPort"]
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    if data.get("Age") is not None:
        out["age"] = data["Age"]
    if data.get("PacketCount") is not None:
        out["packet_count"] = data["PacketCount"]
    if data.get("ByteCount") is not None:
        out["byte_count"] = data["ByteCount"]
    else:
        out["byte_count"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Flow) -> dict:
    out: dict = {}
    if "source_address" in value:
        import capo_network_firewall.types.address

        out["SourceAddress"] = capo_network_firewall.types.address.serialize_cbor(
            value["source_address"]
        )
    if "destination_address" in value:
        import capo_network_firewall.types.address

        out["DestinationAddress"] = capo_network_firewall.types.address.serialize_cbor(
            value["destination_address"]
        )
    if "source_port" in value:
        out["SourcePort"] = value["source_port"]
    if "destination_port" in value:
        out["DestinationPort"] = value["destination_port"]
    if "protocol" in value:
        out["Protocol"] = value["protocol"]
    if "age" in value:
        out["Age"] = value["age"]
    if "packet_count" in value:
        out["PacketCount"] = value["packet_count"]
    out["ByteCount"] = value.get("byte_count", 0)
    return out


def deserialize_cbor(data: dict) -> Flow:
    out: Flow = {}  # type: ignore[typeddict-item]
    if data.get("SourceAddress") is not None:
        import capo_network_firewall.types.address

        out["source_address"] = capo_network_firewall.types.address.deserialize_cbor(
            data["SourceAddress"]
        )
    if data.get("DestinationAddress") is not None:
        import capo_network_firewall.types.address

        out["destination_address"] = (
            capo_network_firewall.types.address.deserialize_cbor(
                data["DestinationAddress"]
            )
        )
    if data.get("SourcePort") is not None:
        out["source_port"] = data["SourcePort"]
    if data.get("DestinationPort") is not None:
        out["destination_port"] = data["DestinationPort"]
    if data.get("Protocol") is not None:
        out["protocol"] = data["Protocol"]
    if data.get("Age") is not None:
        out["age"] = data["Age"]
    if data.get("PacketCount") is not None:
        out["packet_count"] = data["PacketCount"]
    if data.get("ByteCount") is not None:
        out["byte_count"] = data["ByteCount"]
    else:
        out["byte_count"] = 0
    return out
