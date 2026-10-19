"""Generated from Smithy shape ``com.amazonaws.geoplaces#Intersection``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.access_point_list
    import capo_geo_places.types.address
    import capo_geo_places.types.bounding_box
    import capo_geo_places.types.distance_meters
    import capo_geo_places.types.position
    import capo_geo_places.types.sensitive_string


class Intersection(TypedDict, closed=True):
    place_id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place result.</p>"""
    title: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The localized display name of this result item based on request parameter <code>language</code>.</p>"""
    address: NotRequired["capo_geo_places.types.address.Address"]
    position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    distance: NotRequired["capo_geo_places.types.distance_meters.DistanceMeters"]
    """<p>The distance in meters from the QueryPosition.</p>"""
    route_distance: NotRequired["capo_geo_places.types.distance_meters.DistanceMeters"]
    """<p>The distance from the routing position of the nearby address to the street result.</p>"""
    map_view: NotRequired["capo_geo_places.types.bounding_box.BoundingBox"]
    """<p>The bounding box enclosing the geometric shape (area or line) that an individual result covers.</p> <p>The bounding box formed is defined as a set of four coordinates: <code>[{westward lng}, {southern lat}, {eastward lng}, {northern lat}]</code> </p>"""
    access_points: NotRequired[
        "capo_geo_places.types.access_point_list.AccessPointList"
    ]
    """<p>Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Intersection) -> dict:
    out: dict = {}
    out["PlaceId"] = value["place_id"]
    out["Title"] = value["title"]
    if "address" in value:
        import capo_geo_places.types.address

        out["Address"] = capo_geo_places.types.address.serialize_json(value["address"])
    if "position" in value:
        import capo_geo_places.types.position

        out["Position"] = capo_geo_places.types.position.serialize_json(
            value["position"]
        )
    if "distance" in value:
        out["Distance"] = value["distance"]
    if "route_distance" in value:
        out["RouteDistance"] = value["route_distance"]
    if "map_view" in value:
        import capo_geo_places.types.bounding_box

        out["MapView"] = capo_geo_places.types.bounding_box.serialize_json(
            value["map_view"]
        )
    if "access_points" in value:
        import capo_geo_places.types.access_point_list

        out["AccessPoints"] = capo_geo_places.types.access_point_list.serialize_json(
            value["access_points"]
        )
    return out


def deserialize_json(data: dict) -> Intersection:
    out: Intersection = {}  # type: ignore[typeddict-item]
    if data.get("PlaceId") is not None:
        out["place_id"] = data["PlaceId"]
    else:
        out["place_id"] = ""
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        out["title"] = ""
    if data.get("Address") is not None:
        import capo_geo_places.types.address

        out["address"] = capo_geo_places.types.address.deserialize_json(data["Address"])
    if data.get("Position") is not None:
        import capo_geo_places.types.position

        out["position"] = capo_geo_places.types.position.deserialize_json(
            data["Position"]
        )
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    if data.get("RouteDistance") is not None:
        out["route_distance"] = data["RouteDistance"]
    if data.get("MapView") is not None:
        import capo_geo_places.types.bounding_box

        out["map_view"] = capo_geo_places.types.bounding_box.deserialize_json(
            data["MapView"]
        )
    if data.get("AccessPoints") is not None:
        import capo_geo_places.types.access_point_list

        out["access_points"] = capo_geo_places.types.access_point_list.deserialize_json(
            data["AccessPoints"]
        )
    return out


def redact_sensitive(value: Intersection) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place_id" in value:
        out["place_id"] = "*** Sensitive Data Redacted ***"
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "address" in value:
        import capo_geo_places.types.address

        out["address"] = capo_geo_places.types.address.redact_sensitive(
            value["address"]
        )
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "route_distance" in value:
        out["route_distance"] = "*** Sensitive Data Redacted ***"
    if "map_view" in value:
        out["map_view"] = "*** Sensitive Data Redacted ***"
    if "access_points" in value:
        import capo_geo_places.types.access_point_list

        out["access_points"] = capo_geo_places.types.access_point_list.redact_sensitive(
            value["access_points"]
        )
    return out
