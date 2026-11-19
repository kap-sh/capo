"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsDataTransferProtection``."""

from typing import Literal, TypeAlias, cast

HdfsDataTransferProtection: TypeAlias = Literal[
    "DISABLED",
    "AUTHENTICATION",
    "INTEGRITY",
    "PRIVACY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HdfsDataTransferProtection) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> HdfsDataTransferProtection:
    return cast(HdfsDataTransferProtection, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: HdfsDataTransferProtection) -> str:
    return value


def deserialize_cbor(data: str) -> HdfsDataTransferProtection:
    return cast(HdfsDataTransferProtection, data)
