"""Generated from Smithy shape ``com.amazonaws.geoplaces#AutocompleteRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.api_key
    import capo_geo_places.types.autocomplete_additional_feature_list
    import capo_geo_places.types.autocomplete_filter
    import capo_geo_places.types.autocomplete_intended_use
    import capo_geo_places.types.country_code
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.position
    import capo_geo_places.types.postal_code_mode
    import capo_geo_places.types.sensitive_string


class AutocompleteRequest(TypedDict, closed=True):
    query_text: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p> <note> <p>The fields <code>QueryText</code>, and <code>QueryID</code> are mutually exclusive.</p> </note>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 5</p>"""
    bias_position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position in longitude and latitude that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p> <note> <p>The fields <code>BiasPosition</code>, <code>FilterBoundingBox</code>, and <code>FilterCircle</code> are mutually exclusive.</p> </note>"""
    filter: NotRequired["capo_geo_places.types.autocomplete_filter.AutocompleteFilter"]
    """<p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>"""
    postal_code_mode: NotRequired[
        "capo_geo_places.types.postal_code_mode.PostalCodeMode"
    ]
    """<p>The <code>PostalCodeMode</code> affects how postal code results are returned. If a postal code spans multiple localities and this value is empty, partial district or locality information may be returned under a single postal code result entry. If it's populated with the value <code>EnumerateSpannedLocalities</code>, all cities in that postal code are returned. If it's populated with the value <code>EnumerateSpannedDistricts</code>, all combinations of the postal code with the corresponding district and city names are returned.</p>"""
    additional_features: NotRequired[
        "capo_geo_places.types.autocomplete_additional_feature_list.AutocompleteAdditionalFeatureList"
    ]
    """<p>A list of optional additional parameters that can be requested for each result.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p>A list of <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""
    political_view: NotRequired["capo_geo_places.types.country_code.CountryCode"]
    """<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p> <p>The following political views are currently supported:</p> <ul> <li> <p> <code>ARG</code>: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands</p> </li> <li> <p> <code>EGY</code>: Egypt's view on Bir Tawil</p> </li> <li> <p> <code>IND</code>: India's view on Gilgit-Baltistan</p> </li> <li> <p> <code>KEN</code>: Kenya's view on the Ilemi Triangle</p> </li> <li> <p> <code>MAR</code>: Morocco's view on Western Sahara</p> </li> <li> <p> <code>RUS</code>: Russia's view on Crimea</p> </li> <li> <p> <code>SDN</code>: Sudan's view on the Halaib Triangle</p> </li> <li> <p> <code>SRB</code>: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands</p> </li> <li> <p> <code>SUR</code>: Suriname's view on the Courantyne Headwaters and Lawa Headwaters</p> </li> <li> <p> <code>SYR</code>: Syria's view on the Golan Heights</p> </li> <li> <p> <code>TUR</code>: Turkey's view on Cyprus and Northern Cyprus</p> </li> <li> <p> <code>TZA</code>: Tanzania's view on Lake Malawi</p> </li> <li> <p> <code>URY</code>: Uruguay's view on Rincon de Artigas</p> </li> <li> <p> <code>VNM</code>: Vietnam's view on the Paracel Islands and Spratly Islands</p> </li> </ul>"""
    intended_use: NotRequired[
        "capo_geo_places.types.autocomplete_intended_use.AutocompleteIntendedUse"
    ]
    """<p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Currently, <code>Autocomplete</code> does not support storage of results. </p>"""
    key: NotRequired["capo_geo_places.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutocompleteRequest) -> dict:
    out: dict = {}
    out["QueryText"] = value["query_text"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "bias_position" in value:
        import capo_geo_places.types.position

        out["BiasPosition"] = capo_geo_places.types.position.serialize_json(
            value["bias_position"]
        )
    if "filter" in value:
        import capo_geo_places.types.autocomplete_filter

        out["Filter"] = capo_geo_places.types.autocomplete_filter.serialize_json(
            value["filter"]
        )
    if "postal_code_mode" in value:
        import capo_geo_places.types.postal_code_mode

        out["PostalCodeMode"] = capo_geo_places.types.postal_code_mode.serialize_json(
            value["postal_code_mode"]
        )
    if "additional_features" in value:
        import capo_geo_places.types.autocomplete_additional_feature_list

        out["AdditionalFeatures"] = (
            capo_geo_places.types.autocomplete_additional_feature_list.serialize_json(
                value["additional_features"]
            )
        )
    if "language" in value:
        out["Language"] = value["language"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "intended_use" in value:
        import capo_geo_places.types.autocomplete_intended_use

        out["IntendedUse"] = (
            capo_geo_places.types.autocomplete_intended_use.serialize_json(
                value["intended_use"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutocompleteRequest:
    out: AutocompleteRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryText") is not None:
        out["query_text"] = data["QueryText"]
    else:
        raise DeserializationError("AutocompleteRequest.query_text required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("BiasPosition") is not None:
        import capo_geo_places.types.position

        out["bias_position"] = capo_geo_places.types.position.deserialize_json(
            data["BiasPosition"]
        )
    if data.get("Filter") is not None:
        import capo_geo_places.types.autocomplete_filter

        out["filter"] = capo_geo_places.types.autocomplete_filter.deserialize_json(
            data["Filter"]
        )
    if data.get("PostalCodeMode") is not None:
        import capo_geo_places.types.postal_code_mode

        out["postal_code_mode"] = (
            capo_geo_places.types.postal_code_mode.deserialize_json(
                data["PostalCodeMode"]
            )
        )
    if data.get("AdditionalFeatures") is not None:
        import capo_geo_places.types.autocomplete_additional_feature_list

        out["additional_features"] = (
            capo_geo_places.types.autocomplete_additional_feature_list.deserialize_json(
                data["AdditionalFeatures"]
            )
        )
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("IntendedUse") is not None:
        import capo_geo_places.types.autocomplete_intended_use

        out["intended_use"] = (
            capo_geo_places.types.autocomplete_intended_use.deserialize_json(
                data["IntendedUse"]
            )
        )
    return out
