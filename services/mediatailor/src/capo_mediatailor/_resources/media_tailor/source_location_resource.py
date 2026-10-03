from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_mediatailor._auth._signers
import capo_mediatailor._auth._sigv4
from capo_mediatailor._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_mediatailor.types.__list_of_segment_delivery_configuration
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.access_configuration
    import capo_mediatailor.types.create_source_location_request
    import capo_mediatailor.types.create_source_location_response
    import capo_mediatailor.types.default_segment_delivery_configuration
    import capo_mediatailor.types.delete_source_location_request
    import capo_mediatailor.types.delete_source_location_response
    import capo_mediatailor.types.describe_source_location_request
    import capo_mediatailor.types.describe_source_location_response
    import capo_mediatailor.types.http_configuration
    import capo_mediatailor.types.list_source_locations_request
    import capo_mediatailor.types.list_source_locations_response
    import capo_mediatailor.types.max_results
    import capo_mediatailor.types.source_location
    import capo_mediatailor.types.update_source_location_request
    import capo_mediatailor.types.update_source_location_response
    from capo_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from capo_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class SourceLocationResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        http_configuration: "capo_mediatailor.types.http_configuration.HttpConfiguration",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        access_configuration: Optional[
            "capo_mediatailor.types.access_configuration.AccessConfiguration"
        ] = None,
        default_segment_delivery_configuration: Optional[
            "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
        ] = None,
        segment_delivery_configurations: Optional[
            "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_source_location_response.CreateSourceLocationResponse":
        """<p>Creates a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            access_configuration: <p>Access configuration parameters. Configures the type of authentication used to access content from your source location.</p>
            default_segment_delivery_configuration: <p>The optional configuration for the server that serves segments.</p>
            http_configuration: <p>The source's HTTP package configurations.</p>
            segment_delivery_configurations: <p>A list of the segment delivery configurations associated with this resource.</p>
            source_location_name: <p>The name associated with the source location.</p>
            tags: <p>The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_source_location_request.CreateSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_source_location_response.CreateSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_source_location.create_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_source_location_request.CreateSourceLocationRequest = {
            "http_configuration": http_configuration,
            "source_location_name": source_location_name,
        }
        if access_configuration is not None:
            input_["access_configuration"] = access_configuration
        if default_segment_delivery_configuration is not None:
            input_["default_segment_delivery_configuration"] = (
                default_segment_delivery_configuration
            )
        if segment_delivery_configurations is not None:
            input_["segment_delivery_configurations"] = segment_delivery_configurations
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
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_source_location_response.DescribeSourceLocationResponse":
        """<p>Describes a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_source_location_request.DescribeSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_source_location_response.DescribeSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_source_location.describe_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_source_location_request.DescribeSourceLocationRequest = {
            "source_location_name": source_location_name
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
        http_configuration: "capo_mediatailor.types.http_configuration.HttpConfiguration",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        access_configuration: Optional[
            "capo_mediatailor.types.access_configuration.AccessConfiguration"
        ] = None,
        default_segment_delivery_configuration: Optional[
            "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
        ] = None,
        segment_delivery_configurations: Optional[
            "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
        ] = None,
    ) -> "capo_mediatailor.types.update_source_location_response.UpdateSourceLocationResponse":
        """<p>Updates a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            access_configuration: <p>Access configuration parameters. Configures the type of authentication used to access content from your source location.</p>
            default_segment_delivery_configuration: <p>The optional configuration for the host server that serves segments.</p>
            http_configuration: <p>The HTTP configuration for the source location.</p>
            segment_delivery_configurations: <p>A list of the segment delivery configurations associated with this resource.</p>
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_source_location_request.UpdateSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_source_location_response.UpdateSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_source_location.update_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_source_location_request.UpdateSourceLocationRequest = {
            "http_configuration": http_configuration,
            "source_location_name": source_location_name,
        }
        if access_configuration is not None:
            input_["access_configuration"] = access_configuration
        if default_segment_delivery_configuration is not None:
            input_["default_segment_delivery_configuration"] = (
                default_segment_delivery_configuration
            )
        if segment_delivery_configurations is not None:
            input_["segment_delivery_configurations"] = segment_delivery_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_source_location_response.DeleteSourceLocationResponse":
        """<p>Deletes a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_source_location_request.DeleteSourceLocationRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_source_location_response.DeleteSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_source_location

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_source_location.delete_source_location(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_source_location_request.DeleteSourceLocationRequest = {
            "source_location_name": source_location_name
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
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_source_locations_response.ListSourceLocationsResponse":
        """<p>Lists the source locations for a channel. A source location defines the host server URL, and contains a list of sources.</p>

        Args:
            max_results: <p> The maximum number of source locations that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> source locations, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListSourceLocations</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_source_locations_request.ListSourceLocationsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_source_locations_response.ListSourceLocationsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_source_locations

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_source_locations.list_source_locations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_source_locations_request.ListSourceLocationsRequest = {}
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


class AsyncSourceLocationResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        http_configuration: "capo_mediatailor.types.http_configuration.HttpConfiguration",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        access_configuration: Optional[
            "capo_mediatailor.types.access_configuration.AccessConfiguration"
        ] = None,
        default_segment_delivery_configuration: Optional[
            "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
        ] = None,
        segment_delivery_configurations: Optional[
            "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_source_location_response.CreateSourceLocationResponse":
        """<p>Creates a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            access_configuration: <p>Access configuration parameters. Configures the type of authentication used to access content from your source location.</p>
            default_segment_delivery_configuration: <p>The optional configuration for the server that serves segments.</p>
            http_configuration: <p>The source's HTTP package configurations.</p>
            segment_delivery_configurations: <p>A list of the segment delivery configurations associated with this resource.</p>
            source_location_name: <p>The name associated with the source location.</p>
            tags: <p>The tags to assign to the source location. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.create_source_location_request.CreateSourceLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.create_source_location_response.CreateSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_source_location

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.create_source_location.async_create_source_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_source_location_request.CreateSourceLocationRequest = {
            "http_configuration": http_configuration,
            "source_location_name": source_location_name,
        }
        if access_configuration is not None:
            input_["access_configuration"] = access_configuration
        if default_segment_delivery_configuration is not None:
            input_["default_segment_delivery_configuration"] = (
                default_segment_delivery_configuration
            )
        if segment_delivery_configurations is not None:
            input_["segment_delivery_configurations"] = segment_delivery_configurations
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
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.describe_source_location_response.DescribeSourceLocationResponse":
        """<p>Describes a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.describe_source_location_request.DescribeSourceLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.describe_source_location_response.DescribeSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_source_location

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.describe_source_location.async_describe_source_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_source_location_request.DescribeSourceLocationRequest = {
            "source_location_name": source_location_name
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
        http_configuration: "capo_mediatailor.types.http_configuration.HttpConfiguration",
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        access_configuration: Optional[
            "capo_mediatailor.types.access_configuration.AccessConfiguration"
        ] = None,
        default_segment_delivery_configuration: Optional[
            "capo_mediatailor.types.default_segment_delivery_configuration.DefaultSegmentDeliveryConfiguration"
        ] = None,
        segment_delivery_configurations: Optional[
            "capo_mediatailor.types.__list_of_segment_delivery_configuration.__listOfSegmentDeliveryConfiguration"
        ] = None,
    ) -> "capo_mediatailor.types.update_source_location_response.UpdateSourceLocationResponse":
        """<p>Updates a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            access_configuration: <p>Access configuration parameters. Configures the type of authentication used to access content from your source location.</p>
            default_segment_delivery_configuration: <p>The optional configuration for the host server that serves segments.</p>
            http_configuration: <p>The HTTP configuration for the source location.</p>
            segment_delivery_configurations: <p>A list of the segment delivery configurations associated with this resource.</p>
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.update_source_location_request.UpdateSourceLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.update_source_location_response.UpdateSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_source_location

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.update_source_location.async_update_source_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_source_location_request.UpdateSourceLocationRequest = {
            "http_configuration": http_configuration,
            "source_location_name": source_location_name,
        }
        if access_configuration is not None:
            input_["access_configuration"] = access_configuration
        if default_segment_delivery_configuration is not None:
            input_["default_segment_delivery_configuration"] = (
                default_segment_delivery_configuration
            )
        if segment_delivery_configurations is not None:
            input_["segment_delivery_configurations"] = segment_delivery_configurations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_source_location_response.DeleteSourceLocationResponse":
        """<p>Deletes a source location. A source location is a container for sources. For more information about source locations, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/channel-assembly-source-locations.html">Working with source locations</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            source_location_name: <p>The name of the source location.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.delete_source_location_request.DeleteSourceLocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.delete_source_location_response.DeleteSourceLocationResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_source_location

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.delete_source_location.async_delete_source_location(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_source_location_request.DeleteSourceLocationRequest = {
            "source_location_name": source_location_name
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
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_source_locations_response.ListSourceLocationsResponse":
        """<p>Lists the source locations for a channel. A source location defines the host server URL, and contains a list of sources.</p>

        Args:
            max_results: <p> The maximum number of source locations that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> source locations, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListSourceLocations</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.list_source_locations_request.ListSourceLocationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.list_source_locations_response.ListSourceLocationsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_source_locations

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.list_source_locations.async_list_source_locations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_source_locations_request.ListSourceLocationsRequest = {}
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
