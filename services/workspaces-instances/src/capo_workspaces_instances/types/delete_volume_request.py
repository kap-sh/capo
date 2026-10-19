"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#DeleteVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.volume_id


class DeleteVolumeRequest(TypedDict, closed=True):
    volume_id: "capo_workspaces_instances.types.volume_id.VolumeId"
    """<p>Identifier of the volume to delete.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteVolumeRequest) -> dict:
    out: dict = {}
    out["VolumeId"] = value["volume_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteVolumeRequest:
    out: DeleteVolumeRequest = {}  # type: ignore[typeddict-item]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    else:
        out["volume_id"] = ""
    return out
