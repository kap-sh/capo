"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#CreateVolumeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.volume_id


class CreateVolumeResponse(TypedDict, closed=True):
    volume_id: NotRequired["capo_workspaces_instances.types.volume_id.VolumeId"]
    """<p>Unique identifier for the new volume.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVolumeResponse) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVolumeResponse:
    out: CreateVolumeResponse = {}  # type: ignore[typeddict-item]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: CreateVolumeResponse) -> dict:
    out: dict = {}
    if "volume_id" in value:
        out["VolumeId"] = value["volume_id"]
    return out


def deserialize_cbor(data: dict) -> CreateVolumeResponse:
    out: CreateVolumeResponse = {}  # type: ignore[typeddict-item]
    if data.get("VolumeId") is not None:
        out["volume_id"] = data["VolumeId"]
    return out
