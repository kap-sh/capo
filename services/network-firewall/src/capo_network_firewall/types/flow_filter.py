"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FlowFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_network_firewall.types.address
    import capo_network_firewall.types.port
    import capo_network_firewall.types.protocol_strings


class FlowFilter(TypedDict, closed=True):
    source_address: NotRequired["capo_network_firewall.types.address.Address"]
    destination_address: NotRequired["capo_network_firewall.types.address.Address"]
    source_port: NotRequired["capo_network_firewall.types.port.Port"]
    """<p>The source port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    destination_port: NotRequired["capo_network_firewall.types.port.Port"]
    """<p>The destination port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    protocols: NotRequired[
        "capo_network_firewall.types.protocol_strings.ProtocolStrings"
    ]
    """<p>The protocols to inspect for, specified using the assigned internet protocol number (IANA) for each protocol. If not specified, this matches with any protocol.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FlowFilter) -> dict:
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
    if "protocols" in value:
        import capo_network_firewall.types.protocol_strings

        out["Protocols"] = (
            capo_network_firewall.types.protocol_strings.serialize_aws_json_1_0(
                value["protocols"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> FlowFilter:
    out: FlowFilter = {}  # type: ignore[typeddict-item]
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
    if data.get("Protocols") is not None:
        import capo_network_firewall.types.protocol_strings

        out["protocols"] = (
            capo_network_firewall.types.protocol_strings.deserialize_aws_json_1_0(
                data["Protocols"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FlowFilter) -> dict:
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
    if "protocols" in value:
        import capo_network_firewall.types.protocol_strings

        out["Protocols"] = capo_network_firewall.types.protocol_strings.serialize_cbor(
            value["protocols"]
        )
    return out


def deserialize_cbor(data: dict) -> FlowFilter:
    out: FlowFilter = {}  # type: ignore[typeddict-item]
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
    if data.get("Protocols") is not None:
        import capo_network_firewall.types.protocol_strings

        out["protocols"] = (
            capo_network_firewall.types.protocol_strings.deserialize_cbor(
                data["Protocols"]
            )
        )
    return out
