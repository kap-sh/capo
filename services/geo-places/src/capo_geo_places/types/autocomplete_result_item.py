"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteResultItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.address
    import capo_geo_places.types.autocomplete_highlights
    import capo_geo_places.types.country_code3
    import capo_geo_places.types.distance_meters
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.place_type
    import capo_geo_places.types.sensitive_boolean
    import capo_geo_places.types.sensitive_string


class AutocompleteResultItem(TypedDict, closed=True):
    place_id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The PlaceId of the place associated with this result. This can be used to look up additional details about the result via GetPlace.</p>"""
    place_type: "capo_geo_places.types.place_type.PlaceType"
    """<p>PlaceType describes the type of result entry returned.</p>"""
    title: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>A formatted string for display when presenting this result to an end user.</p>"""
    address: NotRequired["capo_geo_places.types.address.Address"]
    """<p>The address associated with this result.</p>"""
    distance: "capo_geo_places.types.distance_meters.DistanceMeters"
    """<p>The distance in meters between the center of the search area and this result. Useful to evaluate how far away from the original bias position the result is.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p>A list of <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""
    political_view: NotRequired["capo_geo_places.types.country_code3.CountryCode3"]
    """<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>"""
    highlights: NotRequired[
        "capo_geo_places.types.autocomplete_highlights.AutocompleteHighlights"
    ]
    """<p>Indicates the starting and ending index of the place in the text query that match the found title. </p>"""
    estimated_point_address: NotRequired[
        "capo_geo_places.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>If <code>true</code>, indicates that the coordinates of the position and access points of the point address are estimated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteResultItem) -> dict:
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
    out["Distance"] = value.get("distance", 0)
    if "language" in value:
        out["Language"] = value["language"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "highlights" in value:
        import capo_geo_places.types.autocomplete_highlights

        out["Highlights"] = (
            capo_geo_places.types.autocomplete_highlights.serialize_json(
                value["highlights"]
            )
        )
    if "estimated_point_address" in value:
        out["EstimatedPointAddress"] = value["estimated_point_address"]
    return out


def deserialize_json(data: dict) -> AutocompleteResultItem:
    out: AutocompleteResultItem = {}  # type: ignore[typeddict-item]
    if data.get("PlaceId") is not None:
        out["place_id"] = data["PlaceId"]
    else:
        raise DeserializationError("AutocompleteResultItem.place_id required")
    if data.get("PlaceType") is not None:
        import capo_geo_places.types.place_type

        out["place_type"] = capo_geo_places.types.place_type.deserialize_json(
            data["PlaceType"]
        )
    else:
        raise DeserializationError("AutocompleteResultItem.place_type required")
    if data.get("Title") is not None:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("AutocompleteResultItem.title required")
    if data.get("Address") is not None:
        import capo_geo_places.types.address

        out["address"] = capo_geo_places.types.address.deserialize_json(data["Address"])
    if data.get("Distance") is not None:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("Highlights") is not None:
        import capo_geo_places.types.autocomplete_highlights

        out["highlights"] = (
            capo_geo_places.types.autocomplete_highlights.deserialize_json(
                data["Highlights"]
            )
        )
    if data.get("EstimatedPointAddress") is not None:
        out["estimated_point_address"] = data["EstimatedPointAddress"]
    return out
