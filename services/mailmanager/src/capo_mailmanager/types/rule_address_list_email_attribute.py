"""Generated from Smithy shape ``com.amazonaws.mailmanager#RuleAddressListEmailAttribute``."""

from typing import Literal, TypeAlias, cast

RuleAddressListEmailAttribute: TypeAlias = Literal[
    "RECIPIENT",
    "MAIL_FROM",
    "SENDER",
    "FROM",
    "TO",
    "CC",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RuleAddressListEmailAttribute) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RuleAddressListEmailAttribute:
    return cast(RuleAddressListEmailAttribute, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: RuleAddressListEmailAttribute) -> str:
    return value


def deserialize_cbor(data: str) -> RuleAddressListEmailAttribute:
    return cast(RuleAddressListEmailAttribute, data)
