"""Generated from Smithy shape ``com.amazonaws.servicecatalog#PrincipalType``."""

from typing import Literal, TypeAlias, cast

PrincipalType: TypeAlias = Literal[
    "IAM",
    "IAM_PATTERN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PrincipalType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PrincipalType:
    return cast(PrincipalType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PrincipalType) -> str:
    return value


def deserialize_cbor(data: str) -> PrincipalType:
    return cast(PrincipalType, data)
