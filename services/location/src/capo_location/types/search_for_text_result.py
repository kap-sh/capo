"""Generated from Smithy shape ``com.amazonaws.location#SearchForTextResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.place
    import capo_location.types.place_id
    import capo_location.types.sensitive_double


class SearchForTextResult(TypedDict, closed=True):
    place: "capo_location.types.place.Place"
    """<p>Details about the search result, such as its address and position.</p>"""
    distance: NotRequired["capo_location.types.sensitive_double.SensitiveDouble"]
    """<p>The distance in meters of a great-circle arc between the bias position specified and the result. <code>Distance</code> will be returned only if a bias position was specified in the query.</p> <note> <p>A great-circle arc is the shortest path on a sphere, in this case the Earth. This returns the shortest distance between two locations.</p> </note>"""
    relevance: NotRequired["capo_location.types.sensitive_double.SensitiveDouble"]
    """<p>The relative confidence in the match for a result among the results returned. For example, if more fields for an address match (including house number, street, city, country/region, and postal code), the relevance score is closer to 1.</p> <p>Returned only when the partner selected is Esri or Grab.</p>"""
    place_id: NotRequired["capo_location.types.place_id.PlaceId"]
    """<p>The unique identifier of the place. You can use this with the <code>GetPlace</code> operation to find the place again later.</p> <note> <p>For <code>SearchPlaceIndexForText</code> operations, the <code>PlaceId</code> is returned only by place indexes that use HERE or Grab as a data provider.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchForTextResult) -> dict:
    out: dict = {}
    import capo_location.types.place

    out["Place"] = capo_location.types.place.serialize_json(value["place"])
    if "distance" in value:
        out["Distance"] = (
            "NaN"
            if value["distance"] != value["distance"]
            else "Infinity"
            if value["distance"] == float("inf")
            else "-Infinity"
            if value["distance"] == float("-inf")
            else value["distance"]
        )
    if "relevance" in value:
        out["Relevance"] = (
            "NaN"
            if value["relevance"] != value["relevance"]
            else "Infinity"
            if value["relevance"] == float("inf")
            else "-Infinity"
            if value["relevance"] == float("-inf")
            else value["relevance"]
        )
    if "place_id" in value:
        out["PlaceId"] = value["place_id"]
    return out


def deserialize_json(data: dict) -> SearchForTextResult:
    out: SearchForTextResult = {}  # type: ignore[typeddict-item]
    if data.get("Place") is not None:
        import capo_location.types.place

        out["place"] = capo_location.types.place.deserialize_json(data["Place"])
    else:
        raise DeserializationError("SearchForTextResult.place required")
    if data.get("Distance") is not None:
        out["distance"] = float(data["Distance"])
    if data.get("Relevance") is not None:
        out["relevance"] = float(data["Relevance"])
    if data.get("PlaceId") is not None:
        out["place_id"] = data["PlaceId"]
    return out


def redact_sensitive(value: SearchForTextResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place" in value:
        import capo_location.types.place

        out["place"] = capo_location.types.place.redact_sensitive(value["place"])
    if "distance" in value:
        out["distance"] = "*** Sensitive Data Redacted ***"
    if "relevance" in value:
        out["relevance"] = "*** Sensitive Data Redacted ***"
    if "place_id" in value:
        out["place_id"] = "*** Sensitive Data Redacted ***"
    return out
