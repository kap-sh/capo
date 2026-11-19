"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsRpcProtection``."""

from typing import Literal, TypeAlias, cast

HdfsRpcProtection: TypeAlias = Literal[
    "DISABLED",
    "AUTHENTICATION",
    "INTEGRITY",
    "PRIVACY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HdfsRpcProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HdfsRpcProtection:
    return cast(HdfsRpcProtection, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HdfsRpcProtection) -> str:
    return value


def deserialize_cbor(data: str) -> HdfsRpcProtection:
    return cast(HdfsRpcProtection, data)
