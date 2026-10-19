"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#GetVehicleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.vehicle_name


class GetVehicleRequest(TypedDict, closed=True):
    vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName"
    """<p> The ID of the vehicle to retrieve information about. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetVehicleRequest) -> dict:
    out: dict = {}
    out["vehicleName"] = value["vehicle_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetVehicleRequest:
    out: GetVehicleRequest = {}  # type: ignore[typeddict-item]
    if data.get("vehicleName") is not None:
        out["vehicle_name"] = data["vehicleName"]
    else:
        out["vehicle_name"] = ""
    return out
