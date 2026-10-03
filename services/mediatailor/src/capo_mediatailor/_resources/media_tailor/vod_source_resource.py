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
    import capo_mediatailor.types.__map_of__string
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.create_vod_source_request
    import capo_mediatailor.types.create_vod_source_response
    import capo_mediatailor.types.delete_vod_source_request
    import capo_mediatailor.types.delete_vod_source_response
    import capo_mediatailor.types.describe_vod_source_request
    import capo_mediatailor.types.describe_vod_source_response
    import capo_mediatailor.types.http_package_configurations
    import capo_mediatailor.types.list_vod_sources_request
    import capo_mediatailor.types.list_vod_sources_response
    import capo_mediatailor.types.max_results
    import capo_mediatailor.types.update_vod_source_request
    import capo_mediatailor.types.update_vod_source_response
    import capo_mediatailor.types.vod_source
    from capo_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from capo_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class VodSourceResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_vod_source_response.CreateVodSourceResponse":
        """<p>The VOD source configuration parameters.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this VOD source.</p>
            source_location_name: <p>The name of the source location for this VOD source.</p>
            tags: <p>The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            vod_source_name: <p>The name associated with the VOD source.&gt;</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.create_vod_source_request.CreateVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.create_vod_source_response.CreateVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.create_vod_source.create_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_vod_source_request.CreateVodSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }
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
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> (
        "capo_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
    ):
        """<p>Provides details about a specific video on demand (VOD) source in a specific source location.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD Source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.describe_vod_source.describe_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest = {
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
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
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse":
        """<p>Updates a VOD source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the VOD source on this account.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.update_vod_source.update_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }

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
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse":
        """<p>The video on demand (VOD) source to delete.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_vod_source

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_vod_source.delete_vod_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest = {
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
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
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse":
        """<p>Lists the VOD sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p> The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> VOD sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListVodSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source list.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_vod_sources

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_vod_sources.list_vod_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest = {
            "source_location_name": source_location_name
        }
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


class AsyncVodSourceResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.create_vod_source_response.CreateVodSourceResponse":
        """<p>The VOD source configuration parameters.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configuration parameters for this VOD source.</p>
            source_location_name: <p>The name of the source location for this VOD source.</p>
            tags: <p>The tags to assign to the VOD source. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>
            vod_source_name: <p>The name associated with the VOD source.&gt;</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.create_vod_source_request.CreateVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.create_vod_source_response.CreateVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.create_vod_source

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.create_vod_source.async_create_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.create_vod_source_request.CreateVodSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }
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
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> (
        "capo_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
    ):
        """<p>Provides details about a specific video on demand (VOD) source in a specific source location.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD Source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.describe_vod_source_response.DescribeVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.describe_vod_source

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.describe_vod_source.async_describe_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.describe_vod_source_request.DescribeVodSourceRequest = {
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
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
        http_package_configurations: "capo_mediatailor.types.http_package_configurations.HttpPackageConfigurations",
        source_location_name: "capo_mediatailor.types.__string.__string",
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse":
        """<p>Updates a VOD source's configuration.</p>

        Args:
            http_package_configurations: <p>A list of HTTP package configurations for the VOD source on this account.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.update_vod_source_response.UpdateVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.update_vod_source

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.update_vod_source.async_update_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.update_vod_source_request.UpdateVodSourceRequest = {
            "http_package_configurations": http_package_configurations,
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
        }

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
        vod_source_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse":
        """<p>The video on demand (VOD) source to delete.</p>

        Args:
            source_location_name: <p>The name of the source location associated with this VOD Source.</p>
            vod_source_name: <p>The name of the VOD source.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.delete_vod_source_response.DeleteVodSourceResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_vod_source

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.delete_vod_source.async_delete_vod_source(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_vod_source_request.DeleteVodSourceRequest = {
            "source_location_name": source_location_name,
            "vod_source_name": vod_source_name,
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
        source_location_name: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        max_results: Optional["capo_mediatailor.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_mediatailor.types.__string.__string"] = None,
    ) -> "capo_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse":
        """<p>Lists the VOD sources contained in a source location. A source represents a piece of content.</p>

        Args:
            max_results: <p> The maximum number of VOD sources that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> VOD sources, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses DynamoDB-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListVodSources</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>
            source_location_name: <p>The name of the source location associated with this VOD Source list.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.list_vod_sources_response.ListVodSourcesResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_vod_sources

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.list_vod_sources.async_list_vod_sources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_vod_sources_request.ListVodSourcesRequest = {
            "source_location_name": source_location_name
        }
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
