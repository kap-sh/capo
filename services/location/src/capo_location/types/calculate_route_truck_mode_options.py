"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteTruckModeOptions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.sensitive_boolean
    import capo_location.types.truck_dimensions
    import capo_location.types.truck_weight


class CalculateRouteTruckModeOptions(TypedDict, closed=True):
    avoid_ferries: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids ferries when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    avoid_tolls: NotRequired["capo_location.types.sensitive_boolean.SensitiveBoolean"]
    """<p>Avoids tolls when calculating routes.</p> <p>Default Value: <code>false</code> </p> <p>Valid Values: <code>false</code> | <code>true</code> </p>"""
    dimensions: NotRequired["capo_location.types.truck_dimensions.TruckDimensions"]
    """<p>Specifies the truck's dimension specifications including length, height, width, and unit of measurement. Used to avoid roads that can't support the truck's dimensions.</p>"""
    weight: NotRequired["capo_location.types.truck_weight.TruckWeight"]
    """<p>Specifies the truck's weight specifications including total weight and unit of measurement. Used to avoid roads that can't support the truck's weight.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteTruckModeOptions) -> dict:
    out: dict = {}
    if "avoid_ferries" in value:
        out["AvoidFerries"] = value["avoid_ferries"]
    if "avoid_tolls" in value:
        out["AvoidTolls"] = value["avoid_tolls"]
    if "dimensions" in value:
        import capo_location.types.truck_dimensions

        out["Dimensions"] = capo_location.types.truck_dimensions.serialize_json(
            value["dimensions"]
        )
    if "weight" in value:
        import capo_location.types.truck_weight

        out["Weight"] = capo_location.types.truck_weight.serialize_json(value["weight"])
    return out


def deserialize_json(data: dict) -> CalculateRouteTruckModeOptions:
    out: CalculateRouteTruckModeOptions = {}  # type: ignore[typeddict-item]
    if data.get("AvoidFerries") is not None:
        out["avoid_ferries"] = data["AvoidFerries"]
    if data.get("AvoidTolls") is not None:
        out["avoid_tolls"] = data["AvoidTolls"]
    if data.get("Dimensions") is not None:
        import capo_location.types.truck_dimensions

        out["dimensions"] = capo_location.types.truck_dimensions.deserialize_json(
            data["Dimensions"]
        )
    if data.get("Weight") is not None:
        import capo_location.types.truck_weight

        out["weight"] = capo_location.types.truck_weight.deserialize_json(
            data["Weight"]
        )
    return out


def redact_sensitive(value: CalculateRouteTruckModeOptions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "avoid_ferries" in value:
        out["avoid_ferries"] = "*** Sensitive Data Redacted ***"
    if "avoid_tolls" in value:
        out["avoid_tolls"] = "*** Sensitive Data Redacted ***"
    if "dimensions" in value:
        import capo_location.types.truck_dimensions

        out["dimensions"] = capo_location.types.truck_dimensions.redact_sensitive(
            value["dimensions"]
        )
    if "weight" in value:
        import capo_location.types.truck_weight

        out["weight"] = capo_location.types.truck_weight.redact_sensitive(
            value["weight"]
        )
    return out
