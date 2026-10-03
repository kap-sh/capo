"""Generated from Smithy shape ``com.amazonaws.ec2#SnapshotInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.snapshot_state
    import capo_ec2.types.sse_type
    import capo_ec2.types.string
    import capo_ec2.types.tag_list


class SnapshotInfo(TypedDict, closed=True):
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>Description specified by the CreateSnapshotRequest that has been applied to all snapshots.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Tags associated with this snapshot.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>Source volume from which this snapshot was created.</p>"""
    state: NotRequired["capo_ec2.types.snapshot_state.SnapshotState"]
    """<p>Current state of the snapshot.</p>"""
    volume_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>Size of the volume from which this snapshot was created.</p>"""
    start_time: NotRequired["capo_ec2.types.millisecond_date_time.MillisecondDateTime"]
    """<p>Time this snapshot was started. This is the same for all snapshots initiated by the same request.</p>"""
    progress: NotRequired["capo_ec2.types.string.String"]
    """<p>Progress this snapshot has made towards completing.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>Account id used when creating this snapshot.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>Snapshot id that can be used to describe this snapshot.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the snapshot is stored. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html">Amazon EBS local snapshots on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    sse_type: NotRequired["capo_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone of the snapshots. For example, <code>us-west-1a</code> (Availability Zone) or <code>us-west-2-lax-1a</code> (Local Zone).</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: SnapshotInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "state" in value:
        import capo_ec2.types.snapshot_state

        capo_ec2.types.snapshot_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "volume_size" in value:
        pairs.append((f"{key_prefix}VolumeSize", str(value["volume_size"])))
    if "start_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "progress" in value:
        pairs.append((f"{key_prefix}Progress", str(value["progress"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "sse_type" in value:
        import capo_ec2.types.sse_type

        capo_ec2.types.sse_type.serialize_ec2_query(
            value["sse_type"], pairs, f"{key_prefix}SseType"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))


def deserialize_ec2_query(el: Element) -> SnapshotInfo:
    out: SnapshotInfo = {}  # type: ignore[typeddict-item]
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_volume_id = el.find("volumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.snapshot_state

        out["state"] = capo_ec2.types.snapshot_state.deserialize_ec2_query(child_state)
    child_volume_size = el.find("volumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_start_time = el.find("startTime")
    if child_start_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["start_time"] = capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
            child_start_time
        )
    child_progress = el.find("progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_sse_type = el.find("sseType")
    if child_sse_type is not None:
        import capo_ec2.types.sse_type

        out["sse_type"] = capo_ec2.types.sse_type.deserialize_ec2_query(child_sse_type)
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    return out
