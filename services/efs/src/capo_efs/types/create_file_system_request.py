"""Generated from Smithy shape ``com.amazonaws.efs#CreateFileSystemRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.availability_zone_name
    import capo_efs.types.backup
    import capo_efs.types.creation_token
    import capo_efs.types.encrypted
    import capo_efs.types.kms_key_id
    import capo_efs.types.performance_mode
    import capo_efs.types.provisioned_throughput_in_mibps
    import capo_efs.types.tags
    import capo_efs.types.throughput_mode


class CreateFileSystemRequest(TypedDict, closed=True):
    creation_token: "capo_efs.types.creation_token.CreationToken"
    """<p>A string of up to 64 ASCII characters. Amazon EFS uses this to ensure idempotent creation.</p>"""
    performance_mode: NotRequired["capo_efs.types.performance_mode.PerformanceMode"]
    """<p>The performance mode of the file system. We recommend <code>generalPurpose</code> performance mode for all file systems. File systems using the <code>maxIO</code> performance mode can scale to higher levels of aggregate throughput and operations per second with a tradeoff of slightly higher latencies for most file operations. The performance mode can't be changed after the file system has been created. The <code>maxIO</code> mode is not supported on One Zone file systems.</p> <important> <p>Due to the higher per-operation latencies with Max I/O, we recommend using General Purpose performance mode for all file systems.</p> </important> <p>Default is <code>generalPurpose</code>.</p>"""
    encrypted: NotRequired["capo_efs.types.encrypted.Encrypted"]
    """<p>A Boolean value that, if true, creates an encrypted file system. When creating an encrypted file system, you have the option of specifying an existing Key Management Service key (KMS key). If you don't specify a KMS key, then the default KMS key for Amazon EFS, <code>/aws/elasticfilesystem</code>, is used to protect the encrypted file system. </p>"""
    kms_key_id: NotRequired["capo_efs.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the KMS key that you want to use to protect the encrypted file system. This parameter is required only if you want to use a non-default KMS key. If this parameter is not specified, the default KMS key for Amazon EFS is used. You can specify a KMS key ID using the following formats:</p> <ul> <li> <p>Key ID - A unique identifier of the key, for example <code>1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>ARN - An Amazon Resource Name (ARN) for the key, for example <code>arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab</code>.</p> </li> <li> <p>Key alias - A previously created display name for a key, for example <code>alias/projectKey1</code>.</p> </li> <li> <p>Key alias ARN - An ARN for a key alias, for example <code>arn:aws:kms:us-west-2:444455556666:alias/projectKey1</code>.</p> </li> </ul> <p>If you use <code>KmsKeyId</code>, you must set the <a>CreateFileSystemRequest$Encrypted</a> parameter to true.</p> <important> <p>EFS accepts only symmetric KMS keys. You cannot use asymmetric KMS keys with Amazon EFS file systems.</p> </important>"""
    throughput_mode: NotRequired["capo_efs.types.throughput_mode.ThroughputMode"]
    """<p>Specifies the throughput mode for the file system. The mode can be <code>bursting</code>, <code>provisioned</code>, or <code>elastic</code>. If you set <code>ThroughputMode</code> to <code>provisioned</code>, you must also set a value for <code>ProvisionedThroughputInMibps</code>. After you create the file system, you can decrease your file system's Provisioned throughput or change between the throughput modes, with certain time restrictions. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/performance.html#provisioned-throughput">Specifying throughput with provisioned mode</a> in the <i>Amazon EFS User Guide</i>. </p> <p>Default is <code>bursting</code>.</p>"""
    provisioned_throughput_in_mibps: NotRequired[
        "capo_efs.types.provisioned_throughput_in_mibps.ProvisionedThroughputInMibps"
    ]
    """<p>The throughput, measured in mebibytes per second (MiBps), that you want to provision for a file system that you're creating. Required if <code>ThroughputMode</code> is set to <code>provisioned</code>. Valid values are 1-3414 MiBps, with the upper limit depending on Region. To increase this limit, contact Amazon Web Services Support. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/limits.html#soft-limits">Amazon EFS quotas that you can increase</a> in the <i>Amazon EFS User Guide</i>.</p>"""
    availability_zone_name: NotRequired[
        "capo_efs.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>For One Zone file systems, specify the Amazon Web Services Availability Zone in which to create the file system. Use the format <code>us-east-1a</code> to specify the Availability Zone. For more information about One Zone file systems, see <a href="https://docs.aws.amazon.com/efs/latest/ug/availability-durability.html#file-system-type">EFS file system types</a> in the <i>Amazon EFS User Guide</i>.</p> <note> <p>One Zone file systems are not available in all Availability Zones in Amazon Web Services Regions where Amazon EFS is available.</p> </note>"""
    backup: NotRequired["capo_efs.types.backup.Backup"]
    """<p>Specifies whether automatic backups are enabled on the file system that you are creating. Set the value to <code>true</code> to enable automatic backups. If you are creating a One Zone file system, automatic backups are enabled by default. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/awsbackup.html#automatic-backups">Automatic backups</a> in the <i>Amazon EFS User Guide</i>.</p> <p>Default is <code>false</code>. However, if you specify an <code>AvailabilityZoneName</code>, the default is <code>true</code>.</p> <note> <p>Backup is not available in all Amazon Web Services Regions where Amazon EFS is available.</p> </note>"""
    tags: NotRequired["capo_efs.types.tags.Tags"]
    """<p>Use to create one or more tags associated with the file system. Each tag is a user-defined key-value pair. Name your file system on creation by including a <code>"Key":"Name","Value":"{value}"</code> key-value pair. Each key must be unique. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFileSystemRequest) -> dict:
    out: dict = {}
    out["CreationToken"] = value["creation_token"]
    if "performance_mode" in value:
        import capo_efs.types.performance_mode

        out["PerformanceMode"] = capo_efs.types.performance_mode.serialize_json(
            value["performance_mode"]
        )
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "throughput_mode" in value:
        import capo_efs.types.throughput_mode

        out["ThroughputMode"] = capo_efs.types.throughput_mode.serialize_json(
            value["throughput_mode"]
        )
    if "provisioned_throughput_in_mibps" in value:
        out["ProvisionedThroughputInMibps"] = (
            "NaN"
            if value["provisioned_throughput_in_mibps"]
            != value["provisioned_throughput_in_mibps"]
            else "Infinity"
            if value["provisioned_throughput_in_mibps"] == float("inf")
            else "-Infinity"
            if value["provisioned_throughput_in_mibps"] == float("-inf")
            else value["provisioned_throughput_in_mibps"]
        )
    if "availability_zone_name" in value:
        out["AvailabilityZoneName"] = value["availability_zone_name"]
    if "backup" in value:
        out["Backup"] = value["backup"]
    if "tags" in value:
        import capo_efs.types.tags

        out["Tags"] = capo_efs.types.tags.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateFileSystemRequest:
    out: CreateFileSystemRequest = {}  # type: ignore[typeddict-item]
    if data.get("CreationToken") is not None:
        out["creation_token"] = data["CreationToken"]
    else:
        raise DeserializationError("CreateFileSystemRequest.creation_token required")
    if data.get("PerformanceMode") is not None:
        import capo_efs.types.performance_mode

        out["performance_mode"] = capo_efs.types.performance_mode.deserialize_json(
            data["PerformanceMode"]
        )
    if data.get("Encrypted") is not None:
        out["encrypted"] = data["Encrypted"]
    if data.get("KmsKeyId") is not None:
        out["kms_key_id"] = data["KmsKeyId"]
    if data.get("ThroughputMode") is not None:
        import capo_efs.types.throughput_mode

        out["throughput_mode"] = capo_efs.types.throughput_mode.deserialize_json(
            data["ThroughputMode"]
        )
    if data.get("ProvisionedThroughputInMibps") is not None:
        out["provisioned_throughput_in_mibps"] = float(
            data["ProvisionedThroughputInMibps"]
        )
    if data.get("AvailabilityZoneName") is not None:
        out["availability_zone_name"] = data["AvailabilityZoneName"]
    if data.get("Backup") is not None:
        out["backup"] = data["Backup"]
    if data.get("Tags") is not None:
        import capo_efs.types.tags

        out["tags"] = capo_efs.types.tags.deserialize_json(data["Tags"])
    return out
