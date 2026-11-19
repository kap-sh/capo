"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleStringEmailAttribute``."""

from typing import Literal, TypeAlias, cast

RuleStringEmailAttribute: TypeAlias = Literal[
    "MAIL_FROM",
    "HELO",
    "RECIPIENT",
    "SENDER",
    "FROM",
    "SUBJECT",
    "TO",
    "CC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleStringEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleStringEmailAttribute:
    return cast(RuleStringEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleStringEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> RuleStringEmailAttribute:
    return cast(RuleStringEmailAttribute, data)
