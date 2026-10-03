"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#CodeGuruProfiler``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_codeguruprofiler._auth._signers
import capo_codeguruprofiler._auth._sigv4
from capo_codeguruprofiler._auth._identity import Credentials
from capo_codeguruprofiler._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_codeguruprofiler._auth._zapros_handler import AuthMiddleware
from capo_codeguruprofiler._pagination import resolve_path as _resolve_path
from capo_codeguruprofiler._resources.code_guru_profiler.profiling_group import (
    AsyncProfilingGroup,
)
from capo_codeguruprofiler._services._aws_config import aaws_config
from capo_codeguruprofiler._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.action_group
    import capo_codeguruprofiler.types.add_notification_channels_request
    import capo_codeguruprofiler.types.add_notification_channels_response
    import capo_codeguruprofiler.types.agent_orchestration_config
    import capo_codeguruprofiler.types.agent_profile
    import capo_codeguruprofiler.types.aggregation_period
    import capo_codeguruprofiler.types.anomaly_instance_id
    import capo_codeguruprofiler.types.batch_get_frame_metric_data_request
    import capo_codeguruprofiler.types.batch_get_frame_metric_data_response
    import capo_codeguruprofiler.types.channel_id
    import capo_codeguruprofiler.types.channels
    import capo_codeguruprofiler.types.client_token
    import capo_codeguruprofiler.types.compute_platform
    import capo_codeguruprofiler.types.configure_agent_request
    import capo_codeguruprofiler.types.configure_agent_response
    import capo_codeguruprofiler.types.create_profiling_group_request
    import capo_codeguruprofiler.types.create_profiling_group_response
    import capo_codeguruprofiler.types.delete_profiling_group_request
    import capo_codeguruprofiler.types.delete_profiling_group_response
    import capo_codeguruprofiler.types.describe_profiling_group_request
    import capo_codeguruprofiler.types.describe_profiling_group_response
    import capo_codeguruprofiler.types.feedback_type
    import capo_codeguruprofiler.types.fleet_instance_id
    import capo_codeguruprofiler.types.frame_metrics
    import capo_codeguruprofiler.types.get_findings_report_account_summary_request
    import capo_codeguruprofiler.types.get_findings_report_account_summary_response
    import capo_codeguruprofiler.types.get_notification_configuration_request
    import capo_codeguruprofiler.types.get_notification_configuration_response
    import capo_codeguruprofiler.types.get_policy_request
    import capo_codeguruprofiler.types.get_policy_response
    import capo_codeguruprofiler.types.get_profile_request
    import capo_codeguruprofiler.types.get_profile_response
    import capo_codeguruprofiler.types.get_recommendations_request
    import capo_codeguruprofiler.types.get_recommendations_response
    import capo_codeguruprofiler.types.list_findings_reports_request
    import capo_codeguruprofiler.types.list_findings_reports_response
    import capo_codeguruprofiler.types.list_profile_times_request
    import capo_codeguruprofiler.types.list_profile_times_response
    import capo_codeguruprofiler.types.list_profiling_groups_request
    import capo_codeguruprofiler.types.list_profiling_groups_response
    import capo_codeguruprofiler.types.list_tags_for_resource_request
    import capo_codeguruprofiler.types.list_tags_for_resource_response
    import capo_codeguruprofiler.types.locale
    import capo_codeguruprofiler.types.max_depth
    import capo_codeguruprofiler.types.max_results
    import capo_codeguruprofiler.types.metadata
    import capo_codeguruprofiler.types.order_by
    import capo_codeguruprofiler.types.pagination_token
    import capo_codeguruprofiler.types.period
    import capo_codeguruprofiler.types.post_agent_profile_request
    import capo_codeguruprofiler.types.post_agent_profile_response
    import capo_codeguruprofiler.types.principals
    import capo_codeguruprofiler.types.profile_time
    import capo_codeguruprofiler.types.profiling_group_arn
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.put_permission_request
    import capo_codeguruprofiler.types.put_permission_response
    import capo_codeguruprofiler.types.remove_notification_channel_request
    import capo_codeguruprofiler.types.remove_notification_channel_response
    import capo_codeguruprofiler.types.remove_permission_request
    import capo_codeguruprofiler.types.remove_permission_response
    import capo_codeguruprofiler.types.revision_id
    import capo_codeguruprofiler.types.submit_feedback_request
    import capo_codeguruprofiler.types.submit_feedback_response
    import capo_codeguruprofiler.types.tag_keys
    import capo_codeguruprofiler.types.tag_resource_request
    import capo_codeguruprofiler.types.tag_resource_response
    import capo_codeguruprofiler.types.tags_map
    import capo_codeguruprofiler.types.timestamp
    import capo_codeguruprofiler.types.untag_resource_request
    import capo_codeguruprofiler.types.untag_resource_response
    import capo_codeguruprofiler.types.update_profiling_group_request
    import capo_codeguruprofiler.types.update_profiling_group_response


class AsyncCodeGuruProfilerClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncCodeGuruProfilerClient:
    """A client for the ``CodeGuruProfiler`` service.

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
        self._config = AsyncCodeGuruProfilerClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.profiling_group = AsyncProfilingGroup(self)

    def operation_options(
        self, config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncCodeGuruProfilerClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    async def get_findings_report_account_summary(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        daily_reports_only: Optional[bool] = None,
    ) -> "capo_codeguruprofiler.types.get_findings_report_account_summary_response.GetFindingsReportAccountSummaryResponse":
        """<p> Returns a list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_FindingsReportSummary.html"> <code>FindingsReportSummary</code> </a> objects that contain analysis results for all profiling groups in your AWS account. </p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>GetFindingsReportAccountSummary</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of results returned by <code> GetFindingsReportAccountSummary</code> in paginated output. When this parameter is used, <code>GetFindingsReportAccountSummary</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>GetFindingsReportAccountSummary</code> request with the returned <code>nextToken</code> value.</p>
            daily_reports_only: <p>A <code>Boolean</code> value indicating whether to only return reports from daily profiles. If set to <code>True</code>, only analysis data from daily profiles is returned. If set to <code>False</code>, analysis data is returned from smaller time windows (for example, one hour).</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.get_findings_report_account_summary_request.GetFindingsReportAccountSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.get_findings_report_account_summary_response.GetFindingsReportAccountSummaryResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.get_findings_report_account_summary

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.get_findings_report_account_summary.async_get_findings_report_account_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.get_findings_report_account_summary_request.GetFindingsReportAccountSummaryRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if daily_reports_only is not None:
            input_["daily_reports_only"] = daily_reports_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_findings_report_account_summary(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        daily_reports_only: Optional[bool] = None,
    ) -> "AsyncIterator[capo_codeguruprofiler.types.get_findings_report_account_summary_response.GetFindingsReportAccountSummaryResponse]":
        _token = next_token
        while True:
            _response = await self.get_findings_report_account_summary(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                daily_reports_only=daily_reports_only,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p> Returns a list of the tags that are assigned to a specified resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that contains the tags to return. </p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn",
        tags: "capo_codeguruprofiler.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.tag_resource_response.TagResourceResponse":
        """<p> Use to assign one or more tags to a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that the tags are added to. </p>
            tags: <p> The list of tags that are added to the specified resource. </p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.tag_resource

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def untag_resource(
        self,
        resource_arn: "capo_codeguruprofiler.types.profiling_group_arn.ProfilingGroupArn",
        tag_keys: "capo_codeguruprofiler.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.untag_resource_response.UntagResourceResponse":
        """<p> Use to remove one or more tags from a resource. </p>

        Args:
            resource_arn: <p> The Amazon Resource Name (ARN) of the resource that contains the tags to remove. </p>
            tag_keys: <p> A list of tag keys. Existing tags of resources with keys in this list are removed from the specified resource. </p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.untag_resource

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_profiling_group(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        client_token: "capo_codeguruprofiler.types.client_token.ClientToken",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        compute_platform: Optional[
            "capo_codeguruprofiler.types.compute_platform.ComputePlatform"
        ] = None,
        agent_orchestration_config: Optional[
            "capo_codeguruprofiler.types.agent_orchestration_config.AgentOrchestrationConfig"
        ] = None,
        tags: Optional["capo_codeguruprofiler.types.tags_map.TagsMap"] = None,
    ) -> "capo_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse":
        """<p>Creates a profiling group.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group to create.</p>
            compute_platform: <p> The compute platform of the profiling group. Use <code>AWSLambda</code> if your application runs on AWS Lambda. Use <code>Default</code> if your application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. If not specified, <code>Default</code> is used. </p>
            client_token: <p> Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental creation of duplicate profiling groups if there are failures and retries. </p>
            agent_orchestration_config: <p> Specifies whether profiling is enabled or disabled for the created profiling group. </p>
            tags: <p> A list of tags to add to the created profiling group. </p>

        Raises:
            capo_codeguruprofiler.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a> to request a service quota increase. </p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.create_profiling_group_request.CreateProfilingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.create_profiling_group_response.CreateProfilingGroupResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.create_profiling_group

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.create_profiling_group.async_create_profiling_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.create_profiling_group_request.CreateProfilingGroupRequest = {
            "profiling_group_name": profiling_group_name,
            "client_token": client_token,
        }
        if compute_platform is not None:
            input_["compute_platform"] = compute_platform
        if agent_orchestration_config is not None:
            input_["agent_orchestration_config"] = agent_orchestration_config
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_profiling_group(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.describe_profiling_group_response.DescribeProfilingGroupResponse":
        """<p> Returns a <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> object that contains information about the requested profiling group. </p>

        Args:
            profiling_group_name: <p> The name of the profiling group to get information about. </p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.describe_profiling_group_request.DescribeProfilingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.describe_profiling_group_response.DescribeProfilingGroupResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.describe_profiling_group

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.describe_profiling_group.async_describe_profiling_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.describe_profiling_group_request.DescribeProfilingGroupRequest = {
            "profiling_group_name": profiling_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_profiling_group(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        agent_orchestration_config: "capo_codeguruprofiler.types.agent_orchestration_config.AgentOrchestrationConfig",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.update_profiling_group_response.UpdateProfilingGroupResponse":
        """<p>Updates a profiling group.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group to update.</p>
            agent_orchestration_config: <p> Specifies whether profiling is enabled or disabled for a profiling group. </p>

        Raises:
            capo_codeguruprofiler.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.update_profiling_group_request.UpdateProfilingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.update_profiling_group_response.UpdateProfilingGroupResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.update_profiling_group

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.update_profiling_group.async_update_profiling_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.update_profiling_group_request.UpdateProfilingGroupRequest = {
            "profiling_group_name": profiling_group_name,
            "agent_orchestration_config": agent_orchestration_config,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_profiling_group(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.delete_profiling_group_response.DeleteProfilingGroupResponse":
        """<p>Deletes a profiling group.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group to delete.</p>

        Raises:
            capo_codeguruprofiler.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.delete_profiling_group_request.DeleteProfilingGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.delete_profiling_group_response.DeleteProfilingGroupResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.delete_profiling_group

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.delete_profiling_group.async_delete_profiling_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.delete_profiling_group_request.DeleteProfilingGroupRequest = {
            "profiling_group_name": profiling_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_profiling_groups(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        include_description: Optional[bool] = None,
    ) -> "capo_codeguruprofiler.types.list_profiling_groups_response.ListProfilingGroupsResponse":
        """<p> Returns a list of profiling groups. The profiling groups are returned as <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> objects. </p>

        Args:
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListProfilingGroups</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of profiling groups results returned by <code>ListProfilingGroups</code> in paginated output. When this parameter is used, <code>ListProfilingGroups</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListProfilingGroups</code> request with the returned <code>nextToken</code> value. </p>
            include_description: <p>A <code>Boolean</code> value indicating whether to include a description. If <code>true</code>, then a list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription.html"> <code>ProfilingGroupDescription</code> </a> objects that contain detailed information about profiling groups is returned. If <code>false</code>, then a list of profiling group names is returned.</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.list_profiling_groups_request.ListProfilingGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.list_profiling_groups_response.ListProfilingGroupsResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.list_profiling_groups

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.list_profiling_groups.async_list_profiling_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.list_profiling_groups_request.ListProfilingGroupsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if include_description is not None:
            input_["include_description"] = include_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_profiling_groups(
        self,
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        include_description: Optional[bool] = None,
    ) -> "AsyncIterator[capo_codeguruprofiler.types.list_profiling_groups_response.ListProfilingGroupsResponse]":
        _token = next_token
        while True:
            _response = await self.list_profiling_groups(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                include_description=include_description,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def add_notification_channels(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        channels: "capo_codeguruprofiler.types.channels.Channels",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.add_notification_channels_response.AddNotificationChannelsResponse":
        """<p>Add up to 2 anomaly notifications channels for a profiling group.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group that we are setting up notifications for.</p>
            channels: <p>One or 2 channels to report to when anomalies are detected.</p>

        Raises:
            capo_codeguruprofiler.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use <a href="https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html">Service Quotas</a> to request a service quota increase. </p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.add_notification_channels_request.AddNotificationChannelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.add_notification_channels_response.AddNotificationChannelsResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.add_notification_channels

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.add_notification_channels.async_add_notification_channels(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.add_notification_channels_request.AddNotificationChannelsRequest = {
            "profiling_group_name": profiling_group_name,
            "channels": channels,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_get_frame_metric_data(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        start_time: Optional["capo_codeguruprofiler.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_codeguruprofiler.types.timestamp.Timestamp"] = None,
        period: Optional["capo_codeguruprofiler.types.period.Period"] = None,
        target_resolution: Optional[
            "capo_codeguruprofiler.types.aggregation_period.AggregationPeriod"
        ] = None,
        frame_metrics: Optional[
            "capo_codeguruprofiler.types.frame_metrics.FrameMetrics"
        ] = None,
    ) -> "capo_codeguruprofiler.types.batch_get_frame_metric_data_response.BatchGetFrameMetricDataResponse":
        """<p> Returns the time series of values for a requested list of frame metrics from a time period.</p>

        Args:
            profiling_group_name: <p> The name of the profiling group associated with the the frame metrics used to return the time series values. </p>
            start_time: <p> The start time of the time period for the frame metrics used to return the time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>
            end_time: <p> The end time of the time period for the returned time series values. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>
            period: <p> The duration of the frame metrics used to return the time series values. Specify using the ISO 8601 format. The maximum period duration is one day (<code>PT24H</code> or <code>P1D</code>). </p>
            target_resolution: <p>The requested resolution of time steps for the returned time series of values. If the requested target resolution is not available due to data not being retained we provide a best effort result by falling back to the most granular available resolution after the target resolution. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>
            frame_metrics: <p> The details of the metrics that are used to request a time series of values. The metric includes the name of the frame, the aggregation type to calculate the metric value for the frame, and the thread states to use to get the count for the metric value of the frame.</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.batch_get_frame_metric_data_request.BatchGetFrameMetricDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.batch_get_frame_metric_data_response.BatchGetFrameMetricDataResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.batch_get_frame_metric_data

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.batch_get_frame_metric_data.async_batch_get_frame_metric_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.batch_get_frame_metric_data_request.BatchGetFrameMetricDataRequest = {
            "profiling_group_name": profiling_group_name
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if period is not None:
            input_["period"] = period
        if target_resolution is not None:
            input_["target_resolution"] = target_resolution
        if frame_metrics is not None:
            input_["frame_metrics"] = frame_metrics

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def configure_agent(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        fleet_instance_id: Optional[
            "capo_codeguruprofiler.types.fleet_instance_id.FleetInstanceId"
        ] = None,
        metadata: Optional["capo_codeguruprofiler.types.metadata.Metadata"] = None,
    ) -> "capo_codeguruprofiler.types.configure_agent_response.ConfigureAgentResponse":
        """<p> Used by profiler agents to report their current state and to receive remote configuration updates. For example, <code>ConfigureAgent</code> can be used to tell an agent whether to profile or not and for how long to return profiling data. </p>

        Args:
            profiling_group_name: <p> The name of the profiling group for which the configured agent is collecting profiling data. </p>
            fleet_instance_id: <p> A universally unique identifier (UUID) for a profiling instance. For example, if the profiling instance is an Amazon EC2 instance, it is the instance ID. If it is an AWS Fargate container, it is the container's task ID. </p>
            metadata: <p> Metadata captured about the compute platform the agent is running on. It includes information about sampling and reporting. The valid fields are:</p> <ul> <li> <p> <code>COMPUTE_PLATFORM</code> - The compute platform on which the agent is running </p> </li> <li> <p> <code>AGENT_ID</code> - The ID for an agent instance. </p> </li> <li> <p> <code>AWS_REQUEST_ID</code> - The AWS request ID of a Lambda invocation. </p> </li> <li> <p> <code>EXECUTION_ENVIRONMENT</code> - The execution environment a Lambda function is running on. </p> </li> <li> <p> <code>LAMBDA_FUNCTION_ARN</code> - The Amazon Resource Name (ARN) that is used to invoke a Lambda function. </p> </li> <li> <p> <code>LAMBDA_MEMORY_LIMIT_IN_MB</code> - The memory allocated to a Lambda function. </p> </li> <li> <p> <code>LAMBDA_REMAINING_TIME_IN_MILLISECONDS</code> - The time in milliseconds before execution of a Lambda function times out. </p> </li> <li> <p> <code>LAMBDA_TIME_GAP_BETWEEN_INVOKES_IN_MILLISECONDS</code> - The time in milliseconds between two invocations of a Lambda function. </p> </li> <li> <p> <code>LAMBDA_PREVIOUS_EXECUTION_TIME_IN_MILLISECONDS</code> - The time in milliseconds for the previous Lambda invocation. </p> </li> </ul>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.configure_agent_request.ConfigureAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.configure_agent_response.ConfigureAgentResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.configure_agent

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.configure_agent.async_configure_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.configure_agent_request.ConfigureAgentRequest = {
            "profiling_group_name": profiling_group_name
        }
        if fleet_instance_id is not None:
            input_["fleet_instance_id"] = fleet_instance_id
        if metadata is not None:
            input_["metadata"] = metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_notification_configuration(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.get_notification_configuration_response.GetNotificationConfigurationResponse":
        """<p>Get the current configuration for anomaly notifications for a profiling group.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group we want to get the notification configuration for.</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.get_notification_configuration_request.GetNotificationConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.get_notification_configuration_response.GetNotificationConfigurationResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.get_notification_configuration

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.get_notification_configuration.async_get_notification_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.get_notification_configuration_request.GetNotificationConfigurationRequest = {
            "profiling_group_name": profiling_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_policy(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.get_policy_response.GetPolicyResponse":
        """<p> Returns the JSON-formatted resource-based policy on a profiling group. </p>

        Args:
            profiling_group_name: <p>The name of the profiling group.</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.get_policy_request.GetPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.get_policy

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.get_policy.async_get_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.get_policy_request.GetPolicyRequest = {
            "profiling_group_name": profiling_group_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_profile(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        start_time: Optional["capo_codeguruprofiler.types.timestamp.Timestamp"] = None,
        period: Optional["capo_codeguruprofiler.types.period.Period"] = None,
        end_time: Optional["capo_codeguruprofiler.types.timestamp.Timestamp"] = None,
        max_depth: Optional["capo_codeguruprofiler.types.max_depth.MaxDepth"] = None,
        accept: Optional[str] = None,
    ) -> "capo_codeguruprofiler.types.get_profile_response.GetProfileResponse":
        """<p> Gets the aggregated profile of a profiling group for a specified time range. Amazon CodeGuru Profiler collects posted agent profiles for a profiling group into aggregated profiles. </p> <note> <p> Because aggregated profiles expire over time <code>GetProfile</code> is not idempotent. </p> </note> <p> Specify the time range for the requested aggregated profile using 1 or 2 of the following parameters: <code>startTime</code>, <code>endTime</code>, <code>period</code>. The maximum time range allowed is 7 days. If you specify all 3 parameters, an exception is thrown. If you specify only <code>period</code>, the latest aggregated profile is returned. </p> <p> Aggregated profiles are available with aggregation periods of 5 minutes, 1 hour, and 1 day, aligned to UTC. The aggregation period of an aggregated profile determines how long it is retained. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime.html"> <code>AggregatedProfileTime</code> </a>. The aggregated profile's aggregation period determines how long it is retained by CodeGuru Profiler. </p> <ul> <li> <p> If the aggregation period is 5 minutes, the aggregated profile is retained for 15 days. </p> </li> <li> <p> If the aggregation period is 1 hour, the aggregated profile is retained for 60 days. </p> </li> <li> <p> If the aggregation period is 1 day, the aggregated profile is retained for 3 years. </p> </li> </ul> <p>There are two use cases for calling <code>GetProfile</code>.</p> <ol> <li> <p> If you want to return an aggregated profile that already exists, use <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ListProfileTimes.html"> <code>ListProfileTimes</code> </a> to view the time ranges of existing aggregated profiles. Use them in a <code>GetProfile</code> request to return a specific, existing aggregated profile. </p> </li> <li> <p> If you want to return an aggregated profile for a time range that doesn't align with an existing aggregated profile, then CodeGuru Profiler makes a best effort to combine existing aggregated profiles from the requested time range and return them as one aggregated profile. </p> <p> If aggregated profiles do not exist for the full time range requested, then aggregated profiles for a smaller time range are returned. For example, if the requested time range is from 00:00 to 00:20, and the existing aggregated profiles are from 00:15 and 00:25, then the aggregated profiles from 00:15 to 00:20 are returned. </p> </li> </ol>

        Args:
            profiling_group_name: <p>The name of the profiling group to get.</p>
            start_time: <p>The start time of the profile to get. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.</p> <p> If you specify <code>startTime</code>, then you must also specify <code>period</code> or <code>endTime</code>, but not both. </p>
            period: <p> Used with <code>startTime</code> or <code>endTime</code> to specify the time range for the returned aggregated profile. Specify using the ISO 8601 format. For example, <code>P1DT1H1M1S</code>. </p> <p> To get the latest aggregated profile, specify only <code>period</code>. </p>
            end_time: <p> The end time of the requested profile. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p> <p> If you specify <code>endTime</code>, then you must also specify <code>period</code> or <code>startTime</code>, but not both. </p>
            max_depth: <p> The maximum depth of the stacks in the code that is represented in the aggregated profile. For example, if CodeGuru Profiler finds a method <code>A</code>, which calls method <code>B</code>, which calls method <code>C</code>, which calls method <code>D</code>, then the depth is 4. If the <code>maxDepth</code> is set to 2, then the aggregated profile contains representations of methods <code>A</code> and <code>B</code>. </p>
            accept: <p> The format of the returned profiling data. The format maps to the <code>Accept</code> and <code>Content-Type</code> headers of the HTTP request. You can specify one of the following: or the default . </p> <ul> <li> <p> <code>application/json</code> — standard JSON format </p> </li> <li> <p> <code>application/x-amzn-ion</code> — the Amazon Ion data format. For more information, see <a href="http://amzn.github.io/ion-docs/">Amazon Ion</a>. </p> </li> </ul>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.get_profile_request.GetProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.get_profile_response.GetProfileResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.get_profile

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.get_profile.async_get_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.get_profile_request.GetProfileRequest = {
            "profiling_group_name": profiling_group_name
        }
        if start_time is not None:
            input_["start_time"] = start_time
        if period is not None:
            input_["period"] = period
        if end_time is not None:
            input_["end_time"] = end_time
        if max_depth is not None:
            input_["max_depth"] = max_depth
        if accept is not None:
            input_["accept"] = accept

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recommendations(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        start_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        end_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        locale: Optional["capo_codeguruprofiler.types.locale.Locale"] = None,
    ) -> "capo_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse":
        """<p> Returns a list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Recommendation.html"> <code>Recommendation</code> </a> objects that contain recommendations for a profiling group for a given time period. A list of <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_Anomaly.html"> <code>Anomaly</code> </a> objects that contains details about anomalies detected in the profiling group for the same time period is also returned. </p>

        Args:
            profiling_group_name: <p> The name of the profiling group to get analysis data about. </p>
            start_time: <p> The end time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>
            end_time: <p> The start time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>
            locale: <p> The language used to provide analysis. Specify using a string that is one of the following <code>BCP 47</code> language codes. </p> <ul> <li> <p> <code>de-DE</code> - German, Germany </p> </li> <li> <p> <code>en-GB</code> - English, United Kingdom </p> </li> <li> <p> <code>en-US</code> - English, United States </p> </li> <li> <p> <code>es-ES</code> - Spanish, Spain </p> </li> <li> <p> <code>fr-FR</code> - French, France </p> </li> <li> <p> <code>it-IT</code> - Italian, Italy </p> </li> <li> <p> <code>ja-JP</code> - Japanese, Japan </p> </li> <li> <p> <code>ko-KR</code> - Korean, Republic of Korea </p> </li> <li> <p> <code>pt-BR</code> - Portugese, Brazil </p> </li> <li> <p> <code>zh-CN</code> - Chinese, China </p> </li> <li> <p> <code>zh-TW</code> - Chinese, Taiwan </p> </li> </ul>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.get_recommendations

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.get_recommendations.async_get_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.get_recommendations_request.GetRecommendationsRequest = {
            "profiling_group_name": profiling_group_name,
            "start_time": start_time,
            "end_time": end_time,
        }
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_findings_reports(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        start_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        end_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        daily_reports_only: Optional[bool] = None,
    ) -> "capo_codeguruprofiler.types.list_findings_reports_response.ListFindingsReportsResponse":
        """<p>List the available reports for a given profiling group and time range.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group from which to search for analysis data.</p>
            start_time: <p> The start time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>
            end_time: <p> The end time of the profile to get analysis data about. You must specify <code>startTime</code> and <code>endTime</code>. This is specified using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC. </p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListFindingsReportsRequest</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>
            max_results: <p>The maximum number of report results returned by <code>ListFindingsReports</code> in paginated output. When this parameter is used, <code>ListFindingsReports</code> only returns <code>maxResults</code> results in a single page along with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListFindingsReports</code> request with the returned <code>nextToken</code> value.</p>
            daily_reports_only: <p>A <code>Boolean</code> value indicating whether to only return reports from daily profiles. If set to <code>True</code>, only analysis data from daily profiles is returned. If set to <code>False</code>, analysis data is returned from smaller time windows (for example, one hour).</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.list_findings_reports_request.ListFindingsReportsRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.list_findings_reports_response.ListFindingsReportsResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.list_findings_reports

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.list_findings_reports.async_list_findings_reports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.list_findings_reports_request.ListFindingsReportsRequest = {
            "profiling_group_name": profiling_group_name,
            "start_time": start_time,
            "end_time": end_time,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if daily_reports_only is not None:
            input_["daily_reports_only"] = daily_reports_only

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_findings_reports(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        start_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        end_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        daily_reports_only: Optional[bool] = None,
    ) -> "AsyncIterator[capo_codeguruprofiler.types.list_findings_reports_response.ListFindingsReportsResponse]":
        _token = next_token
        while True:
            _response = await self.list_findings_reports(
                profiling_group_name,
                start_time,
                end_time,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                daily_reports_only=daily_reports_only,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_profile_times(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        start_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        end_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        period: "capo_codeguruprofiler.types.aggregation_period.AggregationPeriod",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        order_by: Optional["capo_codeguruprofiler.types.order_by.OrderBy"] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_codeguruprofiler.types.list_profile_times_response.ListProfileTimesResponse":
        """<p>Lists the start times of the available aggregated profiles of a profiling group for an aggregation period within the specified time range.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group.</p>
            start_time: <p>The start time of the time range from which to list the profiles.</p>
            end_time: <p>The end time of the time range from which to list the profiles.</p>
            period: <p> The aggregation period. This specifies the period during which an aggregation profile collects posted agent profiles for a profiling group. There are 3 valid values. </p> <ul> <li> <p> <code>P1D</code> — 1 day </p> </li> <li> <p> <code>PT1H</code> — 1 hour </p> </li> <li> <p> <code>PT5M</code> — 5 minutes </p> </li> </ul>
            order_by: <p>The order (ascending or descending by start time of the profile) to use when listing profiles. Defaults to <code>TIMESTAMP_DESCENDING</code>. </p>
            max_results: <p>The maximum number of profile time results returned by <code>ListProfileTimes</code> in paginated output. When this parameter is used, <code>ListProfileTimes</code> only returns <code>maxResults</code> results in a single page with a <code>nextToken</code> response element. The remaining results of the initial request can be seen by sending another <code>ListProfileTimes</code> request with the returned <code>nextToken</code> value. </p>
            next_token: <p>The <code>nextToken</code> value returned from a previous paginated <code>ListProfileTimes</code> request where <code>maxResults</code> was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the <code>nextToken</code> value. </p> <note> <p>This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.</p> </note>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.list_profile_times_request.ListProfileTimesRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.list_profile_times_response.ListProfileTimesResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.list_profile_times

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.list_profile_times.async_list_profile_times(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.list_profile_times_request.ListProfileTimesRequest = {
            "profiling_group_name": profiling_group_name,
            "start_time": start_time,
            "end_time": end_time,
            "period": period,
        }
        if order_by is not None:
            input_["order_by"] = order_by
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

    async def iter_list_profile_times(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        start_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        end_time: "capo_codeguruprofiler.types.timestamp.Timestamp",
        period: "capo_codeguruprofiler.types.aggregation_period.AggregationPeriod",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        order_by: Optional["capo_codeguruprofiler.types.order_by.OrderBy"] = None,
        max_results: Optional[
            "capo_codeguruprofiler.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_codeguruprofiler.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_codeguruprofiler.types.profile_time.ProfileTime]":
        _token = next_token
        while True:
            _response = await self.list_profile_times(
                profiling_group_name,
                start_time,
                end_time,
                period,
                config_overrides=config_overrides,
                order_by=order_by,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("profile_times",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def post_agent_profile(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        agent_profile: "capo_codeguruprofiler.types.agent_profile.AgentProfile",
        content_type: str,
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        profile_token: Optional[
            "capo_codeguruprofiler.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_codeguruprofiler.types.post_agent_profile_response.PostAgentProfileResponse":
        """<p> Submits profiling data to an aggregated profile of a profiling group. To get an aggregated profile that is created with this profiling data, use <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_GetProfile.html"> <code>GetProfile</code> </a>. </p>

        Args:
            profiling_group_name: <p> The name of the profiling group with the aggregated profile that receives the submitted profiling data. </p>
            agent_profile: <p> The submitted profiling data. </p>
            profile_token: <p> Amazon CodeGuru Profiler uses this universally unique identifier (UUID) to prevent the accidental submission of duplicate profiling data if there are failures and retries. </p>
            content_type: <p> The format of the submitted profiling data. The format maps to the <code>Accept</code> and <code>Content-Type</code> headers of the HTTP request. You can specify one of the following: or the default . </p> <ul> <li> <p> <code>application/json</code> — standard JSON format </p> </li> <li> <p> <code>application/x-amzn-ion</code> — the Amazon Ion data format. For more information, see <a href="http://amzn.github.io/ion-docs/">Amazon Ion</a>. </p> </li> </ul>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.post_agent_profile_request.PostAgentProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.post_agent_profile_response.PostAgentProfileResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.post_agent_profile

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.post_agent_profile.async_post_agent_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.post_agent_profile_request.PostAgentProfileRequest = {
            "profiling_group_name": profiling_group_name,
            "agent_profile": agent_profile,
            "content_type": content_type,
        }
        if profile_token is None:
            profile_token = str(uuid.uuid4())
        input_["profile_token"] = profile_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_permission(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        action_group: "capo_codeguruprofiler.types.action_group.ActionGroup",
        principals: "capo_codeguruprofiler.types.principals.Principals",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        revision_id: Optional[
            "capo_codeguruprofiler.types.revision_id.RevisionId"
        ] = None,
    ) -> "capo_codeguruprofiler.types.put_permission_response.PutPermissionResponse":
        """<p> Adds permissions to a profiling group's resource-based policy that are provided using an action group. If a profiling group doesn't have a resource-based policy, one is created for it using the permissions in the action group and the roles and users in the <code>principals</code> parameter. </p> <p> The one supported action group that can be added is <code>agentPermission</code> which grants <code>ConfigureAgent</code> and <code>PostAgent</code> permissions. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html">Resource-based policies in CodeGuru Profiler</a> in the <i>Amazon CodeGuru Profiler User Guide</i>, <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html"> <code>ConfigureAgent</code> </a>, and <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html"> <code>PostAgentProfile</code> </a>. </p> <p> The first time you call <code>PutPermission</code> on a profiling group, do not specify a <code>revisionId</code> because it doesn't have a resource-based policy. Subsequent calls must provide a <code>revisionId</code> to specify which revision of the resource-based policy to add the permissions to. </p> <p> The response contains the profiling group's JSON-formatted resource policy. </p>

        Args:
            profiling_group_name: <p>The name of the profiling group to grant access to.</p>
            action_group: <p> Specifies an action group that contains permissions to add to a profiling group resource. One action group is supported, <code>agentPermissions</code>, which grants permission to perform actions required by the profiling agent, <code>ConfigureAgent</code> and <code>PostAgentProfile</code> permissions. </p>
            principals: <p> A list ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not are supported in the ARNs. </p>
            revision_id: <p> A universally unique identifier (UUID) for the revision of the policy you are adding to the profiling group. Do not specify this when you add permissions to a profiling group for the first time. If a policy already exists on the profiling group, you must specify the <code>revisionId</code>. </p>

        Raises:
            capo_codeguruprofiler.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.put_permission_request.PutPermissionRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.put_permission_response.PutPermissionResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.put_permission

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.put_permission.async_put_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.put_permission_request.PutPermissionRequest = {
            "profiling_group_name": profiling_group_name,
            "action_group": action_group,
            "principals": principals,
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_notification_channel(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        channel_id: "capo_codeguruprofiler.types.channel_id.ChannelId",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.remove_notification_channel_response.RemoveNotificationChannelResponse":
        """<p>Remove one anomaly notifications channel for a profiling group.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group we want to change notification configuration for.</p>
            channel_id: <p>The id of the channel that we want to stop receiving notifications.</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.remove_notification_channel_request.RemoveNotificationChannelRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.remove_notification_channel_response.RemoveNotificationChannelResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.remove_notification_channel

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.remove_notification_channel.async_remove_notification_channel(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.remove_notification_channel_request.RemoveNotificationChannelRequest = {
            "profiling_group_name": profiling_group_name,
            "channel_id": channel_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_permission(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        action_group: "capo_codeguruprofiler.types.action_group.ActionGroup",
        revision_id: "capo_codeguruprofiler.types.revision_id.RevisionId",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
    ) -> "capo_codeguruprofiler.types.remove_permission_response.RemovePermissionResponse":
        """<p> Removes permissions from a profiling group's resource-based policy that are provided using an action group. The one supported action group that can be removed is <code>agentPermission</code> which grants <code>ConfigureAgent</code> and <code>PostAgent</code> permissions. For more information, see <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html">Resource-based policies in CodeGuru Profiler</a> in the <i>Amazon CodeGuru Profiler User Guide</i>, <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ConfigureAgent.html"> <code>ConfigureAgent</code> </a>, and <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_PostAgentProfile.html"> <code>PostAgentProfile</code> </a>. </p>

        Args:
            profiling_group_name: <p>The name of the profiling group.</p>
            action_group: <p> Specifies an action group that contains the permissions to remove from a profiling group's resource-based policy. One action group is supported, <code>agentPermissions</code>, which grants <code>ConfigureAgent</code> and <code>PostAgentProfile</code> permissions. </p>
            revision_id: <p> A universally unique identifier (UUID) for the revision of the resource-based policy from which you want to remove permissions. </p>

        Raises:
            capo_codeguruprofiler.errors.conflict_exception.ConflictException: <p>The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. </p>
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.remove_permission_request.RemovePermissionRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.remove_permission_response.RemovePermissionResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.remove_permission

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.remove_permission.async_remove_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.remove_permission_request.RemovePermissionRequest = {
            "profiling_group_name": profiling_group_name,
            "action_group": action_group,
            "revision_id": revision_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def submit_feedback(
        self,
        profiling_group_name: "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName",
        anomaly_instance_id: "capo_codeguruprofiler.types.anomaly_instance_id.AnomalyInstanceId",
        type: "capo_codeguruprofiler.types.feedback_type.FeedbackType",
        *,
        config_overrides: Optional[AsyncCodeGuruProfilerClientConfig] = None,
        comment: Optional[str] = None,
    ) -> "capo_codeguruprofiler.types.submit_feedback_response.SubmitFeedbackResponse":
        """<p>Sends feedback to CodeGuru Profiler about whether the anomaly detected by the analysis is useful or not.</p>

        Args:
            profiling_group_name: <p>The name of the profiling group that is associated with the analysis data.</p>
            anomaly_instance_id: <p>The universally unique identifier (UUID) of the <a href="https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AnomalyInstance.html"> <code>AnomalyInstance</code> </a> object that is included in the analysis data.</p>
            type: <p> The feedback tpye. Thee are two valid values, <code>Positive</code> and <code>Negative</code>. </p>
            comment: <p>Optional feedback about this anomaly.</p>

        Raises:
            capo_codeguruprofiler.errors.internal_server_exception.InternalServerException: <p>The server encountered an internal error and is unable to complete the request.</p>
            capo_codeguruprofiler.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource specified in the request does not exist.</p>
            capo_codeguruprofiler.errors.throttling_exception.ThrottlingException: <p>The request was denied due to request throttling.</p>
            capo_codeguruprofiler.errors.validation_exception.ValidationException: <p>The parameter is not valid.</p>
            capo_codeguruprofiler.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_codeguruprofiler.types.submit_feedback_request.SubmitFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_codeguruprofiler.types.submit_feedback_response.SubmitFeedbackResponse"
        ]:
            import capo_codeguruprofiler._operations.code_guru_profiler.submit_feedback

            (
                output,
                http_response,
            ) = await capo_codeguruprofiler._operations.code_guru_profiler.submit_feedback.async_submit_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_codeguruprofiler.types.submit_feedback_request.SubmitFeedbackRequest = {
            "profiling_group_name": profiling_group_name,
            "anomaly_instance_id": anomaly_instance_id,
            "type": type,
        }
        if comment is not None:
            input_["comment"] = comment

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
