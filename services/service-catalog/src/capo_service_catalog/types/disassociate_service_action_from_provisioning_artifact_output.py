"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DisassociateServiceActionFromProvisioningArtifactOutput``."""

from typing_extensions import TypedDict


class DisassociateServiceActionFromProvisioningArtifactOutput(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DisassociateServiceActionFromProvisioningArtifactOutput,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DisassociateServiceActionFromProvisioningArtifactOutput:
    out: DisassociateServiceActionFromProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(
    value: DisassociateServiceActionFromProvisioningArtifactOutput,
) -> dict:
    out: dict = {}
    return out


def deserialize_cbor(
    data: dict,
) -> DisassociateServiceActionFromProvisioningArtifactOutput:
    out: DisassociateServiceActionFromProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    return out
