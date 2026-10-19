"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#PolygonGeometryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.linear_rings


class PolygonGeometryInput(TypedDict, closed=True):
    coordinates: "capo_sagemaker_geospatial.types.linear_rings.LinearRings"
    """<p>Coordinates representing a Polygon based on the <a href="https://www.rfc-editor.org/rfc/rfc7946#section-3.1.6">GeoJson spec</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PolygonGeometryInput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types.linear_rings

    out["Coordinates"] = capo_sagemaker_geospatial.types.linear_rings.serialize_json(
        value["coordinates"]
    )
    return out


def deserialize_json(data: dict) -> PolygonGeometryInput:
    out: PolygonGeometryInput = {}  # type: ignore[typeddict-item]
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


def redact_sensitive(value: PolygonGeometryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "coordinates" in value:
        import capo_sagemaker_geospatial.types.linear_rings

        out["coordinates"] = (
            capo_sagemaker_geospatial.types.linear_rings.redact_sensitive(
                value["coordinates"]
            )
        )
    return out
