"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationEfsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import capo_datasync.types.efs_in_transit_encryption
    import capo_datasync.types.efs_subdirectory
    import capo_datasync.types.location_arn
    import capo_datasync.types.updated_efs_access_point_arn
    import capo_datasync.types.updated_efs_iam_role_arn


class UpdateLocationEfsRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the Amazon EFS transfer location that you're updating.</p>"""
    subdirectory: NotRequired["capo_datasync.types.efs_subdirectory.EfsSubdirectory"]
    """<p>Specifies a mount path for your Amazon EFS file system. This is where DataSync reads or writes data on your file system (depending on if this is a source or destination location).</p> <p>By default, DataSync uses the root directory (or <a href="https://docs.aws.amazon.com/efs/latest/ug/efs-access-points.html">access point</a> if you provide one by using <code>AccessPointArn</code>). You can also include subdirectories using forward slashes (for example, <code>/path/to/folder</code>).</p>"""
    access_point_arn: NotRequired[
        "capo_datasync.types.updated_efs_access_point_arn.UpdatedEfsAccessPointArn"
    ]
    """<p>Specifies the Amazon Resource Name (ARN) of the access point that DataSync uses to mount your Amazon EFS file system.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam">Accessing restricted Amazon EFS file systems</a>.</p>"""
    file_system_access_role_arn: NotRequired[
        "capo_datasync.types.updated_efs_iam_role_arn.UpdatedEfsIamRoleArn"
    ]
    """<p>Specifies an Identity and Access Management (IAM) role that allows DataSync to access your Amazon EFS file system.</p> <p>For information on creating this role, see <a href="https://docs.aws.amazon.com/datasync/latest/userguide/create-efs-location.html#create-efs-location-iam-role">Creating a DataSync IAM role for Amazon EFS file system access</a>.</p>"""
    in_transit_encryption: NotRequired[
        "capo_datasync.types.efs_in_transit_encryption.EfsInTransitEncryption"
    ]
    """<p>Specifies whether you want DataSync to use Transport Layer Security (TLS) 1.2 encryption when it transfers data to or from your Amazon EFS file system.</p> <p>If you specify an access point using <code>AccessPointArn</code> or an IAM role using <code>FileSystemAccessRoleArn</code>, you must set this parameter to <code>TLS1_2</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationEfsRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
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


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationEfsRequest:
    out: UpdateLocationEfsRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        raise DeserializationError("UpdateLocationEfsRequest.location_arn required")
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
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
