"""Generated from Smithy shape ``com.amazonaws.servicecatalog#SourceProvisioningArtifactPropertiesMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact_property_name
    import capo_service_catalog.types.provisioning_artifact_property_value

SourceProvisioningArtifactPropertiesMap: TypeAlias = dict[
    "capo_service_catalog.types.provisioning_artifact_property_name.ProvisioningArtifactPropertyName",
    "capo_service_catalog.types.provisioning_artifact_property_value.ProvisioningArtifactPropertyValue",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    input_to_serialize: SourceProvisioningArtifactPropertiesMap,
) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.provisioning_artifact_property_name

        out[
            capo_service_catalog.types.provisioning_artifact_property_name.serialize_aws_json_1_1(
                key
            )
        ] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceProvisioningArtifactPropertiesMap:
    out: SourceProvisioningArtifactPropertiesMap = {}
    for key, value in data.items():
        import capo_service_catalog.types.provisioning_artifact_property_name

        if value is None:
            continue
        out[
            capo_service_catalog.types.provisioning_artifact_property_name.deserialize_aws_json_1_1(
                key
            )
        ] = value
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(input_to_serialize: SourceProvisioningArtifactPropertiesMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_service_catalog.types.provisioning_artifact_property_name

        out[
            capo_service_catalog.types.provisioning_artifact_property_name.serialize_cbor(
                key
            )
        ] = value
    return out


def deserialize_cbor(data: dict) -> SourceProvisioningArtifactPropertiesMap:
    out: SourceProvisioningArtifactPropertiesMap = {}
    for key, value in data.items():
        import capo_service_catalog.types.provisioning_artifact_property_name

        if value is None:
            continue
        out[
            capo_service_catalog.types.provisioning_artifact_property_name.deserialize_cbor(
                key
            )
        ] = value
    return out
