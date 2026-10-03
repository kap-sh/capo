"""Generated from Smithy shape ``com.amazonaws.ecs#TaskManagedEBSVolumeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ecs.errors import DeserializationError

if TYPE_CHECKING:
    import capo_ecs.types.boxed_boolean
    import capo_ecs.types.boxed_integer
    import capo_ecs.types.ebs_snapshot_id
    import capo_ecs.types.ebs_tag_specifications
    import capo_ecs.types.ebs_volume_type
    import capo_ecs.types.ebskms_key_id
    import capo_ecs.types.iam_role_arn
    import capo_ecs.types.task_filesystem_type
    import capo_ecs.types.task_managed_ebs_volume_termination_policy


class TaskManagedEBSVolumeConfiguration(TypedDict, closed=True):
    encrypted: NotRequired["capo_ecs.types.boxed_boolean.BoxedBoolean"]
    """<p>Indicates whether the volume should be encrypted. If you turn on Region-level Amazon EBS encryption by default but set this value as <code>false</code>, the setting is overridden and the volume is encrypted with the KMS key specified for Amazon EBS encryption by default. This parameter maps 1:1 with the <code>Encrypted</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    kms_key_id: NotRequired["capo_ecs.types.ebskms_key_id.EBSKMSKeyId"]
    """<p>The Amazon Resource Name (ARN) identifier of the Amazon Web Services Key Management Service key to use for Amazon EBS encryption. When a key is specified using this parameter, it overrides Amazon EBS default encryption or any KMS key that you specified for cluster-level managed storage encryption. This parameter maps 1:1 with the <code>KmsKeyId</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>. For more information about encrypting Amazon EBS volumes attached to a task, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ebs-kms-encryption.html">Encrypt data stored in Amazon EBS volumes attached to Amazon ECS tasks</a>.</p> <important> <p>Amazon Web Services authenticates the Amazon Web Services Key Management Service key asynchronously. Therefore, if you specify an ID, alias, or ARN that is invalid, the action can appear to complete, but eventually fails.</p> </important>"""
    volume_type: NotRequired["capo_ecs.types.ebs_volume_type.EBSVolumeType"]
    """<p>The volume type. This parameter maps 1:1 with the <code>VolumeType</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html">Amazon EBS volume types</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>The following are the supported volume types.</p> <ul> <li> <p>General Purpose SSD: <code>gp2</code>|<code>gp3</code> </p> </li> <li> <p>Provisioned IOPS SSD: <code>io1</code>|<code>io2</code> </p> </li> <li> <p>Throughput Optimized HDD: <code>st1</code> </p> </li> <li> <p>Cold HDD: <code>sc1</code> </p> </li> <li> <p>Magnetic: <code>standard</code> </p> <note> <p>The magnetic volume type is not supported on Fargate.</p> </note> </li> </ul>"""
    size_in_gi_b: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The size of the volume in GiB. You must specify either a volume size or a snapshot ID. If you specify a snapshot ID, the snapshot size is used for the volume size by default. You can optionally specify a volume size greater than or equal to the snapshot size. This parameter maps 1:1 with the <code>Size</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>.</p> <p>The following are the supported volume size values for each volume type.</p> <ul> <li> <p> <code>gp2</code> and <code>gp3</code>: 1-16,384</p> </li> <li> <p> <code>io1</code> and <code>io2</code>: 4-16,384</p> </li> <li> <p> <code>st1</code> and <code>sc1</code>: 125-16,384</p> </li> <li> <p> <code>standard</code>: 1-1,024</p> </li> </ul>"""
    snapshot_id: NotRequired["capo_ecs.types.ebs_snapshot_id.EBSSnapshotId"]
    """<p>The snapshot that Amazon ECS uses to create the volume. You must specify either a snapshot ID or a volume size. This parameter maps 1:1 with the <code>SnapshotId</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    volume_initialization_rate: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The rate, in MiB/s, at which data is fetched from a snapshot of an existing Amazon EBS volume to create a new volume for attachment to the task. This property can be specified only if you specify a <code>snapshotId</code>. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html">Initialize Amazon EBS volumes</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    iops: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.</p> <p>The following are the supported values for each volume type.</p> <ul> <li> <p> <code>gp3</code>: 3,000 - 16,000 IOPS</p> </li> <li> <p> <code>io1</code>: 100 - 64,000 IOPS</p> </li> <li> <p> <code>io2</code>: 100 - 256,000 IOPS</p> </li> </ul> <p>This parameter is required for <code>io1</code> and <code>io2</code> volume types. The default for <code>gp3</code> volumes is <code>3,000 IOPS</code>. This parameter is not supported for <code>st1</code>, <code>sc1</code>, or <code>standard</code> volume types.</p> <p>This parameter maps 1:1 with the <code>Iops</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    throughput: NotRequired["capo_ecs.types.boxed_integer.BoxedInteger"]
    """<p>The throughput to provision for a volume, in MiB/s, with a maximum of 1,000 MiB/s. This parameter maps 1:1 with the <code>Throughput</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>.</p> <important> <p>This parameter is only supported for the <code>gp3</code> volume type.</p> </important>"""
    tag_specifications: NotRequired[
        "capo_ecs.types.ebs_tag_specifications.EBSTagSpecifications"
    ]
    """<p>The tags to apply to the volume. Amazon ECS applies service-managed tags by default. This parameter maps 1:1 with the <code>TagSpecifications.N</code> parameter of the <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateVolume.html">CreateVolume API</a> in the <i>Amazon EC2 API Reference</i>.</p>"""
    role_arn: "capo_ecs.types.iam_role_arn.IAMRoleArn"
    """<p>The ARN of the IAM role to associate with this volume. This is the Amazon ECS infrastructure IAM role that is used to manage your Amazon Web Services infrastructure. We recommend using the Amazon ECS-managed <code>AmazonECSInfrastructureRolePolicyForVolumes</code> IAM policy with this role. For more information, see <a href="https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure_IAM_role.html">Amazon ECS infrastructure IAM role</a> in the <i>Amazon ECS Developer Guide</i>.</p>"""
    termination_policy: NotRequired[
        "capo_ecs.types.task_managed_ebs_volume_termination_policy.TaskManagedEBSVolumeTerminationPolicy"
    ]
    """<p>The termination policy for the volume when the task exits. This provides a way to control whether Amazon ECS terminates the Amazon EBS volume when the task stops.</p>"""
    filesystem_type: NotRequired[
        "capo_ecs.types.task_filesystem_type.TaskFilesystemType"
    ]
    """<p>The Linux filesystem type for the volume. For volumes created from a snapshot, you must specify the same filesystem type that the volume was using when the snapshot was created. If there is a filesystem type mismatch, the task will fail to start.</p> <p>The available filesystem types are <code>ext3</code>, <code>ext4</code>, and <code>xfs</code>. If no value is specified, the <code>xfs</code> filesystem type is used by default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TaskManagedEBSVolumeConfiguration) -> dict:
    out: dict = {}
    if "encrypted" in value:
        out["encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    if "volume_type" in value:
        out["volumeType"] = value["volume_type"]
    if "size_in_gi_b" in value:
        out["sizeInGiB"] = value["size_in_gi_b"]
    if "snapshot_id" in value:
        out["snapshotId"] = value["snapshot_id"]
    if "volume_initialization_rate" in value:
        out["volumeInitializationRate"] = value["volume_initialization_rate"]
    if "iops" in value:
        out["iops"] = value["iops"]
    if "throughput" in value:
        out["throughput"] = value["throughput"]
    if "tag_specifications" in value:
        import capo_ecs.types.ebs_tag_specifications

        out["tagSpecifications"] = (
            capo_ecs.types.ebs_tag_specifications.serialize_aws_json_1_1(
                value["tag_specifications"]
            )
        )
    out["roleArn"] = value["role_arn"]
    if "termination_policy" in value:
        import capo_ecs.types.task_managed_ebs_volume_termination_policy

        out["terminationPolicy"] = (
            capo_ecs.types.task_managed_ebs_volume_termination_policy.serialize_aws_json_1_1(
                value["termination_policy"]
            )
        )
    if "filesystem_type" in value:
        import capo_ecs.types.task_filesystem_type

        out["filesystemType"] = (
            capo_ecs.types.task_filesystem_type.serialize_aws_json_1_1(
                value["filesystem_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TaskManagedEBSVolumeConfiguration:
    out: TaskManagedEBSVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("encrypted") is not None:
        out["encrypted"] = data["encrypted"]
    if data.get("kmsKeyId") is not None:
        out["kms_key_id"] = data["kmsKeyId"]
    if data.get("volumeType") is not None:
        out["volume_type"] = data["volumeType"]
    if data.get("sizeInGiB") is not None:
        out["size_in_gi_b"] = data["sizeInGiB"]
    if data.get("snapshotId") is not None:
        out["snapshot_id"] = data["snapshotId"]
    if data.get("volumeInitializationRate") is not None:
        out["volume_initialization_rate"] = data["volumeInitializationRate"]
    if data.get("iops") is not None:
        out["iops"] = data["iops"]
    if data.get("throughput") is not None:
        out["throughput"] = data["throughput"]
    if data.get("tagSpecifications") is not None:
        import capo_ecs.types.ebs_tag_specifications

        out["tag_specifications"] = (
            capo_ecs.types.ebs_tag_specifications.deserialize_aws_json_1_1(
                data["tagSpecifications"]
            )
        )
    if data.get("roleArn") is not None:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "TaskManagedEBSVolumeConfiguration.role_arn required"
        )
    if data.get("terminationPolicy") is not None:
        import capo_ecs.types.task_managed_ebs_volume_termination_policy

        out["termination_policy"] = (
            capo_ecs.types.task_managed_ebs_volume_termination_policy.deserialize_aws_json_1_1(
                data["terminationPolicy"]
            )
        )
    if data.get("filesystemType") is not None:
        import capo_ecs.types.task_filesystem_type

        out["filesystem_type"] = (
            capo_ecs.types.task_filesystem_type.deserialize_aws_json_1_1(
                data["filesystemType"]
            )
        )
    return out
