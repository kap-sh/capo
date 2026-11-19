"""Generated from Smithy shape ``com.amazonaws.codebuild#CredentialProviderType``."""

from typing import Literal, TypeAlias, cast

CredentialProviderType: TypeAlias = Literal["SECRETS_MANAGER",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CredentialProviderType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CredentialProviderType:
    return cast(CredentialProviderType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CredentialProviderType) -> str:
    return value


def deserialize_cbor(data: str) -> CredentialProviderType:
    return cast(CredentialProviderType, data)
