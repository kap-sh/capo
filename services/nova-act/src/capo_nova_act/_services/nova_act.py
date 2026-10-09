"""Generated from Smithy shape ``com.amazonaws.novaact#AmazonNovaAgentsDataPlane``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_nova_act._auth._signers
import capo_nova_act._auth._sigv4
from capo_nova_act._auth._identity import Credentials
from capo_nova_act._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_nova_act._auth._zapros_handler import AuthMiddleware
from capo_nova_act._pagination import resolve_path as _resolve_path
from capo_nova_act._resources.amazon_nova_agents_data_plane.act_resource import (
    ActResource,
)
from capo_nova_act._resources.amazon_nova_agents_data_plane.model_resource import (
    ModelResource,
)
from capo_nova_act._resources.amazon_nova_agents_data_plane.service_linked_role_resource import (
    ServiceLinkedRoleResource,
)
from capo_nova_act._resources.amazon_nova_agents_data_plane.session_resource import (
    SessionResource,
)
from capo_nova_act._resources.amazon_nova_agents_data_plane.workflow_definition_resource import (
    WorkflowDefinitionResource,
)
from capo_nova_act._resources.amazon_nova_agents_data_plane.workflow_run_resource import (
    WorkflowRunResource,
)
from capo_nova_act._services._aws_config import aws_config
from capo_nova_act._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_nova_act.types.act_error
    import capo_nova_act.types.act_status
    import capo_nova_act.types.act_summary
    import capo_nova_act.types.call_results
    import capo_nova_act.types.client_info
    import capo_nova_act.types.client_token
    import capo_nova_act.types.cloud_watch_log_group_name
    import capo_nova_act.types.create_act_request
    import capo_nova_act.types.create_act_response
    import capo_nova_act.types.create_session_request
    import capo_nova_act.types.create_session_response
    import capo_nova_act.types.create_workflow_definition_request
    import capo_nova_act.types.create_workflow_definition_response
    import capo_nova_act.types.create_workflow_run_request
    import capo_nova_act.types.create_workflow_run_response
    import capo_nova_act.types.delete_workflow_definition_request
    import capo_nova_act.types.delete_workflow_definition_response
    import capo_nova_act.types.delete_workflow_run_request
    import capo_nova_act.types.delete_workflow_run_response
    import capo_nova_act.types.get_workflow_definition_request
    import capo_nova_act.types.get_workflow_definition_response
    import capo_nova_act.types.get_workflow_run_request
    import capo_nova_act.types.get_workflow_run_response
    import capo_nova_act.types.invoke_act_step_request
    import capo_nova_act.types.invoke_act_step_response
    import capo_nova_act.types.list_acts_request
    import capo_nova_act.types.list_acts_response
    import capo_nova_act.types.list_models_request
    import capo_nova_act.types.list_models_response
    import capo_nova_act.types.list_sessions_request
    import capo_nova_act.types.list_sessions_response
    import capo_nova_act.types.list_workflow_definitions_request
    import capo_nova_act.types.list_workflow_definitions_response
    import capo_nova_act.types.list_workflow_runs_request
    import capo_nova_act.types.list_workflow_runs_response
    import capo_nova_act.types.max_results
    import capo_nova_act.types.model_id
    import capo_nova_act.types.next_token
    import capo_nova_act.types.session_summary
    import capo_nova_act.types.sort_order
    import capo_nova_act.types.task
    import capo_nova_act.types.tool_specs
    import capo_nova_act.types.update_act_request
    import capo_nova_act.types.update_act_response
    import capo_nova_act.types.update_workflow_run_request
    import capo_nova_act.types.update_workflow_run_response
    import capo_nova_act.types.uuid_string
    import capo_nova_act.types.workflow_definition_name
    import capo_nova_act.types.workflow_definition_summary
    import capo_nova_act.types.workflow_description
    import capo_nova_act.types.workflow_export_config
    import capo_nova_act.types.workflow_run_status
    import capo_nova_act.types.workflow_run_summary


class NovaActClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class NovaActClient:
    """A client for the ``NovaAct`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
        anonymous: bool | None = None,
    ):
        self._client = Client(http_handler).wrap_with_middleware(
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
                Client(http_handler)
            )
        self._config = NovaActClientConfig(
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

        # resources
        self.act_resource = ActResource(self)
        self.model_resource = ModelResource(self)
        self.service_linked_role_resource = ServiceLinkedRoleResource(self)
        self.session_resource = SessionResource(self)
        self.workflow_definition_resource = WorkflowDefinitionResource(self)
        self.workflow_run_resource = WorkflowRunResource(self)

    def operation_options(
        self, config_overrides: Optional[NovaActClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: NovaActClientConfig = config_overrides or {}
        interceptors_: list[Interceptor[Any, Any]] = [
            *overrides.get(
                "operation_interceptors", self._config.get("operation_interceptors", [])
            ),
            aws_config(),
            retry(),
        ]
        options_: OperationOptions = OperationOptions(
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

    def create_act(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        task: "capo_nova_act.types.task.Task",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        tool_specs: Optional["capo_nova_act.types.tool_specs.ToolSpecs"] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_act_response.CreateActResponse":
        """<p>Creates a new AI task (act) within a session that can interact with tools and perform specific actions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to create the act in.</p>
            task: <p>The task description that defines what the act should accomplish.</p>
            tool_specs: <p>A list of tool specifications that the act can invoke to complete its task.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.create_act_request.CreateActRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_act_response.CreateActResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_act

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_act.create_act(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.create_act_request.CreateActRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "task": task,
        }
        if tool_specs is not None:
            input_["tool_specs"] = tool_specs
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_acts(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        workflow_run_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        session_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_acts_response.ListActsResponse":
        """<p>Lists all acts within a specific session with their current status and execution details.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the session.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the session.</p>
            session_id: <p>The unique identifier of the session to list acts for.</p>
            max_results: <p>The maximum number of acts to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned acts (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_acts_request.ListActsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_acts_response.ListActsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_acts

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_acts.list_acts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.list_acts_request.ListActsRequest = {
            "workflow_definition_name": workflow_definition_name
        }
        if workflow_run_id is not None:
            input_["workflow_run_id"] = workflow_run_id
        if session_id is not None:
            input_["session_id"] = session_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_acts(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        workflow_run_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        session_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "Iterator[capo_nova_act.types.act_summary.ActSummary]":
        _token = next_token
        while True:
            _response = self.list_acts(
                workflow_definition_name,
                config_overrides=config_overrides,
                workflow_run_id=workflow_run_id,
                session_id=session_id,
                max_results=max_results,
                next_token=_token,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("act_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def invoke_act_step(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        act_id: "capo_nova_act.types.uuid_string.UuidString",
        call_results: "capo_nova_act.types.call_results.CallResults",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        previous_step_id: Optional["capo_nova_act.types.uuid_string.UuidString"] = None,
    ) -> "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse":
        """<p>Executes the next step of an act, processing tool call results and returning new tool calls if needed.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to invoke the next step for.</p>
            call_results: <p>The results from previous tool calls that the act requested.</p>
            previous_step_id: <p>The identifier of the previous step, used for tracking execution flow.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.invoke_act_step_response.InvokeActStepResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.invoke_act_step.invoke_act_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.invoke_act_step_request.InvokeActStepRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "act_id": act_id,
            "call_results": call_results,
        }
        if previous_step_id is not None:
            input_["previous_step_id"] = previous_step_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_act(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        session_id: "capo_nova_act.types.uuid_string.UuidString",
        act_id: "capo_nova_act.types.uuid_string.UuidString",
        status: "capo_nova_act.types.act_status.ActStatus",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        error: Optional["capo_nova_act.types.act_error.ActError"] = None,
    ) -> "capo_nova_act.types.update_act_response.UpdateActResponse":
        """<p>Updates an existing act's configuration, status, or error information.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the act.</p>
            workflow_run_id: <p>The unique identifier of the workflow run containing the act.</p>
            session_id: <p>The unique identifier of the session containing the act.</p>
            act_id: <p>The unique identifier of the act to update.</p>
            status: <p>The new status to set for the act.</p>
            error: <p>Error information to associate with the act, if applicable.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.update_act_request.UpdateActRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.update_act_response.UpdateActResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.update_act

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.update_act.update_act(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.update_act_request.UpdateActRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "session_id": session_id,
            "act_id": act_id,
            "status": status,
        }
        if error is not None:
            input_["error"] = error

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_models(
        self,
        client_compatibility_version: int,
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.list_models_response.ListModelsResponse":
        """<p>Lists all available AI models that can be used for workflow execution, including their status and compatibility information.</p>

        Args:
            client_compatibility_version: <p>The client compatibility version to filter models by compatibility.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_models_request.ListModelsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_models_response.ListModelsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_models

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_models.list_models(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.list_models_request.ListModelsRequest = {
            "client_compatibility_version": client_compatibility_version
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_session(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_session_response.CreateSessionResponse":
        """<p>Creates a new session context within a workflow run to manage conversation state and acts.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to create the session in.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.create_session_request.CreateSessionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_session

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_session.create_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.create_session_request.CreateSessionRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_sessions(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions within a specific workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to list sessions for.</p>
            max_results: <p>The maximum number of sessions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned sessions (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_sessions

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.list_sessions_request.ListSessionsRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_sessions(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "Iterator[capo_nova_act.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = self.list_sessions(
                workflow_definition_name,
                workflow_run_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("session_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_workflow_definition(
        self,
        name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        description: Optional[
            "capo_nova_act.types.workflow_description.WorkflowDescription"
        ] = None,
        export_config: Optional[
            "capo_nova_act.types.workflow_export_config.WorkflowExportConfig"
        ] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
    ) -> "capo_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse":
        """<p>Creates a new workflow definition template that can be used to execute multiple workflow runs.</p>

        Args:
            name: <p>The name of the workflow definition. Must be unique within your account and region.</p>
            description: <p>An optional description of the workflow definition's purpose and functionality.</p>
            export_config: <p>Configuration for exporting workflow execution data to Amazon Simple Storage Service.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed a service quota limit.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_workflow_definition_response.CreateWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_definition.create_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.create_workflow_definition_request.CreateWorkflowDefinitionRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if export_config is not None:
            input_["export_config"] = export_config
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workflow_definition(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse":
        """<p>Retrieves the details and configuration of a specific workflow definition.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to retrieve.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.get_workflow_definition_response.GetWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_definition.get_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.get_workflow_definition_request.GetWorkflowDefinitionRequest = {
            "workflow_definition_name": workflow_definition_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workflow_definition(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse":
        """<p>Deletes a workflow definition and all associated resources. This operation cannot be undone.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to delete.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.delete_workflow_definition_response.DeleteWorkflowDefinitionResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_definition.delete_workflow_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.delete_workflow_definition_request.DeleteWorkflowDefinitionRequest = {
            "workflow_definition_name": workflow_definition_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workflow_definitions(
        self,
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse":
        """<p>Lists all workflow definitions in your account with optional filtering and pagination.</p>

        Args:
            max_results: <p>The maximum number of workflow definitions to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow definitions (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_workflow_definitions_response.ListWorkflowDefinitionsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_definitions.list_workflow_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.list_workflow_definitions_request.ListWorkflowDefinitionsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workflow_definitions(
        self,
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "Iterator[capo_nova_act.types.workflow_definition_summary.WorkflowDefinitionSummary]":
        _token = next_token
        while True:
            _response = self.list_workflow_definitions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("workflow_definition_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_workflow_run(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        model_id: "capo_nova_act.types.model_id.ModelId",
        client_info: "capo_nova_act.types.client_info.ClientInfo",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        client_token: Optional["capo_nova_act.types.client_token.ClientToken"] = None,
        log_group_name: Optional[
            "capo_nova_act.types.cloud_watch_log_group_name.CloudWatchLogGroupName"
        ] = None,
    ) -> "capo_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse":
        """<p>Creates a new execution instance of a workflow definition with specified parameters.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to execute.</p>
            model_id: <p>The ID of the AI model to use for workflow execution.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            log_group_name: <p>The CloudWatch log group name for storing workflow execution logs.</p>
            client_info: <p>Information about the client making the request, including compatibility version and SDK version.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.create_workflow_run_response.CreateWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.create_workflow_run.create_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.create_workflow_run_request.CreateWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "model_id": model_id,
            "client_info": client_info,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workflow_run(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse":
        """<p>Retrieves the current state, configuration, and execution details of a workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to retrieve.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.get_workflow_run_response.GetWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.get_workflow_run.get_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.get_workflow_run_request.GetWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workflow_run(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        status: "capo_nova_act.types.workflow_run_status.WorkflowRunStatus",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse":
        """<p>Updates the configuration or state of an active workflow run.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to update.</p>
            status: <p>The new status to set for the workflow run.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.update_workflow_run_response.UpdateWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.update_workflow_run.update_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.update_workflow_run_request.UpdateWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workflow_run(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        workflow_run_id: "capo_nova_act.types.uuid_string.UuidString",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
    ) -> "capo_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse":
        """<p>Terminates and cleans up a workflow run, stopping all associated acts and sessions.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition containing the workflow run.</p>
            workflow_run_id: <p>The unique identifier of the workflow run to delete.</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.delete_workflow_run_response.DeleteWorkflowRunResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.delete_workflow_run.delete_workflow_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.delete_workflow_run_request.DeleteWorkflowRunRequest = {
            "workflow_definition_name": workflow_definition_name,
            "workflow_run_id": workflow_run_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workflow_runs(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "capo_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse":
        """<p>Lists all workflow runs for a specific workflow definition with optional filtering and pagination.</p>

        Args:
            workflow_definition_name: <p>The name of the workflow definition to list workflow runs for.</p>
            max_results: <p>The maximum number of workflow runs to return in a single response.</p>
            next_token: <p>The token for retrieving the next page of results.</p>
            sort_order: <p>The sort order for the returned workflow runs (ascending or descending).</p>

        Raises:
            capo_nova_act.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_nova_act.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the resource.</p>
            capo_nova_act.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Please try again later.</p>
            capo_nova_act.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource was not found.</p>
            capo_nova_act.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please try again later.</p>
            capo_nova_act.errors.validation_exception.ValidationException: <p>The input parameters for the request are invalid.</p>
            capo_nova_act.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest]",
        ) -> OperationResponse[
            "capo_nova_act.types.list_workflow_runs_response.ListWorkflowRunsResponse"
        ]:
            import capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs

            output, http_response = (
                capo_nova_act._operations.amazon_nova_agents_data_plane.list_workflow_runs.list_workflow_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_nova_act.types.list_workflow_runs_request.ListWorkflowRunsRequest = {
            "workflow_definition_name": workflow_definition_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_workflow_runs(
        self,
        workflow_definition_name: "capo_nova_act.types.workflow_definition_name.WorkflowDefinitionName",
        *,
        config_overrides: Optional[NovaActClientConfig] = None,
        max_results: Optional["capo_nova_act.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_nova_act.types.next_token.NextToken"] = None,
        sort_order: Optional["capo_nova_act.types.sort_order.SortOrder"] = None,
    ) -> "Iterator[capo_nova_act.types.workflow_run_summary.WorkflowRunSummary]":
        _token = next_token
        while True:
            _response = self.list_workflow_runs(
                workflow_definition_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("workflow_run_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
