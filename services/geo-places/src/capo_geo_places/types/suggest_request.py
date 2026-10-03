"""Generated from Smithy shape ``com.amazonaws.geoplaces#SuggestRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.api_key
    import capo_geo_places.types.country_code
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.position
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.suggest_additional_feature_list
    import capo_geo_places.types.suggest_filter
    import capo_geo_places.types.suggest_intended_use
    import capo_geo_places.types.suggest_travel_mode


class SuggestRequest(TypedDict, closed=True):
    query_text: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p> <note> <p>The fields <code>QueryText</code> and <code>QueryID</code> are mutually exclusive.</p> </note>"""
    max_results: NotRequired["int"]
    """<p> An optional limit for the number of results returned in a single call. </p> <p>Default value: 20</p>"""
    max_query_refinements: NotRequired["int"]
    """<p> Maximum number of query terms to be returned for use with a search text query. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    bias_position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p> <note> <p>The fields <code>BiasPosition</code>, <code>FilterBoundingBox</code>, and <code>FilterCircle</code> are mutually exclusive.</p> </note>"""
    filter: NotRequired["capo_geo_places.types.suggest_filter.SuggestFilter"]
    """<p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>"""
    additional_features: NotRequired[
        "capo_geo_places.types.suggest_additional_feature_list.SuggestAdditionalFeatureList"
    ]
    """<p> A list of optional additional parameters, such as time zone, that can be requested for each result. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>Core</code> and <code>TimeZone</code> values. </p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p> A list of <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the following codes: <code>en, id, km, lo, ms, my, pt, th, tl, vi, zh</code> </p>"""
    political_view: NotRequired["capo_geo_places.types.country_code.CountryCode"]
    """<p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    intended_use: NotRequired[
        "capo_geo_places.types.suggest_intended_use.SuggestIntendedUse"
    ]
    """<p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Currently, <code>Suggest</code> does not support storage of results. </p>"""
    travel_mode: NotRequired[
        "capo_geo_places.types.suggest_travel_mode.SuggestTravelMode"
    ]
    """<p>Indicates the mode of mobility used by the end user. This is used to improve the relevance of search results. Valid values are <code>Car</code>, <code>Scooter</code>, and <code>Truck</code>.</p>"""
    key: NotRequired["capo_geo_places.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SuggestRequest) -> dict:
    out: dict = {}
    out["QueryText"] = value["query_text"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "max_query_refinements" in value:
        out["MaxQueryRefinements"] = value["max_query_refinements"]
    if "bias_position" in value:
        import capo_geo_places.types.position

        out["BiasPosition"] = capo_geo_places.types.position.serialize_json(
            value["bias_position"]
        )
    if "filter" in value:
        import capo_geo_places.types.suggest_filter

        out["Filter"] = capo_geo_places.types.suggest_filter.serialize_json(
            value["filter"]
        )
    if "additional_features" in value:
        import capo_geo_places.types.suggest_additional_feature_list

        out["AdditionalFeatures"] = (
            capo_geo_places.types.suggest_additional_feature_list.serialize_json(
                value["additional_features"]
            )
        )
    if "language" in value:
        out["Language"] = value["language"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "intended_use" in value:
        import capo_geo_places.types.suggest_intended_use

        out["IntendedUse"] = capo_geo_places.types.suggest_intended_use.serialize_json(
            value["intended_use"]
        )
    if "travel_mode" in value:
        import capo_geo_places.types.suggest_travel_mode

        out["TravelMode"] = capo_geo_places.types.suggest_travel_mode.serialize_json(
            value["travel_mode"]
        )
    return out


def deserialize_json(data: dict) -> SuggestRequest:
    out: SuggestRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryText") is not None:
        out["query_text"] = data["QueryText"]
    else:
        raise DeserializationError("SuggestRequest.query_text required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("MaxQueryRefinements") is not None:
        out["max_query_refinements"] = data["MaxQueryRefinements"]
    if data.get("BiasPosition") is not None:
        import capo_geo_places.types.position

        out["bias_position"] = capo_geo_places.types.position.deserialize_json(
            data["BiasPosition"]
        )
    if data.get("Filter") is not None:
        import capo_geo_places.types.suggest_filter

        out["filter"] = capo_geo_places.types.suggest_filter.deserialize_json(
            data["Filter"]
        )
    if data.get("AdditionalFeatures") is not None:
        import capo_geo_places.types.suggest_additional_feature_list

        out["additional_features"] = (
            capo_geo_places.types.suggest_additional_feature_list.deserialize_json(
                data["AdditionalFeatures"]
            )
        )
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("IntendedUse") is not None:
        import capo_geo_places.types.suggest_intended_use

        out["intended_use"] = (
            capo_geo_places.types.suggest_intended_use.deserialize_json(
                data["IntendedUse"]
            )
        )
    if data.get("TravelMode") is not None:
        import capo_geo_places.types.suggest_travel_mode

        out["travel_mode"] = capo_geo_places.types.suggest_travel_mode.deserialize_json(
            data["TravelMode"]
        )
    return out
