"""Generated from Smithy shape ``com.amazonaws.servicecatalog#CreateProvisioningArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact_detail
    import capo_service_catalog.types.provisioning_artifact_info
    import capo_service_catalog.types.status


class CreateProvisioningArtifactOutput(TypedDict, closed=True):
    provisioning_artifact_detail: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_detail.ProvisioningArtifactDetail"
    ]
    """<p>Information about the provisioning artifact.</p>"""
    info: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_info.ProvisioningArtifactInfo"
    ]
    """<p>Specify the template source with one of the following options, but not both. Keys accepted: [ <code>LoadTemplateFromURL</code>, <code>ImportFromPhysicalId</code> ].</p> <p>Use the URL of the CloudFormation template in Amazon S3 or GitHub in JSON format. </p> <p> <code>LoadTemplateFromURL</code> </p> <p>Use the URL of the CloudFormation template in Amazon S3 or GitHub in JSON format.</p> <p> <code>ImportFromPhysicalId</code> </p> <p>Use the physical id of the resource that contains the template; currently supports CloudFormation stack ARN.</p>"""
    status: NotRequired["capo_service_catalog.types.status.Status"]
    """<p>The status of the current request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateProvisioningArtifactOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_detail" in value:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["ProvisioningArtifactDetail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.serialize_aws_json_1_1(
                value["provisioning_artifact_detail"]
            )
        )
    if "info" in value:
        import capo_service_catalog.types.provisioning_artifact_info

        out["Info"] = (
            capo_service_catalog.types.provisioning_artifact_info.serialize_aws_json_1_1(
                value["info"]
            )
        )
    if "status" in value:
        import capo_service_catalog.types.status

        out["Status"] = capo_service_catalog.types.status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateProvisioningArtifactOutput:
    out: CreateProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactDetail") is not None:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["provisioning_artifact_detail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.deserialize_aws_json_1_1(
                data["ProvisioningArtifactDetail"]
            )
        )
    if data.get("Info") is not None:
        import capo_service_catalog.types.provisioning_artifact_info

        out["info"] = (
            capo_service_catalog.types.provisioning_artifact_info.deserialize_aws_json_1_1(
                data["Info"]
            )
        )
    if data.get("Status") is not None:
        import capo_service_catalog.types.status

        out["status"] = capo_service_catalog.types.status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateProvisioningArtifactOutput) -> dict:
    out: dict = {}
    if "provisioning_artifact_detail" in value:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["ProvisioningArtifactDetail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.serialize_cbor(
                value["provisioning_artifact_detail"]
            )
        )
    if "info" in value:
        import capo_service_catalog.types.provisioning_artifact_info

        out["Info"] = (
            capo_service_catalog.types.provisioning_artifact_info.serialize_cbor(
                value["info"]
            )
        )
    if "status" in value:
        import capo_service_catalog.types.status

        out["Status"] = capo_service_catalog.types.status.serialize_cbor(
            value["status"]
        )
    return out


def deserialize_cbor(data: dict) -> CreateProvisioningArtifactOutput:
    out: CreateProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProvisioningArtifactDetail") is not None:
        import capo_service_catalog.types.provisioning_artifact_detail

        out["provisioning_artifact_detail"] = (
            capo_service_catalog.types.provisioning_artifact_detail.deserialize_cbor(
                data["ProvisioningArtifactDetail"]
            )
        )
    if data.get("Info") is not None:
        import capo_service_catalog.types.provisioning_artifact_info

        out["info"] = (
            capo_service_catalog.types.provisioning_artifact_info.deserialize_cbor(
                data["Info"]
            )
        )
    if data.get("Status") is not None:
        import capo_service_catalog.types.status

        out["status"] = capo_service_catalog.types.status.deserialize_cbor(
            data["Status"]
        )
    return out
