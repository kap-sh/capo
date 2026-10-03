"""Generated from Smithy shape ``com.amazonaws.ebs#StartSnapshotResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ebs.types.block_size
    import capo_ebs.types.description
    import capo_ebs.types.kms_key_arn
    import capo_ebs.types.owner_id
    import capo_ebs.types.snapshot_id
    import capo_ebs.types.sse_type
    import capo_ebs.types.status
    import capo_ebs.types.tags
    import capo_ebs.types.time_stamp
    import capo_ebs.types.volume_size


class StartSnapshotResponse(TypedDict, closed=True):
    description: NotRequired["capo_ebs.types.description.Description"]
    """<p>The description of the snapshot.</p>"""
    snapshot_id: NotRequired["capo_ebs.types.snapshot_id.SnapshotId"]
    """<p>The ID of the snapshot.</p>"""
    owner_id: NotRequired["capo_ebs.types.owner_id.OwnerId"]
    """<p>The Amazon Web Services account ID of the snapshot owner.</p>"""
    status: NotRequired["capo_ebs.types.status.Status"]
    """<p>The status of the snapshot.</p>"""
    start_time: NotRequired["capo_ebs.types.time_stamp.TimeStamp"]
    """<p>The timestamp when the snapshot was created.</p>"""
    volume_size: NotRequired["capo_ebs.types.volume_size.VolumeSize"]
    """<p>The size of the volume, in GiB.</p>"""
    block_size: NotRequired["capo_ebs.types.block_size.BlockSize"]
    """<p>The size of the blocks in the snapshot, in bytes.</p>"""
    tags: NotRequired["capo_ebs.types.tags.Tags"]
    """<p>The tags applied to the snapshot. You can specify up to 50 tags per snapshot. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html"> Tagging your Amazon EC2 resources</a> in the <i>Amazon Elastic Compute Cloud User Guide</i>.</p>"""
    parent_snapshot_id: NotRequired["capo_ebs.types.snapshot_id.SnapshotId"]
    """<p>The ID of the parent snapshot.</p>"""
    kms_key_arn: NotRequired["capo_ebs.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the Key Management Service (KMS) key used to encrypt the snapshot.</p>"""
    sse_type: NotRequired["capo_ebs.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSnapshotResponse) -> dict:
    out: dict = {}
    if "description" in value:
        out["Description"] = value["description"]
    if "snapshot_id" in value:
        out["SnapshotId"] = value["snapshot_id"]
    if "owner_id" in value:
        out["OwnerId"] = value["owner_id"]
    if "status" in value:
        import capo_ebs.types.status

        out["Status"] = capo_ebs.types.status.serialize_json(value["status"])
    if "start_time" in value:
        import capo_ebs.types.time_stamp

        out["StartTime"] = capo_ebs.types.time_stamp.serialize_json(value["start_time"])
    if "volume_size" in value:
        out["VolumeSize"] = value["volume_size"]
    if "block_size" in value:
        out["BlockSize"] = value["block_size"]
    if "tags" in value:
        import capo_ebs.types.tags

        out["Tags"] = capo_ebs.types.tags.serialize_json(value["tags"])
    if "parent_snapshot_id" in value:
        out["ParentSnapshotId"] = value["parent_snapshot_id"]
    if "kms_key_arn" in value:
        out["KmsKeyArn"] = value["kms_key_arn"]
    if "sse_type" in value:
        import capo_ebs.types.sse_type

        out["SseType"] = capo_ebs.types.sse_type.serialize_json(value["sse_type"])
    return out


def deserialize_json(data: dict) -> StartSnapshotResponse:
    out: StartSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("SnapshotId") is not None:
        out["snapshot_id"] = data["SnapshotId"]
    if data.get("OwnerId") is not None:
        out["owner_id"] = data["OwnerId"]
    if data.get("Status") is not None:
        import capo_ebs.types.status

        out["status"] = capo_ebs.types.status.deserialize_json(data["Status"])
    if data.get("StartTime") is not None:
        import capo_ebs.types.time_stamp

        out["start_time"] = capo_ebs.types.time_stamp.deserialize_json(
            data["StartTime"]
        )
    if data.get("VolumeSize") is not None:
        out["volume_size"] = data["VolumeSize"]
    if data.get("BlockSize") is not None:
        out["block_size"] = data["BlockSize"]
    if data.get("Tags") is not None:
        import capo_ebs.types.tags

        out["tags"] = capo_ebs.types.tags.deserialize_json(data["Tags"])
    if data.get("ParentSnapshotId") is not None:
        out["parent_snapshot_id"] = data["ParentSnapshotId"]
    if data.get("KmsKeyArn") is not None:
        out["kms_key_arn"] = data["KmsKeyArn"]
    if data.get("SseType") is not None:
        import capo_ebs.types.sse_type

        out["sse_type"] = capo_ebs.types.sse_type.deserialize_json(data["SseType"])
    return out
