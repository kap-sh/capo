"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleVerdictAttribute``."""

from typing import Literal, TypeAlias, cast

RuleVerdictAttribute: TypeAlias = Literal[
    "SPF",
    "DKIM",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleVerdictAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleVerdictAttribute:
    return cast(RuleVerdictAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleVerdictAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> RuleVerdictAttribute:
    return cast(RuleVerdictAttribute, data)
