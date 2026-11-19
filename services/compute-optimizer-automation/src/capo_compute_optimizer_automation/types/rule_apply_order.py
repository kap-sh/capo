"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RuleApplyOrder``."""

from typing import Literal, TypeAlias, cast

RuleApplyOrder: TypeAlias = Literal[
    "BeforeAccountRules",
    "AfterAccountRules",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleApplyOrder) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleApplyOrder:
    return cast(RuleApplyOrder, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleApplyOrder) -> str:
    return value


def deserialize_cbor(data: str) -> RuleApplyOrder:
    return cast(RuleApplyOrder, data)
