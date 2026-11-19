"""Generated from Smithy shape ``com.amazonaws.appstream#CreateExportImageTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.ami_name
    import capo_appstream.types.arn
    import capo_appstream.types.description
    import capo_appstream.types.name
    import capo_appstream.types.tags


class CreateExportImageTaskRequest(TypedDict, closed=True):
    image_name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the WorkSpaces Applications image to export. The image must be in an available state and owned by your account.</p>"""
    ami_name: NotRequired["capo_appstream.types.ami_name.AmiName"]
    """<p>The name for the exported EC2 AMI. This is a required field that must be unique within your account and region.</p>"""
    iam_role_arn: NotRequired["capo_appstream.types.arn.Arn"]
    """<p>The ARN of the IAM role that allows WorkSpaces Applications to create the AMI. The role must have permissions to copy images, describe images, and create tags, with a trust relationship allowing appstream.amazonaws.com to assume the role.</p>"""
    tag_specifications: NotRequired["capo_appstream.types.tags.Tags"]
    """<p>The tags to apply to the exported AMI. These tags help you organize and manage your EC2 AMIs.</p>"""
    ami_description: NotRequired["capo_appstream.types.description.Description"]
    """<p>An optional description for the exported AMI. This description will be applied to the resulting EC2 AMI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateExportImageTaskRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "ami_name" in value:
        out["AmiName"] = value["ami_name"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "tag_specifications" in value:
        import capo_appstream.types.tags

        out["TagSpecifications"] = capo_appstream.types.tags.serialize_aws_json_1_1(
            value["tag_specifications"]
        )
    if "ami_description" in value:
        out["AmiDescription"] = value["ami_description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateExportImageTaskRequest:
    out: CreateExportImageTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    if data.get("AmiName") is not None:
        out["ami_name"] = data["AmiName"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("TagSpecifications") is not None:
        import capo_appstream.types.tags

        out["tag_specifications"] = capo_appstream.types.tags.deserialize_aws_json_1_1(
            data["TagSpecifications"]
        )
    if data.get("AmiDescription") is not None:
        out["ami_description"] = data["AmiDescription"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateExportImageTaskRequest) -> dict:
    out: dict = {}
    if "image_name" in value:
        out["ImageName"] = value["image_name"]
    if "ami_name" in value:
        out["AmiName"] = value["ami_name"]
    if "iam_role_arn" in value:
        out["IamRoleArn"] = value["iam_role_arn"]
    if "tag_specifications" in value:
        import capo_appstream.types.tags

        out["TagSpecifications"] = capo_appstream.types.tags.serialize_cbor(
            value["tag_specifications"]
        )
    if "ami_description" in value:
        out["AmiDescription"] = value["ami_description"]
    return out


def deserialize_cbor(data: dict) -> CreateExportImageTaskRequest:
    out: CreateExportImageTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("ImageName") is not None:
        out["image_name"] = data["ImageName"]
    if data.get("AmiName") is not None:
        out["ami_name"] = data["AmiName"]
    if data.get("IamRoleArn") is not None:
        out["iam_role_arn"] = data["IamRoleArn"]
    if data.get("TagSpecifications") is not None:
        import capo_appstream.types.tags

        out["tag_specifications"] = capo_appstream.types.tags.deserialize_cbor(
            data["TagSpecifications"]
        )
    if data.get("AmiDescription") is not None:
        out["ami_description"] = data["AmiDescription"]
    return out
