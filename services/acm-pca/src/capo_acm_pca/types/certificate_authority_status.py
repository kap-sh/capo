"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityStatus``."""

from typing import Literal, TypeAlias, cast

CertificateAuthorityStatus: TypeAlias = Literal[
    "CREATING",
    "PENDING_CERTIFICATE",
    "ACTIVE",
    "DELETED",
    "DISABLED",
    "EXPIRED",
    "FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthorityStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateAuthorityStatus:
    return cast(CertificateAuthorityStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateAuthorityStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CertificateAuthorityStatus:
    return cast(CertificateAuthorityStatus, data)
