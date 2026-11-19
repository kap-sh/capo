"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleNumberEmailAttribute``."""

from typing import Literal, TypeAlias, cast

RuleNumberEmailAttribute: TypeAlias = Literal["MESSAGE_SIZE",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleNumberEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleNumberEmailAttribute:
    return cast(RuleNumberEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleNumberEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> RuleNumberEmailAttribute:
    return cast(RuleNumberEmailAttribute, data)
