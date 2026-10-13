"""Generated from Smithy shape ``com.amazonaws.fsx#RestoreVolumeFromSnapshotResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.administrative_actions
    import capo_fsx.types.volume_id
    import capo_fsx.types.volume_lifecycle


class RestoreVolumeFromSnapshotResponse(TypedDict, closed=True):
    volume_id: NotRequired["capo_fsx.types.volume_id.VolumeId"]
    """<p>The ID of the volume that you restored.</p>"""
    lifecycle: NotRequired["capo_fsx.types.volume_lifecycle.VolumeLifecycle"]
    """<p>The lifecycle state of the volume being restored.</p>"""
    administrative_actions: NotRequired[
        "capo_fsx.types.administrative_actions.AdministrativeActions"
    ]
    """<p>A list of administrative actions for the file system that are in process or waiting to be processed. Administrative actions describe changes to the Amazon FSx system.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RestoreVolumeFromSnapshotResponse) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    if "lifecycle" in value:
        import capo_fsx.types.volume_lifecycle

        out["Lifecycle"] = capo_fsx.types.volume_lifecycle.serialize_aws_json_1_1(
            value["lifecycle"]
        )
    if "administrative_actions" in value:
        import capo_fsx.types.administrative_actions

        out["AdministrativeActions"] = (
            capo_fsx.types.administrative_actions.serialize_aws_json_1_1(
                value["administrative_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RestoreVolumeFromSnapshotResponse:
    out: RestoreVolumeFromSnapshotResponse = {}  # type: ignore[typeddict-item]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    if data.get("Lifecycle") is not None:
        import capo_fsx.types.volume_lifecycle

        out["lifecycle"] = capo_fsx.types.volume_lifecycle.deserialize_aws_json_1_1(
            data["Lifecycle"]
        )
    if data.get("AdministrativeActions") is not None:
        import capo_fsx.types.administrative_actions

        out["administrative_actions"] = (
            capo_fsx.types.administrative_actions.deserialize_aws_json_1_1(
                data["AdministrativeActions"]
            )
        )
    return out


def redact_sensitive(value: RestoreVolumeFromSnapshotResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "administrative_actions" in value:
        import capo_fsx.types.administrative_actions

        out["administrative_actions"] = (
            capo_fsx.types.administrative_actions.redact_sensitive(
                value["administrative_actions"]
            )
        )
    return out
