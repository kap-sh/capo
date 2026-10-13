"""Generated from Smithy shape ``com.amazonaws.georoutes#Isoline``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.distance_meters
    import capo_geo_routes.types.duration_seconds
    import capo_geo_routes.types.isoline_connection_list
    import capo_geo_routes.types.isoline_shape_geometry_list


class Isoline(TypedDict, closed=True):
    connections: "capo_geo_routes.types.isoline_connection_list.IsolineConnectionList"
    """<p>Lines connecting separate parts of the reachable area that can be reached within the same threshold. These occur when areas are reachable but not contiguous, such as when separated by water or unroutable areas. When present, these lines represent actual transportation network segments (such as ferry routes or bridges) that connect the separated areas.</p>"""
    distance_threshold: "capo_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The travel distance in meters used to calculate this isoline, if distance-based thresholds were specified in the request.</p>"""
    geometries: (
        "capo_geo_routes.types.isoline_shape_geometry_list.IsolineShapeGeometryList"
    )
    """<p>The shapes that define the reachable area, provided in the requested geometry format.</p>"""
    time_threshold: "capo_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>The travel time in seconds used to calculate this isoline, if time-based thresholds were specified in the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Isoline) -> dict:
    out: dict = {}
    import capo_geo_routes.types.isoline_connection_list

    out["Connections"] = capo_geo_routes.types.isoline_connection_list.serialize_json(
        value["connections"]
    )
    out["DistanceThreshold"] = value.get("distance_threshold", 0)
    import capo_geo_routes.types.isoline_shape_geometry_list

    out["Geometries"] = (
        capo_geo_routes.types.isoline_shape_geometry_list.serialize_json(
            value["geometries"]
        )
    )
    out["TimeThreshold"] = value.get("time_threshold", 0)
    return out


def deserialize_json(data: dict) -> Isoline:
    out: Isoline = {}  # type: ignore[typeddict-item]
    if data.get("Connections") is not None:
        import capo_geo_routes.types.isoline_connection_list

        out["connections"] = (
            capo_geo_routes.types.isoline_connection_list.deserialize_json(
                data["Connections"]
            )
        )
    else:
        raise DeserializationError("Isoline.connections required")
    if data.get("DistanceThreshold") is not None:
        out["distance_threshold"] = data["DistanceThreshold"]
    else:
        out["distance_threshold"] = 0
    if data.get("Geometries") is not None:
        import capo_geo_routes.types.isoline_shape_geometry_list

        out["geometries"] = (
            capo_geo_routes.types.isoline_shape_geometry_list.deserialize_json(
                data["Geometries"]
            )
        )
    else:
        raise DeserializationError("Isoline.geometries required")
    if data.get("TimeThreshold") is not None:
        out["time_threshold"] = data["TimeThreshold"]
    else:
        out["time_threshold"] = 0
    return out


def redact_sensitive(value: Isoline) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "connections" in value:
        import capo_geo_routes.types.isoline_connection_list

        out["connections"] = (
            capo_geo_routes.types.isoline_connection_list.redact_sensitive(
                value["connections"]
            )
        )
    if "distance_threshold" in value:
        out["distance_threshold"] = "*** Sensitive Data Redacted ***"
    if "geometries" in value:
        import capo_geo_routes.types.isoline_shape_geometry_list

        out["geometries"] = (
            capo_geo_routes.types.isoline_shape_geometry_list.redact_sensitive(
                value["geometries"]
            )
        )
    if "time_threshold" in value:
        out["time_threshold"] = "*** Sensitive Data Redacted ***"
    return out
