"""Generated from Smithy shape ``com.amazonaws.athena#UpdateCapacityReservationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_athena.types.capacity_reservation_name
    import capo_athena.types.target_dpus_integer


class UpdateCapacityReservationInput(TypedDict, closed=True):
    target_dpus: "capo_athena.types.target_dpus_integer.TargetDpusInteger"
    """<p>The new number of requested data processing units.</p>"""
    name: "capo_athena.types.capacity_reservation_name.CapacityReservationName"
    """<p>The name of the capacity reservation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateCapacityReservationInput) -> dict:
    out: dict = {}
    out["TargetDpus"] = value["target_dpus"]
    out["Name"] = value["name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateCapacityReservationInput:
    out: UpdateCapacityReservationInput = {}  # type: ignore[typeddict-item]
    if data.get("TargetDpus") is not None:
        out["target_dpus"] = data["TargetDpus"]
    else:
        out["target_dpus"] = 0
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    return out
