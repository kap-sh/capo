"""Generated from Smithy shape ``com.amazonaws.mailmanager#LambdaInvocationType``."""

from typing import Literal, TypeAlias, cast

LambdaInvocationType: TypeAlias = Literal[
    "EVENT",
    "REQUEST_RESPONSE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LambdaInvocationType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> LambdaInvocationType:
    return cast(LambdaInvocationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LambdaInvocationType) -> str:
    return value


def deserialize_cbor(data: str) -> LambdaInvocationType:
    return cast(LambdaInvocationType, data)
