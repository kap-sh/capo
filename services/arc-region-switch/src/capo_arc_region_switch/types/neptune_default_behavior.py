"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#NeptuneDefaultBehavior``."""

from typing import Literal, TypeAlias, cast

NeptuneDefaultBehavior: TypeAlias = Literal[
    "switchoverOnly",
    "failover",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NeptuneDefaultBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> NeptuneDefaultBehavior:
    return cast(NeptuneDefaultBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NeptuneDefaultBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> NeptuneDefaultBehavior:
    return cast(NeptuneDefaultBehavior, data)
