"""Generated from Smithy shape ``com.amazonaws.ecs#S3FilesVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.string


class S3FilesVolumeConfiguration(TypedDict, closed=True):
    file_system_arn: "capo_ecs.types.string.String"
    """<p>The full ARN of the S3 Files file system to mount.</p>"""
    root_directory: NotRequired["capo_ecs.types.string.String"]
    """<p>The directory within the Amazon S3 Files file system to mount as the root directory. If this parameter is omitted, the root of the Amazon S3 Files file system will be used. Specifying <code>/</code> will have the same effect as omitting this parameter.</p> <important> <p>If a S3 Files access point is specified in the <code>accessPointArn</code>, the root directory parameter must either be omitted or set to <code>/</code> which will enforce the path set on the S3 Files access point.</p> </important>"""
    transit_encryption_port: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The port to use for sending encrypted data between the ECS host and the S3 Files file system. If you do not specify a transit encryption port, it will use the port selection strategy that the Amazon S3 Files mount helper uses. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-mounting.html">S3 Files mount helper</a>.</p>"""
    access_point_arn: NotRequired["capo_ecs.types.string.String"]
    """<p>The full ARN of the S3 Files access point to use. If an access point is specified, the root directory value specified in the <code>S3FilesVolumeConfiguration</code> must either be omitted or set to <code>/</code> which will enforce the path set on the S3 Files access point. For more information, see <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-files-access-points-creating.html">Creating S3 Files access points</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3FilesVolumeConfiguration) -> dict:
    out: dict = {}
    out["fileSystemArn"] = value["file_system_arn"]
    if "root_directory" in value:
        out["rootDirectory"] = value["root_directory"]
    if "transit_encryption_port" in value:
        out["transitEncryptionPort"] = value["transit_encryption_port"]
    if "access_point_arn" in value:
        out["accessPointArn"] = value["access_point_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3FilesVolumeConfiguration:
    out: S3FilesVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("fileSystemArn") is not None:
        out["file_system_arn"] = data["fileSystemArn"]
    else:
        raise DeserializationError(
            "S3FilesVolumeConfiguration.file_system_arn required"
        )
    if data.get("rootDirectory") is not None:
        out["root_directory"] = data["rootDirectory"]
    if data.get("transitEncryptionPort") is not None:
        out["transit_encryption_port"] = data["transitEncryptionPort"]
    if data.get("accessPointArn") is not None:
        out["access_point_arn"] = data["accessPointArn"]
    return out
