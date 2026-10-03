"""Generated from Smithy shape ``com.amazonaws.ec2#CopyVolumesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.kms_key_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.volume_id
    import capo_ec2.types.volume_type


class CopyVolumesRequest(TypedDict, closed=True):
    source_volume_id: NotRequired["capo_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the source EBS volume to copy.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) to provision for the volume copy. Required for <code>io1</code> and <code>io2</code> volumes. Optional for <code>gp3</code> volumes. Omit for all other volume types. Full provisioned IOPS performance can be achieved only once the volume copy is fully initialized. </p> <p>Valid ranges:</p> <ul> <li> <p>gp3: <code>3,000 </code>(<i>default</i>)<code> - 80,000</code> IOPS</p> </li> <li> <p>io1: <code>100 - 64,000</code> IOPS</p> </li> <li> <p>io2: <code>100 - 256,000</code> IOPS</p> </li> </ul> <note> <p> <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html"> Instances built on the Nitro System</a> can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.</p> </note>"""
    size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume copy, in GiBs. The size must be equal to or greater than the size of the source volume. If not specified, the size defaults to the size of the source volume.</p> <p>Maximum supported sizes:</p> <ul> <li> <p>gp2: <code>16,384</code> GiB</p> </li> <li> <p>gp3: <code>65,536</code> GiB</p> </li> <li> <p>io1: <code>16,384</code> GiB</p> </li> <li> <p>io2: <code>65,536</code> GiB</p> </li> <li> <p>st1 and sc1: <code>16,384</code> GiB</p> </li> <li> <p>standard: <code>1024</code> GiB</p> </li> </ul>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The volume type for the volume copy. If not specified, the volume type defaults to <code>gp2</code>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the volume copy during creation.</p>"""
    multi_attach_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to enable Amazon EBS Multi-Attach for the volume copy. If you enable Multi-Attach, you can attach the volume to up to 16 Nitro instances in the same Availability Zone simultaneously. Supported with <code>io1</code> and <code>io2</code> volumes only. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html"> Amazon EBS Multi-Attach</a>.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The throughput to provision for the volume copy, in MiB/s. Supported for <code>gp3</code> volumes only. Omit for all other volume types. Full provisioned throughput performance can be achieved only once the volume copy is fully initialized.</p> <p>Valid Range: <code>125 - 2000</code> MiB/s</p> <p></p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html"> Ensure Idempotency</a>.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to encrypt the volume copy. If the source volume is encrypted, the service always encrypts the copy regardless of this value. Set to <code>true</code> to encrypt a copy of an unencrypted source volume during the copy operation. If you set <code>Encrypted</code> to <code>true</code> but do not specify <code>KmsKeyId</code>, the service uses the default KMS key for EBS encryption in your account.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.kms_key_id.KmsKeyId"]
    """<p>The identifier of the KMS key to use for encryption of the volume copy. Specify a symmetric encryption KMS key. You can specify a KMS key using the key ID, key ARN, alias name, or alias ARN. If you set <code>Encrypted</code> to <code>true</code> but do not specify this parameter, the service uses the default KMS key for EBS encryption in your account. For cross-account volume copies, this must be a KMS key in the calling account.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CopyVolumesRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "source_volume_id" in value:
        pairs.append((f"{key_prefix}SourceVolumeId", str(value["source_volume_id"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))
    if "volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{key_prefix}VolumeType"
        )
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
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
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))


def deserialize_ec2_query(el: Element) -> CopyVolumesRequest:
    out: CopyVolumesRequest = {}  # type: ignore[typeddict-item]
    child_source_volume_id = el.find("SourceVolumeId")
    if child_source_volume_id is not None:
        out["source_volume_id"] = str(child_source_volume_id.text or "")
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        import capo_ec2.types.volume_type

        out["volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
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
    child_encrypted = el.find("Encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    return out
