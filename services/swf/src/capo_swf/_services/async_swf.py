"""Generated from Smithy shape ``com.amazonaws.swf#SimpleWorkflowService``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_swf._auth._signers
import capo_swf._auth._sigv4
from capo_swf._auth._identity import Credentials
from capo_swf._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_swf._auth._zapros_handler import AuthMiddleware
from capo_swf._pagination import resolve_path as _resolve_path
from capo_swf._services._aws_config import aaws_config
from capo_swf._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_swf.types.activity_task
    import capo_swf.types.activity_task_status
    import capo_swf.types.activity_type
    import capo_swf.types.activity_type_detail
    import capo_swf.types.activity_type_info
    import capo_swf.types.activity_type_infos
    import capo_swf.types.arn
    import capo_swf.types.child_policy
    import capo_swf.types.close_status_filter
    import capo_swf.types.count_closed_workflow_executions_input
    import capo_swf.types.count_open_workflow_executions_input
    import capo_swf.types.count_pending_activity_tasks_input
    import capo_swf.types.count_pending_decision_tasks_input
    import capo_swf.types.data
    import capo_swf.types.decision_list
    import capo_swf.types.decision_task
    import capo_swf.types.delete_activity_type_input
    import capo_swf.types.delete_workflow_type_input
    import capo_swf.types.deprecate_activity_type_input
    import capo_swf.types.deprecate_domain_input
    import capo_swf.types.deprecate_workflow_type_input
    import capo_swf.types.describe_activity_type_input
    import capo_swf.types.describe_domain_input
    import capo_swf.types.describe_workflow_execution_input
    import capo_swf.types.describe_workflow_type_input
    import capo_swf.types.description
    import capo_swf.types.domain_detail
    import capo_swf.types.domain_info
    import capo_swf.types.domain_infos
    import capo_swf.types.domain_name
    import capo_swf.types.duration_in_days
    import capo_swf.types.duration_in_seconds_optional
    import capo_swf.types.execution_time_filter
    import capo_swf.types.failure_reason
    import capo_swf.types.get_workflow_execution_history_input
    import capo_swf.types.history
    import capo_swf.types.history_event
    import capo_swf.types.identity
    import capo_swf.types.limited_data
    import capo_swf.types.list_activity_types_input
    import capo_swf.types.list_closed_workflow_executions_input
    import capo_swf.types.list_domains_input
    import capo_swf.types.list_open_workflow_executions_input
    import capo_swf.types.list_tags_for_resource_input
    import capo_swf.types.list_tags_for_resource_output
    import capo_swf.types.list_workflow_types_input
    import capo_swf.types.name
    import capo_swf.types.page_size
    import capo_swf.types.page_token
    import capo_swf.types.pending_task_count
    import capo_swf.types.poll_for_activity_task_input
    import capo_swf.types.poll_for_decision_task_input
    import capo_swf.types.record_activity_task_heartbeat_input
    import capo_swf.types.register_activity_type_input
    import capo_swf.types.register_domain_input
    import capo_swf.types.register_workflow_type_input
    import capo_swf.types.registration_status
    import capo_swf.types.request_cancel_workflow_execution_input
    import capo_swf.types.resource_tag_key_list
    import capo_swf.types.resource_tag_list
    import capo_swf.types.respond_activity_task_canceled_input
    import capo_swf.types.respond_activity_task_completed_input
    import capo_swf.types.respond_activity_task_failed_input
    import capo_swf.types.respond_decision_task_completed_input
    import capo_swf.types.reverse_order
    import capo_swf.types.run
    import capo_swf.types.signal_name
    import capo_swf.types.signal_workflow_execution_input
    import capo_swf.types.start_at_previous_started_event
    import capo_swf.types.start_workflow_execution_input
    import capo_swf.types.tag_filter
    import capo_swf.types.tag_list
    import capo_swf.types.tag_resource_input
    import capo_swf.types.task_list
    import capo_swf.types.task_priority
    import capo_swf.types.task_token
    import capo_swf.types.terminate_reason
    import capo_swf.types.terminate_workflow_execution_input
    import capo_swf.types.undeprecate_activity_type_input
    import capo_swf.types.undeprecate_domain_input
    import capo_swf.types.undeprecate_workflow_type_input
    import capo_swf.types.untag_resource_input
    import capo_swf.types.version
    import capo_swf.types.workflow_execution
    import capo_swf.types.workflow_execution_count
    import capo_swf.types.workflow_execution_detail
    import capo_swf.types.workflow_execution_filter
    import capo_swf.types.workflow_execution_info
    import capo_swf.types.workflow_execution_infos
    import capo_swf.types.workflow_id
    import capo_swf.types.workflow_run_id_optional
    import capo_swf.types.workflow_type
    import capo_swf.types.workflow_type_detail
    import capo_swf.types.workflow_type_filter
    import capo_swf.types.workflow_type_info
    import capo_swf.types.workflow_type_infos


class AsyncSWFClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSWFClient:
    """A client for the ``SWF`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_dual_stack: The value of the ``AWS::UseDualStack`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
        anonymous: Send requests unsigned, without resolving credentials, even for operations that require authentication.
    """

    def __init__(
        self,
        http_handler: AsyncBaseHandler | None = None,
        operation_interceptors: Iterable[AsyncInterceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = AsyncSWFClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
                "anonymous": anonymous,
            }
        )

    def operation_options(
        self, config_overrides: Optional[AsyncSWFClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSWFClientConfig = config_overrides or {}
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
            use_dual_stack=overrides.get(
                "use_dual_stack", self._config.get("use_dual_stack")
            ),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
            anonymous=overrides.get("anonymous", self._config.get("anonymous")),
        )
        return interceptors_, options_

    async def count_closed_workflow_executions(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        start_time_filter: Optional[
            "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
        ] = None,
        close_time_filter: Optional[
            "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
        ] = None,
        execution_filter: Optional[
            "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
        ] = None,
        type_filter: Optional[
            "capo_swf.types.workflow_type_filter.WorkflowTypeFilter"
        ] = None,
        tag_filter: Optional["capo_swf.types.tag_filter.TagFilter"] = None,
        close_status_filter: Optional[
            "capo_swf.types.close_status_filter.CloseStatusFilter"
        ] = None,
    ) -> "capo_swf.types.workflow_execution_count.WorkflowExecutionCount":
        """<p>Returns the number of closed workflow executions within the given domain that meet the specified filtering criteria.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>tagFilter.tag</code>: String constraint. The key is <code>swf:tagFilter.tag</code>.</p> </li> <li> <p> <code>typeFilter.name</code>: String constraint. The key is <code>swf:typeFilter.name</code>.</p> </li> <li> <p> <code>typeFilter.version</code>: String constraint. The key is <code>swf:typeFilter.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain containing the workflow executions to count.</p>
            start_time_filter: <p>If specified, only workflow executions that meet the start time criteria of the filter are counted.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>
            close_time_filter: <p>If specified, only workflow executions that meet the close time criteria of the filter are counted.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>
            execution_filter: <p>If specified, only workflow executions matching the <code>WorkflowId</code> in the filter are counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            type_filter: <p>If specified, indicates the type of the workflow executions to be counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            tag_filter: <p>If specified, only executions that have a tag that matches the filter are counted.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            close_status_filter: <p>If specified, only workflow executions that match this close status are counted. This filter has an affect only if <code>executionStatus</code> is specified as <code>CLOSED</code>.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.count_closed_workflow_executions_input.CountClosedWorkflowExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.workflow_execution_count.WorkflowExecutionCount"
        ]:
            import capo_swf._operations.simple_workflow_service.count_closed_workflow_executions

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.count_closed_workflow_executions.async_count_closed_workflow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.count_closed_workflow_executions_input.CountClosedWorkflowExecutionsInput = {
            "domain": domain
        }
        if start_time_filter is not None:
            input_["start_time_filter"] = start_time_filter
        if close_time_filter is not None:
            input_["close_time_filter"] = close_time_filter
        if execution_filter is not None:
            input_["execution_filter"] = execution_filter
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if tag_filter is not None:
            input_["tag_filter"] = tag_filter
        if close_status_filter is not None:
            input_["close_status_filter"] = close_status_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def count_open_workflow_executions(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        start_time_filter: "capo_swf.types.execution_time_filter.ExecutionTimeFilter",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        type_filter: Optional[
            "capo_swf.types.workflow_type_filter.WorkflowTypeFilter"
        ] = None,
        tag_filter: Optional["capo_swf.types.tag_filter.TagFilter"] = None,
        execution_filter: Optional[
            "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
        ] = None,
    ) -> "capo_swf.types.workflow_execution_count.WorkflowExecutionCount":
        """<p>Returns the number of open workflow executions within the given domain that meet the specified filtering criteria.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>tagFilter.tag</code>: String constraint. The key is <code>swf:tagFilter.tag</code>.</p> </li> <li> <p> <code>typeFilter.name</code>: String constraint. The key is <code>swf:typeFilter.name</code>.</p> </li> <li> <p> <code>typeFilter.version</code>: String constraint. The key is <code>swf:typeFilter.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain containing the workflow executions to count.</p>
            start_time_filter: <p>Specifies the start time criteria that workflow executions must meet in order to be counted.</p>
            type_filter: <p>Specifies the type of the workflow executions to be counted.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            tag_filter: <p>If specified, only executions that have a tag that matches the filter are counted.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            execution_filter: <p>If specified, only workflow executions matching the <code>WorkflowId</code> in the filter are counted.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.count_open_workflow_executions_input.CountOpenWorkflowExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.workflow_execution_count.WorkflowExecutionCount"
        ]:
            import capo_swf._operations.simple_workflow_service.count_open_workflow_executions

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.count_open_workflow_executions.async_count_open_workflow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.count_open_workflow_executions_input.CountOpenWorkflowExecutionsInput = {
            "domain": domain,
            "start_time_filter": start_time_filter,
        }
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if tag_filter is not None:
            input_["tag_filter"] = tag_filter
        if execution_filter is not None:
            input_["execution_filter"] = execution_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def count_pending_activity_tasks(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        task_list: "capo_swf.types.task_list.TaskList",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> "capo_swf.types.pending_task_count.PendingTaskCount":
        """<p>Returns the estimated number of activity tasks in the specified task list. The count returned is an approximation and isn't guaranteed to be exact. If you specify a task list that no activity task was ever scheduled in then <code>0</code> is returned.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the <code>taskList.name</code> parameter by using a <code>Condition</code> element with the <code>swf:taskList.name</code> key to allow the action to access only certain task lists.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain that contains the task list.</p>
            task_list: <p>The name of the task list.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.count_pending_activity_tasks_input.CountPendingActivityTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.pending_task_count.PendingTaskCount"
        ]:
            import capo_swf._operations.simple_workflow_service.count_pending_activity_tasks

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.count_pending_activity_tasks.async_count_pending_activity_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.count_pending_activity_tasks_input.CountPendingActivityTasksInput = {
            "domain": domain,
            "task_list": task_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def count_pending_decision_tasks(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        task_list: "capo_swf.types.task_list.TaskList",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> "capo_swf.types.pending_task_count.PendingTaskCount":
        """<p>Returns the estimated number of decision tasks in the specified task list. The count returned is an approximation and isn't guaranteed to be exact. If you specify a task list that no decision task was ever scheduled in then <code>0</code> is returned.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the <code>taskList.name</code> parameter by using a <code>Condition</code> element with the <code>swf:taskList.name</code> key to allow the action to access only certain task lists.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain that contains the task list.</p>
            task_list: <p>The name of the task list.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.count_pending_decision_tasks_input.CountPendingDecisionTasksInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.pending_task_count.PendingTaskCount"
        ]:
            import capo_swf._operations.simple_workflow_service.count_pending_decision_tasks

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.count_pending_decision_tasks.async_count_pending_decision_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.count_pending_decision_tasks_input.CountPendingDecisionTasksInput = {
            "domain": domain,
            "task_list": task_list,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_activity_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        activity_type: "capo_swf.types.activity_type.ActivityType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <i>activity type</i>.</p> <p>Note: Prior to deletion, activity types must first be <b>deprecated</b>. </p> <p> After an activity type has been deleted, you cannot schedule new activities of that type. Activities that started before the type was deleted will continue to run. </p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>activityType.name</code>: String constraint. The key is <code>swf:activityType.name</code>.</p> </li> <li> <p> <code>activityType.version</code>: String constraint. The key is <code>swf:activityType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the activity type is registered.</p>
            activity_type: <p>The activity type to delete.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_not_deprecated_fault.TypeNotDeprecatedFault: <p>Returned when the resource type has not been deprecated.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.delete_activity_type_input.DeleteActivityTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.delete_activity_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.delete_activity_type.async_delete_activity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.delete_activity_type_input.DeleteActivityTypeInput = {
            "domain": domain,
            "activity_type": activity_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workflow_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_type: "capo_swf.types.workflow_type.WorkflowType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified <i>workflow type</i>.</p> <p>Note: Prior to deletion, workflow types must first be <b>deprecated</b>.</p> <p> After a workflow type has been deleted, you cannot create new executions of that type. Executions that started before the type was deleted will continue to run. </p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>workflowType.name</code>: String constraint. The key is <code>swf:workflowType.name</code>.</p> </li> <li> <p> <code>workflowType.version</code>: String constraint. The key is <code>swf:workflowType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the workflow type is registered.</p>
            workflow_type: <p>The workflow type to delete.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_not_deprecated_fault.TypeNotDeprecatedFault: <p>Returned when the resource type has not been deprecated.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.delete_workflow_type_input.DeleteWorkflowTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.delete_workflow_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.delete_workflow_type.async_delete_workflow_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.delete_workflow_type_input.DeleteWorkflowTypeInput = {
            "domain": domain,
            "workflow_type": workflow_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deprecate_activity_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        activity_type: "capo_swf.types.activity_type.ActivityType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Deprecates the specified <i>activity type</i>. After an activity type has been deprecated, you cannot create new tasks of that activity type. Tasks of this type that were scheduled before the type was deprecated continue to run.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>activityType.name</code>: String constraint. The key is <code>swf:activityType.name</code>.</p> </li> <li> <p> <code>activityType.version</code>: String constraint. The key is <code>swf:activityType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the activity type is registered.</p>
            activity_type: <p>The activity type to deprecate.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_deprecated_fault.TypeDeprecatedFault: <p>Returned when the specified activity or workflow type was already deprecated.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.deprecate_activity_type_input.DeprecateActivityTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.deprecate_activity_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.deprecate_activity_type.async_deprecate_activity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.deprecate_activity_type_input.DeprecateActivityTypeInput = {
            "domain": domain,
            "activity_type": activity_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deprecate_domain(
        self,
        name: "capo_swf.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Deprecates the specified domain. After a domain has been deprecated it cannot be used to create new workflow executions or register new types. However, you can still use visibility actions on this domain. Deprecating a domain also deprecates all activity and workflow types registered in the domain. Executions that were started before the domain was deprecated continues to run.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            name: <p>The name of the domain to deprecate.</p>

        Raises:
            capo_swf.errors.domain_deprecated_fault.DomainDeprecatedFault: <p>Returned when the specified domain has been deprecated.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.deprecate_domain_input.DeprecateDomainInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.deprecate_domain

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.deprecate_domain.async_deprecate_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.deprecate_domain_input.DeprecateDomainInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deprecate_workflow_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_type: "capo_swf.types.workflow_type.WorkflowType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Deprecates the specified <i>workflow type</i>. After a workflow type has been deprecated, you cannot create new executions of that type. Executions that were started before the type was deprecated continues to run. A deprecated workflow type may still be used when calling visibility actions.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>workflowType.name</code>: String constraint. The key is <code>swf:workflowType.name</code>.</p> </li> <li> <p> <code>workflowType.version</code>: String constraint. The key is <code>swf:workflowType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the workflow type is registered.</p>
            workflow_type: <p>The workflow type to deprecate.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_deprecated_fault.TypeDeprecatedFault: <p>Returned when the specified activity or workflow type was already deprecated.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.deprecate_workflow_type_input.DeprecateWorkflowTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.deprecate_workflow_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.deprecate_workflow_type.async_deprecate_workflow_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.deprecate_workflow_type_input.DeprecateWorkflowTypeInput = {
            "domain": domain,
            "workflow_type": workflow_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_activity_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        activity_type: "capo_swf.types.activity_type.ActivityType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> "capo_swf.types.activity_type_detail.ActivityTypeDetail":
        """<p>Returns information about the specified activity type. This includes configuration settings provided when the type was registered and other general information about the type.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>activityType.name</code>: String constraint. The key is <code>swf:activityType.name</code>.</p> </li> <li> <p> <code>activityType.version</code>: String constraint. The key is <code>swf:activityType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the activity type is registered.</p>
            activity_type: <p>The activity type to get information about. Activity types are identified by the <code>name</code> and <code>version</code> that were supplied when the activity was registered.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.describe_activity_type_input.DescribeActivityTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.activity_type_detail.ActivityTypeDetail"
        ]:
            import capo_swf._operations.simple_workflow_service.describe_activity_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.describe_activity_type.async_describe_activity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.describe_activity_type_input.DescribeActivityTypeInput = {
            "domain": domain,
            "activity_type": activity_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_domain(
        self,
        name: "capo_swf.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> "capo_swf.types.domain_detail.DomainDetail":
        """<p>Returns information about the specified domain, including description and status.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            name: <p>The name of the domain to describe.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.describe_domain_input.DescribeDomainInput]",
        ) -> AsyncOperationResponse["capo_swf.types.domain_detail.DomainDetail"]:
            import capo_swf._operations.simple_workflow_service.describe_domain

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.describe_domain.async_describe_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.describe_domain_input.DescribeDomainInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_workflow_execution(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        execution: "capo_swf.types.workflow_execution.WorkflowExecution",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> "capo_swf.types.workflow_execution_detail.WorkflowExecutionDetail":
        """<p>Returns information about the specified workflow execution including its type and some statistics.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain containing the workflow execution.</p>
            execution: <p>The workflow execution to describe.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.describe_workflow_execution_input.DescribeWorkflowExecutionInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.workflow_execution_detail.WorkflowExecutionDetail"
        ]:
            import capo_swf._operations.simple_workflow_service.describe_workflow_execution

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.describe_workflow_execution.async_describe_workflow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.describe_workflow_execution_input.DescribeWorkflowExecutionInput = {
            "domain": domain,
            "execution": execution,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_workflow_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_type: "capo_swf.types.workflow_type.WorkflowType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> "capo_swf.types.workflow_type_detail.WorkflowTypeDetail":
        """<p>Returns information about the specified <i>workflow type</i>. This includes configuration settings specified when the type was registered and other information such as creation date, current status, etc.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>workflowType.name</code>: String constraint. The key is <code>swf:workflowType.name</code>.</p> </li> <li> <p> <code>workflowType.version</code>: String constraint. The key is <code>swf:workflowType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which this workflow type is registered.</p>
            workflow_type: <p>The workflow type to describe.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.describe_workflow_type_input.DescribeWorkflowTypeInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.workflow_type_detail.WorkflowTypeDetail"
        ]:
            import capo_swf._operations.simple_workflow_service.describe_workflow_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.describe_workflow_type.async_describe_workflow_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.describe_workflow_type_input.DescribeWorkflowTypeInput = {
            "domain": domain,
            "workflow_type": workflow_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_workflow_execution_history(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        execution: "capo_swf.types.workflow_execution.WorkflowExecution",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_swf.types.history.History":
        """<p>Returns the history of the specified workflow execution. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the <code>nextPageToken</code> returned by the initial call.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain containing the workflow execution.</p>
            execution: <p>Specifies the workflow execution for which to return the history.</p>
            next_page_token: <p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>
            maximum_page_size: <p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>
            reverse_order: <p>When set to <code>true</code>, returns the events in reverse order. By default the results are returned in ascending order of the <code>eventTimeStamp</code> of the events.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.get_workflow_execution_history_input.GetWorkflowExecutionHistoryInput]",
        ) -> AsyncOperationResponse["capo_swf.types.history.History"]:
            import capo_swf._operations.simple_workflow_service.get_workflow_execution_history

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.get_workflow_execution_history.async_get_workflow_execution_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.get_workflow_execution_history_input.GetWorkflowExecutionHistoryInput = {
            "domain": domain,
            "execution": execution,
        }
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if maximum_page_size is not None:
            input_["maximum_page_size"] = maximum_page_size
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_workflow_execution_history(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        execution: "capo_swf.types.workflow_execution.WorkflowExecution",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "AsyncIterator[capo_swf.types.history_event.HistoryEvent]":
        _token = next_page_token
        while True:
            _response = await self.get_workflow_execution_history(
                domain,
                execution,
                config_overrides=config_overrides,
                next_page_token=_token,
                maximum_page_size=maximum_page_size,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_activity_types(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        registration_status: "capo_swf.types.registration_status.RegistrationStatus",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        name: Optional["capo_swf.types.name.Name"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_swf.types.activity_type_infos.ActivityTypeInfos":
        """<p>Returns information about all activities registered in the specified domain that match the specified name and registration status. The result includes information like creation date, current status of the activity, etc. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the <code>nextPageToken</code> returned by the initial call.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the activity types have been registered.</p>
            name: <p>If specified, only lists the activity types that have this name.</p>
            registration_status: <p>Specifies the registration status of the activity types to list.</p>
            next_page_token: <p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>
            maximum_page_size: <p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>
            reverse_order: <p>When set to <code>true</code>, returns the results in reverse order. By default, the results are returned in ascending alphabetical order by <code>name</code> of the activity types.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.list_activity_types_input.ListActivityTypesInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.activity_type_infos.ActivityTypeInfos"
        ]:
            import capo_swf._operations.simple_workflow_service.list_activity_types

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.list_activity_types.async_list_activity_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.list_activity_types_input.ListActivityTypesInput = {
            "domain": domain,
            "registration_status": registration_status,
        }
        if name is not None:
            input_["name"] = name
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if maximum_page_size is not None:
            input_["maximum_page_size"] = maximum_page_size
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_activity_types(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        registration_status: "capo_swf.types.registration_status.RegistrationStatus",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        name: Optional["capo_swf.types.name.Name"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "AsyncIterator[capo_swf.types.activity_type_info.ActivityTypeInfo]":
        _token = next_page_token
        while True:
            _response = await self.list_activity_types(
                domain,
                registration_status,
                config_overrides=config_overrides,
                name=name,
                next_page_token=_token,
                maximum_page_size=maximum_page_size,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("type_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_closed_workflow_executions(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        start_time_filter: Optional[
            "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
        ] = None,
        close_time_filter: Optional[
            "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
        ] = None,
        execution_filter: Optional[
            "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
        ] = None,
        close_status_filter: Optional[
            "capo_swf.types.close_status_filter.CloseStatusFilter"
        ] = None,
        type_filter: Optional[
            "capo_swf.types.workflow_type_filter.WorkflowTypeFilter"
        ] = None,
        tag_filter: Optional["capo_swf.types.tag_filter.TagFilter"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_swf.types.workflow_execution_infos.WorkflowExecutionInfos":
        """<p>Returns a list of closed workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>tagFilter.tag</code>: String constraint. The key is <code>swf:tagFilter.tag</code>.</p> </li> <li> <p> <code>typeFilter.name</code>: String constraint. The key is <code>swf:typeFilter.name</code>.</p> </li> <li> <p> <code>typeFilter.version</code>: String constraint. The key is <code>swf:typeFilter.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain that contains the workflow executions to list.</p>
            start_time_filter: <p>If specified, the workflow executions are included in the returned results based on whether their start times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their start times.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>
            close_time_filter: <p>If specified, the workflow executions are included in the returned results based on whether their close times are within the range specified by this filter. Also, if this parameter is specified, the returned results are ordered by their close times.</p> <note> <p> <code>startTimeFilter</code> and <code>closeTimeFilter</code> are mutually exclusive. You must specify one of these in a request but not both.</p> </note>
            execution_filter: <p>If specified, only workflow executions matching the workflow ID specified in the filter are returned.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            close_status_filter: <p>If specified, only workflow executions that match this <i>close status</i> are listed. For example, if TERMINATED is specified, then only TERMINATED workflow executions are listed.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            type_filter: <p>If specified, only executions of the type specified in the filter are returned.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            tag_filter: <p>If specified, only executions that have the matching tag are listed.</p> <note> <p> <code>closeStatusFilter</code>, <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            next_page_token: <p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>
            maximum_page_size: <p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>
            reverse_order: <p>When set to <code>true</code>, returns the results in reverse order. By default the results are returned in descending order of the start or the close time of the executions.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.list_closed_workflow_executions_input.ListClosedWorkflowExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.workflow_execution_infos.WorkflowExecutionInfos"
        ]:
            import capo_swf._operations.simple_workflow_service.list_closed_workflow_executions

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.list_closed_workflow_executions.async_list_closed_workflow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.list_closed_workflow_executions_input.ListClosedWorkflowExecutionsInput = {
            "domain": domain
        }
        if start_time_filter is not None:
            input_["start_time_filter"] = start_time_filter
        if close_time_filter is not None:
            input_["close_time_filter"] = close_time_filter
        if execution_filter is not None:
            input_["execution_filter"] = execution_filter
        if close_status_filter is not None:
            input_["close_status_filter"] = close_status_filter
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if tag_filter is not None:
            input_["tag_filter"] = tag_filter
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if maximum_page_size is not None:
            input_["maximum_page_size"] = maximum_page_size
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_closed_workflow_executions(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        start_time_filter: Optional[
            "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
        ] = None,
        close_time_filter: Optional[
            "capo_swf.types.execution_time_filter.ExecutionTimeFilter"
        ] = None,
        execution_filter: Optional[
            "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
        ] = None,
        close_status_filter: Optional[
            "capo_swf.types.close_status_filter.CloseStatusFilter"
        ] = None,
        type_filter: Optional[
            "capo_swf.types.workflow_type_filter.WorkflowTypeFilter"
        ] = None,
        tag_filter: Optional["capo_swf.types.tag_filter.TagFilter"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "AsyncIterator[capo_swf.types.workflow_execution_info.WorkflowExecutionInfo]":
        _token = next_page_token
        while True:
            _response = await self.list_closed_workflow_executions(
                domain,
                config_overrides=config_overrides,
                start_time_filter=start_time_filter,
                close_time_filter=close_time_filter,
                execution_filter=execution_filter,
                close_status_filter=close_status_filter,
                type_filter=type_filter,
                tag_filter=tag_filter,
                next_page_token=_token,
                maximum_page_size=maximum_page_size,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("execution_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_domains(
        self,
        registration_status: "capo_swf.types.registration_status.RegistrationStatus",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_swf.types.domain_infos.DomainInfos":
        """<p>Returns the list of domains registered in the account. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains. The element must be set to <code>arn:aws:swf::AccountID:domain/*</code>, where <i>AccountID</i> is the account ID, with no dashes.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            next_page_token: <p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>
            registration_status: <p>Specifies the registration status of the domains to list.</p>
            maximum_page_size: <p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>
            reverse_order: <p>When set to <code>true</code>, returns the results in reverse order. By default, the results are returned in ascending alphabetical order by <code>name</code> of the domains.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.list_domains_input.ListDomainsInput]",
        ) -> AsyncOperationResponse["capo_swf.types.domain_infos.DomainInfos"]:
            import capo_swf._operations.simple_workflow_service.list_domains

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.list_domains.async_list_domains(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.list_domains_input.ListDomainsInput = {
            "registration_status": registration_status
        }
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if maximum_page_size is not None:
            input_["maximum_page_size"] = maximum_page_size
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_domains(
        self,
        registration_status: "capo_swf.types.registration_status.RegistrationStatus",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "AsyncIterator[capo_swf.types.domain_info.DomainInfo]":
        _token = next_page_token
        while True:
            _response = await self.list_domains(
                registration_status,
                config_overrides=config_overrides,
                next_page_token=_token,
                maximum_page_size=maximum_page_size,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("domain_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_open_workflow_executions(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        start_time_filter: "capo_swf.types.execution_time_filter.ExecutionTimeFilter",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        type_filter: Optional[
            "capo_swf.types.workflow_type_filter.WorkflowTypeFilter"
        ] = None,
        tag_filter: Optional["capo_swf.types.tag_filter.TagFilter"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
        execution_filter: Optional[
            "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
        ] = None,
    ) -> "capo_swf.types.workflow_execution_infos.WorkflowExecutionInfos":
        """<p>Returns a list of open workflow executions in the specified domain that meet the filtering criteria. The results may be split into multiple pages. To retrieve subsequent pages, make the call again using the nextPageToken returned by the initial call.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>tagFilter.tag</code>: String constraint. The key is <code>swf:tagFilter.tag</code>.</p> </li> <li> <p> <code>typeFilter.name</code>: String constraint. The key is <code>swf:typeFilter.name</code>.</p> </li> <li> <p> <code>typeFilter.version</code>: String constraint. The key is <code>swf:typeFilter.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain that contains the workflow executions to list.</p>
            start_time_filter: <p>Workflow executions are included in the returned results based on whether their start times are within the range specified by this filter.</p>
            type_filter: <p>If specified, only executions of the type specified in the filter are returned.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            tag_filter: <p>If specified, only executions that have the matching tag are listed.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>
            next_page_token: <p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>
            maximum_page_size: <p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>
            reverse_order: <p>When set to <code>true</code>, returns the results in reverse order. By default the results are returned in descending order of the start time of the executions.</p>
            execution_filter: <p>If specified, only workflow executions matching the workflow ID specified in the filter are returned.</p> <note> <p> <code>executionFilter</code>, <code>typeFilter</code> and <code>tagFilter</code> are mutually exclusive. You can specify at most one of these in a request.</p> </note>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.list_open_workflow_executions_input.ListOpenWorkflowExecutionsInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.workflow_execution_infos.WorkflowExecutionInfos"
        ]:
            import capo_swf._operations.simple_workflow_service.list_open_workflow_executions

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.list_open_workflow_executions.async_list_open_workflow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.list_open_workflow_executions_input.ListOpenWorkflowExecutionsInput = {
            "domain": domain,
            "start_time_filter": start_time_filter,
        }
        if type_filter is not None:
            input_["type_filter"] = type_filter
        if tag_filter is not None:
            input_["tag_filter"] = tag_filter
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if maximum_page_size is not None:
            input_["maximum_page_size"] = maximum_page_size
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if execution_filter is not None:
            input_["execution_filter"] = execution_filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_open_workflow_executions(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        start_time_filter: "capo_swf.types.execution_time_filter.ExecutionTimeFilter",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        type_filter: Optional[
            "capo_swf.types.workflow_type_filter.WorkflowTypeFilter"
        ] = None,
        tag_filter: Optional["capo_swf.types.tag_filter.TagFilter"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
        execution_filter: Optional[
            "capo_swf.types.workflow_execution_filter.WorkflowExecutionFilter"
        ] = None,
    ) -> "AsyncIterator[capo_swf.types.workflow_execution_info.WorkflowExecutionInfo]":
        _token = next_page_token
        while True:
            _response = await self.list_open_workflow_executions(
                domain,
                start_time_filter,
                config_overrides=config_overrides,
                type_filter=type_filter,
                tag_filter=tag_filter,
                next_page_token=_token,
                maximum_page_size=maximum_page_size,
                reverse_order=reverse_order,
                execution_filter=execution_filter,
            )
            _page = _resolve_path(_response, ("execution_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_swf.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> "capo_swf.types.list_tags_for_resource_output.ListTagsForResourceOutput":
        """<p>List tags for a given domain.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the Amazon SWF domain.</p>

        Raises:
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.list_tags_for_resource_input.ListTagsForResourceInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.list_tags_for_resource_output.ListTagsForResourceOutput"
        ]:
            import capo_swf._operations.simple_workflow_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.list_tags_for_resource_input.ListTagsForResourceInput = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_workflow_types(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        registration_status: "capo_swf.types.registration_status.RegistrationStatus",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        name: Optional["capo_swf.types.name.Name"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "capo_swf.types.workflow_type_infos.WorkflowTypeInfos":
        """<p>Returns information about workflow types in the specified domain. The results may be split into multiple pages that can be retrieved by making the call repeatedly.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the workflow types have been registered.</p>
            name: <p>If specified, lists the workflow type with this name.</p>
            registration_status: <p>Specifies the registration status of the workflow types to list.</p>
            next_page_token: <p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p>
            maximum_page_size: <p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p>
            reverse_order: <p>When set to <code>true</code>, returns the results in reverse order. By default the results are returned in ascending alphabetical order of the <code>name</code> of the workflow types.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.list_workflow_types_input.ListWorkflowTypesInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.workflow_type_infos.WorkflowTypeInfos"
        ]:
            import capo_swf._operations.simple_workflow_service.list_workflow_types

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.list_workflow_types.async_list_workflow_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.list_workflow_types_input.ListWorkflowTypesInput = {
            "domain": domain,
            "registration_status": registration_status,
        }
        if name is not None:
            input_["name"] = name
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if maximum_page_size is not None:
            input_["maximum_page_size"] = maximum_page_size
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_workflow_types(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        registration_status: "capo_swf.types.registration_status.RegistrationStatus",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        name: Optional["capo_swf.types.name.Name"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
    ) -> "AsyncIterator[capo_swf.types.workflow_type_info.WorkflowTypeInfo]":
        _token = next_page_token
        while True:
            _response = await self.list_workflow_types(
                domain,
                registration_status,
                config_overrides=config_overrides,
                name=name,
                next_page_token=_token,
                maximum_page_size=maximum_page_size,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("type_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def poll_for_activity_task(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        task_list: "capo_swf.types.task_list.TaskList",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        identity: Optional["capo_swf.types.identity.Identity"] = None,
    ) -> "capo_swf.types.activity_task.ActivityTask":
        r"""<p>Used by workers to get an <a>ActivityTask</a> from the specified activity <code>taskList</code>. This initiates a long poll, where the service holds the HTTP connection open and responds as soon as a task becomes available. The maximum time the service holds on to the request before responding is 60 seconds. If no task is available within 60 seconds, the poll returns an empty result. An empty result, in this context, means that an ActivityTask is returned, but that the value of taskToken is an empty string. If a task is returned, the worker should use its type to identify and process it correctly.</p> <important> <p>Workers should set their client side socket timeout to at least 70 seconds (10 seconds higher than the maximum time service may hold the poll request).</p> </important> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the <code>taskList.name</code> parameter by using a <code>Condition</code> element with the <code>swf:taskList.name</code> key to allow the action to access only certain task lists.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain that contains the task lists being polled.</p>
            task_list: <p>Specifies the task list to poll for activity tasks.</p> <p>The specified string must not start or end with whitespace. It must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            identity: <p>Identity of the worker making the request, recorded in the <code>ActivityTaskStarted</code> event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.</p>

        Raises:
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.poll_for_activity_task_input.PollForActivityTaskInput]",
        ) -> AsyncOperationResponse["capo_swf.types.activity_task.ActivityTask"]:
            import capo_swf._operations.simple_workflow_service.poll_for_activity_task

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.poll_for_activity_task.async_poll_for_activity_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.poll_for_activity_task_input.PollForActivityTaskInput = {
            "domain": domain,
            "task_list": task_list,
        }
        if identity is not None:
            input_["identity"] = identity

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def poll_for_decision_task(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        task_list: "capo_swf.types.task_list.TaskList",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        identity: Optional["capo_swf.types.identity.Identity"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
        start_at_previous_started_event: Optional[
            "capo_swf.types.start_at_previous_started_event.StartAtPreviousStartedEvent"
        ] = None,
    ) -> "capo_swf.types.decision_task.DecisionTask":
        r"""<p>Used by deciders to get a <a>DecisionTask</a> from the specified decision <code>taskList</code>. A decision task may be returned for any open workflow execution that is using the specified task list. The task includes a paginated view of the history of the workflow execution. The decider should use the workflow type and the history to determine how to properly handle the task.</p> <p>This action initiates a long poll, where the service holds the HTTP connection open and responds as soon a task becomes available. If no decision task is available in the specified task list before the timeout of 60 seconds expires, an empty result is returned. An empty result, in this context, means that a DecisionTask is returned, but that the value of taskToken is an empty string.</p> <important> <p>Deciders should set their client side socket timeout to at least 70 seconds (10 seconds higher than the timeout).</p> </important> <important> <p>Because the number of workflow history events for a single workflow execution might be very large, the result returned might be split up across a number of pages. To retrieve subsequent pages, make additional calls to <code>PollForDecisionTask</code> using the <code>nextPageToken</code> returned by the initial call. Note that you do <i>not</i> call <code>GetWorkflowExecutionHistory</code> with this <code>nextPageToken</code>. Instead, call <code>PollForDecisionTask</code> again.</p> </important> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the <code>taskList.name</code> parameter by using a <code>Condition</code> element with the <code>swf:taskList.name</code> key to allow the action to access only certain task lists.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain containing the task lists to poll.</p>
            task_list: <p>Specifies the task list to poll for decision tasks.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            identity: <p>Identity of the decider making the request, which is recorded in the DecisionTaskStarted event in the workflow history. This enables diagnostic tracing when problems arise. The form of this identity is user defined.</p>
            next_page_token: <p>If <code>NextPageToken</code> is returned there are more results available. The value of <code>NextPageToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return a <code>400</code> error: "<code>Specified token has exceeded its maximum lifetime</code>". </p> <p>The configured <code>maximumPageSize</code> determines how many results can be returned in a single call. </p> <note> <p>The <code>nextPageToken</code> returned by this action cannot be used with <a>GetWorkflowExecutionHistory</a> to get the next page. You must call <a>PollForDecisionTask</a> again (with the <code>nextPageToken</code>) to retrieve the next page of history records. Calling <a>PollForDecisionTask</a> with a <code>nextPageToken</code> doesn't return a new decision task.</p> </note>
            maximum_page_size: <p>The maximum number of results that are returned per call. Use <code>nextPageToken</code> to obtain further pages of results. </p> <p>This is an upper limit only; the actual number of results returned per call may be fewer than the specified maximum.</p>
            reverse_order: <p>When set to <code>true</code>, returns the events in reverse order. By default the results are returned in ascending order of the <code>eventTimestamp</code> of the events.</p>
            start_at_previous_started_event: <p>When set to <code>true</code>, returns the events with <code>eventTimestamp</code> greater than or equal to <code>eventTimestamp</code> of the most recent <code>DecisionTaskStarted</code> event. By default, this parameter is set to <code>false</code>.</p>

        Raises:
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.poll_for_decision_task_input.PollForDecisionTaskInput]",
        ) -> AsyncOperationResponse["capo_swf.types.decision_task.DecisionTask"]:
            import capo_swf._operations.simple_workflow_service.poll_for_decision_task

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.poll_for_decision_task.async_poll_for_decision_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.poll_for_decision_task_input.PollForDecisionTaskInput = {
            "domain": domain,
            "task_list": task_list,
        }
        if identity is not None:
            input_["identity"] = identity
        if next_page_token is not None:
            input_["next_page_token"] = next_page_token
        if maximum_page_size is not None:
            input_["maximum_page_size"] = maximum_page_size
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order
        if start_at_previous_started_event is not None:
            input_["start_at_previous_started_event"] = start_at_previous_started_event

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_poll_for_decision_task(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        task_list: "capo_swf.types.task_list.TaskList",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        identity: Optional["capo_swf.types.identity.Identity"] = None,
        next_page_token: Optional["capo_swf.types.page_token.PageToken"] = None,
        maximum_page_size: Optional["capo_swf.types.page_size.PageSize"] = None,
        reverse_order: Optional["capo_swf.types.reverse_order.ReverseOrder"] = None,
        start_at_previous_started_event: Optional[
            "capo_swf.types.start_at_previous_started_event.StartAtPreviousStartedEvent"
        ] = None,
    ) -> "AsyncIterator[capo_swf.types.history_event.HistoryEvent]":
        _token = next_page_token
        while True:
            _response = await self.poll_for_decision_task(
                domain,
                task_list,
                config_overrides=config_overrides,
                identity=identity,
                next_page_token=_token,
                maximum_page_size=maximum_page_size,
                reverse_order=reverse_order,
                start_at_previous_started_event=start_at_previous_started_event,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_page_token",))
            if not _token:
                break

    async def record_activity_task_heartbeat(
        self,
        task_token: "capo_swf.types.task_token.TaskToken",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        details: Optional["capo_swf.types.limited_data.LimitedData"] = None,
    ) -> "capo_swf.types.activity_task_status.ActivityTaskStatus":
        """<p>Used by activity workers to report to the service that the <a>ActivityTask</a> represented by the specified <code>taskToken</code> is still making progress. The worker can also specify details of the progress, for example percent complete, using the <code>details</code> parameter. This action can also be used by the worker as a mechanism to check if cancellation is being requested for the activity task. If a cancellation is being attempted for the specified task, then the boolean <code>cancelRequested</code> flag returned by the service is set to <code>true</code>.</p> <p>This action resets the <code>taskHeartbeatTimeout</code> clock. The <code>taskHeartbeatTimeout</code> is specified in <a>RegisterActivityType</a>.</p> <p>This action doesn't in itself create an event in the workflow execution history. However, if the task times out, the workflow execution history contains a <code>ActivityTaskTimedOut</code> event that contains the information from the last heartbeat generated by the activity worker.</p> <note> <p>The <code>taskStartToCloseTimeout</code> of an activity type is the maximum duration of an activity task, regardless of the number of <a>RecordActivityTaskHeartbeat</a> requests received. The <code>taskStartToCloseTimeout</code> is also specified in <a>RegisterActivityType</a>.</p> </note> <note> <p>This operation is only useful for long-lived activities to report liveliness of the task and to determine if a cancellation is being attempted.</p> </note> <important> <p>If the <code>cancelRequested</code> flag returns <code>true</code>, a cancellation is being attempted. If the worker can cancel the activity, it should respond with <a>RespondActivityTaskCanceled</a>. Otherwise, it should ignore the cancellation request.</p> </important> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            task_token: <p>The <code>taskToken</code> of the <a>ActivityTask</a>.</p> <important> <p> <code>taskToken</code> is generated by the service and should be treated as an opaque value. If the task is passed to another process, its <code>taskToken</code> must also be passed. This enables it to provide its progress and respond with results. </p> </important>
            details: <p>If specified, contains details about the progress of the task.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.record_activity_task_heartbeat_input.RecordActivityTaskHeartbeatInput]",
        ) -> AsyncOperationResponse[
            "capo_swf.types.activity_task_status.ActivityTaskStatus"
        ]:
            import capo_swf._operations.simple_workflow_service.record_activity_task_heartbeat

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.record_activity_task_heartbeat.async_record_activity_task_heartbeat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.record_activity_task_heartbeat_input.RecordActivityTaskHeartbeatInput = {
            "task_token": task_token
        }
        if details is not None:
            input_["details"] = details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_activity_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        name: "capo_swf.types.name.Name",
        version: "capo_swf.types.version.Version",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        description: Optional["capo_swf.types.description.Description"] = None,
        default_task_start_to_close_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
        default_task_heartbeat_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
        default_task_list: Optional["capo_swf.types.task_list.TaskList"] = None,
        default_task_priority: Optional[
            "capo_swf.types.task_priority.TaskPriority"
        ] = None,
        default_task_schedule_to_start_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
        default_task_schedule_to_close_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
    ) -> None:
        r"""<p>Registers a new <i>activity type</i> along with its configuration settings in the specified domain.</p> <important> <p>A <code>TypeAlreadyExists</code> fault is returned if the type already exists in the domain. You cannot change any configuration settings of the type after its registration, and it must be registered as a new version.</p> </important> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>defaultTaskList.name</code>: String constraint. The key is <code>swf:defaultTaskList.name</code>.</p> </li> <li> <p> <code>name</code>: String constraint. The key is <code>swf:name</code>.</p> </li> <li> <p> <code>version</code>: String constraint. The key is <code>swf:version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which this activity is to be registered.</p>
            name: <p>The name of the activity type within the domain.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            version: <p>The version of the activity type.</p> <note> <p>The activity type consists of the name and version, the combination of which must be unique within the domain.</p> </note> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            description: <p>A textual description of the activity type.</p>
            default_task_start_to_close_timeout: <p>If set, specifies the default maximum duration that a worker can take to process tasks of this activity type. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>
            default_task_heartbeat_timeout: <p>If set, specifies the default maximum time before which a worker processing a task of this type must report progress by calling <a>RecordActivityTaskHeartbeat</a>. If the timeout is exceeded, the activity task is automatically timed out. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>. If the activity worker subsequently attempts to record a heartbeat or returns a result, the activity worker receives an <code>UnknownResource</code> fault. In this case, Amazon SWF no longer considers the activity task to be valid; the activity worker should clean up the activity task.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>
            default_task_list: <p>If set, specifies the default task list to use for scheduling tasks of this activity type. This default task list is used if a task list isn't provided when a task is scheduled through the <code>ScheduleActivityTask</code> <a>Decision</a>.</p>
            default_task_priority: <p>The default task priority to assign to the activity type. If not assigned, then <code>0</code> is used. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>in the <i>Amazon SWF Developer Guide</i>.</i>.</p>
            default_task_schedule_to_start_timeout: <p>If set, specifies the default maximum duration that a task of this activity type can wait before being assigned to a worker. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>
            default_task_schedule_to_close_timeout: <p>If set, specifies the default maximum duration for a task of this activity type. This default can be overridden when scheduling an activity task using the <code>ScheduleActivityTask</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>

        Raises:
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_already_exists_fault.TypeAlreadyExistsFault: <p>Returned if the type already exists in the specified domain. You may get this fault if you are registering a type that is either already registered or deprecated, or if you undeprecate a type that is currently registered.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.register_activity_type_input.RegisterActivityTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.register_activity_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.register_activity_type.async_register_activity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.register_activity_type_input.RegisterActivityTypeInput = {
            "domain": domain,
            "name": name,
            "version": version,
        }
        if description is not None:
            input_["description"] = description
        if default_task_start_to_close_timeout is not None:
            input_["default_task_start_to_close_timeout"] = (
                default_task_start_to_close_timeout
            )
        if default_task_heartbeat_timeout is not None:
            input_["default_task_heartbeat_timeout"] = default_task_heartbeat_timeout
        if default_task_list is not None:
            input_["default_task_list"] = default_task_list
        if default_task_priority is not None:
            input_["default_task_priority"] = default_task_priority
        if default_task_schedule_to_start_timeout is not None:
            input_["default_task_schedule_to_start_timeout"] = (
                default_task_schedule_to_start_timeout
            )
        if default_task_schedule_to_close_timeout is not None:
            input_["default_task_schedule_to_close_timeout"] = (
                default_task_schedule_to_close_timeout
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_domain(
        self,
        name: "capo_swf.types.domain_name.DomainName",
        workflow_execution_retention_period_in_days: "capo_swf.types.duration_in_days.DurationInDays",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        description: Optional["capo_swf.types.description.Description"] = None,
        tags: Optional["capo_swf.types.resource_tag_list.ResourceTagList"] = None,
    ) -> None:
        r"""<p>Registers a new domain.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>You cannot use an IAM policy to control domain access for this action. The name of the domain being registered is available as the resource of this action.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            name: <p>Name of the domain to register. The name must be unique in the region that the domain is registered in.</p> <p>The specified string must not start or end with whitespace. It must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            description: <p>A text description of the domain.</p>
            workflow_execution_retention_period_in_days: <p>The duration (in days) that records and histories of workflow executions on the domain should be kept by the service. After the retention period, the workflow execution isn't available in the results of visibility calls.</p> <p>If you pass the value <code>NONE</code> or <code>0</code> (zero), then the workflow execution history isn't retained. As soon as the workflow execution completes, the execution record and its history are deleted.</p> <p>The maximum workflow execution retention period is 90 days. For more information about Amazon SWF service limits, see: <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-limits.html">Amazon SWF Service Limits</a> in the <i>Amazon SWF Developer Guide</i>.</p>
            tags: <p>Tags to be added when registering a domain.</p> <p>Tags may only contain unicode letters, digits, whitespace, or these symbols: <code>_ . : / = + - @</code>.</p>

        Raises:
            capo_swf.errors.domain_already_exists_fault.DomainAlreadyExistsFault: <p>Returned if the domain already exists. You may get this fault if you are registering a domain that is either already registered or deprecated, or if you undeprecate a domain that is currently registered.</p>
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.too_many_tags_fault.TooManyTagsFault: <p>You've exceeded the number of tags allowed for a domain.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.register_domain_input.RegisterDomainInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.register_domain

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.register_domain.async_register_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.register_domain_input.RegisterDomainInput = {
            "name": name,
            "workflow_execution_retention_period_in_days": workflow_execution_retention_period_in_days,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_workflow_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        name: "capo_swf.types.name.Name",
        version: "capo_swf.types.version.Version",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        description: Optional["capo_swf.types.description.Description"] = None,
        default_task_start_to_close_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
        default_execution_start_to_close_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
        default_task_list: Optional["capo_swf.types.task_list.TaskList"] = None,
        default_task_priority: Optional[
            "capo_swf.types.task_priority.TaskPriority"
        ] = None,
        default_child_policy: Optional[
            "capo_swf.types.child_policy.ChildPolicy"
        ] = None,
        default_lambda_role: Optional["capo_swf.types.arn.Arn"] = None,
    ) -> None:
        r"""<p>Registers a new <i>workflow type</i> and its configuration settings in the specified domain.</p> <p>The retention period for the workflow history is set by the <a>RegisterDomain</a> action.</p> <important> <p>If the type already exists, then a <code>TypeAlreadyExists</code> fault is returned. You cannot change the configuration settings of a workflow type once it is registered and it must be registered as a new version.</p> </important> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>defaultTaskList.name</code>: String constraint. The key is <code>swf:defaultTaskList.name</code>.</p> </li> <li> <p> <code>name</code>: String constraint. The key is <code>swf:name</code>.</p> </li> <li> <p> <code>version</code>: String constraint. The key is <code>swf:version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which to register the workflow type.</p>
            name: <p>The name of the workflow type.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            version: <p>The version of the workflow type.</p> <note> <p>The workflow type consists of the name and version, the combination of which must be unique within the domain. To get a list of all currently registered workflow types, use the <a>ListWorkflowTypes</a> action.</p> </note> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            description: <p>Textual description of the workflow type.</p>
            default_task_start_to_close_timeout: <p>If set, specifies the default maximum duration of decision tasks for this workflow type. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p>
            default_execution_start_to_close_timeout: <p>If set, specifies the default maximum duration for executions of this workflow type. You can override this default when starting an execution through the <a>StartWorkflowExecution</a> Action or <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The duration is specified in seconds; an integer greater than or equal to 0. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for <code>defaultExecutionStartToCloseTimeout</code>; there is a one-year max limit on the time that a workflow execution can run. Exceeding this limit always causes the workflow execution to time out.</p>
            default_task_list: <p>If set, specifies the default task list to use for scheduling decision tasks for executions of this workflow type. This default is used only if a task list isn't provided when starting the execution through the <a>StartWorkflowExecution</a> Action or <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p>
            default_task_priority: <p>The default task priority to assign to the workflow type. If not assigned, then <code>0</code> is used. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>
            default_child_policy: <p>If set, specifies the default policy to use for the child workflow executions when a workflow execution of this type is terminated, by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout. This default can be overridden when starting a workflow execution using the <a>StartWorkflowExecution</a> action or the <code>StartChildWorkflowExecution</code> <a>Decision</a>.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul>
            default_lambda_role: <p>The default IAM role attached to this workflow type.</p> <note> <p>Executions of this workflow type need IAM roles to invoke Lambda functions. If you don't specify an IAM role when you start this workflow type, the default Lambda role is attached to the execution. For more information, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html">https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>

        Raises:
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_already_exists_fault.TypeAlreadyExistsFault: <p>Returned if the type already exists in the specified domain. You may get this fault if you are registering a type that is either already registered or deprecated, or if you undeprecate a type that is currently registered.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.register_workflow_type_input.RegisterWorkflowTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.register_workflow_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.register_workflow_type.async_register_workflow_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.register_workflow_type_input.RegisterWorkflowTypeInput = {
            "domain": domain,
            "name": name,
            "version": version,
        }
        if description is not None:
            input_["description"] = description
        if default_task_start_to_close_timeout is not None:
            input_["default_task_start_to_close_timeout"] = (
                default_task_start_to_close_timeout
            )
        if default_execution_start_to_close_timeout is not None:
            input_["default_execution_start_to_close_timeout"] = (
                default_execution_start_to_close_timeout
            )
        if default_task_list is not None:
            input_["default_task_list"] = default_task_list
        if default_task_priority is not None:
            input_["default_task_priority"] = default_task_priority
        if default_child_policy is not None:
            input_["default_child_policy"] = default_child_policy
        if default_lambda_role is not None:
            input_["default_lambda_role"] = default_lambda_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def request_cancel_workflow_execution(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_id: "capo_swf.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        run_id: Optional[
            "capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
        ] = None,
    ) -> None:
        """<p>Records a <code>WorkflowExecutionCancelRequested</code> event in the currently running workflow execution identified by the given domain, workflowId, and runId. This logically requests the cancellation of the workflow execution as a whole. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> <note> <p>If the runId isn't specified, the <code>WorkflowExecutionCancelRequested</code> event is recorded in the history of the current open workflow execution with the specified workflowId in the domain.</p> </note> <note> <p>Because this action allows the workflow to properly clean up and gracefully close, it should be used instead of <a>TerminateWorkflowExecution</a> when possible.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain containing the workflow execution to cancel.</p>
            workflow_id: <p>The workflowId of the workflow execution to cancel.</p>
            run_id: <p>The runId of the workflow execution to cancel.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.request_cancel_workflow_execution_input.RequestCancelWorkflowExecutionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.request_cancel_workflow_execution

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.request_cancel_workflow_execution.async_request_cancel_workflow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.request_cancel_workflow_execution_input.RequestCancelWorkflowExecutionInput = {
            "domain": domain,
            "workflow_id": workflow_id,
        }
        if run_id is not None:
            input_["run_id"] = run_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def respond_activity_task_canceled(
        self,
        task_token: "capo_swf.types.task_token.TaskToken",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        details: Optional["capo_swf.types.data.Data"] = None,
    ) -> None:
        """<p>Used by workers to tell the service that the <a>ActivityTask</a> identified by the <code>taskToken</code> was successfully canceled. Additional <code>details</code> can be provided using the <code>details</code> argument.</p> <p>These <code>details</code> (if provided) appear in the <code>ActivityTaskCanceled</code> event added to the workflow history.</p> <important> <p>Only use this operation if the <code>canceled</code> flag of a <a>RecordActivityTaskHeartbeat</a> request returns <code>true</code> and if the activity can be safely undone or abandoned.</p> </important> <p>A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to <a>RespondActivityTaskCompleted</a>, RespondActivityTaskCanceled, <a>RespondActivityTaskFailed</a>, or the task has <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html#swf-dev-timeout-types">timed out</a>.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            task_token: <p>The <code>taskToken</code> of the <a>ActivityTask</a>.</p> <important> <p> <code>taskToken</code> is generated by the service and should be treated as an opaque value. If the task is passed to another process, its <code>taskToken</code> must also be passed. This enables it to provide its progress and respond with results.</p> </important>
            details: <p> Information about the cancellation.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.respond_activity_task_canceled_input.RespondActivityTaskCanceledInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.respond_activity_task_canceled

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.respond_activity_task_canceled.async_respond_activity_task_canceled(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.respond_activity_task_canceled_input.RespondActivityTaskCanceledInput = {
            "task_token": task_token
        }
        if details is not None:
            input_["details"] = details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def respond_activity_task_completed(
        self,
        task_token: "capo_swf.types.task_token.TaskToken",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        result: Optional["capo_swf.types.data.Data"] = None,
    ) -> None:
        """<p>Used by workers to tell the service that the <a>ActivityTask</a> identified by the <code>taskToken</code> completed successfully with a <code>result</code> (if provided). The <code>result</code> appears in the <code>ActivityTaskCompleted</code> event in the workflow history.</p> <important> <p>If the requested task doesn't complete successfully, use <a>RespondActivityTaskFailed</a> instead. If the worker finds that the task is canceled through the <code>canceled</code> flag returned by <a>RecordActivityTaskHeartbeat</a>, it should cancel the task, clean up and then call <a>RespondActivityTaskCanceled</a>.</p> </important> <p>A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to RespondActivityTaskCompleted, <a>RespondActivityTaskCanceled</a>, <a>RespondActivityTaskFailed</a>, or the task has <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html#swf-dev-timeout-types">timed out</a>.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            task_token: <p>The <code>taskToken</code> of the <a>ActivityTask</a>.</p> <important> <p> <code>taskToken</code> is generated by the service and should be treated as an opaque value. If the task is passed to another process, its <code>taskToken</code> must also be passed. This enables it to provide its progress and respond with results.</p> </important>
            result: <p>The result of the activity task. It is a free form string that is implementation specific.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.respond_activity_task_completed_input.RespondActivityTaskCompletedInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.respond_activity_task_completed

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.respond_activity_task_completed.async_respond_activity_task_completed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.respond_activity_task_completed_input.RespondActivityTaskCompletedInput = {
            "task_token": task_token
        }
        if result is not None:
            input_["result"] = result

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def respond_activity_task_failed(
        self,
        task_token: "capo_swf.types.task_token.TaskToken",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        reason: Optional["capo_swf.types.failure_reason.FailureReason"] = None,
        details: Optional["capo_swf.types.data.Data"] = None,
    ) -> None:
        """<p>Used by workers to tell the service that the <a>ActivityTask</a> identified by the <code>taskToken</code> has failed with <code>reason</code> (if specified). The <code>reason</code> and <code>details</code> appear in the <code>ActivityTaskFailed</code> event added to the workflow history.</p> <p>A task is considered open from the time that it is scheduled until it is closed. Therefore a task is reported as open while a worker is processing it. A task is closed after it has been specified in a call to <a>RespondActivityTaskCompleted</a>, <a>RespondActivityTaskCanceled</a>, RespondActivityTaskFailed, or the task has <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dg-basic.html#swf-dev-timeout-types">timed out</a>.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            task_token: <p>The <code>taskToken</code> of the <a>ActivityTask</a>.</p> <important> <p> <code>taskToken</code> is generated by the service and should be treated as an opaque value. If the task is passed to another process, its <code>taskToken</code> must also be passed. This enables it to provide its progress and respond with results.</p> </important>
            reason: <p>Description of the error that may assist in diagnostics.</p>
            details: <p> Detailed information about the failure.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.respond_activity_task_failed_input.RespondActivityTaskFailedInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.respond_activity_task_failed

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.respond_activity_task_failed.async_respond_activity_task_failed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.respond_activity_task_failed_input.RespondActivityTaskFailedInput = {
            "task_token": task_token
        }
        if reason is not None:
            input_["reason"] = reason
        if details is not None:
            input_["details"] = details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def respond_decision_task_completed(
        self,
        task_token: "capo_swf.types.task_token.TaskToken",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        decisions: Optional["capo_swf.types.decision_list.DecisionList"] = None,
        execution_context: Optional["capo_swf.types.data.Data"] = None,
        task_list: Optional["capo_swf.types.task_list.TaskList"] = None,
        task_list_schedule_to_start_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
    ) -> None:
        """<p>Used by deciders to tell the service that the <a>DecisionTask</a> identified by the <code>taskToken</code> has successfully completed. The <code>decisions</code> argument specifies the list of decisions made while processing the task.</p> <p>A <code>DecisionTaskCompleted</code> event is added to the workflow history. The <code>executionContext</code> specified is attached to the event in the workflow execution history.</p> <p> <b>Access Control</b> </p> <p>If an IAM policy grants permission to use <code>RespondDecisionTaskCompleted</code>, it can express permissions for the list of decisions in the <code>decisions</code> parameter. Each of the decisions has one or more parameters, much like a regular API call. To allow for policies to be as readable as possible, you can express permissions on decisions as if they were actual API calls, including applying conditions to some parameters. For more information, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            task_token: <p>The <code>taskToken</code> from the <a>DecisionTask</a>.</p> <important> <p> <code>taskToken</code> is generated by the service and should be treated as an opaque value. If the task is passed to another process, its <code>taskToken</code> must also be passed. This enables it to provide its progress and respond with results.</p> </important>
            decisions: <p>The list of decisions (possibly empty) made by the decider while processing this decision task. See the docs for the <a>Decision</a> structure for details.</p>
            execution_context: <p>User defined context to add to workflow execution.</p>
            task_list: <p>The task list to use for the future decision tasks of this workflow execution. This list overrides the original task list you specified while starting the workflow execution. </p>
            task_list_schedule_to_start_timeout: <p>Specifies a timeout (in seconds) for the task list override. When this parameter is missing, the task list override is permanent. This parameter makes it possible to temporarily override the task list. If a decision task scheduled on the override task list is not started within the timeout, the decision task will time out. Amazon SWF will revert the override and schedule a new decision task to the original task list.</p> <p>If a decision task scheduled on the override task list is started within the timeout, but not completed within the start-to-close timeout, Amazon SWF will also revert the override and schedule a new decision task to the original task list.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.respond_decision_task_completed_input.RespondDecisionTaskCompletedInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.respond_decision_task_completed

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.respond_decision_task_completed.async_respond_decision_task_completed(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.respond_decision_task_completed_input.RespondDecisionTaskCompletedInput = {
            "task_token": task_token
        }
        if decisions is not None:
            input_["decisions"] = decisions
        if execution_context is not None:
            input_["execution_context"] = execution_context
        if task_list is not None:
            input_["task_list"] = task_list
        if task_list_schedule_to_start_timeout is not None:
            input_["task_list_schedule_to_start_timeout"] = (
                task_list_schedule_to_start_timeout
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def signal_workflow_execution(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_id: "capo_swf.types.workflow_id.WorkflowId",
        signal_name: "capo_swf.types.signal_name.SignalName",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        run_id: Optional[
            "capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
        ] = None,
        input: Optional["capo_swf.types.data.Data"] = None,
    ) -> None:
        """<p>Records a <code>WorkflowExecutionSignaled</code> event in the workflow execution history and creates a decision task for the workflow execution identified by the given domain, workflowId and runId. The event is recorded with the specified user defined signalName and input (if provided).</p> <note> <p>If a runId isn't specified, then the <code>WorkflowExecutionSignaled</code> event is recorded in the history of the current open workflow with the matching workflowId in the domain.</p> </note> <note> <p>If the specified workflow execution isn't open, this method fails with <code>UnknownResource</code>.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain containing the workflow execution to signal.</p>
            workflow_id: <p>The workflowId of the workflow execution to signal.</p>
            run_id: <p>The runId of the workflow execution to signal.</p>
            signal_name: <p>The name of the signal. This name must be meaningful to the target workflow.</p>
            input: <p>Data to attach to the <code>WorkflowExecutionSignaled</code> event in the target workflow execution's history.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.signal_workflow_execution_input.SignalWorkflowExecutionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.signal_workflow_execution

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.signal_workflow_execution.async_signal_workflow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.signal_workflow_execution_input.SignalWorkflowExecutionInput = {
            "domain": domain,
            "workflow_id": workflow_id,
            "signal_name": signal_name,
        }
        if run_id is not None:
            input_["run_id"] = run_id
        if input is not None:
            input_["input"] = input

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_workflow_execution(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_id: "capo_swf.types.workflow_id.WorkflowId",
        workflow_type: "capo_swf.types.workflow_type.WorkflowType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        task_list: Optional["capo_swf.types.task_list.TaskList"] = None,
        task_priority: Optional["capo_swf.types.task_priority.TaskPriority"] = None,
        input: Optional["capo_swf.types.data.Data"] = None,
        execution_start_to_close_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
        tag_list: Optional["capo_swf.types.tag_list.TagList"] = None,
        task_start_to_close_timeout: Optional[
            "capo_swf.types.duration_in_seconds_optional.DurationInSecondsOptional"
        ] = None,
        child_policy: Optional["capo_swf.types.child_policy.ChildPolicy"] = None,
        lambda_role: Optional["capo_swf.types.arn.Arn"] = None,
    ) -> "capo_swf.types.run.Run":
        r"""<p>Starts an execution of the workflow type in the specified domain using the provided <code>workflowId</code> and input data.</p> <p>This action returns the newly started workflow execution.</p> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>tagList.member.0</code>: The key is <code>swf:tagList.member.0</code>.</p> </li> <li> <p> <code>tagList.member.1</code>: The key is <code>swf:tagList.member.1</code>.</p> </li> <li> <p> <code>tagList.member.2</code>: The key is <code>swf:tagList.member.2</code>.</p> </li> <li> <p> <code>tagList.member.3</code>: The key is <code>swf:tagList.member.3</code>.</p> </li> <li> <p> <code>tagList.member.4</code>: The key is <code>swf:tagList.member.4</code>.</p> </li> <li> <p> <code>taskList</code>: String constraint. The key is <code>swf:taskList.name</code>.</p> </li> <li> <p> <code>workflowType.name</code>: String constraint. The key is <code>swf:workflowType.name</code>.</p> </li> <li> <p> <code>workflowType.version</code>: String constraint. The key is <code>swf:workflowType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain in which the workflow execution is created.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            workflow_id: <p>The user defined identifier associated with the workflow execution. You can use this to associate a custom identifier with the workflow execution. You may specify the same identifier if a workflow execution is logically a <i>restart</i> of a previous execution. You cannot have two open workflow executions with the same <code>workflowId</code> at the same time within the same domain.</p> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            workflow_type: <p>The type of the workflow to start.</p>
            task_list: <p>The task list to use for the decision tasks generated for this workflow execution. This overrides the <code>defaultTaskList</code> specified when registering the workflow type.</p> <note> <p>A task list for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task list was specified at registration time then a fault is returned.</p> </note> <p>The specified string must not contain a <code>:</code> (colon), <code>/</code> (slash), <code>|</code> (vertical bar), or any control characters (<code>\u0000-\u001f</code> | <code>\u007f-\u009f</code>). Also, it must <i>not</i> be the literal string <code>arn</code>.</p>
            task_priority: <p>The task priority to use for this workflow execution. This overrides any default priority that was assigned when the workflow type was registered. If not set, then the default task priority for the workflow type is used. Valid values are integers that range from Java's <code>Integer.MIN_VALUE</code> (-2147483648) to <code>Integer.MAX_VALUE</code> (2147483647). Higher numbers indicate higher priority.</p> <p>For more information about setting task priority, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/programming-priority.html">Setting Task Priority</a> in the <i>Amazon SWF Developer Guide</i>.</p>
            input: <p>The input for the workflow execution. This is a free form string which should be meaningful to the workflow you are starting. This <code>input</code> is made available to the new workflow execution in the <code>WorkflowExecutionStarted</code> history event.</p>
            execution_start_to_close_timeout: <p>The total duration for this workflow execution. This overrides the defaultExecutionStartToCloseTimeout specified when registering the workflow type.</p> <p>The duration is specified in seconds; an integer greater than or equal to <code>0</code>. Exceeding this limit causes the workflow execution to time out. Unlike some of the other timeout parameters in Amazon SWF, you cannot specify a value of "NONE" for this timeout; there is a one-year max limit on the time that a workflow execution can run.</p> <note> <p>An execution start-to-close timeout must be specified either through this parameter or as a default when the workflow type is registered. If neither this parameter nor a default execution start-to-close timeout is specified, a fault is returned.</p> </note>
            tag_list: <p>The list of tags to associate with the workflow execution. You can specify a maximum of 5 tags. You can list workflow executions with a specific tag by calling <a>ListOpenWorkflowExecutions</a> or <a>ListClosedWorkflowExecutions</a> and specifying a <a>TagFilter</a>.</p>
            task_start_to_close_timeout: <p>Specifies the maximum duration of decision tasks for this workflow execution. This parameter overrides the <code>defaultTaskStartToCloseTimout</code> specified when registering the workflow type using <a>RegisterWorkflowType</a>.</p> <p>The duration is specified in seconds, an integer greater than or equal to <code>0</code>. You can use <code>NONE</code> to specify unlimited duration.</p> <note> <p>A task start-to-close timeout for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default task start-to-close timeout was specified at registration time then a fault is returned.</p> </note>
            child_policy: <p>If set, specifies the policy to use for the child workflow executions of this workflow execution if it is terminated, by calling the <a>TerminateWorkflowExecution</a> action explicitly or due to an expired timeout. This policy overrides the default child policy specified when registering the workflow type using <a>RegisterWorkflowType</a>.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul> <note> <p>A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.</p> </note>
            lambda_role: <p>The IAM role to attach to this workflow execution.</p> <note> <p>Executions of this workflow type need IAM roles to invoke Lambda functions. If you don't attach an IAM role, any attempt to schedule a Lambda task fails. This results in a <code>ScheduleLambdaFunctionFailed</code> history event. For more information, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html">https://docs.aws.amazon.com/amazonswf/latest/developerguide/lambda-task.html</a> in the <i>Amazon SWF Developer Guide</i>.</p> </note>

        Raises:
            capo_swf.errors.default_undefined_fault.DefaultUndefinedFault: <p>The <code>StartWorkflowExecution</code> API action was called without the required parameters set.</p> <p>Some workflow execution parameters, such as the decision <code>taskList</code>, must be set to start the execution. However, these parameters might have been set as defaults when the workflow type was registered. In this case, you can omit these parameters from the <code>StartWorkflowExecution</code> call and Amazon SWF uses the values defined in the workflow type.</p> <note> <p>If these parameters aren't set and no default parameters were defined in the workflow type, this error is displayed.</p> </note>
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_deprecated_fault.TypeDeprecatedFault: <p>Returned when the specified activity or workflow type was already deprecated.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.workflow_execution_already_started_fault.WorkflowExecutionAlreadyStartedFault: <p>Returned by <a>StartWorkflowExecution</a> when an open execution with the same workflowId is already running in the specified domain.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.start_workflow_execution_input.StartWorkflowExecutionInput]",
        ) -> AsyncOperationResponse["capo_swf.types.run.Run"]:
            import capo_swf._operations.simple_workflow_service.start_workflow_execution

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.start_workflow_execution.async_start_workflow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.start_workflow_execution_input.StartWorkflowExecutionInput = {
            "domain": domain,
            "workflow_id": workflow_id,
            "workflow_type": workflow_type,
        }
        if task_list is not None:
            input_["task_list"] = task_list
        if task_priority is not None:
            input_["task_priority"] = task_priority
        if input is not None:
            input_["input"] = input
        if execution_start_to_close_timeout is not None:
            input_["execution_start_to_close_timeout"] = (
                execution_start_to_close_timeout
            )
        if tag_list is not None:
            input_["tag_list"] = tag_list
        if task_start_to_close_timeout is not None:
            input_["task_start_to_close_timeout"] = task_start_to_close_timeout
        if child_policy is not None:
            input_["child_policy"] = child_policy
        if lambda_role is not None:
            input_["lambda_role"] = lambda_role

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_swf.types.arn.Arn",
        tags: "capo_swf.types.resource_tag_list.ResourceTagList",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Add a tag to a Amazon SWF domain.</p> <note> <p>Amazon SWF supports a maximum of 50 tags per resource.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the Amazon SWF domain.</p>
            tags: <p>The list of tags to add to a domain. </p> <p>Tags may only contain unicode letters, digits, whitespace, or these symbols: <code>_ . : / = + - @</code>.</p>

        Raises:
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.too_many_tags_fault.TooManyTagsFault: <p>You've exceeded the number of tags allowed for a domain.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.tag_resource_input.TagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.tag_resource_input.TagResourceInput = {
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

    async def terminate_workflow_execution(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_id: "capo_swf.types.workflow_id.WorkflowId",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
        run_id: Optional[
            "capo_swf.types.workflow_run_id_optional.WorkflowRunIdOptional"
        ] = None,
        reason: Optional["capo_swf.types.terminate_reason.TerminateReason"] = None,
        details: Optional["capo_swf.types.data.Data"] = None,
        child_policy: Optional["capo_swf.types.child_policy.ChildPolicy"] = None,
    ) -> None:
        """<p>Records a <code>WorkflowExecutionTerminated</code> event and forces closure of the workflow execution identified by the given domain, runId, and workflowId. The child policy, registered with the workflow type or specified when starting this execution, is applied to any open child workflow executions of this workflow execution.</p> <important> <p>If the identified workflow execution was in progress, it is terminated immediately.</p> </important> <note> <p>If a runId isn't specified, then the <code>WorkflowExecutionTerminated</code> event is recorded in the history of the current open workflow with the matching workflowId in the domain.</p> </note> <note> <p>You should consider using <a>RequestCancelWorkflowExecution</a> action instead because it allows the workflow to gracefully close while <a>TerminateWorkflowExecution</a> doesn't.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The domain of the workflow execution to terminate.</p>
            workflow_id: <p>The workflowId of the workflow execution to terminate.</p>
            run_id: <p>The runId of the workflow execution to terminate.</p>
            reason: <p> A descriptive reason for terminating the workflow execution.</p>
            details: <p> Details for terminating the workflow execution.</p>
            child_policy: <p>If set, specifies the policy to use for the child workflow executions of the workflow execution being terminated. This policy overrides the child policy specified for the workflow execution at registration time or when starting the execution.</p> <p>The supported child policies are:</p> <ul> <li> <p> <code>TERMINATE</code> – The child executions are terminated.</p> </li> <li> <p> <code>REQUEST_CANCEL</code> – A request to cancel is attempted for each child execution by recording a <code>WorkflowExecutionCancelRequested</code> event in its history. It is up to the decider to take appropriate actions when it receives an execution history with this event.</p> </li> <li> <p> <code>ABANDON</code> – No action is taken. The child executions continue to run.</p> </li> </ul> <note> <p>A child policy for this workflow execution must be specified either as a default for the workflow type or through this parameter. If neither this parameter is set nor a default child policy was specified at registration time then a fault is returned.</p> </note>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.terminate_workflow_execution_input.TerminateWorkflowExecutionInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.terminate_workflow_execution

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.terminate_workflow_execution.async_terminate_workflow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.terminate_workflow_execution_input.TerminateWorkflowExecutionInput = {
            "domain": domain,
            "workflow_id": workflow_id,
        }
        if run_id is not None:
            input_["run_id"] = run_id
        if reason is not None:
            input_["reason"] = reason
        if details is not None:
            input_["details"] = details
        if child_policy is not None:
            input_["child_policy"] = child_policy

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def undeprecate_activity_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        activity_type: "capo_swf.types.activity_type.ActivityType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Undeprecates a previously deprecated <i>activity type</i>. After an activity type has been undeprecated, you can create new tasks of that activity type.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>activityType.name</code>: String constraint. The key is <code>swf:activityType.name</code>.</p> </li> <li> <p> <code>activityType.version</code>: String constraint. The key is <code>swf:activityType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain of the deprecated activity type.</p>
            activity_type: <p>The activity type to undeprecate.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_already_exists_fault.TypeAlreadyExistsFault: <p>Returned if the type already exists in the specified domain. You may get this fault if you are registering a type that is either already registered or deprecated, or if you undeprecate a type that is currently registered.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.undeprecate_activity_type_input.UndeprecateActivityTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.undeprecate_activity_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.undeprecate_activity_type.async_undeprecate_activity_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.undeprecate_activity_type_input.UndeprecateActivityTypeInput = {
            "domain": domain,
            "activity_type": activity_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def undeprecate_domain(
        self,
        name: "capo_swf.types.domain_name.DomainName",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Undeprecates a previously deprecated domain. After a domain has been undeprecated it can be used to create new workflow executions or register new types.</p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>You cannot use an IAM policy to constrain this action's parameters.</p> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            name: <p>The name of the domain of the deprecated workflow type.</p>

        Raises:
            capo_swf.errors.domain_already_exists_fault.DomainAlreadyExistsFault: <p>Returned if the domain already exists. You may get this fault if you are registering a domain that is either already registered or deprecated, or if you undeprecate a domain that is currently registered.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.undeprecate_domain_input.UndeprecateDomainInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.undeprecate_domain

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.undeprecate_domain.async_undeprecate_domain(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.undeprecate_domain_input.UndeprecateDomainInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def undeprecate_workflow_type(
        self,
        domain: "capo_swf.types.domain_name.DomainName",
        workflow_type: "capo_swf.types.workflow_type.WorkflowType",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Undeprecates a previously deprecated <i>workflow type</i>. After a workflow type has been undeprecated, you can create new executions of that type. </p> <note> <p>This operation is eventually consistent. The results are best effort and may not exactly reflect recent updates and changes.</p> </note> <p> <b>Access Control</b> </p> <p>You can use IAM policies to control this action's access to Amazon SWF resources as follows:</p> <ul> <li> <p>Use a <code>Resource</code> element with the domain name to limit the action to only specified domains.</p> </li> <li> <p>Use an <code>Action</code> element to allow or deny permission to call this action.</p> </li> <li> <p>Constrain the following parameters by using a <code>Condition</code> element with the appropriate keys.</p> <ul> <li> <p> <code>workflowType.name</code>: String constraint. The key is <code>swf:workflowType.name</code>.</p> </li> <li> <p> <code>workflowType.version</code>: String constraint. The key is <code>swf:workflowType.version</code>.</p> </li> </ul> </li> </ul> <p>If the caller doesn't have sufficient permissions to invoke the action, or the parameter values fall outside the specified constraints, the action fails. The associated event attribute's <code>cause</code> parameter is set to <code>OPERATION_NOT_PERMITTED</code>. For details and example IAM policies, see <a href="https://docs.aws.amazon.com/amazonswf/latest/developerguide/swf-dev-iam.html">Using IAM to Manage Access to Amazon SWF Workflows</a> in the <i>Amazon SWF Developer Guide</i>.</p>

        Args:
            domain: <p>The name of the domain of the deprecated workflow type.</p>
            workflow_type: <p>The name of the domain of the deprecated workflow type.</p>

        Raises:
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.type_already_exists_fault.TypeAlreadyExistsFault: <p>Returned if the type already exists in the specified domain. You may get this fault if you are registering a type that is either already registered or deprecated, or if you undeprecate a type that is currently registered.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.undeprecate_workflow_type_input.UndeprecateWorkflowTypeInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.undeprecate_workflow_type

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.undeprecate_workflow_type.async_undeprecate_workflow_type(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.undeprecate_workflow_type_input.UndeprecateWorkflowTypeInput = {
            "domain": domain,
            "workflow_type": workflow_type,
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
        resource_arn: "capo_swf.types.arn.Arn",
        tag_keys: "capo_swf.types.resource_tag_key_list.ResourceTagKeyList",
        *,
        config_overrides: Optional[AsyncSWFClientConfig] = None,
    ) -> None:
        """<p>Remove a tag from a Amazon SWF domain.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) for the Amazon SWF domain.</p>
            tag_keys: <p>The list of tags to remove from the Amazon SWF domain.</p>

        Raises:
            capo_swf.errors.limit_exceeded_fault.LimitExceededFault: <p>Returned by any operation if a system imposed limitation has been reached. To address this fault you should either clean up unused resources or increase the limit by contacting AWS.</p>
            capo_swf.errors.operation_not_permitted_fault.OperationNotPermittedFault: <p>Returned when the caller doesn't have sufficient permissions to invoke the action.</p>
            capo_swf.errors.unknown_resource_fault.UnknownResourceFault: <p>Returned when the named resource cannot be found with in the scope of this operation (region or domain). This could happen if the named resource was never created or is no longer available for this operation.</p>
            capo_swf.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_swf.types.untag_resource_input.UntagResourceInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_swf._operations.simple_workflow_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_swf._operations.simple_workflow_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_swf.types.untag_resource_input.UntagResourceInput = {
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
