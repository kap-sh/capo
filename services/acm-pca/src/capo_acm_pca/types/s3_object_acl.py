"""Generated from Smithy shape ``com.amazonaws.acmpca#S3ObjectAcl``."""

from typing import Literal, TypeAlias, cast

S3ObjectAcl: TypeAlias = Literal[
    "PUBLIC_READ",
    "BUCKET_OWNER_FULL_CONTROL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3ObjectAcl) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> S3ObjectAcl:
    return cast(S3ObjectAcl, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: S3ObjectAcl) -> str:
    return value


def deserialize_cbor(data: str) -> S3ObjectAcl:
    return cast(S3ObjectAcl, data)
