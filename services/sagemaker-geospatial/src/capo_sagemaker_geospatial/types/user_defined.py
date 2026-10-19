"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#UserDefined``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.unit


class UserDefined(TypedDict, closed=True):
    value: "float"
    """<p>The value for output resolution of the result.</p>"""
    unit: "capo_sagemaker_geospatial.types.unit.Unit"
    """<p>The units for output resolution of the result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UserDefined) -> dict:
    out: dict = {}
    out["Value"] = (
        "NaN"
        if value["value"] != value["value"]
        else "Infinity"
        if value["value"] == float("inf")
        else "-Infinity"
        if value["value"] == float("-inf")
        else value["value"]
    )
    out["Unit"] = value["unit"]
    return out


def deserialize_json(data: dict) -> UserDefined:
    out: UserDefined = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = float(data["Value"])
    else:
        out["value"] = 0.0
    if data.get("Unit") is not None:
        out["unit"] = data["Unit"]
    else:
        out["unit"] = ""
    return out
