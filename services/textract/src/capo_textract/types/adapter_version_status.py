"""Generated from Smithy shape ``com.amazonaws.textract#AdapterVersionStatus``."""

from typing import Literal, TypeAlias, cast

AdapterVersionStatus: TypeAlias = Literal[
    "ACTIVE",
    "AT_RISK",
    "DEPRECATED",
    "CREATION_ERROR",
    "CREATION_IN_PROGRESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdapterVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AdapterVersionStatus:
    return cast(AdapterVersionStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AdapterVersionStatus) -> str:
    return value


def deserialize_cbor(data: str) -> AdapterVersionStatus:
    return cast(AdapterVersionStatus, data)
