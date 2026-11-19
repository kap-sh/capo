"""Generated from Smithy shape ``com.amazonaws.codeconnections#ProviderType``."""

from typing import Literal, TypeAlias, cast

ProviderType: TypeAlias = Literal[
    "Bitbucket",
    "GitHub",
    "GitHubEnterpriseServer",
    "GitLab",
    "GitLabSelfManaged",
    "AzureDevOps",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ProviderType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ProviderType:
    return cast(ProviderType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProviderType) -> str:
    return value


def deserialize_cbor(data: str) -> ProviderType:
    return cast(ProviderType, data)
