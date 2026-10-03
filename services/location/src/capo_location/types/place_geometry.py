"""Generated from Smithy shape ``com.amazonaws.location#PlaceGeometry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.position


class PlaceGeometry(TypedDict, closed=True):
    point: NotRequired["capo_location.types.position.Position"]
    """<p>A single point geometry specifies a location for a Place using <a href="https://gisgeography.com/wgs84-world-geodetic-system/">WGS 84</a> coordinates:</p> <ul> <li> <p> <i>x</i> — Specifies the x coordinate or longitude. </p> </li> <li> <p> <i>y</i> — Specifies the y coordinate or latitude. </p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: PlaceGeometry) -> dict:
    out: dict = {}
    if "point" in value:
        import capo_location.types.position

        out["Point"] = capo_location.types.position.serialize_json(value["point"])
    return out


def deserialize_json(data: dict) -> PlaceGeometry:
    out: PlaceGeometry = {}  # type: ignore[typeddict-item]
    if data.get("Point") is not None:
        import capo_location.types.position

        out["point"] = capo_location.types.position.deserialize_json(data["Point"])
    return out
