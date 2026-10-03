"""Generated from Smithy shape ``com.amazonaws.ec2#VolumeRecycleBinInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_ec2._protocol.xml import Element

if TYPE_CHECKING:
    import capo_ec2.types.date_time
    import capo_ec2.types.integer
    import capo_ec2.types.millisecond_date_time
    import capo_ec2.types.operator_response
    import capo_ec2.types.string
    import capo_ec2.types.volume_id
    import capo_ec2.types.volume_state
    import capo_ec2.types.volume_type


class VolumeRecycleBinInfo(TypedDict, closed=True):
    volume_id: NotRequired["capo_ec2.types.volume_id.VolumeId"]
    """<p>The ID of the volume.</p>"""
    volume_type: NotRequired["capo_ec2.types.volume_type.VolumeType"]
    """<p>The volume type.</p>"""
    state: NotRequired["capo_ec2.types.volume_state.VolumeState"]
    """<p>The state of the volume.</p>"""
    size: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The size of the volume, in GiB.</p>"""
    iops: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The number of I/O operations per second (IOPS) for the volume.</p>"""
    throughput: NotRequired["capo_ec2.types.integer.Integer"]
    """<p>The throughput that the volume supports, in MiB/s.</p>"""
    outpost_arn: NotRequired["capo_ec2.types.string.String"]
    """<p>The ARN of the Outpost on which the volume is stored. For more information, see <a href="https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volumes-outposts.html">Amazon EBS volumes on Outposts</a> in the <i>Amazon EBS User Guide</i>.</p>"""
    availability_zone: NotRequired["capo_ec2.types.string.String"]
    """<p>The Availability Zone for the volume.</p>"""
    availability_zone_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the Availability Zone for the volume.</p>"""
    source_volume_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The ID of the source volume.</p>"""
    snapshot_id: NotRequired["capo_ec2.types.string.String"]
    """<p>The snapshot from which the volume was created, if applicable.</p>"""
    operator: NotRequired["capo_ec2.types.operator_response.OperatorResponse"]
    """<p>The service provider that manages the volume.</p>"""
    create_time: NotRequired["capo_ec2.types.date_time.DateTime"]
    """<p>The time stamp when volume creation was initiated.</p>"""
    recycle_bin_enter_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the volume entered the Recycle Bin.</p>"""
    recycle_bin_exit_time: NotRequired[
        "capo_ec2.types.millisecond_date_time.MillisecondDateTime"
    ]
    """<p>The date and time when the volume is to be permanently deleted from the Recycle Bin.</p>"""


# --- ec2Query ser/de ---
def serialize_ec2_query(
    value: VolumeRecycleBinInfo, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "volume_id" in value:
        pairs.append((f"{key_prefix}VolumeId", str(value["volume_id"])))
    if "volume_type" in value:
        import capo_ec2.types.volume_type

        capo_ec2.types.volume_type.serialize_ec2_query(
            value["volume_type"], pairs, f"{key_prefix}VolumeType"
        )
    if "state" in value:
        import capo_ec2.types.volume_state

        capo_ec2.types.volume_state.serialize_ec2_query(
            value["state"], pairs, f"{key_prefix}State"
        )
    if "size" in value:
        pairs.append((f"{key_prefix}Size", str(value["size"])))
    if "iops" in value:
        pairs.append((f"{key_prefix}Iops", str(value["iops"])))
    if "throughput" in value:
        pairs.append((f"{key_prefix}Throughput", str(value["throughput"])))
    if "outpost_arn" in value:
        pairs.append((f"{key_prefix}OutpostArn", str(value["outpost_arn"])))
    if "availability_zone" in value:
        pairs.append((f"{key_prefix}AvailabilityZone", str(value["availability_zone"])))
    if "availability_zone_id" in value:
        pairs.append(
            (f"{key_prefix}AvailabilityZoneId", str(value["availability_zone_id"]))
        )
    if "source_volume_id" in value:
        pairs.append((f"{key_prefix}SourceVolumeId", str(value["source_volume_id"])))
    if "snapshot_id" in value:
        pairs.append((f"{key_prefix}SnapshotId", str(value["snapshot_id"])))
    if "operator" in value:
        import capo_ec2.types.operator_response

        capo_ec2.types.operator_response.serialize_ec2_query(
            value["operator"], pairs, f"{key_prefix}Operator"
        )
    if "create_time" in value:
        import capo_ec2.types.date_time

        capo_ec2.types.date_time.serialize_ec2_query(
            value["create_time"], pairs, f"{key_prefix}CreateTime"
        )
    if "recycle_bin_enter_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_enter_time"], pairs, f"{key_prefix}RecycleBinEnterTime"
        )
    if "recycle_bin_exit_time" in value:
        import capo_ec2.types.millisecond_date_time

        capo_ec2.types.millisecond_date_time.serialize_ec2_query(
            value["recycle_bin_exit_time"], pairs, f"{key_prefix}RecycleBinExitTime"
        )


def deserialize_ec2_query(el: Element) -> VolumeRecycleBinInfo:
    out: VolumeRecycleBinInfo = {}  # type: ignore[typeddict-item]
    child_volume_id = el.find("volumeId")
    if child_volume_id is not None:
        out["volume_id"] = str(child_volume_id.text or "")
    child_volume_type = el.find("volumeType")
    if child_volume_type is not None:
        import capo_ec2.types.volume_type

        out["volume_type"] = capo_ec2.types.volume_type.deserialize_ec2_query(
            child_volume_type
        )
    child_state = el.find("state")
    if child_state is not None:
        import capo_ec2.types.volume_state

        out["state"] = capo_ec2.types.volume_state.deserialize_ec2_query(child_state)
    child_size = el.find("size")
    if child_size is not None:
        out["size"] = int(child_size.text or "")
    child_iops = el.find("iops")
    if child_iops is not None:
        out["iops"] = int(child_iops.text or "")
    child_throughput = el.find("throughput")
    if child_throughput is not None:
        out["throughput"] = int(child_throughput.text or "")
    child_outpost_arn = el.find("outpostArn")
    if child_outpost_arn is not None:
        out["outpost_arn"] = str(child_outpost_arn.text or "")
    child_availability_zone = el.find("availabilityZone")
    if child_availability_zone is not None:
        out["availability_zone"] = str(child_availability_zone.text or "")
    child_availability_zone_id = el.find("availabilityZoneId")
    if child_availability_zone_id is not None:
        out["availability_zone_id"] = str(child_availability_zone_id.text or "")
    child_source_volume_id = el.find("sourceVolumeId")
    if child_source_volume_id is not None:
        out["source_volume_id"] = str(child_source_volume_id.text or "")
    child_snapshot_id = el.find("snapshotId")
    if child_snapshot_id is not None:
        out["snapshot_id"] = str(child_snapshot_id.text or "")
    child_operator = el.find("operator")
    if child_operator is not None:
        import capo_ec2.types.operator_response

        out["operator"] = capo_ec2.types.operator_response.deserialize_ec2_query(
            child_operator
        )
    child_create_time = el.find("createTime")
    if child_create_time is not None:
        import capo_ec2.types.date_time

        out["create_time"] = capo_ec2.types.date_time.deserialize_ec2_query(
            child_create_time
        )
    child_recycle_bin_enter_time = el.find("recycleBinEnterTime")
    if child_recycle_bin_enter_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["recycle_bin_enter_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_enter_time
            )
        )
    child_recycle_bin_exit_time = el.find("recycleBinExitTime")
    if child_recycle_bin_exit_time is not None:
        import capo_ec2.types.millisecond_date_time

        out["recycle_bin_exit_time"] = (
            capo_ec2.types.millisecond_date_time.deserialize_ec2_query(
                child_recycle_bin_exit_time
            )
        )
    return out
