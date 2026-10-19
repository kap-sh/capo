"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fleet_id


class GetFleetRequest(TypedDict, closed=True):
    fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId"
    """<p> The ID of the fleet to retrieve information about. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetFleetRequest) -> dict:
    out: dict = {}
    out["fleetId"] = value["fleet_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetFleetRequest:
    out: GetFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    return out
