"""Generated from Smithy shape ``com.amazonaws.acmpca#CertificateAuthorityUsageMode``."""

from typing import Literal, TypeAlias, cast

CertificateAuthorityUsageMode: TypeAlias = Literal[
    "GENERAL_PURPOSE",
    "SHORT_LIVED_CERTIFICATE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateAuthorityUsageMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateAuthorityUsageMode:
    return cast(CertificateAuthorityUsageMode, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateAuthorityUsageMode) -> str:
    return value


def deserialize_cbor(data: str) -> CertificateAuthorityUsageMode:
    return cast(CertificateAuthorityUsageMode, data)
