"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulRuleProtocol``."""

from typing import Literal, TypeAlias, cast

StatefulRuleProtocol: TypeAlias = Literal[
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
    "IMAP",
    "MSN",
    "KRB5",
    "IKEV2",
    "TFTP",
    "NTP",
    "DHCP",
    "HTTP2",
    "QUIC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulRuleProtocol) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatefulRuleProtocol:
    return cast(StatefulRuleProtocol, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatefulRuleProtocol) -> str:
    return value


def deserialize_cbor(data: str) -> StatefulRuleProtocol:
    return cast(StatefulRuleProtocol, data)
