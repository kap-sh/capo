"""Generated from Smithy shape ``com.amazonaws.workspaces#DeletableCertificateBasedAuthProperty``."""

from typing import Literal, TypeAlias, cast

DeletableCertificateBasedAuthProperty: TypeAlias = Literal[
    "CERTIFICATE_BASED_AUTH_PROPERTIES_CERTIFICATE_AUTHORITY_ARN",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeletableCertificateBasedAuthProperty) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DeletableCertificateBasedAuthProperty:
    return cast(DeletableCertificateBasedAuthProperty, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeletableCertificateBasedAuthProperty) -> str:
    return value


def deserialize_cbor(data: str) -> DeletableCertificateBasedAuthProperty:
    return cast(DeletableCertificateBasedAuthProperty, data)
