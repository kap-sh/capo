"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RevocationCheckAction``."""

from typing import Literal, TypeAlias, cast

RevocationCheckAction: TypeAlias = Literal[
    "PASS",
    "DROP",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RevocationCheckAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RevocationCheckAction:
    return cast(RevocationCheckAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RevocationCheckAction) -> str:
    return value


def deserialize_cbor(data: str) -> RevocationCheckAction:
    return cast(RevocationCheckAction, data)
