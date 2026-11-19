"""Generated from Smithy shape ``com.amazonaws.servicecatalog#ProvisioningArtifact``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.id
    import capo_service_catalog.types.provisioning_artifact_created_time
    import capo_service_catalog.types.provisioning_artifact_description
    import capo_service_catalog.types.provisioning_artifact_guidance
    import capo_service_catalog.types.provisioning_artifact_name


class ProvisioningArtifact(TypedDict, closed=True):
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
    guidance: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_guidance.ProvisioningArtifactGuidance"
    ]
    """<p>Information set by the administrator to provide guidance to end users about which provisioning artifacts to use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ProvisioningArtifact) -> dict:
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
    if "guidance" in value:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["Guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.serialize_aws_json_1_1(
                value["guidance"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ProvisioningArtifact:
    out: ProvisioningArtifact = {}  # type: ignore[typeddict-item]
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
    if data.get("Guidance") is not None:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.deserialize_aws_json_1_1(
                data["Guidance"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ProvisioningArtifact) -> dict:
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
    if "guidance" in value:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["Guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.serialize_cbor(
                value["guidance"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ProvisioningArtifact:
    out: ProvisioningArtifact = {}  # type: ignore[typeddict-item]
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
    if data.get("Guidance") is not None:
        import capo_service_catalog.types.provisioning_artifact_guidance

        out["guidance"] = (
            capo_service_catalog.types.provisioning_artifact_guidance.deserialize_cbor(
                data["Guidance"]
            )
        )
    return out
