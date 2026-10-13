"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteChargeStepDetails``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.energy_kilowatt_hours
    import capo_geo_routes.types.power_kilowatts


class RouteChargeStepDetails(TypedDict, closed=True):
    arrival_charge: NotRequired[
        "capo_geo_routes.types.energy_kilowatt_hours.EnergyKilowattHours"
    ]
    """<p>Estimated vehicle battery charge before this step (in kWh). </p>"""
    consumable_power: NotRequired[
        "capo_geo_routes.types.power_kilowatts.PowerKilowatts"
    ]
    """<p>Maximum charging power available to the vehicle.</p> <p> <b>Unit</b>: <code>KwH</code> </p>"""
    desired_charge: NotRequired[
        "capo_geo_routes.types.energy_kilowatt_hours.EnergyKilowattHours"
    ]
    """<p>Details that are specific to a Charge step.</p> <p> <b>Unit</b>: <code>KwH</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteChargeStepDetails) -> dict:
    out: dict = {}
    if "arrival_charge" in value:
        out["ArrivalCharge"] = (
            "NaN"
            if value["arrival_charge"] != value["arrival_charge"]
            else "Infinity"
            if value["arrival_charge"] == float("inf")
            else "-Infinity"
            if value["arrival_charge"] == float("-inf")
            else value["arrival_charge"]
        )
    if "consumable_power" in value:
        out["ConsumablePower"] = (
            "NaN"
            if value["consumable_power"] != value["consumable_power"]
            else "Infinity"
            if value["consumable_power"] == float("inf")
            else "-Infinity"
            if value["consumable_power"] == float("-inf")
            else value["consumable_power"]
        )
    if "desired_charge" in value:
        out["DesiredCharge"] = (
            "NaN"
            if value["desired_charge"] != value["desired_charge"]
            else "Infinity"
            if value["desired_charge"] == float("inf")
            else "-Infinity"
            if value["desired_charge"] == float("-inf")
            else value["desired_charge"]
        )
    return out


def deserialize_json(data: dict) -> RouteChargeStepDetails:
    out: RouteChargeStepDetails = {}  # type: ignore[typeddict-item]
    if data.get("ArrivalCharge") is not None:
        out["arrival_charge"] = float(data["ArrivalCharge"])
    if data.get("ConsumablePower") is not None:
        out["consumable_power"] = float(data["ConsumablePower"])
    if data.get("DesiredCharge") is not None:
        out["desired_charge"] = float(data["DesiredCharge"])
    return out


def redact_sensitive(value: RouteChargeStepDetails) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "arrival_charge" in value:
        out["arrival_charge"] = "*** Sensitive Data Redacted ***"
    if "consumable_power" in value:
        out["consumable_power"] = "*** Sensitive Data Redacted ***"
    if "desired_charge" in value:
        out["desired_charge"] = "*** Sensitive Data Redacted ***"
    return out
