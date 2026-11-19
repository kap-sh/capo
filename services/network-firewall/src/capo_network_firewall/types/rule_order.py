"""Generated from Smithy shape ``com.amazonaws.networkfirewall#RuleOrder``."""

from typing import Literal, TypeAlias, cast

RuleOrder: TypeAlias = Literal[
    "DEFAULT_ACTION_ORDER",
    "STRICT_ORDER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleOrder) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleOrder:
    return cast(RuleOrder, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleOrder) -> str:
    return value


def deserialize_cbor(data: str) -> RuleOrder:
    return cast(RuleOrder, data)
