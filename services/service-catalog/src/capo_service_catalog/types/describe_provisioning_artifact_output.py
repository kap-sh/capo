"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProvisioningArtifactOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.provisioning_artifact_detail
    import capo_service_catalog.types.provisioning_artifact_info
    import capo_service_catalog.types.provisioning_artifact_parameters
    import capo_service_catalog.types.status


class DescribeProvisioningArtifactOutput(TypedDict, closed=True):
    provisioning_artifact_detail: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_detail.ProvisioningArtifactDetail"
    ]
    """<p>Information about the provisioning artifact.</p>"""
    info: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_info.ProvisioningArtifactInfo"
    ]
    """<p>The URL of the CloudFormation template in Amazon S3 or GitHub in JSON format.</p>"""
    status: NotRequired["capo_service_catalog.types.status.Status"]
    """<p>The status of the current request.</p>"""
    provisioning_artifact_parameters: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_parameters.ProvisioningArtifactParameters"
    ]
    """<p>Information about the parameters used to provision the product. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProvisioningArtifactOutput) -> dict:
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
    if "provisioning_artifact_parameters" in value:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["ProvisioningArtifactParameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.serialize_aws_json_1_1(
                value["provisioning_artifact_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProvisioningArtifactOutput:
    out: DescribeProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("ProvisioningArtifactParameters") is not None:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["provisioning_artifact_parameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.deserialize_aws_json_1_1(
                data["ProvisioningArtifactParameters"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProvisioningArtifactOutput) -> dict:
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
    if "provisioning_artifact_parameters" in value:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["ProvisioningArtifactParameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.serialize_cbor(
                value["provisioning_artifact_parameters"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> DescribeProvisioningArtifactOutput:
    out: DescribeProvisioningArtifactOutput = {}  # type: ignore[typeddict-item]
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
    if data.get("ProvisioningArtifactParameters") is not None:
        import capo_service_catalog.types.provisioning_artifact_parameters

        out["provisioning_artifact_parameters"] = (
            capo_service_catalog.types.provisioning_artifact_parameters.deserialize_cbor(
                data["ProvisioningArtifactParameters"]
            )
        )
    return out
