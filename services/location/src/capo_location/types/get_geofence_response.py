"""Generated from Smithy shape ``com.amazonaws.location#GetGeofenceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.geofence_geometry
    import capo_location.types.id
    import capo_location.types.property_map
    import capo_location.types.timestamp


class GetGeofenceResponse(TypedDict, closed=True):
    geofence_id: "capo_location.types.id.Id"
    """<p>The geofence identifier.</p>"""
    geometry: "capo_location.types.geofence_geometry.GeofenceGeometry"
    """<p>Contains the geofence geometry details describing the position of the geofence. Can be a circle, a polygon, or a multipolygon.</p>"""
    status: "str"
    """<p>Identifies the state of the geofence. A geofence will hold one of the following states:</p> <ul> <li> <p> <code>ACTIVE</code> — The geofence has been indexed by the system. </p> </li> <li> <p> <code>PENDING</code> — The geofence is being processed by the system.</p> </li> <li> <p> <code>FAILED</code> — The geofence failed to be indexed by the system.</p> </li> <li> <p> <code>DELETED</code> — The geofence has been deleted from the system index.</p> </li> <li> <p> <code>DELETING</code> — The geofence is being deleted from the system index.</p> </li> </ul>"""
    create_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence collection was created in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    update_time: "capo_location.types.timestamp.Timestamp"
    """<p>The timestamp for when the geofence collection was last updated in <a href="https://www.iso.org/iso-8601-date-and-time-format.html">ISO 8601</a> format: <code>YYYY-MM-DDThh:mm:ss.sssZ</code> </p>"""
    geofence_properties: NotRequired["capo_location.types.property_map.PropertyMap"]
    """<p>User defined properties of the geofence. A property is a key-value pair stored with the geofence and added to any geofence event triggered with that geofence.</p> <p>Format: <code>"key" : "value"</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGeofenceResponse) -> dict:
    out: dict = {}
    out["GeofenceId"] = value["geofence_id"]
    import capo_location.types.geofence_geometry

    out["Geometry"] = capo_location.types.geofence_geometry.serialize_json(
        value["geometry"]
    )
    out["Status"] = value["status"]
    import capo_location.types.timestamp

    out["CreateTime"] = capo_location.types.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_location.types.timestamp

    out["UpdateTime"] = capo_location.types.timestamp.serialize_json(
        value["update_time"]
    )
    if "geofence_properties" in value:
        import capo_location.types.property_map

        out["GeofenceProperties"] = capo_location.types.property_map.serialize_json(
            value["geofence_properties"]
        )
    return out


def deserialize_json(data: dict) -> GetGeofenceResponse:
    out: GetGeofenceResponse = {}  # type: ignore[typeddict-item]
    if data.get("GeofenceId") is not None:
        out["geofence_id"] = data["GeofenceId"]
    else:
        raise DeserializationError("GetGeofenceResponse.geofence_id required")
    if data.get("Geometry") is not None:
        import capo_location.types.geofence_geometry

        out["geometry"] = capo_location.types.geofence_geometry.deserialize_json(
            data["Geometry"]
        )
    else:
        raise DeserializationError("GetGeofenceResponse.geometry required")
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        raise DeserializationError("GetGeofenceResponse.status required")
    if data.get("CreateTime") is not None:
        import capo_location.types.timestamp

        out["create_time"] = capo_location.types.timestamp.deserialize_json(
            data["CreateTime"]
        )
    else:
        raise DeserializationError("GetGeofenceResponse.create_time required")
    if data.get("UpdateTime") is not None:
        import capo_location.types.timestamp

        out["update_time"] = capo_location.types.timestamp.deserialize_json(
            data["UpdateTime"]
        )
    else:
        raise DeserializationError("GetGeofenceResponse.update_time required")
    if data.get("GeofenceProperties") is not None:
        import capo_location.types.property_map

        out["geofence_properties"] = capo_location.types.property_map.deserialize_json(
            data["GeofenceProperties"]
        )
    return out
