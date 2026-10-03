"""Generated from Smithy shape ``com.amazonaws.ec2#Snapshot``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.boolean
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.long
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.snapshot_completion_duration_minutes_response
    import capo_ec2.types.snapshot_state
    import capo_ec2.types.sse_type
    import capo_ec2.types.storage_tier
    import capo_ec2.types.string
    import capo_ec2.types.tag_list
    import capo_ec2.types.transfer_type


class Snapshot(TypedDict, closed=True):
    owner_alias: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Web Services owner alias, from an Amazon-maintained list (<code>amazon</code>). This is not the user-configured Amazon Web Services account alias set using the IAM console.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the snapshot is stored. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/snapshots-outposts.html">Amazon EBS local snapshots on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    tags: NotRequired["capo_ec2.types.tag_list.TagList"]
    """<p>Any tags assigned to the snapshot.</p>"""
    storage_tier: NotRequired["capo_ec2.types.storage_tier.StorageTier"]
    """<p>The storage tier in which the snapshot is stored. <code>standard</code> indicates that the snapshot is stored in the standard snapshot storage tier and that it is ready for use. <code>archive</code> indicates that the snapshot is currently archived and that it must be restored before it can be used.</p>"""
    restore_expiry_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>Only for archived snapshots that are temporarily restored. Indicates the date and time when a temporarily restored snapshot will be automatically re-archived.</p>"""
    sse_type: NotRequired["capo_ec2.types.sse_type.SSEType"]
    """<p>Reserved for future use.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone or Local Zone of the snapshot. For example, <code>us-west-1a</code> (Availability Zone) or <code>us-west-2-lax-1a</code> (Local Zone).</p>"""
    transfer_type: NotRequired["capo_ec2.types.transfer_type.TransferType"]
    """<note> <p>Only for snapshot copies.</p> </note> <p>Indicates whether the snapshot copy was created with a standard or time-based snapshot copy operation. Time-based snapshot copy operations complete within the completion duration specified in the request. Standard snapshot copy operations are completed on a best-effort basis.</p> <ul> <li> <p> <code>standard</code> - The snapshot copy was created with a standard snapshot copy operation.</p> </li> <li> <p> <code>time-based</code> - The snapshot copy was created with a time-based snapshot copy operation.</p> </li> </ul>"""
    completion_duration_minutes: NotRequired[
        "capo_ec2.types.snapshot_completion_duration_minutes_response.SnapshotCompletionDurationMinutesResponse"
    ]
    """<note> <p>Only for snapshot copies created with time-based snapshot copy operations.</p> </note> <p>The completion duration requested for the time-based snapshot copy operation.</p>"""
    completion_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The time stamp when the snapshot was completed.</p>"""
    full_snapshot_size_in_bytes: NotRequired["capo_ec2.types.long.Long"]
    """<p>The full size of the snapshot, in bytes.</p> <important> <p>This is <b>not</b> the incremental size of the snapshot. This is the full snapshot size and represents the size of all the blocks that were written to the source volume at the time the snapshot was created.</p> </important>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the snapshot. Each snapshot receives a unique identifier when it is created.</p>"""
    volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the volume that was used to create the snapshot. Snapshots created by a copy snapshot operation have an arbitrary volume ID that you should not use for any purpose.</p>"""
    state: NotRequired["capo_ec2.types.snapshot_state.SnapshotState"]
    """<p>The snapshot state.</p>"""
    state_message: NotRequired["capo_ec2.types.string.String"]
    """<p>Encrypted Amazon EBS snapshots are copied asynchronously. If a snapshot copy operation fails (for example, if the proper KMS permissions are not obtained) this field displays error state details to help you diagnose why the error occurred. This parameter is only returned by <a>DescribeSnapshots</a>.</p>"""
    start_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time stamp when the snapshot was initiated.</p>"""
    progress: NotRequired["capo_ec2.types.string.String"]
    """<p>The progress of the snapshot, as a percentage.</p>"""
    owner_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Amazon Web Services account that owns the EBS snapshot.</p>"""
    description: NotRequired["capo_ec2.types.string.String"]
    """<p>The description for the snapshot.</p>"""
    volume_size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    encrypted: NotRequired["capo_ec2.types.boolean.Boolean"]
    """<p>Indicates whether the snapshot is encrypted.</p>"""
    kms_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that was used to protect the volume encryption key for the parent volume.</p>"""
    data_encryption_key_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The data encryption key identifier for the snapshot. This value is a unique identifier that corresponds to the data encryption key that was used to encrypt the original volume or snapshot copy. Because data encryption keys are inherited by volumes created from snapshots, and vice versa, if snapshots share the same data encryption key identifier, then they belong to the same volume/snapshot lineage. This parameter is only returned by <a>DescribeSnapshots</a>.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: Snapshot, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "owner_alias" in value:
        pairs.append((f"{key_prefix}OwnerAlias", str(value["owner_alias"])))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "tags" in value:
        import capo_ec2.types.tag_list

        capo_ec2.types.tag_list.serialize_ec2_query(
            value["tags"], pairs, f"{key_prefix}TagSet"
        )
    if "storage_tier" in value:
        import capo_ec2.types.storage_tier

        capo_ec2.types.storage_tier.serialize_ec2_query(
            value["storage_tier"], pairs, f"{key_prefix}StorageTier"
        )
    if "restore_expiry_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["restore_expiry_time"], pairs, f"{key_prefix}RestoreExpiryTime"
        )
    if "sse_type" in value:
        import capo_ec2.types.sse_type

        capo_ec2.types.sse_type.serialize_ec2_query(
            value["sse_type"], pairs, f"{key_prefix}SseType"
        )
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "transfer_type" in value:
        import capo_ec2.types.transfer_type

        capo_ec2.types.transfer_type.serialize_ec2_query(
            value["transfer_type"], pairs, f"{key_prefix}TransferType"
        )
    if "completion_duration_minutes" in value:
        pairs.append(
            (
                f"{key_prefix}CompletionDurationMinutes",
                str(value["completion_duration_minutes"]),
            )
        )
    if "completion_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["completion_time"], pairs, f"{key_prefix}CompletionTime"
        )
    if "full_snapshot_size_in_bytes" in value:
        pairs.append(
            (
                f"{key_prefix}FullSnapshotSizeInBytes",
                str(value["full_snapshot_size_in_bytes"]),
            )
        )
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "state" in value:
        import capo_ec2.types.snapshot_state

        capo_ec2.types.snapshot_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}Status"
        )
    if "state_message" in value:
        pairs.append((f"{key_prefix}StatusMessage", str(value["state_message"])))
    if "start_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["start_time"], pairs, f"{key_prefix}StartTime"
        )
    if "progress" in value:
        pairs.append((f"{key_prefix}Progress", str(value["progress"])))
    if "owner_id" in value:
        pairs.append((f"{key_prefix}OwnerId", str(value["owner_id"])))
    if "description" in value:
        pairs.append((f"{key_prefix}Description", str(value["description"])))
    if "volume_size" in value:
        pairs.append((f"{key_prefix}VolumeSize", str(value["volume_size"])))
    if "encrypted" in value:
        pairs.append(
            (f"{key_prefix}Encrypted", "true" if value["encrypted"] else "false")
        )
    if "kms_key_id" in value:
        pairs.append((f"{key_prefix}KmsKeyId", str(value["kms_key_id"])))
    if "data_encryption_key_id" in value:
        pairs.append(
            (f"{key_prefix}DataEncryptionKeyId", str(value["data_encryption_key_id"]))
        )


def deserialize_ec2_query(el: Element) -> Snapshot:
    out: Snapshot = {}  # type: ignore[typeddict-item]
    child_owner_alias = el.find("ownerAlias")
    if child_owner_alias is not None:
        out["owner_alias"] = str(child_owner_alias.text or "")
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_tags = el.find("tagSet")
    if child_tags is not None:
        import capo_ec2.types.tag_list

        out["tags"] = capo_ec2.types.tag_list.deserialize_ec2_query(child_tags)
    child_storage_tier = el.find("storageTier")
    if child_storage_tier is not None:
        import capo_ec2.types.storage_tier

        out["storage_tier"] = capo_ec2.types.storage_tier.deserialize_ec2_query(
            child_storage_tier
        )
    child_restore_expiry_time = el.find("restoreExpiryTime")
    if child_restore_expiry_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["restore_expiry_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_restore_expiry_time
            )
        )
    child_sse_type = el.find("sseType")
    if child_sse_type is not None:
        import capo_ec2.types.sse_type

        out["sse_type"] = capo_ec2.types.sse_type.deserialize_ec2_query(child_sse_type)
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_transfer_type = el.find("transferType")
    if child_transfer_type is not None:
        import capo_ec2.types.transfer_type

        out["transfer_type"] = capo_ec2.types.transfer_type.deserialize_ec2_query(
            child_transfer_type
        )
    child_completion_duration_minutes = el.find("completionDurationMinutes")
    if child_completion_duration_minutes is not None:
        out["completion_duration_minutes"] = int(
            child_completion_duration_minutes.text or ""
        )
    child_completion_time = el.find("completionTime")
    if child_completion_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["completion_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_completion_time
            )
        )
    child_full_snapshot_size_in_bytes = el.find("fullSnapshotSizeInBytes")
    if child_full_snapshot_size_in_bytes is not None:
        out["full_snapshot_size_in_bytes"] = int(
            child_full_snapshot_size_in_bytes.text or ""
        )
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_volume_id = el.find("volumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_state = el.find("status")
    if child_state is not None:
        import capo_ec2.types.snapshot_state

        out["state"] = capo_ec2.types.snapshot_state.deserialize_ec2_query(child_state)
    child_state_message = el.find("statusMessage")
    if child_state_message is not None:
        out["state_message"] = str(child_state_message.text or "")
    child_start_time = el.find("startTime")
    if child_start_time is not None:
        import capo_ec2.types.date_time

        out["start_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_start_time
        )
    child_progress = el.find("progress")
    if child_progress is not None:
        out["progress"] = str(child_progress.text or "")
    child_owner_id = el.find("ownerId")
    if child_owner_id is not None:
        out["owner_id"] = str(child_owner_id.text or "")
    child_description = el.find("description")
    if child_description is not None:
        out["description"] = str(child_description.text or "")
    child_volume_size = el.find("volumeSize")
    if child_volume_size is not None:
        out["volume_size"] = int(child_volume_size.text or "")
    child_encrypted = el.find("encrypted")
    if child_encrypted is not None:
        out["encrypted"] = (child_encrypted.text or "").lower() == "true"
    child_kms_key_id = el.find("kmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_data_encryption_key_id = el.find("dataEncryptionKeyId")
    if child_data_encryption_key_id is not None:
        out["data_encryption_key_id"] = str(child_data_encryption_key_id.text or "")
    return out
