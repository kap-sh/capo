"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteVolumeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id
    import capo_deadline.types.volume_id


class DeleteVolumeRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm that contains the fleet."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the fleet that contains the volume."""
    volume_id: "capo_deadline.types.volume_id.VolumeId"
    """The volume ID of the volume to delete."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVolumeRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteVolumeRequest:
    out: DeleteVolumeRequest = {}  # type: ignore[typeddict-item]
    return out
