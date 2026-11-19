"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsAuthenticationType``."""

from typing import Literal, TypeAlias, cast

HdfsAuthenticationType: TypeAlias = Literal[
    "SIMPLE",
    "KERBEROS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HdfsAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HdfsAuthenticationType:
    return cast(HdfsAuthenticationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HdfsAuthenticationType) -> str:
    return value


def deserialize_cbor(data: str) -> HdfsAuthenticationType:
    return cast(HdfsAuthenticationType, data)
