"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#ArcRegionSwitch``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_arc_region_switch._auth._signers
import capo_arc_region_switch._auth._sigv4
from capo_arc_region_switch._auth._identity import Credentials
from capo_arc_region_switch._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_arc_region_switch._auth._zapros_handler import AuthMiddleware
from capo_arc_region_switch._pagination import resolve_path as _resolve_path
from capo_arc_region_switch._resources.arc_region_switch.region_switch_plan import (
    AsyncRegionSwitchPlan,
)
from capo_arc_region_switch._services._aws_config import aaws_config
from capo_arc_region_switch._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_arc_region_switch.types.abbreviated_execution
    import capo_arc_region_switch.types.abbreviated_plan
    import capo_arc_region_switch.types.approval
    import capo_arc_region_switch.types.approve_plan_execution_step_request
    import capo_arc_region_switch.types.approve_plan_execution_step_response
    import capo_arc_region_switch.types.associated_alarm_map
    import capo_arc_region_switch.types.cancel_plan_execution_request
    import capo_arc_region_switch.types.cancel_plan_execution_response
    import capo_arc_region_switch.types.create_plan_request
    import capo_arc_region_switch.types.create_plan_response
    import capo_arc_region_switch.types.delete_plan_request
    import capo_arc_region_switch.types.delete_plan_response
    import capo_arc_region_switch.types.execution_action
    import capo_arc_region_switch.types.execution_comment
    import capo_arc_region_switch.types.execution_event
    import capo_arc_region_switch.types.execution_id
    import capo_arc_region_switch.types.execution_mode
    import capo_arc_region_switch.types.execution_state
    import capo_arc_region_switch.types.get_plan_evaluation_status_request
    import capo_arc_region_switch.types.get_plan_evaluation_status_response
    import capo_arc_region_switch.types.get_plan_execution_request
    import capo_arc_region_switch.types.get_plan_execution_response
    import capo_arc_region_switch.types.get_plan_execution_step_states_max_results
    import capo_arc_region_switch.types.get_plan_in_region_request
    import capo_arc_region_switch.types.get_plan_in_region_response
    import capo_arc_region_switch.types.get_plan_request
    import capo_arc_region_switch.types.get_plan_response
    import capo_arc_region_switch.types.iam_role_arn
    import capo_arc_region_switch.types.list_execution_events_max_results
    import capo_arc_region_switch.types.list_executions_max_results
    import capo_arc_region_switch.types.list_plan_execution_events_request
    import capo_arc_region_switch.types.list_plan_execution_events_response
    import capo_arc_region_switch.types.list_plan_executions_request
    import capo_arc_region_switch.types.list_plan_executions_response
    import capo_arc_region_switch.types.list_plans_in_region_request
    import capo_arc_region_switch.types.list_plans_in_region_response
    import capo_arc_region_switch.types.list_plans_request
    import capo_arc_region_switch.types.list_plans_response
    import capo_arc_region_switch.types.list_route53_health_checks_in_region_request
    import capo_arc_region_switch.types.list_route53_health_checks_in_region_response
    import capo_arc_region_switch.types.list_route53_health_checks_request
    import capo_arc_region_switch.types.list_route53_health_checks_response
    import capo_arc_region_switch.types.list_service_quota_warnings_request
    import capo_arc_region_switch.types.list_service_quota_warnings_response
    import capo_arc_region_switch.types.list_tags_for_resource_request
    import capo_arc_region_switch.types.list_tags_for_resource_response
    import capo_arc_region_switch.types.max_results
    import capo_arc_region_switch.types.next_token
    import capo_arc_region_switch.types.plan_arn
    import capo_arc_region_switch.types.plan_arn_list
    import capo_arc_region_switch.types.plan_name
    import capo_arc_region_switch.types.recovery_approach
    import capo_arc_region_switch.types.recovery_execution_id
    import capo_arc_region_switch.types.region
    import capo_arc_region_switch.types.region_list
    import capo_arc_region_switch.types.report_configuration
    import capo_arc_region_switch.types.resource_warning
    import capo_arc_region_switch.types.route53_health_check
    import capo_arc_region_switch.types.route53_hosted_zone_id
    import capo_arc_region_switch.types.route53_record_name
    import capo_arc_region_switch.types.service_quota_warning_summary
    import capo_arc_region_switch.types.start_plan_execution_request
    import capo_arc_region_switch.types.start_plan_execution_response
    import capo_arc_region_switch.types.step_name
    import capo_arc_region_switch.types.step_state
    import capo_arc_region_switch.types.tag_keys
    import capo_arc_region_switch.types.tag_resource_request
    import capo_arc_region_switch.types.tag_resource_response
    import capo_arc_region_switch.types.tags
    import capo_arc_region_switch.types.trigger_list
    import capo_arc_region_switch.types.untag_resource_request
    import capo_arc_region_switch.types.untag_resource_response
    import capo_arc_region_switch.types.update_plan_execution_action
    import capo_arc_region_switch.types.update_plan_execution_request
    import capo_arc_region_switch.types.update_plan_execution_response
    import capo_arc_region_switch.types.update_plan_execution_step_action
    import capo_arc_region_switch.types.update_plan_execution_step_request
    import capo_arc_region_switch.types.update_plan_execution_step_response
    import capo_arc_region_switch.types.update_plan_request
    import capo_arc_region_switch.types.update_plan_response
    import capo_arc_region_switch.types.workflow_list


class AsyncARCRegionswitchClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncARCRegionswitchClient:
    """A client for the ``ARCRegionswitch`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncARCRegionswitchClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.region_switch_plan = AsyncRegionSwitchPlan(self)

    def operation_options(
        self, config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncARCRegionswitchClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    async def approve_plan_execution_step(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        step_name: "capo_arc_region_switch.types.step_name.StepName",
        approval: "capo_arc_region_switch.types.approval.Approval",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
    ) -> "capo_arc_region_switch.types.approve_plan_execution_step_response.ApprovePlanExecutionStepResponse":
        """<p>Approves a step in a plan execution that requires manual approval. When you create a plan, you can include approval steps that require manual intervention before the execution can proceed. This operation allows you to provide that approval.</p> <p>You must specify the plan ARN, execution ID, step name, and approval status. You can also provide an optional comment explaining the approval decision.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            step_name: <p>The name of a step in a plan execution.</p>
            approval: <p>The status of approval for a plan execution step. </p>
            comment: <p>A comment that you can enter about a plan execution.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.approve_plan_execution_step_request.ApprovePlanExecutionStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.approve_plan_execution_step_response.ApprovePlanExecutionStepResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.approve_plan_execution_step

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.approve_plan_execution_step.async_approve_plan_execution_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.approve_plan_execution_step_request.ApprovePlanExecutionStepRequest = {
            "plan_arn": plan_arn,
            "execution_id": execution_id,
            "step_name": step_name,
            "approval": approval,
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

    async def cancel_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
    ) -> "capo_arc_region_switch.types.cancel_plan_execution_response.CancelPlanExecutionResponse":
        """<p>Cancels an in-progress plan execution. This operation stops the execution of the plan and prevents any further steps from being processed.</p> <p>You must specify the plan ARN and execution ID. You can also provide an optional comment explaining why the execution was canceled.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            comment: <p>A comment that you can enter about canceling a plan execution step.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.cancel_plan_execution_request.CancelPlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.cancel_plan_execution_response.CancelPlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.cancel_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.cancel_plan_execution.async_cancel_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.cancel_plan_execution_request.CancelPlanExecutionRequest = {
            "plan_arn": plan_arn,
            "execution_id": execution_id,
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

    async def get_plan_evaluation_status(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.get_plan_evaluation_status_response.GetPlanEvaluationStatusResponse":
        """<p>Retrieves the evaluation status of a Region switch plan. The evaluation status provides information about the last time the plan was evaluated and any warnings or issues detected.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the Region switch plan to retrieve evaluation status for.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_evaluation_status_request.GetPlanEvaluationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_evaluation_status_response.GetPlanEvaluationStatusResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan_evaluation_status

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan_evaluation_status.async_get_plan_evaluation_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.get_plan_evaluation_status_request.GetPlanEvaluationStatusRequest = {
            "plan_arn": plan_arn
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

    async def iter_get_plan_evaluation_status(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.resource_warning.ResourceWarning]":
        _token = next_token
        while True:
            _response = await self.get_plan_evaluation_status(
                plan_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("warnings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.get_plan_execution_step_states_max_results.GetPlanExecutionStepStatesMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "capo_arc_region_switch.types.get_plan_execution_response.GetPlanExecutionResponse":
        """<p>Retrieves detailed information about a specific plan execution. You must specify the plan ARN and execution ID.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan with the execution to retrieve.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_execution_request.GetPlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_execution_response.GetPlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan_execution.async_get_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.get_plan_execution_request.GetPlanExecutionRequest = {
            "plan_arn": plan_arn,
            "execution_id": execution_id,
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

    async def iter_get_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.get_plan_execution_step_states_max_results.GetPlanExecutionStepStatesMaxResults"
        ] = None,
        next_token: Optional[str] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.step_state.StepState]":
        _token = next_token
        while True:
            _response = await self.get_plan_execution(
                plan_arn,
                execution_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("step_states",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_plan_in_region(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.get_plan_in_region_response.GetPlanInRegionResponse":
        """<p>Retrieves information about a Region switch plan in a specific Amazon Web Services Region. This operation is useful for getting Region-specific information about a plan.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan in Region.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_in_region_request.GetPlanInRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_in_region_response.GetPlanInRegionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan_in_region

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan_in_region.async_get_plan_in_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.get_plan_in_region_request.GetPlanInRegionRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_plan_execution_events(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_execution_events_max_results.ListExecutionEventsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        name: Optional["capo_arc_region_switch.types.step_name.StepName"] = None,
    ) -> "capo_arc_region_switch.types.list_plan_execution_events_response.ListPlanExecutionEventsResponse":
        """<p>Lists the events that occurred during a plan execution. These events provide a detailed timeline of the execution process.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            name: <p>The name of the plan execution event.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plan_execution_events_request.ListPlanExecutionEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plan_execution_events_response.ListPlanExecutionEventsResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plan_execution_events

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plan_execution_events.async_list_plan_execution_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_plan_execution_events_request.ListPlanExecutionEventsRequest = {
            "plan_arn": plan_arn,
            "execution_id": execution_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_plan_execution_events(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_execution_events_max_results.ListExecutionEventsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        name: Optional["capo_arc_region_switch.types.step_name.StepName"] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.execution_event.ExecutionEvent]":
        _token = next_token
        while True:
            _response = await self.list_plan_execution_events(
                plan_arn,
                execution_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_plan_executions(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_executions_max_results.ListExecutionsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        state: Optional[
            "capo_arc_region_switch.types.execution_state.ExecutionState"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_plan_executions_response.ListPlanExecutionsResponse":
        """<p>Lists the executions of a Region switch plan. This operation returns information about both current and historical executions.</p>

        Args:
            plan_arn: <p>The ARN for the plan.</p>
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>
            state: <p>The state of the plan execution. For example, the plan execution might be In Progress.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plan_executions_request.ListPlanExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plan_executions_response.ListPlanExecutionsResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plan_executions

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plan_executions.async_list_plan_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_plan_executions_request.ListPlanExecutionsRequest = {
            "plan_arn": plan_arn
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state is not None:
            input_["state"] = state

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_plan_executions(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.list_executions_max_results.ListExecutionsMaxResults"
        ] = None,
        next_token: Optional[str] = None,
        state: Optional[
            "capo_arc_region_switch.types.execution_state.ExecutionState"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.abbreviated_execution.AbbreviatedExecution]":
        _token = next_token
        while True:
            _response = await self.list_plan_executions(
                plan_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state=state,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_plans_in_region(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_plans_in_region_response.ListPlansInRegionResponse":
        """<p>Lists all Region switch plans in your Amazon Web Services account that are available in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plans_in_region_request.ListPlansInRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plans_in_region_response.ListPlansInRegionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plans_in_region

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plans_in_region.async_list_plans_in_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_plans_in_region_request.ListPlansInRegionRequest = {}
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

    async def iter_list_plans_in_region(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.abbreviated_plan.AbbreviatedPlan]":
        _token = next_token
        while True:
            _response = await self.list_plans_in_region(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("plans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_route53_health_checks(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_route53_health_checks_response.ListRoute53HealthChecksResponse":
        """<p>List the Amazon Route 53 health checks.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Amazon Route 53 health check request.</p>
            hosted_zone_id: <p>The hosted zone ID for the health checks.</p>
            record_name: <p>The record name for the health checks.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.illegal_argument_exception.IllegalArgumentException: <p>The request processing has an invalid argument.</p>
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_route53_health_checks_request.ListRoute53HealthChecksRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_route53_health_checks_response.ListRoute53HealthChecksResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks.async_list_route53_health_checks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_route53_health_checks_request.ListRoute53HealthChecksRequest = {
            "arn": arn
        }
        if hosted_zone_id is not None:
            input_["hosted_zone_id"] = hosted_zone_id
        if record_name is not None:
            input_["record_name"] = record_name
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

    async def iter_list_route53_health_checks(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.route53_health_check.Route53HealthCheck]":
        _token = next_token
        while True:
            _response = await self.list_route53_health_checks(
                arn,
                config_overrides=config_overrides,
                hosted_zone_id=hosted_zone_id,
                record_name=record_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("health_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_route53_health_checks_in_region(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_route53_health_checks_in_region_response.ListRoute53HealthChecksInRegionResponse":
        """<p>List the Amazon Route 53 health checks in a specific Amazon Web Services Region.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the Arc Region Switch Plan.</p>
            hosted_zone_id: <p>The hosted zone ID for the health checks.</p>
            record_name: <p>The record name for the health checks.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.illegal_argument_exception.IllegalArgumentException: <p>The request processing has an invalid argument.</p>
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Example ListRoute53HealthChecksInRegion

            >>> await client.list_route53_health_checks_in_region(arn='arn:aws:arc-region-switch::123456789012:plan/example:000000', hosted_zone_id='Z0123456789ABCDEFGHI', record_name='my.record.name', max_results=10, next_token='eyJNYXJrZXIiOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAxfQ')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_route53_health_checks_in_region_request.ListRoute53HealthChecksInRegionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_route53_health_checks_in_region_response.ListRoute53HealthChecksInRegionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks_in_region

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_route53_health_checks_in_region.async_list_route53_health_checks_in_region(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_route53_health_checks_in_region_request.ListRoute53HealthChecksInRegionRequest = {
            "arn": arn
        }
        if hosted_zone_id is not None:
            input_["hosted_zone_id"] = hosted_zone_id
        if record_name is not None:
            input_["record_name"] = record_name
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

    async def iter_list_route53_health_checks_in_region(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        hosted_zone_id: Optional[
            "capo_arc_region_switch.types.route53_hosted_zone_id.Route53HostedZoneId"
        ] = None,
        record_name: Optional[
            "capo_arc_region_switch.types.route53_record_name.Route53RecordName"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.route53_health_check.Route53HealthCheck]":
        _token = next_token
        while True:
            _response = await self.list_route53_health_checks_in_region(
                arn,
                config_overrides=config_overrides,
                hosted_zone_id=hosted_zone_id,
                record_name=record_name,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("health_checks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_service_quota_warnings(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        plan_arns: Optional[
            "capo_arc_region_switch.types.plan_arn_list.PlanArnList"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_service_quota_warnings_response.ListServiceQuotaWarningsResponse":
        """<p>Lists the service quota warnings for the plans that you can access. Region switch creates a warning when the applied quota value in one Region of a plan is lower than the value required for the matching resource in another Region or account in the plan.</p> <p>Returns the warnings for the plans that you own and for plans that are shared with your account through AWS Resource Access Manager (AWS RAM). To return warnings for specific plans, provide a list of plan Amazon Resource Names (ARNs). Region switch ignores any plan ARN that you can't access. If you don't provide any plan ARNs, Region switch returns the warnings for all of your accessible plans.</p>

        Args:
            plan_arns: <p>The Amazon Resource Names (ARNs) of the plans to return service quota warnings for. You can specify up to 100 plan ARNs. Region switch ignores any plan ARN that you can't access. If you omit this parameter, Region switch returns the warnings for all of your accessible plans.</p>
            max_results: <p>The maximum number of results to return with this call. Valid values are <code>1</code> to <code>100</code>. If you don't specify a value, the operation returns up to the maximum number of results.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_service_quota_warnings_request.ListServiceQuotaWarningsRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_service_quota_warnings_response.ListServiceQuotaWarningsResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_service_quota_warnings

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_service_quota_warnings.async_list_service_quota_warnings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_service_quota_warnings_request.ListServiceQuotaWarningsRequest = {}
        if plan_arns is not None:
            input_["plan_arns"] = plan_arns
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

    async def iter_list_service_quota_warnings(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        plan_arns: Optional[
            "capo_arc_region_switch.types.plan_arn_list.PlanArnList"
        ] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.service_quota_warning_summary.ServiceQuotaWarningSummary]":
        _token = next_token
        while True:
            _response = await self.list_service_quota_warnings(
                config_overrides=config_overrides,
                plan_arns=plan_arns,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_quota_warning_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        target_region: str,
        action: "capo_arc_region_switch.types.execution_action.ExecutionAction",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        mode: Optional[
            "capo_arc_region_switch.types.execution_mode.ExecutionMode"
        ] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
        latest_version: Optional[str] = None,
        recovery_execution_id: Optional[
            "capo_arc_region_switch.types.recovery_execution_id.RecoveryExecutionId"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_arc_region_switch.types.start_plan_execution_response.StartPlanExecutionResponse":
        """<p>Starts the execution of a Region switch plan. You can execute a plan in either <code>graceful</code> or <code>ungraceful</code> mode.</p> <p>Specifing <code>ungraceful</code> mode either changes the behavior of the execution blocks in a workflow or skips specific execution blocks.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan to execute.</p>
            target_region: <p>The Amazon Web Services Region to target with this execution. This is the Region that traffic will be shifted to or from, depending on the action.</p>
            action: <p>The action to perform. Valid values are <code>activate</code> (to shift traffic to the target Region) or <code>deactivate</code> (to shift traffic away from the target Region).</p>
            mode: <p>The plan execution mode. Valid values are <code>graceful</code>, for starting the execution in graceful mode, or <code>ungraceful</code>, for starting the execution in ungraceful mode.</p>
            comment: <p>An optional comment explaining why the plan execution is being started.</p>
            latest_version: <p>A boolean value indicating whether to use the latest version of the plan. If set to false, you must specify a specific version.</p>
            recovery_execution_id: <p>The execution identifier of the recovery execution that ran in the opposite region post-recovery is ran in. Required when starting a post-recovery execution.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request and returns the result of the original successful request. If you don't provide a client token, the service automatically generates one. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.conflict_exception.ConflictException: <p>The client token was already used with different request parameters. A client token must map to the same parameters for every request. To retry this operation, provide a new client token.</p>
            capo_arc_region_switch.errors.illegal_argument_exception.IllegalArgumentException: <p>The request processing has an invalid argument.</p>
            capo_arc_region_switch.errors.illegal_state_exception.IllegalStateException: <p>The operation failed because the current state of the resource doesn't allow the operation to proceed.</p> <p>HTTP Status Code: 400</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.start_plan_execution_request.StartPlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.start_plan_execution_response.StartPlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.start_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.start_plan_execution.async_start_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.start_plan_execution_request.StartPlanExecutionRequest = {
            "plan_arn": plan_arn,
            "target_region": target_region,
            "action": action,
        }
        if mode is not None:
            input_["mode"] = mode
        if comment is not None:
            input_["comment"] = comment
        if latest_version is not None:
            input_["latest_version"] = latest_version
        if recovery_execution_id is not None:
            input_["recovery_execution_id"] = recovery_execution_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_plan_execution(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        action: "capo_arc_region_switch.types.update_plan_execution_action.UpdatePlanExecutionAction",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        comment: Optional[
            "capo_arc_region_switch.types.execution_comment.ExecutionComment"
        ] = None,
    ) -> "capo_arc_region_switch.types.update_plan_execution_response.UpdatePlanExecutionResponse":
        """<p>Updates an in-progress plan execution. This operation allows you to modify certain aspects of the execution, such as adding a comment or changing the action.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan with the execution to update.</p>
            execution_id: <p>The execution identifier of a plan execution.</p>
            action: <p>The action specified for a plan execution, for example, Switch to Graceful or Pause.</p>
            comment: <p>An optional comment about the plan execution.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.illegal_state_exception.IllegalStateException: <p>The operation failed because the current state of the resource doesn't allow the operation to proceed.</p> <p>HTTP Status Code: 400</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.update_plan_execution_request.UpdatePlanExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.update_plan_execution_response.UpdatePlanExecutionResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.update_plan_execution

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.update_plan_execution.async_update_plan_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.update_plan_execution_request.UpdatePlanExecutionRequest = {
            "plan_arn": plan_arn,
            "execution_id": execution_id,
            "action": action,
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

    async def update_plan_execution_step(
        self,
        plan_arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        execution_id: "capo_arc_region_switch.types.execution_id.ExecutionId",
        comment: "capo_arc_region_switch.types.execution_comment.ExecutionComment",
        step_name: str,
        action_to_take: "capo_arc_region_switch.types.update_plan_execution_step_action.UpdatePlanExecutionStepAction",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.update_plan_execution_step_response.UpdatePlanExecutionStepResponse":
        """<p>Updates a specific step in an in-progress plan execution. This operation allows you to modify the step's comment or action.</p>

        Args:
            plan_arn: <p>The Amazon Resource Name (ARN) of the plan containing the execution step to update.</p>
            execution_id: <p>The unique identifier of the plan execution containing the step to update.</p>
            comment: <p>An optional comment about the plan execution.</p>
            step_name: <p>The name of the execution step to update.</p>
            action_to_take: <p>The updated action to take for the step. This can be used to skip or retry a step.</p>

        Raises:
            capo_arc_region_switch.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p> <p>HTTP Status Code: 403</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.update_plan_execution_step_request.UpdatePlanExecutionStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.update_plan_execution_step_response.UpdatePlanExecutionStepResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.update_plan_execution_step

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.update_plan_execution_step.async_update_plan_execution_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.update_plan_execution_step_request.UpdatePlanExecutionStepRequest = {
            "plan_arn": plan_arn,
            "execution_id": execution_id,
            "comment": comment,
            "step_name": step_name,
            "action_to_take": action_to_take,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_plan(
        self,
        workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList",
        execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn",
        name: "capo_arc_region_switch.types.plan_name.PlanName",
        regions: "capo_arc_region_switch.types.region_list.RegionList",
        recovery_approach: "capo_arc_region_switch.types.recovery_approach.RecoveryApproach",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        description: Optional[str] = None,
        recovery_time_objective_minutes: Optional[int] = None,
        associated_alarms: Optional[
            "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
        ] = None,
        triggers: Optional[
            "capo_arc_region_switch.types.trigger_list.TriggerList"
        ] = None,
        report_configuration: Optional[
            "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
        ] = None,
        service_quota_checks_enabled: Optional[bool] = None,
        primary_region: Optional["capo_arc_region_switch.types.region.Region"] = None,
        tags: Optional["capo_arc_region_switch.types.tags.Tags"] = None,
    ) -> "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse":
        """<p>Creates a new Region switch plan. A plan defines the steps required to shift traffic from one Amazon Web Services Region to another.</p> <p>You must specify a name for the plan, the primary Region, and at least one additional Region. You can also provide a description, execution role, recovery time objective, associated alarms, triggers, and workflows that define the steps to execute during a Region switch.</p>

        Args:
            description: <p>The description of a Region switch plan.</p>
            workflows: <p>An array of workflows included in a Region switch plan.</p>
            execution_role: <p>An execution role is a way to categorize a Region switch plan.</p>
            recovery_time_objective_minutes: <p>Optionally, you can specify an recovery time objective for a Region switch plan, in minutes.</p>
            associated_alarms: <p>The alarms associated with a Region switch plan.</p>
            triggers: <p>The triggers associated with a Region switch plan.</p>
            service_quota_checks_enabled: <p>Specifies whether to enable service quota checks for the Region switch plan.</p>
            name: <p>The name of a Region switch plan.</p>
            regions: <p>An array that specifies the Amazon Web Services Regions for a Region switch plan. Specify two Regions.</p>
            recovery_approach: <p>The recovery approach for a Region switch plan, which can be active/active (activeActive) or active/passive (activePassive).</p>
            primary_region: <p>The primary Amazon Web Services Region for the application. This is the Region where the application normally runs before any Region switch occurs.</p>
            tags: <p>The tags to apply to the Region switch plan.</p>

        Raises:
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.create_plan_request.CreatePlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.create_plan_response.CreatePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.create_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.create_plan.async_create_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.create_plan_request.CreatePlanRequest = {
            "workflows": workflows,
            "execution_role": execution_role,
            "name": name,
            "regions": regions,
            "recovery_approach": recovery_approach,
        }
        if description is not None:
            input_["description"] = description
        if recovery_time_objective_minutes is not None:
            input_["recovery_time_objective_minutes"] = recovery_time_objective_minutes
        if associated_alarms is not None:
            input_["associated_alarms"] = associated_alarms
        if triggers is not None:
            input_["triggers"] = triggers
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration
        if service_quota_checks_enabled is not None:
            input_["service_quota_checks_enabled"] = service_quota_checks_enabled
        if primary_region is not None:
            input_["primary_region"] = primary_region
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_plan(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.get_plan_response.GetPlanResponse":
        """<p>Retrieves detailed information about a Region switch plan. You must specify the ARN of the plan.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>

        Raises:
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.get_plan_request.GetPlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.get_plan_response.GetPlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.get_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.get_plan.async_get_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.get_plan_request.GetPlanRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_plan(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        workflows: "capo_arc_region_switch.types.workflow_list.WorkflowList",
        execution_role: "capo_arc_region_switch.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        description: Optional[str] = None,
        recovery_time_objective_minutes: Optional[int] = None,
        associated_alarms: Optional[
            "capo_arc_region_switch.types.associated_alarm_map.AssociatedAlarmMap"
        ] = None,
        triggers: Optional[
            "capo_arc_region_switch.types.trigger_list.TriggerList"
        ] = None,
        report_configuration: Optional[
            "capo_arc_region_switch.types.report_configuration.ReportConfiguration"
        ] = None,
        service_quota_checks_enabled: Optional[bool] = None,
    ) -> "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse":
        """<p>Updates an existing Region switch plan. You can modify the plan's description, workflows, execution role, recovery time objective, associated alarms, and triggers.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>
            description: <p>The updated description for the Region switch plan.</p>
            workflows: <p>The updated workflows for the Region switch plan.</p>
            execution_role: <p>The updated IAM role ARN that grants Region switch the permissions needed to execute the plan steps.</p>
            recovery_time_objective_minutes: <p>The updated target recovery time objective (RTO) in minutes for the plan.</p>
            associated_alarms: <p>The updated CloudWatch alarms associated with the plan.</p>
            triggers: <p>The updated conditions that can automatically trigger the execution of the plan.</p>
            report_configuration: <p>The updated report configuration for the plan.</p>
            service_quota_checks_enabled: <p>Specifies whether service quota checks are enabled for the Region switch plan.</p>

        Raises:
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.update_plan_response.UpdatePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.update_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.update_plan.async_update_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.update_plan_request.UpdatePlanRequest = {
            "arn": arn,
            "workflows": workflows,
            "execution_role": execution_role,
        }
        if description is not None:
            input_["description"] = description
        if recovery_time_objective_minutes is not None:
            input_["recovery_time_objective_minutes"] = recovery_time_objective_minutes
        if associated_alarms is not None:
            input_["associated_alarms"] = associated_alarms
        if triggers is not None:
            input_["triggers"] = triggers
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration
        if service_quota_checks_enabled is not None:
            input_["service_quota_checks_enabled"] = service_quota_checks_enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_plan(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.delete_plan_response.DeletePlanResponse":
        """<p>Deletes a Region switch plan. You must specify the ARN of the plan to delete.</p> <p>You cannot delete a plan that has an active execution in progress.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the plan.</p>

        Raises:
            capo_arc_region_switch.errors.illegal_state_exception.IllegalStateException: <p>The operation failed because the current state of the resource doesn't allow the operation to proceed.</p> <p>HTTP Status Code: 400</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.delete_plan_request.DeletePlanRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.delete_plan_response.DeletePlanResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.delete_plan

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.delete_plan.async_delete_plan(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.delete_plan_request.DeletePlanRequest = {
            "arn": arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_plans(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "capo_arc_region_switch.types.list_plans_response.ListPlansResponse":
        """<p>Lists all Region switch plans in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The number of objects that you want to return with this call.</p>
            next_token: <p>Specifies that you want to receive the next page of results. Valid only if you received a <code>nextToken</code> response in the previous request. If you did, it indicates that more output is available. Set this parameter to the value provided by the previous call's <code>nextToken</code> response to request the next page of results.</p>

        Raises:
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_plans_request.ListPlansRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_plans_response.ListPlansResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_plans

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_plans.async_list_plans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_plans_request.ListPlansRequest = {}
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

    async def iter_list_plans(
        self,
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
        max_results: Optional[
            "capo_arc_region_switch.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_arc_region_switch.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_arc_region_switch.types.abbreviated_plan.AbbreviatedPlan]":
        _token = next_token
        while True:
            _response = await self.list_plans(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("plans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags attached to a Region switch resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "arn": arn
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
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        tags: "capo_arc_region_switch.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or updates tags for a Region switch resource. You can assign metadata to your resources in the form of tags, which are key-value pairs.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for a tag that you add to a resource.</p>
            tags: <p>Tags that you add to a resource. You can add a maximum of 50 tags in Region switch.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.tag_resource

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.tag_resource_request.TagResourceRequest = {
            "arn": arn,
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
        arn: "capo_arc_region_switch.types.plan_arn.PlanArn",
        resource_tag_keys: "capo_arc_region_switch.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[AsyncARCRegionswitchClientConfig] = None,
    ) -> "capo_arc_region_switch.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a Region switch resource.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) for a tag you remove a resource from.</p>
            resource_tag_keys: <p>Tag keys that you remove from a resource.</p>

        Raises:
            capo_arc_region_switch.errors.internal_server_exception.InternalServerException: <p>The request processing has failed because of an unknown error, exception, or failure.</p> <p>HTTP Status Code: 500</p>
            capo_arc_region_switch.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource was not found.</p> <p>HTTP Status Code: 404</p>
            capo_arc_region_switch.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_arc_region_switch.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_arc_region_switch.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_arc_region_switch._operations.arc_region_switch.untag_resource

            (
                output,
                http_response,
            ) = await capo_arc_region_switch._operations.arc_region_switch.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_arc_region_switch.types.untag_resource_request.UntagResourceRequest = {
            "arn": arn,
            "resource_tag_keys": resource_tag_keys,
        }

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
