"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DeleteProvisioningArtifactOutput``."""

from typing_extensions import TypedDict


class DeleteProvisioningArtifactOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteProvisioningArtifactOutput) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteProvisioningArtifactOutput:
    out: DeleteProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteProvisioningArtifactOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(data: dict) -> DeleteProvisioningArtifactOutput:
    out: DeleteProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    return out
