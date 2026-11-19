"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactPropertyName``."""

from typing import Literal, TypeAlias, cast

ProvisioningArtifactPropertyName: TypeAlias = Literal["Id",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactPropertyName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningArtifactPropertyName:
    return cast(ProvisioningArtifactPropertyName, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactPropertyName) -> str:
    return value


def deserialize_cbor(data: str) -> ProvisioningArtifactPropertyName:
    return cast(ProvisioningArtifactPropertyName, data)
