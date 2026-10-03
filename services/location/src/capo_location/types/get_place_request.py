"""Generated from Smithy shape ``com.amazonaws.location#GetPlaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.language_tag
    import capo_location.types.place_id
    import capo_location.types.resource_name


class GetPlaceRequest(TypedDict, closed=True):
    index_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource that you want to use for the search.</p>"""
    place_id: "capo_location.types.place_id.PlaceId"
    """<p>The identifier of the place to find.</p>"""
    language: NotRequired["capo_location.types.language_tag.LanguageTag"]
    """<p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPlaceRequest:
    out: GetPlaceRequest = {}  # type: ignore[typeddict-item]
    return out
