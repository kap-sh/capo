"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CopyProductStatus``."""

from typing import Literal, TypeAlias, cast

CopyProductStatus: TypeAlias = Literal[
    "SUCCEEDED",
    "IN_PROGRESS",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CopyProductStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CopyProductStatus:
    return cast(CopyProductStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CopyProductStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CopyProductStatus:
    return cast(CopyProductStatus, data)
