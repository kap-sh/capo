"""Generated from Smithy shape ``com.amazonaws.lightsail#PortInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.network_protocol
    import capo_lightsail.types.port
    import capo_lightsail.types.string_list


class PortInfo(TypedDict, closed=True):
    from_port: "capo_lightsail.types.port.Port"
    """<p>The first port in a range of open ports on an instance.</p> <p>Allowed ports:</p> <ul> <li> <p>TCP and UDP - <code>0</code> to <code>65535</code> </p> </li> <li> <p>ICMP - The ICMP type for IPv4 addresses. For example, specify <code>8</code> as the <code>fromPort</code> (ICMP type), and <code>-1</code> as the <code>toPort</code> (ICMP code), to enable ICMP Ping. For more information, see <a href="https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages">Control Messages</a> on <i>Wikipedia</i>.</p> </li> <li> <p>ICMPv6 - The ICMP type for IPv6 addresses. For example, specify <code>128</code> as the <code>fromPort</code> (ICMPv6 type), and <code>0</code> as <code>toPort</code> (ICMPv6 code). For more information, see <a href="https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_for_IPv6">Internet Control Message Protocol for IPv6</a>.</p> </li> </ul>"""
    to_port: "capo_lightsail.types.port.Port"
    """<p>The last port in a range of open ports on an instance.</p> <p>Allowed ports:</p> <ul> <li> <p>TCP and UDP - <code>0</code> to <code>65535</code> </p> </li> <li> <p>ICMP - The ICMP code for IPv4 addresses. For example, specify <code>8</code> as the <code>fromPort</code> (ICMP type), and <code>-1</code> as the <code>toPort</code> (ICMP code), to enable ICMP Ping. For more information, see <a href="https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages">Control Messages</a> on <i>Wikipedia</i>.</p> </li> <li> <p>ICMPv6 - The ICMP code for IPv6 addresses. For example, specify <code>128</code> as the <code>fromPort</code> (ICMPv6 type), and <code>0</code> as <code>toPort</code> (ICMPv6 code). For more information, see <a href="https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol_for_IPv6">Internet Control Message Protocol for IPv6</a>.</p> </li> </ul>"""
    protocol: NotRequired["capo_lightsail.types.network_protocol.NetworkProtocol"]
    """<p>The IP protocol name.</p> <p>The name can be one of the following:</p> <ul> <li> <p> <code>tcp</code> - Transmission Control Protocol (TCP) provides reliable, ordered, and error-checked delivery of streamed data between applications running on hosts communicating by an IP network. If you have an application that doesn't require reliable data stream service, use UDP instead.</p> </li> <li> <p> <code>all</code> - All transport layer protocol types. For more general information, see <a href="https://en.wikipedia.org/wiki/Transport_layer">Transport layer</a> on <i>Wikipedia</i>.</p> </li> <li> <p> <code>udp</code> - With User Datagram Protocol (UDP), computer applications can send messages (or datagrams) to other hosts on an Internet Protocol (IP) network. Prior communications are not required to set up transmission channels or data paths. Applications that don't require reliable data stream service can use UDP, which provides a connectionless datagram service that emphasizes reduced latency over reliability. If you do require reliable data stream service, use TCP instead.</p> </li> <li> <p> <code>icmp</code> - Internet Control Message Protocol (ICMP) is used to send error messages and operational information indicating success or failure when communicating with an instance. For example, an error is indicated when an instance could not be reached. When you specify <code>icmp</code> as the <code>protocol</code>, you must specify the ICMP type using the <code>fromPort</code> parameter, and ICMP code using the <code>toPort</code> parameter.</p> </li> <li> <p> <code>icmp6</code> - Internet Control Message Protocol (ICMP) for IPv6. When you specify <code>icmp6</code> as the <code>protocol</code>, you must specify the ICMP type using the <code>fromPort</code> parameter, and ICMP code using the <code>toPort</code> parameter.</p> </li> </ul>"""
    cidrs: NotRequired["capo_lightsail.types.string_list.StringList"]
    """<p>The IPv4 address, or range of IPv4 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol.</p> <note> <p>The <code>ipv6Cidrs</code> parameter lists the IPv6 addresses that are allowed to connect to an instance.</p> </note> <p>Examples:</p> <ul> <li> <p>To allow the IP address <code>192.0.2.44</code>, specify <code>192.0.2.44</code> or <code>192.0.2.44/32</code>. </p> </li> <li> <p>To allow the IP addresses <code>192.0.2.0</code> to <code>192.0.2.255</code>, specify <code>192.0.2.0/24</code>.</p> </li> </ul> <p>For more information about CIDR block notation, see <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation">Classless Inter-Domain Routing</a> on <i>Wikipedia</i>.</p>"""
    ipv6_cidrs: NotRequired["capo_lightsail.types.string_list.StringList"]
    """<p>The IPv6 address, or range of IPv6 addresses (in CIDR notation) that are allowed to connect to an instance through the ports, and the protocol. Only devices with an IPv6 address can connect to an instance through IPv6; otherwise, IPv4 should be used.</p> <note> <p>The <code>cidrs</code> parameter lists the IPv4 addresses that are allowed to connect to an instance.</p> </note> <p>For more information about CIDR block notation, see <a href="https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing#CIDR_notation">Classless Inter-Domain Routing</a> on <i>Wikipedia</i>.</p>"""
    cidr_list_aliases: NotRequired["capo_lightsail.types.string_list.StringList"]
    """<p>An alias that defines access for a preconfigured range of IP addresses.</p> <p>The only alias currently supported is <code>lightsail-connect</code>, which allows IP addresses of the browser-based RDP/SSH client in the Lightsail console to connect to your instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PortInfo) -> dict:
    out: dict = {}
    out["fromPort"] = value.get("from_port", 0)
    out["toPort"] = value.get("to_port", 0)
    if "protocol" in value:
        import capo_lightsail.types.network_protocol

        out["protocol"] = capo_lightsail.types.network_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "cidrs" in value:
        import capo_lightsail.types.string_list

        out["cidrs"] = capo_lightsail.types.string_list.serialize_aws_json_1_1(
            value["cidrs"]
        )
    if "ipv6_cidrs" in value:
        import capo_lightsail.types.string_list

        out["ipv6Cidrs"] = capo_lightsail.types.string_list.serialize_aws_json_1_1(
            value["ipv6_cidrs"]
        )
    if "cidr_list_aliases" in value:
        import capo_lightsail.types.string_list

        out["cidrListAliases"] = (
            capo_lightsail.types.string_list.serialize_aws_json_1_1(
                value["cidr_list_aliases"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PortInfo:
    out: PortInfo = {}  # type: ignore[typeddict-item]
    if data.get("fromPort") is not None:
        out["from_port"] = data["fromPort"]
    else:
        out["from_port"] = 0
    if data.get("toPort") is not None:
        out["to_port"] = data["toPort"]
    else:
        out["to_port"] = 0
    if data.get("protocol") is not None:
        import capo_lightsail.types.network_protocol

        out["protocol"] = (
            capo_lightsail.types.network_protocol.deserialize_aws_json_1_1(
                data["protocol"]
            )
        )
    if data.get("cidrs") is not None:
        import capo_lightsail.types.string_list

        out["cidrs"] = capo_lightsail.types.string_list.deserialize_aws_json_1_1(
            data["cidrs"]
        )
    if data.get("ipv6Cidrs") is not None:
        import capo_lightsail.types.string_list

        out["ipv6_cidrs"] = capo_lightsail.types.string_list.deserialize_aws_json_1_1(
            data["ipv6Cidrs"]
        )
    if data.get("cidrListAliases") is not None:
        import capo_lightsail.types.string_list

        out["cidr_list_aliases"] = (
            capo_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["cidrListAliases"]
            )
        )
    return out
