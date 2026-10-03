"""Generated from Smithy shape ``com.amazonaws.geoplaces#GeocodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.address_translation_component_list
    import capo_geo_places.types.api_key
    import capo_geo_places.types.country_code
    import capo_geo_places.types.geocode_additional_feature_list
    import capo_geo_places.types.geocode_address_names_mode
    import capo_geo_places.types.geocode_filter
    import capo_geo_places.types.geocode_intended_use
    import capo_geo_places.types.geocode_query_components
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.position
    import capo_geo_places.types.postal_code_mode
    import capo_geo_places.types.sensitive_string


class GeocodeRequest(TypedDict, closed=True):
    query_text: NotRequired["capo_geo_places.types.sensitive_string.SensitiveString"]
    """<p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p>"""
    query_components: NotRequired[
        "capo_geo_places.types.geocode_query_components.GeocodeQueryComponents"
    ]
    max_results: NotRequired["int"]
    """<p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 20</p>"""
    bias_position: NotRequired["capo_geo_places.types.position.Position"]
    """<p>The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p>"""
    filter: NotRequired["capo_geo_places.types.geocode_filter.GeocodeFilter"]
    """<p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>"""
    additional_features: NotRequired[
        "capo_geo_places.types.geocode_additional_feature_list.GeocodeAdditionalFeatureList"
    ]
    """<p>A list of optional additional parameters, such as time zone, that can be requested for each result.</p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p>A list of <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>"""
    political_view: NotRequired["capo_geo_places.types.country_code.CountryCode"]
    """<p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>"""
    intended_use: NotRequired[
        "capo_geo_places.types.geocode_intended_use.GeocodeIntendedUse"
    ]
    """<p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <note> <p>When storing <code>Geocode</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href="https://aws.amazon.com/location/sla/">user agreement</a> and <a href="https://aws.amazon.com/location/pricing/">service pricing structure</a> to determine the correct setting for your use case.</p> </note>"""
    key: NotRequired["capo_geo_places.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>"""
    postal_code_mode: NotRequired[
        "capo_geo_places.types.postal_code_mode.PostalCodeMode"
    ]
    """<p>The <code>PostalCodeMode</code> affects how postal code results are returned. If a postal code spans multiple localities and this value is empty, partial district or locality information may be returned under a single postal code result entry. If it's populated with the value <code>EnumerateSpannedLocalities</code>, all cities in that postal code are returned. If it's populated with the value <code>EnumerateSpannedDistricts</code>, all combinations of the postal code with the corresponding district and city names are returned.</p>"""
    address_translations: NotRequired[
        "capo_geo_places.types.address_translation_component_list.AddressTranslationComponentList"
    ]
    """<p>Specifies which address components to include translations for. Translations include all name variants and alternative names for the requested fields in all available languages. Valid values are <code>District</code>, <code>Locality</code>, <code>Region</code>, and <code>SubRegion</code>.</p>"""
    address_names_mode: NotRequired[
        "capo_geo_places.types.geocode_address_names_mode.GeocodeAddressNamesMode"
    ]
    """<p>Specifies how address names are returned. If not set, the service returns normalized (official) names by default. When set to <code>Matched</code>, address names in the response are based on the input query rather than official names. When set to <code>Administrative</code>, the service returns the official administrative names for address components. <code>Administrative</code> currently applies only to addresses in the United States.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeocodeRequest) -> dict:
    out: dict = {}
    if "query_text" in value:
        out["QueryText"] = value["query_text"]
    if "query_components" in value:
        import capo_geo_places.types.geocode_query_components

        out["QueryComponents"] = (
            capo_geo_places.types.geocode_query_components.serialize_json(
                value["query_components"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "bias_position" in value:
        import capo_geo_places.types.position

        out["BiasPosition"] = capo_geo_places.types.position.serialize_json(
            value["bias_position"]
        )
    if "filter" in value:
        import capo_geo_places.types.geocode_filter

        out["Filter"] = capo_geo_places.types.geocode_filter.serialize_json(
            value["filter"]
        )
    if "additional_features" in value:
        import capo_geo_places.types.geocode_additional_feature_list

        out["AdditionalFeatures"] = (
            capo_geo_places.types.geocode_additional_feature_list.serialize_json(
                value["additional_features"]
            )
        )
    if "language" in value:
        out["Language"] = value["language"]
    if "political_view" in value:
        out["PoliticalView"] = value["political_view"]
    if "intended_use" in value:
        import capo_geo_places.types.geocode_intended_use

        out["IntendedUse"] = capo_geo_places.types.geocode_intended_use.serialize_json(
            value["intended_use"]
        )
    if "postal_code_mode" in value:
        import capo_geo_places.types.postal_code_mode

        out["PostalCodeMode"] = capo_geo_places.types.postal_code_mode.serialize_json(
            value["postal_code_mode"]
        )
    if "address_translations" in value:
        import capo_geo_places.types.address_translation_component_list

        out["AddressTranslations"] = (
            capo_geo_places.types.address_translation_component_list.serialize_json(
                value["address_translations"]
            )
        )
    if "address_names_mode" in value:
        import capo_geo_places.types.geocode_address_names_mode

        out["AddressNamesMode"] = (
            capo_geo_places.types.geocode_address_names_mode.serialize_json(
                value["address_names_mode"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeocodeRequest:
    out: GeocodeRequest = {}  # type: ignore[typeddict-item]
    if data.get("QueryText") is not None:
        out["query_text"] = data["QueryText"]
    if data.get("QueryComponents") is not None:
        import capo_geo_places.types.geocode_query_components

        out["query_components"] = (
            capo_geo_places.types.geocode_query_components.deserialize_json(
                data["QueryComponents"]
            )
        )
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("BiasPosition") is not None:
        import capo_geo_places.types.position

        out["bias_position"] = capo_geo_places.types.position.deserialize_json(
            data["BiasPosition"]
        )
    if data.get("Filter") is not None:
        import capo_geo_places.types.geocode_filter

        out["filter"] = capo_geo_places.types.geocode_filter.deserialize_json(
            data["Filter"]
        )
    if data.get("AdditionalFeatures") is not None:
        import capo_geo_places.types.geocode_additional_feature_list

        out["additional_features"] = (
            capo_geo_places.types.geocode_additional_feature_list.deserialize_json(
                data["AdditionalFeatures"]
            )
        )
    if data.get("Language") is not None:
        out["language"] = data["Language"]
    if data.get("PoliticalView") is not None:
        out["political_view"] = data["PoliticalView"]
    if data.get("IntendedUse") is not None:
        import capo_geo_places.types.geocode_intended_use

        out["intended_use"] = (
            capo_geo_places.types.geocode_intended_use.deserialize_json(
                data["IntendedUse"]
            )
        )
    if data.get("PostalCodeMode") is not None:
        import capo_geo_places.types.postal_code_mode

        out["postal_code_mode"] = (
            capo_geo_places.types.postal_code_mode.deserialize_json(
                data["PostalCodeMode"]
            )
        )
    if data.get("AddressTranslations") is not None:
        import capo_geo_places.types.address_translation_component_list

        out["address_translations"] = (
            capo_geo_places.types.address_translation_component_list.deserialize_json(
                data["AddressTranslations"]
            )
        )
    if data.get("AddressNamesMode") is not None:
        import capo_geo_places.types.geocode_address_names_mode

        out["address_names_mode"] = (
            capo_geo_places.types.geocode_address_names_mode.deserialize_json(
                data["AddressNamesMode"]
            )
        )
    return out
