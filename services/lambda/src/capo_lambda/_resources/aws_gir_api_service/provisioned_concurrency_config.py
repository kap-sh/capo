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
    import capo_lambda.types.delete_provisioned_concurrency_config_request
    import capo_lambda.types.function_name
    import capo_lambda.types.get_provisioned_concurrency_config_request
    import capo_lambda.types.get_provisioned_concurrency_config_response
    import capo_lambda.types.positive_integer
    import capo_lambda.types.put_provisioned_concurrency_config_request
    import capo_lambda.types.put_provisioned_concurrency_config_response
    import capo_lambda.types.qualifier
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class ProvisionedConcurrencyConfig:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def put(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        provisioned_concurrent_executions: "capo_lambda.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_provisioned_concurrency_config_response.PutProvisionedConcurrencyConfigResponse":
        """<p>Adds a provisioned concurrency configuration to a function's alias or version.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>
            provisioned_concurrent_executions: <p>The amount of provisioned concurrency to allocate for the version or alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To allocate provisioned concurrency
            The following example allocates 100 provisioned concurrency for the BLUE alias of the specified function.

            >>> client.put(function_name='my-function', provisioned_concurrent_executions=100, qualifier='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.put_provisioned_concurrency_config_request.PutProvisionedConcurrencyConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.put_provisioned_concurrency_config_response.PutProvisionedConcurrencyConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_provisioned_concurrency_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.put_provisioned_concurrency_config.put_provisioned_concurrency_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_provisioned_concurrency_config_request.PutProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
            "provisioned_concurrent_executions": provisioned_concurrent_executions,
        }

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
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_provisioned_concurrency_config_response.GetProvisionedConcurrencyConfigResponse":
        """<p>Retrieves the provisioned concurrency configuration for a function's alias or version.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.provisioned_concurrency_config_not_found_exception.ProvisionedConcurrencyConfigNotFoundException: <p>The specified configuration does not exist.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view a provisioned concurrency configuration
            The following example displays details for the provisioned concurrency configuration for the BLUE alias of the specified function.

            >>> client.read(function_name='my-function', qualifier='BLUE')
            To get a provisioned concurrency configuration
            The following example returns details for the provisioned concurrency configuration for the BLUE alias of the specified function.

            >>> client.read(function_name='my-function', qualifier='BLUE')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.get_provisioned_concurrency_config_request.GetProvisionedConcurrencyConfigRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.get_provisioned_concurrency_config_response.GetProvisionedConcurrencyConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_provisioned_concurrency_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.get_provisioned_concurrency_config.get_provisioned_concurrency_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_provisioned_concurrency_config_request.GetProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
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
        function_name: "capo_lambda.types.function_name.FunctionName",
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
    ) -> None:
        """<p>Deletes the provisioned concurrency configuration for a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a provisioned concurrency configuration
            The following example deletes the provisioned concurrency configuration for the GREEN alias of a function named my-function.

            >>> client.delete(function_name='my-function', qualifier='GREEN')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest]",
        ) -> OperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_provisioned_concurrency_config

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.delete_provisioned_concurrency_config.delete_provisioned_concurrency_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output


class AsyncProvisionedConcurrencyConfig:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def put(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        provisioned_concurrent_executions: "capo_lambda.types.positive_integer.PositiveInteger",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.put_provisioned_concurrency_config_response.PutProvisionedConcurrencyConfigResponse":
        """<p>Adds a provisioned concurrency configuration to a function's alias or version.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>
            provisioned_concurrent_executions: <p>The amount of provisioned concurrency to allocate for the version or alias.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To allocate provisioned concurrency
            The following example allocates 100 provisioned concurrency for the BLUE alias of the specified function.

            >>> await client.put(function_name='my-function', provisioned_concurrent_executions=100, qualifier='BLUE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.put_provisioned_concurrency_config_request.PutProvisionedConcurrencyConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.put_provisioned_concurrency_config_response.PutProvisionedConcurrencyConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.put_provisioned_concurrency_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.put_provisioned_concurrency_config.async_put_provisioned_concurrency_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.put_provisioned_concurrency_config_request.PutProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
            "provisioned_concurrent_executions": provisioned_concurrent_executions,
        }

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
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> "capo_lambda.types.get_provisioned_concurrency_config_response.GetProvisionedConcurrencyConfigResponse":
        """<p>Retrieves the provisioned concurrency configuration for a function's alias or version.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.provisioned_concurrency_config_not_found_exception.ProvisionedConcurrencyConfigNotFoundException: <p>The specified configuration does not exist.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To view a provisioned concurrency configuration
            The following example displays details for the provisioned concurrency configuration for the BLUE alias of the specified function.

            >>> await client.read(function_name='my-function', qualifier='BLUE')
            To get a provisioned concurrency configuration
            The following example returns details for the provisioned concurrency configuration for the BLUE alias of the specified function.

            >>> await client.read(function_name='my-function', qualifier='BLUE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.get_provisioned_concurrency_config_request.GetProvisionedConcurrencyConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.get_provisioned_concurrency_config_response.GetProvisionedConcurrencyConfigResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.get_provisioned_concurrency_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.get_provisioned_concurrency_config.async_get_provisioned_concurrency_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.get_provisioned_concurrency_config_request.GetProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
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
        function_name: "capo_lambda.types.function_name.FunctionName",
        qualifier: "capo_lambda.types.qualifier.Qualifier",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
    ) -> None:
        """<p>Deletes the provisioned concurrency configuration for a function.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>my-function</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:my-function</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:my-function</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            qualifier: <p>The version number or alias name.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a provisioned concurrency configuration
            The following example deletes the provisioned concurrency configuration for the GREEN alias of a function named my-function.

            >>> await client.delete(function_name='my-function', qualifier='GREEN')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_lambda._operations.aws_gir_api_service.delete_provisioned_concurrency_config

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.delete_provisioned_concurrency_config.async_delete_provisioned_concurrency_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.delete_provisioned_concurrency_config_request.DeleteProvisionedConcurrencyConfigRequest = {
            "function_name": function_name,
            "qualifier": qualifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output
