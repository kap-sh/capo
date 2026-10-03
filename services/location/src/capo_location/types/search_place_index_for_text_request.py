"""Generated from Smithy shape ``com.amazonaws.location#SearchPlaceIndexForTextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.bounding_box
    import capo_location.types.country_code_list
    import capo_location.types.filter_place_category_list
    import capo_location.types.language_tag
    import capo_location.types.place_index_search_result_limit
    import capo_location.types.position
    import capo_location.types.resource_name
    import capo_location.types.sensitive_string


class SearchPlaceIndexForTextRequest(TypedDict, closed=True):
    index_name: "capo_location.types.resource_name.ResourceName"
    """<p>The name of the place index resource you want to use for the search.</p>"""
    text: "capo_location.types.sensitive_string.SensitiveString"
    """<p>The address, name, city, or region to be used in the search in free-form text format. For example, <code>123 Any Street</code>.</p>"""
    bias_position: NotRequired["capo_location.types.position.Position"]
    """<p>An optional parameter that indicates a preference for places that are closer to a specified position.</p> <p> If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p> <note> <p> <code>BiasPosition</code> and <code>FilterBBox</code> are mutually exclusive. Specifying both options results in an error. </p> </note>"""
    filter_b_box: NotRequired["capo_location.types.bounding_box.BoundingBox"]
    """<p>An optional parameter that limits the search results by returning only places that are within the provided bounding box.</p> <p> If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.</p> <p>For example, <code>[-12.7935, -37.4835, -12.0684, -36.9542]</code> represents a bounding box where the southwest corner has longitude <code>-12.7935</code> and latitude <code>-37.4835</code>, and the northeast corner has longitude <code>-12.0684</code> and latitude <code>-36.9542</code>.</p> <note> <p> <code>FilterBBox</code> and <code>BiasPosition</code> are mutually exclusive. Specifying both options results in an error. </p> </note>"""
    filter_countries: NotRequired[
        "capo_location.types.country_code_list.CountryCodeList"
    ]
    """<p>An optional parameter that limits the search results by returning only places that are in a specified list of countries.</p> <ul> <li> <p>Valid values include <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country codes. For example, Australia uses three upper-case characters: <code>AUS</code>.</p> </li> </ul>"""
    max_results: NotRequired[
        "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
    ]
    """<p>An optional parameter. The maximum number of results returned per request. </p> <p>The default: <code>50</code> </p>"""
    language: NotRequired["capo_location.types.language_tag.LanguageTag"]
    """<p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for <code>Athens, Greece</code>, with the <code>language</code> parameter set to <code>en</code>. The result found will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the result found will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>"""
    filter_categories: NotRequired[
        "capo_location.types.filter_place_category_list.FilterPlaceCategoryList"
    ]
    """<p>A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match <i>any</i> of the categories listed.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>"""
    key: NotRequired["capo_location.types.api_key.ApiKey"]
    """<p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchPlaceIndexForTextRequest) -> dict:
    out: dict = {}
    out["Text"] = value["text"]
    if "bias_position" in value:
        import capo_location.types.position

        out["BiasPosition"] = capo_location.types.position.serialize_json(
            value["bias_position"]
        )
    if "filter_b_box" in value:
        import capo_location.types.bounding_box

        out["FilterBBox"] = capo_location.types.bounding_box.serialize_json(
            value["filter_b_box"]
        )
    if "filter_countries" in value:
        import capo_location.types.country_code_list

        out["FilterCountries"] = capo_location.types.country_code_list.serialize_json(
            value["filter_countries"]
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "language" in value:
        out["Language"] = value["language"]
    if "filter_categories" in value:
        import capo_location.types.filter_place_category_list

        out["FilterCategories"] = (
            capo_location.types.filter_place_category_list.serialize_json(
                value["filter_categories"]
            )
        )
    return out


def deserialize_json(data: dict) -> SearchPlaceIndexForTextRequest:
    out: SearchPlaceIndexForTextRequest = {}  # type: ignore[typeddict-item]
    if data.get("Text") is not None:
        out["text"] = data["Text"]
    else:
        raise DeserializationError("SearchPlaceIndexForTextRequest.text required")
    if data.get("BiasPosition") is not None:
        import capo_location.types.position

        out["bias_position"] = capo_location.types.position.deserialize_json(
            data["BiasPosition"]
        )
    if data.get("FilterBBox") is not None:
        import capo_location.types.bounding_box

        out["filter_b_box"] = capo_location.types.bounding_box.deserialize_json(
            data["FilterBBox"]
        )
    if data.get("FilterCountries") is not None:
        import capo_location.types.country_code_list

        out["filter_countries"] = (
            capo_location.types.country_code_list.deserialize_json(
                data["FilterCountries"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("FilterCategories") is not None:
        import capo_location.types.filter_place_category_list

        out["filter_categories"] = (
            capo_location.types.filter_place_category_list.deserialize_json(
                data["FilterCategories"]
            )
        )
    return out
