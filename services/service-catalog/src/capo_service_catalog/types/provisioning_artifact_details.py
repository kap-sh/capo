"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact_detail

ProvisioningArtifactDetails: TypeAlias = list[
    "capo_service_catalog.types.provisioning_artifact_detail.ProvisioningArtifactDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactDetails) -> list:
    import capo_service_catalog.types.provisioning_artifact_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact_detail.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifactDetails:
    import capo_service_catalog.types.provisioning_artifact_detail

    out: ProvisioningArtifactDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact_detail.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactDetails) -> list:
    import capo_service_catalog.types.provisioning_artifact_detail

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact_detail.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ProvisioningArtifactDetails:
    import capo_service_catalog.types.provisioning_artifact_detail

    out: ProvisioningArtifactDetails = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact_detail.deserialize_cbor(
                item
            )
        )
    return out
