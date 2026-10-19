"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialCoordinateBounds``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.latitude
    import capo_quicksight.types.longitude


class GeospatialCoordinateBounds(TypedDict, closed=True):
    north: "capo_quicksight.types.latitude.Latitude"
    """<p>The latitude of the north bound of the geospatial coordinate bounds.</p>"""
    south: "capo_quicksight.types.latitude.Latitude"
    """<p>The latitude of the south bound of the geospatial coordinate bounds.</p>"""
    west: "capo_quicksight.types.longitude.Longitude"
    """<p>The longitude of the west bound of the geospatial coordinate bounds.</p>"""
    east: "capo_quicksight.types.longitude.Longitude"
    """<p>The longitude of the east bound of the geospatial coordinate bounds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialCoordinateBounds) -> dict:
    out: dict = {}
    out["North"] = (
        "NaN"
        if value["north"] != value["north"]
        else "Infinity"
        if value["north"] == float("inf")
        else "-Infinity"
        if value["north"] == float("-inf")
        else value["north"]
    )
    out["South"] = (
        "NaN"
        if value["south"] != value["south"]
        else "Infinity"
        if value["south"] == float("inf")
        else "-Infinity"
        if value["south"] == float("-inf")
        else value["south"]
    )
    out["West"] = (
        "NaN"
        if value["west"] != value["west"]
        else "Infinity"
        if value["west"] == float("inf")
        else "-Infinity"
        if value["west"] == float("-inf")
        else value["west"]
    )
    out["East"] = (
        "NaN"
        if value["east"] != value["east"]
        else "Infinity"
        if value["east"] == float("inf")
        else "-Infinity"
        if value["east"] == float("-inf")
        else value["east"]
    )
    return out


def deserialize_json(data: dict) -> GeospatialCoordinateBounds:
    out: GeospatialCoordinateBounds = {}  # type: ignore[typeddict-item]
    if data.get("North") is not None:
        out["north"] = float(data["North"])
    else:
        out["north"] = 0.0
    if data.get("South") is not None:
        out["south"] = float(data["South"])
    else:
        out["south"] = 0.0
    if data.get("West") is not None:
        out["west"] = float(data["West"])
    else:
        out["west"] = 0.0
    if data.get("East") is not None:
        out["east"] = float(data["East"])
    else:
        out["east"] = 0.0
    return out
