"""Generated from Smithy shape ``com.amazonaws.appstream#SoftwareAssociations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.error_details_list
    import capo_appstream.types.software_deployment_status
    import capo_appstream.types.string


class SoftwareAssociations(TypedDict, closed=True):
    software_name: NotRequired["capo_appstream.types.string.String"]
    """<p>The name of the license-included application.</p> <p>Possible values include the following:</p> <ul> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Professional_Plus_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Professional_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Professional_64Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Office_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2021_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_32Bit</p> </li> <li> <p>Microsoft_Visio_2024_LTSC_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2021_Standard_64Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_32Bit</p> </li> <li> <p>Microsoft_Project_2024_Standard_64Bit</p> </li> </ul>"""
    status: NotRequired[
        "capo_appstream.types.software_deployment_status.SoftwareDeploymentStatus"
    ]
    """<p>The deployment status of the license-included application.</p>"""
    deployment_error: NotRequired[
        "capo_appstream.types.error_details_list.ErrorDetailsList"
    ]
    """<p>The error details for failed deployments of the license-included application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SoftwareAssociations) -> dict:
    out: dict = {}
    if "software_name" in value:
        out["SoftwareName"] = value["software_name"]
    if "status" in value:
        import capo_appstream.types.software_deployment_status

        out["Status"] = (
            capo_appstream.types.software_deployment_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "deployment_error" in value:
        import capo_appstream.types.error_details_list

        out["DeploymentError"] = (
            capo_appstream.types.error_details_list.serialize_aws_json_1_1(
                value["deployment_error"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SoftwareAssociations:
    out: SoftwareAssociations = {}  # type: ignore[typeddict-item]
    if data.get("SoftwareName") is not None:
        out["software_name"] = data["SoftwareName"]
    if data.get("Status") is not None:
        import capo_appstream.types.software_deployment_status

        out["status"] = (
            capo_appstream.types.software_deployment_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if data.get("DeploymentError") is not None:
        import capo_appstream.types.error_details_list

        out["deployment_error"] = (
            capo_appstream.types.error_details_list.deserialize_aws_json_1_1(
                data["DeploymentError"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SoftwareAssociations) -> dict:
    out: dict = {}
    if "software_name" in value:
        out["SoftwareName"] = value["software_name"]
    if "status" in value:
        import capo_appstream.types.software_deployment_status

        out["Status"] = capo_appstream.types.software_deployment_status.serialize_cbor(
            value["status"]
        )
    if "deployment_error" in value:
        import capo_appstream.types.error_details_list

        out["DeploymentError"] = capo_appstream.types.error_details_list.serialize_cbor(
            value["deployment_error"]
        )
    return out


def deserialize_cbor(data: dict) -> SoftwareAssociations:
    out: SoftwareAssociations = {}  # type: ignore[typeddict-item]
    if data.get("SoftwareName") is not None:
        out["software_name"] = data["SoftwareName"]
    if data.get("Status") is not None:
        import capo_appstream.types.software_deployment_status

        out["status"] = (
            capo_appstream.types.software_deployment_status.deserialize_cbor(
                data["Status"]
            )
        )
    if data.get("DeploymentError") is not None:
        import capo_appstream.types.error_details_list

        out["deployment_error"] = (
            capo_appstream.types.error_details_list.deserialize_cbor(
                data["DeploymentError"]
            )
        )
    return out
