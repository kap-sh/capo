"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#DisassociateVehicleFleetRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.fleet_id
    import capo_iotfleetwise.types.vehicle_name


class DisassociateVehicleFleetRequest(TypedDict, closed=True):
    vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName"
    """<p> The unique ID of the vehicle to disassociate from the fleet.</p>"""
    fleet_id: "capo_iotfleetwise.types.fleet_id.fleetId"
    """<p> The unique ID of a fleet. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateVehicleFleetRequest) -> dict:
    out: dict = {}
    out["vehicleName"] = value["vehicle_name"]
    out["fleetId"] = value["fleet_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateVehicleFleetRequest:
    out: DisassociateVehicleFleetRequest = {}  # type: ignore[typeddict-item]
    if data.get("vehicleName") is not None:
        out["vehicle_name"] = data["vehicleName"]
    else:
        out["vehicle_name"] = ""
    if data.get("fleetId") is not None:
        out["fleet_id"] = data["fleetId"]
    else:
        out["fleet_id"] = ""
    return out
