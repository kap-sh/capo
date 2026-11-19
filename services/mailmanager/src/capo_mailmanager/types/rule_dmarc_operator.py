"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleDmarcOperator``."""

from typing import Literal, TypeAlias, cast

RuleDmarcOperator: TypeAlias = Literal[
    "EQUALS",
    "NOT_EQUALS",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleDmarcOperator) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleDmarcOperator:
    return cast(RuleDmarcOperator, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleDmarcOperator) -> str:
    return value


def deserialize_cbor(data: str) -> RuleDmarcOperator:
    return cast(RuleDmarcOperator, data)
