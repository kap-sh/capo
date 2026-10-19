"""Generated from Smithy shape ``com.amazonaws.deadline#CreateFleetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.fleet_id


class CreateFleetResponse(TypedDict, closed=True):
    fleet_id: "capo_deadline.types.fleet_id.FleetId"
    """<p>The fleet ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFleetResponse) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    return out


def deserialize_json(data: dict) -> CreateFleetResponse:
    out: CreateFleetResponse = {}  # type: ignore[typeddict-item]
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    return out
