"""Generated from Smithy shape ``com.amazonaws.networkfirewall#TransparentFilteringNatScope``."""

from typing import Literal, TypeAlias, cast

TransparentFilteringNatScope: TypeAlias = Literal[
    "NAT_ALL",
    "NAT_NONE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TransparentFilteringNatScope) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> TransparentFilteringNatScope:
    return cast(TransparentFilteringNatScope, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TransparentFilteringNatScope) -> str:
    return value


def deserialize_cbor(data: str) -> TransparentFilteringNatScope:
    return cast(TransparentFilteringNatScope, data)
