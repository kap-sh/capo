"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactGuidance``."""

from typing import Literal, TypeAlias, cast

ProvisioningArtifactGuidance: TypeAlias = Literal[
    "DEFAULT",
    "DEPRECATED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactGuidance) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ProvisioningArtifactGuidance:
    return cast(ProvisioningArtifactGuidance, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactGuidance) -> str:
    return value


def deserialize_cbor(data: str) -> ProvisioningArtifactGuidance:
    return cast(ProvisioningArtifactGuidance, data)
