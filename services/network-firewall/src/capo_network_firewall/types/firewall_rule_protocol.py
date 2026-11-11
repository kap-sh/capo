"""Generated from Smithy shape ``com.amazonaws.networkfirewall#FirewallRuleProtocol``."""

from typing import Literal, TypeAlias, cast

FirewallRuleProtocol: TypeAlias = Literal[
    "IP",
    "TCP",
    "UDP",
    "ICMP",
    "HTTP",
    "FTP",
    "TLS",
    "SMB",
    "DNS",
    "DCERPC",
    "SSH",
    "SMTP",
    "MSN",
    "KRB5",
    "IKEV2",
    "TFTP",
    "NTP",
    "DHCP",
    "HTTP2",
    "QUIC",
    "ICMPV4",
    "ICMPV6",
    "SCTP",
    "IPV4",
    "IPV6",
    "DOH2",
    "FTP_DATA",
    "NFS",
    "RDP",
    "RFB",
    "MQTT",
    "PGSQL",
    "SNMP",
    "TELNET",
    "WEBSOCKET",
    "LDAP",
    "POP3",
    "MDNS",
    "BITTORRENT_DHT",
    "DNP3",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: FirewallRuleProtocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> FirewallRuleProtocol:
    return cast(FirewallRuleProtocol, data)
