"""Generated from Smithy shape ``com.amazonaws.datasync#EfsInTransitEncryption``."""

from typing import Literal, TypeAlias, cast

EfsInTransitEncryption: TypeAlias = Literal[
    "NONE",
    "TLS1_2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EfsInTransitEncryption) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EfsInTransitEncryption:
    return cast(EfsInTransitEncryption, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: EfsInTransitEncryption) -> str:
    return value


def deserialize_cbor(data: str) -> EfsInTransitEncryption:
    return cast(EfsInTransitEncryption, data)
