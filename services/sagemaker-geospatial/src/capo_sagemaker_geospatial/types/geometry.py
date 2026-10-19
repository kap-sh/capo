"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#Geometry``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.linear_rings


class Geometry(TypedDict, closed=True):
    type: "str"
    """<p>GeoJson Geometry types like Polygon and MultiPolygon.</p>"""
    coordinates: "capo_sagemaker_geospatial.types.linear_rings.LinearRings"
    """<p>The coordinates of the GeoJson Geometry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Geometry) -> dict:
    out: dict = {}
    out["Type"] = value["type"]
    import capo_sagemaker_geospatial.types.linear_rings

    out["Coordinates"] = capo_sagemaker_geospatial.types.linear_rings.serialize_json(
        value["coordinates"]
    )
    return out


def deserialize_json(data: dict) -> Geometry:
    out: Geometry = {}  # type: ignore[typeddict-item]
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("Coordinates") is not None:
        import capo_sagemaker_geospatial.types.linear_rings

        out["coordinates"] = (
            capo_sagemaker_geospatial.types.linear_rings.deserialize_json(
                data["Coordinates"]
            )
        )
    else:
        out["coordinates"] = []
    return out


def redact_sensitive(value: Geometry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "coordinates" in value:
        import capo_sagemaker_geospatial.types.linear_rings

        out["coordinates"] = (
            capo_sagemaker_geospatial.types.linear_rings.redact_sensitive(
                value["coordinates"]
            )
        )
    return out
