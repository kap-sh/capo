"""Generated from Smithy shape ``com.amazonaws.memorydb#InputAuthenticationType``."""

from typing import Literal, TypeAlias, cast

InputAuthenticationType: TypeAlias = Literal[
    "password",
    "iam",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InputAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> InputAuthenticationType:
    return cast(InputAuthenticationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InputAuthenticationType) -> str:
    return value


def deserialize_cbor(data: str) -> InputAuthenticationType:
    return cast(InputAuthenticationType, data)
