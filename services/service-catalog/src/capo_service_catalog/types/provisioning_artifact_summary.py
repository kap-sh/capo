"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.provisioning_artifact_created_time
    import capo_service_catalog.types.provisioning_artifact_description
    import capo_service_catalog.types.provisioning_artifact_info
    import capo_service_catalog.types.provisioning_artifact_name


class ProvisioningArtifactSummary(TypedDict, closed=True):
    id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    name: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_description.ProvisioningArtifactDescription"
    ]
    """<p>The description of the provisioning artifact.</p>"""
    created_time: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_created_time.ProvisioningArtifactCreatedTime"
    ]
    """<p>The UTC time stamp of the creation time.</p>"""
    provisioning_artifact_metadata: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_info.ProvisioningArtifactInfo"
    ]
    """<p>The metadata for the provisioning artifact. This is used with Amazon Web Services Marketplace products.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import capo_service_catalog.types.provisioning_artifact_created_time

        out["CreatedTime"] = (
            capo_service_catalog.types.provisioning_artifact_created_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "provisioning_artifact_metadata" in value:
        import capo_service_catalog.types.provisioning_artifact_info

        out["ProvisioningArtifactMetadata"] = (
            capo_service_catalog.types.provisioning_artifact_info.serialize_aws_json_1_1(
                value["provisioning_artifact_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactSummary:
    out: ProvisioningArtifactSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.provisioning_artifact_created_time

        out["created_time"] = (
            capo_service_catalog.types.provisioning_artifact_created_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if data.get("ProvisioningArtifactMetadata") is not None:
        import capo_service_catalog.types.provisioning_artifact_info

        out["provisioning_artifact_metadata"] = (
            capo_service_catalog.types.provisioning_artifact_info.deserialize_aws_json_1_1(
                data["ProvisioningArtifactMetadata"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "created_time" in value:
        import capo_service_catalog.types.provisioning_artifact_created_time

        out["CreatedTime"] = (
            capo_service_catalog.types.provisioning_artifact_created_time.serialize_cbor(
                value["created_time"]
            )
        )
    if "provisioning_artifact_metadata" in value:
        import capo_service_catalog.types.provisioning_artifact_info

        out["ProvisioningArtifactMetadata"] = (
            capo_service_catalog.types.provisioning_artifact_info.serialize_cbor(
                value["provisioning_artifact_metadata"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ProvisioningArtifactSummary:
    out: ProvisioningArtifactSummary = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.provisioning_artifact_created_time

        out["created_time"] = (
            capo_service_catalog.types.provisioning_artifact_created_time.deserialize_cbor(
                data["CreatedTime"]
            )
        )
    if data.get("ProvisioningArtifactMetadata") is not None:
        import capo_service_catalog.types.provisioning_artifact_info

        out["provisioning_artifact_metadata"] = (
            capo_service_catalog.types.provisioning_artifact_info.deserialize_cbor(
                data["ProvisioningArtifactMetadata"]
            )
        )
    return out
