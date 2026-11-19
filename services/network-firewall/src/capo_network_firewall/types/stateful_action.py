"""Generated from Smithy shape ``com.amazonaws.networkfirewall#StatefulAction``."""

from typing import Literal, TypeAlias, cast

StatefulAction: TypeAlias = Literal[
    "PASS",
    "DROP",
    "ALERT",
    "REJECT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: StatefulAction) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> StatefulAction:
    return cast(StatefulAction, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: StatefulAction) -> str:
    return value


def deserialize_cbor(data: str) -> StatefulAction:
    return cast(StatefulAction, data)
