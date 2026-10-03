from __future__ import annotations

from typing import TYPE_CHECKING, Optional

import capo_lambda._auth._signers
import capo_lambda._auth._sigv4
from capo_lambda._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import capo_lambda.types.alias
    import capo_lambda.types.alias_configuration
    import capo_lambda.types.alias_routing_configuration
    import capo_lambda.types.create_alias_request
    import capo_lambda.types.delete_alias_request
    import capo_lambda.types.description
    import capo_lambda.types.function_name
    import capo_lambda.types.get_alias_request
    import capo_lambda.types.list_aliases_request
    import capo_lambda.types.list_aliases_response
    import capo_lambda.types.max_list_items
    import capo_lambda.types.string
    import capo_lambda.types.update_alias_request
    import capo_lambda.types.version_with_latest_published
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class FunctionAlias:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def put(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        function_version: "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        routing_config: Optional[
            "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
        ] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        """<p>Creates an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a> for a Lambda function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version.</p> <p>You can also map an alias to split invocation requests between two versions. Use the <code>RoutingConfig</code> parameter to specify a second version and the percentage of invocation requests that it receives.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>
            function_version: <p>The function version that the alias invokes.</p>
            description: <p>A description of the alias.</p>
            routing_config: <p>The <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing">routing configuration</a> of the alias.</p>

        Raises:
            capo_lambda.errors.alias_limit_exceeded_exception.AliasLimitExceededException: <p>Lambda couldn't create the alias because your Amazon Web Services account has exceeded the maximum number of aliases allowed per Lambda function. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an alias for a Lambda function
            The following example creates an alias named LIVE that points to version 1 of the my-function Lambda function.

            >>> client.put(description='alias for live version of function', function_name='my-function', function_version='1', name='LIVE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.create_alias_request.CreateAliasRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.create_alias.create_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_alias_request.CreateAliasRequest = {
            "function_name": function_name,
            "name": name,
            "function_version": function_version,
        }
        if description is not None:
            input_["description"] = description
        if routing_config is not None:
            input_["routing_config"] = routing_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def read(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        """<p>Returns details about a Lambda function <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function alias
            The following example returns details about an alias named BLUE for a function named my-function

            >>> client.read(function_name='my-function', name='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_alias_request.GetAliasRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_alias.get_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_alias_request.GetAliasRequest = {
            "function_name": function_name,
            "name": name,
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
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_version: Optional[
            "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
        ] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        routing_config: Optional[
            "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        """<p>Updates the configuration of a Lambda function <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>
            function_version: <p>The function version that the alias invokes.</p>
            description: <p>A description of the alias.</p>
            routing_config: <p>The <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing">routing configuration</a> of the alias.</p>
            revision_id: <p>Only update the alias if the revision ID matches the ID that's specified. Use this option to avoid modifying an alias that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a function alias
            The following example updates the alias named BLUE to send 30% of traffic to version 2 and 70% to version 1.

            >>> client.update(function_name='my-function', function_version='2', name='BLUE', routing_config={'AdditionalVersionWeights': {'1': 0.7}})
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.update_alias_request.UpdateAliasRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.update_alias.update_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_alias_request.UpdateAliasRequest = {
            "function_name": function_name,
            "name": name,
        }
        if function_version is not None:
            input_["function_version"] = function_version
        if description is not None:
            input_["description"] = description
        if routing_config is not None:
            input_["routing_config"] = routing_config
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        """<p>Deletes a Lambda function <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a Lambda function alias
            The following example deletes an alias named BLUE from a function named my-function

            >>> client.delete(function_name='my-function', name='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_alias_request.DeleteAliasRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_alias

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_alias.delete_alias(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_alias_request.DeleteAliasRequest = {
            "function_name": function_name,
            "name": name,
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
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        function_version: Optional[
            "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_aliases_response.ListAliasesResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">aliases</a> for a Lambda function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            function_version: <p>Specify a function version to only list aliases that invoke that version.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Limit the number of aliases returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list a function's aliases
            The following example returns a list of aliases for a function named my-function.

            >>> client.list(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_aliases_request.ListAliasesRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_aliases_response.ListAliasesResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_aliases

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_aliases.list_aliases(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_aliases_request.ListAliasesRequest = {
            "function_name": function_name
        }
        if function_version is not None:
            input_["function_version"] = function_version
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncFunctionAlias:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def put(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        function_version: "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        routing_config: Optional[
            "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
        ] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        """<p>Creates an <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a> for a Lambda function version. Use aliases to provide clients with a function identifier that you can update to invoke a different version.</p> <p>You can also map an alias to split invocation requests between two versions. Use the <code>RoutingConfig</code> parameter to specify a second version and the percentage of invocation requests that it receives.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>
            function_version: <p>The function version that the alias invokes.</p>
            description: <p>A description of the alias.</p>
            routing_config: <p>The <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing">routing configuration</a> of the alias.</p>

        Raises:
            capo_lambda.errors.alias_limit_exceeded_exception.AliasLimitExceededException: <p>Lambda couldn't create the alias because your Amazon Web Services account has exceeded the maximum number of aliases allowed per Lambda function. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create an alias for a Lambda function
            The following example creates an alias named LIVE that points to version 1 of the my-function Lambda function.

            >>> await client.put(description='alias for live version of function', function_name='my-function', function_version='1', name='LIVE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.create_alias_request.CreateAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.create_alias

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.create_alias.async_create_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.create_alias_request.CreateAliasRequest = {
            "function_name": function_name,
            "name": name,
            "function_version": function_version,
        }
        if description is not None:
            input_["description"] = description
        if routing_config is not None:
            input_["routing_config"] = routing_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def read(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        """<p>Returns details about a Lambda function <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a Lambda function alias
            The following example returns details about an alias named BLUE for a function named my-function

            >>> await client.read(function_name='my-function', name='BLUE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_alias_request.GetAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_alias

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_alias.async_get_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_alias_request.GetAliasRequest = {
            "function_name": function_name,
            "name": name,
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
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        function_version: Optional[
            "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
        ] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        routing_config: Optional[
            "capo_lambda.types.alias_routing_configuration.AliasRoutingConfiguration"
        ] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
    ) -> "capo_lambda.types.alias_configuration.AliasConfiguration":
        """<p>Updates the configuration of a Lambda function <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>
            function_version: <p>The function version that the alias invokes.</p>
            description: <p>A description of the alias.</p>
            routing_config: <p>The <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing">routing configuration</a> of the alias.</p>
            revision_id: <p>Only update the alias if the revision ID matches the ID that's specified. Use this option to avoid modifying an alias that has changed since you last read it.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To update a function alias
            The following example updates the alias named BLUE to send 30% of traffic to version 2 and 70% to version 1.

            >>> await client.update(function_name='my-function', function_version='2', name='BLUE', routing_config={'AdditionalVersionWeights': {'1': 0.7}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.update_alias_request.UpdateAliasRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.alias_configuration.AliasConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.update_alias

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.update_alias.async_update_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.update_alias_request.UpdateAliasRequest = {
            "function_name": function_name,
            "name": name,
        }
        if function_version is not None:
            input_["function_version"] = function_version
        if description is not None:
            input_["description"] = description
        if routing_config is not None:
            input_["routing_config"] = routing_config
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        name: "capo_lambda.types.alias.Alias",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> None:
        """<p>Deletes a Lambda function <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">alias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            name: <p>The name of the alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a Lambda function alias
            The following example deletes an alias named BLUE from a function named my-function

            >>> await client.delete(function_name='my-function', name='BLUE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_alias_request.DeleteAliasRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_alias

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_alias.async_delete_alias(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_alias_request.DeleteAliasRequest = {
            "function_name": function_name,
            "name": name,
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
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        function_version: Optional[
            "capo_lambda.types.version_with_latest_published.VersionWithLatestPublished"
        ] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_aliases_response.ListAliasesResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html">aliases</a> for a Lambda function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            function_version: <p>Specify a function version to only list aliases that invoke that version.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>Limit the number of aliases returned.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list a function's aliases
            The following example returns a list of aliases for a function named my-function.

            >>> await client.list(function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_aliases_request.ListAliasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_aliases_response.ListAliasesResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_aliases

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_aliases.async_list_aliases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_aliases_request.ListAliasesRequest = {
            "function_name": function_name
        }
        if function_version is not None:
            input_["function_version"] = function_version
        if marker is not None:
            input_["marker"] = marker
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
