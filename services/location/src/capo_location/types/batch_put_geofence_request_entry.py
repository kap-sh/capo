"""Generated from Smithy shape ``com.amazonaws.location#BatchPutGeofenceRequestEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geofence_geometry
    import capo_location.types.id
    import capo_location.types.property_map


class BatchPutGeofenceRequestEntry(TypedDict, closed=True):
    geofence_id: "capo_location.types.id.Id"
    """<p>The identifier for the geofence to be stored in a given geofence collection.</p>"""
    geometry: "capo_location.types.geofence_geometry.GeofenceGeometry"
    """<p>Contains the details to specify the position of the geofence. Can be a circle, a polygon, or a multipolygon. <code>Polygon</code> and <code>MultiPolygon</code> geometries can be defined using their respective parameters, or encoded in Geobuf format using the <code>Geobuf</code> parameter. Including multiple geometry types in the same request will return a validation error.</p> <note> <p>The geofence <code>Polygon</code> and <code>MultiPolygon</code> formats support a maximum of 1,000 total vertices. The <code>Geobuf</code> format supports a maximum of 100,000 vertices.</p> </note>"""
    geofence_properties: NotRequired["capo_location.types.property_map.PropertyMap"]
    """<p>Associates one of more properties with the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.</p> <p>Format: <code>"key" : "value"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutGeofenceRequestEntry) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import capo_location.types.geofence_geometry

    out["Geometry"] = capo_location.types.geofence_geometry.serialize_json(
        value["geometry"]
    )
    if "geofence_properties" in value:
        import capo_location.types.property_map

        out["GeofenceProperties"] = capo_location.types.property_map.serialize_json(
            value["geofence_properties"]
        )
    return out


def deserialize_json(data: dict) -> BatchPutGeofenceRequestEntry:
    out: BatchPutGeofenceRequestEntry = {}  # type: ignore[typeddict-item]
    if data.get("GeofenceId") is not None:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("BatchPutGeofenceRequestEntry.geofence_id required")
    if data.get("Geometry") is not None:
        import capo_location.types.geofence_geometry

        out["geometry"] = capo_location.types.geofence_geometry.deserialize_json(
            data["Geometry"]
        )
    else:
        raise DeserializationError("BatchPutGeofenceRequestEntry.geometry required")
    if data.get("GeofenceProperties") is not None:
        import capo_location.types.property_map

        out["geofence_properties"] = capo_location.types.property_map.deserialize_json(
            data["GeofenceProperties"]
        )
    return out
