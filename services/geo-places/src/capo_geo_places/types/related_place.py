"""Generated from Smithy shape ``com.amazonaws.geoplaces#RelatedPlace``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.access_point_list
    import capo_geo_places.types.address
    import capo_geo_places.types.place_type
    import capo_geo_places.types.position
    import capo_geo_places.types.sensitive_string


class RelatedPlace(TypedDict, closed=True):
    place_id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place result.</p>"""
    place_type: "capo_geo_places.types.place_type.PlaceType"
    """<p>A <code>PlaceType</code> is a category that the result place must belong to.</p>"""
    title: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The localized display name of this result item based on request parameter <code>language</code>.</p>"""
    address: NotRequired["capo_geo_places.types.address.Address"]
    position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""
    access_points: NotRequired[
        "capo_geo_places.types.access_point_list.AccessPointList"
    ]
    """<p>Position of the access point in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RelatedPlace) -> dict:
    out: dict = {}
    out["PlaceId"] = value["place_id"]
    import capo_geo_places.types.place_type

    out["PlaceType"] = capo_geo_places.types.place_type.serialize_json(
        value["place_type"]
    )
    out["Title"] = value["title"]
    if "address" in value:
        import capo_geo_places.types.address

        out["Address"] = capo_geo_places.types.address.serialize_json(value["address"])
    if "position" in value:
        import capo_geo_places.types.position

        out["Position"] = capo_geo_places.types.position.serialize_json(
            value["position"]
        )
    if "access_points" in value:
        import capo_geo_places.types.access_point_list

        out["AccessPoints"] = capo_geo_places.types.access_point_list.serialize_json(
            value["access_points"]
        )
    return out


def deserialize_json(data: dict) -> RelatedPlace:
    out: RelatedPlace = {}  # type: ignore[typeddict-item]
    if data.get("PlaceId") is not None:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("RelatedPlace.place_id required")
    if data.get("PlaceType") is not None:
        import capo_geo_places.types.place_type

        out["place_type"] = capo_geo_places.types.place_type.deserialize_json(
            data["PlaceType"]
        )
    else:
        raise DeserializationError("RelatedPlace.place_type required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("RelatedPlace.title required")
    if data.get("Address") is not None:
        import capo_geo_places.types.address

        out["address"] = capo_geo_places.types.address.deserialize_json(data["Address"])
    if data.get("Position") is not None:
        import capo_geo_places.types.position

        out["position"] = capo_geo_places.types.position.deserialize_json(
            data["Position"]
        )
    if data.get("AccessPoints") is not None:
        import capo_geo_places.types.access_point_list

        out["access_points"] = capo_geo_places.types.access_point_list.deserialize_json(
            data["AccessPoints"]
        )
    return out


def redact_sensitive(value: RelatedPlace) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place_id" in value:
        out["place_id"] = "*** Sensitive Data Redacted ***"
    if "place_type" in value:
        out["place_type"] = "*** Sensitive Data Redacted ***"
    if "title" in value:
        out["title"] = "*** Sensitive Data Redacted ***"
    if "address" in value:
        import capo_geo_places.types.address

        out["address"] = capo_geo_places.types.address.redact_sensitive(
            value["address"]
        )
    if "position" in value:
        out["position"] = "*** Sensitive Data Redacted ***"
    if "access_points" in value:
        import capo_geo_places.types.access_point_list

        out["access_points"] = capo_geo_places.types.access_point_list.redact_sensitive(
            value["access_points"]
        )
    return out
