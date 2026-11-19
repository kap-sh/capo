"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleIpEmailAttribute``."""

from typing import Literal, TypeAlias, cast

RuleIpEmailAttribute: TypeAlias = Literal["SOURCE_IP",]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleIpEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleIpEmailAttribute:
    return cast(RuleIpEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleIpEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> RuleIpEmailAttribute:
    return cast(RuleIpEmailAttribute, data)
