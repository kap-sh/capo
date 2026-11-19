"""Generated from Smithy shape ``com.amazonaws.datasync#AzureBlobAuthenticationType``."""

from typing import Literal, TypeAlias, cast

AzureBlobAuthenticationType: TypeAlias = Literal[
    "SAS",
    "NONE",
    "OIDC",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AzureBlobAuthenticationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AzureBlobAuthenticationType:
    return cast(AzureBlobAuthenticationType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AzureBlobAuthenticationType) -> str:
    return value


def deserialize_cbor(data: str) -> AzureBlobAuthenticationType:
    return cast(AzureBlobAuthenticationType, data)
