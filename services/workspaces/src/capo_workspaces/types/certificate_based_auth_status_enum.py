"""Generated from Smithy shape ``com.amazonaws.workspaces#CertificateBasedAuthStatusEnum``."""

from typing import Literal, TypeAlias, cast

CertificateBasedAuthStatusEnum: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateBasedAuthStatusEnum) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateBasedAuthStatusEnum:
    return cast(CertificateBasedAuthStatusEnum, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateBasedAuthStatusEnum) -> str:
    return value


def deserialize_cbor(data: str) -> CertificateBasedAuthStatusEnum:
    return cast(CertificateBasedAuthStatusEnum, data)
