"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#MultiPolygonGeometryInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.linear_rings_list


class MultiPolygonGeometryInput(TypedDict, closed=True):
    coordinates: "capo_sagemaker_geospatial.types.linear_rings_list.LinearRingsList"
    """<p>The coordinates of the multipolygon geometry.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MultiPolygonGeometryInput) -> dict:
    out: dict = {}
    import capo_sagemaker_geospatial.types.linear_rings_list

    out["Coordinates"] = (
        capo_sagemaker_geospatial.types.linear_rings_list.serialize_json(
            value["coordinates"]
        )
    )
    return out


def deserialize_json(data: dict) -> MultiPolygonGeometryInput:
    out: MultiPolygonGeometryInput = {}  # type: ignore[typeddict-item]
    if data.get("Coordinates") is not None:
        import capo_sagemaker_geospatial.types.linear_rings_list

        out["coordinates"] = (
            capo_sagemaker_geospatial.types.linear_rings_list.deserialize_json(
                data["Coordinates"]
            )
        )
    else:
        raise DeserializationError("MultiPolygonGeometryInput.coordinates required")
    return out


def redact_sensitive(value: MultiPolygonGeometryInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "coordinates" in value:
        import capo_sagemaker_geospatial.types.linear_rings_list

        out["coordinates"] = (
            capo_sagemaker_geospatial.types.linear_rings_list.redact_sensitive(
                value["coordinates"]
            )
        )
    return out
