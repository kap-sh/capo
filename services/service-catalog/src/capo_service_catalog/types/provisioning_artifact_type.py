"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactType``."""

from typing import Literal, TypeAlias, cast

ProvisioningArtifactType: TypeAlias = Literal[
    "CLOUD_FORMATION_TEMPLATE",
    "MARKETPLACE_AMI",
    "MARKETPLACE_CAR",
    "TERRAFORM_OPEN_SOURCE",
    "TERRAFORM_CLOUD",
    "EXTERNAL",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningArtifactType:
    return cast(ProvisioningArtifactType, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactType) -> str:
    return value


def deserialize_cbor(data: str) -> ProvisioningArtifactType:
    return cast(ProvisioningArtifactType, data)
