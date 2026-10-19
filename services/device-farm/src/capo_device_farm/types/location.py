"""Generated from Smithy shape ``com.amazonaws.devicefarm#Location``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_device_farm.types.double


class Location(TypedDict, closed=True):
    latitude: "capo_device_farm.types.double.Double"
    """<p>The latitude.</p>"""
    longitude: "capo_device_farm.types.double.Double"
    """<p>The longitude.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Location) -> dict:
    out: dict = {}
    out["latitude"] = (
        "NaN"
        if value["latitude"] != value["latitude"]
        else "Infinity"
        if value["latitude"] == float("inf")
        else "-Infinity"
        if value["latitude"] == float("-inf")
        else value["latitude"]
    )
    out["longitude"] = (
        "NaN"
        if value["longitude"] != value["longitude"]
        else "Infinity"
        if value["longitude"] == float("inf")
        else "-Infinity"
        if value["longitude"] == float("-inf")
        else value["longitude"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> Location:
    out: Location = {}  # type: ignore[typeddict-item]
    if data.get("latitude") is not None:
        out["latitude"] = float(data["latitude"])
    else:
        out["latitude"] = 0.0
    if data.get("longitude") is not None:
        out["longitude"] = float(data["longitude"])
    else:
        out["longitude"] = 0.0
    return out
