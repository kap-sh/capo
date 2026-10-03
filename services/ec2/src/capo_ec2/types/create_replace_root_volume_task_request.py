"""Generated from Smithy shape ``com.amazonaws.ec2#CreateReplaceRootVolumeTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.image_id
    import capo_ec2.types.instance_id
    import capo_ec2.types.long
    import capo_ec2.types.snapshot_id
    import capo_ec2.types.string
    import capo_ec2.types.tag_specification_list
    import capo_ec2.types.volume_id


class CreateReplaceRootVolumeTaskRequest(TypedDict, closed=True):
    instance_id: NotRequired["capo_ec2.types.instance_id.InstanceId"]
    """<p>The ID of the instance for which to replace the root volume.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot from which to restore the replacement root volume. The specified snapshot must be a snapshot that you previously created from the original root volume.</p> <p>If you want to restore the replacement root volume to the initial launch state, if you want to restore the replacement root volume from an AMI, or if you want to replace the root volume with a specified volume, omit this parameter.</p>"""
    client_token: NotRequired["capo_ec2.types.string.String"]
    """<p>Unique, case-sensitive identifier you provide to ensure the idempotency of the request. If you do not specify a client token, a randomly generated token is used for the request to ensure idempotency. For more information, see <a href="https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html">Ensuring idempotency</a>.</p>"""
    dry_run: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is <code>DryRunOperation</code>. Otherwise, it is <code>UnauthorizedOperation</code>.</p>"""
    tag_specifications: NotRequired[
        "capo_ec2.types.tag_specification_list.TagSpecificationList"
    ]
    """<p>The tags to apply to the root volume replacement task.</p>"""
    image_id: NotRequired["capo_ec2.types.image_id.ImageId"]
    """<p>The ID of the AMI to use to restore the root volume. The specified AMI must have the same product code, billing information, architecture type, and virtualization type as that of the instance.</p> <p>If you want to restore the replacement volume from a specific snapshot, if you want to restore it to its launch state, or if you want to replace the root volume with a specified volume, omit this parameter.</p>"""
    delete_replaced_root_volume: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether to automatically delete the original root volume after the root volume replacement task completes. To delete the original root volume, specify <code>true</code>. If you choose to keep the original root volume after the replacement task completes, you must manually delete it when you no longer need it.</p>"""
    volume_initialization_rate: NotRequired["capo_ec2.types.long.Long"]
    """<p>Specifies the Amazon EBS Provisioned Rate for Volume Initialization (volume initialization rate), in MiB/s, at which to download the snapshot blocks from Amazon S3 to the replacement root volume. This is also known as <i>volume initialization</i>. Specifying a volume initialization rate ensures that the volume is initialized at a predictable and consistent rate after creation.</p> <p>Omit this parameter if:</p> <ul> <li> <p>You want to create the volume using fast snapshot restore. You must specify a snapshot that is enabled for fast snapshot restore. In this case, the volume is fully initialized at creation.</p> <note> <p>If you specify a snapshot that is enabled for fast snapshot restore and a volume initialization rate, the volume will be initialized at the specified rate instead of fast snapshot restore.</p> </note> </li> <li> <p>You want to create a volume that is initialized at the default rate.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/initalize-volume.html"> Initialize Amazon EBS volumes</a> in the <i>Amazon EC2 User Guide</i>.</p> <p>Valid range: 100 - 300 MiB/s</p>"""
    volume_id: NotRequired["capo_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume to use as the replacement root volume. The specified volume must be in the same Availability Zone as the instance, must be in the <code>available</code> state, and must not be attached to an instance. If the original root volume is encrypted, the specified volume must also be encrypted.</p> <p>If you want to restore the replacement root volume from a specific snapshot, an AMI, or to its launch state, omit this parameter.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: CreateReplaceRootVolumeTaskRequest, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "instance_id" in value:
        pairs.append((f"{key_prefix}InstanceId", str(value["instance_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "client_token" in value:
        pairs.append((f"{key_prefix}ClientToken", str(value["client_token"])))
    if "dry_run" in value:
        pairs.append((f"{key_prefix}DryRun", "true" if value["dry_run"] else "false"))
    if "tag_specifications" in value:
        import capo_ec2.types.tag_specification_list

        capo_ec2.types.tag_specification_list.serialize_ec2_query(
            value["tag_specifications"], pairs, f"{key_prefix}TagSpecification"
        )
    if "image_id" in value:
        pairs.append((f"{key_prefix}ImageId", str(value["image_id"])))
    if "delete_replaced_root_volume" in value:
        pairs.append(
            (
                f"{key_prefix}DeleteReplacedRootVolume",
                "true" if value["delete_replaced_root_volume"] else "false",
            )
        )
    if "volume_initialization_rate" in value:
        pairs.append(
            (
                f"{key_prefix}VolumeInitializationRate",
                str(value["volume_initialization_rate"]),
            )
        )
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))


def deserialize_ec2_query(el: Element) -> CreateReplaceRootVolumeTaskRequest:
    out: CreateReplaceRootVolumeTaskRequest = {}  # type: ignore[typeddict-item]
    child_instance_id = el.find("InstanceId")
    if child_instance_id is not None:
        out["instance_id"] = str(child_instance_id.text or "")
    child_snapshot_id = el.find("SnapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_client_token = el.find("ClientToken")
    if child_client_token is not None:
        out["client_token"] = str(child_client_token.text or "")
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
    child_image_id = el.find("ImageId")
    if child_image_id is not None:
        out["image_id"] = str(child_image_id.text or "")
    child_delete_replaced_root_volume = el.find("DeleteReplacedRootVolume")
    if child_delete_replaced_root_volume is not None:
        out["delete_replaced_root_volume"] = (
            child_delete_replaced_root_volume.text or ""
        ).lower() == "true"
    child_volume_initialization_rate = el.find("VolumeInitializationRate")
    if child_volume_initialization_rate is not None:
        out["volume_initialization_rate"] = int(
            child_volume_initialization_rate.text or ""
        )
    child_volume_id = el.find("VolumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    return out
