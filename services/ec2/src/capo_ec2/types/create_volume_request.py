"""Generated from Smithy shape ``com.amazonaws.ec2#CreateVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.availability_zone_id
    import capo_ec2.types.availability_zone_name
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.operator_request
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.volume_type


class CreateVolumeRequest(TypedDict, closed=True):
    availability_zone: NotRequired[
        "capo_ec2.types.availability_zone_name.AvailabilityZoneName"
    ]
    """<p>The ID of the Availability Zone in which to create the volume. For example, <code>us-east-1a</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""
    availability_zone_id: NotRequired[
        "capo_ec2.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The ID of the Availability Zone in which to create the volume. For example, <code>use1-az1</code>.</p> <p>Either <code>AvailabilityZone</code> or <code>AvailabilityZoneId</code> must be specified, but not both.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the volume should be encrypted. The effect of setting the encryption state to <code>true</code> depends on the volume origin (new or from a snapshot), starting encryption state, ownership, and whether encryption by default is enabled. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/work-with-ebs-encr.html#encryption-by-default">Encryption by default</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Encrypted Amazon EBS volumes must be attached to instances that support Amazon EBS encryption. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-encryption-requirements.html#ebs-encryption_supported_instances">Supported instance types</a>.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) to provision for the volume. Required for <code>io1</code> and <code>io2</code> volumes. Optional for <code>gp3</code> volumes. Omit for all other volume types. </p> <p>Valid ranges:</p> <ul> <li> <p>gp3: <code>3,000 </code>(<i>default</i>)<code> - 80,000</code> IOPS</p> </li> <li> <p>io1: <code>100 - 64,000</code> IOPS</p> </li> <li> <p>io2: <code>100 - 256,000</code> IOPS</p> </li> </ul> <note> <p> <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html"> Instances built on the Nitro System</a> can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.</p> </note>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for Amazon EBS encryption. If this parameter is not specified, your KMS key for Amazon EBS is used. If <code>KmsKeyId</code> is specified, the encrypted state must be <code>true</code>.</p> <p>You can specify the KMS key using any of the following:</p> <ul> <li> <p>Key ID. For example, 1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Key alias. For example, alias/ExampleAlias.</p> </li> <li> <p>Key ARN. For example, arn:aws:kms:us-east-1:012345678910:key/1234abcd-12ab-34cd-56ef-1234567890ab.</p> </li> <li> <p>Alias ARN. For example, arn:aws:kms:us-east-1:012345678910:alias/ExampleAlias.</p> </li> </ul> <p>Amazon Web Services authenticates the KMS key asynchronously. Therefore, if you specify an ID, alias, or ARN that is not valid, the action can appear to complete, but eventually fails.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the Outpost on which to create the volume.</p> <p>If you intend to use a volume with an instance running on an outpost, then you must create the volume on the same outpost as the instance. You can't use a volume created in an Amazon Web Services Region with an instance on an Amazon Web Services outpost, or the other way around.</p>"""
    size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size. If you specify a snapshot, the default is the snapshot size, and you can specify a volume size that is equal to or larger than the snapshot size.</p> <p>Valid sizes:</p> <ul> <li> <p>gp2: <code>1 - 16,384</code> GiB</p> </li> <li> <p>gp3: <code>1 - 65,536</code> GiB</p> </li> <li> <p>io1: <code>4 - 16,384</code> GiB</p> </li> <li> <p>io2: <code>4 - 65,536</code> GiB</p> </li> <li> <p>st1 and sc1: <code>125 - 16,384</code> GiB</p> </li> <li> <p>standard: <code>1 - 1024</code> GiB</p> </li> </ul>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The snapshot from which to create the volume. You must specify either a snapshot ID or a volume size.</p>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The volume type. This parameter can be one of the following values:</p> <ul> <li> <p>General Purpose SSD: <code>gp2</code> | <code>gp3</code> </p> </li> <li> <p>Provisioned IOPS SSD: <code>io1</code> | <code>io2</code> </p> </li> <li> <p>Throughput Optimized HDD: <code>st1</code> </p> </li> <li> <p>Cold HDD: <code>sc1</code> </p> </li> <li> <p>Magnetic: <code>standard</code> </p> </li> </ul> <important> <p>Throughput Optimized HDD (<code>st1</code>) and Cold HDD (<code>sc1</code>) volumes can't be used as boot volumes.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Default: <code>gp2</code> </p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the volume during creation.</p>"""
    multi_attach_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16 <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html">Instances built on the Nitro System</a> in the same Availability Zone. This parameter is supported with <code>io1</code> and <code>io2</code> volumes only. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html"> Amazon EBS Multi-Attach</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The throughput to provision for the volume, in MiB/s. Supported for <code>gp3</code> volumes only. Omit for all other volume types.</p> <p>Valid Range: <code>125 - 2000</code> MiB/s</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensure Idempotency</a>.</p>"""
    volume_initialization_rate: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the volume. This is also known as <i>volume initialization</i>. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.</p> <p>This parameter is supported only for volumes created from snapshots. Omit this parameter if:</p> <ul> <li> <p>You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.</p> <note> <p>If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.</p> </note> </li> <li> <p>You want to create a volume that is initialized at the default rate.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html"> Initialize Amazon EBS volumes</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Valid range: 100 - 300 MiB/s</p>"""
    operator: NotRequired["capo_ec2.types.operator_request.OperatorRequest"]
    """<p>Reserved for internal use.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateVolumeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{key_prefix}VolumeType"
        )
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "multi_attach_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}MultiAttachEnabled",
                "true" if value["multi_attach_enabled"] else "false",
            )
        )
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "volume_initialization_rate" in value:
        pairs.append(
            (
                f"{key_prefix}VolumeInitializationRate",
                str(value["volume_initialization_rate"]),
            )
        )
    if "operator" in value:
        import capo_ec2.types.operator_request

        capo_ec2.types.operator_request.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))


def deserialize_ec2_query(el: Element) -> CreateVolumeRequest:
    out: CreateVolumeRequest = {}  # type: ignore[typeddict-item]
    child_availability_zone = el.find("AvailabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("AvailabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_outpost_arn = el.find("OutpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        import capo_ec2.types.volume_type

        out["volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_tag_specifications = el.find("TagSpecification")
    if child_tag_specifications is not None:
        import capo_ec2.types.tag_specification_list

        out["tag_specifications"] = (
            capo_ec2.types.tag_specification_list.deserialize_ec2_query(
                child_tag_specifications
            )
        )
    child_multi_attach_enabled = el.find("MultiAttachEnabled")
    if child_multi_attach_enabled is not None:
        out["multi_attach_enabled"] = (
            child_multi_attach_enabled.text or ""
        ).lower() == "true"
    child_throughput = el.find("Throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
    child_volume_initialization_rate = el.find("VolumeInitializationRate")
    if child_volume_initialization_rate is not None:
        out["volume_initialization_rate"] = int(
            child_volume_initialization_rate.text or ""
        )
    child_operator = el.find("Operator")
    if child_operator is not None:
        import capo_ec2.types.operator_request

        out["operator"] = capo_ec2.types.operator_request.deserialize_ec2_query(
            child_operator
        )
    child_dry_run = el.find("dryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    return out
