from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_sagemaker_geospatial._auth._signers
import capo_sagemaker_geospatial._auth._sigv4
from capo_sagemaker_geospatial._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_sagemaker_geospatial.types.data_collection_arn
    import capo_sagemaker_geospatial.types.get_raster_data_collection_input
    import capo_sagemaker_geospatial.types.get_raster_data_collection_output
    import capo_sagemaker_geospatial.types.list_raster_data_collections_input
    import capo_sagemaker_geospatial.types.list_raster_data_collections_output
    import capo_sagemaker_geospatial.types.next_token
    import capo_sagemaker_geospatial.types.raster_data_collection_metadata
    import capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input
    import capo_sagemaker_geospatial.types.search_raster_data_collection_input
    import capo_sagemaker_geospatial.types.search_raster_data_collection_output
    from capo_sagemaker_geospatial._services.async_sage_maker_geospatial import (
        AsyncSageMakerGeospatialClient,
        AsyncSageMakerGeospatialClientConfig,
    )
    from capo_sagemaker_geospatial._services.sage_maker_geospatial import (
        SageMakerGeospatialClient,
        SageMakerGeospatialClientConfig,
    )


class RasterDataCollection:
    def __init__(self, service: SageMakerGeospatialClient) -> None:
        self._service = service

    def read(
        self,
        arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput":
        """<p>Use this operation to get details of a specific raster data collection.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection.get_raster_data_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput = {
            "arn": arn
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
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput":
        """<p>Use this operation to get raster data collections.</p>

        Args:
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections.list_raster_data_collections(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_raster_data_collection(
        self,
        arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        raster_data_collection_query: "capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.RasterDataCollectionQueryWithBandFilterInput",
        *,
        config_overrides: Optional[SageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
    ) -> "capo_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput":
        """<p>Allows you run image query on a specific raster data collection to get a list of the satellite imagery matching the selected filters.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>
            raster_data_collection_query: <p>RasterDataCollectionQuery consisting of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html">AreaOfInterest(AOI)</a>, <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html">PropertyFilters</a> and <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html">TimeRangeFilterInput</a> used in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html">SearchRasterDataCollection</a>.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput]",
        ) -> OperationResponse[
            "capo_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection

            output, http_response = (
                capo_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection.search_raster_data_collection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput = {
            "arn": arn,
            "raster_data_collection_query": raster_data_collection_query,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncRasterDataCollection:
    def __init__(self, service: AsyncSageMakerGeospatialClient) -> None:
        self._service = service

    async def read(
        self,
        arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
    ) -> "capo_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput":
        """<p>Use this operation to get details of a specific raster data collection.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.get_raster_data_collection_output.GetRasterDataCollectionOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.get_raster_data_collection.async_get_raster_data_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.get_raster_data_collection_input.GetRasterDataCollectionInput = {
            "arn": arn
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
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput":
        """<p>Use this operation to get raster data collections.</p>

        Args:
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>
            max_results: <p>The total number of items to return.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.list_raster_data_collections_output.ListRasterDataCollectionsOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.list_raster_data_collections.async_list_raster_data_collections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.list_raster_data_collections_input.ListRasterDataCollectionsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_raster_data_collection(
        self,
        arn: "capo_sagemaker_geospatial.types.data_collection_arn.DataCollectionArn",
        raster_data_collection_query: "capo_sagemaker_geospatial.types.raster_data_collection_query_with_band_filter_input.RasterDataCollectionQueryWithBandFilterInput",
        *,
        config_overrides: Optional[AsyncSageMakerGeospatialClientConfig] = None,
        next_token: Optional[
            "capo_sagemaker_geospatial.types.next_token.NextToken"
        ] = None,
    ) -> "capo_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput":
        """<p>Allows you run image query on a specific raster data collection to get a list of the satellite imagery matching the selected filters.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the raster data collection.</p>
            raster_data_collection_query: <p>RasterDataCollectionQuery consisting of <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_AreaOfInterest.html">AreaOfInterest(AOI)</a>, <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_PropertyFilter.html">PropertyFilters</a> and <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_TimeRangeFilterInput.html">TimeRangeFilterInput</a> used in <a href="https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_geospatial_SearchRasterDataCollection.html">SearchRasterDataCollection</a>.</p>
            next_token: <p>If the previous response was truncated, you receive this token. Use it in your next request to receive the next set of results.</p>

        Raises:
            capo_sagemaker_geospatial.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_sagemaker_geospatial.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p>
            capo_sagemaker_geospatial.errors.resource_not_found_exception.ResourceNotFoundException: <p>The request references a resource which does not exist.</p>
            capo_sagemaker_geospatial.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_sagemaker_geospatial.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by an Amazon Web Services service.</p>
            capo_sagemaker_geospatial.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_geospatial.types.search_raster_data_collection_output.SearchRasterDataCollectionOutput"
        ]:
            import capo_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection

            (
                output,
                http_response,
            ) = await capo_sagemaker_geospatial._operations.sage_maker_geospatial.search_raster_data_collection.async_search_raster_data_collection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_sagemaker_geospatial.types.search_raster_data_collection_input.SearchRasterDataCollectionInput = {
            "arn": arn,
            "raster_data_collection_query": raster_data_collection_query,
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
