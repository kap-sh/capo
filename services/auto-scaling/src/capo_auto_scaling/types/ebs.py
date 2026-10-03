"""Generated from Smithy shape ``com.amazonaws.autoscaling#Ebs``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import capo_auto_scaling.types.block_device_ebs_delete_on_termination
    import capo_auto_scaling.types.block_device_ebs_encrypted
    import capo_auto_scaling.types.block_device_ebs_iops
    import capo_auto_scaling.types.block_device_ebs_throughput
    import capo_auto_scaling.types.block_device_ebs_volume_size
    import capo_auto_scaling.types.block_device_ebs_volume_type
    import capo_auto_scaling.types.xml_string_max_len255


class Ebs(TypedDict, closed=True):
    snapshot_id: NotRequired[
        "capo_auto_scaling.types.xml_string_max_len255.XmlStringMaxLen255"
    ]
    """<p>The snapshot ID of the volume to use.</p> <p>You must specify either a <code>VolumeSize</code> or a <code>SnapshotId</code>.</p>"""
    volume_size: NotRequired[
        "capo_auto_scaling.types.block_device_ebs_volume_size.BlockDeviceEbsVolumeSize"
    ]
    """<p>The volume size, in GiBs. The following are the supported volumes sizes for each volume type: </p> <ul> <li> <p> <code>gp2</code> and <code>gp3</code>: 1-16,384</p> </li> <li> <p> <code>io1</code>: 4-16,384</p> </li> <li> <p> <code>st1</code> and <code>sc1</code>: 125-16,384</p> </li> <li> <p> <code>standard</code>: 1-1,024</p> </li> </ul> <p>You must specify either a <code>SnapshotId</code> or a <code>VolumeSize</code>. If you specify both <code>SnapshotId</code> and <code>VolumeSize</code>, the volume size must be equal or greater than the size of the snapshot.</p>"""
    volume_type: NotRequired[
        "capo_auto_scaling.types.block_device_ebs_volume_type.BlockDeviceEbsVolumeType"
    ]
    """<p>The volume type. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Valid values: <code>standard</code> | <code>io1</code> | <code>gp2</code> | <code>st1</code> | <code>sc1</code> | <code>gp3</code> </p>"""
    delete_on_termination: NotRequired[
        "capo_auto_scaling.types.block_device_ebs_delete_on_termination.BlockDeviceEbsDeleteOnTermination"
    ]
    """<p>Indicates whether the volume is deleted on instance termination. For Amazon EC2 Auto Scaling, the default value is <code>true</code>.</p>"""
    iops: NotRequired[
        "capo_auto_scaling.types.block_device_ebs_iops.BlockDeviceEbsIops"
    ]
    """<p>The number of input/output (I/O) operations per second (IOPS) to provision for the volume. For <code>gp3</code> and <code>io1</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting. </p> <p>The following are the supported values for each volume type: </p> <ul> <li> <p> <code>gp3</code>: 3,000-16,000 IOPS</p> </li> <li> <p> <code>io1</code>: 100-64,000 IOPS</p> </li> </ul> <p>For <code>io1</code> volumes, we guarantee 64,000 IOPS only for <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html">Instances built on the Amazon Web Services Nitro System</a>. Other instance families guarantee performance up to 32,000 IOPS. </p> <p> <code>Iops</code> is supported when the volume type is <code>gp3</code> or <code>io1</code> and required only when the volume type is <code>io1</code>. (Not used with <code>standard</code>, <code>gp2</code>, <code>st1</code>, or <code>sc1</code> volumes.) </p>"""
    encrypted: NotRequired[
        "capo_auto_scaling.types.block_device_ebs_encrypted.BlockDeviceEbsEncrypted"
    ]
    """<p>Specifies whether the volume should be encrypted. Encrypted EBS volumes can only be attached to instances that support Amazon EBS encryption. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html">Requirements for Amazon EBS encryption</a> in the <i>Amazon EBS User Guide</i>. If your AMI uses encrypted volumes, you can also only launch it on supported instance types.</p> <note> <p>If you are creating a volume from a snapshot, you cannot create an unencrypted volume from an encrypted snapshot. Also, you cannot specify a KMS key ID when using a launch configuration.</p> <p>If you enable encryption by default, the EBS volumes that you create are always encrypted, either using the Amazon Web Services managed KMS key or a customer-managed KMS key, regardless of whether the snapshot was encrypted. </p> <p>For more information, see <a href="https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-data-protection.html#encryption">Use Amazon Web Services KMS keys to encrypt Amazon EBS volumes</a> in the <i>Amazon EC2 Auto Scaling User Guide</i>.</p> </note>"""
    throughput: NotRequired[
        "capo_auto_scaling.types.block_device_ebs_throughput.BlockDeviceEbsThroughput"
    ]
    """<p>The throughput (MiBps) to provision for a <code>gp3</code> volume.</p>"""


# --- awsQuery ser/de ---
def serialize_query(value: Ebs, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "volume_size" in value:
        pairs.append((f"{key_prefix}VolumeSize", str(value["volume_size"])))
    if "volume_type" in value:
        pairs.append((f"{key_prefix}VolumeType", str(value["volume_type"])))
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))


def deserialize_query(el: Element) -> Ebs:
    out: Ebs = {}  # type: ignore[typeddict-item]
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_size = el.find("VolumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        out["volume_type"] = str(child_volume_type.text or "")
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_throughput = el.find("Throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    return out
