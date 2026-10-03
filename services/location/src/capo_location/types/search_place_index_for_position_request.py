"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForPositionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.language_tag
    import capo_location.types.place_index_search_result_limit
    import capo_location.types.position
    import capo_location.types.resource_name


class SearchPlaceIndexForPositionRequest(TypedDict, closed=True):
    index_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource you want to use for the search.</p>"""
    position: "capo_location.types.position.Position"
    """<p>Specifies the longitude and latitude of the position to query.</p> <p> This parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents a position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p>"""
    max_results: NotRequired[
        "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
    ]
    """<p>An optional parameter. The maximum number of results returned per request.</p> <p>Default value: <code>50</code> </p>"""
    language: NotRequired["capo_location.types.language_tag.LanguageTag"]
    """<p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForPositionRequest) -> dict:
    out: dict = {}
    import capo_location.types.position

    out["Position"] = capo_location.types.position.serialize_json(value["position"])
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "language" in value:
        out["Language"] = value["language"]
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForPositionRequest:
    out: SearchPlaceIndexForPositionRequest = {}  # type: ignore[typeddict-item]
    if data.get("Position") is not None:
        import capo_location.types.position

        out["position"] = capo_location.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError(
            "SearchPlaceIndexForPositionRequest.position required"
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    return out
