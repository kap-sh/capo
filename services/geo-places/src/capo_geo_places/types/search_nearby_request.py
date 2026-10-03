"""Generated from Smithy shape ``com.amazonaws.geoplaces#SearchNearbyRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_geo_places.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_places.types.api_key
    import capo_geo_places.types.country_code
    import capo_geo_places.types.distance_meters
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.position
    import capo_geo_places.types.search_nearby_additional_feature_list
    import capo_geo_places.types.search_nearby_filter
    import capo_geo_places.types.search_nearby_intended_use
    import capo_geo_places.types.token


class SearchNearbyRequest(TypedDict, closed=True):
    query_position: "capo_geo_places.types.position.Position"
    """<p>The position in World Geodetic System (WGS 84) format: [longitude, latitude] for which you are querying nearby results for. Results closer to the position will be ranked higher then results further away from the position</p>"""
    query_radius: NotRequired["capo_geo_places.types.distance_meters.DistanceMeters"]
    """<p>The maximum distance in meters from the QueryPosition from which a result will be returned.</p> <note> <p>The fields <code>QueryText</code>, and <code>QueryID</code> are mutually exclusive.</p> </note>"""
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 20</p>"""
    filter: NotRequired["capo_geo_places.types.search_nearby_filter.SearchNearbyFilter"]
    """<p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>"""
    additional_features: NotRequired[
        "capo_geo_places.types.search_nearby_additional_feature_list.SearchNearbyAdditionalFeatureList"
    ]
    """<p>A list of optional additional parameters, such as time zone, that can be requested for each result.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p>A list of <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""
    political_view: NotRequired["capo_geo_places.types.country_code.CountryCode"]
    """<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>"""
    intended_use: NotRequired[
        "capo_geo_places.types.search_nearby_intended_use.SearchNearbyIntendedUse"
    ]
    """<p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <note> <p>When storing <code>SearchNearby</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href="https://aws.amazon.com/location/sla/">user agreement</a> and <a href="https://aws.amazon.com/location/pricing/">service pricing structure</a> to determine the correct setting for your use case.</p> </note>"""
    next_token: NotRequired["capo_geo_places.types.token.Token"]
    """<p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. </p>"""
    key: NotRequired["capo_geo_places.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SearchNearbyRequest) -> dict:
    out: dict = {}
    import capo_geo_places.types.position

    out["QueryPosition"] = capo_geo_places.types.position.serialize_json(
        value["query_position"]
    )
    if "query_radius" in value:
        out["QueryRadius"] = value["query_radius"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "filter" in value:
        import capo_geo_places.types.search_nearby_filter

        out["Filter"] = capo_geo_places.types.search_nearby_filter.serialize_json(
            value["filter"]
        )
    if "additional_features" in value:
        import capo_geo_places.types.search_nearby_additional_feature_list

        out["AdditionalFeatures"] = (
            capo_geo_places.types.search_nearby_additional_feature_list.serialize_json(
                value["additional_features"]
            )
        )
    if "language" in value:
        out["Language"] = value["language"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "intended_use" in value:
        import capo_geo_places.types.search_nearby_intended_use

        out["IntendedUse"] = (
            capo_geo_places.types.search_nearby_intended_use.serialize_json(
                value["intended_use"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> SearchNearbyRequest:
    out: SearchNearbyRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryPosition") is not None:
        import capo_geo_places.types.position

        out["query_position"] = capo_geo_places.types.position.deserialize_json(
            data["QueryPosition"]
        )
    else:
        raise DeserializationError("SearchNearbyRequest.query_position required")
    if data.get("QueryRadius") is not None:
        out["query_radius"] = data["QueryRadius"]
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("Filter") is not None:
        import capo_geo_places.types.search_nearby_filter

        out["filter"] = capo_geo_places.types.search_nearby_filter.deserialize_json(
            data["Filter"]
        )
    if data.get("AdditionalFeatures") is not None:
        import capo_geo_places.types.search_nearby_additional_feature_list

        out["additional_features"] = (
            capo_geo_places.types.search_nearby_additional_feature_list.deserialize_json(
                data["AdditionalFeatures"]
            )
        )
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("IntendedUse") is not None:
        import capo_geo_places.types.search_nearby_intended_use

        out["intended_use"] = (
            capo_geo_places.types.search_nearby_intended_use.deserialize_json(
                data["IntendedUse"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
