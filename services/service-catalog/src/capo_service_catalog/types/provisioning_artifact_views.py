"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactViews``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact_view

ProvisioningArtifactViews: TypeAlias = list[
    "capo_service_catalog.types.provisioning_artifact_view.ProvisioningArtifactView"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactViews) -> list:
    import capo_service_catalog.types.provisioning_artifact_view

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact_view.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ProvisioningArtifactViews:
    import capo_service_catalog.types.provisioning_artifact_view

    out: ProvisioningArtifactViews = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact_view.deserialize_aws_json_1_1(
                item
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactViews) -> list:
    import capo_service_catalog.types.provisioning_artifact_view

    out: list = []
    for item in value:
        out.append(
            capo_service_catalog.types.provisioning_artifact_view.serialize_cbor(item)
        )
    return out


def deserialize_cbor(data: list) -> ProvisioningArtifactViews:
    import capo_service_catalog.types.provisioning_artifact_view

    out: ProvisioningArtifactViews = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_service_catalog.types.provisioning_artifact_view.deserialize_cbor(item)
        )
    return out
