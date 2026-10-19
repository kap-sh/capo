"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateSnapshotScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.description
    import capo_storage_gateway.types.hour_of_day
    import capo_storage_gateway.types.recurrence_in_hours
    import capo_storage_gateway.types.tags
    import capo_storage_gateway.types.volume_arn


class UpdateSnapshotScheduleInput(TypedDict, closed=True):
    volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN"
    """<p>The Amazon Resource Name (ARN) of the volume. Use the <a>ListVolumes</a> operation to return a list of gateway volumes.</p>"""
    start_at: "capo_storage_gateway.types.hour_of_day.HourOfDay"
    """<p>The hour of the day at which the snapshot schedule begins represented as <i>hh</i>, where <i>hh</i> is the hour (0 to 23). The hour of the day is in the time zone of the gateway.</p>"""
    recurrence_in_hours: (
        "capo_storage_gateway.types.recurrence_in_hours.RecurrenceInHours"
    )
    """<p>Frequency of snapshots. Specify the number of hours between snapshots.</p>"""
    description: NotRequired["capo_storage_gateway.types.description.Description"]
    """<p>Optional description of the snapshot that overwrites the existing description.</p>"""
    tags: NotRequired["capo_storage_gateway.types.tags.Tags"]
    """<p>A list of up to 50 tags that can be assigned to a snapshot. Each tag is a key-value pair.</p> <note> <p>Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tag's key is 128 characters, and the maximum length for a tag's value is 256.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSnapshotScheduleInput) -> dict:
    out: dict = {}
    out["VolumeARN"] = value["volume_arn"]
    out["StartAt"] = value["start_at"]
    out["RecurrenceInHours"] = value["recurrence_in_hours"]
    if "description" in value:
        out["Description"] = value["description"]
    if "tags" in value:
        import capo_storage_gateway.types.tags

        out["Tags"] = capo_storage_gateway.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSnapshotScheduleInput:
    out: UpdateSnapshotScheduleInput = {}  # type: ignore[typeddict-item]
    if data.get("VolumeARN") is not None:
        out["volume_arn"] = data["VolumeARN"]
    else:
        out["volume_arn"] = ""
    if data.get("StartAt") is not None:
        out["start_at"] = data["StartAt"]
    else:
        out["start_at"] = 0
    if data.get("RecurrenceInHours") is not None:
        out["recurrence_in_hours"] = data["RecurrenceInHours"]
    else:
        out["recurrence_in_hours"] = 0
    if data.get("Description") is not None:
        out["description"] = data["Description"]
    if data.get("Tags") is not None:
        import capo_storage_gateway.types.tags

        out["tags"] = capo_storage_gateway.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
