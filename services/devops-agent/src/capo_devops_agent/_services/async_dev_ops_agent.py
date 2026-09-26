"""Generated from Smithy shape ``com.amazonaws.devopsagent#DevOpsAgent``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_devops_agent._auth._signers
import capo_devops_agent._auth._sigv4
from capo_devops_agent._auth._identity import Credentials
from capo_devops_agent._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_devops_agent._auth._zapros_handler import AuthMiddleware
from capo_devops_agent._pagination import resolve_path as _resolve_path
from capo_devops_agent._resources.dev_ops_agent.agent_space_resource import (
    AsyncAgentSpaceResource,
)
from capo_devops_agent._resources.dev_ops_agent.private_connection_resource import (
    AsyncPrivateConnectionResource,
)
from capo_devops_agent._resources.dev_ops_agent.service_resource import (
    AsyncServiceResource,
)
from capo_devops_agent._services._aws_config import aaws_config
from capo_devops_agent._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_devops_agent.types.agent_space
    import capo_devops_agent.types.agent_space_id
    import capo_devops_agent.types.agent_space_name
    import capo_devops_agent.types.asset
    import capo_devops_agent.types.asset_content
    import capo_devops_agent.types.asset_file_body
    import capo_devops_agent.types.asset_file_path
    import capo_devops_agent.types.asset_file_summary
    import capo_devops_agent.types.asset_id_list
    import capo_devops_agent.types.asset_type
    import capo_devops_agent.types.asset_type_summary
    import capo_devops_agent.types.asset_version_metadata
    import capo_devops_agent.types.associate_service_input
    import capo_devops_agent.types.associate_service_output
    import capo_devops_agent.types.association
    import capo_devops_agent.types.association_id
    import capo_devops_agent.types.auth_flow
    import capo_devops_agent.types.backlog_task_description
    import capo_devops_agent.types.backlog_task_title
    import capo_devops_agent.types.certificate_string
    import capo_devops_agent.types.chat_execution_id
    import capo_devops_agent.types.create_agent_space_input
    import capo_devops_agent.types.create_agent_space_output
    import capo_devops_agent.types.create_asset_file_request
    import capo_devops_agent.types.create_asset_file_response
    import capo_devops_agent.types.create_asset_request
    import capo_devops_agent.types.create_asset_response
    import capo_devops_agent.types.create_backlog_task_request
    import capo_devops_agent.types.create_backlog_task_response
    import capo_devops_agent.types.create_chat_request
    import capo_devops_agent.types.create_chat_response
    import capo_devops_agent.types.create_private_connection_input
    import capo_devops_agent.types.create_private_connection_output
    import capo_devops_agent.types.delete_agent_space_input
    import capo_devops_agent.types.delete_agent_space_output
    import capo_devops_agent.types.delete_asset_file_request
    import capo_devops_agent.types.delete_asset_file_response
    import capo_devops_agent.types.delete_asset_request
    import capo_devops_agent.types.delete_asset_response
    import capo_devops_agent.types.delete_private_connection_input
    import capo_devops_agent.types.delete_private_connection_output
    import capo_devops_agent.types.deregister_service_input
    import capo_devops_agent.types.deregister_service_output
    import capo_devops_agent.types.describe_private_connection_input
    import capo_devops_agent.types.describe_private_connection_output
    import capo_devops_agent.types.description
    import capo_devops_agent.types.disable_operator_app_input
    import capo_devops_agent.types.disassociate_service_input
    import capo_devops_agent.types.disassociate_service_output
    import capo_devops_agent.types.enable_operator_app_input
    import capo_devops_agent.types.enable_operator_app_output
    import capo_devops_agent.types.execution
    import capo_devops_agent.types.get_account_usage_input
    import capo_devops_agent.types.get_account_usage_output
    import capo_devops_agent.types.get_agent_space_input
    import capo_devops_agent.types.get_agent_space_output
    import capo_devops_agent.types.get_asset_content_request
    import capo_devops_agent.types.get_asset_content_response
    import capo_devops_agent.types.get_asset_file_request
    import capo_devops_agent.types.get_asset_file_response
    import capo_devops_agent.types.get_asset_request
    import capo_devops_agent.types.get_asset_response
    import capo_devops_agent.types.get_association_input
    import capo_devops_agent.types.get_association_output
    import capo_devops_agent.types.get_backlog_task_request
    import capo_devops_agent.types.get_backlog_task_response
    import capo_devops_agent.types.get_operator_app_input
    import capo_devops_agent.types.get_operator_app_output
    import capo_devops_agent.types.get_recommendation_request
    import capo_devops_agent.types.get_recommendation_response
    import capo_devops_agent.types.get_service_input
    import capo_devops_agent.types.get_service_output
    import capo_devops_agent.types.goal
    import capo_devops_agent.types.goal_schedule_input
    import capo_devops_agent.types.goal_status
    import capo_devops_agent.types.goal_type
    import capo_devops_agent.types.idp_client_id
    import capo_devops_agent.types.idp_client_secret
    import capo_devops_agent.types.journal_record
    import capo_devops_agent.types.kms_key_arn
    import capo_devops_agent.types.list_agent_spaces_input
    import capo_devops_agent.types.list_agent_spaces_output
    import capo_devops_agent.types.list_asset_files_request
    import capo_devops_agent.types.list_asset_files_response
    import capo_devops_agent.types.list_asset_types_request
    import capo_devops_agent.types.list_asset_types_response
    import capo_devops_agent.types.list_asset_versions_request
    import capo_devops_agent.types.list_asset_versions_response
    import capo_devops_agent.types.list_assets_request
    import capo_devops_agent.types.list_assets_response
    import capo_devops_agent.types.list_associations_input
    import capo_devops_agent.types.list_associations_output
    import capo_devops_agent.types.list_backlog_tasks_request
    import capo_devops_agent.types.list_backlog_tasks_response
    import capo_devops_agent.types.list_chats_request
    import capo_devops_agent.types.list_chats_response
    import capo_devops_agent.types.list_executions_request
    import capo_devops_agent.types.list_executions_response
    import capo_devops_agent.types.list_goals_request
    import capo_devops_agent.types.list_goals_response
    import capo_devops_agent.types.list_journal_records_request
    import capo_devops_agent.types.list_journal_records_response
    import capo_devops_agent.types.list_pending_messages_request
    import capo_devops_agent.types.list_pending_messages_response
    import capo_devops_agent.types.list_private_connections_input
    import capo_devops_agent.types.list_private_connections_output
    import capo_devops_agent.types.list_recommendations_request
    import capo_devops_agent.types.list_recommendations_response
    import capo_devops_agent.types.list_services_input
    import capo_devops_agent.types.list_services_output
    import capo_devops_agent.types.list_tags_for_resource_request
    import capo_devops_agent.types.list_tags_for_resource_response
    import capo_devops_agent.types.list_webhooks_input
    import capo_devops_agent.types.list_webhooks_output
    import capo_devops_agent.types.locale
    import capo_devops_agent.types.message_content
    import capo_devops_agent.types.next_token
    import capo_devops_agent.types.order_type
    import capo_devops_agent.types.post_register_service_supported_service
    import capo_devops_agent.types.priority
    import capo_devops_agent.types.private_connection_mode
    import capo_devops_agent.types.private_connection_name
    import capo_devops_agent.types.recommendation_priority
    import capo_devops_agent.types.recommendation_status
    import capo_devops_agent.types.reference_input
    import capo_devops_agent.types.register_service_input
    import capo_devops_agent.types.register_service_output
    import capo_devops_agent.types.registered_service
    import capo_devops_agent.types.resource_id
    import capo_devops_agent.types.role_arn
    import capo_devops_agent.types.send_message_context
    import capo_devops_agent.types.send_message_request
    import capo_devops_agent.types.send_message_response
    import capo_devops_agent.types.service
    import capo_devops_agent.types.service_configuration
    import capo_devops_agent.types.service_details
    import capo_devops_agent.types.service_id
    import capo_devops_agent.types.service_name
    import capo_devops_agent.types.tag_key_list
    import capo_devops_agent.types.tag_resource_request
    import capo_devops_agent.types.tag_resource_response
    import capo_devops_agent.types.tags
    import capo_devops_agent.types.task
    import capo_devops_agent.types.task_filter
    import capo_devops_agent.types.task_sort_field
    import capo_devops_agent.types.task_sort_order
    import capo_devops_agent.types.task_status
    import capo_devops_agent.types.task_type
    import capo_devops_agent.types.untag_resource_request
    import capo_devops_agent.types.untag_resource_response
    import capo_devops_agent.types.update_agent_space_input
    import capo_devops_agent.types.update_agent_space_output
    import capo_devops_agent.types.update_asset_file_request
    import capo_devops_agent.types.update_asset_file_response
    import capo_devops_agent.types.update_asset_request
    import capo_devops_agent.types.update_asset_response
    import capo_devops_agent.types.update_association_input
    import capo_devops_agent.types.update_association_output
    import capo_devops_agent.types.update_backlog_task_request
    import capo_devops_agent.types.update_backlog_task_response
    import capo_devops_agent.types.update_goal_request
    import capo_devops_agent.types.update_goal_response
    import capo_devops_agent.types.update_operator_app_idp_config_input
    import capo_devops_agent.types.update_operator_app_idp_config_output
    import capo_devops_agent.types.update_private_connection_certificate_input
    import capo_devops_agent.types.update_private_connection_certificate_output
    import capo_devops_agent.types.update_recommendation_request
    import capo_devops_agent.types.update_recommendation_response
    import capo_devops_agent.types.user_type
    import capo_devops_agent.types.validate_aws_associations_input
    import capo_devops_agent.types.validate_aws_associations_output


class AsyncDevOpsAgentClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncDevOpsAgentClient:
    """A client for the ``DevOpsAgent`` service.

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
        self._config = AsyncDevOpsAgentClientConfig(
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
        self.agent_space_resource = AsyncAgentSpaceResource(self)
        self.private_connection_resource = AsyncPrivateConnectionResource(self)
        self.service_resource = AsyncServiceResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDevOpsAgentClientConfig = config_overrides or {}
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

    async def create_asset(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_type: "capo_devops_agent.types.asset_type.AssetType",
        content: "capo_devops_agent.types.asset_content.AssetContent",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        metadata: Optional[object] = None,
        client_token: Optional[str] = None,
    ) -> "capo_devops_agent.types.create_asset_response.CreateAssetResponse":
        """<p>Creates a new asset in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space where the asset will be created</p>
            asset_type: <p>The type of asset to create</p>
            metadata: <p>The metadata describing this asset</p>
            content: <p>The content for the asset. Provide a single file or a zip bundle.</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset creation</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_asset_request.CreateAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_asset_response.CreateAssetResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_asset

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_asset.async_create_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.create_asset_request.CreateAssetRequest = {
            "agent_space_id": agent_space_id,
            "asset_type": asset_type,
            "content": content,
        }
        if metadata is not None:
            input_["metadata"] = metadata
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

    async def create_asset_file(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        path: "capo_devops_agent.types.asset_file_path.AssetFilePath",
        content: "capo_devops_agent.types.asset_file_body.AssetFileBody",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        metadata: Optional[object] = None,
        client_token: Optional[str] = None,
    ) -> "capo_devops_agent.types.create_asset_file_response.CreateAssetFileResponse":
        """<p>Creates a file in an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to create the file in</p>
            path: <p>The path of the file within the asset</p>
            content: <p>The content of the file to create</p>
            metadata: <p>Optional metadata describing this file</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset file creation</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_asset_file_request.CreateAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_asset_file_response.CreateAssetFileResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_asset_file

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_asset_file.async_create_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.create_asset_file_request.CreateAssetFileRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
            "path": path,
            "content": content,
        }
        if metadata is not None:
            input_["metadata"] = metadata
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

    async def create_backlog_task(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        task_type: "capo_devops_agent.types.task_type.TaskType",
        title: "capo_devops_agent.types.backlog_task_title.BacklogTaskTitle",
        priority: "capo_devops_agent.types.priority.Priority",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        reference: Optional[
            "capo_devops_agent.types.reference_input.ReferenceInput"
        ] = None,
        description: Optional[
            "capo_devops_agent.types.backlog_task_description.BacklogTaskDescription"
        ] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_devops_agent.types.create_backlog_task_response.CreateBacklogTaskResponse"
    ):
        """<p>Creates a new backlog task in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space where the task will be created</p>
            reference: <p>Optional reference information for the task</p>
            task_type: <p>The type of task being created</p>
            title: <p>The title of the backlog task</p>
            description: <p>Optional detailed description of the task</p>
            priority: <p>The priority level of the task</p>
            client_token: <p>Client-provided token for idempotent operations</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_backlog_task_request.CreateBacklogTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_backlog_task_response.CreateBacklogTaskResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_backlog_task

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_backlog_task.async_create_backlog_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.create_backlog_task_request.CreateBacklogTaskRequest = {
            "agent_space_id": agent_space_id,
            "task_type": task_type,
            "title": title,
            "priority": priority,
        }
        if reference is not None:
            input_["reference"] = reference
        if description is not None:
            input_["description"] = description
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

    async def create_chat(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        user_id: Optional["capo_devops_agent.types.resource_id.ResourceId"] = None,
        user_type: Optional["capo_devops_agent.types.user_type.UserType"] = None,
    ) -> "capo_devops_agent.types.create_chat_response.CreateChatResponse":
        """<p>Creates a new chat execution in the specified agent space</p>

        Args:
            user_id: <p>The user identifier for the chat. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>
            user_type: <p>The authentication type of the user</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_chat_request.CreateChatRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_chat_response.CreateChatResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_chat

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_chat.async_create_chat(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.create_chat_request.CreateChatRequest = {
            "agent_space_id": agent_space_id
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if user_type is not None:
            input_["user_type"] = user_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_asset_response.DeleteAssetResponse":
        """<p>Deletes an asset and all its files from the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to delete</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.delete_asset_request.DeleteAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.delete_asset_response.DeleteAssetResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_asset

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.delete_asset_request.DeleteAssetRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset_file(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        path: "capo_devops_agent.types.asset_file_path.AssetFilePath",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_asset_file_response.DeleteAssetFileResponse":
        """<p>Deletes a file from an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset containing the file</p>
            path: <p>The path of the file within the asset to delete</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.delete_asset_file_request.DeleteAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.delete_asset_file_response.DeleteAssetFileResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_asset_file

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.delete_asset_file.async_delete_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.delete_asset_file_request.DeleteAssetFileRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
            "path": path,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_account_usage(
        self, *, config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None
    ) -> "capo_devops_agent.types.get_account_usage_output.GetAccountUsageOutput":
        """<p>Retrieves monthly account usage metrics and limits for the AWS account.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_account_usage_input.GetAccountUsageInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_account_usage_output.GetAccountUsageOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_account_usage

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_account_usage.async_get_account_usage(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_account_usage_input.GetAccountUsageInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
    ) -> "capo_devops_agent.types.get_asset_response.GetAssetResponse":
        """<p>Gets an asset from the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to retrieve</p>
            asset_version: <p>The specific version of the asset to retrieve. If omitted, the latest version is returned.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_asset_request.GetAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_asset_response.GetAssetResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_asset

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_asset.async_get_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_asset_request.GetAssetRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
        }
        if asset_version is not None:
            input_["asset_version"] = asset_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset_content(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
    ) -> "capo_devops_agent.types.get_asset_content_response.GetAssetContentResponse":
        """<p>Gets an asset's content as a zip bundle</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset</p>
            asset_version: <p>The specific asset version to export. If omitted, the latest version is returned.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_asset_content_request.GetAssetContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_asset_content_response.GetAssetContentResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_asset_content

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_asset_content.async_get_asset_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_asset_content_request.GetAssetContentRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
        }
        if asset_version is not None:
            input_["asset_version"] = asset_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset_file(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        path: "capo_devops_agent.types.asset_file_path.AssetFilePath",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
    ) -> "capo_devops_agent.types.get_asset_file_response.GetAssetFileResponse":
        """<p>Gets a file from an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset containing the file</p>
            path: <p>The path of the file within the asset to retrieve</p>
            asset_version: <p>The specific asset version to retrieve the file from. If omitted, the latest version is returned.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_asset_file_request.GetAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_asset_file_response.GetAssetFileResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_asset_file

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_asset_file.async_get_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_asset_file_request.GetAssetFileRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
            "path": path,
        }
        if asset_version is not None:
            input_["asset_version"] = asset_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_backlog_task(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_backlog_task_response.GetBacklogTaskResponse":
        """<p>Gets a backlog task for the specified agent space and task id</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the task</p>
            task_id: <p>The unique identifier of the task to retrieve</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_backlog_task_request.GetBacklogTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_backlog_task_response.GetBacklogTaskResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_backlog_task

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_backlog_task.async_get_backlog_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_backlog_task_request.GetBacklogTaskRequest = {
            "agent_space_id": agent_space_id,
            "task_id": task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_recommendation(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        recommendation_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        recommendation_version: Optional[int] = None,
    ) -> (
        "capo_devops_agent.types.get_recommendation_response.GetRecommendationResponse"
    ):
        """<p>Retrieves a specific recommendation by its ID</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the recommendation</p>
            recommendation_id: <p>The unique identifier for the recommendation to retrieve</p>
            recommendation_version: <p>Specific version of the recommendation to retrieve. If not specified, returns the latest version.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_recommendation

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_recommendation.async_get_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_recommendation_request.GetRecommendationRequest = {
            "agent_space_id": agent_space_id,
            "recommendation_id": recommendation_id,
        }
        if recommendation_version is not None:
            input_["recommendation_version"] = recommendation_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_asset_files(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_devops_agent.types.list_asset_files_response.ListAssetFilesResponse":
        """<p>Lists files in an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset whose files to list</p>
            asset_version: <p>The specific asset version to list files from. If omitted, files from the latest version are returned.</p>
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>
            max_results: <p>The maximum number of results to return in a single response</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_asset_files_request.ListAssetFilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_asset_files_response.ListAssetFilesResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_asset_files

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_asset_files.async_list_asset_files(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_asset_files_request.ListAssetFilesRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
        }
        if asset_version is not None:
            input_["asset_version"] = asset_version
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

    async def iter_list_asset_files(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_version: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.asset_file_summary.AssetFileSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_files(
                agent_space_id,
                asset_id,
                config_overrides=config_overrides,
                asset_version=asset_version,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_assets(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_type: Optional["capo_devops_agent.types.asset_type.AssetType"] = None,
        updated_after: Optional[datetime.datetime] = None,
        updated_before: Optional[datetime.datetime] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_devops_agent.types.list_assets_response.ListAssetsResponse":
        """<p>Lists assets in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space to list assets from</p>
            asset_type: <p>Filter results to only assets of this type</p>
            updated_after: <p>Filter results to only assets updated after this timestamp</p>
            updated_before: <p>Filter results to only assets updated before this timestamp</p>
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>
            max_results: <p>The maximum number of results to return in a single response</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_assets_request.ListAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_assets_response.ListAssetsResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_assets

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_assets.async_list_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_assets_request.ListAssetsRequest = {
            "agent_space_id": agent_space_id
        }
        if asset_type is not None:
            input_["asset_type"] = asset_type
        if updated_after is not None:
            input_["updated_after"] = updated_after
        if updated_before is not None:
            input_["updated_before"] = updated_before
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

    async def iter_list_assets(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        asset_type: Optional["capo_devops_agent.types.asset_type.AssetType"] = None,
        updated_after: Optional[datetime.datetime] = None,
        updated_before: Optional[datetime.datetime] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.asset.Asset]":
        _token = next_token
        while True:
            _response = await self.list_assets(
                agent_space_id,
                config_overrides=config_overrides,
                asset_type=asset_type,
                updated_after=updated_after,
                updated_before=updated_before,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_types(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "capo_devops_agent.types.list_asset_types_response.ListAssetTypesResponse":
        """<p>Lists the supported asset types</p>

        Args:
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>
            max_results: <p>The maximum number of results to return in a single response</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_asset_types_request.ListAssetTypesRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_asset_types_response.ListAssetTypesResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_asset_types

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_asset_types.async_list_asset_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_asset_types_request.ListAssetTypesRequest = {}
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

    async def iter_list_asset_types(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        max_results: Optional[int] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.asset_type_summary.AssetTypeSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_types(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_versions(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> (
        "capo_devops_agent.types.list_asset_versions_response.ListAssetVersionsResponse"
    ):
        """<p>Lists versions of an asset in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset whose versions to list</p>
            max_results: <p>The maximum number of results to return in a single response</p>
            next_token: <p>Pagination token from a previous response to retrieve the next page of results</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_asset_versions_request.ListAssetVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_asset_versions_response.ListAssetVersionsResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_asset_versions

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_asset_versions.async_list_asset_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_asset_versions_request.ListAssetVersionsRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
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

    async def iter_list_asset_versions(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.asset_version_metadata.AssetVersionMetadata]":
        _token = next_token
        while True:
            _response = await self.list_asset_versions(
                agent_space_id,
                asset_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_backlog_tasks(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        filter: Optional["capo_devops_agent.types.task_filter.TaskFilter"] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        sort_field: Optional[
            "capo_devops_agent.types.task_sort_field.TaskSortField"
        ] = None,
        order: Optional["capo_devops_agent.types.task_sort_order.TaskSortOrder"] = None,
    ) -> "capo_devops_agent.types.list_backlog_tasks_response.ListBacklogTasksResponse":
        """<p>Lists backlog tasks in the specified agent space with optional filtering and sorting</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the tasks</p>
            filter: <p>Filter criteria to apply when listing tasks Filtering restrictions: - Each filter field list is limited to a single value - Filtering by Priority and Status at the same time when not filtering by Type is not permitted - Timestamp filters (createdAfter, createdBefore) can be combined with other filters when not sorting by priority</p>
            limit: <p>Maximum number of tasks to return in a single response (1-1000, default: 100)</p>
            next_token: <p>Token for retrieving the next page of results</p>
            sort_field: <p>Field to sort by Sorting restrictions: - Only sorting on createdAt is supported when using priority or status filters alone. - Sorting by priority is not supported when using Timestamp filters (createdAfter, createdBefore)</p>
            order: <p>Sort order for the tasks based on sortField (default: DESC)</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_backlog_tasks_request.ListBacklogTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_backlog_tasks_response.ListBacklogTasksResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_backlog_tasks

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_backlog_tasks.async_list_backlog_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_backlog_tasks_request.ListBacklogTasksRequest = {
            "agent_space_id": agent_space_id
        }
        if filter is not None:
            input_["filter"] = filter
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_field is not None:
            input_["sort_field"] = sort_field
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_backlog_tasks(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        filter: Optional["capo_devops_agent.types.task_filter.TaskFilter"] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        sort_field: Optional[
            "capo_devops_agent.types.task_sort_field.TaskSortField"
        ] = None,
        order: Optional["capo_devops_agent.types.task_sort_order.TaskSortOrder"] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.task.Task]":
        _token = next_token
        while True:
            _response = await self.list_backlog_tasks(
                agent_space_id,
                config_overrides=config_overrides,
                filter=filter,
                limit=limit,
                next_token=_token,
                sort_field=sort_field,
                order=order,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_chats(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        user_id: Optional["capo_devops_agent.types.resource_id.ResourceId"] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_devops_agent.types.list_chats_response.ListChatsResponse":
        """<p>Retrieves a paginated list of the user's recent chat executions</p>

        Args:
            user_id: <p>The user identifier to list chats for. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>
            max_results: <p>Maximum number of results to return</p>
            next_token: <p>Token for pagination</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_chats_request.ListChatsRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_chats_response.ListChatsResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_chats

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_chats.async_list_chats(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_chats_request.ListChatsRequest = {
            "agent_space_id": agent_space_id
        }
        if user_id is not None:
            input_["user_id"] = user_id
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

    async def list_executions(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "capo_devops_agent.types.list_executions_response.ListExecutionsResponse":
        """<p>List executions</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space</p>
            task_id: <p>The unique identifier of the task whose executions to retrieve</p>
            limit: <p>Maximum number of executions to return</p>
            next_token: <p>Token for pagination to retrieve the next set of results</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_executions_request.ListExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_executions_response.ListExecutionsResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_executions

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_executions.async_list_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_executions_request.ListExecutionsRequest = {
            "agent_space_id": agent_space_id,
            "task_id": task_id,
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_executions(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.execution.Execution]":
        _token = next_token
        while True:
            _response = await self.list_executions(
                agent_space_id,
                task_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_goals(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        status: Optional["capo_devops_agent.types.goal_status.GoalStatus"] = None,
        goal_type: Optional["capo_devops_agent.types.goal_type.GoalType"] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "capo_devops_agent.types.list_goals_response.ListGoalsResponse":
        """<p>Lists goals in the specified agent space with optional filtering</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space</p>
            status: <p>Filter goals by goal status</p>
            goal_type: <p>Filter goals by goal type</p>
            limit: <p>Maximum number of goals to return</p>
            next_token: <p>Pagination token for the next set of results</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_goals_request.ListGoalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_goals_response.ListGoalsResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_goals

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_goals.async_list_goals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_goals_request.ListGoalsRequest = {
            "agent_space_id": agent_space_id
        }
        if status is not None:
            input_["status"] = status
        if goal_type is not None:
            input_["goal_type"] = goal_type
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_goals(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        status: Optional["capo_devops_agent.types.goal_status.GoalStatus"] = None,
        goal_type: Optional["capo_devops_agent.types.goal_type.GoalType"] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.goal.Goal]":
        _token = next_token
        while True:
            _response = await self.list_goals(
                agent_space_id,
                config_overrides=config_overrides,
                status=status,
                goal_type=goal_type,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("goals",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_journal_records(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        record_type: Optional[str] = None,
        order: Optional["capo_devops_agent.types.order_type.OrderType"] = None,
    ) -> "capo_devops_agent.types.list_journal_records_response.ListJournalRecordsResponse":
        """<p>List journal records for a specific execution</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the execution</p>
            execution_id: <p>The unique identifier of the execution whose journal records to retrieve</p>
            limit: <p>Maximum number of records to return in a single response (1-100, default: 100)</p>
            next_token: <p>Token for retrieving the next page of results</p>
            record_type: <p>Filter records by type (empty string returns all types)</p>
            order: <p>Sort order for the records based on timestamp (default: DESC)</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_journal_records_request.ListJournalRecordsRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_journal_records_response.ListJournalRecordsResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_journal_records

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_journal_records.async_list_journal_records(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_journal_records_request.ListJournalRecordsRequest = {
            "agent_space_id": agent_space_id,
            "execution_id": execution_id,
        }
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token
        if record_type is not None:
            input_["record_type"] = record_type
        if order is not None:
            input_["order"] = order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_journal_records(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        record_type: Optional[str] = None,
        order: Optional["capo_devops_agent.types.order_type.OrderType"] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.journal_record.JournalRecord]":
        _token = next_token
        while True:
            _response = await self.list_journal_records(
                agent_space_id,
                execution_id,
                config_overrides=config_overrides,
                limit=limit,
                next_token=_token,
                record_type=record_type,
                order=order,
            )
            _page = _resolve_path(_response, ("records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pending_messages(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.list_pending_messages_response.ListPendingMessagesResponse":
        """<p>List pending messages for a specific execution.</p>

        Args:
            execution_id: <p>The unique identifier of the execution whose journal records to retrieve</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_pending_messages_request.ListPendingMessagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_pending_messages_response.ListPendingMessagesResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_pending_messages

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_pending_messages.async_list_pending_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_pending_messages_request.ListPendingMessagesRequest = {
            "agent_space_id": agent_space_id,
            "execution_id": execution_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_recommendations(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        task_id: Optional["capo_devops_agent.types.resource_id.ResourceId"] = None,
        goal_id: Optional["capo_devops_agent.types.resource_id.ResourceId"] = None,
        status: Optional[
            "capo_devops_agent.types.recommendation_status.RecommendationStatus"
        ] = None,
        priority: Optional[
            "capo_devops_agent.types.recommendation_priority.RecommendationPriority"
        ] = None,
        limit: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "capo_devops_agent.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists recommendations for the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the recommendations</p>
            task_id: <p>Optional task ID to filter recommendations by specific task</p>
            goal_id: <p>Optional goal ID to filter recommendations by specific goal</p>
            status: <p>Optional status to filter recommendations by their current status</p>
            priority: <p>Optional priority to filter recommendations by priority level</p>
            limit: <p>Maximum number of recommendations to return in a single response</p>
            next_token: <p>Token for retrieving the next page of results</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_recommendations

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_recommendations.async_list_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_recommendations_request.ListRecommendationsRequest = {
            "agent_space_id": agent_space_id
        }
        if task_id is not None:
            input_["task_id"] = task_id
        if goal_id is not None:
            input_["goal_id"] = goal_id
        if status is not None:
            input_["status"] = status
        if priority is not None:
            input_["priority"] = priority
        if limit is not None:
            input_["limit"] = limit
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
        resource_arn: str,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for the specified AWS DevOps Agent resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def send_message(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        execution_id: "capo_devops_agent.types.chat_execution_id.ChatExecutionId",
        content: "capo_devops_agent.types.message_content.MessageContent",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        context: Optional[
            "capo_devops_agent.types.send_message_context.SendMessageContext"
        ] = None,
        user_id: Optional["capo_devops_agent.types.resource_id.ResourceId"] = None,
        asset_ids: Optional["capo_devops_agent.types.asset_id_list.AssetIdList"] = None,
    ) -> "AsyncGenerator[capo_devops_agent.types.send_message_response.SendMessageResponse]":
        """<p>Sends a chat message and streams the response for the specified agent space execution</p>

        Args:
            agent_space_id: <p>The agent space identifier</p>
            execution_id: <p>The execution identifier for the chat session</p>
            content: <p>The user message content</p>
            context: <p>Optional context for the message</p>
            user_id: <p>User identifier. This field is deprecated and will be ignored — the service resolves user identity from the authenticated session.</p>
            asset_ids: <p>Optional list of asset identifiers to attach to the message</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.send_message_request.SendMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.send_message_response.SendMessageResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.send_message

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.send_message.async_send_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.send_message_request.SendMessageRequest = {
            "agent_space_id": agent_space_id,
            "execution_id": execution_id,
            "content": content,
        }
        if context is not None:
            input_["context"] = context
        if user_id is not None:
            input_["user_id"] = user_id
        if asset_ids is not None:
            input_["asset_ids"] = asset_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def tag_resource(
        self,
        resource_arn: str,
        tags: "capo_devops_agent.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.tag_resource_response.TagResourceResponse":
        """<p>Adds or overwrites tags for the specified AWS DevOps Agent resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to tag.</p>
            tags: <p>Tags to add to the resource.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.tag_resource

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: str,
        tag_keys: "capo_devops_agent.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from the specified AWS DevOps Agent resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource to untag.</p>
            tag_keys: <p>Tag keys to remove.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.untag_resource

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_asset(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        metadata: Optional[object] = None,
        content: Optional["capo_devops_agent.types.asset_content.AssetContent"] = None,
        client_token: Optional[str] = None,
    ) -> "capo_devops_agent.types.update_asset_response.UpdateAssetResponse":
        """<p>Updates an asset in the specified agent space</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset to update</p>
            metadata: <p>Metadata fields to update. Only the fields present in this document are updated. Omitted fields retain their current values.</p>
            content: <p>Optional content to set or replace. A single file adds or replaces one file; a zip replaces all files.</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset update</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_asset_request.UpdateAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_asset_response.UpdateAssetResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_asset

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_asset.async_update_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_asset_request.UpdateAssetRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
        }
        if metadata is not None:
            input_["metadata"] = metadata
        if content is not None:
            input_["content"] = content
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

    async def update_asset_file(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        asset_id: "capo_devops_agent.types.resource_id.ResourceId",
        path: "capo_devops_agent.types.asset_file_path.AssetFilePath",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        content: Optional[
            "capo_devops_agent.types.asset_file_body.AssetFileBody"
        ] = None,
        metadata: Optional[object] = None,
        client_token: Optional[str] = None,
    ) -> "capo_devops_agent.types.update_asset_file_response.UpdateAssetFileResponse":
        """<p>Updates a file in an asset</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the asset</p>
            asset_id: <p>The unique identifier of the asset containing the file</p>
            path: <p>The path of the file within the asset to update</p>
            content: <p>Updated file content. If omitted, the existing content is unchanged.</p>
            metadata: <p>Metadata fields to update. Only the fields present in this document are updated. Omitted fields retain their current values.</p>
            client_token: <p>A unique, case-sensitive identifier used for idempotent asset file update</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_asset_file_request.UpdateAssetFileRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_asset_file_response.UpdateAssetFileResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_asset_file

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_asset_file.async_update_asset_file(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_asset_file_request.UpdateAssetFileRequest = {
            "agent_space_id": agent_space_id,
            "asset_id": asset_id,
            "path": path,
        }
        if content is not None:
            input_["content"] = content
        if metadata is not None:
            input_["metadata"] = metadata
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

    async def update_backlog_task(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        task_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        task_status: Optional["capo_devops_agent.types.task_status.TaskStatus"] = None,
        client_token: Optional[str] = None,
    ) -> (
        "capo_devops_agent.types.update_backlog_task_response.UpdateBacklogTaskResponse"
    ):
        """<p>Update an existing backlog task.</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the task</p>
            task_id: <p>The unique identifier of the task to update</p>
            task_status: <p>Updated task status</p>
            client_token: <p>Client-provided token for idempotent operations</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_backlog_task_request.UpdateBacklogTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_backlog_task_response.UpdateBacklogTaskResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_backlog_task

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_backlog_task.async_update_backlog_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_backlog_task_request.UpdateBacklogTaskRequest = {
            "agent_space_id": agent_space_id,
            "task_id": task_id,
        }
        if task_status is not None:
            input_["task_status"] = task_status
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

    async def update_goal(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        goal_id: str,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        evaluation_schedule: Optional[
            "capo_devops_agent.types.goal_schedule_input.GoalScheduleInput"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_devops_agent.types.update_goal_response.UpdateGoalResponse":
        """<p>Update an existing goal</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the goal</p>
            goal_id: <p>The unique identifier of the goal to update</p>
            evaluation_schedule: <p>Update goal schedule state</p>
            client_token: <p>Client-provided token for idempotent operations</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_goal_request.UpdateGoalRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_goal_response.UpdateGoalResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_goal

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_goal.async_update_goal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_goal_request.UpdateGoalRequest = {
            "agent_space_id": agent_space_id,
            "goal_id": goal_id,
        }
        if evaluation_schedule is not None:
            input_["evaluation_schedule"] = evaluation_schedule
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

    async def update_recommendation(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        recommendation_id: "capo_devops_agent.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        status: Optional[
            "capo_devops_agent.types.recommendation_status.RecommendationStatus"
        ] = None,
        additional_context: Optional[str] = None,
        client_token: Optional[str] = None,
    ) -> "capo_devops_agent.types.update_recommendation_response.UpdateRecommendationResponse":
        """<p>Updates an existing recommendation with new content, status, or metadata</p>

        Args:
            agent_space_id: <p>The unique identifier for the agent space containing the recommendation</p>
            recommendation_id: <p>The unique identifier for the recommendation to update</p>
            status: <p>Current status of the recommendation</p>
            additional_context: <p>Additional context for recommendation</p>
            client_token: <p>A unique token that ensures idempotency of the request</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_recommendation_request.UpdateRecommendationRequest]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_recommendation_response.UpdateRecommendationResponse"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_recommendation

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_recommendation.async_update_recommendation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_recommendation_request.UpdateRecommendationRequest = {
            "agent_space_id": agent_space_id,
            "recommendation_id": recommendation_id,
        }
        if status is not None:
            input_["status"] = status
        if additional_context is not None:
            input_["additional_context"] = additional_context
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

    async def create_agent_space(
        self,
        name: "capo_devops_agent.types.agent_space_name.AgentSpaceName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        description: Optional["capo_devops_agent.types.description.Description"] = None,
        locale: Optional["capo_devops_agent.types.locale.Locale"] = None,
        kms_key_arn: Optional["capo_devops_agent.types.kms_key_arn.KmsKeyArn"] = None,
        client_token: Optional[str] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
    ) -> "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput":
        """<p>Creates a new AgentSpace with the specified name and description. Duplicate space names are allowed.</p>

        Args:
            name: <p>The name of the AgentSpace.</p>
            description: <p>The description of the AgentSpace.</p>
            locale: <p>The locale for the AgentSpace, which determines the language used in agent responses.</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            client_token: <p>Client-provided token to ensure request idempotency. When the same token is provided in subsequent calls, the same response is returned within a 8-hour window.</p>
            tags: <p>Tags to add to the AgentSpace at creation time.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_agent_space_output.CreateAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_agent_space.async_create_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.create_agent_space_input.CreateAgentSpaceInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_space(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput":
        """<p>Retrieves detailed information about a specific AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_agent_space_input.GetAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_agent_space_output.GetAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_agent_space.async_get_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_agent_space_input.GetAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_agent_space(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        name: Optional[
            "capo_devops_agent.types.agent_space_name.AgentSpaceName"
        ] = None,
        description: Optional["capo_devops_agent.types.description.Description"] = None,
        locale: Optional["capo_devops_agent.types.locale.Locale"] = None,
    ) -> "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput":
        """<p>Updates the information of an existing AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            name: <p>The updated name of the AgentSpace.</p>
            description: <p>The updated description of the AgentSpace.</p>
            locale: <p>The updated locale for the AgentSpace, which determines the language used in agent responses.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_agent_space_output.UpdateAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_agent_space.async_update_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_agent_space_input.UpdateAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if locale is not None:
            input_["locale"] = locale

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_agent_space(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput":
        """<p>Deletes an AgentSpace. This operation is idempotent and returns a 204 No Content response on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.delete_agent_space_output.DeleteAgentSpaceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_agent_space

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.delete_agent_space.async_delete_agent_space(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.delete_agent_space_input.DeleteAgentSpaceInput = {
            "agent_space_id": agent_space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disable_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        auth_flow: Optional["capo_devops_agent.types.auth_flow.AuthFlow"] = None,
    ) -> None:
        """<p>Disable the Operator App for the specified AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. idc</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.identity_center_service_exception.IdentityCenterServiceException: <p>Calls to the customer Identity Center have failed</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput]",
        ) -> AsyncOperationResponse[None]:
            import capo_devops_agent._operations.dev_ops_agent.disable_operator_app

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.disable_operator_app.async_disable_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.disable_operator_app_input.DisableOperatorAppInput = {
            "agent_space_id": agent_space_id
        }
        if auth_flow is not None:
            input_["auth_flow"] = auth_flow

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def enable_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        auth_flow: "capo_devops_agent.types.auth_flow.AuthFlow",
        operator_app_role_arn: "capo_devops_agent.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        idc_instance_arn: Optional[str] = None,
        issuer_url: Optional[str] = None,
        idp_client_id: Optional[
            "capo_devops_agent.types.idp_client_id.IdpClientId"
        ] = None,
        idp_client_secret: Optional[
            "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
        provider: Optional[str] = None,
    ) -> "capo_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput":
        """<p>Enable the Operator App to access the given AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            auth_flow: <p>The authentication flow configured for the operator App. e.g. iam or idc</p>
            operator_app_role_arn: <p>The IAM role end users assume to access AIDevOps APIs</p>
            idc_instance_arn: <p>The IdC instance Arn used to create an IdC auth application</p>
            issuer_url: <p>The OIDC issuer URL of the external Identity Provider</p>
            idp_client_id: <p>The OIDC client ID for the IdP application</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>
            provider: <p>The Identity Provider name (e.g., Entra, Okta, Google)</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.identity_center_service_exception.IdentityCenterServiceException: <p>Calls to the customer Identity Center have failed</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.enable_operator_app_output.EnableOperatorAppOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.enable_operator_app

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.enable_operator_app.async_enable_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.enable_operator_app_input.EnableOperatorAppInput = {
            "agent_space_id": agent_space_id,
            "auth_flow": auth_flow,
            "operator_app_role_arn": operator_app_role_arn,
        }
        if idc_instance_arn is not None:
            input_["idc_instance_arn"] = idc_instance_arn
        if issuer_url is not None:
            input_["issuer_url"] = issuer_url
        if idp_client_id is not None:
            input_["idp_client_id"] = idp_client_id
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret
        if provider is not None:
            input_["provider"] = provider

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_operator_app(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_operator_app_output.GetOperatorAppOutput":
        """<p>Get the full auth configuration of operator including any enabled auth flow</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_operator_app_input.GetOperatorAppInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_operator_app_output.GetOperatorAppOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_operator_app

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_operator_app.async_get_operator_app(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_operator_app_input.GetOperatorAppInput = {
            "agent_space_id": agent_space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_operator_app_idp_config(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        idp_client_secret: Optional[
            "capo_devops_agent.types.idp_client_secret.IdpClientSecret"
        ] = None,
    ) -> "capo_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput":
        """<p>Update the external Identity Provider configuration for the Operator App</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            idp_client_secret: <p>The OIDC client secret for the IdP application</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_operator_app_idp_config_output.UpdateOperatorAppIdpConfigOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_operator_app_idp_config.async_update_operator_app_idp_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_operator_app_idp_config_input.UpdateOperatorAppIdpConfigInput = {
            "agent_space_id": agent_space_id
        }
        if idp_client_secret is not None:
            input_["idp_client_secret"] = idp_client_secret

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_agent_spaces(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput":
        """<p>Lists all AgentSpaces with optional pagination.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_agent_spaces_output.ListAgentSpacesOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_agent_spaces

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_agent_spaces.async_list_agent_spaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_agent_spaces_input.ListAgentSpacesInput = {}
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

    async def iter_list_agent_spaces(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.agent_space.AgentSpace]":
        _token = next_token
        while True:
            _response = await self.list_agent_spaces(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_spaces",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def associate_service(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        service_id: "capo_devops_agent.types.service_id.ServiceId",
        configuration: "capo_devops_agent.types.service_configuration.ServiceConfiguration",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.associate_service_output.AssociateServiceOutput":
        """<p>Adds a specific service association to an AgentSpace. It overwrites the existing association of the same service. Returns 201 Created on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            service_id: <p>The unique identifier of the service.</p>
            configuration: <p>The configuration that directs how AgentSpace interacts with the given service.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.associate_service_input.AssociateServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.associate_service_output.AssociateServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.associate_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.associate_service.async_associate_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.associate_service_input.AssociateServiceInput = {
            "agent_space_id": agent_space_id,
            "service_id": service_id,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_association(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        association_id: "capo_devops_agent.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_association_output.GetAssociationOutput":
        """<p>Retrieves given associations configured for a specific AgentSpace.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            association_id: <p>The unique identifier of the given association.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_association_input.GetAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_association_output.GetAssociationOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_association

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_association.async_get_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_association_input.GetAssociationInput = {
            "agent_space_id": agent_space_id,
            "association_id": association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_association(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        association_id: "capo_devops_agent.types.association_id.AssociationId",
        configuration: "capo_devops_agent.types.service_configuration.ServiceConfiguration",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.update_association_output.UpdateAssociationOutput":
        """<p>Partially updates the configuration of an existing service association for an AgentSpace. Present fields are fully replaced; absent fields are left unchanged. Returns 200 OK on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            association_id: <p>The unique identifier of the given association.</p>
            configuration: <p>The configuration that directs how AgentSpace interacts with the given service. The entire configuration is replaced on update.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_association_input.UpdateAssociationInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_association_output.UpdateAssociationOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_association

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_association.async_update_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_association_input.UpdateAssociationInput = {
            "agent_space_id": agent_space_id,
            "association_id": association_id,
            "configuration": configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_service(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        association_id: "capo_devops_agent.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> (
        "capo_devops_agent.types.disassociate_service_output.DisassociateServiceOutput"
    ):
        """<p>Deletes a specific service association from an AgentSpace. This operation is idempotent and returns a 204 No Content response on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            association_id: <p>The unique identifier of the given association.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.disassociate_service_input.DisassociateServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.disassociate_service_output.DisassociateServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.disassociate_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.disassociate_service.async_disassociate_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.disassociate_service_input.DisassociateServiceInput = {
            "agent_space_id": agent_space_id,
            "association_id": association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_webhooks(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        association_id: "capo_devops_agent.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.list_webhooks_output.ListWebhooksOutput":
        """<p>List all webhooks for given Association</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            association_id: <p>The unique identifier of the given association.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_webhooks_input.ListWebhooksInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_webhooks_output.ListWebhooksOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_webhooks

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_webhooks.async_list_webhooks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_webhooks_input.ListWebhooksInput = {
            "agent_space_id": agent_space_id,
            "association_id": association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_associations(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        filter_service_types: Optional[str] = None,
    ) -> "capo_devops_agent.types.list_associations_output.ListAssociationsOutput":
        """<p>List all associations for given AgentSpace</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
            filter_service_types: <p>A comma-separated list of service types to filter list associations output</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_associations_input.ListAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_associations_output.ListAssociationsOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_associations

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_associations.async_list_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_associations_input.ListAssociationsInput = {
            "agent_space_id": agent_space_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_service_types is not None:
            input_["filter_service_types"] = filter_service_types

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_associations(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        filter_service_types: Optional[str] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.association.Association]":
        _token = next_token
        while True:
            _response = await self.list_associations(
                agent_space_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter_service_types=filter_service_types,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def validate_aws_associations(
        self,
        agent_space_id: "capo_devops_agent.types.agent_space_id.AgentSpaceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.validate_aws_associations_output.ValidateAwsAssociationsOutput":
        """<p>Validates an aws association and set status and returns a 204 No Content response on success.</p>

        Args:
            agent_space_id: <p>The unique identifier of the AgentSpace</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.validate_aws_associations_input.ValidateAwsAssociationsInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.validate_aws_associations_output.ValidateAwsAssociationsOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.validate_aws_associations

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.validate_aws_associations.async_validate_aws_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.validate_aws_associations_input.ValidateAwsAssociationsInput = {
            "agent_space_id": agent_space_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_private_connection(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        mode: "capo_devops_agent.types.private_connection_mode.PrivateConnectionMode",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
    ) -> "capo_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput":
        """<p>Creates a Private Connection to a target resource.</p>

        Args:
            name: <p>Unique name for this Private Connection within the account.</p>
            mode: <p>Private Connection mode configuration.</p>
            tags: <p>Tags to add to the Private Connection at creation time.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.create_private_connection_output.CreatePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.create_private_connection

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.create_private_connection.async_create_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.create_private_connection_input.CreatePrivateConnectionInput = {
            "name": name,
            "mode": mode,
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

    async def describe_private_connection(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput":
        """<p>Retrieves details of an existing Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.describe_private_connection_output.DescribePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.describe_private_connection

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.describe_private_connection.async_describe_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.describe_private_connection_input.DescribePrivateConnectionInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_private_connection(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput":
        """<p>Deletes a Private Connection. The deletion is asynchronous and returns DELETE_IN_PROGRESS status.</p>

        Args:
            name: <p>The name of the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.delete_private_connection_output.DeletePrivateConnectionOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.delete_private_connection

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.delete_private_connection.async_delete_private_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.delete_private_connection_input.DeletePrivateConnectionInput = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_private_connections(
        self, *, config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None
    ) -> "capo_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput":
        """<p>Lists all Private Connections in the caller's account.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_private_connections_output.ListPrivateConnectionsOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_private_connections

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_private_connections.async_list_private_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_private_connections_input.ListPrivateConnectionsInput = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_private_connection_certificate(
        self,
        name: "capo_devops_agent.types.private_connection_name.PrivateConnectionName",
        certificate: "capo_devops_agent.types.certificate_string.CertificateString",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput":
        """<p>Updates the certificate associated with a Private Connection.</p>

        Args:
            name: <p>The name of the Private Connection.</p>
            certificate: <p>The new certificate for the Private Connection.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.update_private_connection_certificate_output.UpdatePrivateConnectionCertificateOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.update_private_connection_certificate

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.update_private_connection_certificate.async_update_private_connection_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.update_private_connection_certificate_input.UpdatePrivateConnectionCertificateInput = {
            "name": name,
            "certificate": certificate,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_service(
        self,
        service: "capo_devops_agent.types.post_register_service_supported_service.PostRegisterServiceSupportedService",
        service_details: "capo_devops_agent.types.service_details.ServiceDetails",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        kms_key_arn: Optional["capo_devops_agent.types.kms_key_arn.KmsKeyArn"] = None,
        private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        target_url_private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        exchange_url_private_connection_name: Optional[
            "capo_devops_agent.types.private_connection_name.PrivateConnectionName"
        ] = None,
        name: Optional["capo_devops_agent.types.service_name.ServiceName"] = None,
        tags: Optional["capo_devops_agent.types.tags.Tags"] = None,
    ) -> "capo_devops_agent.types.register_service_output.RegisterServiceOutput":
        """<p>This operation registers the specified service</p>

        Args:
            service_details: <p>Service-specific authorization configuration parameters</p>
            kms_key_arn: <p>The ARN of the AWS Key Management Service (AWS KMS) customer managed key that's used to encrypt resources.</p>
            private_connection_name: <p>The name of the private connection to use for VPC connectivity.</p>
            target_url_private_connection_name: <p>The name of the private connection to use for API calls (target URL) only. Cannot be specified when privateConnectionName is provided.</p>
            exchange_url_private_connection_name: <p>The name of the private connection to use for OAuth token exchange requests only. Cannot be specified when privateConnectionName is provided.</p>
            name: <p>The display name for the service registration.</p>
            tags: <p>Tags to add to the Service at registration time.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.register_service_input.RegisterServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.register_service_output.RegisterServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.register_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.register_service.async_register_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.register_service_input.RegisterServiceInput = {
            "service": service,
            "service_details": service_details,
        }
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if private_connection_name is not None:
            input_["private_connection_name"] = private_connection_name
        if target_url_private_connection_name is not None:
            input_["target_url_private_connection_name"] = (
                target_url_private_connection_name
            )
        if exchange_url_private_connection_name is not None:
            input_["exchange_url_private_connection_name"] = (
                exchange_url_private_connection_name
            )
        if name is not None:
            input_["name"] = name
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_service(
        self,
        service_id: "capo_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.get_service_output.GetServiceOutput":
        """<p>Retrieves given service by it's unique identifier</p>

        Args:
            service_id: <p>The unique identifier of the given service.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.get_service_input.GetServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.get_service_output.GetServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.get_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.get_service.async_get_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.get_service_input.GetServiceInput = {
            "service_id": service_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_service(
        self,
        service_id: "capo_devops_agent.types.service_id.ServiceId",
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
    ) -> "capo_devops_agent.types.deregister_service_output.DeregisterServiceOutput":
        """<p>Deregister a service</p>

        Args:
            service_id: <p>The service id to deregister. A service can only be deregistered if it is not associated with any AgentSpace.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.deregister_service_input.DeregisterServiceInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.deregister_service_output.DeregisterServiceOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.deregister_service

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.deregister_service.async_deregister_service(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.deregister_service_input.DeregisterServiceInput = {
            "service_id": service_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_services(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        filter_service_type: Optional["capo_devops_agent.types.service.Service"] = None,
    ) -> "capo_devops_agent.types.list_services_output.ListServicesOutput":
        """<p>List a list of registered service on the account level.</p>

        Args:
            max_results: <p>Maximum number of results to return in a single call.</p>
            next_token: <p>Token for the next page of results.</p>
            filter_service_type: <p>Optional filter to list only services of a specific type.</p>

        Raises:
            capo_devops_agent.errors.access_denied_exception.AccessDeniedException: <p>Access to the requested resource is denied due to insufficient permissions.</p>
            capo_devops_agent.errors.conflict_exception.ConflictException: <p>The request conflicts with the current state of the resource.</p>
            capo_devops_agent.errors.content_size_exceeded_exception.ContentSizeExceededException: <p>This exception is thrown when the content size exceeds the allowed limit.</p>
            capo_devops_agent.errors.internal_server_exception.InternalServerException: <p>This exception is thrown when an unexpected error occurs in the processing of a request.</p>
            capo_devops_agent.errors.invalid_parameter_exception.InvalidParameterException: <p>One or more parameters provided in the request are invalid.</p>
            capo_devops_agent.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource could not be found.</p>
            capo_devops_agent.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request would exceed the service quota limit.</p>
            capo_devops_agent.errors.throttling_exception.ThrottlingException: <p>The request was throttled due to too many requests. Please slow down and try again.</p>
            capo_devops_agent.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_devops_agent.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_devops_agent.types.list_services_input.ListServicesInput]",
        ) -> AsyncOperationResponse[
            "capo_devops_agent.types.list_services_output.ListServicesOutput"
        ]:
            import capo_devops_agent._operations.dev_ops_agent.list_services

            (
                output,
                http_response,
            ) = await capo_devops_agent._operations.dev_ops_agent.list_services.async_list_services(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_devops_agent.types.list_services_input.ListServicesInput = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter_service_type is not None:
            input_["filter_service_type"] = filter_service_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_services(
        self,
        *,
        config_overrides: Optional[AsyncDevOpsAgentClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional["capo_devops_agent.types.next_token.NextToken"] = None,
        filter_service_type: Optional["capo_devops_agent.types.service.Service"] = None,
    ) -> "AsyncIterator[capo_devops_agent.types.registered_service.RegisteredService]":
        _token = next_token
        while True:
            _response = await self.list_services(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter_service_type=filter_service_type,
            )
            _page = _resolve_path(_response, ("services",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
