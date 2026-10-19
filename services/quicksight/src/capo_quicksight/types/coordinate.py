"""Generated from Smithy shape ``com.amazonaws.quicksight#Coordinate``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.coordinate_latitude_double
    import capo_quicksight.types.coordinate_longitude_double


class Coordinate(TypedDict, closed=True):
    latitude: (
        "capo_quicksight.types.coordinate_latitude_double.CoordinateLatitudeDouble"
    )
    """<p>The latitude coordinate value for the geocode preference.</p>"""
    longitude: (
        "capo_quicksight.types.coordinate_longitude_double.CoordinateLongitudeDouble"
    )
    """<p>The longitude coordinate value for the geocode preference.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Coordinate) -> dict:
    out: dict = {}
    out["Latitude"] = (
        "NaN"
        if value["latitude"] != value["latitude"]
        else "Infinity"
        if value["latitude"] == float("inf")
        else "-Infinity"
        if value["latitude"] == float("-inf")
        else value["latitude"]
    )
    out["Longitude"] = (
        "NaN"
        if value["longitude"] != value["longitude"]
        else "Infinity"
        if value["longitude"] == float("inf")
        else "-Infinity"
        if value["longitude"] == float("-inf")
        else value["longitude"]
    )
    return out


def deserialize_json(data: dict) -> Coordinate:
    out: Coordinate = {}  # type: ignore[typeddict-item]
    if data.get("Latitude") is not None:
        out["latitude"] = float(data["Latitude"])
    else:
        out["latitude"] = 0.0
    if data.get("Longitude") is not None:
        out["longitude"] = float(data["Longitude"])
    else:
        out["longitude"] = 0.0
    return out
