"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TCPFlag``."""

from typing import Literal, TypeAlias, cast

TCPFlag: TypeAlias = Literal[
    "FIN",
    "SYN",
    "RST",
    "PSH",
    "ACK",
    "URG",
    "ECE",
    "CWR",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TCPFlag) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TCPFlag:
    return cast(TCPFlag, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TCPFlag) -> str:
    return value


def deserialize_cbor(data: str) -> TCPFlag:
    return cast(TCPFlag, data)
