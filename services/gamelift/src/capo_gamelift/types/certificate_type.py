"""Generated from Smithy shape ``com.amazonaws.gamelift#CertificateType``."""

from typing import Literal, TypeAlias, cast

CertificateType: TypeAlias = Literal[
    "DISABLED",
    "GENERATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateType:
    return cast(CertificateType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateType) -> str:
    return value


def deserialize_cbor(data: str) -> CertificateType:
    return cast(CertificateType, data)
