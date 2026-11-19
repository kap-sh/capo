"""Generated from Smithy shape ``com.amazonaws.servicecatalog#AssociateServiceActionWithProvisioningArtifactOutput``."""

from typing_extensions import TypedDict


class AssociateServiceActionWithProvisioningArtifactOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: AssociateServiceActionWithProvisioningArtifactOutput,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> AssociateServiceActionWithProvisioningArtifactOutput:
    out: AssociateServiceActionWithProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateServiceActionWithProvisioningArtifactOutput) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(
    data: dict,
) -> AssociateServiceActionWithProvisioningArtifactOutput:
    out: AssociateServiceActionWithProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    return out
