"""Generated from Smithy shape ``com.amazonaws.deadline#GetFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id


class GetFleetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm in the fleet."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the fleet to get."""


# --- restJson1 ser/de ---
def serialize_json(value: GetFleetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetFleetRequest:
    out: GetFleetRequest = {}  # type: ignore[typeddict-item]
    return out
