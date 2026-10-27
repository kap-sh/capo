"""Generated from Smithy shape ``com.amazonaws.deadline#DeleteFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.client_token
    import capo_deadline.types.farm_id
    import capo_deadline.types.fleet_id


class DeleteFleetRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """The farm ID of the farm to remove from the fleet."""
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """The fleet ID of the fleet to delete."""
    client_token: NotRequired["capo_deadline.types.client_token.ClientToken"]
    """The unique token which the server uses to recognize retries of the same request."""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFleetRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteFleetRequest:
    out: DeleteFleetRequest = {}  # type: ignore[typeddict-item]
    return out
