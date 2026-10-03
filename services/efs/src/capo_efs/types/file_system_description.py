"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_efs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_efs.types.availability_zone_id
    import capo_efs.types.availability_zone_name
    import capo_efs.types.aws_account_id
    import capo_efs.types.creation_token
    import capo_efs.types.encrypted
    import capo_efs.types.file_system_arn
    import capo_efs.types.file_system_id
    import capo_efs.types.file_system_protection_description
    import capo_efs.types.file_system_size
    import capo_efs.types.kms_key_id
    import capo_efs.types.life_cycle_state
    import capo_efs.types.mount_target_count
    import capo_efs.types.performance_mode
    import capo_efs.types.provisioned_throughput_in_mibps
    import capo_efs.types.tag_value
    import capo_efs.types.tags
    import capo_efs.types.throughput_mode
    import capo_efs.types.timestamp


class FileSystemDescription(TypedDict, closed=True):
    owner_id: "capo_efs.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account that created the file system.</p>"""
    creation_token: "capo_efs.types.creation_token.CreationToken"
    """<p>The opaque string specified in the request.</p>"""
    file_system_id: "capo_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system, assigned by Amazon EFS.</p>"""
    file_system_arn: NotRequired["capo_efs.types.file_system_arn.FileSystemArn"]
    """<p>The Amazon Resource Name (ARN) for the EFS file system, in the format <code>arn:aws:elasticfilesystem:<i>region</i>:<i>account-id</i>:file-system/<i>file-system-id</i> </code>. Example with sample data: <code>arn:aws:elasticfilesystem:us-west-2:1111333322228888:file-system/fs-01234567</code> </p>"""
    creation_time: "capo_efs.types.timestamp.Timestamp"
    """<p>The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).</p>"""
    life_cycle_state: "capo_efs.types.life_cycle_state.LifeCycleState"
    """<p>The lifecycle phase of the file system.</p>"""
    name: NotRequired["capo_efs.types.tag_value.TagValue"]
    """<p>You can add tags to a file system, including a <code>Name</code> tag. For more information, see <a>CreateFileSystem</a>. If the file system has a <code>Name</code> tag, Amazon EFS returns the value in this field. </p>"""
    number_of_mount_targets: "capo_efs.types.mount_target_count.MountTargetCount"
    """<p>The current number of mount targets that the file system has. For more information, see <a>CreateMountTarget</a>.</p>"""
    size_in_bytes: "capo_efs.types.file_system_size.FileSystemSize"
    """<p>The latest known metered size (in bytes) of data stored in the file system, in its <code>Value</code> field, and the time at which that size was determined in its <code>Timestamp</code> field. The <code>Timestamp</code> value is the integer number of seconds since 1970-01-01T00:00:00Z. The <code>SizeInBytes</code> value doesn't represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, <code>SizeInBytes</code> represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time. </p>"""
    performance_mode: "capo_efs.types.performance_mode.PerformanceMode"
    """<p>The performance mode of the file system.</p>"""
    encrypted: NotRequired["capo_efs.types.encrypted.Encrypted"]
    """<p>A Boolean value that, if true, indicates that the file system is encrypted.</p>"""
    kms_key_id: NotRequired["capo_efs.types.kms_key_id.KmsKeyId"]
    """<p>The ID of an KMS key used to protect the encrypted file system.</p>"""
    throughput_mode: NotRequired["capo_efs.types.throughput_mode.ThroughputMode"]
    """<p>Displays the file system's throughput mode. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes">Throughput modes</a> in the <i>Amazon EFS User Guide</i>. </p>"""
    provisioned_throughput_in_mibps: NotRequired[
        "capo_efs.types.provisioned_throughput_in_mibps.ProvisionedThroughputInMibps"
    ]
    """<p>The amount of provisioned throughput, measured in MiBps, for the file system. Valid for file systems using <code>ThroughputMode</code> set to <code>provisioned</code>.</p>"""
    availability_zone_name: NotRequired[
        "capo_efs.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>Describes the Amazon Web Services Availability Zone in which the file system is located, and is valid only for One Zone file systems. For more information, see <a href="https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html">Using EFS storage classes</a> in the <i>Amazon EFS User Guide</i>.</p>"""
    availability_zone_id: NotRequired[
        "capo_efs.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The unique and consistent identifier of the Availability Zone in which the file system is located, and is valid only for One Zone file systems. For example, <code>use1-az1</code> is an Availability Zone ID for the us-east-1 Amazon Web Services Region, and it has the same location in every Amazon Web Services account.</p>"""
    tags: "capo_efs.types.tags.Tags"
    """<p>The tags associated with the file system, presented as an array of <code>Tag</code> objects.</p>"""
    file_system_protection: NotRequired[
        "capo_efs.types.file_system_protection_description.FileSystemProtectionDescription"
    ]
    """<p>Describes the protection on the file system. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemDescription) -> dict:
    out: dict = {}
    out["OwnerId"] = value["owner_id"]
    out["CreationToken"] = value["creation_token"]
    out["FileSystemId"] = value["file_system_id"]
    if "file_system_arn" in value:
        out["FileSystemArn"] = value["file_system_arn"]
    import capo_efs.types.timestamp

    out["CreationTime"] = capo_efs.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_efs.types.life_cycle_state

    out["LifeCycleState"] = capo_efs.types.life_cycle_state.serialize_json(
        value["life_cycle_state"]
    )
    if "name" in value:
        out["Name"] = value["name"]
    out["NumberOfMountTargets"] = value.get("number_of_mount_targets", 0)
    import capo_efs.types.file_system_size

    out["SizeInBytes"] = capo_efs.types.file_system_size.serialize_json(
        value["size_in_bytes"]
    )
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
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    import capo_efs.types.tags

    out["Tags"] = capo_efs.types.tags.serialize_json(value["tags"])
    if "file_system_protection" in value:
        import capo_efs.types.file_system_protection_description

        out["FileSystemProtection"] = (
            capo_efs.types.file_system_protection_description.serialize_json(
                value["file_system_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> FileSystemDescription:
    out: FileSystemDescription = {}  # type: ignore[typeddict-item]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    else:
        raise DeserializationError("FileSystemDescription.owner_id required")
    if data.get("CreationToken") is not None:
        out["creation_token"] = data["CreationToken"]
    else:
        raise DeserializationError("FileSystemDescription.creation_token required")
    if data.get("FileSystemId") is not None:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("FileSystemDescription.file_system_id required")
    if data.get("FileSystemArn") is not None:
        out["file_system_arn"] = data["FileSystemArn"]
    if data.get("CreationTime") is not None:
        import capo_efs.types.timestamp

        out["creation_time"] = capo_efs.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        raise DeserializationError("FileSystemDescription.creation_time required")
    if data.get("LifeCycleState") is not None:
        import capo_efs.types.life_cycle_state

        out["life_cycle_state"] = capo_efs.types.life_cycle_state.deserialize_json(
            data["LifeCycleState"]
        )
    else:
        raise DeserializationError("FileSystemDescription.life_cycle_state required")
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("NumberOfMountTargets") is not None:
        out["number_of_mount_targets"] = data["NumberOfMountTargets"]
    else:
        out["number_of_mount_targets"] = 0
    if data.get("SizeInBytes") is not None:
        import capo_efs.types.file_system_size

        out["size_in_bytes"] = capo_efs.types.file_system_size.deserialize_json(
            data["SizeInBytes"]
        )
    else:
        raise DeserializationError("FileSystemDescription.size_in_bytes required")
    if data.get("PerformanceMode") is not None:
        import capo_efs.types.performance_mode

        out["performance_mode"] = capo_efs.types.performance_mode.deserialize_json(
            data["PerformanceMode"]
        )
    else:
        raise DeserializationError("FileSystemDescription.performance_mode required")
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
    if data.get("AvailabilityZoneId") is not None:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if data.get("Tags") is not None:
        import capo_efs.types.tags

        out["tags"] = capo_efs.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("FileSystemDescription.tags required")
    if data.get("FileSystemProtection") is not None:
        import capo_efs.types.file_system_protection_description

        out["file_system_protection"] = (
            capo_efs.types.file_system_protection_description.deserialize_json(
                data["FileSystemProtection"]
            )
        )
    return out
