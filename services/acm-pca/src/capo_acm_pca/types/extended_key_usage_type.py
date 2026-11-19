"""Generated from Smithy shape ``com.amazonaws.acmpca#ExtendedKeyUsageType``."""

from typing import Literal, TypeAlias, cast

ExtendedKeyUsageType: TypeAlias = Literal[
    "SERVER_AUTH",
    "CLIENT_AUTH",
    "CODE_SIGNING",
    "EMAIL_PROTECTION",
    "TIME_STAMPING",
    "OCSP_SIGNING",
    "SMART_CARD_LOGIN",
    "DOCUMENT_SIGNING",
    "CERTIFICATE_TRANSPARENCY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExtendedKeyUsageType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ExtendedKeyUsageType:
    return cast(ExtendedKeyUsageType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ExtendedKeyUsageType) -> str:
    return value


def deserialize_cbor(data: str) -> ExtendedKeyUsageType:
    return cast(ExtendedKeyUsageType, data)
