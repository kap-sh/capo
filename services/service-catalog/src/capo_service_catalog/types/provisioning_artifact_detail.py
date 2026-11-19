"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifactDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.creation_time
    import capo_service_catalog.types.id
    import capo_service_catalog.types.provisioning_artifact_active
    import capo_service_catalog.types.provisioning_artifact_guidance
    import capo_service_catalog.types.provisioning_artifact_name
    import capo_service_catalog.types.provisioning_artifact_type
    import capo_service_catalog.types.source_revision


class ProvisioningArtifactDetail(TypedDict, closed=True):
    id: NotRequired["capo_service_catalog.types.id.Id"]
    """<p>The identifier of the provisioning artifact.</p>"""
    name: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The name of the provisioning artifact.</p>"""
    description: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_name.ProvisioningArtifactName"
    ]
    """<p>The description of the provisioning artifact.</p>"""
    type: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_type.ProvisioningArtifactType"
    ]
    """<p>The type of provisioning artifact.</p> <ul> <li> <p> <code>CLOUD_FORMATION_TEMPLATE</code> - CloudFormation template</p> </li> <li> <p> <code>TERRAFORM_OPEN_SOURCE</code> - Terraform Open Source configuration file</p> </li> <li> <p> <code>TERRAFORM_CLOUD</code> - Terraform Cloud configuration file</p> </li> <li> <p> <code>EXTERNAL</code> - External configuration file</p> </li> </ul>"""
    created_time: NotRequired["capo_service_catalog.types.creation_time.CreationTime"]
    """<p>The UTC time stamp of the creation time.</p>"""
    active: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_active.ProvisioningArtifactActive"
    ]
    """<p>Indicates whether the product version is active.</p>"""
    guidance: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_guidance.ProvisioningArtifactGuidance"
    ]
    """<p>Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.</p>"""
    source_revision: NotRequired[
        "capo_service_catalog.types.source_revision.SourceRevision"
    ]
    """<p>Specifies the revision of the external artifact that was used to automatically sync the Service Catalog product and create the provisioning artifact. Service Catalog includes this response parameter as a high level field to the existing <code>ProvisioningArtifactDetail</code> type, which is returned as part of the response for <code>CreateProduct</code>, <code>UpdateProduct</code>, <code>DescribeProductAsAdmin</code>, <code>DescribeProvisioningArtifact</code>, <code>ListProvisioningArtifact</code>, and <code>UpdateProvisioningArticat</code> APIs. </p> <p>This field only exists for Repo-Synced products. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifactDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_service_catalog.types.provisioning_artifact_type

        out["Type"] = (
            capo_service_catalog.types.provisioning_artifact_type.serialize_aws_json_1_1(
                value["type"]
            )
        )
    if "created_time" in value:
        import capo_service_catalog.types.creation_time

        out["CreatedTime"] = (
            capo_service_catalog.types.creation_time.serialize_aws_json_1_1(
                value["created_time"]
            )
        )
    if "active" in value:
        out["Active"] = value["active"]
    if "guidance" in value:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["Guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.serialize_aws_json_1_1(
                value["guidance"]
            )
        )
    if "source_revision" in value:
        out["SourceRevision"] = value["source_revision"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifactDetail:
    out: ProvisioningArtifactDetail = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_service_catalog.types.provisioning_artifact_type

        out["type"] = (
            capo_service_catalog.types.provisioning_artifact_type.deserialize_aws_json_1_1(
                data["Type"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.creation_time

        out["created_time"] = (
            capo_service_catalog.types.creation_time.deserialize_aws_json_1_1(
                data["CreatedTime"]
            )
        )
    if data.get("Active") is not None:
        out["active"] = data["Active"]
    if data.get("Guidance") is not None:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.deserialize_aws_json_1_1(
                data["Guidance"]
            )
        )
    if data.get("SourceRevision") is not None:
        out["source_revision"] = data["SourceRevision"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifactDetail) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        import capo_service_catalog.types.provisioning_artifact_type

        out["Type"] = (
            capo_service_catalog.types.provisioning_artifact_type.serialize_cbor(
                value["type"]
            )
        )
    if "created_time" in value:
        import capo_service_catalog.types.creation_time

        out["CreatedTime"] = capo_service_catalog.types.creation_time.serialize_cbor(
            value["created_time"]
        )
    if "active" in value:
        out["Active"] = value["active"]
    if "guidance" in value:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["Guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.serialize_cbor(
                value["guidance"]
            )
        )
    if "source_revision" in value:
        out["SourceRevision"] = value["source_revision"]
    return out


def deserialize_cbor(data: dict) -> ProvisioningArtifactDetail:
    out: ProvisioningArtifactDetail = {}  # type: ignore[typeddict-item]
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Type") is not None:
        import capo_service_catalog.types.provisioning_artifact_type

        out["type"] = (
            capo_service_catalog.types.provisioning_artifact_type.deserialize_cbor(
                data["Type"]
            )
        )
    if data.get("CreatedTime") is not None:
        import capo_service_catalog.types.creation_time

        out["created_time"] = capo_service_catalog.types.creation_time.deserialize_cbor(
            data["CreatedTime"]
        )
    if data.get("Active") is not None:
        out["active"] = data["Active"]
    if data.get("Guidance") is not None:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.deserialize_cbor(
                data["Guidance"]
            )
        )
    if data.get("SourceRevision") is not None:
        out["source_revision"] = data["SourceRevision"]
    return out
