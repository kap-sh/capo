"""Generated from Smithy shape ``com.amazonaws.athena#GetCapacityAssignmentConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.capacity_reservation_name


class GetCapacityAssignmentConfigurationInput(TypedDict, closed=True):
    capacity_reservation_name: (
        "capo_athena.types.capacity_reservation_name.CapacityReservationName"
    )
    """<p>The name of the capacity reservation to retrieve the capacity assignment configuration for.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCapacityAssignmentConfigurationInput) -> dict:
    out: dict = {}
    out["CapacityReservationName"] = value["capacity_reservation_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCapacityAssignmentConfigurationInput:
    out: GetCapacityAssignmentConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("CapacityReservationName") is not None:
        out["capacity_reservation_name"] = data["CapacityReservationName"]
    else:
        out["capacity_reservation_name"] = ""
    return out
