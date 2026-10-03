"""Generated from Smithy shape ``com.amazonaws.workspaces#ImportWorkspaceImageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_workspaces.errors import DeserializationError

if TYPE_CHECKING:
    import capo_workspaces.types.application_list
    import capo_workspaces.types.ec2_image_id
    import capo_workspaces.types.tag_list
    import capo_workspaces.types.workspace_image_description
    import capo_workspaces.types.workspace_image_ingestion_process
    import capo_workspaces.types.workspace_image_name


class ImportWorkspaceImageRequest(TypedDict, closed=True):
    ec2_image_id: "capo_workspaces.types.ec2_image_id.Ec2ImageId"
    """<p>The identifier of the EC2 image.</p>"""
    ingestion_process: "capo_workspaces.types.workspace_image_ingestion_process.WorkspaceImageIngestionProcess"
    """<p>The ingestion process to be used when importing the image, depending on which protocol you want to use for your BYOL Workspace image, either PCoIP, WSP, or bring your own protocol (BYOP). To use DCV, specify a value that ends in <code>_WSP</code>. To use PCoIP, specify a value that does not end in <code>_WSP</code>. To use BYOP, specify a value that ends in <code>_BYOP</code>.</p> <p>For non-GPU-enabled bundles (bundles other than Graphics or GraphicsPro), specify <code>BYOL_REGULAR</code>, <code>BYOL_REGULAR_WSP</code>, or <code>BYOL_REGULAR_BYOP</code>, depending on the protocol.</p> <note> <p>The <code>BYOL_REGULAR_BYOP</code> and <code>BYOL_GRAPHICS_G4DN_BYOP</code> values are only supported by Amazon WorkSpaces Core. Contact your account team to be allow-listed to use these values. For more information, see <a href="http://aws.amazon.com/workspaces/core/">Amazon WorkSpaces Core</a>.</p> </note>"""
    image_name: "capo_workspaces.types.workspace_image_name.WorkspaceImageName"
    """<p>The name of the WorkSpace image.</p>"""
    image_description: (
        "capo_workspaces.types.workspace_image_description.WorkspaceImageDescription"
    )
    """<p>The description of the WorkSpace image.</p>"""
    tags: NotRequired["capo_workspaces.types.tag_list.TagList"]
    """<p>The tags. Each WorkSpaces resource can have a maximum of 50 tags.</p>"""
    applications: NotRequired["capo_workspaces.types.application_list.ApplicationList"]
    """<p>If specified, the version of Microsoft Office to subscribe to. Valid only for Windows 10 and 11 BYOL images. For more information about subscribing to Office for BYOL images, see <a href="https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html"> Bring Your Own Windows Desktop Licenses</a>.</p> <note> <ul> <li> <p>Although this parameter is an array, only one item is allowed at this time.</p> </li> <li> <p>During the image import process, non-GPU DCV (formerly WSP) WorkSpaces with Windows 11 support only <code>Microsoft_Office_2019</code>. GPU DCV (formerly WSP) WorkSpaces with Windows 11 do not support Office installation.</p> </li> </ul> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportWorkspaceImageRequest) -> dict:
    out: dict = {}
    out["Ec2ImageId"] = value["ec2_image_id"]
    import capo_workspaces.types.workspace_image_ingestion_process

    out["IngestionProcess"] = (
        capo_workspaces.types.workspace_image_ingestion_process.serialize_aws_json_1_1(
            value["ingestion_process"]
        )
    )
    out["ImageName"] = value["image_name"]
    out["ImageDescription"] = value["image_description"]
    if "tags" in value:
        import capo_workspaces.types.tag_list

        out["Tags"] = capo_workspaces.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "applications" in value:
        import capo_workspaces.types.application_list

        out["Applications"] = (
            capo_workspaces.types.application_list.serialize_aws_json_1_1(
                value["applications"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportWorkspaceImageRequest:
    out: ImportWorkspaceImageRequest = {}  # type: ignore[typeddict-item]
    if data.get("Ec2ImageId") is not None:
        out["ec2_image_id"] = data["Ec2ImageId"]
    else:
        raise DeserializationError("ImportWorkspaceImageRequest.ec2_image_id required")
    if data.get("IngestionProcess") is not None:
        import capo_workspaces.types.workspace_image_ingestion_process

        out["ingestion_process"] = (
            capo_workspaces.types.workspace_image_ingestion_process.deserialize_aws_json_1_1(
                data["IngestionProcess"]
            )
        )
    else:
        raise DeserializationError(
            "ImportWorkspaceImageRequest.ingestion_process required"
        )
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    else:
        raise DeserializationError("ImportWorkspaceImageRequest.image_name required")
    if data.get("ImageDescription") is not None:
        out["image_description"] = data["ImageDescription"]
    else:
        raise DeserializationError(
            "ImportWorkspaceImageRequest.image_description required"
        )
    if data.get("Tags") is not None:
        import capo_workspaces.types.tag_list

        out["tags"] = capo_workspaces.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("Applications") is not None:
        import capo_workspaces.types.application_list

        out["applications"] = (
            capo_workspaces.types.application_list.deserialize_aws_json_1_1(
                data["Applications"]
            )
        )
    return out
