"""Generated from Smithy shape ``com.amazonaws.location#TruckWeight``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.sensitive_double
    import capo_location.types.vehicle_weight_unit


class TruckWeight(TypedDict, closed=True):
    total: NotRequired["capo_location.types.sensitive_double.SensitiveDouble"]
    """<p>The total weight of the truck. </p> <ul> <li> <p>For example, <code>3500</code>.</p> </li> </ul>"""
    unit: NotRequired["capo_location.types.vehicle_weight_unit.VehicleWeightUnit"]
    """<p>The unit of measurement to use for the truck weight.</p> <p>Default Value: <code>Kilograms</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TruckWeight) -> dict:
    out: dict = {}
    if "total" in value:
        out["Total"] = (
            "NaN"
            if value["total"] != value["total"]
            else "Infinity"
            if value["total"] == float("inf")
            else "-Infinity"
            if value["total"] == float("-inf")
            else value["total"]
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> TruckWeight:
    out: TruckWeight = {}  # type: ignore[typeddict-item]
    if data.get("Total") is not None:
        out["total"] = float(data["Total"])
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out


def redact_sensitive(value: TruckWeight) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "total" in value:
        out["total"] = "*** Sensitive Data Redacted ***"
    return out
