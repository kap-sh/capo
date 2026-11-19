"""Generated from Smithy shape ``com.amazonaws.appstream#CertificateBasedAuthStatus``."""

from typing import Literal, TypeAlias, cast

CertificateBasedAuthStatus: TypeAlias = Literal[
    "DISABLED",
    "ENABLED",
    "ENABLED_NO_DIRECTORY_LOGIN_FALLBACK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateBasedAuthStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CertificateBasedAuthStatus:
    return cast(CertificateBasedAuthStatus, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CertificateBasedAuthStatus) -> str:
    return value


def deserialize_cbor(data: str) -> CertificateBasedAuthStatus:
    return cast(CertificateBasedAuthStatus, data)
