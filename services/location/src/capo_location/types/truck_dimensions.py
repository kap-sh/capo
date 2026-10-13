"""Generated from Smithy shape ``com.amazonaws.location#TruckDimensions``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.dimension_unit
    import capo_location.types.sensitive_double


class TruckDimensions(TypedDict, closed=True):
    length: NotRequired["capo_location.types.sensitive_double.SensitiveDouble"]
    """<p>The length of the truck.</p> <ul> <li> <p>For example, <code>15.5</code>.</p> </li> </ul> <note> <p> For routes calculated with a HERE resource, this value must be between 0 and 300 meters. </p> </note>"""
    height: NotRequired["capo_location.types.sensitive_double.SensitiveDouble"]
    """<p>The height of the truck.</p> <ul> <li> <p>For example, <code>4.5</code>.</p> </li> </ul> <note> <p> For routes calculated with a HERE resource, this value must be between 0 and 50 meters. </p> </note>"""
    width: NotRequired["capo_location.types.sensitive_double.SensitiveDouble"]
    """<p>The width of the truck.</p> <ul> <li> <p>For example, <code>4.5</code>.</p> </li> </ul> <note> <p> For routes calculated with a HERE resource, this value must be between 0 and 50 meters. </p> </note>"""
    unit: NotRequired["capo_location.types.dimension_unit.DimensionUnit"]
    """<p> Specifies the unit of measurement for the truck dimensions.</p> <p>Default Value: <code>Meters</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TruckDimensions) -> dict:
    out: dict = {}
    if "length" in value:
        out["Length"] = (
            "NaN"
            if value["length"] != value["length"]
            else "Infinity"
            if value["length"] == float("inf")
            else "-Infinity"
            if value["length"] == float("-inf")
            else value["length"]
        )
    if "height" in value:
        out["Height"] = (
            "NaN"
            if value["height"] != value["height"]
            else "Infinity"
            if value["height"] == float("inf")
            else "-Infinity"
            if value["height"] == float("-inf")
            else value["height"]
        )
    if "width" in value:
        out["Width"] = (
            "NaN"
            if value["width"] != value["width"]
            else "Infinity"
            if value["width"] == float("inf")
            else "-Infinity"
            if value["width"] == float("-inf")
            else value["width"]
        )
    if "unit" in value:
        out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> TruckDimensions:
    out: TruckDimensions = {}  # type: ignore[typeddict-item]
    if data.get("Length") is not None:
        out["length"] = float(data["Length"])
    if data.get("Height") is not None:
        out["height"] = float(data["Height"])
    if data.get("Width") is not None:
        out["width"] = float(data["Width"])
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    return out


def redact_sensitive(value: TruckDimensions) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "length" in value:
        out["length"] = "*** Sensitive Data Redacted ***"
    if "height" in value:
        out["height"] = "*** Sensitive Data Redacted ***"
    if "width" in value:
        out["width"] = "*** Sensitive Data Redacted ***"
    return out
