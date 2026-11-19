"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#MarketTypeEnum``."""

from typing import Literal, TypeAlias, cast

MarketTypeEnum: TypeAlias = Literal[
    "spot",
    "capacity-block",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MarketTypeEnum) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MarketTypeEnum:
    return cast(MarketTypeEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: MarketTypeEnum) -> str:
    return value


def deserialize_cbor(data: str) -> MarketTypeEnum:
    return cast(MarketTypeEnum, data)
