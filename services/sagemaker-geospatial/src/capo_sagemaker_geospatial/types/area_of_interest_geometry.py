"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#AreaOfInterestGeometry``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_sagemaker_geospatial.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.multi_polygon_geometry_input
    import capo_sagemaker_geospatial.types.polygon_geometry_input


class _AreaOfInterestGeometry_PolygonGeometry(TypedDict, closed=True):
    PolygonGeometry: (
        "capo_sagemaker_geospatial.types.polygon_geometry_input.PolygonGeometryInput"
    )


class _AreaOfInterestGeometry_MultiPolygonGeometry(TypedDict, closed=True):
    MultiPolygonGeometry: "capo_sagemaker_geospatial.types.multi_polygon_geometry_input.MultiPolygonGeometryInput"


AreaOfInterestGeometry: TypeAlias = (
    _AreaOfInterestGeometry_PolygonGeometry
    | _AreaOfInterestGeometry_MultiPolygonGeometry
)


# --- restJson1 ser/de ---
def serialize_json(value: AreaOfInterestGeometry) -> dict:
    if "PolygonGeometry" in value:
        import capo_sagemaker_geospatial.types.polygon_geometry_input

        return {
            "PolygonGeometry": capo_sagemaker_geospatial.types.polygon_geometry_input.serialize_json(
                value["PolygonGeometry"]
            )
        }
    elif "MultiPolygonGeometry" in value:
        import capo_sagemaker_geospatial.types.multi_polygon_geometry_input

        return {
            "MultiPolygonGeometry": capo_sagemaker_geospatial.types.multi_polygon_geometry_input.serialize_json(
                value["MultiPolygonGeometry"]
            )
        }
    else:
        raise SerializationError("AreaOfInterestGeometry: no variant present")


def deserialize_json(data: dict) -> AreaOfInterestGeometry:
    if data.get("PolygonGeometry") is not None:
        import capo_sagemaker_geospatial.types.polygon_geometry_input

        return {
            "PolygonGeometry": capo_sagemaker_geospatial.types.polygon_geometry_input.deserialize_json(
                data["PolygonGeometry"]
            )
        }
    elif data.get("MultiPolygonGeometry") is not None:
        import capo_sagemaker_geospatial.types.multi_polygon_geometry_input

        return {
            "MultiPolygonGeometry": capo_sagemaker_geospatial.types.multi_polygon_geometry_input.deserialize_json(
                data["MultiPolygonGeometry"]
            )
        }
    else:
        raise DeserializationError("AreaOfInterestGeometry: no recognized variant key")


def redact_sensitive(value: AreaOfInterestGeometry) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "PolygonGeometry" in value:
        import capo_sagemaker_geospatial.types.polygon_geometry_input

        out["PolygonGeometry"] = (
            capo_sagemaker_geospatial.types.polygon_geometry_input.redact_sensitive(
                value["PolygonGeometry"]
            )
        )
    if "MultiPolygonGeometry" in value:
        import capo_sagemaker_geospatial.types.multi_polygon_geometry_input

        out["MultiPolygonGeometry"] = (
            capo_sagemaker_geospatial.types.multi_polygon_geometry_input.redact_sensitive(
                value["MultiPolygonGeometry"]
            )
        )
    return out
