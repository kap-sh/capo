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
    import capo_mediatailor.types.aws_service_request_configuration
    import capo_mediatailor.types.concurrent_executor_configuration
    import capo_mediatailor.types.custom_output_configuration
    import capo_mediatailor.types.delete_function_request
    import capo_mediatailor.types.delete_function_response
    import capo_mediatailor.types.function
    import capo_mediatailor.types.function_type
    import capo_mediatailor.types.get_function_request
    import capo_mediatailor.types.get_function_response
    import capo_mediatailor.types.http_request_configuration
    import capo_mediatailor.types.list_functions_request
    import capo_mediatailor.types.list_functions_response
    import capo_mediatailor.types.max_results
    import capo_mediatailor.types.put_function_request
    import capo_mediatailor.types.put_function_response
    import capo_mediatailor.types.sequential_executor_configuration
    import capo_mediatailor.types.vast_request_configuration
    from capo_mediatailor._services.async_media_tailor import (
        AsyncMediaTailorClient,
        AsyncMediaTailorClientConfig,
    )
    from capo_mediatailor._services.media_tailor import (
        MediaTailorClient,
        MediaTailorClientConfig,
    )


class FunctionResource:
    def __init__(self, service: MediaTailorClient) -> None:
        self._service = service

    def put(
        self,
        function_id: "capo_mediatailor.types.__string.__string",
        function_type: "capo_mediatailor.types.function_type.FunctionType",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
        description: Optional["capo_mediatailor.types.__string.__string"] = None,
        http_request_configuration: Optional[
            "capo_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
        ] = None,
        aws_service_request_configuration: Optional[
            "capo_mediatailor.types.aws_service_request_configuration.AwsServiceRequestConfiguration"
        ] = None,
        custom_output_configuration: Optional[
            "capo_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        concurrent_executor_configuration: Optional[
            "capo_mediatailor.types.concurrent_executor_configuration.ConcurrentExecutorConfiguration"
        ] = None,
        sequential_executor_configuration: Optional[
            "capo_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
        ] = None,
        vast_request_configuration: Optional[
            "capo_mediatailor.types.vast_request_configuration.VastRequestConfiguration"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.put_function_response.PutFunctionResponse":
        """<p>Creates or updates a function. A function defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function. The identifier must be unique within your account.</p>
            function_type: <p>The type of the function, which determines what the function can do at runtime. Valid values:</p> <ul> <li> <p> <code>CUSTOM_OUTPUT</code> – Evaluates expressions and produces output bindings with no external calls.</p> </li> <li> <p> <code>HTTP_REQUEST</code> – Makes an HTTP call to an external service and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>AWS_SERVICE_REQUEST</code> – Makes an authenticated request to a supported AWS service API and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>VAST_REQUEST</code> – Calls a VAST endpoint, parses the response as VAST, and makes the parsed ads available to output expressions.</p> </li> <li> <p> <code>SEQUENTIAL_EXECUTOR</code> – Runs a sequence of child functions in order, passing data between steps through temporary data.</p> </li> <li> <p> <code>CONCURRENT_EXECUTOR</code> – Runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>
            description: <p>A description of the function.</p>
            http_request_configuration: <p>The configuration for an <code>HTTP_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>HTTP_REQUEST</code>.</p>
            aws_service_request_configuration: <p>The configuration for an <code>AWS_SERVICE_REQUEST</code> function. You must specify this parameter when <code>FunctionType</code> is <code>AWS_SERVICE_REQUEST</code>.</p>
            custom_output_configuration: <p>The configuration for a <code>CUSTOM_OUTPUT</code> function. Specifies the runtime and output expressions. Required when <code>FunctionType</code> is <code>CUSTOM_OUTPUT</code>.</p>
            concurrent_executor_configuration: <p>The configuration for a <code>CONCURRENT_EXECUTOR</code> function. Specifies the list of child functions to run in parallel, the maximum concurrency, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>CONCURRENT_EXECUTOR</code>.</p>
            sequential_executor_configuration: <p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>SEQUENTIAL_EXECUTOR</code>.</p>
            vast_request_configuration: <p>The configuration for a <code>VAST_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>VAST_REQUEST</code>.</p>
            tags: <p>The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.put_function_request.PutFunctionRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.put_function_response.PutFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.put_function

            output, http_response = (
                capo_mediatailor._operations.media_tailor.put_function.put_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.put_function_request.PutFunctionRequest = {
            "function_id": function_id,
            "function_type": function_type,
        }
        if description is not None:
            input_["description"] = description
        if http_request_configuration is not None:
            input_["http_request_configuration"] = http_request_configuration
        if aws_service_request_configuration is not None:
            input_["aws_service_request_configuration"] = (
                aws_service_request_configuration
            )
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if concurrent_executor_configuration is not None:
            input_["concurrent_executor_configuration"] = (
                concurrent_executor_configuration
            )
        if sequential_executor_configuration is not None:
            input_["sequential_executor_configuration"] = (
                sequential_executor_configuration
            )
        if vast_request_configuration is not None:
            input_["vast_request_configuration"] = vast_request_configuration
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
        function_id: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the configuration and metadata for a function. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.get_function_request.GetFunctionRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_function

            output, http_response = (
                capo_mediatailor._operations.media_tailor.get_function.get_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_function_request.GetFunctionRequest = {
            "function_id": function_id
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
        function_id: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[MediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_function_response.DeleteFunctionResponse":
        """<p>Deletes a function. MediaTailor prevents deletion of a function that is still referenced by a playback configuration or by another function. Remove all references before deleting. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function to delete.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.delete_function_request.DeleteFunctionRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_function

            output, http_response = (
                capo_mediatailor._operations.media_tailor.delete_function.delete_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_function_request.DeleteFunctionRequest = {
            "function_id": function_id
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
    ) -> "capo_mediatailor.types.list_functions_response.ListFunctionsResponse":
        """<p>Retrieves all functions associated with your AWS account in the current Region. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of functions that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> functions, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses token-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListFunctions</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mediatailor.types.list_functions_request.ListFunctionsRequest]",
        ) -> OperationResponse[
            "capo_mediatailor.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_functions

            output, http_response = (
                capo_mediatailor._operations.media_tailor.list_functions.list_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_functions_request.ListFunctionsRequest = {}
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


class AsyncFunctionResource:
    def __init__(self, service: AsyncMediaTailorClient) -> None:
        self._service = service

    async def put(
        self,
        function_id: "capo_mediatailor.types.__string.__string",
        function_type: "capo_mediatailor.types.function_type.FunctionType",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
        description: Optional["capo_mediatailor.types.__string.__string"] = None,
        http_request_configuration: Optional[
            "capo_mediatailor.types.http_request_configuration.HttpRequestConfiguration"
        ] = None,
        aws_service_request_configuration: Optional[
            "capo_mediatailor.types.aws_service_request_configuration.AwsServiceRequestConfiguration"
        ] = None,
        custom_output_configuration: Optional[
            "capo_mediatailor.types.custom_output_configuration.CustomOutputConfiguration"
        ] = None,
        concurrent_executor_configuration: Optional[
            "capo_mediatailor.types.concurrent_executor_configuration.ConcurrentExecutorConfiguration"
        ] = None,
        sequential_executor_configuration: Optional[
            "capo_mediatailor.types.sequential_executor_configuration.SequentialExecutorConfiguration"
        ] = None,
        vast_request_configuration: Optional[
            "capo_mediatailor.types.vast_request_configuration.VastRequestConfiguration"
        ] = None,
        tags: Optional[
            "capo_mediatailor.types.__map_of__string.__mapOf__string"
        ] = None,
    ) -> "capo_mediatailor.types.put_function_response.PutFunctionResponse":
        """<p>Creates or updates a function. A function defines reusable logic that MediaTailor executes at lifecycle hooks during ad insertion. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function. The identifier must be unique within your account.</p>
            function_type: <p>The type of the function, which determines what the function can do at runtime. Valid values:</p> <ul> <li> <p> <code>CUSTOM_OUTPUT</code> – Evaluates expressions and produces output bindings with no external calls.</p> </li> <li> <p> <code>HTTP_REQUEST</code> – Makes an HTTP call to an external service and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>AWS_SERVICE_REQUEST</code> – Makes an authenticated request to a supported AWS service API and evaluates output expressions that can reference the response.</p> </li> <li> <p> <code>VAST_REQUEST</code> – Calls a VAST endpoint, parses the response as VAST, and makes the parsed ads available to output expressions.</p> </li> <li> <p> <code>SEQUENTIAL_EXECUTOR</code> – Runs a sequence of child functions in order, passing data between steps through temporary data.</p> </li> <li> <p> <code>CONCURRENT_EXECUTOR</code> – Runs a set of child functions in parallel, up to a maximum concurrency, and combines their output when all functions complete.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions-types.html">Function types and composition</a> in the <i>MediaTailor User Guide</i>.</p>
            description: <p>A description of the function.</p>
            http_request_configuration: <p>The configuration for an <code>HTTP_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>HTTP_REQUEST</code>.</p>
            aws_service_request_configuration: <p>The configuration for an <code>AWS_SERVICE_REQUEST</code> function. You must specify this parameter when <code>FunctionType</code> is <code>AWS_SERVICE_REQUEST</code>.</p>
            custom_output_configuration: <p>The configuration for a <code>CUSTOM_OUTPUT</code> function. Specifies the runtime and output expressions. Required when <code>FunctionType</code> is <code>CUSTOM_OUTPUT</code>.</p>
            concurrent_executor_configuration: <p>The configuration for a <code>CONCURRENT_EXECUTOR</code> function. Specifies the list of child functions to run in parallel, the maximum concurrency, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>CONCURRENT_EXECUTOR</code>.</p>
            sequential_executor_configuration: <p>The configuration for a <code>SEQUENTIAL_EXECUTOR</code> function. Specifies the ordered list of child functions to execute, an optional output block, and a timeout. Required when <code>FunctionType</code> is <code>SEQUENTIAL_EXECUTOR</code>.</p>
            vast_request_configuration: <p>The configuration for a <code>VAST_REQUEST</code> function. Specifies the HTTP method, URL, headers, body, timeout, and output expressions. Required when <code>FunctionType</code> is <code>VAST_REQUEST</code>.</p>
            tags: <p>The tags to assign to the function. Tags are key-value pairs that you can associate with Amazon resources to help with organization, access control, and cost tracking. For more information, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/tagging.html">Tagging AWS Elemental MediaTailor Resources</a>.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.put_function_request.PutFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.put_function_response.PutFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.put_function

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.put_function.async_put_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.put_function_request.PutFunctionRequest = {
            "function_id": function_id,
            "function_type": function_type,
        }
        if description is not None:
            input_["description"] = description
        if http_request_configuration is not None:
            input_["http_request_configuration"] = http_request_configuration
        if aws_service_request_configuration is not None:
            input_["aws_service_request_configuration"] = (
                aws_service_request_configuration
            )
        if custom_output_configuration is not None:
            input_["custom_output_configuration"] = custom_output_configuration
        if concurrent_executor_configuration is not None:
            input_["concurrent_executor_configuration"] = (
                concurrent_executor_configuration
            )
        if sequential_executor_configuration is not None:
            input_["sequential_executor_configuration"] = (
                sequential_executor_configuration
            )
        if vast_request_configuration is not None:
            input_["vast_request_configuration"] = vast_request_configuration
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
        function_id: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.get_function_response.GetFunctionResponse":
        """<p>Retrieves the configuration and metadata for a function. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.get_function_request.GetFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.get_function_response.GetFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.get_function

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.get_function.async_get_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.get_function_request.GetFunctionRequest = {
            "function_id": function_id
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
        function_id: "capo_mediatailor.types.__string.__string",
        *,
        config_overrides: Optional[AsyncMediaTailorClientConfig] = None,
    ) -> "capo_mediatailor.types.delete_function_response.DeleteFunctionResponse":
        """<p>Deletes a function. MediaTailor prevents deletion of a function that is still referenced by a playback configuration or by another function. Remove all references before deleting. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            function_id: <p>The identifier of the function to delete.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.delete_function_request.DeleteFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.delete_function_response.DeleteFunctionResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.delete_function

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.delete_function.async_delete_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.delete_function_request.DeleteFunctionRequest = {
            "function_id": function_id
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
    ) -> "capo_mediatailor.types.list_functions_response.ListFunctionsResponse":
        """<p>Retrieves all functions associated with your AWS account in the current Region. For more information about functions, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/monetization-functions.html">Working with functions</a> in the <i>MediaTailor User Guide</i>.</p>

        Args:
            max_results: <p>The maximum number of functions that you want MediaTailor to return in response to the current request. If there are more than <code>MaxResults</code> functions, use the value of <code>NextToken</code> in the response to get the next page of results.</p> <p>The default value is 100. MediaTailor uses token-based pagination, which means that a response might contain fewer than <code>MaxResults</code> items, including 0 items, even when more results are available. To retrieve all results, you must continue making requests using the <code>NextToken</code> value from each response until the response no longer includes a <code>NextToken</code> value.</p>
            next_token: <p>Pagination token returned by the list request when results exceed the maximum allowed. Use the token to fetch the next page of results.</p> <p>For the first <code>ListFunctions</code> request, omit this value. For subsequent requests, get the value of <code>NextToken</code> from the previous response and specify that value for <code>NextToken</code> in the request. Continue making requests until the response no longer includes a <code>NextToken</code> value, which indicates that all results have been retrieved.</p>

        Raises:
            capo_mediatailor.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_mediatailor.types.list_functions_request.ListFunctionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_mediatailor.types.list_functions_response.ListFunctionsResponse"
        ]:
            import capo_mediatailor._operations.media_tailor.list_functions

            (
                output,
                http_response,
            ) = await capo_mediatailor._operations.media_tailor.list_functions.async_list_functions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_mediatailor.types.list_functions_request.ListFunctionsRequest = {}
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
