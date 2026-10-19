"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteSnapshotScheduleInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.volume_arn


class DeleteSnapshotScheduleInput(TypedDict, closed=True):
    volume_arn: "capo_storage_gateway.types.volume_arn.VolumeARN"
    """<p>The volume which snapshot schedule to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteSnapshotScheduleInput) -> dict:
    out: dict = {}
    out["VolumeARN"] = value["volume_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteSnapshotScheduleInput:
    out: DeleteSnapshotScheduleInput = {}  # type: ignore[typeddict-item]
    if data.get("VolumeARN") is not None:
        out["volume_arn"] = data["VolumeARN"]
    else:
        out["volume_arn"] = ""
    return out
