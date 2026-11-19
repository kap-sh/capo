"""Generated from Smithy shape ``com.amazonaws.computeoptimizerautomation#RuleType``."""

from typing import Literal, TypeAlias, cast

RuleType: TypeAlias = Literal[
    "OrganizationRule",
    "AccountRule",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleType:
    return cast(RuleType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleType) -> str:
    return value


def deserialize_cbor(data: str) -> RuleType:
    return cast(RuleType, data)
