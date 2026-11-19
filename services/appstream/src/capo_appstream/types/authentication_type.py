"""Generated from Smithy shape ``com.amazonaws.appstream#AuthenticationType``."""

from typing import Literal, TypeAlias, cast

AuthenticationType: TypeAlias = Literal[
    "API",
    "SAML",
    "USERPOOL",
    "AWS_AD",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AuthenticationType) -> str:
    return value


def deserialize_cbor(data: str) -> AuthenticationType:
    return cast(AuthenticationType, data)
