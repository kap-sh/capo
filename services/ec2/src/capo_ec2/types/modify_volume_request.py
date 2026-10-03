"""Generated from Smithy shape ``com.amazonaws.ec2#ModifyVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.volume_id
    import capo_ec2.types.volume_type


class ModifyVolumeRequest(TypedDict, closed=True):
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    volume_id: NotRequired["capo_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume.</p>"""
    size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The target size of the volume, in GiB. The target volume size must be greater than or equal to the existing size of the volume.</p> <p>The following are the supported volumes sizes for each volume type:</p> <ul> <li> <p> <code>gp2</code>: 1 - 16,384 GiB</p> </li> <li> <p> <code>gp3</code>: 1 - 65,536 GiB</p> </li> <li> <p> <code>io1</code>: 4 - 16,384 GiB</p> </li> <li> <p> <code>io2</code>: 4 - 65,536 GiB</p> </li> <li> <p> <code>st1</code> and <code>sc1</code>: 125 - 16,384 GiB</p> </li> <li> <p> <code>standard</code>: 1 - 1024 GiB</p> </li> </ul> <p>Default: The existing size is retained.</p>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The target EBS volume type of the volume. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html">Amazon EBS volume types</a> in the <i>Amazon EBS User Guide</i>.</p> <p>Default: The existing type is retained.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The target IOPS rate of the volume. This parameter is valid only for <code>gp3</code>, <code>io1</code>, and <code>io2</code> volumes.</p> <p>The following are the supported values for each volume type:</p> <ul> <li> <p> <code>gp3</code>: 3,000 - 80,000 IOPS</p> </li> <li> <p> <code>io1</code>: 100 - 64,000 IOPS</p> </li> <li> <p> <code>io2</code>: 100 - 256,000 IOPS</p> </li> </ul> <note> <p> <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html"> Instances built on the Nitro System</a> can support up to 256,000 IOPS. Other instances can support up to 32,000 IOPS.</p> </note> <p>Default: The existing value is retained if you keep the same volume type. If you change the volume type to <code>io1</code>, <code>io2</code>, or <code>gp3</code>, the default is 3,000.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The target throughput of the volume, in MiB/s. This parameter is valid only for <code>gp3</code> volumes. The maximum value is 2,000.</p> <p>Default: The existing value is retained if the source and target volume type is <code>gp3</code>. Otherwise, the default value is 125.</p> <p>Valid Range: Minimum value of 125. Maximum value of 2,000.</p>"""
    multi_attach_enabled: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Specifies whether to enable Amazon EBS Multi-Attach. If you enable Multi-Attach, you can attach the volume to up to 16 <a href="https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html"> Nitro-based instances</a> in the same Availability Zone. This parameter is supported with <code>io1</code> and <code>io2</code> volumes only. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-multi.html"> Amazon EBS Multi-Attach</a> in the <i>Amazon EBS User Guide</i>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: ModifyVolumeRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))
    if "volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{key_prefix}VolumeType"
        )
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))
    if "multi_attach_enabled" in value:
        pairs.append(
            (
                f"{key_prefix}MultiAttachEnabled",
                "true" if value["multi_attach_enabled"] else "false",
            )
        )


def deserialize_ec2_query(el: Element) -> ModifyVolumeRequest:
    out: ModifyVolumeRequest = {}  # type: ignore[typeddict-item]
    child_dry_run = el.find("DryRun")
    if child_dry_run is not None:
        out["dry_run"] = (child_dry_run.text or "").lower() == "true"
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_size = el.find("Size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_volume_type = el.find("VolumeType")
    if child_volume_type is not None:
        import capo_ec2.types.volume_type

        out["volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_iops = el.find("Iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_throughput = el.find("Throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_multi_attach_enabled = el.find("MultiAttachEnabled")
    if child_multi_attach_enabled is not None:
        out["multi_attach_enabled"] = (
            child_multi_attach_enabled.text or ""
        ).lower() == "true"
    return out
