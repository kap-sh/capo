"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteTollPriceValueRange``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_geo_routes.types.sensitive_double


class RouteTollPriceValueRange(TypedDict, closed=True):
    min: "capo_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Minimum price.</p>"""
    max: "capo_geo_routes.types.sensitive_double.SensitiveDouble"
    """<p>Maximum price.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteTollPriceValueRange) -> dict:
    out: dict = {}
    out["Min"] = (
        "NaN"
        if value["min"] != value["min"]
        else "Infinity"
        if value["min"] == float("inf")
        else "-Infinity"
        if value["min"] == float("-inf")
        else value["min"]
    )
    out["Max"] = (
        "NaN"
        if value["max"] != value["max"]
        else "Infinity"
        if value["max"] == float("inf")
        else "-Infinity"
        if value["max"] == float("-inf")
        else value["max"]
    )
    return out


def deserialize_json(data: dict) -> RouteTollPriceValueRange:
    out: RouteTollPriceValueRange = {}  # type: ignore[typeddict-item]
    if data.get("Min") is not None:
        out["min"] = float(data["Min"])
    else:
        out["min"] = 0.0
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    else:
        out["max"] = 0.0
    return out


def redact_sensitive(value: RouteTollPriceValueRange) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "min" in value:
        out["min"] = "*** Sensitive Data Redacted ***"
    if "max" in value:
        out["max"] = "*** Sensitive Data Redacted ***"
    return out
