"""Generated from Smithy shape ``com.amazonaws.fms#RuleOrder``."""

from typing import Literal, TypeAlias, cast

RuleOrder: TypeAlias = Literal[
    "STRICT_ORDER",
    "DEFAULT_ACTION_ORDER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleOrder) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> RuleOrder:
    return cast(RuleOrder, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleOrder) -> str:
    return value


def deserialize_cbor(data: str) -> RuleOrder:
    return cast(RuleOrder, data)
