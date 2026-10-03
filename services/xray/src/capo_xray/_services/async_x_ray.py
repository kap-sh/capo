"""Generated from Smithy shape ``com.amazonaws.xray#AWSXRay``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_xray._auth._signers
import capo_xray._auth._sigv4
from capo_xray._auth._identity import Credentials
from capo_xray._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_xray._auth._zapros_handler import AuthMiddleware
from capo_xray._pagination import resolve_path as _resolve_path
from capo_xray._services._aws_config import aaws_config
from capo_xray._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_xray.types.amazon_resource_name
    import capo_xray.types.batch_get_traces_request
    import capo_xray.types.batch_get_traces_result
    import capo_xray.types.boolean
    import capo_xray.types.cancel_trace_retrieval_request
    import capo_xray.types.cancel_trace_retrieval_result
    import capo_xray.types.create_group_request
    import capo_xray.types.create_group_result
    import capo_xray.types.create_sampling_rule_request
    import capo_xray.types.create_sampling_rule_result
    import capo_xray.types.delete_group_request
    import capo_xray.types.delete_group_result
    import capo_xray.types.delete_resource_policy_request
    import capo_xray.types.delete_resource_policy_result
    import capo_xray.types.delete_sampling_rule_request
    import capo_xray.types.delete_sampling_rule_result
    import capo_xray.types.ec2_instance_id
    import capo_xray.types.encryption_key_id
    import capo_xray.types.encryption_type
    import capo_xray.types.entity_selector_expression
    import capo_xray.types.filter_expression
    import capo_xray.types.get_encryption_config_request
    import capo_xray.types.get_encryption_config_result
    import capo_xray.types.get_group_request
    import capo_xray.types.get_group_result
    import capo_xray.types.get_groups_next_token
    import capo_xray.types.get_groups_request
    import capo_xray.types.get_groups_result
    import capo_xray.types.get_indexing_rules_request
    import capo_xray.types.get_indexing_rules_result
    import capo_xray.types.get_insight_events_max_results
    import capo_xray.types.get_insight_events_request
    import capo_xray.types.get_insight_events_result
    import capo_xray.types.get_insight_impact_graph_request
    import capo_xray.types.get_insight_impact_graph_result
    import capo_xray.types.get_insight_request
    import capo_xray.types.get_insight_result
    import capo_xray.types.get_insight_summaries_max_results
    import capo_xray.types.get_insight_summaries_request
    import capo_xray.types.get_insight_summaries_result
    import capo_xray.types.get_retrieved_traces_graph_request
    import capo_xray.types.get_retrieved_traces_graph_result
    import capo_xray.types.get_sampling_rules_request
    import capo_xray.types.get_sampling_rules_result
    import capo_xray.types.get_sampling_statistic_summaries_request
    import capo_xray.types.get_sampling_statistic_summaries_result
    import capo_xray.types.get_sampling_targets_request
    import capo_xray.types.get_sampling_targets_result
    import capo_xray.types.get_service_graph_request
    import capo_xray.types.get_service_graph_result
    import capo_xray.types.get_time_series_service_statistics_request
    import capo_xray.types.get_time_series_service_statistics_result
    import capo_xray.types.get_trace_graph_request
    import capo_xray.types.get_trace_graph_result
    import capo_xray.types.get_trace_segment_destination_request
    import capo_xray.types.get_trace_segment_destination_result
    import capo_xray.types.get_trace_summaries_request
    import capo_xray.types.get_trace_summaries_result
    import capo_xray.types.group_arn
    import capo_xray.types.group_name
    import capo_xray.types.group_summary
    import capo_xray.types.hostname
    import capo_xray.types.indexing_rule_value_update
    import capo_xray.types.insight_id
    import capo_xray.types.insight_state_list
    import capo_xray.types.insights_configuration
    import capo_xray.types.list_resource_policies_request
    import capo_xray.types.list_resource_policies_result
    import capo_xray.types.list_retrieved_traces_request
    import capo_xray.types.list_retrieved_traces_result
    import capo_xray.types.list_tags_for_resource_request
    import capo_xray.types.list_tags_for_resource_response
    import capo_xray.types.nullable_boolean
    import capo_xray.types.nullable_integer
    import capo_xray.types.policy_document
    import capo_xray.types.policy_name
    import capo_xray.types.policy_revision_id
    import capo_xray.types.put_encryption_config_request
    import capo_xray.types.put_encryption_config_result
    import capo_xray.types.put_resource_policy_request
    import capo_xray.types.put_resource_policy_result
    import capo_xray.types.put_telemetry_records_request
    import capo_xray.types.put_telemetry_records_result
    import capo_xray.types.put_trace_segments_request
    import capo_xray.types.put_trace_segments_result
    import capo_xray.types.resource_arn
    import capo_xray.types.resource_policy
    import capo_xray.types.resource_policy_next_token
    import capo_xray.types.retrieval_token
    import capo_xray.types.sampling_boost_statistics_document_list
    import capo_xray.types.sampling_rule
    import capo_xray.types.sampling_rule_record
    import capo_xray.types.sampling_rule_update
    import capo_xray.types.sampling_statistic_summary
    import capo_xray.types.sampling_statistics_document_list
    import capo_xray.types.sampling_strategy
    import capo_xray.types.service
    import capo_xray.types.start_trace_retrieval_request
    import capo_xray.types.start_trace_retrieval_result
    import capo_xray.types.string
    import capo_xray.types.tag
    import capo_xray.types.tag_key_list
    import capo_xray.types.tag_list
    import capo_xray.types.tag_resource_request
    import capo_xray.types.tag_resource_response
    import capo_xray.types.telemetry_record_list
    import capo_xray.types.time_range_type
    import capo_xray.types.time_series_service_statistics
    import capo_xray.types.timestamp
    import capo_xray.types.token
    import capo_xray.types.trace
    import capo_xray.types.trace_format_type
    import capo_xray.types.trace_id_list
    import capo_xray.types.trace_id_list_for_retrieval
    import capo_xray.types.trace_segment_destination
    import capo_xray.types.trace_segment_document_list
    import capo_xray.types.trace_summary
    import capo_xray.types.untag_resource_request
    import capo_xray.types.untag_resource_response
    import capo_xray.types.update_group_request
    import capo_xray.types.update_group_result
    import capo_xray.types.update_indexing_rule_request
    import capo_xray.types.update_indexing_rule_result
    import capo_xray.types.update_sampling_rule_request
    import capo_xray.types.update_sampling_rule_result
    import capo_xray.types.update_trace_segment_destination_request
    import capo_xray.types.update_trace_segment_destination_result


class AsyncXRayClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncXRayClient:
    """A client for the ``XRay`` service.

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
        self._config = AsyncXRayClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncXRayClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncXRayClientConfig = config_overrides or {}
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

    async def batch_get_traces(
        self,
        trace_ids: "capo_xray.types.trace_id_list.TraceIdList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.batch_get_traces_result.BatchGetTracesResult":
        """<note> <p>You cannot find traces through this API if Transaction Search is enabled since trace is not indexed in X-Ray.</p> </note> <p>Retrieves a list of traces specified by ID. Each trace is a collection of segment documents that originates from a single request. Use <code>GetTraceSummaries</code> to get a list of trace IDs.</p>

        Args:
            trace_ids: <p>Specify the trace IDs of requests for which to retrieve segments.</p>
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.batch_get_traces_request.BatchGetTracesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.batch_get_traces_result.BatchGetTracesResult"
        ]:
            import capo_xray._operations.awsx_ray.batch_get_traces

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.batch_get_traces.async_batch_get_traces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.batch_get_traces_request.BatchGetTracesRequest = {
            "trace_ids": trace_ids
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

    async def iter_batch_get_traces(
        self,
        trace_ids: "capo_xray.types.trace_id_list.TraceIdList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.trace.Trace]":
        _token = next_token
        while True:
            _response = await self.batch_get_traces(
                trace_ids,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("traces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_trace_retrieval(
        self,
        retrieval_token: "capo_xray.types.retrieval_token.RetrievalToken",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.cancel_trace_retrieval_result.CancelTraceRetrievalResult":
        """<p> Cancels an ongoing trace retrieval job initiated by <code>StartTraceRetrieval</code> using the provided <code>RetrievalToken</code>. A successful cancellation will return an HTTP 200 response. </p>

        Args:
            retrieval_token: <p> Retrieval token. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.cancel_trace_retrieval_request.CancelTraceRetrievalRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.cancel_trace_retrieval_result.CancelTraceRetrievalResult"
        ]:
            import capo_xray._operations.awsx_ray.cancel_trace_retrieval

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.cancel_trace_retrieval.async_cancel_trace_retrieval(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.cancel_trace_retrieval_request.CancelTraceRetrievalRequest = {
            "retrieval_token": retrieval_token
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_group(
        self,
        group_name: "capo_xray.types.group_name.GroupName",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        filter_expression: Optional[
            "capo_xray.types.filter_expression.FilterExpression"
        ] = None,
        insights_configuration: Optional[
            "capo_xray.types.insights_configuration.InsightsConfiguration"
        ] = None,
        tags: Optional["capo_xray.types.tag_list.TagList"] = None,
    ) -> "capo_xray.types.create_group_result.CreateGroupResult":
        """<p>Creates a group resource with a name and a filter expression. </p>

        Args:
            group_name: <p>The case-sensitive name of the new group. Default is a reserved name and names must be unique.</p>
            filter_expression: <p>The filter expression defining criteria by which to group traces.</p>
            insights_configuration: <p>The structure containing configurations related to insights.</p> <ul> <li> <p>The InsightsEnabled boolean can be set to true to enable insights for the new group or false to disable insights for the new group.</p> </li> <li> <p>The NotificationsEnabled boolean can be set to true to enable insights notifications for the new group. Notifications may only be enabled on a group with InsightsEnabled set to true.</p> </li> </ul>
            tags: <p>A map that contains one or more tag keys and tag values to attach to an X-Ray group. For more information about ways to use tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>Maximum number of user-applied tags per resource: 50</p> </li> <li> <p>Maximum tag key length: 128 Unicode characters</p> </li> <li> <p>Maximum tag value length: 256 Unicode characters</p> </li> <li> <p>Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - and @</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for keys; it's reserved for Amazon Web Services use.</p> </li> </ul>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.create_group_request.CreateGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.create_group_result.CreateGroupResult"
        ]:
            import capo_xray._operations.awsx_ray.create_group

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.create_group.async_create_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.create_group_request.CreateGroupRequest = {
            "group_name": group_name
        }
        if filter_expression is not None:
            input_["filter_expression"] = filter_expression
        if insights_configuration is not None:
            input_["insights_configuration"] = insights_configuration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_sampling_rule(
        self,
        sampling_rule: "capo_xray.types.sampling_rule.SamplingRule",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        tags: Optional["capo_xray.types.tag_list.TagList"] = None,
    ) -> "capo_xray.types.create_sampling_rule_result.CreateSamplingRuleResult":
        """<p>Creates a rule to control sampling behavior for instrumented applications. Services retrieve rules with <a href="https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html">GetSamplingRules</a>, and evaluate each rule in ascending order of <i>priority</i> for each request. If a rule matches, the service records a trace, borrowing it from the reservoir size. After 10 seconds, the service reports back to X-Ray with <a href="https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html">GetSamplingTargets</a> to get updated versions of each in-use rule. The updated rule contains a trace quota that the service can use instead of borrowing from the reservoir.</p>

        Args:
            sampling_rule: <p>The rule definition.</p>
            tags: <p>A map that contains one or more tag keys and tag values to attach to an X-Ray sampling rule. For more information about ways to use tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>Maximum number of user-applied tags per resource: 50</p> </li> <li> <p>Maximum tag key length: 128 Unicode characters</p> </li> <li> <p>Maximum tag value length: 256 Unicode characters</p> </li> <li> <p>Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - and @</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for keys; it's reserved for Amazon Web Services use.</p> </li> </ul>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.rule_limit_exceeded_exception.RuleLimitExceededException: <p>You have reached the maximum number of sampling rules.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.create_sampling_rule_request.CreateSamplingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.create_sampling_rule_result.CreateSamplingRuleResult"
        ]:
            import capo_xray._operations.awsx_ray.create_sampling_rule

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.create_sampling_rule.async_create_sampling_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.create_sampling_rule_request.CreateSamplingRuleRequest = {
            "sampling_rule": sampling_rule
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

    async def delete_group(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
    ) -> "capo_xray.types.delete_group_result.DeleteGroupResult":
        """<p>Deletes a group resource.</p>

        Args:
            group_name: <p>The case-sensitive name of the group.</p>
            group_arn: <p>The ARN of the group that was generated on creation.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.delete_group_request.DeleteGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.delete_group_result.DeleteGroupResult"
        ]:
            import capo_xray._operations.awsx_ray.delete_group

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.delete_group.async_delete_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.delete_group_request.DeleteGroupRequest = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group_arn is not None:
            input_["group_arn"] = group_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        policy_name: "capo_xray.types.policy_name.PolicyName",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        policy_revision_id: Optional[
            "capo_xray.types.policy_revision_id.PolicyRevisionId"
        ] = None,
    ) -> "capo_xray.types.delete_resource_policy_result.DeleteResourcePolicyResult":
        """<p>Deletes a resource policy from the target Amazon Web Services account.</p>

        Args:
            policy_name: <p>The name of the resource policy to delete.</p>
            policy_revision_id: <p>Specifies a specific policy revision to delete. Provide a <code>PolicyRevisionId</code> to ensure an atomic delete operation. If the provided revision id does not match the latest policy revision id, an <code>InvalidPolicyRevisionIdException</code> exception is returned. </p>

        Raises:
            capo_xray.errors.invalid_policy_revision_id_exception.InvalidPolicyRevisionIdException: <p>A policy revision id was provided which does not match the latest policy revision. This exception is also if a policy revision id of 0 is provided via <code>PutResourcePolicy</code> and a policy with the same name already exists.</p>
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.delete_resource_policy_result.DeleteResourcePolicyResult"
        ]:
            import capo_xray._operations.awsx_ray.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "policy_name": policy_name
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_sampling_rule(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        rule_name: Optional["capo_xray.types.string.String"] = None,
        rule_arn: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.delete_sampling_rule_result.DeleteSamplingRuleResult":
        """<p>Deletes a sampling rule.</p>

        Args:
            rule_name: <p>The name of the sampling rule. Specify a rule by either name or ARN, but not both.</p>
            rule_arn: <p>The ARN of the sampling rule. Specify a rule by either name or ARN, but not both.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.delete_sampling_rule_request.DeleteSamplingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.delete_sampling_rule_result.DeleteSamplingRuleResult"
        ]:
            import capo_xray._operations.awsx_ray.delete_sampling_rule

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.delete_sampling_rule.async_delete_sampling_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.delete_sampling_rule_request.DeleteSamplingRuleRequest = {}
        if rule_name is not None:
            input_["rule_name"] = rule_name
        if rule_arn is not None:
            input_["rule_arn"] = rule_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_encryption_config(
        self, *, config_overrides: Optional[AsyncXRayClientConfig] = None
    ) -> "capo_xray.types.get_encryption_config_result.GetEncryptionConfigResult":
        """<p>Retrieves the current encryption configuration for X-Ray data.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_encryption_config_request.GetEncryptionConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_encryption_config_result.GetEncryptionConfigResult"
        ]:
            import capo_xray._operations.awsx_ray.get_encryption_config

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_encryption_config.async_get_encryption_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_encryption_config_request.GetEncryptionConfigRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_group(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
    ) -> "capo_xray.types.get_group_result.GetGroupResult":
        """<p>Retrieves group resource details.</p>

        Args:
            group_name: <p>The case-sensitive name of the group.</p>
            group_arn: <p>The ARN of the group that was generated on creation.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_group_request.GetGroupRequest]",
        ) -> AsyncOperationResponse["capo_xray.types.get_group_result.GetGroupResult"]:
            import capo_xray._operations.awsx_ray.get_group

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_group.async_get_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_group_request.GetGroupRequest = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group_arn is not None:
            input_["group_arn"] = group_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_groups(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional[
            "capo_xray.types.get_groups_next_token.GetGroupsNextToken"
        ] = None,
    ) -> "capo_xray.types.get_groups_result.GetGroupsResult":
        """<p>Retrieves all active group details.</p>

        Args:
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_groups_request.GetGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_groups_result.GetGroupsResult"
        ]:
            import capo_xray._operations.awsx_ray.get_groups

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_groups.async_get_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_groups_request.GetGroupsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_groups(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional[
            "capo_xray.types.get_groups_next_token.GetGroupsNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_xray.types.group_summary.GroupSummary]":
        _token = next_token
        while True:
            _response = await self.get_groups(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_indexing_rules(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_indexing_rules_result.GetIndexingRulesResult":
        """<p> Retrieves all indexing rules.</p> <p>Indexing rules are used to determine the server-side sampling rate for spans ingested through the CloudWatchLogs destination and indexed by X-Ray. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html">Transaction Search</a>.</p>

        Args:
            next_token: <p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_indexing_rules_request.GetIndexingRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_indexing_rules_result.GetIndexingRulesResult"
        ]:
            import capo_xray._operations.awsx_ray.get_indexing_rules

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_indexing_rules.async_get_indexing_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_indexing_rules_request.GetIndexingRulesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_insight(
        self,
        insight_id: "capo_xray.types.insight_id.InsightId",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.get_insight_result.GetInsightResult":
        """<p>Retrieves the summary information of an insight. This includes impact to clients and root cause services, the top anomalous services, the category, the state of the insight, and the start and end time of the insight.</p>

        Args:
            insight_id: <p>The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_insight_request.GetInsightRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_insight_result.GetInsightResult"
        ]:
            import capo_xray._operations.awsx_ray.get_insight

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_insight.async_get_insight(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_insight_request.GetInsightRequest = {
            "insight_id": insight_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_insight_events(
        self,
        insight_id: "capo_xray.types.insight_id.InsightId",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        max_results: Optional[
            "capo_xray.types.get_insight_events_max_results.GetInsightEventsMaxResults"
        ] = None,
        next_token: Optional["capo_xray.types.token.Token"] = None,
    ) -> "capo_xray.types.get_insight_events_result.GetInsightEventsResult":
        """<p>X-Ray reevaluates insights periodically until they're resolved, and records each intermediate state as an event. You can review an insight's events in the Impact Timeline on the Inspect page in the X-Ray console.</p>

        Args:
            insight_id: <p>The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.</p>
            max_results: <p>Used to retrieve at most the specified value of events.</p>
            next_token: <p>Specify the pagination token returned by a previous request to retrieve the next page of events. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_insight_events_request.GetInsightEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_insight_events_result.GetInsightEventsResult"
        ]:
            import capo_xray._operations.awsx_ray.get_insight_events

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_insight_events.async_get_insight_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_insight_events_request.GetInsightEventsRequest = {
            "insight_id": insight_id
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

    async def iter_get_insight_events(
        self,
        insight_id: "capo_xray.types.insight_id.InsightId",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        max_results: Optional[
            "capo_xray.types.get_insight_events_max_results.GetInsightEventsMaxResults"
        ] = None,
        next_token: Optional["capo_xray.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_xray.types.get_insight_events_result.GetInsightEventsResult]":
        _token = next_token
        while True:
            _response = await self.get_insight_events(
                insight_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_insight_impact_graph(
        self,
        insight_id: "capo_xray.types.insight_id.InsightId",
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.token.Token"] = None,
    ) -> "capo_xray.types.get_insight_impact_graph_result.GetInsightImpactGraphResult":
        """<p>Retrieves a service graph structure filtered by the specified insight. The service graph is limited to only structural information. For a complete service graph, use this API with the GetServiceGraph API.</p>

        Args:
            insight_id: <p>The insight's unique identifier. Use the GetInsightSummaries action to retrieve an InsightId.</p>
            start_time: <p>The estimated start time of the insight, in Unix time seconds. The StartTime is inclusive of the value provided and can't be more than 30 days old.</p>
            end_time: <p>The estimated end time of the insight, in Unix time seconds. The EndTime is exclusive of the value provided. The time range between the start time and end time can't be more than six hours. </p>
            next_token: <p>Specify the pagination token returned by a previous request to retrieve the next page of results. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_insight_impact_graph_request.GetInsightImpactGraphRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_insight_impact_graph_result.GetInsightImpactGraphResult"
        ]:
            import capo_xray._operations.awsx_ray.get_insight_impact_graph

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_insight_impact_graph.async_get_insight_impact_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_insight_impact_graph_request.GetInsightImpactGraphRequest = {
            "insight_id": insight_id,
            "start_time": start_time,
            "end_time": end_time,
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

    async def get_insight_summaries(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        states: Optional["capo_xray.types.insight_state_list.InsightStateList"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        max_results: Optional[
            "capo_xray.types.get_insight_summaries_max_results.GetInsightSummariesMaxResults"
        ] = None,
        next_token: Optional["capo_xray.types.token.Token"] = None,
    ) -> "capo_xray.types.get_insight_summaries_result.GetInsightSummariesResult":
        """<p>Retrieves the summaries of all insights in the specified group matching the provided filter values.</p>

        Args:
            states: <p>The list of insight states. </p>
            group_arn: <p>The Amazon Resource Name (ARN) of the group. Required if the GroupName isn't provided.</p>
            group_name: <p>The name of the group. Required if the GroupARN isn't provided.</p>
            start_time: <p>The beginning of the time frame in which the insights started. The start time can't be more than 30 days old.</p>
            end_time: <p>The end of the time frame in which the insights ended. The end time can't be more than 30 days old.</p>
            max_results: <p>The maximum number of results to display.</p>
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_insight_summaries_request.GetInsightSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_insight_summaries_result.GetInsightSummariesResult"
        ]:
            import capo_xray._operations.awsx_ray.get_insight_summaries

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_insight_summaries.async_get_insight_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_insight_summaries_request.GetInsightSummariesRequest = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if states is not None:
            input_["states"] = states
        if group_arn is not None:
            input_["group_arn"] = group_arn
        if group_name is not None:
            input_["group_name"] = group_name
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

    async def iter_get_insight_summaries(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        states: Optional["capo_xray.types.insight_state_list.InsightStateList"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        max_results: Optional[
            "capo_xray.types.get_insight_summaries_max_results.GetInsightSummariesMaxResults"
        ] = None,
        next_token: Optional["capo_xray.types.token.Token"] = None,
    ) -> "AsyncIterator[capo_xray.types.get_insight_summaries_result.GetInsightSummariesResult]":
        _token = next_token
        while True:
            _response = await self.get_insight_summaries(
                start_time,
                end_time,
                config_overrides=config_overrides,
                states=states,
                group_arn=group_arn,
                group_name=group_name,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_retrieved_traces_graph(
        self,
        retrieval_token: "capo_xray.types.retrieval_token.RetrievalToken",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_retrieved_traces_graph_result.GetRetrievedTracesGraphResult":
        """<p> Retrieves a service graph for traces based on the specified <code>RetrievalToken</code> from the CloudWatch log group generated by Transaction Search. This API does not initiate a retrieval job. You must first execute <code>StartTraceRetrieval</code> to obtain the required <code>RetrievalToken</code>. </p> <p>The trace graph describes services that process incoming requests and any downstream services they call, which may include Amazon Web Services resources, external APIs, or databases.</p> <p>The response is empty until the <code>RetrievalStatus</code> is <i>COMPLETE</i>. Retry the request after the status changes from <i>RUNNING</i> or <i>SCHEDULED</i> to <i>COMPLETE</i> to access the full service graph.</p> <p> When CloudWatch log is the destination, this API can support cross-account observability and service graph retrieval across linked accounts.</p> <p>For retrieving graphs from X-Ray directly as opposed to the Transaction-Search Log group, see <a href="https://docs.aws.amazon.com/xray/latest/api/API_GetTraceGraph.html">GetTraceGraph</a>.</p>

        Args:
            retrieval_token: <p> Retrieval token. </p>
            next_token: <p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_retrieved_traces_graph_request.GetRetrievedTracesGraphRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_retrieved_traces_graph_result.GetRetrievedTracesGraphResult"
        ]:
            import capo_xray._operations.awsx_ray.get_retrieved_traces_graph

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_retrieved_traces_graph.async_get_retrieved_traces_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_retrieved_traces_graph_request.GetRetrievedTracesGraphRequest = {
            "retrieval_token": retrieval_token
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

    async def get_sampling_rules(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_sampling_rules_result.GetSamplingRulesResult":
        """<p>Retrieves all sampling rules.</p>

        Args:
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_sampling_rules_request.GetSamplingRulesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_sampling_rules_result.GetSamplingRulesResult"
        ]:
            import capo_xray._operations.awsx_ray.get_sampling_rules

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_sampling_rules.async_get_sampling_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_sampling_rules_request.GetSamplingRulesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_sampling_rules(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.sampling_rule_record.SamplingRuleRecord]":
        _token = next_token
        while True:
            _response = await self.get_sampling_rules(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sampling_rule_records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_sampling_statistic_summaries(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_sampling_statistic_summaries_result.GetSamplingStatisticSummariesResult":
        """<p>Retrieves information about recent sampling results for all sampling rules.</p>

        Args:
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_sampling_statistic_summaries_request.GetSamplingStatisticSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_sampling_statistic_summaries_result.GetSamplingStatisticSummariesResult"
        ]:
            import capo_xray._operations.awsx_ray.get_sampling_statistic_summaries

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_sampling_statistic_summaries.async_get_sampling_statistic_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_sampling_statistic_summaries_request.GetSamplingStatisticSummariesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_sampling_statistic_summaries(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.sampling_statistic_summary.SamplingStatisticSummary]":
        _token = next_token
        while True:
            _response = await self.get_sampling_statistic_summaries(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sampling_statistic_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_sampling_targets(
        self,
        sampling_statistics_documents: "capo_xray.types.sampling_statistics_document_list.SamplingStatisticsDocumentList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        sampling_boost_statistics_documents: Optional[
            "capo_xray.types.sampling_boost_statistics_document_list.SamplingBoostStatisticsDocumentList"
        ] = None,
    ) -> "capo_xray.types.get_sampling_targets_result.GetSamplingTargetsResult":
        """<p>Requests a sampling quota for rules that the service is using to sample requests. </p>

        Args:
            sampling_statistics_documents: <p>Information about rules that the service is using to sample requests.</p>
            sampling_boost_statistics_documents: <p>Information about rules that the service is using to boost sampling rate.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_sampling_targets_request.GetSamplingTargetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_sampling_targets_result.GetSamplingTargetsResult"
        ]:
            import capo_xray._operations.awsx_ray.get_sampling_targets

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_sampling_targets.async_get_sampling_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_sampling_targets_request.GetSamplingTargetsRequest = {
            "sampling_statistics_documents": sampling_statistics_documents
        }
        if sampling_boost_statistics_documents is not None:
            input_["sampling_boost_statistics_documents"] = (
                sampling_boost_statistics_documents
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service_graph(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_service_graph_result.GetServiceGraphResult":
        """<p>Retrieves a document that describes services that process incoming requests, and downstream services that they call as a result. Root services process incoming requests and make calls to downstream services. Root services are applications that use the <a href="https://docs.aws.amazon.com/xray/index.html">Amazon Web Services X-Ray SDK</a>. Downstream services can be other applications, Amazon Web Services resources, HTTP web APIs, or SQL databases.</p>

        Args:
            start_time: <p>The start of the time frame for which to generate a graph.</p>
            end_time: <p>The end of the timeframe for which to generate a graph.</p>
            group_name: <p>The name of a group based on which you want to generate a graph.</p>
            group_arn: <p>The Amazon Resource Name (ARN) of a group based on which you want to generate a graph.</p>
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_service_graph_request.GetServiceGraphRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_service_graph_result.GetServiceGraphResult"
        ]:
            import capo_xray._operations.awsx_ray.get_service_graph

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_service_graph.async_get_service_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_service_graph_request.GetServiceGraphRequest = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if group_name is not None:
            input_["group_name"] = group_name
        if group_arn is not None:
            input_["group_arn"] = group_arn
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_service_graph(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.service.Service]":
        _token = next_token
        while True:
            _response = await self.get_service_graph(
                start_time,
                end_time,
                config_overrides=config_overrides,
                group_name=group_name,
                group_arn=group_arn,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_time_series_service_statistics(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
        entity_selector_expression: Optional[
            "capo_xray.types.entity_selector_expression.EntitySelectorExpression"
        ] = None,
        period: Optional["capo_xray.types.nullable_integer.NullableInteger"] = None,
        forecast_statistics: Optional[
            "capo_xray.types.nullable_boolean.NullableBoolean"
        ] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_time_series_service_statistics_result.GetTimeSeriesServiceStatisticsResult":
        """<p>Get an aggregation of service statistics defined by a specific time range.</p>

        Args:
            start_time: <p>The start of the time frame for which to aggregate statistics.</p>
            end_time: <p>The end of the time frame for which to aggregate statistics.</p>
            group_name: <p>The case-sensitive name of the group for which to pull statistics from.</p>
            group_arn: <p>The Amazon Resource Name (ARN) of the group for which to pull statistics from.</p>
            entity_selector_expression: <p>A filter expression defining entities that will be aggregated for statistics. Supports ID, service, and edge functions. If no selector expression is specified, edge statistics are returned. </p>
            period: <p>Aggregation period in seconds.</p>
            forecast_statistics: <p>The forecasted high and low fault count values. Forecast enabled requests require the EntitySelectorExpression ID be provided.</p>
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_time_series_service_statistics_request.GetTimeSeriesServiceStatisticsRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_time_series_service_statistics_result.GetTimeSeriesServiceStatisticsResult"
        ]:
            import capo_xray._operations.awsx_ray.get_time_series_service_statistics

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_time_series_service_statistics.async_get_time_series_service_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_time_series_service_statistics_request.GetTimeSeriesServiceStatisticsRequest = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if group_name is not None:
            input_["group_name"] = group_name
        if group_arn is not None:
            input_["group_arn"] = group_arn
        if entity_selector_expression is not None:
            input_["entity_selector_expression"] = entity_selector_expression
        if period is not None:
            input_["period"] = period
        if forecast_statistics is not None:
            input_["forecast_statistics"] = forecast_statistics
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_time_series_service_statistics(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
        entity_selector_expression: Optional[
            "capo_xray.types.entity_selector_expression.EntitySelectorExpression"
        ] = None,
        period: Optional["capo_xray.types.nullable_integer.NullableInteger"] = None,
        forecast_statistics: Optional[
            "capo_xray.types.nullable_boolean.NullableBoolean"
        ] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.time_series_service_statistics.TimeSeriesServiceStatistics]":
        _token = next_token
        while True:
            _response = await self.get_time_series_service_statistics(
                start_time,
                end_time,
                config_overrides=config_overrides,
                group_name=group_name,
                group_arn=group_arn,
                entity_selector_expression=entity_selector_expression,
                period=period,
                forecast_statistics=forecast_statistics,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("time_series_service_statistics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_trace_graph(
        self,
        trace_ids: "capo_xray.types.trace_id_list.TraceIdList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_trace_graph_result.GetTraceGraphResult":
        """<p>Retrieves a service graph for one or more specific trace IDs.</p>

        Args:
            trace_ids: <p>Trace IDs of requests for which to generate a service graph.</p>
            next_token: <p>Pagination token.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_trace_graph_request.GetTraceGraphRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_trace_graph_result.GetTraceGraphResult"
        ]:
            import capo_xray._operations.awsx_ray.get_trace_graph

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_trace_graph.async_get_trace_graph(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_trace_graph_request.GetTraceGraphRequest = {
            "trace_ids": trace_ids
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

    async def iter_get_trace_graph(
        self,
        trace_ids: "capo_xray.types.trace_id_list.TraceIdList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.service.Service]":
        _token = next_token
        while True:
            _response = await self.get_trace_graph(
                trace_ids,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_trace_segment_destination(
        self, *, config_overrides: Optional[AsyncXRayClientConfig] = None
    ) -> "capo_xray.types.get_trace_segment_destination_result.GetTraceSegmentDestinationResult":
        """<p> Retrieves the current destination of data sent to <code>PutTraceSegments</code> and <i>OpenTelemetry protocol (OTLP)</i> endpoint. The Transaction Search feature requires a CloudWatchLogs destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html">Transaction Search</a> and <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-OpenTelemetry-Sections.html">OpenTelemetry</a>. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_trace_segment_destination_request.GetTraceSegmentDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_trace_segment_destination_result.GetTraceSegmentDestinationResult"
        ]:
            import capo_xray._operations.awsx_ray.get_trace_segment_destination

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_trace_segment_destination.async_get_trace_segment_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_trace_segment_destination_request.GetTraceSegmentDestinationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_trace_summaries(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        time_range_type: Optional[
            "capo_xray.types.time_range_type.TimeRangeType"
        ] = None,
        sampling: Optional["capo_xray.types.nullable_boolean.NullableBoolean"] = None,
        sampling_strategy: Optional[
            "capo_xray.types.sampling_strategy.SamplingStrategy"
        ] = None,
        filter_expression: Optional[
            "capo_xray.types.filter_expression.FilterExpression"
        ] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.get_trace_summaries_result.GetTraceSummariesResult":
        """<p>Retrieves IDs and annotations for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to <code>BatchGetTraces</code>.</p> <p>A filter expression can target traced requests that hit specific service nodes or edges, have errors, or come from a known user. For example, the following filter expression targets traces that pass through <code>api.example.com</code>:</p> <p> <code>service("api.example.com")</code> </p> <p>This filter expression finds traces that have an annotation named <code>account</code> with the value <code>12345</code>:</p> <p> <code>annotation.account = "12345"</code> </p> <p>For a full list of indexed fields and keywords that you can use in filter expressions, see <a href="https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-console.html#xray-console-filters">Use filter expressions</a> in the <i>Amazon Web Services X-Ray Developer Guide</i>.</p>

        Args:
            start_time: <p>The start of the time frame for which to retrieve traces.</p>
            end_time: <p>The end of the time frame for which to retrieve traces.</p>
            time_range_type: <p>Query trace summaries by TraceId (trace start time), Event (trace update time), or Service (trace segment end time).</p>
            sampling: <p>Set to <code>true</code> to get summaries for only a subset of available traces.</p>
            sampling_strategy: <p>A parameter to indicate whether to enable sampling on trace summaries. Input parameters are Name and Value.</p>
            filter_expression: <p>Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.</p>
            next_token: <p>Specify the pagination token returned by a previous request to retrieve the next page of results.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.get_trace_summaries_request.GetTraceSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.get_trace_summaries_result.GetTraceSummariesResult"
        ]:
            import capo_xray._operations.awsx_ray.get_trace_summaries

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.get_trace_summaries.async_get_trace_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.get_trace_summaries_request.GetTraceSummariesRequest = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if time_range_type is not None:
            input_["time_range_type"] = time_range_type
        if sampling is not None:
            input_["sampling"] = sampling
        if sampling_strategy is not None:
            input_["sampling_strategy"] = sampling_strategy
        if filter_expression is not None:
            input_["filter_expression"] = filter_expression
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_trace_summaries(
        self,
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        time_range_type: Optional[
            "capo_xray.types.time_range_type.TimeRangeType"
        ] = None,
        sampling: Optional["capo_xray.types.nullable_boolean.NullableBoolean"] = None,
        sampling_strategy: Optional[
            "capo_xray.types.sampling_strategy.SamplingStrategy"
        ] = None,
        filter_expression: Optional[
            "capo_xray.types.filter_expression.FilterExpression"
        ] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.trace_summary.TraceSummary]":
        _token = next_token
        while True:
            _response = await self.get_trace_summaries(
                start_time,
                end_time,
                config_overrides=config_overrides,
                time_range_type=time_range_type,
                sampling=sampling,
                sampling_strategy=sampling_strategy,
                filter_expression=filter_expression,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("trace_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_policies(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional[
            "capo_xray.types.resource_policy_next_token.ResourcePolicyNextToken"
        ] = None,
    ) -> "capo_xray.types.list_resource_policies_result.ListResourcePoliciesResult":
        """<p>Returns the list of resource policies in the target Amazon Web Services account.</p>

        Args:
            next_token: <p>Not currently supported.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.list_resource_policies_request.ListResourcePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.list_resource_policies_result.ListResourcePoliciesResult"
        ]:
            import capo_xray._operations.awsx_ray.list_resource_policies

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.list_resource_policies.async_list_resource_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.list_resource_policies_request.ListResourcePoliciesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_resource_policies(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional[
            "capo_xray.types.resource_policy_next_token.ResourcePolicyNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_xray.types.resource_policy.ResourcePolicy]":
        _token = next_token
        while True:
            _response = await self.list_resource_policies(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resource_policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_retrieved_traces(
        self,
        retrieval_token: "capo_xray.types.retrieval_token.RetrievalToken",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        trace_format: Optional[
            "capo_xray.types.trace_format_type.TraceFormatType"
        ] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.list_retrieved_traces_result.ListRetrievedTracesResult":
        """<p> Retrieves a list of traces for a given <code>RetrievalToken</code> from the CloudWatch log group generated by Transaction Search. For information on what each trace returns, see <a href="https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html">BatchGetTraces</a>. </p> <p>This API does not initiate a retrieval process. To start a trace retrieval, use <code>StartTraceRetrieval</code>, which generates the required <code>RetrievalToken</code>.</p> <p> When the <code>RetrievalStatus</code> is not <i>COMPLETE</i>, the API will return an empty response. Retry the request once the retrieval has completed to access the full list of traces.</p> <p>For cross-account observability, this API can retrieve traces from linked accounts when CloudWatch log is set as the destination across relevant accounts. For more details, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p> <p>For retrieving data from X-Ray directly as opposed to the Transaction Search generated log group, see <a href="https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html">BatchGetTraces</a>.</p>

        Args:
            retrieval_token: <p> Retrieval token. </p>
            trace_format: <p> Format of the requested traces. </p>
            next_token: <p> Specify the pagination token returned by a previous request to retrieve the next page of indexes. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.list_retrieved_traces_request.ListRetrievedTracesRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.list_retrieved_traces_result.ListRetrievedTracesResult"
        ]:
            import capo_xray._operations.awsx_ray.list_retrieved_traces

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.list_retrieved_traces.async_list_retrieved_traces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.list_retrieved_traces_request.ListRetrievedTracesRequest = {
            "retrieval_token": retrieval_token
        }
        if trace_format is not None:
            input_["trace_format"] = trace_format
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_xray.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "capo_xray.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Returns a list of tags that are applied to the specified Amazon Web Services X-Ray group or sampling rule.</p>

        Args:
            resource_arn: <p>The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.</p>
            next_token: <p>A pagination token. If multiple pages of results are returned, use the <code>NextToken</code> value returned with the current page of results as the value of this parameter to get the next page of results.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_xray._operations.awsx_ray.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
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

    async def iter_list_tags_for_resource(
        self,
        resource_arn: "capo_xray.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        next_token: Optional["capo_xray.types.string.String"] = None,
    ) -> "AsyncIterator[capo_xray.types.tag.Tag]":
        _token = next_token
        while True:
            _response = await self.list_tags_for_resource(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tags",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_encryption_config(
        self,
        type: "capo_xray.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        key_id: Optional["capo_xray.types.encryption_key_id.EncryptionKeyId"] = None,
    ) -> "capo_xray.types.put_encryption_config_result.PutEncryptionConfigResult":
        """<p>Updates the encryption configuration for X-Ray data.</p>

        Args:
            key_id: <p>An Amazon Web Services KMS key in one of the following formats:</p> <ul> <li> <p> <b>Alias</b> - The name of the key. For example, <code>alias/MyKey</code>.</p> </li> <li> <p> <b>Key ID</b> - The KMS key ID of the key. For example, <code>ae4aa6d49-a4d8-9df9-a475-4ff6d7898456</code>. Amazon Web Services X-Ray does not support asymmetric KMS keys.</p> </li> <li> <p> <b>ARN</b> - The full Amazon Resource Name of the key ID or alias. For example, <code>arn:aws:kms:us-east-2:123456789012:key/ae4aa6d49-a4d8-9df9-a475-4ff6d7898456</code>. Use this format to specify a key in a different account.</p> </li> </ul> <p>Omit this key if you set <code>Type</code> to <code>NONE</code>.</p>
            type: <p>The type of encryption. Set to <code>KMS</code> to use your own key for encryption. Set to <code>NONE</code> for default encryption.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.put_encryption_config_request.PutEncryptionConfigRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.put_encryption_config_result.PutEncryptionConfigResult"
        ]:
            import capo_xray._operations.awsx_ray.put_encryption_config

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.put_encryption_config.async_put_encryption_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.put_encryption_config_request.PutEncryptionConfigRequest = {
            "type": type
        }
        if key_id is not None:
            input_["key_id"] = key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        policy_name: "capo_xray.types.policy_name.PolicyName",
        policy_document: "capo_xray.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        policy_revision_id: Optional[
            "capo_xray.types.policy_revision_id.PolicyRevisionId"
        ] = None,
        bypass_policy_lockout_check: Optional["capo_xray.types.boolean.Boolean"] = None,
    ) -> "capo_xray.types.put_resource_policy_result.PutResourcePolicyResult":
        """<p> Sets the resource policy to grant one or more Amazon Web Services services and accounts permissions to access X-Ray. Each resource policy will be associated with a specific Amazon Web Services account. Each Amazon Web Services account can have a maximum of 5 resource policies, and each policy name must be unique within that account. The maximum size of each resource policy is 5KB. </p>

        Args:
            policy_name: <p>The name of the resource policy. Must be unique within a specific Amazon Web Services account.</p>
            policy_document: <p>The resource policy document, which can be up to 5kb in size.</p>
            policy_revision_id: <p>Specifies a specific policy revision, to ensure an atomic create operation. By default the resource policy is created if it does not exist, or updated with an incremented revision id. The revision id is unique to each policy in the account.</p> <p>If the policy revision id does not match the latest revision id, the operation will fail with an <code>InvalidPolicyRevisionIdException</code> exception. You can also provide a <code>PolicyRevisionId</code> of 0. In this case, the operation will fail with an <code>InvalidPolicyRevisionIdException</code> exception if a resource policy with the same name already exists. </p>
            bypass_policy_lockout_check: <p>A flag to indicate whether to bypass the resource policy lockout safety check.</p> <important> <p>Setting this value to true increases the risk that the policy becomes unmanageable. Do not set this value to true indiscriminately.</p> </important> <p>Use this parameter only when you include a policy in the request and you intend to prevent the principal that is making the request from making a subsequent <code>PutResourcePolicy</code> request.</p> <p>The default value is false.</p>

        Raises:
            capo_xray.errors.invalid_policy_revision_id_exception.InvalidPolicyRevisionIdException: <p>A policy revision id was provided which does not match the latest policy revision. This exception is also if a policy revision id of 0 is provided via <code>PutResourcePolicy</code> and a policy with the same name already exists.</p>
            capo_xray.errors.lockout_prevention_exception.LockoutPreventionException: <p>The provided resource policy would prevent the caller of this request from calling PutResourcePolicy in the future.</p>
            capo_xray.errors.malformed_policy_document_exception.MalformedPolicyDocumentException: <p>Invalid policy document provided in request.</p>
            capo_xray.errors.policy_count_limit_exceeded_exception.PolicyCountLimitExceededException: <p>Exceeded the maximum number of resource policies for a target Amazon Web Services account.</p>
            capo_xray.errors.policy_size_limit_exceeded_exception.PolicySizeLimitExceededException: <p>Exceeded the maximum size for a resource policy.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.put_resource_policy_result.PutResourcePolicyResult"
        ]:
            import capo_xray._operations.awsx_ray.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "policy_name": policy_name,
            "policy_document": policy_document,
        }
        if policy_revision_id is not None:
            input_["policy_revision_id"] = policy_revision_id
        if bypass_policy_lockout_check is not None:
            input_["bypass_policy_lockout_check"] = bypass_policy_lockout_check

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_telemetry_records(
        self,
        telemetry_records: "capo_xray.types.telemetry_record_list.TelemetryRecordList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        ec2_instance_id: Optional[
            "capo_xray.types.ec2_instance_id.EC2InstanceId"
        ] = None,
        hostname: Optional["capo_xray.types.hostname.Hostname"] = None,
        resource_arn: Optional["capo_xray.types.resource_arn.ResourceARN"] = None,
    ) -> "capo_xray.types.put_telemetry_records_result.PutTelemetryRecordsResult":
        """<p>Used by the Amazon Web Services X-Ray daemon to upload telemetry.</p>

        Args:
            telemetry_records: <p></p>
            ec2_instance_id: <p></p>
            hostname: <p></p>
            resource_arn: <p></p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.put_telemetry_records_request.PutTelemetryRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.put_telemetry_records_result.PutTelemetryRecordsResult"
        ]:
            import capo_xray._operations.awsx_ray.put_telemetry_records

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.put_telemetry_records.async_put_telemetry_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.put_telemetry_records_request.PutTelemetryRecordsRequest = {
            "telemetry_records": telemetry_records
        }
        if ec2_instance_id is not None:
            input_["ec2_instance_id"] = ec2_instance_id
        if hostname is not None:
            input_["hostname"] = hostname
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_trace_segments(
        self,
        trace_segment_documents: "capo_xray.types.trace_segment_document_list.TraceSegmentDocumentList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.put_trace_segments_result.PutTraceSegmentsResult":
        """<p>Uploads segment documents to Amazon Web Services X-Ray. A segment document can be a completed segment, an in-progress segment, or an array of subsegments.</p> <p>Segments must include the following fields. For the full segment document schema, see <a href="https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-api.html#xray-api-segmentdocuments.html">Amazon Web Services X-Ray Segment Documents</a> in the <i>Amazon Web Services X-Ray Developer Guide</i>.</p> <p class="title"> <b>Required segment document fields</b> </p> <ul> <li> <p> <code>name</code> - The name of the service that handled the request.</p> </li> <li> <p> <code>id</code> - A 64-bit identifier for the segment, unique among segments in the same trace, in 16 hexadecimal digits.</p> </li> <li> <p> <code>trace_id</code> - A unique identifier that connects all segments and subsegments originating from a single client request.</p> </li> <li> <p> <code>start_time</code> - Time the segment or subsegment was created, in floating point seconds in epoch time, accurate to milliseconds. For example, <code>1480615200.010</code> or <code>1.480615200010E9</code>.</p> </li> <li> <p> <code>end_time</code> - Time the segment or subsegment was closed. For example, <code>1480615200.090</code> or <code>1.480615200090E9</code>. Specify either an <code>end_time</code> or <code>in_progress</code>.</p> </li> <li> <p> <code>in_progress</code> - Set to <code>true</code> instead of specifying an <code>end_time</code> to record that a segment has been started, but is not complete. Send an in-progress segment when your application receives a request that will take a long time to serve, to trace that the request was received. When the response is sent, send the complete segment to overwrite the in-progress segment.</p> </li> </ul> <p>A <code>trace_id</code> consists of three numbers separated by hyphens. For example, 1-58406520-a006649127e371903a2de979. For trace IDs created by an X-Ray SDK, or by Amazon Web Services services integrated with X-Ray, a trace ID includes:</p> <p class="title"> <b>Trace ID Format</b> </p> <ul> <li> <p>The version number, for instance, <code>1</code>.</p> </li> <li> <p>The time of the original request, in Unix epoch time, in 8 hexadecimal digits. For example, 10:00AM December 2nd, 2016 PST in epoch time is <code>1480615200</code> seconds, or <code>58406520</code> in hexadecimal.</p> </li> <li> <p>A 96-bit identifier for the trace, globally unique, in 24 hexadecimal digits.</p> </li> </ul> <note> <p>Trace IDs created via OpenTelemetry have a different format based on the <a href="https://www.w3.org/TR/trace-context/">W3C Trace Context specification</a>. A W3C trace ID must be formatted in the X-Ray trace ID format when sending to X-Ray. For example, a W3C trace ID <code>4efaaf4d1e8720b39541901950019ee5</code> should be formatted as <code>1-4efaaf4d-1e8720b39541901950019ee5</code> when sending to X-Ray. While X-Ray trace IDs include the original request timestamp in Unix epoch time, this is not required or validated. </p> </note>

        Args:
            trace_segment_documents: <p>A string containing a JSON document defining one or more segments or subsegments.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.put_trace_segments_request.PutTraceSegmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.put_trace_segments_result.PutTraceSegmentsResult"
        ]:
            import capo_xray._operations.awsx_ray.put_trace_segments

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.put_trace_segments.async_put_trace_segments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.put_trace_segments_request.PutTraceSegmentsRequest = {
            "trace_segment_documents": trace_segment_documents
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_trace_retrieval(
        self,
        trace_ids: "capo_xray.types.trace_id_list_for_retrieval.TraceIdListForRetrieval",
        start_time: "capo_xray.types.timestamp.Timestamp",
        end_time: "capo_xray.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.start_trace_retrieval_result.StartTraceRetrievalResult":
        """<p> Initiates a trace retrieval process using the specified time range and for the given trace IDs in the Transaction Search generated CloudWatch log group. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html">Transaction Search</a>. </p> <p>API returns a <code>RetrievalToken</code>, which can be used with <code>ListRetrievedTraces</code> or <code>GetRetrievedTracesGraph</code> to fetch results. Retrievals will time out after 60 minutes. To execute long time ranges, consider segmenting into multiple retrievals.</p> <p>If you are using <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>, you can use this operation in a monitoring account to retrieve data from a linked source account, as long as both accounts have transaction search enabled.</p> <p>For retrieving data from X-Ray directly as opposed to the Transaction-Search Log group, see <a href="https://docs.aws.amazon.com/xray/latest/api/API_BatchGetTraces.html">BatchGetTraces</a>.</p>

        Args:
            trace_ids: <p> Specify the trace IDs of the traces to be retrieved. </p>
            start_time: <p> The start of the time range to retrieve traces. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC. </p>
            end_time: <p> The end of the time range to retrieve traces. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since January 1, 1970, 00:00:00 UTC.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.start_trace_retrieval_request.StartTraceRetrievalRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.start_trace_retrieval_result.StartTraceRetrievalResult"
        ]:
            import capo_xray._operations.awsx_ray.start_trace_retrieval

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.start_trace_retrieval.async_start_trace_retrieval(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.start_trace_retrieval_request.StartTraceRetrievalRequest = {
            "trace_ids": trace_ids,
            "start_time": start_time,
            "end_time": end_time,
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
        resource_arn: "capo_xray.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_xray.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.tag_resource_response.TagResourceResponse":
        """<p>Applies tags to an existing Amazon Web Services X-Ray group or sampling rule.</p>

        Args:
            resource_arn: <p>The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.</p>
            tags: <p>A map that contains one or more tag keys and tag values to attach to an X-Ray group or sampling rule. For more information about ways to use tags, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference</i>.</p> <p>The following restrictions apply to tags:</p> <ul> <li> <p>Maximum number of user-applied tags per resource: 50</p> </li> <li> <p>Maximum tag key length: 128 Unicode characters</p> </li> <li> <p>Maximum tag value length: 256 Unicode characters</p> </li> <li> <p>Valid values for key and value: a-z, A-Z, 0-9, space, and the following characters: _ . : / = + - and @</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Don't use <code>aws:</code> as a prefix for keys; it's reserved for Amazon Web Services use. You cannot edit or delete system tags.</p> </li> </ul>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.too_many_tags_exception.TooManyTagsException: <p>You have exceeded the maximum number of tags you can apply to this resource.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_xray._operations.awsx_ray.tag_resource

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_xray.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_xray.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from an Amazon Web Services X-Ray group or sampling rule. You cannot edit or delete system tags (those with an <code>aws:</code> prefix).</p>

        Args:
            resource_arn: <p>The Amazon Resource Number (ARN) of an X-Ray group or sampling rule.</p>
            tag_keys: <p>Keys for one or more tags that you want to remove from an X-Ray group or sampling rule.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_xray._operations.awsx_ray.untag_resource

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_group(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        group_name: Optional["capo_xray.types.group_name.GroupName"] = None,
        group_arn: Optional["capo_xray.types.group_arn.GroupARN"] = None,
        filter_expression: Optional[
            "capo_xray.types.filter_expression.FilterExpression"
        ] = None,
        insights_configuration: Optional[
            "capo_xray.types.insights_configuration.InsightsConfiguration"
        ] = None,
    ) -> "capo_xray.types.update_group_result.UpdateGroupResult":
        """<p>Updates a group resource.</p>

        Args:
            group_name: <p>The case-sensitive name of the group.</p>
            group_arn: <p>The ARN that was generated upon creation.</p>
            filter_expression: <p>The updated filter expression defining criteria by which to group traces.</p>
            insights_configuration: <p>The structure containing configurations related to insights.</p> <ul> <li> <p>The InsightsEnabled boolean can be set to true to enable insights for the group or false to disable insights for the group.</p> </li> <li> <p>The NotificationsEnabled boolean can be set to true to enable insights notifications for the group. Notifications can only be enabled on a group with InsightsEnabled set to true.</p> </li> </ul>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.update_group_request.UpdateGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.update_group_result.UpdateGroupResult"
        ]:
            import capo_xray._operations.awsx_ray.update_group

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.update_group.async_update_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.update_group_request.UpdateGroupRequest = {}
        if group_name is not None:
            input_["group_name"] = group_name
        if group_arn is not None:
            input_["group_arn"] = group_arn
        if filter_expression is not None:
            input_["filter_expression"] = filter_expression
        if insights_configuration is not None:
            input_["insights_configuration"] = insights_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_indexing_rule(
        self,
        name: "capo_xray.types.string.String",
        rule: "capo_xray.types.indexing_rule_value_update.IndexingRuleValueUpdate",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.update_indexing_rule_result.UpdateIndexingRuleResult":
        """<p> Modifies an indexing rule’s configuration. </p> <p>Indexing rules are used for determining the sampling rate for spans indexed from CloudWatch Logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html">Transaction Search</a>.</p>

        Args:
            name: <p> Name of the indexing rule to be updated. </p>
            rule: <p> Rule configuration to be updated. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.resource_not_found_exception.ResourceNotFoundException: <p>The resource was not found. Verify that the name or Amazon Resource Name (ARN) of the resource is correct.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.update_indexing_rule_request.UpdateIndexingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.update_indexing_rule_result.UpdateIndexingRuleResult"
        ]:
            import capo_xray._operations.awsx_ray.update_indexing_rule

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.update_indexing_rule.async_update_indexing_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.update_indexing_rule_request.UpdateIndexingRuleRequest = {
            "name": name,
            "rule": rule,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_sampling_rule(
        self,
        sampling_rule_update: "capo_xray.types.sampling_rule_update.SamplingRuleUpdate",
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
    ) -> "capo_xray.types.update_sampling_rule_result.UpdateSamplingRuleResult":
        """<p>Modifies a sampling rule's configuration.</p>

        Args:
            sampling_rule_update: <p>The rule and fields to change.</p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.update_sampling_rule_request.UpdateSamplingRuleRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.update_sampling_rule_result.UpdateSamplingRuleResult"
        ]:
            import capo_xray._operations.awsx_ray.update_sampling_rule

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.update_sampling_rule.async_update_sampling_rule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.update_sampling_rule_request.UpdateSamplingRuleRequest = {
            "sampling_rule_update": sampling_rule_update
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_trace_segment_destination(
        self,
        *,
        config_overrides: Optional[AsyncXRayClientConfig] = None,
        destination: Optional[
            "capo_xray.types.trace_segment_destination.TraceSegmentDestination"
        ] = None,
    ) -> "capo_xray.types.update_trace_segment_destination_result.UpdateTraceSegmentDestinationResult":
        """<p> Modifies the destination of data sent to <code>PutTraceSegments</code>. The Transaction Search feature requires the CloudWatchLogs destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Transaction-Search.html">Transaction Search</a>. </p>

        Args:
            destination: <p> The configured destination of trace segments. </p>

        Raises:
            capo_xray.errors.invalid_request_exception.InvalidRequestException: <p>The request is missing required parameters or has invalid parameters.</p>
            capo_xray.errors.throttled_exception.ThrottledException: <p>The request exceeds the maximum number of requests per second.</p>
            capo_xray.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_xray.types.update_trace_segment_destination_request.UpdateTraceSegmentDestinationRequest]",
        ) -> AsyncOperationResponse[
            "capo_xray.types.update_trace_segment_destination_result.UpdateTraceSegmentDestinationResult"
        ]:
            import capo_xray._operations.awsx_ray.update_trace_segment_destination

            (
                output,
                http_response,
            ) = await capo_xray._operations.awsx_ray.update_trace_segment_destination.async_update_trace_segment_destination(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_xray.types.update_trace_segment_destination_request.UpdateTraceSegmentDestinationRequest = {}
        if destination is not None:
            input_["destination"] = destination

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
