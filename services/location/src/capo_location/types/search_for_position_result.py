"""Generated from Smithy shape ``com.amazonaws.location#SearchForPositionResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.place
    import capo_location.types.place_id
    import capo_location.types.sensitive_double


class SearchForPositionResult(TypedDict, closed=True):
    place: "capo_location.types.place.Place"
    """<p>Details about the search result, such as its address and position.</p>"""
    distance: "capo_location.types.sensitive_double.SensitiveDouble"
    """<p>The distance in meters of a great-circle arc between the query position and the result.</p> <note> <p>A great-circle arc is the shortest path on a sphere, in this case the Earth. This returns the shortest distance between two locations.</p> </note>"""
    place_id: NotRequired["capo_location.types.place_id.PlaceId"]
    """<p>The unique identifier of the place. You can use this with the <code>GetPlace</code> operation to find the place again later.</p> <note> <p>For <code>SearchPlaceIndexForPosition</code> operations, the <code>PlaceId</code> is returned only by place indexes that use HERE or Grab as a data provider.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchForPositionResult) -> dict:
    out: dict = {}
    import capo_location.types.place

    out["Place"] = capo_location.types.place.serialize_json(value["place"])
    out["Distance"] = (
        "NaN"
        if value["distance"] != value["distance"]
        else "Infinity"
        if value["distance"] == float("inf")
        else "-Infinity"
        if value["distance"] == float("-inf")
        else value["distance"]
    )
    if "place_id" in value:
        out["PlaceId"] = value["place_id"]
    return out


def deserialize_json(data: dict) -> SearchForPositionResult:
    out: SearchForPositionResult = {}  # type: ignore[typeddict-item]
    if data.get("Place") is not None:
        import capo_location.types.place

        out["place"] = capo_location.types.place.deserialize_json(data["Place"])
    else:
        raise DeserializationError("SearchForPositionResult.place required")
    if data.get("Distance") is not None:
        out["distance"] = float(data["Distance"])
    else:
        raise DeserializationError("SearchForPositionResult.distance required")
    if data.get("PlaceId") is not None:
        out["place_id"] = data["PlaceId"]
    return out


def redact_sensitive(value: SearchForPositionResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place" in value:
        import capo_location.types.place

        out["place"] = capo_location.types.place.redact_sensitive(value["place"])
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "place_id" in value:
        out["place_id"] = "*** Sensitive Data Redacted ***"
    return out
