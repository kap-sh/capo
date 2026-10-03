"""Generated from Smithy shape ``com.amazonaws.geoplaces#GetPlaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_geo_places.types.api_key
    import capo_geo_places.types.country_code
    import capo_geo_places.types.get_place_additional_feature_list
    import capo_geo_places.types.get_place_address_names_mode
    import capo_geo_places.types.get_place_intended_use
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.sensitive_string


class GetPlaceRequest(TypedDict, closed=True):
    place_id: "capo_geo_places.types.sensitive_string.SensitiveString"
    """<p>The <code>PlaceId</code> of the place you wish to receive the information for.</p>"""
    additional_features: NotRequired[
        "capo_geo_places.types.get_place_additional_feature_list.GetPlaceAdditionalFeatureList"
    ]
    """<p> A list of optional additional parameters such as time zone that can be requested for each result. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>TimeZone</code> value. </p>"""
    language: NotRequired["capo_geo_places.types.language_tag.LanguageTag"]
    """<p> A list of <a href="https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. For <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the following codes: <code>en, id, km, lo, ms, my, pt, th, tl, vi, zh</code> </p>"""
    political_view: NotRequired["capo_geo_places.types.country_code.CountryCode"]
    """<p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p>"""
    intended_use: NotRequired[
        "capo_geo_places.types.get_place_intended_use.GetPlaceIntendedUse"
    ]
    """<p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href="https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html">GrabMaps</a> customers. </p> <note> <p>When storing <code>GetPlace</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href="https://aws.amazon.com/location/sla/">user agreement</a> and <a href="https://aws.amazon.com/location/pricing/">service pricing structure</a> to determine the correct setting for your use case.</p> </note>"""
    key: NotRequired["capo_geo_places.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>"""
    address_names_mode: NotRequired[
        "capo_geo_places.types.get_place_address_names_mode.GetPlaceAddressNamesMode"
    ]
    """<p>Specifies how address names are returned. When set to <code>Administrative</code>, the service returns the official administrative names for address components. <code>Administrative</code> currently applies only to addresses in the United States.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPlaceRequest:
    out: GetPlaceRequest = {}  # type: ignore[typeddict-item]
    return out
