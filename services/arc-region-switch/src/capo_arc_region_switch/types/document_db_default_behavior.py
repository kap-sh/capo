"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#DocumentDbDefaultBehavior``."""

from typing import Literal, TypeAlias, cast

DocumentDbDefaultBehavior: TypeAlias = Literal[
    "switchoverOnly",
    "failover",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DocumentDbDefaultBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DocumentDbDefaultBehavior:
    return cast(DocumentDbDefaultBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DocumentDbDefaultBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> DocumentDbDefaultBehavior:
    return cast(DocumentDbDefaultBehavior, data)
