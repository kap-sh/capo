"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#BatchCreateVehicleRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.create_vehicle_request_items


class BatchCreateVehicleRequest(TypedDict, closed=True):
    vehicles: (
        "capo_iotfleetwise.types.create_vehicle_request_items.createVehicleRequestItems"
    )
    """<p> A list of information about each vehicle to create. For more information, see the API data type.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateVehicleRequest) -> dict:
    out: dict = {}
    import capo_iotfleetwise.types.create_vehicle_request_items

    out["vehicles"] = (
        capo_iotfleetwise.types.create_vehicle_request_items.serialize_aws_json_1_0(
            value["vehicles"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateVehicleRequest:
    out: BatchCreateVehicleRequest = {}  # type: ignore[typeddict-item]
    if data.get("vehicles") is not None:
        import capo_iotfleetwise.types.create_vehicle_request_items

        out["vehicles"] = (
            capo_iotfleetwise.types.create_vehicle_request_items.deserialize_aws_json_1_0(
                data["vehicles"]
            )
        )
    else:
        out["vehicles"] = []
    return out
