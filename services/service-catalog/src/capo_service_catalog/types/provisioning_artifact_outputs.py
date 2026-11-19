"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactOutputs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact_output

ProvisioningArtifactOutputs: TypeAlias = list[
    "capo_service_catalog.types.provisioning_artifact_output.ProvisioningArtifactOutput"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactOutputs) -> list:
    import capo_service_catalog.types.provisioning_artifact_output

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact_output.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifactOutputs:
    import capo_service_catalog.types.provisioning_artifact_output

    out: ProvisioningArtifactOutputs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact_output.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactOutputs) -> list:
    import capo_service_catalog.types.provisioning_artifact_output

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact_output.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ProvisioningArtifactOutputs:
    import capo_service_catalog.types.provisioning_artifact_output

    out: ProvisioningArtifactOutputs = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact_output.deserialize_cbor(
                item
            )
        )
    return out
