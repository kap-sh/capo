"""Generated from Smithy shape ``com.amazonaws.datasync#CreateLocationEfsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.ec2_config
    import capo_datasync.types.efs_access_point_arn
    import capo_datasync.types.efs_filesystem_arn
    import capo_datasync.types.efs_in_transit_encryption
    import capo_datasync.types.efs_subdirectory
    import capo_datasync.types.iam_role_arn
    import capo_datasync.types.input_tag_list


class CreateLocationEfsRequest(TypedDict, closed=True):
    subdirectory: NotRequired["capo_datasync.types.efs_subdirectory.EfsSubdirectory"]
    """<p>Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or destination location).</p> <p>By default, DataSync uses the root directory (or <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html">access point</a> if you provide one by using <code>AccessPointArn</code>). You can also include subdirectories using forward slashes (for example, <code>/path/to/folder</code>).</p>"""
    efs_filesystem_arn: "capo_datasync.types.efs_filesystem_arn.EfsFilesystemArn"
    """<p>Specifies the ARN for your Amazon EFS file system.</p>"""
    ec2_config: "capo_datasync.types.ec2_config.Ec2Config"
    """<p>Specifies the subnet and security groups DataSync uses to connect to one of your Amazon EFS file system's <a href="https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html">mount targets</a>.</p>"""
    tags: NotRequired["capo_datasync.types.input_tag_list.InputTagList"]
    """<p>Specifies the key-value pair that represents a tag that you want to add to the resource. The value can be an empty string. This value helps you manage, filter, and search for your resources. We recommend that you create a name tag for your location.</p>"""
    access_point_arn: NotRequired[
        "capo_datasync.types.efs_access_point_arn.EfsAccessPointArn"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to mount your Amazon EFS file system.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam">Accessing restricted file systems</a>.</p>"""
    file_system_access_role_arn: NotRequired[
        "capo_datasync.types.iam_role_arn.IamRoleArn"
    ]
    """<p>Specifies an Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.</p> <p>For information on creating this role, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role">Creating a DataSync IAM role for file system access</a>.</p>"""
    in_transit_encryption: NotRequired[
        "capo_datasync.types.efs_in_transit_encryption.EfsInTransitEncryption"
    ]
    """<p>Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it transfers data to or from your Amazon EFS file system.</p> <p>If you specify an access point using <code>AccessPointArn</code> or an IAM role using <code>FileSystemAccessRoleArn</code>, you must set this parameter to <code>TLS1_2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateLocationEfsRequest) -> dict:
    out: dict = {}
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    out["EfsFilesystemArn"] = value["efs_filesystem_arn"]
    import capo_datasync.types.ec2_config

    out["Ec2Config"] = capo_datasync.types.ec2_config.serialize_aws_json_1_1(
        value["ec2_config"]
    )
    if "tags" in value:
        import capo_datasync.types.input_tag_list

        out["Tags"] = capo_datasync.types.input_tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "access_point_arn" in value:
        out["AccessPointArn"] = value["access_point_arn"]
    if "file_system_access_role_arn" in value:
        out["FileSystemAccessRoleArn"] = value["file_system_access_role_arn"]
    if "in_transit_encryption" in value:
        import capo_datasync.types.efs_in_transit_encryption

        out["InTransitEncryption"] = (
            capo_datasync.types.efs_in_transit_encryption.serialize_aws_json_1_1(
                value["in_transit_encryption"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateLocationEfsRequest:
    out: CreateLocationEfsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    if data.get("EfsFilesystemArn") is not None:
        out["efs_filesystem_arn"] = data["EfsFilesystemArn"]
    else:
        raise DeserializationError(
            "CreateLocationEfsRequest.efs_filesystem_arn required"
        )
    if data.get("Ec2Config") is not None:
        import capo_datasync.types.ec2_config

        out["ec2_config"] = capo_datasync.types.ec2_config.deserialize_aws_json_1_1(
            data["Ec2Config"]
        )
    else:
        raise DeserializationError("CreateLocationEfsRequest.ec2_config required")
    if data.get("Tags") is not None:
        import capo_datasync.types.input_tag_list

        out["tags"] = capo_datasync.types.input_tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("AccessPointArn") is not None:
        out["access_point_arn"] = data["AccessPointArn"]
    if data.get("FileSystemAccessRoleArn") is not None:
        out["file_system_access_role_arn"] = data["FileSystemAccessRoleArn"]
    if data.get("InTransitEncryption") is not None:
        import capo_datasync.types.efs_in_transit_encryption

        out["in_transit_encryption"] = (
            capo_datasync.types.efs_in_transit_encryption.deserialize_aws_json_1_1(
                data["InTransitEncryption"]
            )
        )
    return out
