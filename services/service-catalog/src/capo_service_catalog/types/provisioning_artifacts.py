"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifacts``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact

ProvisioningArtifacts: TypeAlias = list[
    "capo_service_catalog.types.provisioning_artifact.ProvisioningArtifact"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifacts) -> list:
    import capo_service_catalog.types.provisioning_artifact

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifacts:
    import capo_service_catalog.types.provisioning_artifact

    out: ProvisioningArtifacts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifacts) -> list:
    import capo_service_catalog.types.provisioning_artifact

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ProvisioningArtifacts:
    import capo_service_catalog.types.provisioning_artifact

    out: ProvisioningArtifacts = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact.deserialize_cbor(item)
        )
    return out
