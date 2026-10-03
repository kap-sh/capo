"""Generated from Smithy shape ``com.amazonaws.ec2#FleetEbsBlockDeviceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.volume_type


class FleetEbsBlockDeviceRequest(TypedDict, closed=True):
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the encryption state of an EBS volume is changed while being restored from a backing snapshot. The effect of setting the encryption state to <code>true</code> depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption.html">Amazon EBS encryption</a> in the <i>Amazon EBS User Guide</i>.</p> <p>In no case can you remove encryption from an encrypted volume.</p> <p>Encrypted volumes can only be attached to instances that support Amazon EBS encryption. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html#ebs-encryption_supported_instances">Supported instance types</a>.</p> <p>This parameter is not returned by <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImageAttribute">DescribeImageAttribute</a>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateImage">CreateImage</a> and <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RegisterImage">RegisterImage</a>, whether you can include this parameter, and the allowed values differ depending on the type of block device mapping you are creating.</p> <ul> <li> <p>If you are creating a block device mapping for a <b>new (empty) volume</b>, you can include this parameter, and specify either <code>true</code> for an encrypted volume, or <code>false</code> for an unencrypted volume. If you omit this parameter, it defaults to <code>false</code> (unencrypted).</p> </li> <li> <p>If you are creating a block device mapping from an <b>existing encrypted or unencrypted snapshot</b>, you must omit this parameter. If you include this parameter, the request will fail, regardless of the value that you specify.</p> </li> <li> <p>If you are creating a block device mapping from an <b>existing unencrypted volume</b>, you can include this parameter, but you must specify <code>false</code>. If you specify <code>true</code>, the request will fail. In this case, we recommend that you omit the parameter.</p> </li> <li> <p>If you are creating a block device mapping from an <b>existing encrypted volume</b>, you can include this parameter, and specify either <code>true</code> or <code>false</code>. However, if you specify <code>false</code>, the parameter is ignored and the block device mapping is always encrypted. In this case, we recommend that you omit the parameter.</p> </li> </ul>"""
    delete_on_termination: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the EBS volume is deleted on instance termination. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/preserving-volumes-on-termination.html">Preserve data when an instance is terminated</a> in the <i>Amazon EC2 User Guide</i>.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS). For <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes, this represents the number of IOPS that are provisioned for the volume. For <code>gp2</code> volumes, this represents the baseline performance of the volume and the rate at which the volume accumulates I/O credits for bursting.</p> <p>The following are the supported values for each volume type:</p> <ul> <li> <p> <code>gp3</code>: 3,000 - 80,000 IOPS</p> </li> <li> <p> <code>io1</code>: 100 - 64,000 IOPS</p> </li> <li> <p> <code>io2</code>: 100 - 256,000 IOPS</p> </li> </ul> <p>For <code>io2</code> volumes, you can achieve up to 256,000 IOPS on <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances">instances built on the Nitro System</a>. On other instances, you can achieve performance up to 32,000 IOPS.</p> <p>This parameter is required for <code>io1</code> and <code>io2</code> volumes. The default for <code>gp3</code> volumes is 3,000 IOPS.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p> <p>This parameter is valid only for <code>gp3</code> volumes.</p> <p>Valid Range: Minimum value of 125. Maximum value of 2,000.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>Identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for EBS encryption.</p> <p>This parameter is only supported on <code>BlockDeviceMapping</code> objects called by <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet.html">CreateFleet</a>, <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotInstances.html">RequestSpotInstances</a>, and <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html">RunInstances</a>.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    volume_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size. You can specify a volume size that is equal to or larger than the snapshot size.</p> <p>The following are the supported sizes for each volume type:</p> <ul> <li> <p> <code>gp2</code>: 1 - 16,384 GiB</p> </li> <li> <p> <code>gp3</code>: 1 - 65,536 GiB</p> </li> <li> <p> <code>io1</code>: 4 - 16,384 GiB</p> </li> <li> <p> <code>io2</code>: 4 - 65,536 GiB</p> </li> <li> <p> <code>st1</code> and <code>sc1</code>: 125 - 16,384 GiB</p> </li> <li> <p> <code>standard</code>: 1 - 1024 GiB</p> </li> </ul>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The volume type. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: FleetEbsBlockDeviceRequest, pairs: list[tuple[str, str]], prefix: str
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
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))
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


def deserialize_ec2_query(el: Element) -> FleetEbsBlockDeviceRequest:
    out: FleetEbsBlockDeviceRequest = {}  # type: ignore[typeddict-item]
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
    child_throughput = el.find("Throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
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
    return out
