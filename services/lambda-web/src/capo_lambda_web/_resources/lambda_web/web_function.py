from __future__ import annotations

from typing import TYPE_CHECKING, Any, Optional

import capo_lambda_web._auth._signers
import capo_lambda_web._auth._sigv4
from capo_lambda_web._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationLogging,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda_web.types.create_web_function_request
    import capo_lambda_web.types.create_web_function_response
    import capo_lambda_web.types.delete_web_function_request
    import capo_lambda_web.types.endpoint_config
    import capo_lambda_web.types.filter_list
    import capo_lambda_web.types.function_name
    import capo_lambda_web.types.function_summary
    import capo_lambda_web.types.get_web_function_request
    import capo_lambda_web.types.get_web_function_response
    import capo_lambda_web.types.list_web_functions_request
    import capo_lambda_web.types.list_web_functions_response
    import capo_lambda_web.types.max_results
    import capo_lambda_web.types.next_token
    import capo_lambda_web.types.revision_config
    import capo_lambda_web.types.tags
    from capo_lambda_web._services.async_lambda_web import (
        AsyncLambdaWebClient,
        AsyncLambdaWebClientConfig,
    )
    from capo_lambda_web._services.lambda_web import (
        LambdaWebClient,
        LambdaWebClientConfig,
    )


class WebFunction:
    def __init__(self, service: LambdaWebClient) -> None:
        self._service = service

    def put(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaWebClientConfig] = None,
        revision_config: Optional[
            "capo_lambda_web.types.revision_config.RevisionConfig"
        ] = None,
        endpoint_config: Optional[
            "capo_lambda_web.types.endpoint_config.EndpointConfig"
        ] = None,
        tags: Optional["capo_lambda_web.types.tags.Tags"] = None,
    ) -> "capo_lambda_web.types.create_web_function_response.CreateWebFunctionResponse":
        """<p>Creates a web function with an initial revision and endpoint. To create a web function, you provide the function name, revision configuration (code and service settings), and endpoint configuration.</p> <p>To use this operation, you must have the <code>CreateWebFunction</code> permission on the web function. You don't need separate permissions for the initial revision or endpoint.</p>

        Args:
            function_name: <p>The name of the web function. The name can contain letters, numbers, hyphens (-), and underscores (_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.</p>
            revision_config: <p>The configuration for the initial revision of the web function, including code and service settings.</p>
            endpoint_config: <p>The configuration for the initial endpoint of the web function.</p>
            tags: <p>A map of tag keys and values to apply to the web function.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda_web.types.create_web_function_response.CreateWebFunctionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.create_web_function

            output, http_response = (
                capo_lambda_web._operations.lambda_web.create_web_function.create_web_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest",
        ) -> dict[str, Any]:
            import capo_lambda_web.types.create_web_function_request

            return capo_lambda_web.types.create_web_function_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateWebFunction", redact_input=_redact_input),
        )
        input_: capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest = {
            "function_name": function_name
        }
        if revision_config is not None:
            input_["revision_config"] = revision_config
        if endpoint_config is not None:
            input_["endpoint_config"] = endpoint_config
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
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaWebClientConfig] = None,
    ) -> "capo_lambda_web.types.get_web_function_response.GetWebFunctionResponse":
        """<p>Retrieves details about a web function, including its current state and configuration.</p>

        Args:
            function_name: <p>The web function to retrieve.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_web.types.get_web_function_request.GetWebFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda_web.types.get_web_function_response.GetWebFunctionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.get_web_function

            output, http_response = (
                capo_lambda_web._operations.lambda_web.get_web_function.get_web_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWebFunction")
        )
        input_: capo_lambda_web.types.get_web_function_request.GetWebFunctionRequest = {
            "function_name": function_name
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
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaWebClientConfig] = None,
    ) -> None:
        """<p>Deletes a web function and all of its associated revisions and endpoints.</p> <p>To use this operation, you must have the <code>DeleteWebFunction</code> permission on the web function. You don't need the <code>DeleteWebFunctionRevision</code> or <code>DeleteWebFunctionEndpoint</code> permission.</p>

        Args:
            function_name: <p>The web function to delete.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_web.types.delete_web_function_request.DeleteWebFunctionRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.delete_web_function

            output, http_response = (
                capo_lambda_web._operations.lambda_web.delete_web_function.delete_web_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWebFunction")
        )
        input_: capo_lambda_web.types.delete_web_function_request.DeleteWebFunctionRequest = {
            "function_name": function_name
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
        config_overrides: Optional[LambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "capo_lambda_web.types.list_web_functions_response.ListWebFunctionsResponse":
        """<p>Lists web functions in your account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            filters: <p>A list of filters to apply to the results. The only supported filter name is <code>state</code>. If you don't specify a filter, the operation returns all web functions.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.</p>
            next_token: <p>The pagination token that's returned by a previous request to retrieve the next page of results.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_lambda_web.types.list_web_functions_request.ListWebFunctionsRequest]",
        ) -> OperationResponse[
            "capo_lambda_web.types.list_web_functions_response.ListWebFunctionsResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.list_web_functions

            output, http_response = (
                capo_lambda_web._operations.lambda_web.list_web_functions.list_web_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWebFunctions")
        )
        input_: capo_lambda_web.types.list_web_functions_request.ListWebFunctionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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


class AsyncWebFunction:
    def __init__(self, service: AsyncLambdaWebClient) -> None:
        self._service = service

    async def put(
        self,
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        revision_config: Optional[
            "capo_lambda_web.types.revision_config.RevisionConfig"
        ] = None,
        endpoint_config: Optional[
            "capo_lambda_web.types.endpoint_config.EndpointConfig"
        ] = None,
        tags: Optional["capo_lambda_web.types.tags.Tags"] = None,
    ) -> "capo_lambda_web.types.create_web_function_response.CreateWebFunctionResponse":
        """<p>Creates a web function with an initial revision and endpoint. To create a web function, you provide the function name, revision configuration (code and service settings), and endpoint configuration.</p> <p>To use this operation, you must have the <code>CreateWebFunction</code> permission on the web function. You don't need separate permissions for the initial revision or endpoint.</p>

        Args:
            function_name: <p>The name of the web function. The name can contain letters, numbers, hyphens (-), and underscores (_), and can't begin or end with a hyphen or an underscore. The name is limited to 64 characters in length.</p>
            revision_config: <p>The configuration for the initial revision of the web function, including code and service settings.</p>
            endpoint_config: <p>The configuration for the initial endpoint of the web function.</p>
            tags: <p>A map of tag keys and values to apply to the web function.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota, such as the maximum number of web functions in your account or the maximum number of revisions or endpoints per web function. Request a quota increase or reduce usage and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.create_web_function_response.CreateWebFunctionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.create_web_function

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.create_web_function.async_create_web_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        def _redact_input(
            input_: "capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest",
        ) -> dict[str, Any]:
            import capo_lambda_web.types.create_web_function_request

            return capo_lambda_web.types.create_web_function_request.redact_sensitive(
                input_
            )

        interceptors_, options_ = self._service.operation_options(
            config_overrides,
            OperationLogging("CreateWebFunction", redact_input=_redact_input),
        )
        input_: capo_lambda_web.types.create_web_function_request.CreateWebFunctionRequest = {
            "function_name": function_name
        }
        if revision_config is not None:
            input_["revision_config"] = revision_config
        if endpoint_config is not None:
            input_["endpoint_config"] = endpoint_config
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
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> "capo_lambda_web.types.get_web_function_response.GetWebFunctionResponse":
        """<p>Retrieves details about a web function, including its current state and configuration.</p>

        Args:
            function_name: <p>The web function to retrieve.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.get_web_function_request.GetWebFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.get_web_function_response.GetWebFunctionResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.get_web_function

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.get_web_function.async_get_web_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("GetWebFunction")
        )
        input_: capo_lambda_web.types.get_web_function_request.GetWebFunctionRequest = {
            "function_name": function_name
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
        function_name: "capo_lambda_web.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
    ) -> None:
        """<p>Deletes a web function and all of its associated revisions and endpoints.</p> <p>To use this operation, you must have the <code>DeleteWebFunction</code> permission on the web function. You don't need the <code>DeleteWebFunctionRevision</code> or <code>DeleteWebFunctionEndpoint</code> permission.</p>

        Args:
            function_name: <p>The web function to delete.</p> <p>You can specify either of the following:</p> <ul> <li> <p>The function name, for example <code>my-function</code>.</p> </li> <li> <p>The function ARN.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource. For example, the resource is being modified by another request, you tried to delete a revision that is serving traffic on an endpoint, or the policy revision ID that you specified doesn't match the current policy. Resolve the conflict and try again.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified web function, revision, endpoint, or resource-based policy doesn't exist. Verify the resource identifier and try again.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.delete_web_function_request.DeleteWebFunctionRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda_web._operations.lambda_web.delete_web_function

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.delete_web_function.async_delete_web_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("DeleteWebFunction")
        )
        input_: capo_lambda_web.types.delete_web_function_request.DeleteWebFunctionRequest = {
            "function_name": function_name
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
        config_overrides: Optional[AsyncLambdaWebClientConfig] = None,
        filters: Optional["capo_lambda_web.types.filter_list.FilterList"] = None,
        max_results: Optional["capo_lambda_web.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_lambda_web.types.next_token.NextToken"] = None,
    ) -> "capo_lambda_web.types.list_web_functions_response.ListWebFunctionsResponse":
        """<p>Lists web functions in your account. Use pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            filters: <p>A list of filters to apply to the results. The only supported filter name is <code>state</code>. If you don't specify a filter, the operation returns all web functions.</p>
            max_results: <p>The maximum number of results to return in a single call. Minimum value of 1, maximum value of 50. Default is 50.</p>
            next_token: <p>The pagination token that's returned by a previous request to retrieve the next page of results.</p>

        Raises:
            capo_lambda_web.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform this operation. Check the IAM policies for your identity and any resource-based policy on the web function.</p>
            capo_lambda_web.errors.internal_server_exception.InternalServerException: <p>The request failed because of an internal error in the service. Retry the request. If the error persists, open a support case.</p>
            capo_lambda_web.errors.throttling_exception.ThrottlingException: <p>The request was denied because it exceeded the request rate that Lambda allows for your account. Reduce the frequency of requests and retry with exponential backoff.</p>
            capo_lambda_web.errors.validation_exception.ValidationException: <p>The request failed validation because a parameter was missing, malformed, or outside the allowed range. Check the request parameters and try again.</p>
            capo_lambda_web.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda_web.types.list_web_functions_request.ListWebFunctionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda_web.types.list_web_functions_response.ListWebFunctionsResponse"
        ]:
            import capo_lambda_web._operations.lambda_web.list_web_functions

            (
                output,
                http_response,
            ) = await capo_lambda_web._operations.lambda_web.list_web_functions.async_list_web_functions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(
            config_overrides, OperationLogging("ListWebFunctions")
        )
        input_: capo_lambda_web.types.list_web_functions_request.ListWebFunctionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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
