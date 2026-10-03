"""Generated from Smithy shape ``com.amazonaws.ec2#LaunchTemplateEbsBlockDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.volume_type


class LaunchTemplateEbsBlockDeviceRequest(TypedDict, closed=True):
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you are creating a volume from a snapshot, you can't specify an encryption value.</p>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is deleted on instance termination.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.</p> <p>The following are the supported values for each volume type:</p> <ul> <li> <p> <code>gp3</code>: 3,000 - 80,000 IOPS</p> </li> <li> <p> <code>io1</code>: 100 - 64,000 IOPS</p> </li> <li> <p> <code>io2</code>: 100 - 256,000 IOPS</p> </li> </ul> <p>For <code>io2</code> volumes, you can achieve up to 256,000 IOPS on <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html">instances built on the Nitro System</a>. On other instances, you can achieve performance up to 32,000 IOPS.</p> <p>This parameter is supported for <code>io1</code>, <code>io2</code>, and <code>gp3</code> volumes only.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. The following are the supported volumes sizes for each volume type:</p> <ul> <li> <p> <code>gp2</code>: 1 - 16,384 GiB</p> </li> <li> <p> <code>gp3</code>: 1 - 65,536 GiB</p> </li> <li> <p> <code>io1</code>: 4 - 16,384 GiB</p> </li> <li> <p> <code>io2</code>: 4 - 65,536 GiB</p> </li> <li> <p> <code>st1</code> and <code>sc1</code>: 125 - 16,384 GiB</p> </li> <li> <p> <code>standard</code>: 1 - 1024 GiB</p> </li> </ul>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The volume type. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The throughput to provision for a <code>gp3</code> volume, with a maximum of 2,000 MiB/s.</p> <p>Valid Range: Minimum value of 125. Maximum value of 2,000.</p>"""
    volume_initialization_rate: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the volume. This is also known as <i>volume initialization</i>. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.</p> <p>This parameter is supported only for volumes created from snapshots. Omit this parameter if:</p> <ul> <li> <p>You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.</p> <note> <p>If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.</p> </note> </li> <li> <p>You want to create a volume that is initialized at the default rate.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html"> Initialize Amazon EBS volumes</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Valid range: 100 - 300 MiB/s</p>"""
    ebs_card_index: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The index of the EBS card. Some instance types support multiple EBS cards. The default EBS card index is 0.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: LaunchTemplateEbsBlockDeviceRequest,
    pairs: list[tuple[str, str]],
    prefix: str,
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "delete_on_termination" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteOnTermination",
                "true" if value["delete_on_termination"] else "false",
            )
        )
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "volume_size" in value:
        pairs.append((f"{key_prefix}VolumeSize", str(value["volume_size"])))
    if "volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{key_prefix}VolumeType"
        )
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))
    if "volume_initialization_rate" in value:
        pairs.append(
            (
                f"{key_prefix}VolumeInitializationRate",
                str(value["volume_initialization_rate"]),
            )
        )
    if "ebs_card_index" in value:
        pairs.append((f"{key_prefix}EbsCardIndex", str(value["ebs_card_index"])))


def deserialize_ec2_query(el: Element) -> LaunchTemplateEbsBlockDeviceRequest:
    out: LaunchTemplateEbsBlockDeviceRequest = {}  # type: ignore[typeddict-item]
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_delete_on_termination = el.find("DeleteOnTermination")
    if child_delete_on_termination is not None:
        out["delete_on_termination"] = (
            child_delete_on_termination.text or ""
        ).lower() == "true"
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_size = el.find("VolumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        import capo_ec2.types.volume_type

        out["volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_throughput = el.find("Throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_volume_initialization_rate = el.find("VolumeInitializationRate")
    if child_volume_initialization_rate is not None:
        out["volume_initialization_rate"] = int(
            child_volume_initialization_rate.text or ""
        )
    child_ebs_card_index = el.find("EbsCardIndex")
    if child_ebs_card_index is not None:
        out["ebs_card_index"] = int(child_ebs_card_index.text or "")
    return out
