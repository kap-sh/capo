"""Generated from Smithy shape ``com.amazonaws.sagemakera2iruntime#AmazonSageMakerA2IRuntime``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_sagemaker_a2i_runtime._auth._signers
import capo_sagemaker_a2i_runtime._auth._sigv4
from capo_sagemaker_a2i_runtime._auth._identity import Credentials
from capo_sagemaker_a2i_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_sagemaker_a2i_runtime._auth._zapros_handler import AuthMiddleware
from capo_sagemaker_a2i_runtime._pagination import resolve_path as _resolve_path
from capo_sagemaker_a2i_runtime._services._aws_config import aaws_config
from capo_sagemaker_a2i_runtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_sagemaker_a2i_runtime.types.delete_human_loop_request
    import capo_sagemaker_a2i_runtime.types.delete_human_loop_response
    import capo_sagemaker_a2i_runtime.types.describe_human_loop_request
    import capo_sagemaker_a2i_runtime.types.describe_human_loop_response
    import capo_sagemaker_a2i_runtime.types.flow_definition_arn
    import capo_sagemaker_a2i_runtime.types.human_loop_data_attributes
    import capo_sagemaker_a2i_runtime.types.human_loop_input
    import capo_sagemaker_a2i_runtime.types.human_loop_name
    import capo_sagemaker_a2i_runtime.types.human_loop_summary
    import capo_sagemaker_a2i_runtime.types.list_human_loops_request
    import capo_sagemaker_a2i_runtime.types.list_human_loops_response
    import capo_sagemaker_a2i_runtime.types.max_results
    import capo_sagemaker_a2i_runtime.types.next_token
    import capo_sagemaker_a2i_runtime.types.sort_order
    import capo_sagemaker_a2i_runtime.types.start_human_loop_request
    import capo_sagemaker_a2i_runtime.types.start_human_loop_response
    import capo_sagemaker_a2i_runtime.types.stop_human_loop_request
    import capo_sagemaker_a2i_runtime.types.stop_human_loop_response
    import capo_sagemaker_a2i_runtime.types.timestamp


class AsyncSageMakerA2IRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSageMakerA2IRuntimeClient:
    """A client for the ``SageMakerA2IRuntime`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = AsyncClient(http_handler).wrap_with_middleware(
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
                AsyncClient(http_handler)
            )
        self._config = AsyncSageMakerA2IRuntimeClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSageMakerA2IRuntimeClientConfig = config_overrides or {}
        interceptors_: list[AsyncInterceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aaws_config(),
            aretry(),
        ]
        options_: AsyncOperationOptions = AsyncOperationOptions(
            client=self._client,
            retry_max_attempts=overrides.get(
                "retry_max_attempts", self._config.get("retry_max_attempts")
            ),
            region=overrides.get("region", self._config.get("region")),
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def delete_human_loop(
        self,
        human_loop_name: "capo_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
    ) -> "capo_sagemaker_a2i_runtime.types.delete_human_loop_response.DeleteHumanLoopResponse":
        """<p>Deletes the specified human loop for a flow definition.</p> <p>If the human loop was deleted, this operation will return a <code>ResourceNotFoundException</code>. </p>

        Args:
            human_loop_name: <p>The name of the human loop that you want to delete.</p>

        Raises:
            capo_sagemaker_a2i_runtime.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_sagemaker_a2i_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again. </p>
            capo_sagemaker_a2i_runtime.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_sagemaker_a2i_runtime.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_sagemaker_a2i_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_a2i_runtime.types.delete_human_loop_request.DeleteHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_a2i_runtime.types.delete_human_loop_response.DeleteHumanLoopResponse"
        ]:
            import capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.delete_human_loop

            (
                output,
                http_response,
            ) = await capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.delete_human_loop.async_delete_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_a2i_runtime.types.delete_human_loop_request.DeleteHumanLoopRequest = {
            "human_loop_name": human_loop_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_human_loop(
        self,
        human_loop_name: "capo_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName",
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
    ) -> "capo_sagemaker_a2i_runtime.types.describe_human_loop_response.DescribeHumanLoopResponse":
        """<p>Returns information about the specified human loop. If the human loop was deleted, this operation will return a <code>ResourceNotFoundException</code> error. </p>

        Args:
            human_loop_name: <p>The name of the human loop that you want information about.</p>

        Raises:
            capo_sagemaker_a2i_runtime.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_sagemaker_a2i_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again. </p>
            capo_sagemaker_a2i_runtime.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_sagemaker_a2i_runtime.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_sagemaker_a2i_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_a2i_runtime.types.describe_human_loop_request.DescribeHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_a2i_runtime.types.describe_human_loop_response.DescribeHumanLoopResponse"
        ]:
            import capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.describe_human_loop

            (
                output,
                http_response,
            ) = await capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.describe_human_loop.async_describe_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_a2i_runtime.types.describe_human_loop_request.DescribeHumanLoopRequest = {
            "human_loop_name": human_loop_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_human_loops(
        self,
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
        creation_time_after: Optional[
            "capo_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "capo_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        flow_definition_arn: Optional[
            "capo_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn"
        ] = None,
        sort_order: Optional[
            "capo_sagemaker_a2i_runtime.types.sort_order.SortOrder"
        ] = None,
        next_token: Optional[
            "capo_sagemaker_a2i_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_sagemaker_a2i_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_sagemaker_a2i_runtime.types.list_human_loops_response.ListHumanLoopsResponse":
        """<p>Returns information about human loops, given the specified parameters. If a human loop was deleted, it will not be included.</p>

        Args:
            creation_time_after: <p>(Optional) The timestamp of the date when you want the human loops to begin in ISO 8601 format. For example, <code>2020-02-24</code>.</p>
            creation_time_before: <p>(Optional) The timestamp of the date before which you want the human loops to begin in ISO 8601 format. For example, <code>2020-02-24</code>.</p>
            flow_definition_arn: <p>The Amazon Resource Name (ARN) of a flow definition.</p>
            sort_order: <p>Optional. The order for displaying results. Valid values: <code>Ascending</code> and <code>Descending</code>.</p>
            next_token: <p>A token to display the next page of results.</p>
            max_results: <p>The total number of items to return. If the total number of available items is more than the value specified in <code>MaxResults</code>, then a <code>NextToken</code> is returned in the output. You can use this token to display the next page of results. </p>

        Raises:
            capo_sagemaker_a2i_runtime.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_sagemaker_a2i_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again. </p>
            capo_sagemaker_a2i_runtime.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_sagemaker_a2i_runtime.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_sagemaker_a2i_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_a2i_runtime.types.list_human_loops_request.ListHumanLoopsRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_a2i_runtime.types.list_human_loops_response.ListHumanLoopsResponse"
        ]:
            import capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.list_human_loops

            (
                output,
                http_response,
            ) = await capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.list_human_loops.async_list_human_loops(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_a2i_runtime.types.list_human_loops_request.ListHumanLoopsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if flow_definition_arn is not None:
            input_["flow_definition_arn"] = flow_definition_arn
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    async def iter_list_human_loops(
        self,
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
        creation_time_after: Optional[
            "capo_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        creation_time_before: Optional[
            "capo_sagemaker_a2i_runtime.types.timestamp.Timestamp"
        ] = None,
        flow_definition_arn: Optional[
            "capo_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn"
        ] = None,
        sort_order: Optional[
            "capo_sagemaker_a2i_runtime.types.sort_order.SortOrder"
        ] = None,
        next_token: Optional[
            "capo_sagemaker_a2i_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_sagemaker_a2i_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_sagemaker_a2i_runtime.types.human_loop_summary.HumanLoopSummary]":
        _token = next_token
        while True:
            _response = await self.list_human_loops(
                config_overrides=config_overrides,
                creation_time_after=creation_time_after,
                creation_time_before=creation_time_before,
                flow_definition_arn=flow_definition_arn,
                sort_order=sort_order,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("human_loop_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_human_loop(
        self,
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
        human_loop_name: Optional[
            "capo_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
        ] = None,
        flow_definition_arn: Optional[
            "capo_sagemaker_a2i_runtime.types.flow_definition_arn.FlowDefinitionArn"
        ] = None,
        human_loop_input: Optional[
            "capo_sagemaker_a2i_runtime.types.human_loop_input.HumanLoopInput"
        ] = None,
        data_attributes: Optional[
            "capo_sagemaker_a2i_runtime.types.human_loop_data_attributes.HumanLoopDataAttributes"
        ] = None,
    ) -> "capo_sagemaker_a2i_runtime.types.start_human_loop_response.StartHumanLoopResponse":
        """<p>Starts a human loop, provided that at least one activation condition is met.</p>

        Args:
            human_loop_name: <p>The name of the human loop.</p>
            flow_definition_arn: <p>The Amazon Resource Name (ARN) of the flow definition associated with this human loop.</p>
            human_loop_input: <p>An object that contains information about the human loop.</p>
            data_attributes: <p>Attributes of the specified data. Use <code>DataAttributes</code> to specify if your data is free of personally identifiable information and/or free of adult content.</p>

        Raises:
            capo_sagemaker_a2i_runtime.errors.conflict_exception.ConflictException: <p>Your request has the same name as another active human loop but has different input data. You cannot start two human loops with the same name and different input data.</p>
            capo_sagemaker_a2i_runtime.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_sagemaker_a2i_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account. For a list of Amazon A2I service quotes, see <a href="https://docs.aws.amazon.com/general/latest/gr/a2i.html">Amazon Augmented AI Service Quotes</a>. Delete some resources or request an increase in your service quota. You can request a quota increase using Service Quotas or the AWS Support Center. To request an increase, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html">AWS Service Quotas</a> in the <i>AWS General Reference</i>.</p>
            capo_sagemaker_a2i_runtime.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_sagemaker_a2i_runtime.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_sagemaker_a2i_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_a2i_runtime.types.start_human_loop_request.StartHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_a2i_runtime.types.start_human_loop_response.StartHumanLoopResponse"
        ]:
            import capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.start_human_loop

            (
                output,
                http_response,
            ) = await capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.start_human_loop.async_start_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_a2i_runtime.types.start_human_loop_request.StartHumanLoopRequest = {}
        if human_loop_name is not None:
            input_["human_loop_name"] = human_loop_name
        if flow_definition_arn is not None:
            input_["flow_definition_arn"] = flow_definition_arn
        if human_loop_input is not None:
            input_["human_loop_input"] = human_loop_input
        if data_attributes is not None:
            input_["data_attributes"] = data_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_human_loop(
        self,
        *,
        config_overrides: Optional[AsyncSageMakerA2IRuntimeClientConfig] = None,
        human_loop_name: Optional[
            "capo_sagemaker_a2i_runtime.types.human_loop_name.HumanLoopName"
        ] = None,
    ) -> "capo_sagemaker_a2i_runtime.types.stop_human_loop_response.StopHumanLoopResponse":
        """<p>Stops the specified human loop.</p>

        Args:
            human_loop_name: <p>The name of the human loop that you want to stop.</p>

        Raises:
            capo_sagemaker_a2i_runtime.errors.internal_server_exception.InternalServerException: <p>We couldn't process your request because of an issue with the server. Try again later.</p>
            capo_sagemaker_a2i_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again. </p>
            capo_sagemaker_a2i_runtime.errors.throttling_exception.ThrottlingException: <p>You exceeded the maximum number of requests.</p>
            capo_sagemaker_a2i_runtime.errors.validation_exception.ValidationException: <p>The request isn't valid. Check the syntax and try again.</p>
            capo_sagemaker_a2i_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_sagemaker_a2i_runtime.types.stop_human_loop_request.StopHumanLoopRequest]",
        ) -> AsyncOperationResponse[
            "capo_sagemaker_a2i_runtime.types.stop_human_loop_response.StopHumanLoopResponse"
        ]:
            import capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.stop_human_loop

            (
                output,
                http_response,
            ) = await capo_sagemaker_a2i_runtime._operations.amazon_sage_maker_a2_i_runtime.stop_human_loop.async_stop_human_loop(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_sagemaker_a2i_runtime.types.stop_human_loop_request.StopHumanLoopRequest = {}
        if human_loop_name is not None:
            input_["human_loop_name"] = human_loop_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
