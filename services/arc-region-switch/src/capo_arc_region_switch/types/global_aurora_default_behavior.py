"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#GlobalAuroraDefaultBehavior``."""

from typing import Literal, TypeAlias, cast

GlobalAuroraDefaultBehavior: TypeAlias = Literal[
    "switchoverOnly",
    "failover",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GlobalAuroraDefaultBehavior) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> GlobalAuroraDefaultBehavior:
    return cast(GlobalAuroraDefaultBehavior, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GlobalAuroraDefaultBehavior) -> str:
    return value


def deserialize_cbor(data: str) -> GlobalAuroraDefaultBehavior:
    return cast(GlobalAuroraDefaultBehavior, data)
