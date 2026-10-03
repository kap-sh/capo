"""Generated from Smithy shape ``com.amazonaws.networkfirewall#Header``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_firewall.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_firewall.types.destination
    import capo_network_firewall.types.port
    import capo_network_firewall.types.source
    import capo_network_firewall.types.stateful_rule_direction
    import capo_network_firewall.types.stateful_rule_protocol


class Header(TypedDict, closed=True):
    protocol: "capo_network_firewall.types.stateful_rule_protocol.StatefulRuleProtocol"
    """<p>The protocol to inspect for. To specify all, you can use <code>IP</code>, because all traffic on Amazon Web Services and on the internet is IP.</p>"""
    source: "capo_network_firewall.types.source.Source"
    """<p>The source IP address or address range to inspect for, in CIDR notation. To match with any address, specify <code>ANY</code>. </p> <p>Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6. </p> <p>Examples: </p> <ul> <li> <p>To configure Network Firewall to inspect for the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p>"""
    source_port: "capo_network_firewall.types.port.Port"
    """<p>The source port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""
    direction: (
        "capo_network_firewall.types.stateful_rule_direction.StatefulRuleDirection"
    )
    """<p>The direction of traffic flow to inspect. If set to <code>ANY</code>, the inspection matches bidirectional traffic, both from the source to the destination and from the destination to the source. If set to <code>FORWARD</code>, the inspection only matches traffic going from the source to the destination. </p>"""
    destination: "capo_network_firewall.types.destination.Destination"
    """<p>The destination IP address or address range to inspect for, in CIDR notation. To match with any address, specify <code>ANY</code>. </p> <p>Specify an IP address or a block of IP addresses in Classless Inter-Domain Routing (CIDR) notation. Network Firewall supports all address ranges for IPv4 and IPv6. </p> <p>Examples: </p> <ul> <li> <p>To configure Network Firewall to inspect for the IP address 192.0.2.44, specify <code>192.0.2.44/32</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for IP addresses from 192.0.2.0 to 192.0.2.255, specify <code>192.0.2.0/24</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for the IP address 1111:0000:0000:0000:0000:0000:0000:0111, specify <code>1111:0000:0000:0000:0000:0000:0000:0111/128</code>.</p> </li> <li> <p>To configure Network Firewall to inspect for IP addresses from 1111:0000:0000:0000:0000:0000:0000:0000 to 1111:0000:0000:0000:ffff:ffff:ffff:ffff, specify <code>1111:0000:0000:0000:0000:0000:0000:0000/64</code>.</p> </li> </ul> <p>For more information about CIDR notation, see the Wikipedia entry <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing">Classless Inter-Domain Routing</a>.</p>"""
    destination_port: "capo_network_firewall.types.port.Port"
    """<p>The destination port to inspect for. You can specify an individual port, for example <code>1994</code> and you can specify a port range, for example <code>1990:1994</code>. To match with any port, specify <code>ANY</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Header) -> dict:
    out: dict = {}
    import capo_network_firewall.types.stateful_rule_protocol

    out["Protocol"] = (
        capo_network_firewall.types.stateful_rule_protocol.serialize_aws_json_1_0(
            value["protocol"]
        )
    )
    out["Source"] = value["source"]
    out["SourcePort"] = value["source_port"]
    import capo_network_firewall.types.stateful_rule_direction

    out["Direction"] = (
        capo_network_firewall.types.stateful_rule_direction.serialize_aws_json_1_0(
            value["direction"]
        )
    )
    out["Destination"] = value["destination"]
    out["DestinationPort"] = value["destination_port"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Header:
    out: Header = {}  # type: ignore[typeddict-item]
    if data.get("Protocol") is not None:
        import capo_network_firewall.types.stateful_rule_protocol

        out["protocol"] = (
            capo_network_firewall.types.stateful_rule_protocol.deserialize_aws_json_1_0(
                data["Protocol"]
            )
        )
    else:
        raise DeserializationError("Header.protocol required")
    if data.get("Source") is not None:
        out["source"] = data["Source"]
    else:
        raise DeserializationError("Header.source required")
    if data.get("SourcePort") is not None:
        out["source_port"] = data["SourcePort"]
    else:
        raise DeserializationError("Header.source_port required")
    if data.get("Direction") is not None:
        import capo_network_firewall.types.stateful_rule_direction

        out["direction"] = (
            capo_network_firewall.types.stateful_rule_direction.deserialize_aws_json_1_0(
                data["Direction"]
            )
        )
    else:
        raise DeserializationError("Header.direction required")
    if data.get("Destination") is not None:
        out["destination"] = data["Destination"]
    else:
        raise DeserializationError("Header.destination required")
    if data.get("DestinationPort") is not None:
        out["destination_port"] = data["DestinationPort"]
    else:
        raise DeserializationError("Header.destination_port required")
    return out
