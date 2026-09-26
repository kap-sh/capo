"""Generated from Smithy shape ``com.amazonaws.geoplaces#PlacesService``."""

import warnings
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_geo_places._auth._signers
import capo_geo_places._auth._sigv4
from capo_geo_places._auth._identity import Credentials
from capo_geo_places._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_geo_places._auth._zapros_handler import AuthMiddleware
from capo_geo_places._resources.places_service.provider_resource import ProviderResource
from capo_geo_places._services._aws_config import aws_config
from capo_geo_places._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_geo_places.types.api_key
    import capo_geo_places.types.autocomplete_additional_feature_list
    import capo_geo_places.types.autocomplete_filter
    import capo_geo_places.types.autocomplete_intended_use
    import capo_geo_places.types.autocomplete_request
    import capo_geo_places.types.autocomplete_response
    import capo_geo_places.types.country_code
    import capo_geo_places.types.distance_meters
    import capo_geo_places.types.geocode_additional_feature_list
    import capo_geo_places.types.geocode_filter
    import capo_geo_places.types.geocode_intended_use
    import capo_geo_places.types.geocode_query_components
    import capo_geo_places.types.geocode_request
    import capo_geo_places.types.geocode_response
    import capo_geo_places.types.get_place_additional_feature_list
    import capo_geo_places.types.get_place_intended_use
    import capo_geo_places.types.get_place_request
    import capo_geo_places.types.get_place_response
    import capo_geo_places.types.heading
    import capo_geo_places.types.language_tag
    import capo_geo_places.types.position
    import capo_geo_places.types.postal_code_mode
    import capo_geo_places.types.reverse_geocode_additional_feature_list
    import capo_geo_places.types.reverse_geocode_filter
    import capo_geo_places.types.reverse_geocode_intended_use
    import capo_geo_places.types.reverse_geocode_request
    import capo_geo_places.types.reverse_geocode_response
    import capo_geo_places.types.search_nearby_additional_feature_list
    import capo_geo_places.types.search_nearby_filter
    import capo_geo_places.types.search_nearby_intended_use
    import capo_geo_places.types.search_nearby_request
    import capo_geo_places.types.search_nearby_response
    import capo_geo_places.types.search_text_additional_feature_list
    import capo_geo_places.types.search_text_filter
    import capo_geo_places.types.search_text_intended_use
    import capo_geo_places.types.search_text_request
    import capo_geo_places.types.search_text_response
    import capo_geo_places.types.sensitive_string
    import capo_geo_places.types.suggest_additional_feature_list
    import capo_geo_places.types.suggest_filter
    import capo_geo_places.types.suggest_intended_use
    import capo_geo_places.types.suggest_request
    import capo_geo_places.types.suggest_response
    import capo_geo_places.types.token


class GeoPlacesClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class GeoPlacesClient:
    """A client for the ``GeoPlaces`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
            lambda next: AuthMiddleware(next)
        )
        if credentials is not None and credentials_provider is not None:
            warnings.warn(
                "Both credentials and credentials_provider given; provider takes precedence"
            )
        resolved_credentials_provider: IdentityProvider[Credentials] | None = (
            credentials_provider
        )
        if resolved_credentials_provider is None and credentials is not None:
            resolved_credentials_provider = StaticAwsCredentialsProvider(credentials)
        if resolved_credentials_provider is None and credentials is None:
            resolved_credentials_provider = default_aws_credentials_chain(
                Client(http_handler)
            )
        self._config = GeoPlacesClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.provider_resource = ProviderResource(self)

    def operation_options(
        self, config_overrides: Optional[GeoPlacesClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: GeoPlacesClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def autocomplete(
        self,
        query_text: "capo_geo_places.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[GeoPlacesClientConfig] = None,
        max_results: Optional[int] = None,
        bias_position: Optional["capo_geo_places.types.position.Position"] = None,
        filter: Optional[
            "capo_geo_places.types.autocomplete_filter.AutocompleteFilter"
        ] = None,
        postal_code_mode: Optional[
            "capo_geo_places.types.postal_code_mode.PostalCodeMode"
        ] = None,
        additional_features: Optional[
            "capo_geo_places.types.autocomplete_additional_feature_list.AutocompleteAdditionalFeatureList"
        ] = None,
        language: Optional["capo_geo_places.types.language_tag.LanguageTag"] = None,
        political_view: Optional[
            "capo_geo_places.types.country_code.CountryCode"
        ] = None,
        intended_use: Optional[
            "capo_geo_places.types.autocomplete_intended_use.AutocompleteIntendedUse"
        ] = None,
        key: Optional["capo_geo_places.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_places.types.autocomplete_response.AutocompleteResponse":
        r"""<p> <code>Autocomplete</code> completes potential places and addresses as the user types, based on the partial input. The API enhances the efficiency and accuracy of address by completing query based on a few entered keystrokes. It helps you by completing partial queries with valid address completion. Also, the API supports the filtering of results based on geographic location, country, or specific place types, and can be tailored using optional parameters like language and political views.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/autocomplete.html\">Autocomplete</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            query_text: <p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p> <note> <p>The fields <code>QueryText</code>, and <code>QueryID</code> are mutually exclusive.</p> </note>
            max_results: <p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 5</p>
            bias_position: <p>The position in longitude and latitude that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p> <note> <p>The fields <code>BiasPosition</code>, <code>FilterBoundingBox</code>, and <code>FilterCircle</code> are mutually exclusive.</p> </note>
            filter: <p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>
            postal_code_mode: <p>The <code>PostalCodeMode</code> affects how postal code results are returned. If a postal code spans multiple localities and this value is empty, partial district or locality information may be returned under a single postal code result entry. If it's populated with the value <code>EnumerateSpannedLocalities</code>, all cities in that postal code are returned.</p>
            additional_features: <p>A list of optional additional parameters that can be requested for each result.</p>
            language: <p>A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>
            political_view: <p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p> <p>The following political views are currently supported:</p> <ul> <li> <p> <code>ARG</code>: Argentina's view on the Southern Patagonian Ice Field and Tierra Del Fuego, including the Falkland Islands, South Georgia, and South Sandwich Islands</p> </li> <li> <p> <code>EGY</code>: Egypt's view on Bir Tawil</p> </li> <li> <p> <code>IND</code>: India's view on Gilgit-Baltistan</p> </li> <li> <p> <code>KEN</code>: Kenya's view on the Ilemi Triangle</p> </li> <li> <p> <code>MAR</code>: Morocco's view on Western Sahara</p> </li> <li> <p> <code>RUS</code>: Russia's view on Crimea</p> </li> <li> <p> <code>SDN</code>: Sudan's view on the Halaib Triangle</p> </li> <li> <p> <code>SRB</code>: Serbia's view on Kosovo, Vukovar, and Sarengrad Islands</p> </li> <li> <p> <code>SUR</code>: Suriname's view on the Courantyne Headwaters and Lawa Headwaters</p> </li> <li> <p> <code>SYR</code>: Syria's view on the Golan Heights</p> </li> <li> <p> <code>TUR</code>: Turkey's view on Cyprus and Northern Cyprus</p> </li> <li> <p> <code>TZA</code>: Tanzania's view on Lake Malawi</p> </li> <li> <p> <code>URY</code>: Uruguay's view on Rincon de Artigas</p> </li> <li> <p> <code>VNM</code>: Vietnam's view on the Paracel Islands and Spratly Islands</p> </li> </ul>
            intended_use: <p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Currently, <code>Autocomplete</code> does not support storage of results. </p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>

        Raises:
            capo_geo_places.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_places.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_places.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_places.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_places.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_places.types.autocomplete_request.AutocompleteRequest]",
        ) -> OperationResponse[
            "capo_geo_places.types.autocomplete_response.AutocompleteResponse"
        ]:
            import capo_geo_places._operations.places_service.autocomplete

            output, http_response = (
                capo_geo_places._operations.places_service.autocomplete.autocomplete(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_places.types.autocomplete_request.AutocompleteRequest = {
            "query_text": query_text
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter is not None:
            input_["filter"] = filter
        if postal_code_mode is not None:
            input_["postal_code_mode"] = postal_code_mode
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if language is not None:
            input_["language"] = language
        if political_view is not None:
            input_["political_view"] = political_view
        if intended_use is not None:
            input_["intended_use"] = intended_use
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def geocode(
        self,
        *,
        config_overrides: Optional[GeoPlacesClientConfig] = None,
        query_text: Optional[
            "capo_geo_places.types.sensitive_string.SensitiveString"
        ] = None,
        query_components: Optional[
            "capo_geo_places.types.geocode_query_components.GeocodeQueryComponents"
        ] = None,
        max_results: Optional[int] = None,
        bias_position: Optional["capo_geo_places.types.position.Position"] = None,
        filter: Optional["capo_geo_places.types.geocode_filter.GeocodeFilter"] = None,
        additional_features: Optional[
            "capo_geo_places.types.geocode_additional_feature_list.GeocodeAdditionalFeatureList"
        ] = None,
        language: Optional["capo_geo_places.types.language_tag.LanguageTag"] = None,
        political_view: Optional[
            "capo_geo_places.types.country_code.CountryCode"
        ] = None,
        intended_use: Optional[
            "capo_geo_places.types.geocode_intended_use.GeocodeIntendedUse"
        ] = None,
        key: Optional["capo_geo_places.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_places.types.geocode_response.GeocodeResponse":
        r"""<p> <code>Geocode</code> converts a textual address or place into geographic coordinates. You can obtain geographic coordinates, address component, and other related information. It supports flexible queries, including free-form text or structured queries with components like street names, postal codes, and regions. The Geocode API can also provide additional features such as time zone information and the inclusion of political views.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/geocode.html\">Geocode</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            query_text: <p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p>
            max_results: <p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 20</p>
            bias_position: <p>The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p>
            filter: <p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>
            additional_features: <p>A list of optional additional parameters, such as time zone, that can be requested for each result.</p>
            language: <p>A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>
            political_view: <p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>
            intended_use: <p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>When storing <code>Geocode</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href=\"https://aws.amazon.com/location/sla/\">user agreement</a> and <a href=\"https://aws.amazon.com/location/pricing/\">service pricing structure</a> to determine the correct setting for your use case.</p> </note>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>

        Raises:
            capo_geo_places.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_places.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_places.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_places.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_places.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_places.types.geocode_request.GeocodeRequest]",
        ) -> OperationResponse[
            "capo_geo_places.types.geocode_response.GeocodeResponse"
        ]:
            import capo_geo_places._operations.places_service.geocode

            output, http_response = (
                capo_geo_places._operations.places_service.geocode.geocode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_places.types.geocode_request.GeocodeRequest = {}
        if query_text is not None:
            input_["query_text"] = query_text
        if query_components is not None:
            input_["query_components"] = query_components
        if max_results is not None:
            input_["max_results"] = max_results
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter is not None:
            input_["filter"] = filter
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if language is not None:
            input_["language"] = language
        if political_view is not None:
            input_["political_view"] = political_view
        if intended_use is not None:
            input_["intended_use"] = intended_use
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_place(
        self,
        place_id: "capo_geo_places.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[GeoPlacesClientConfig] = None,
        additional_features: Optional[
            "capo_geo_places.types.get_place_additional_feature_list.GetPlaceAdditionalFeatureList"
        ] = None,
        language: Optional["capo_geo_places.types.language_tag.LanguageTag"] = None,
        political_view: Optional[
            "capo_geo_places.types.country_code.CountryCode"
        ] = None,
        intended_use: Optional[
            "capo_geo_places.types.get_place_intended_use.GetPlaceIntendedUse"
        ] = None,
        key: Optional["capo_geo_places.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_places.types.get_place_response.GetPlaceResponse":
        r"""<p> <code>GetPlace</code> finds a place by its unique ID. A <code>PlaceId</code> is returned by other place operations.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/get-place.html\">GetPlace</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            place_id: <p>The <code>PlaceId</code> of the place you wish to receive the information for.</p>
            additional_features: <p> A list of optional additional parameters such as time zone that can be requested for each result. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>TimeZone</code> value. </p>
            language: <p> A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the following codes: <code>en, id, km, lo, ms, my, pt, th, tl, vi, zh</code> </p>
            political_view: <p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            intended_use: <p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>When storing <code>GetPlace</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href=\"https://aws.amazon.com/location/sla/\">user agreement</a> and <a href=\"https://aws.amazon.com/location/pricing/\">service pricing structure</a> to determine the correct setting for your use case.</p> </note>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>

        Raises:
            capo_geo_places.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_places.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_places.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_places.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_places.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_places.types.get_place_request.GetPlaceRequest]",
        ) -> OperationResponse[
            "capo_geo_places.types.get_place_response.GetPlaceResponse"
        ]:
            import capo_geo_places._operations.places_service.get_place

            output, http_response = (
                capo_geo_places._operations.places_service.get_place.get_place(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_places.types.get_place_request.GetPlaceRequest = {
            "place_id": place_id
        }
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if language is not None:
            input_["language"] = language
        if political_view is not None:
            input_["political_view"] = political_view
        if intended_use is not None:
            input_["intended_use"] = intended_use
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def reverse_geocode(
        self,
        query_position: "capo_geo_places.types.position.Position",
        *,
        config_overrides: Optional[GeoPlacesClientConfig] = None,
        query_radius: Optional[
            "capo_geo_places.types.distance_meters.DistanceMeters"
        ] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_geo_places.types.reverse_geocode_filter.ReverseGeocodeFilter"
        ] = None,
        additional_features: Optional[
            "capo_geo_places.types.reverse_geocode_additional_feature_list.ReverseGeocodeAdditionalFeatureList"
        ] = None,
        language: Optional["capo_geo_places.types.language_tag.LanguageTag"] = None,
        political_view: Optional[
            "capo_geo_places.types.country_code.CountryCode"
        ] = None,
        intended_use: Optional[
            "capo_geo_places.types.reverse_geocode_intended_use.ReverseGeocodeIntendedUse"
        ] = None,
        key: Optional["capo_geo_places.types.api_key.ApiKey"] = None,
        heading: Optional["capo_geo_places.types.heading.Heading"] = None,
    ) -> "capo_geo_places.types.reverse_geocode_response.ReverseGeocodeResponse":
        r"""<p> <code>ReverseGeocode</code> converts geographic coordinates into a human-readable address or place. You can obtain address component, and other related information such as place type, category, street information. The Reverse Geocode API supports filtering to on place type so that you can refine result based on your need. Also, The Reverse Geocode API can also provide additional features such as time zone information and the inclusion of political views.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/reverse-geocode.html\">Reverse Geocode</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            query_position: <p>The position in World Geodetic System (WGS 84) format: [longitude, latitude] for which you are querying nearby results for. Results closer to the position will be ranked higher then results further away from the position</p>
            query_radius: <p> The maximum distance in meters from the QueryPosition from which a result will be returned. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only up to a maximum value of 100,000. </p>
            max_results: <p> An optional limit for the number of results returned in a single call.</p> <p>Default value: 1</p>
            filter: <p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>
            additional_features: <p> A list of optional additional parameters, such as time zone that can be requested for each result. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>TimeZone</code> value. </p>
            language: <p> A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the following codes: <code>en, id, km, lo, ms, my, pt, th, tl, vi, zh</code> </p>
            political_view: <p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            intended_use: <p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). </p> <note> <p>When storing <code>ReverseGeocode</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href=\"https://aws.amazon.com/location/sla/\">user agreement</a> and <a href=\"https://aws.amazon.com/location/pricing/\">service pricing structure</a> to determine the correct setting for your use case.</p> </note>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>
            heading: <p>The heading in degrees from true north in a navigation context. The heading is measured as the angle clockwise from the North direction.</p> <p>Example: North is <code>0</code> degrees, East is <code>90</code> degrees, South is <code>180</code> degrees, and West is <code>270</code> degrees.</p>

        Raises:
            capo_geo_places.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_places.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_places.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_places.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_places.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_places.types.reverse_geocode_request.ReverseGeocodeRequest]",
        ) -> OperationResponse[
            "capo_geo_places.types.reverse_geocode_response.ReverseGeocodeResponse"
        ]:
            import capo_geo_places._operations.places_service.reverse_geocode

            output, http_response = (
                capo_geo_places._operations.places_service.reverse_geocode.reverse_geocode(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_places.types.reverse_geocode_request.ReverseGeocodeRequest = {
            "query_position": query_position
        }
        if query_radius is not None:
            input_["query_radius"] = query_radius
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if language is not None:
            input_["language"] = language
        if political_view is not None:
            input_["political_view"] = political_view
        if intended_use is not None:
            input_["intended_use"] = intended_use
        if key is not None:
            input_["key"] = key
        if heading is not None:
            input_["heading"] = heading

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_nearby(
        self,
        query_position: "capo_geo_places.types.position.Position",
        *,
        config_overrides: Optional[GeoPlacesClientConfig] = None,
        query_radius: Optional[
            "capo_geo_places.types.distance_meters.DistanceMeters"
        ] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_geo_places.types.search_nearby_filter.SearchNearbyFilter"
        ] = None,
        additional_features: Optional[
            "capo_geo_places.types.search_nearby_additional_feature_list.SearchNearbyAdditionalFeatureList"
        ] = None,
        language: Optional["capo_geo_places.types.language_tag.LanguageTag"] = None,
        political_view: Optional[
            "capo_geo_places.types.country_code.CountryCode"
        ] = None,
        intended_use: Optional[
            "capo_geo_places.types.search_nearby_intended_use.SearchNearbyIntendedUse"
        ] = None,
        next_token: Optional["capo_geo_places.types.token.Token"] = None,
        key: Optional["capo_geo_places.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_places.types.search_nearby_response.SearchNearbyResponse":
        r"""<p> <code>SearchNearby</code> queries for points of interest within a radius from a central coordinates, returning place results with optional filters such as categories, business chains, food types and more. The API returns details such as a place name, address, phone, category, food type, contact, opening hours. Also, the API can return phonemes, time zones and more based on requested parameters.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/search-nearby.html\">Search Nearby</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            query_position: <p>The position in World Geodetic System (WGS 84) format: [longitude, latitude] for which you are querying nearby results for. Results closer to the position will be ranked higher then results further away from the position</p>
            query_radius: <p>The maximum distance in meters from the QueryPosition from which a result will be returned.</p> <note> <p>The fields <code>QueryText</code>, and <code>QueryID</code> are mutually exclusive.</p> </note>
            max_results: <p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 20</p>
            filter: <p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>
            additional_features: <p>A list of optional additional parameters, such as time zone, that can be requested for each result.</p>
            language: <p>A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry.</p>
            political_view: <p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country.</p>
            intended_use: <p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p> <note> <p>When storing <code>SearchNearby</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href=\"https://aws.amazon.com/location/sla/\">user agreement</a> and <a href=\"https://aws.amazon.com/location/pricing/\">service pricing structure</a> to determine the correct setting for your use case.</p> </note>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. </p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>

        Raises:
            capo_geo_places.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_places.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_places.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_places.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_places.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_places.types.search_nearby_request.SearchNearbyRequest]",
        ) -> OperationResponse[
            "capo_geo_places.types.search_nearby_response.SearchNearbyResponse"
        ]:
            import capo_geo_places._operations.places_service.search_nearby

            output, http_response = (
                capo_geo_places._operations.places_service.search_nearby.search_nearby(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_places.types.search_nearby_request.SearchNearbyRequest = {
            "query_position": query_position
        }
        if query_radius is not None:
            input_["query_radius"] = query_radius
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if language is not None:
            input_["language"] = language
        if political_view is not None:
            input_["political_view"] = political_view
        if intended_use is not None:
            input_["intended_use"] = intended_use
        if next_token is not None:
            input_["next_token"] = next_token
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_text(
        self,
        *,
        config_overrides: Optional[GeoPlacesClientConfig] = None,
        query_text: Optional[
            "capo_geo_places.types.sensitive_string.SensitiveString"
        ] = None,
        query_id: Optional[
            "capo_geo_places.types.sensitive_string.SensitiveString"
        ] = None,
        max_results: Optional[int] = None,
        bias_position: Optional["capo_geo_places.types.position.Position"] = None,
        filter: Optional[
            "capo_geo_places.types.search_text_filter.SearchTextFilter"
        ] = None,
        additional_features: Optional[
            "capo_geo_places.types.search_text_additional_feature_list.SearchTextAdditionalFeatureList"
        ] = None,
        language: Optional["capo_geo_places.types.language_tag.LanguageTag"] = None,
        political_view: Optional[
            "capo_geo_places.types.country_code.CountryCode"
        ] = None,
        intended_use: Optional[
            "capo_geo_places.types.search_text_intended_use.SearchTextIntendedUse"
        ] = None,
        next_token: Optional["capo_geo_places.types.token.Token"] = None,
        key: Optional["capo_geo_places.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_places.types.search_text_response.SearchTextResponse":
        r"""<p> <code>SearchText</code> searches for geocode and place information. You can then complete a follow-up query suggested from the <code>Suggest</code> API via a query id.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/search-text.html\">Search Text</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            query_text: <p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p> <note> <p>Exactly one of the following fields must be set: <code>QueryText</code> or <code>QueryId</code>.</p> </note>
            query_id: <p>The query Id returned by the suggest API. If passed in the request, the SearchText API will preform a SearchText query with the improved query terms for the original query made to the suggest API. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p> <note> <p>Exactly one of the following fields must be set: <code>QueryText</code> or <code>QueryId</code>.</p> </note>
            max_results: <p>An optional limit for the number of results returned in a single call.</p> <p>Default value: 20</p>
            bias_position: <p>The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p> <note> <p>Exactly one of the following fields must be set: <code>BiasPosition</code>, <code>Filter.BoundingBox</code>, or <code>Filter.Circle</code>.</p> </note>
            filter: <p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>
            additional_features: <p>A list of optional additional parameters, such as time zone, that can be requested for each result. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>TimeZone</code> value.</p>
            language: <p>A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the following codes: <code>en, id, km, lo, ms, my, pt, th, tl, vi, zh</code> </p>
            political_view: <p>The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not available in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers.</p>
            intended_use: <p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). </p> <note> <p>When storing <code>SearchText</code> responses, you <i>must</i> set this field to <code>Storage</code> to comply with the terms of service. These requests will be charged at a higher rate. Please review the <a href=\"https://aws.amazon.com/location/sla/\">user agreement</a> and <a href=\"https://aws.amazon.com/location/pricing/\">service pricing structure</a> to determine the correct setting for your use case.</p> </note>
            next_token: <p>If <code>nextToken</code> is returned, there are more results available. The value of <code>nextToken</code> is a unique pagination token for each page. </p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>

        Raises:
            capo_geo_places.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_places.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_places.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_places.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_places.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_places.types.search_text_request.SearchTextRequest]",
        ) -> OperationResponse[
            "capo_geo_places.types.search_text_response.SearchTextResponse"
        ]:
            import capo_geo_places._operations.places_service.search_text

            output, http_response = (
                capo_geo_places._operations.places_service.search_text.search_text(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_places.types.search_text_request.SearchTextRequest = {}
        if query_text is not None:
            input_["query_text"] = query_text
        if query_id is not None:
            input_["query_id"] = query_id
        if max_results is not None:
            input_["max_results"] = max_results
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter is not None:
            input_["filter"] = filter
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if language is not None:
            input_["language"] = language
        if political_view is not None:
            input_["political_view"] = political_view
        if intended_use is not None:
            input_["intended_use"] = intended_use
        if next_token is not None:
            input_["next_token"] = next_token
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def suggest(
        self,
        query_text: "capo_geo_places.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[GeoPlacesClientConfig] = None,
        max_results: Optional[int] = None,
        max_query_refinements: Optional[int] = None,
        bias_position: Optional["capo_geo_places.types.position.Position"] = None,
        filter: Optional["capo_geo_places.types.suggest_filter.SuggestFilter"] = None,
        additional_features: Optional[
            "capo_geo_places.types.suggest_additional_feature_list.SuggestAdditionalFeatureList"
        ] = None,
        language: Optional["capo_geo_places.types.language_tag.LanguageTag"] = None,
        political_view: Optional[
            "capo_geo_places.types.country_code.CountryCode"
        ] = None,
        intended_use: Optional[
            "capo_geo_places.types.suggest_intended_use.SuggestIntendedUse"
        ] = None,
        key: Optional["capo_geo_places.types.api_key.ApiKey"] = None,
    ) -> "capo_geo_places.types.suggest_response.SuggestResponse":
        r"""<p> <code>Suggest</code> provides intelligent predictions or recommendations based on the user's input or context, such as relevant places, points of interest, query terms or search category. It is designed to help users find places or point of interests candidates or identify a follow on query based on incomplete or misspelled queries. It returns a list of possible matches or refinements that can be used to formulate a more accurate query. Users can select the most appropriate suggestion and use it for further searching. The API provides options for filtering results by location and other attributes, and allows for additional features like phonemes and timezones. The response includes refined query terms and detailed place information.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/suggest.html\">Suggest</a> in the <i>Amazon Location Service Developer Guide</i>.</p>

        Args:
            query_text: <p>The free-form text query to match addresses against. This is usually a partially typed address from an end user in an address box or form.</p> <note> <p>The fields <code>QueryText</code> and <code>QueryID</code> are mutually exclusive.</p> </note>
            max_results: <p> An optional limit for the number of results returned in a single call. </p> <p>Default value: 20</p>
            max_query_refinements: <p> Maximum number of query terms to be returned for use with a search text query. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            bias_position: <p>The position, in longitude and latitude, that the results should be close to. Typically, place results returned are ranked higher the closer they are to this position. Stored in <code>[lng, lat]</code> and in the WGS 84 format.</p> <note> <p>The fields <code>BiasPosition</code>, <code>FilterBoundingBox</code>, and <code>FilterCircle</code> are mutually exclusive.</p> </note>
            filter: <p>A structure which contains a set of inclusion/exclusion properties that results must possess in order to be returned as a result.</p>
            additional_features: <p> A list of optional additional parameters, such as time zone, that can be requested for each result. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the <code>Core</code> and <code>TimeZone</code> values. </p>
            language: <p> A list of <a href=\"https://en.wikipedia.org/wiki/IETF_language_tag\">BCP 47</a> compliant language codes for the results to be rendered in. If there is no data for the result in the requested language, data will be returned in the default language for the entry. For <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers, <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions support only the following codes: <code>en, id, km, lo, ms, my, pt, th, tl, vi, zh</code> </p>
            political_view: <p> The alpha-2 or alpha-3 character code for the political view of a country. The political view applies to the results of the request to represent unresolved territorial claims through the point of view of the specified country. Not supported in <code>ap-southeast-1</code> and <code>ap-southeast-5</code> regions for <a href=\"https://docs.aws.amazon.com/location/latest/developerguide/GrabMaps.html\">GrabMaps</a> customers. </p>
            intended_use: <p> Indicates if the query results will be persisted in customer infrastructure. Defaults to <code>SingleUse</code> (not stored). Currently, <code>Suggest</code> does not support storage of results. </p>
            key: <p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request.</p>

        Raises:
            capo_geo_places.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient access to perform this action.</p>
            capo_geo_places.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception or failure.</p>
            capo_geo_places.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_geo_places.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an AWS service.</p>
            capo_geo_places.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_geo_places.types.suggest_request.SuggestRequest]",
        ) -> OperationResponse[
            "capo_geo_places.types.suggest_response.SuggestResponse"
        ]:
            import capo_geo_places._operations.places_service.suggest

            output, http_response = (
                capo_geo_places._operations.places_service.suggest.suggest(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_geo_places.types.suggest_request.SuggestRequest = {
            "query_text": query_text
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if max_query_refinements is not None:
            input_["max_query_refinements"] = max_query_refinements
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter is not None:
            input_["filter"] = filter
        if additional_features is not None:
            input_["additional_features"] = additional_features
        if language is not None:
            input_["language"] = language
        if political_view is not None:
            input_["political_view"] = political_view
        if intended_use is not None:
            input_["intended_use"] = intended_use
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
