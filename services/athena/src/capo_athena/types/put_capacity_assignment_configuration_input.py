"""Generated from Smithy shape ``com.amazonaws.athena#PutCapacityAssignmentConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.capacity_assignments_list
    import capo_athena.types.capacity_reservation_name


class PutCapacityAssignmentConfigurationInput(TypedDict, closed=True):
    capacity_reservation_name: (
        "capo_athena.types.capacity_reservation_name.CapacityReservationName"
    )
    """<p>The name of the capacity reservation to put a capacity assignment configuration for.</p>"""
    capacity_assignments: (
        "capo_athena.types.capacity_assignments_list.CapacityAssignmentsList"
    )
    """<p>The list of assignments for the capacity assignment configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutCapacityAssignmentConfigurationInput) -> dict:
    out: dict = {}
    out["CapacityReservationName"] = value["capacity_reservation_name"]
    import capo_athena.types.capacity_assignments_list

    out["CapacityAssignments"] = (
        capo_athena.types.capacity_assignments_list.serialize_aws_json_1_1(
            value["capacity_assignments"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutCapacityAssignmentConfigurationInput:
    out: PutCapacityAssignmentConfigurationInput = {}  # type: ignore[typeddict-item]
    if data.get("CapacityReservationName") is not None:
        out["capacity_reservation_name"] = data["CapacityReservationName"]
    else:
        out["capacity_reservation_name"] = ""
    if data.get("CapacityAssignments") is not None:
        import capo_athena.types.capacity_assignments_list

        out["capacity_assignments"] = (
            capo_athena.types.capacity_assignments_list.deserialize_aws_json_1_1(
                data["CapacityAssignments"]
            )
        )
    else:
        out["capacity_assignments"] = []
    return out
