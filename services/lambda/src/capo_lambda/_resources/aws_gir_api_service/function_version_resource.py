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
    import capo_lambda.types.description
    import capo_lambda.types.function_configuration
    import capo_lambda.types.function_name
    import capo_lambda.types.function_version_latest_published
    import capo_lambda.types.list_versions_by_function_request
    import capo_lambda.types.list_versions_by_function_response
    import capo_lambda.types.max_list_items
    import capo_lambda.types.namespaced_function_name
    import capo_lambda.types.publish_version_request
    import capo_lambda.types.string
    from capo_lambda._services._lambda import LambdaClient, LambdaClientConfig
    from capo_lambda._services.async__lambda import (
        AsyncLambdaClient,
        AsyncLambdaClientConfig,
    )


class FunctionVersionResource:
    def __init__(self, service: LambdaClient) -> None:
        self._service = service

    def create(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        code_sha256: Optional["capo_lambda.types.string.String"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        """<p>Creates a <a href="https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html">version</a> from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change.</p> <p>Lambda doesn't publish a version if the function's configuration and code haven't changed since the last version. Use <a>UpdateFunctionCode</a> or <a>UpdateFunctionConfiguration</a> to update the function before publishing a version.</p> <p>Clients can invoke versions directly or with an alias. To create an alias, use <a>CreateAlias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            code_sha256: <p>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of <a>UpdateFunctionCode</a>.</p>
            description: <p>A description for the version to override the description in the function configuration.</p>
            revision_id: <p>Only update the function if the revision ID matches the ID that's specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>

        Raises:
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException: <p>The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To publish a version of a Lambda function
            This operation publishes a version of a Lambda function

            >>> client.create(code_sha256='', description='', function_name='myFunction')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.publish_version_request.PublishVersionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.publish_version

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.publish_version.publish_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.publish_version_request.PublishVersionRequest = {
            "function_name": function_name
        }
        if code_sha256 is not None:
            input_["code_sha256"] = code_sha256
        if description is not None:
            input_["description"] = description
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if publish_to is not None:
            input_["publish_to"] = publish_to

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_versions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[LambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html">versions</a>, with the version-specific configuration of each. Lambda returns up to 50 versions per call.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of versions to return. Note that <code>ListVersionsByFunction</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list versions of a function
            The following example returns a list of versions of a function named my-function

            >>> client.list_versions_by_function(function_name='my-function')
        """

        def _handler(
            req: "OperationRequest[capo_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest]",
        ) -> OperationResponse[
            "capo_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_versions_by_function

            output, http_response = (
                capo_lambda._operations.aws_gir_api_service.list_versions_by_function.list_versions_by_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest = {
            "function_name": function_name
        }
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


class AsyncFunctionVersionResource:
    def __init__(self, service: AsyncLambdaClient) -> None:
        self._service = service

    async def create(
        self,
        function_name: "capo_lambda.types.function_name.FunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        code_sha256: Optional["capo_lambda.types.string.String"] = None,
        description: Optional["capo_lambda.types.description.Description"] = None,
        revision_id: Optional["capo_lambda.types.string.String"] = None,
        publish_to: Optional[
            "capo_lambda.types.function_version_latest_published.FunctionVersionLatestPublished"
        ] = None,
    ) -> "capo_lambda.types.function_configuration.FunctionConfiguration":
        """<p>Creates a <a href="https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html">version</a> from the current code and configuration of a function. Use versions to create a snapshot of your function code and configuration that doesn't change.</p> <p>Lambda doesn't publish a version if the function's configuration and code haven't changed since the last version. Use <a>UpdateFunctionCode</a> or <a>UpdateFunctionConfiguration</a> to update the function before publishing a version.</p> <p>Clients can invoke versions directly or with an alias. To create an alias, use <a>CreateAlias</a>.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            code_sha256: <p>Only publish a version if the hash value matches the value that's specified. Use this option to avoid publishing a version if the function code has changed since you last updated it. You can get the hash for the version that you uploaded from the output of <a>UpdateFunctionCode</a>.</p>
            description: <p>A description for the version to override the description in the function configuration.</p>
            revision_id: <p>Only update the function if the revision ID matches the ID that's specified. Use this option to avoid publishing a version if the function configuration has changed since you last updated it.</p>
            publish_to: <p>Specifies where to publish the function version or configuration.</p>

        Raises:
            capo_lambda.errors.code_storage_exceeded_exception.CodeStorageExceededException: <p>Your Amazon Web Services account has exceeded its maximum total code size. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.function_versions_per_capacity_provider_limit_exceeded_exception.FunctionVersionsPerCapacityProviderLimitExceededException: <p>The maximum number of function versions that can be associated with a single capacity provider has been exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html">Lambda quotas</a>.</p>
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.precondition_failed_exception.PreconditionFailedException: <p>The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.</p> <ul> <li> <p> <b>For AddPermission and RemovePermission API operations:</b> Call <code>GetPolicy</code> to retrieve the latest RevisionId for your resource.</p> </li> <li> <p> <b>For all other API operations:</b> Call <code>GetFunction</code> or <code>GetAlias</code> to retrieve the latest RevisionId for your resource.</p> </li> </ul>
            capo_lambda.errors.resource_conflict_exception.ResourceConflictException: <p>The resource already exists, or another operation is in progress.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To publish a version of a Lambda function
            This operation publishes a version of a Lambda function

            >>> await client.create(code_sha256='', description='', function_name='myFunction')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.publish_version_request.PublishVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.function_configuration.FunctionConfiguration"
        ]:
            import capo_lambda._operations.aws_gir_api_service.publish_version

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.publish_version.async_publish_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.publish_version_request.PublishVersionRequest = {
            "function_name": function_name
        }
        if code_sha256 is not None:
            input_["code_sha256"] = code_sha256
        if description is not None:
            input_["description"] = description
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if publish_to is not None:
            input_["publish_to"] = publish_to

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_versions_by_function(
        self,
        function_name: "capo_lambda.types.namespaced_function_name.NamespacedFunctionName",
        *,
        config_overrides: Optional[AsyncLambdaClientConfig] = None,
        marker: Optional["capo_lambda.types.string.String"] = None,
        max_items: Optional["capo_lambda.types.max_list_items.MaxListItems"] = None,
    ) -> "capo_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse":
        """<p>Returns a list of <a href="https://docs.aws.amazon.com/lambda/latest/dg/versioning-aliases.html">versions</a>, with the version-specific configuration of each. Lambda returns up to 50 versions per call.</p>

        Args:
            function_name: <p>The name or ARN of the Lambda function.</p> <p class="title"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> - <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> - <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Partial ARN</b> - <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.</p>
            marker: <p>Specify the pagination token that's returned by a previous request to retrieve the next page of results.</p>
            max_items: <p>The maximum number of versions to return. Note that <code>ListVersionsByFunction</code> returns a maximum of 50 items in each response, even if you set the number higher.</p>

        Raises:
            capo_lambda.errors.invalid_parameter_value_exception.InvalidParameterValueException: <p>One of the parameters in the request is not valid.</p>
            capo_lambda.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_lambda.errors.service_exception.ServiceException: <p>The Lambda service encountered an internal error.</p>
            capo_lambda.errors.too_many_requests_exception.TooManyRequestsException: <p>The request throughput limit was exceeded. For more information, see <a href="https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests">Lambda quotas</a>.</p>
            capo_lambda.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list versions of a function
            The following example returns a list of versions of a function named my-function

            >>> await client.list_versions_by_function(function_name='my-function')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest]",
        ) -> AsyncOperationResponse[
            "capo_lambda.types.list_versions_by_function_response.ListVersionsByFunctionResponse"
        ]:
            import capo_lambda._operations.aws_gir_api_service.list_versions_by_function

            (
                output,
                http_response,
            ) = await capo_lambda._operations.aws_gir_api_service.list_versions_by_function.async_list_versions_by_function(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: capo_lambda.types.list_versions_by_function_request.ListVersionsByFunctionRequest = {
            "function_name": function_name
        }
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
