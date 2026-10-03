"""Generated from Smithy shape ``com.amazonaws.efs#DestinationToCreate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_efs.types.availability_zone_name
    import capo_efs.types.file_system_id
    import capo_efs.types.kms_key_id
    import capo_efs.types.region_name
    import capo_efs.types.role_arn


class DestinationToCreate(TypedDict, closed=True):
    region: NotRequired["capo_efs.types.region_name.RegionName"]
    """<p>To create a file system that uses Regional storage, specify the Amazon Web Services Region in which to create the destination file system. The Region must be enabled for the Amazon Web Services account that owns the source file system. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable">Managing Amazon Web Services Regions</a> in the <i>Amazon Web Services General Reference Reference Guide</i>.</p>"""
    availability_zone_name: NotRequired[
        "capo_efs.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>To create a file system that uses One Zone storage, specify the name of the Availability Zone in which to create the destination file system.</p>"""
    kms_key_id: NotRequired["capo_efs.types.kms_key_id.KmsKeyId"]
    """<p>Specify the Key Management Service (KMS) key that you want to use to encrypt the destination file system. If you do not specify a KMS key, Amazon EFS uses your default KMS key for Amazon EFS, <code>/aws/elasticfilesystem</code>. This ID can be in one of the following formats:</p> <ul> <li> <p>Key ID - The unique identifier of the key, for example <code>1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>ARN - The ARN for the key, for example <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Key alias - A previously created display name for a key, for example <code>alias/projectKey1</code>.</p> </li> <li> <p>Key alias ARN - The ARN for a key alias, for example <code>arn:aws:kms:us-west-2:444455556666:alias/projectKey1</code>.</p> </li> </ul>"""
    file_system_id: NotRequired["capo_efs.types.file_system_id.FileSystemId"]
    """<p>The ID or ARN of the file system to use for the destination. For cross-account replication, this must be an ARN. The file system's replication overwrite replication must be disabled. If no ID or ARN is specified, then a new file system is created. </p> <note> <p>When you initially configure replication to an existing file system, Amazon EFS writes data to or removes existing data from the destination file system to match data in the source file system. If you don't want to change data in the destination file system, then you should replicate to a new file system instead. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/create-replication.html">https://docs.aws.amazon.com/efs/latest/ug/create-replication.html</a>.</p> </note>"""
    role_arn: NotRequired["capo_efs.types.role_arn.RoleArn"]
    """<p>Amazon Resource Name (ARN) of the IAM role in the source account that allows Amazon EFS to perform replication on its behalf. This is optional for same-account replication and required for cross-account replication.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DestinationToCreate) -> dict:
    out: dict = {}
    if "region" in value:
        out["Region"] = value["region"]
    if "availability_zone_name" in value:
        out["AvailabilityZoneName"] = value["availability_zone_name"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "file_system_id" in value:
        out["FileSystemId"] = value["file_system_id"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    return out


def deserialize_json(data: dict) -> DestinationToCreate:
    out: DestinationToCreate = {}  # type: ignore[typeddict-item]
    if data.get("Region") is not None:
        out["region"] = data["Region"]
    if data.get("AvailabilityZoneName") is not None:
        out["availability_zone_name"] = data["AvailabilityZoneName"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    if data.get("RoleArn") is not None:
        out["role_arn"] = data["RoleArn"]
    return out
