from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_location._auth._signers
import capo_location._auth._sigv4
from capo_location._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_location.types.api_key
    import capo_location.types.bounding_box
    import capo_location.types.country_code_list
    import capo_location.types.create_place_index_request
    import capo_location.types.create_place_index_response
    import capo_location.types.data_source_configuration
    import capo_location.types.delete_place_index_request
    import capo_location.types.delete_place_index_response
    import capo_location.types.describe_place_index_request
    import capo_location.types.describe_place_index_response
    import capo_location.types.filter_place_category_list
    import capo_location.types.get_place_request
    import capo_location.types.get_place_response
    import capo_location.types.language_tag
    import capo_location.types.list_place_indexes_request
    import capo_location.types.list_place_indexes_response
    import capo_location.types.list_place_indexes_response_entry
    import capo_location.types.place_id
    import capo_location.types.place_index_search_result_limit
    import capo_location.types.position
    import capo_location.types.pricing_plan
    import capo_location.types.resource_description
    import capo_location.types.resource_name
    import capo_location.types.search_place_index_for_position_request
    import capo_location.types.search_place_index_for_position_response
    import capo_location.types.search_place_index_for_suggestions_request
    import capo_location.types.search_place_index_for_suggestions_response
    import capo_location.types.search_place_index_for_text_request
    import capo_location.types.search_place_index_for_text_response
    import capo_location.types.sensitive_string
    import capo_location.types.tag_map
    import capo_location.types.token
    import capo_location.types.update_place_index_request
    import capo_location.types.update_place_index_response
    from capo_location._services.async_location import (
        AsyncLocationClient,
        AsyncLocationClientConfig,
    )
    from capo_location._services.location import LocationClient, LocationClientConfig


class PlaceIndexResource:
    def __init__(self, service: LocationClient) -> None:
        self._service = service

    def put(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        data_source: str,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        data_source_configuration: Optional[
            "capo_location.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_place_index_response.CreatePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>CreatePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Creates a place index resource in your Amazon Web Services account. Use a place index resource to geocode addresses and other text queries by using the <code>SearchPlaceIndexForText</code> operation, and reverse geocode coordinates by using the <code>SearchPlaceIndexForPosition</code> operation, and enable autosuggestions by using the <code>SearchPlaceIndexForSuggestions</code> operation.</p> <note> <p>If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the <a href="http://aws.amazon.com/service-terms">Amazon Web Services service terms</a> for more details.</p> </note>

        Args:
            index_name: <p>The name of the place index resource. </p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique place index resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExamplePlaceIndex</code>.</p> </li> </ul>
            data_source: <p>Specifies the geospatial data provider for the new place index.</p> <note> <p>This field is case-sensitive. Enter the valid values as shown. For example, entering <code>HERE</code> returns an error.</p> </note> <p>Valid values include:</p> <ul> <li> <p> <code>Esri</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri</a>'s coverage in your region of interest, see <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm">Esri details on geocoding coverage</a>.</p> </li> <li> <p> <code>Grab</code> – Grab provides place index functionality for Southeast Asia. For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a>' coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area">GrabMaps countries and areas covered</a>.</p> </li> <li> <p> <code>Here</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies</a>' coverage in your region of interest, see <a href="https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html">HERE details on goecoding coverage</a>.</p> <important> <p>If you specify HERE Technologies (<code>Here</code>) as the data provider, you may not <a href="https://docs.aws.amazon.com/location-places/latest/APIReference/API_DataSourceConfiguration.html">store results</a> for locations in Japan. For more information, see the <a href="http://aws.amazon.com/service-terms/">Amazon Web Services service terms</a> for Amazon Location Service.</p> </important> </li> </ul> <p>For additional information , see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Data providers</a> on the <i>Amazon Location Service developer guide</i>.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>The optional description for the place index resource.</p>
            data_source_configuration: <p>Specifies the data storage option requesting Places.</p>
            tags: <p>Applies one or more tags to the place index resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource.</p> </li> <li> <p>Each tag key must be unique and must have exactly one associated value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @</p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.create_place_index_request.CreatePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.create_place_index_response.CreatePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.create_place_index

            output, http_response = (
                capo_location._operations.location_service.create_place_index.create_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.create_place_index_request.CreatePlaceIndexRequest = {
            "index_name": index_name,
            "data_source": data_source,
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if data_source_configuration is not None:
            input_["data_source_configuration"] = data_source_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.describe_place_index_response.DescribePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DescribePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the place index resource details.</p>

        Args:
            index_name: <p>The name of the place index resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.describe_place_index_request.DescribePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.describe_place_index_response.DescribePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.describe_place_index

            output, http_response = (
                capo_location._operations.location_service.describe_place_index.describe_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_place_index_request.DescribePlaceIndexRequest = {
            "index_name": index_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        data_source_configuration: Optional[
            "capo_location.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
    ) -> "capo_location.types.update_place_index_response.UpdatePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>UpdatePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Updates the specified properties of a given place index resource.</p>

        Args:
            index_name: <p>The name of the place index resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>Updates the description for the place index resource.</p>
            data_source_configuration: <p>Updates the data storage option for the place index resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.update_place_index_request.UpdatePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.update_place_index_response.UpdatePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.update_place_index

            output, http_response = (
                capo_location._operations.location_service.update_place_index.update_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.update_place_index_request.UpdatePlaceIndexRequest = {
            "index_name": index_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if data_source_configuration is not None:
            input_["data_source_configuration"] = data_source_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
    ) -> "capo_location.types.delete_place_index_response.DeletePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DeletePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Deletes a place index resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently.</p> </note>

        Args:
            index_name: <p>The name of the place index resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.delete_place_index_request.DeletePlaceIndexRequest]",
        ) -> OperationResponse[
            "capo_location.types.delete_place_index_response.DeletePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.delete_place_index

            output, http_response = (
                capo_location._operations.location_service.delete_place_index.delete_place_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_place_index_request.DeletePlaceIndexRequest = {
            "index_name": index_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_place_indexes_response.ListPlaceIndexesResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>ListPlaceIndexes</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Lists place index resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional limit for the maximum number of results returned in a single call.</p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.list_place_indexes_request.ListPlaceIndexesRequest]",
        ) -> OperationResponse[
            "capo_location.types.list_place_indexes_response.ListPlaceIndexesResponse"
        ]:
            import capo_location._operations.location_service.list_place_indexes

            output, http_response = (
                capo_location._operations.location_service.list_place_indexes.list_place_indexes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_place_indexes_request.ListPlaceIndexesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_place(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        place_id: "capo_location.types.place_id.PlaceId",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.get_place_response.GetPlaceResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the <a href="/location/latest/APIReference/API_geoplaces_GetPlace.html">V2 <code>GetPlace</code> </a> operation unless you require Grab data.</p> <ul> <li> <p>This version of <code>GetPlace</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>Version 2 of the <code>GetPlace</code> operation interoperates with the rest of the Places V2 API, while this version does not.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Finds a place by its unique ID. A <code>PlaceId</code> is returned by other search operations.</p> <note> <p>A PlaceId is valid only if all of the following are the same in the original search request and the call to <code>GetPlace</code>.</p> <ul> <li> <p>Customer Amazon Web Services account</p> </li> <li> <p>Amazon Web Services Region</p> </li> <li> <p>Data provider specified in the place index resource</p> </li> </ul> </note> <note> <p>If your Place index resource is configured with Grab as your geolocation provider and Storage as Intended use, the GetPlace operation is unavailable. For more information, see <a href="http://aws.amazon.com/service-terms">AWS service terms</a>.</p> </note>

        Args:
            index_name: <p>The name of the place index resource that you want to use for the search.</p>
            place_id: <p>The identifier of the place to find.</p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.get_place_request.GetPlaceRequest]",
        ) -> OperationResponse[
            "capo_location.types.get_place_response.GetPlaceResponse"
        ]:
            import capo_location._operations.location_service.get_place

            output, http_response = (
                capo_location._operations.location_service.get_place.get_place(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.get_place_request.GetPlaceRequest = {
            "index_name": index_name,
            "place_id": place_id,
        }
        if language is not None:
            input_["language"] = language
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_place_index_for_position(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        position: "capo_location.types.position.Position",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        max_results: Optional[
            "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
        ] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_position_response.SearchPlaceIndexForPositionResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_ReverseGeocode.html"> <code>ReverseGeocode</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_SearchNearby.html"> <code>SearchNearby</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForPosition</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>ReverseGeocode</code> operation gives better results in the address reverse-geocoding use case, while the version 2 <code>SearchNearby</code> operation gives better results when searching for businesses and points of interest near a specific location.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Reverse geocodes a given coordinate and returns a legible address. Allows you to search for Places or points of interest near a given position.</p>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            position: <p>Specifies the longitude and latitude of the position to query.</p> <p> This parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents a position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p>
            max_results: <p>An optional parameter. The maximum number of results returned per request.</p> <p>Default value: <code>50</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.search_place_index_for_position_request.SearchPlaceIndexForPositionRequest]",
        ) -> OperationResponse[
            "capo_location.types.search_place_index_for_position_response.SearchPlaceIndexForPositionResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_position

            output, http_response = (
                capo_location._operations.location_service.search_place_index_for_position.search_place_index_for_position(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_position_request.SearchPlaceIndexForPositionRequest = {
            "index_name": index_name,
            "position": position,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_place_index_for_suggestions(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        text: "capo_location.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        bias_position: Optional["capo_location.types.position.Position"] = None,
        filter_b_box: Optional["capo_location.types.bounding_box.BoundingBox"] = None,
        filter_countries: Optional[
            "capo_location.types.country_code_list.CountryCodeList"
        ] = None,
        max_results: Optional[int] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        filter_categories: Optional[
            "capo_location.types.filter_place_category_list.FilterPlaceCategoryList"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_suggestions_response.SearchPlaceIndexForSuggestionsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_Suggest.html"> <code>Suggest</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_Autocomplete.html"> <code>Autocomplete</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForSuggestions</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>Suggest</code> operation gives better results for typeahead place search suggestions with fuzzy matching, while the version 2 <code>Autocomplete</code> operation gives better results for address completion based on partial input.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Generates suggestions for addresses and points of interest based on partial or misspelled free-form text. This operation is also known as autocomplete, autosuggest, or fuzzy matching.</p> <p>Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.</p> <note> <p>You can search for suggested place names near a specified position by using <code>BiasPosition</code>, or filter results within a bounding box by using <code>FilterBBox</code>. These parameters are mutually exclusive; using both <code>BiasPosition</code> and <code>FilterBBox</code> in the same command returns an error.</p> </note>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            text: <p>The free-form partial text to use to generate place suggestions. For example, <code>eiffel tow</code>.</p>
            bias_position: <p>An optional parameter that indicates a preference for place suggestions that are closer to a specified position.</p> <p> If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p> <note> <p> <code>BiasPosition</code> and <code>FilterBBox</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_b_box: <p>An optional parameter that limits the search results by returning only suggestions within a specified bounding box.</p> <p> If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.</p> <p>For example, <code>[-12.7935, -37.4835, -12.0684, -36.9542]</code> represents a bounding box where the southwest corner has longitude <code>-12.7935</code> and latitude <code>-37.4835</code>, and the northeast corner has longitude <code>-12.0684</code> and latitude <code>-36.9542</code>.</p> <note> <p> <code>FilterBBox</code> and <code>BiasPosition</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_countries: <p>An optional parameter that limits the search results by returning only suggestions within the provided list of countries.</p> <ul> <li> <p>Use the <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country code. For example, Australia uses three upper-case characters: <code>AUS</code>.</p> </li> </ul>
            max_results: <p>An optional parameter. The maximum number of results returned per request. </p> <p>The default: <code>5</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for <code>Athens, Gr</code> to get suggestions with the <code>language</code> parameter set to <code>en</code>. The results found will most likely be returned as <code>Athens, Greece</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the result found will more likely be returned as <code>Αθήνα, Ελλάδα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            filter_categories: <p>A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match <i>any</i> of the categories listed.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.search_place_index_for_suggestions_request.SearchPlaceIndexForSuggestionsRequest]",
        ) -> OperationResponse[
            "capo_location.types.search_place_index_for_suggestions_response.SearchPlaceIndexForSuggestionsResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_suggestions

            output, http_response = (
                capo_location._operations.location_service.search_place_index_for_suggestions.search_place_index_for_suggestions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_suggestions_request.SearchPlaceIndexForSuggestionsRequest = {
            "index_name": index_name,
            "text": text,
        }
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter_b_box is not None:
            input_["filter_b_box"] = filter_b_box
        if filter_countries is not None:
            input_["filter_countries"] = filter_countries
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if filter_categories is not None:
            input_["filter_categories"] = filter_categories
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_place_index_for_text(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        text: "capo_location.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[LocationClientConfig] = None,
        bias_position: Optional["capo_location.types.position.Position"] = None,
        filter_b_box: Optional["capo_location.types.bounding_box.BoundingBox"] = None,
        filter_countries: Optional[
            "capo_location.types.country_code_list.CountryCodeList"
        ] = None,
        max_results: Optional[
            "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
        ] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        filter_categories: Optional[
            "capo_location.types.filter_place_category_list.FilterPlaceCategoryList"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_text_response.SearchPlaceIndexForTextResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_Geocode.html"> <code>Geocode</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_SearchText.html"> <code>SearchText</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForText</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>Geocode</code> operation gives better results in the address geocoding use case, while the version 2 <code>SearchText</code> operation gives better results when searching for businesses and points of interest.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Geocodes free-form text, such as an address, name, city, or region to allow you to search for Places or points of interest. </p> <p>Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.</p> <note> <p>You can search for places near a given position using <code>BiasPosition</code>, or filter results within a bounding box using <code>FilterBBox</code>. Providing both parameters simultaneously returns an error.</p> </note> <p>Search results are returned in order of highest to lowest relevance.</p>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            text: <p>The address, name, city, or region to be used in the search in free-form text format. For example, <code>123 Any Street</code>.</p>
            bias_position: <p>An optional parameter that indicates a preference for places that are closer to a specified position.</p> <p> If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p> <note> <p> <code>BiasPosition</code> and <code>FilterBBox</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_b_box: <p>An optional parameter that limits the search results by returning only places that are within the provided bounding box.</p> <p> If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.</p> <p>For example, <code>[-12.7935, -37.4835, -12.0684, -36.9542]</code> represents a bounding box where the southwest corner has longitude <code>-12.7935</code> and latitude <code>-37.4835</code>, and the northeast corner has longitude <code>-12.0684</code> and latitude <code>-36.9542</code>.</p> <note> <p> <code>FilterBBox</code> and <code>BiasPosition</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_countries: <p>An optional parameter that limits the search results by returning only places that are in a specified list of countries.</p> <ul> <li> <p>Valid values include <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country codes. For example, Australia uses three upper-case characters: <code>AUS</code>.</p> </li> </ul>
            max_results: <p>An optional parameter. The maximum number of results returned per request. </p> <p>The default: <code>50</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for <code>Athens, Greece</code>, with the <code>language</code> parameter set to <code>en</code>. The result found will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the result found will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            filter_categories: <p>A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match <i>any</i> of the categories listed.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_location.types.search_place_index_for_text_request.SearchPlaceIndexForTextRequest]",
        ) -> OperationResponse[
            "capo_location.types.search_place_index_for_text_response.SearchPlaceIndexForTextResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_text

            output, http_response = (
                capo_location._operations.location_service.search_place_index_for_text.search_place_index_for_text(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_text_request.SearchPlaceIndexForTextRequest = {
            "index_name": index_name,
            "text": text,
        }
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter_b_box is not None:
            input_["filter_b_box"] = filter_b_box
        if filter_countries is not None:
            input_["filter_countries"] = filter_countries
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if filter_categories is not None:
            input_["filter_categories"] = filter_categories
        if key is not None:
            input_["key"] = key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncPlaceIndexResource:
    def __init__(self, service: AsyncLocationClient) -> None:
        self._service = service

    async def put(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        data_source: str,
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        data_source_configuration: Optional[
            "capo_location.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
        tags: Optional["capo_location.types.tag_map.TagMap"] = None,
    ) -> "capo_location.types.create_place_index_response.CreatePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>CreatePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Creates a place index resource in your Amazon Web Services account. Use a place index resource to geocode addresses and other text queries by using the <code>SearchPlaceIndexForText</code> operation, and reverse geocode coordinates by using the <code>SearchPlaceIndexForPosition</code> operation, and enable autosuggestions by using the <code>SearchPlaceIndexForSuggestions</code> operation.</p> <note> <p>If your application is tracking or routing assets you use in your business, such as delivery vehicles or employees, you must not use Esri as your geolocation provider. See section 82 of the <a href="http://aws.amazon.com/service-terms">Amazon Web Services service terms</a> for more details.</p> </note>

        Args:
            index_name: <p>The name of the place index resource. </p> <p>Requirements:</p> <ul> <li> <p>Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (_).</p> </li> <li> <p>Must be a unique place index resource name.</p> </li> <li> <p>No spaces allowed. For example, <code>ExamplePlaceIndex</code>.</p> </li> </ul>
            data_source: <p>Specifies the geospatial data provider for the new place index.</p> <note> <p>This field is case-sensitive. Enter the valid values as shown. For example, entering <code>HERE</code> returns an error.</p> </note> <p>Valid values include:</p> <ul> <li> <p> <code>Esri</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/esri.html">Esri</a>'s coverage in your region of interest, see <a href="https://developers.arcgis.com/rest/geocode/api-reference/geocode-coverage.htm">Esri details on geocoding coverage</a>.</p> </li> <li> <p> <code>Grab</code> – Grab provides place index functionality for Southeast Asia. For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html">GrabMaps</a>' coverage, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/grab.html#grab-coverage-area">GrabMaps countries and areas covered</a>.</p> </li> <li> <p> <code>Here</code> – For additional information about <a href="https://docs.aws.amazon.com/location/previous/developerguide/HERE.html">HERE Technologies</a>' coverage in your region of interest, see <a href="https://developer.here.com/documentation/geocoder/dev_guide/topics/coverage-geocoder.html">HERE details on goecoding coverage</a>.</p> <important> <p>If you specify HERE Technologies (<code>Here</code>) as the data provider, you may not <a href="https://docs.aws.amazon.com/location-places/latest/APIReference/API_DataSourceConfiguration.html">store results</a> for locations in Japan. For more information, see the <a href="http://aws.amazon.com/service-terms/">Amazon Web Services service terms</a> for Amazon Location Service.</p> </important> </li> </ul> <p>For additional information , see <a href="https://docs.aws.amazon.com/location/previous/developerguide/what-is-data-provider.html">Data providers</a> on the <i>Amazon Location Service developer guide</i>.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>The optional description for the place index resource.</p>
            data_source_configuration: <p>Specifies the data storage option requesting Places.</p>
            tags: <p>Applies one or more tags to the place index resource. A tag is a key-value pair that helps you manage, identify, search, and filter your resources.</p> <p>Format: <code>"key" : "value"</code> </p> <p>Restrictions:</p> <ul> <li> <p>Maximum 50 tags per resource.</p> </li> <li> <p>Each tag key must be unique and must have exactly one associated value.</p> </li> <li> <p>Maximum key length: 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length: 256 Unicode characters in UTF-8.</p> </li> <li> <p>Can use alphanumeric characters (A–Z, a–z, 0–9), and the following characters: + - = . _ : / @</p> </li> <li> <p>Cannot use "aws:" as a prefix for a key.</p> </li> </ul>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.conflict_exception.ConflictException: <p>The request was unsuccessful because of a conflict.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The operation was denied because the request would exceed the maximum <a href="https://docs.aws.amazon.com/location/previous/developerguide/location-quotas.html">quota</a> set for Amazon Location Service.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.create_place_index_request.CreatePlaceIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.create_place_index_response.CreatePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.create_place_index

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.create_place_index.async_create_place_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.create_place_index_request.CreatePlaceIndexRequest = {
            "index_name": index_name,
            "data_source": data_source,
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if data_source_configuration is not None:
            input_["data_source_configuration"] = data_source_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "capo_location.types.describe_place_index_response.DescribePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DescribePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Retrieves the place index resource details.</p>

        Args:
            index_name: <p>The name of the place index resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.describe_place_index_request.DescribePlaceIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.describe_place_index_response.DescribePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.describe_place_index

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.describe_place_index.async_describe_place_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.describe_place_index_request.DescribePlaceIndexRequest = {
            "index_name": index_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        pricing_plan: Optional["capo_location.types.pricing_plan.PricingPlan"] = None,
        description: Optional[
            "capo_location.types.resource_description.ResourceDescription"
        ] = None,
        data_source_configuration: Optional[
            "capo_location.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
    ) -> "capo_location.types.update_place_index_response.UpdatePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>UpdatePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Updates the specified properties of a given place index resource.</p>

        Args:
            index_name: <p>The name of the place index resource to update.</p>
            pricing_plan: <p>No longer used. If included, the only allowed value is <code>RequestBasedUsage</code>.</p>
            description: <p>Updates the description for the place index resource.</p>
            data_source_configuration: <p>Updates the data storage option for the place index resource.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.update_place_index_request.UpdatePlaceIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.update_place_index_response.UpdatePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.update_place_index

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.update_place_index.async_update_place_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.update_place_index_request.UpdatePlaceIndexRequest = {
            "index_name": index_name
        }
        if pricing_plan is not None:
            input_["pricing_plan"] = pricing_plan
        if description is not None:
            input_["description"] = description
        if data_source_configuration is not None:
            input_["data_source_configuration"] = data_source_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
    ) -> "capo_location.types.delete_place_index_response.DeletePlaceIndexResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>DeletePlaceIndex</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Deletes a place index resource from your Amazon Web Services account.</p> <note> <p>This operation deletes the resource permanently.</p> </note>

        Args:
            index_name: <p>The name of the place index resource to be deleted.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.delete_place_index_request.DeletePlaceIndexRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.delete_place_index_response.DeletePlaceIndexResponse"
        ]:
            import capo_location._operations.location_service.delete_place_index

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.delete_place_index.async_delete_place_index(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.delete_place_index_request.DeletePlaceIndexRequest = {
            "index_name": index_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_location.types.token.Token"] = None,
    ) -> "capo_location.types.list_place_indexes_response.ListPlaceIndexesResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the Places API V2 unless you require Grab data.</p> <ul> <li> <p> <code>ListPlaceIndexes</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The Places API version 2 has a simplified interface that can be used without creating or managing place index resources.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Lists place index resources in your Amazon Web Services account.</p>

        Args:
            max_results: <p>An optional limit for the maximum number of results returned in a single call.</p> <p>Default value: <code>100</code> </p>
            next_token: <p>The pagination token specifying which page of results to return in the response. If no token is provided, the default page is the first page.</p> <p>Default value: <code>null</code> </p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.list_place_indexes_request.ListPlaceIndexesRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.list_place_indexes_response.ListPlaceIndexesResponse"
        ]:
            import capo_location._operations.location_service.list_place_indexes

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.list_place_indexes.async_list_place_indexes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.list_place_indexes_request.ListPlaceIndexesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_place(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        place_id: "capo_location.types.place_id.PlaceId",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.get_place_response.GetPlaceResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to the <a href="/location/latest/APIReference/API_geoplaces_GetPlace.html">V2 <code>GetPlace</code> </a> operation unless you require Grab data.</p> <ul> <li> <p>This version of <code>GetPlace</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>Version 2 of the <code>GetPlace</code> operation interoperates with the rest of the Places V2 API, while this version does not.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> <li> <p>Start your version 2 API journey with the Places V2 <a href="/location/latest/APIReference/API_Operations_Amazon_Location_Service_Places_V2.html">API Reference</a> or the <a href="/location/latest/developerguide/places.html">Developer Guide</a>.</p> </li> </ul> </important> <p>Finds a place by its unique ID. A <code>PlaceId</code> is returned by other search operations.</p> <note> <p>A PlaceId is valid only if all of the following are the same in the original search request and the call to <code>GetPlace</code>.</p> <ul> <li> <p>Customer Amazon Web Services account</p> </li> <li> <p>Amazon Web Services Region</p> </li> <li> <p>Data provider specified in the place index resource</p> </li> </ul> </note> <note> <p>If your Place index resource is configured with Grab as your geolocation provider and Storage as Intended use, the GetPlace operation is unavailable. For more information, see <a href="http://aws.amazon.com/service-terms">AWS service terms</a>.</p> </note>

        Args:
            index_name: <p>The name of the place index resource that you want to use for the search.</p>
            place_id: <p>The identifier of the place to find.</p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.get_place_request.GetPlaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.get_place_response.GetPlaceResponse"
        ]:
            import capo_location._operations.location_service.get_place

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.get_place.async_get_place(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.get_place_request.GetPlaceRequest = {
            "index_name": index_name,
            "place_id": place_id,
        }
        if language is not None:
            input_["language"] = language
        if key is not None:
            input_["key"] = key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_place_index_for_position(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        position: "capo_location.types.position.Position",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        max_results: Optional[
            "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
        ] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_position_response.SearchPlaceIndexForPositionResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_ReverseGeocode.html"> <code>ReverseGeocode</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_SearchNearby.html"> <code>SearchNearby</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForPosition</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>ReverseGeocode</code> operation gives better results in the address reverse-geocoding use case, while the version 2 <code>SearchNearby</code> operation gives better results when searching for businesses and points of interest near a specific location.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Reverse geocodes a given coordinate and returns a legible address. Allows you to search for Places or points of interest near a given position.</p>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            position: <p>Specifies the longitude and latitude of the position to query.</p> <p> This parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents a position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p>
            max_results: <p>An optional parameter. The maximum number of results returned per request.</p> <p>Default value: <code>50</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for a location around Athens, Greece, with the <code>language</code> parameter set to <code>en</code>. The <code>city</code> in the results will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the <code>city</code> in the results will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.search_place_index_for_position_request.SearchPlaceIndexForPositionRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.search_place_index_for_position_response.SearchPlaceIndexForPositionResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_position

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.search_place_index_for_position.async_search_place_index_for_position(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_position_request.SearchPlaceIndexForPositionRequest = {
            "index_name": index_name,
            "position": position,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if key is not None:
            input_["key"] = key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_place_index_for_suggestions(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        text: "capo_location.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        bias_position: Optional["capo_location.types.position.Position"] = None,
        filter_b_box: Optional["capo_location.types.bounding_box.BoundingBox"] = None,
        filter_countries: Optional[
            "capo_location.types.country_code_list.CountryCodeList"
        ] = None,
        max_results: Optional[int] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        filter_categories: Optional[
            "capo_location.types.filter_place_category_list.FilterPlaceCategoryList"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_suggestions_response.SearchPlaceIndexForSuggestionsResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_Suggest.html"> <code>Suggest</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_Autocomplete.html"> <code>Autocomplete</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForSuggestions</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>Suggest</code> operation gives better results for typeahead place search suggestions with fuzzy matching, while the version 2 <code>Autocomplete</code> operation gives better results for address completion based on partial input.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Generates suggestions for addresses and points of interest based on partial or misspelled free-form text. This operation is also known as autocomplete, autosuggest, or fuzzy matching.</p> <p>Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.</p> <note> <p>You can search for suggested place names near a specified position by using <code>BiasPosition</code>, or filter results within a bounding box by using <code>FilterBBox</code>. These parameters are mutually exclusive; using both <code>BiasPosition</code> and <code>FilterBBox</code> in the same command returns an error.</p> </note>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            text: <p>The free-form partial text to use to generate place suggestions. For example, <code>eiffel tow</code>.</p>
            bias_position: <p>An optional parameter that indicates a preference for place suggestions that are closer to a specified position.</p> <p> If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p> <note> <p> <code>BiasPosition</code> and <code>FilterBBox</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_b_box: <p>An optional parameter that limits the search results by returning only suggestions within a specified bounding box.</p> <p> If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.</p> <p>For example, <code>[-12.7935, -37.4835, -12.0684, -36.9542]</code> represents a bounding box where the southwest corner has longitude <code>-12.7935</code> and latitude <code>-37.4835</code>, and the northeast corner has longitude <code>-12.0684</code> and latitude <code>-36.9542</code>.</p> <note> <p> <code>FilterBBox</code> and <code>BiasPosition</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_countries: <p>An optional parameter that limits the search results by returning only suggestions within the provided list of countries.</p> <ul> <li> <p>Use the <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country code. For example, Australia uses three upper-case characters: <code>AUS</code>.</p> </li> </ul>
            max_results: <p>An optional parameter. The maximum number of results returned per request. </p> <p>The default: <code>5</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for <code>Athens, Gr</code> to get suggestions with the <code>language</code> parameter set to <code>en</code>. The results found will most likely be returned as <code>Athens, Greece</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the result found will more likely be returned as <code>Αθήνα, Ελλάδα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            filter_categories: <p>A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match <i>any</i> of the categories listed.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.search_place_index_for_suggestions_request.SearchPlaceIndexForSuggestionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.search_place_index_for_suggestions_response.SearchPlaceIndexForSuggestionsResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_suggestions

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.search_place_index_for_suggestions.async_search_place_index_for_suggestions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_suggestions_request.SearchPlaceIndexForSuggestionsRequest = {
            "index_name": index_name,
            "text": text,
        }
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter_b_box is not None:
            input_["filter_b_box"] = filter_b_box
        if filter_countries is not None:
            input_["filter_countries"] = filter_countries
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if filter_categories is not None:
            input_["filter_categories"] = filter_categories
        if key is not None:
            input_["key"] = key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_place_index_for_text(
        self,
        index_name: "capo_location.types.resource_name.ResourceName",
        text: "capo_location.types.sensitive_string.SensitiveString",
        *,
        config_overrides: Optional[AsyncLocationClientConfig] = None,
        bias_position: Optional["capo_location.types.position.Position"] = None,
        filter_b_box: Optional["capo_location.types.bounding_box.BoundingBox"] = None,
        filter_countries: Optional[
            "capo_location.types.country_code_list.CountryCodeList"
        ] = None,
        max_results: Optional[
            "capo_location.types.place_index_search_result_limit.PlaceIndexSearchResultLimit"
        ] = None,
        language: Optional["capo_location.types.language_tag.LanguageTag"] = None,
        filter_categories: Optional[
            "capo_location.types.filter_place_category_list.FilterPlaceCategoryList"
        ] = None,
        key: Optional["capo_location.types.api_key.ApiKey"] = None,
    ) -> "capo_location.types.search_place_index_for_text_response.SearchPlaceIndexForTextResponse":
        """<important> <p>This operation is no longer current and may be deprecated in the future. We recommend you upgrade to <a href="/location/latest/APIReference/API_geoplaces_Geocode.html"> <code>Geocode</code> </a> or <a href="/location/latest/APIReference/API_geoplaces_SearchText.html"> <code>SearchText</code> </a> unless you require Grab data.</p> <ul> <li> <p> <code>SearchPlaceIndexForText</code> is part of a previous Amazon Location Service Places API (version 1) which has been superseded by a more intuitive, powerful, and complete API (version 2).</p> </li> <li> <p>The version 2 <code>Geocode</code> operation gives better results in the address geocoding use case, while the version 2 <code>SearchText</code> operation gives better results when searching for businesses and points of interest.</p> </li> <li> <p>If you are using an Amazon Web Services SDK or the Amazon Web Services CLI, note that the Places API version 2 is found under <code>geo-places</code> or <code>geo_places</code>, not under <code>location</code>.</p> </li> <li> <p>Since Grab is not yet fully supported in Places API version 2, we recommend you continue using API version 1 when using Grab.</p> </li> </ul> </important> <p>Geocodes free-form text, such as an address, name, city, or region to allow you to search for Places or points of interest. </p> <p>Optional parameters let you narrow your search results by bounding box or country, or bias your search toward a specific position on the globe.</p> <note> <p>You can search for places near a given position using <code>BiasPosition</code>, or filter results within a bounding box using <code>FilterBBox</code>. Providing both parameters simultaneously returns an error.</p> </note> <p>Search results are returned in order of highest to lowest relevance.</p>

        Args:
            index_name: <p>The name of the place index resource you want to use for the search.</p>
            text: <p>The address, name, city, or region to be used in the search in free-form text format. For example, <code>123 Any Street</code>.</p>
            bias_position: <p>An optional parameter that indicates a preference for places that are closer to a specified position.</p> <p> If provided, this parameter must contain a pair of numbers. The first number represents the X coordinate, or longitude; the second number represents the Y coordinate, or latitude.</p> <p>For example, <code>[-123.1174, 49.2847]</code> represents the position with longitude <code>-123.1174</code> and latitude <code>49.2847</code>.</p> <note> <p> <code>BiasPosition</code> and <code>FilterBBox</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_b_box: <p>An optional parameter that limits the search results by returning only places that are within the provided bounding box.</p> <p> If provided, this parameter must contain a total of four consecutive numbers in two pairs. The first pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the southwest corner of the bounding box; the second pair of numbers represents the X and Y coordinates (longitude and latitude, respectively) of the northeast corner of the bounding box.</p> <p>For example, <code>[-12.7935, -37.4835, -12.0684, -36.9542]</code> represents a bounding box where the southwest corner has longitude <code>-12.7935</code> and latitude <code>-37.4835</code>, and the northeast corner has longitude <code>-12.0684</code> and latitude <code>-36.9542</code>.</p> <note> <p> <code>FilterBBox</code> and <code>BiasPosition</code> are mutually exclusive. Specifying both options results in an error. </p> </note>
            filter_countries: <p>An optional parameter that limits the search results by returning only places that are in a specified list of countries.</p> <ul> <li> <p>Valid values include <a href="https://www.iso.org/iso-3166-country-codes.html">ISO 3166</a> 3-digit country codes. For example, Australia uses three upper-case characters: <code>AUS</code>.</p> </li> </ul>
            max_results: <p>An optional parameter. The maximum number of results returned per request. </p> <p>The default: <code>50</code> </p>
            language: <p>The preferred language used to return results. The value must be a valid <a href="https://tools.ietf.org/search/bcp47">BCP 47</a> language tag, for example, <code>en</code> for English.</p> <p>This setting affects the languages used in the results, but not the results themselves. If no language is specified, or not supported for a particular result, the partner automatically chooses a language for the result.</p> <p>For an example, we'll use the Greek language. You search for <code>Athens, Greece</code>, with the <code>language</code> parameter set to <code>en</code>. The result found will most likely be returned as <code>Athens</code>.</p> <p>If you set the <code>language</code> parameter to <code>el</code>, for Greek, then the result found will more likely be returned as <code>Αθήνα</code>.</p> <p>If the data provider does not have a value for Greek, the result will be in a language that the provider does support.</p>
            filter_categories: <p>A list of one or more Amazon Location categories to filter the returned places. If you include more than one category, the results will include results that match <i>any</i> of the categories listed.</p> <p>For more information about using categories, including a list of Amazon Location categories, see <a href="https://docs.aws.amazon.com/location/previous/developerguide/category-filtering.html">Categories and filtering</a>, in the <i>Amazon Location Service developer guide</i>.</p>
            key: <p>The optional <a href="https://docs.aws.amazon.com/location/previous/developerguide/using-apikeys.html">API key</a> to authorize the request.</p>

        Raises:
            capo_location.errors.access_denied_exception.AccessDeniedException: <p>The request was denied because of insufficient access or permissions. Check with an administrator to verify your permissions.</p>
            capo_location.errors.internal_server_exception.InternalServerException: <p>The request has failed to process because of an unknown server error, exception, or failure.</p>
            capo_location.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource that you've entered was not found in your AWS account.</p>
            capo_location.errors.throttling_exception.ThrottlingException: <p>The request was denied because of request throttling.</p>
            capo_location.errors.validation_exception.ValidationException: <p>The input failed to meet the constraints specified by the AWS service. </p>
            capo_location.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_location.types.search_place_index_for_text_request.SearchPlaceIndexForTextRequest]",
        ) -> AsyncOperationResponse[
            "capo_location.types.search_place_index_for_text_response.SearchPlaceIndexForTextResponse"
        ]:
            import capo_location._operations.location_service.search_place_index_for_text

            (
                output,
                http_response,
            ) = await capo_location._operations.location_service.search_place_index_for_text.async_search_place_index_for_text(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_location.types.search_place_index_for_text_request.SearchPlaceIndexForTextRequest = {
            "index_name": index_name,
            "text": text,
        }
        if bias_position is not None:
            input_["bias_position"] = bias_position
        if filter_b_box is not None:
            input_["filter_b_box"] = filter_b_box
        if filter_countries is not None:
            input_["filter_countries"] = filter_countries
        if max_results is not None:
            input_["max_results"] = max_results
        if language is not None:
            input_["language"] = language
        if filter_categories is not None:
            input_["filter_categories"] = filter_categories
        if key is not None:
            input_["key"] = key

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
