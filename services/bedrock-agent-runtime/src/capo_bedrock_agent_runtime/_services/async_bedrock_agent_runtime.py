"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#AmazonBedrockAgentRunTimeService``."""

import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bedrock_agent_runtime._auth._signers
import capo_bedrock_agent_runtime._auth._sigv4
from capo_bedrock_agent_runtime._auth._identity import Credentials
from capo_bedrock_agent_runtime._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_agent_runtime._auth._zapros_handler import AuthMiddleware
from capo_bedrock_agent_runtime._pagination import resolve_path as _resolve_path
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.agentic_retrieve_stream_resource import (
    AsyncAgenticRetrieveStreamResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.check_ingested_document_acl_resource import (
    AsyncCheckIngestedDocumentAclResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.flow_execution_resource import (
    AsyncFlowExecutionResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.flow_resource import (
    AsyncFlowResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.generate_query_resource import (
    AsyncGenerateQueryResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.get_document_content_resource import (
    AsyncGetDocumentContentResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.get_ingested_document_acl_resource import (
    AsyncGetIngestedDocumentAclResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.inference_resource import (
    AsyncInferenceResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.inline_agent_resource import (
    AsyncInlineAgentResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.memory_resource import (
    AsyncMemoryResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.optimize_prompt_resource import (
    AsyncOptimizePromptResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.rerank_resource import (
    AsyncRerankResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.retrieve_and_generate_resource import (
    AsyncRetrieveAndGenerateResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream_resource import (
    AsyncRetrieveAndGenerateStreamResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.retrieve_resource import (
    AsyncRetrieveResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.session_resource import (
    AsyncSessionResource,
)
from capo_bedrock_agent_runtime._resources.amazon_bedrock_agent_run_time_service.tagging_resource import (
    AsyncTaggingResource,
)
from capo_bedrock_agent_runtime._services._aws_config import aaws_config
from capo_bedrock_agent_runtime._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.agent_action_groups
    import capo_bedrock_agent_runtime.types.agent_alias_id
    import capo_bedrock_agent_runtime.types.agent_collaboration
    import capo_bedrock_agent_runtime.types.agent_id
    import capo_bedrock_agent_runtime.types.agentic_retrieve_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_messages
    import capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration
    import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request
    import capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response
    import capo_bedrock_agent_runtime.types.agentic_retrievers
    import capo_bedrock_agent_runtime.types.aws_resource_arn
    import capo_bedrock_agent_runtime.types.bedrock_model_configurations
    import capo_bedrock_agent_runtime.types.check_ingested_document_acl_request
    import capo_bedrock_agent_runtime.types.check_ingested_document_acl_response
    import capo_bedrock_agent_runtime.types.collaborator_configurations
    import capo_bedrock_agent_runtime.types.collaborators
    import capo_bedrock_agent_runtime.types.create_invocation_request
    import capo_bedrock_agent_runtime.types.create_invocation_response
    import capo_bedrock_agent_runtime.types.create_session_request
    import capo_bedrock_agent_runtime.types.create_session_response
    import capo_bedrock_agent_runtime.types.custom_orchestration
    import capo_bedrock_agent_runtime.types.data_source_id
    import capo_bedrock_agent_runtime.types.date_timestamp
    import capo_bedrock_agent_runtime.types.delete_agent_memory_request
    import capo_bedrock_agent_runtime.types.delete_agent_memory_response
    import capo_bedrock_agent_runtime.types.delete_session_request
    import capo_bedrock_agent_runtime.types.delete_session_response
    import capo_bedrock_agent_runtime.types.document_id
    import capo_bedrock_agent_runtime.types.document_output_format
    import capo_bedrock_agent_runtime.types.end_session_request
    import capo_bedrock_agent_runtime.types.end_session_response
    import capo_bedrock_agent_runtime.types.flow_alias_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_event
    import capo_bedrock_agent_runtime.types.flow_execution_event_type
    import capo_bedrock_agent_runtime.types.flow_execution_id
    import capo_bedrock_agent_runtime.types.flow_execution_identifier
    import capo_bedrock_agent_runtime.types.flow_execution_name
    import capo_bedrock_agent_runtime.types.flow_execution_summary
    import capo_bedrock_agent_runtime.types.flow_identifier
    import capo_bedrock_agent_runtime.types.flow_inputs
    import capo_bedrock_agent_runtime.types.generate_query_request
    import capo_bedrock_agent_runtime.types.generate_query_response
    import capo_bedrock_agent_runtime.types.get_agent_memory_request
    import capo_bedrock_agent_runtime.types.get_agent_memory_response
    import capo_bedrock_agent_runtime.types.get_document_content_request
    import capo_bedrock_agent_runtime.types.get_document_content_response
    import capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request
    import capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response
    import capo_bedrock_agent_runtime.types.get_flow_execution_request
    import capo_bedrock_agent_runtime.types.get_flow_execution_response
    import capo_bedrock_agent_runtime.types.get_ingested_document_acl_request
    import capo_bedrock_agent_runtime.types.get_ingested_document_acl_response
    import capo_bedrock_agent_runtime.types.get_invocation_step_request
    import capo_bedrock_agent_runtime.types.get_invocation_step_response
    import capo_bedrock_agent_runtime.types.get_session_request
    import capo_bedrock_agent_runtime.types.get_session_response
    import capo_bedrock_agent_runtime.types.guardrail_configuration
    import capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn
    import capo_bedrock_agent_runtime.types.inline_bedrock_model_configurations
    import capo_bedrock_agent_runtime.types.inline_session_state
    import capo_bedrock_agent_runtime.types.input_prompt
    import capo_bedrock_agent_runtime.types.input_text
    import capo_bedrock_agent_runtime.types.instruction
    import capo_bedrock_agent_runtime.types.invocation_description
    import capo_bedrock_agent_runtime.types.invocation_identifier
    import capo_bedrock_agent_runtime.types.invocation_step_payload
    import capo_bedrock_agent_runtime.types.invocation_step_summary
    import capo_bedrock_agent_runtime.types.invocation_summary
    import capo_bedrock_agent_runtime.types.invoke_agent_request
    import capo_bedrock_agent_runtime.types.invoke_agent_response
    import capo_bedrock_agent_runtime.types.invoke_flow_request
    import capo_bedrock_agent_runtime.types.invoke_flow_response
    import capo_bedrock_agent_runtime.types.invoke_inline_agent_request
    import capo_bedrock_agent_runtime.types.invoke_inline_agent_response
    import capo_bedrock_agent_runtime.types.kms_key_arn
    import capo_bedrock_agent_runtime.types.knowledge_base_identifier
    import capo_bedrock_agent_runtime.types.knowledge_base_query
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration
    import capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result
    import capo_bedrock_agent_runtime.types.knowledge_bases
    import capo_bedrock_agent_runtime.types.list_flow_execution_events_request
    import capo_bedrock_agent_runtime.types.list_flow_execution_events_response
    import capo_bedrock_agent_runtime.types.list_flow_executions_request
    import capo_bedrock_agent_runtime.types.list_flow_executions_response
    import capo_bedrock_agent_runtime.types.list_invocation_steps_request
    import capo_bedrock_agent_runtime.types.list_invocation_steps_response
    import capo_bedrock_agent_runtime.types.list_invocations_request
    import capo_bedrock_agent_runtime.types.list_invocations_response
    import capo_bedrock_agent_runtime.types.list_sessions_request
    import capo_bedrock_agent_runtime.types.list_sessions_response
    import capo_bedrock_agent_runtime.types.list_tags_for_resource_request
    import capo_bedrock_agent_runtime.types.list_tags_for_resource_response
    import capo_bedrock_agent_runtime.types.max_results
    import capo_bedrock_agent_runtime.types.memory
    import capo_bedrock_agent_runtime.types.memory_id
    import capo_bedrock_agent_runtime.types.memory_type
    import capo_bedrock_agent_runtime.types.model_identifier
    import capo_bedrock_agent_runtime.types.model_performance_configuration
    import capo_bedrock_agent_runtime.types.name
    import capo_bedrock_agent_runtime.types.next_token
    import capo_bedrock_agent_runtime.types.optimize_prompt_request
    import capo_bedrock_agent_runtime.types.optimize_prompt_response
    import capo_bedrock_agent_runtime.types.orchestration_type
    import capo_bedrock_agent_runtime.types.prompt_creation_configurations
    import capo_bedrock_agent_runtime.types.prompt_override_configuration
    import capo_bedrock_agent_runtime.types.put_invocation_step_request
    import capo_bedrock_agent_runtime.types.put_invocation_step_response
    import capo_bedrock_agent_runtime.types.query_generation_input
    import capo_bedrock_agent_runtime.types.rerank_queries_list
    import capo_bedrock_agent_runtime.types.rerank_request
    import capo_bedrock_agent_runtime.types.rerank_response
    import capo_bedrock_agent_runtime.types.rerank_result
    import capo_bedrock_agent_runtime.types.rerank_sources_list
    import capo_bedrock_agent_runtime.types.reranking_configuration
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_input
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_request
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_response
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request
    import capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response
    import capo_bedrock_agent_runtime.types.retrieve_request
    import capo_bedrock_agent_runtime.types.retrieve_response
    import capo_bedrock_agent_runtime.types.session_id
    import capo_bedrock_agent_runtime.types.session_identifier
    import capo_bedrock_agent_runtime.types.session_metadata_map
    import capo_bedrock_agent_runtime.types.session_state
    import capo_bedrock_agent_runtime.types.session_summary
    import capo_bedrock_agent_runtime.types.session_ttl
    import capo_bedrock_agent_runtime.types.start_flow_execution_request
    import capo_bedrock_agent_runtime.types.start_flow_execution_response
    import capo_bedrock_agent_runtime.types.stop_flow_execution_request
    import capo_bedrock_agent_runtime.types.stop_flow_execution_response
    import capo_bedrock_agent_runtime.types.streaming_configurations
    import capo_bedrock_agent_runtime.types.tag_key_list
    import capo_bedrock_agent_runtime.types.tag_resource_request
    import capo_bedrock_agent_runtime.types.tag_resource_response
    import capo_bedrock_agent_runtime.types.taggable_resources_arn
    import capo_bedrock_agent_runtime.types.tags_map
    import capo_bedrock_agent_runtime.types.transformation_configuration
    import capo_bedrock_agent_runtime.types.untag_resource_request
    import capo_bedrock_agent_runtime.types.untag_resource_response
    import capo_bedrock_agent_runtime.types.update_session_request
    import capo_bedrock_agent_runtime.types.update_session_response
    import capo_bedrock_agent_runtime.types.user_context
    import capo_bedrock_agent_runtime.types.uuid


class AsyncBedrockAgentRuntimeClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class AsyncBedrockAgentRuntimeClient:
    """A client for the ``BedrockAgentRuntime`` service.

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
        self._config = AsyncBedrockAgentRuntimeClientConfig(
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
        self.agentic_retrieve_stream_resource = AsyncAgenticRetrieveStreamResource(self)
        self.check_ingested_document_acl_resource = (
            AsyncCheckIngestedDocumentAclResource(self)
        )
        self.flow_execution_resource = AsyncFlowExecutionResource(self)
        self.flow_resource = AsyncFlowResource(self)
        self.generate_query_resource = AsyncGenerateQueryResource(self)
        self.get_document_content_resource = AsyncGetDocumentContentResource(self)
        self.get_ingested_document_acl_resource = AsyncGetIngestedDocumentAclResource(
            self
        )
        self.inference_resource = AsyncInferenceResource(self)
        self.inline_agent_resource = AsyncInlineAgentResource(self)
        self.memory_resource = AsyncMemoryResource(self)
        self.optimize_prompt_resource = AsyncOptimizePromptResource(self)
        self.rerank_resource = AsyncRerankResource(self)
        self.retrieve_and_generate_resource = AsyncRetrieveAndGenerateResource(self)
        self.retrieve_and_generate_stream_resource = (
            AsyncRetrieveAndGenerateStreamResource(self)
        )
        self.retrieve_resource = AsyncRetrieveResource(self)
        self.session_resource = AsyncSessionResource(self)
        self.tagging_resource = AsyncTaggingResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockAgentRuntimeClientConfig = config_overrides or {}
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

    @asynccontextmanager
    async def agentic_retrieve_stream(
        self,
        messages: "capo_bedrock_agent_runtime.types.agentic_retrieve_messages.AgenticRetrieveMessages",
        retrievers: "capo_bedrock_agent_runtime.types.agentic_retrievers.AgenticRetrievers",
        agentic_retrieve_configuration: "capo_bedrock_agent_runtime.types.agentic_retrieve_configuration.AgenticRetrieveConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        policy_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_policy_configuration.AgenticRetrievePolicyConfiguration"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
        memory_configuration: Optional[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_memory_configuration.AgenticRetrieveMemoryConfiguration"
        ] = None,
        generate_response: Optional[bool] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse]":
        """<p>Retrieves information from one or more knowledge bases using an agentic approach. Agentic retrieval uses a foundation model to intelligently decompose complex queries into sub-queries and iteratively retrieve relevant information from your knowledge bases. This approach improves retrieval accuracy for complex, multi-step questions that a single retrieval pass might not fully address.</p> <p>The operation returns results through a stream that includes retrieval results, trace events for visibility into the process, and a generated response synthesized from the results by default, which can be turned off.</p>

        Args:
            messages: <p>The list of messages for the agentic retrieval conversation.</p>
            retrievers: <p>The list of retrievers to use for agentic retrieval.</p>
            agentic_retrieve_configuration: <p>Configuration settings for the agentic retrieval operation.</p>
            policy_configuration: <p>Policy configuration for guardrails and content filtering.</p>
            next_token: <p>Opaque continuation token for paginated results.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>
            memory_configuration: <p>The configuration for using an Amazon Bedrock AgentCore Memory resource with this retrieval.</p>
            generate_response: <p>Whether to generate a response based on the retrieved results.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.agentic_retrieve_stream_response.AgenticRetrieveStreamResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.agentic_retrieve_stream

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.agentic_retrieve_stream.async_agentic_retrieve_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.agentic_retrieve_stream_request.AgenticRetrieveStreamRequest = {
            "messages": messages,
            "retrievers": retrievers,
            "agentic_retrieve_configuration": agentic_retrieve_configuration,
        }
        if policy_configuration is not None:
            input_["policy_configuration"] = policy_configuration
        if next_token is not None:
            input_["next_token"] = next_token
        if user_context is not None:
            input_["user_context"] = user_context
        if memory_configuration is not None:
            input_["memory_configuration"] = memory_configuration
        if generate_response is not None:
            input_["generate_response"] = generate_response

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def check_ingested_document_acl(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId",
        document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId",
        user_context: "capo_bedrock_agent_runtime.types.user_context.UserContext",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.check_ingested_document_acl_response.CheckIngestedDocumentAclResponse":
        """<p>Checks whether a user has access to a specific document by verifying against the ingested access control list (ACL) in a knowledge base. Use this operation to validate that document-level access control is working as expected after ingestion. To use this operation, you must have the <code>bedrock:CheckIngestedDocumentAcl</code> permission.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that contains the document.</p>
            data_source_id: <p>The unique identifier of the data source that contains the document.</p>
            document_id: <p>The unique identifier of the document to check access for.</p>
            user_context: <p>The context object containing identity information for access control filtering, including user ID and optional group memberships used to evaluate the document access control list (ACL).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.check_ingested_document_acl_request.CheckIngestedDocumentAclRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.check_ingested_document_acl_response.CheckIngestedDocumentAclResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.check_ingested_document_acl

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.check_ingested_document_acl.async_check_ingested_document_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.check_ingested_document_acl_request.CheckIngestedDocumentAclRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_id": document_id,
            "user_context": user_context,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_execution_flow_snapshot(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response.GetExecutionFlowSnapshotResponse":
        """<p>Retrieves the flow definition snapshot used for a flow execution. The snapshot represents the flow metadata and definition as it existed at the time the execution was started. Note that even if the flow is edited after an execution starts, the snapshot connected to the execution remains unchanged.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the flow execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request.GetExecutionFlowSnapshotRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_response.GetExecutionFlowSnapshotResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_execution_flow_snapshot

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_execution_flow_snapshot.async_get_execution_flow_snapshot(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_execution_flow_snapshot_request.GetExecutionFlowSnapshotRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_flow_execution_response.GetFlowExecutionResponse":
        """<p>Retrieves details about a specific flow execution, including its status, start and end times, and any errors that occurred during execution.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution to retrieve.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_flow_execution_request.GetFlowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_flow_execution_response.GetFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_flow_execution

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_flow_execution.async_get_flow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_flow_execution_request.GetFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_flow_execution_events(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        event_type: "capo_bedrock_agent_runtime.types.flow_execution_event_type.FlowExecutionEventType",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse":
        """<p>Lists events that occurred during a flow execution. Events provide detailed information about the execution progress, including node inputs and outputs, flow inputs and outputs, condition results, and failure events.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution.</p>
            max_results: <p>The maximum number of events to return in a single response. If more events exist than the specified maxResults value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>
            event_type: <p>The type of events to retrieve. Specify <code>Node</code> for node-level events or <code>Flow</code> for flow-level events.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_flow_execution_events_request.ListFlowExecutionEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_flow_execution_events_response.ListFlowExecutionEventsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_execution_events

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_execution_events.async_list_flow_execution_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_flow_execution_events_request.ListFlowExecutionEventsRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
            "event_type": event_type,
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

    async def iter_list_flow_execution_events(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        event_type: "capo_bedrock_agent_runtime.types.flow_execution_event_type.FlowExecutionEventType",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_agent_runtime.types.flow_execution_event.FlowExecutionEvent]":
        _token = next_token
        while True:
            _response = await self.list_flow_execution_events(
                flow_identifier,
                flow_alias_identifier,
                execution_identifier,
                event_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("flow_execution_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_flow_executions(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        flow_alias_identifier: Optional[
            "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_flow_executions_response.ListFlowExecutionsResponse":
        """<p>Lists all executions of a flow. Results can be paginated and include summary information about each execution, such as status, start and end times, and the execution's Amazon Resource Name (ARN).</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow to list executions for.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias to list executions for.</p>
            max_results: <p>The maximum number of flow executions to return in a single response. If more executions exist than the specified <code>maxResults</code> value, a token is included in the response so that the remaining results can be retrieved.</p>
            next_token: <p>A token to retrieve the next set of results. This value is returned in the response if more results are available.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_flow_executions_request.ListFlowExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_flow_executions_response.ListFlowExecutionsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_executions

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_flow_executions.async_list_flow_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_flow_executions_request.ListFlowExecutionsRequest = {
            "flow_identifier": flow_identifier
        }
        if flow_alias_identifier is not None:
            input_["flow_alias_identifier"] = flow_alias_identifier
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

    async def iter_list_flow_executions(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        flow_alias_identifier: Optional[
            "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_agent_runtime.types.flow_execution_summary.FlowExecutionSummary]":
        _token = next_token
        while True:
            _response = await self.list_flow_executions(
                flow_identifier,
                config_overrides=config_overrides,
                flow_alias_identifier=flow_alias_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("flow_execution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        flow_execution_name: Optional[
            "capo_bedrock_agent_runtime.types.flow_execution_name.FlowExecutionName"
        ] = None,
        model_performance_configuration: Optional[
            "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.start_flow_execution_response.StartFlowExecutionResponse":
        """<p>Starts an execution of an Amazon Bedrock flow. Unlike flows that run until completion or time out after five minutes, flow executions let you run flows asynchronously for longer durations. Flow executions also yield control so that your application can perform other tasks.</p> <p>This operation returns an Amazon Resource Name (ARN) that you can use to track and manage your flow execution.</p> <note> <p>Flow executions is in preview release for Amazon Bedrock and is subject to change.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow to execute.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias to use for the flow execution.</p>
            flow_execution_name: <p>The unique name for the flow execution. If you don't provide one, a system-generated name is used.</p>
            inputs: <p>The input data required for the flow execution. This must match the input schema defined in the flow.</p>
            model_performance_configuration: <p>The performance settings for the foundation model used in the flow execution.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.start_flow_execution_response.StartFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.start_flow_execution

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.start_flow_execution.async_start_flow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.start_flow_execution_request.StartFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "inputs": inputs,
        }
        if flow_execution_name is not None:
            input_["flow_execution_name"] = flow_execution_name
        if model_performance_configuration is not None:
            input_["model_performance_configuration"] = model_performance_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_flow_execution(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        execution_identifier: "capo_bedrock_agent_runtime.types.flow_execution_identifier.FlowExecutionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.stop_flow_execution_response.StopFlowExecutionResponse":
        """<p>Stops an Amazon Bedrock flow's execution. This operation prevents further processing of the flow and changes the execution status to <code>Aborted</code>.</p>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias used for the execution.</p>
            execution_identifier: <p>The unique identifier of the flow execution to stop.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.stop_flow_execution_request.StopFlowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.stop_flow_execution_response.StopFlowExecutionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.stop_flow_execution

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.stop_flow_execution.async_stop_flow_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.stop_flow_execution_request.StopFlowExecutionRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "execution_identifier": execution_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def invoke_flow(
        self,
        flow_identifier: "capo_bedrock_agent_runtime.types.flow_identifier.FlowIdentifier",
        flow_alias_identifier: "capo_bedrock_agent_runtime.types.flow_alias_identifier.FlowAliasIdentifier",
        inputs: "capo_bedrock_agent_runtime.types.flow_inputs.FlowInputs",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        enable_trace: Optional[bool] = None,
        model_performance_configuration: Optional[
            "capo_bedrock_agent_runtime.types.model_performance_configuration.ModelPerformanceConfiguration"
        ] = None,
        execution_id: Optional[
            "capo_bedrock_agent_runtime.types.flow_execution_id.FlowExecutionId"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse]":
        """<p>Invokes an alias of a flow to run the inputs that you specify and return the output of each node as a stream. If there's an error, the error is returned. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-test.html">Test a flow in Amazon Bedrock</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeFlow</code>.</p> </note>

        Args:
            flow_identifier: <p>The unique identifier of the flow.</p>
            flow_alias_identifier: <p>The unique identifier of the flow alias.</p>
            inputs: <p>A list of objects, each containing information about an input into the flow.</p>
            enable_trace: <p>Specifies whether to return the trace for the flow or not. Traces track inputs and outputs for nodes in the flow. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/flows-trace.html">Track each step in your prompt flow by viewing its trace in Amazon Bedrock</a>.</p>
            model_performance_configuration: <p>Model performance settings for the request.</p>
            execution_id: <p>The unique identifier for the current flow execution. If you don't provide a value, Amazon Bedrock creates the identifier for you. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_flow_response.InvokeFlowResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_flow.async_invoke_flow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_flow_request.InvokeFlowRequest = {
            "flow_identifier": flow_identifier,
            "flow_alias_identifier": flow_alias_identifier,
            "inputs": inputs,
        }
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if model_performance_configuration is not None:
            input_["model_performance_configuration"] = model_performance_configuration
        if execution_id is not None:
            input_["execution_id"] = execution_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def generate_query(
        self,
        query_generation_input: "capo_bedrock_agent_runtime.types.query_generation_input.QueryGenerationInput",
        transformation_configuration: "capo_bedrock_agent_runtime.types.transformation_configuration.TransformationConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
    ):
        """<p>Generates an SQL query from a natural language query. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-generate-query.html">Generate a query for structured data</a> in the Amazon Bedrock User Guide.</p>

        Args:
            query_generation_input: <p>Specifies information about a natural language query to transform into SQL.</p>
            transformation_configuration: <p>Specifies configurations for transforming the natural language query into SQL.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.generate_query_response.GenerateQueryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.generate_query.async_generate_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.generate_query_request.GenerateQueryRequest = {
            "query_generation_input": query_generation_input,
            "transformation_configuration": transformation_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_document_content(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId",
        document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        output_format: Optional[
            "capo_bedrock_agent_runtime.types.document_output_format.DocumentOutputFormat"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse":
        """<p>Retrieves the content of an ingested document from a knowledge base. Returns a pre-signed URL for secure document access.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that contains the document.</p>
            data_source_id: <p>The unique identifier of the data source that contains the document.</p>
            document_id: <p>The unique identifier of the document to retrieve content for.</p>
            output_format: <p>The output format for the document content. <code>RAW</code> returns the original file. <code>EXTRACTED</code> returns parsed text as JSON. Defaults to <code>RAW</code>.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that results only include documents the user is authorized to access.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_document_content_response.GetDocumentContentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_document_content

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_document_content.async_get_document_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_document_content_request.GetDocumentContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_id": document_id,
        }
        if output_format is not None:
            input_["output_format"] = output_format
        if user_context is not None:
            input_["user_context"] = user_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ingested_document_acl(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        data_source_id: "capo_bedrock_agent_runtime.types.data_source_id.DataSourceId",
        document_id: "capo_bedrock_agent_runtime.types.document_id.DocumentId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse":
        """<p>Retrieves the ingested access control list (ACL) for a specific document in a knowledge base. Use this operation to inspect the allow and deny lists that were ingested for a document to troubleshoot access control issues. To use this operation, you must have the <code>bedrock:GetIngestedDocumentAcl</code> permission.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base that contains the document.</p>
            data_source_id: <p>The unique identifier of the data source that contains the document.</p>
            document_id: <p>The unique identifier of the document to retrieve the ingested access control list (ACL) for.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_ingested_document_acl_request.GetIngestedDocumentAclRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_ingested_document_acl_response.GetIngestedDocumentAclResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_ingested_document_acl

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_ingested_document_acl.async_get_ingested_document_acl(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_ingested_document_acl_request.GetIngestedDocumentAclRequest = {
            "knowledge_base_id": knowledge_base_id,
            "data_source_id": data_source_id,
            "document_id": document_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def invoke_agent(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_state: Optional[
            "capo_bedrock_agent_runtime.types.session_state.SessionState"
        ] = None,
        end_session: Optional[bool] = None,
        enable_trace: Optional[bool] = None,
        input_text: Optional[
            "capo_bedrock_agent_runtime.types.input_text.InputText"
        ] = None,
        memory_id: Optional[
            "capo_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        bedrock_model_configurations: Optional[
            "capo_bedrock_agent_runtime.types.bedrock_model_configurations.BedrockModelConfigurations"
        ] = None,
        streaming_configurations: Optional[
            "capo_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
        ] = None,
        prompt_creation_configurations: Optional[
            "capo_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
        ] = None,
        source_arn: Optional[
            "capo_bedrock_agent_runtime.types.aws_resource_arn.AWSResourceARN"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse]":
        """<note> <p>Amazon Bedrock Agents (now Amazon Bedrock Agents Classic) is no longer open to new customers. For capabilities similar to Bedrock Agents Classic, explore Amazon Bedrock AgentCore. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-classic-maintenance-mode.html">Amazon Bedrock Agents Classic availability change</a>.</p> </note> <note> </note> <p>Sends a prompt for the agent to process and respond to. Note the following fields for the request:</p> <ul> <li> <p>To continue the same conversation with an agent, use the same <code>sessionId</code> value in the request.</p> </li> <li> <p>To activate trace enablement, turn <code>enableTrace</code> to <code>true</code>. Trace enablement helps you follow the agent's reasoning process that led it to the information it processed, the actions it took, and the final result it yielded. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events">Trace enablement</a>.</p> </li> <li> <p>End a conversation by setting <code>endSession</code> to <code>true</code>.</p> </li> <li> <p>In the <code>sessionState</code> object, you can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group.</p> </li> </ul> <p>The response contains both <b>chunk</b> and <b>trace</b> attributes.</p> <p>The final response is returned in the <code>bytes</code> field of the <code>chunk</code> object. The <code>InvokeAgent</code> returns one chunk for the entire interaction.</p> <ul> <li> <p>The <code>attribution</code> object contains citations for parts of the response.</p> </li> <li> <p>If you set <code>enableTrace</code> to <code>true</code> in the request, you can trace the agent's steps and reasoning process that led it to the response.</p> </li> <li> <p>If the action predicted was configured to return control, the response returns parameters for the action, elicited from the user, in the <code>returnControl</code> field.</p> </li> <li> <p>Errors are also surfaced in the response.</p> </li> </ul>

        Args:
            session_state: <p>Contains parameters that specify various attributes of the session. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            agent_id: <p>The unique identifier of the agent to use.</p>
            agent_alias_id: <p>The alias of the agent to use.</p>
            session_id: <p>The unique identifier of the session. Use the same value across requests to continue the same conversation.</p>
            end_session: <p>Specifies whether to end the session with the agent or not.</p>
            enable_trace: <p>Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html#trace-events">Trace enablement</a>.</p>
            input_text: <p>The prompt text to send the agent.</p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            memory_id: <p>The unique identifier of the agent memory.</p>
            bedrock_model_configurations: <p>Model performance settings for the request.</p>
            streaming_configurations: <p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>
            prompt_creation_configurations: <p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>
            source_arn: <p>The ARN of the resource making the request.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.model_not_ready_exception.ModelNotReadyException: <p> The model specified in the request is not ready to serve inference requests. The AWS SDK will automatically retry the operation up to 5 times. For information about configuring automatic retries, see <a href="https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html">Retry behavior</a> in the <i>AWS SDKs and Tools</i> reference guide. </p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_agent_response.InvokeAgentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_agent.async_invoke_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_agent_request.InvokeAgentRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "session_id": session_id,
        }
        if session_state is not None:
            input_["session_state"] = session_state
        if end_session is not None:
            input_["end_session"] = end_session
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if input_text is not None:
            input_["input_text"] = input_text
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if bedrock_model_configurations is not None:
            input_["bedrock_model_configurations"] = bedrock_model_configurations
        if streaming_configurations is not None:
            input_["streaming_configurations"] = streaming_configurations
        if prompt_creation_configurations is not None:
            input_["prompt_creation_configurations"] = prompt_creation_configurations
        if source_arn is not None:
            input_["source_arn"] = source_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    @asynccontextmanager
    async def invoke_inline_agent(
        self,
        foundation_model: "capo_bedrock_agent_runtime.types.model_identifier.ModelIdentifier",
        instruction: "capo_bedrock_agent_runtime.types.instruction.Instruction",
        session_id: "capo_bedrock_agent_runtime.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        customer_encryption_key_arn: Optional[
            "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
        ] = None,
        idle_session_ttl_in_seconds: Optional[
            "capo_bedrock_agent_runtime.types.session_ttl.SessionTTL"
        ] = None,
        action_groups: Optional[
            "capo_bedrock_agent_runtime.types.agent_action_groups.AgentActionGroups"
        ] = None,
        knowledge_bases: Optional[
            "capo_bedrock_agent_runtime.types.knowledge_bases.KnowledgeBases"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent_runtime.types.guardrail_configuration_with_arn.GuardrailConfigurationWithArn"
        ] = None,
        prompt_override_configuration: Optional[
            "capo_bedrock_agent_runtime.types.prompt_override_configuration.PromptOverrideConfiguration"
        ] = None,
        agent_collaboration: Optional[
            "capo_bedrock_agent_runtime.types.agent_collaboration.AgentCollaboration"
        ] = None,
        collaborator_configurations: Optional[
            "capo_bedrock_agent_runtime.types.collaborator_configurations.CollaboratorConfigurations"
        ] = None,
        agent_name: Optional["capo_bedrock_agent_runtime.types.name.Name"] = None,
        end_session: Optional[bool] = None,
        enable_trace: Optional[bool] = None,
        input_text: Optional[
            "capo_bedrock_agent_runtime.types.input_text.InputText"
        ] = None,
        streaming_configurations: Optional[
            "capo_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
        ] = None,
        prompt_creation_configurations: Optional[
            "capo_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
        ] = None,
        inline_session_state: Optional[
            "capo_bedrock_agent_runtime.types.inline_session_state.InlineSessionState"
        ] = None,
        collaborators: Optional[
            "capo_bedrock_agent_runtime.types.collaborators.Collaborators"
        ] = None,
        bedrock_model_configurations: Optional[
            "capo_bedrock_agent_runtime.types.inline_bedrock_model_configurations.InlineBedrockModelConfigurations"
        ] = None,
        orchestration_type: Optional[
            "capo_bedrock_agent_runtime.types.orchestration_type.OrchestrationType"
        ] = None,
        custom_orchestration: Optional[
            "capo_bedrock_agent_runtime.types.custom_orchestration.CustomOrchestration"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse]":
        """<p> Invokes an inline Amazon Bedrock agent using the configurations you provide with the request. </p> <ul> <li> <p>Specify the following fields for security purposes.</p> <ul> <li> <p>(Optional) <code>customerEncryptionKeyArn</code> – The Amazon Resource Name (ARN) of a KMS key to encrypt the creation of the agent.</p> </li> <li> <p>(Optional) <code>idleSessionTTLinSeconds</code> – Specify the number of seconds for which the agent should maintain session information. After this time expires, the subsequent <code>InvokeInlineAgent</code> request begins a new session.</p> </li> </ul> </li> <li> <p>To override the default prompt behavior for agent orchestration and to use advanced prompts, include a <code>promptOverrideConfiguration</code> object. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html">Advanced prompts</a>.</p> </li> <li> <p>The agent instructions will not be honored if your agent has only one knowledge base, uses default prompts, has no action group, and user input is disabled.</p> </li> </ul> <note> </note>

        Args:
            customer_encryption_key_arn: <p> The Amazon Resource Name (ARN) of the Amazon Web Services KMS key to use to encrypt your inline agent. </p>
            foundation_model: <p> The <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns">model identifier (ID)</a> of the model to use for orchestration by the inline agent. For example, <code>meta.llama3-1-70b-instruct-v1:0</code>. </p>
            instruction: <p> The instructions that tell the inline agent what it should do and how it should interact with users. </p>
            idle_session_ttl_in_seconds: <p> The number of seconds for which the inline agent should maintain session information. After this time expires, the subsequent <code>InvokeInlineAgent</code> request begins a new session. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and the data provided before the timeout is deleted.</p>
            action_groups: <p> A list of action groups with each action group defining the action the inline agent needs to carry out. </p>
            knowledge_bases: <p> Contains information of the knowledge bases to associate with. </p>
            guardrail_configuration: <p> The <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">guardrails</a> to assign to the inline agent. </p>
            prompt_override_configuration: <p> Configurations for advanced prompts used to override the default prompts to enhance the accuracy of the inline agent. </p>
            agent_collaboration: <p> Defines how the inline collaborator agent handles information across multiple collaborator agents to coordinate a final response. The inline collaborator agent can also be the supervisor. </p>
            collaborator_configurations: <p> Settings for an inline agent collaborator called with <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeInlineAgent.html">InvokeInlineAgent</a>. </p>
            agent_name: <p>The name for the agent.</p>
            session_id: <p> The unique identifier of the session. Use the same value across requests to continue the same conversation. </p>
            end_session: <p> Specifies whether to end the session with the inline agent or not. </p>
            enable_trace: <p> Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html">Using trace</a>. </p>
            input_text: <p> The prompt text to send to the agent. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            streaming_configurations: <p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>
            prompt_creation_configurations: <p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeInlineAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>
            inline_session_state: <p> Parameters that specify the various attributes of a sessions. You can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html">Control session context</a>. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>
            collaborators: <p> List of collaborator inline agents. </p>
            bedrock_model_configurations: <p>Model settings for the request.</p>
            orchestration_type: <p>Specifies the type of orchestration strategy for the agent. This is set to DEFAULT orchestration type, by default. </p>
            custom_orchestration: <p>Contains details of the custom orchestration configured for the agent. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.invoke_inline_agent_response.InvokeInlineAgentResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_inline_agent

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.invoke_inline_agent.async_invoke_inline_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.invoke_inline_agent_request.InvokeInlineAgentRequest = {
            "foundation_model": foundation_model,
            "instruction": instruction,
            "session_id": session_id,
        }
        if customer_encryption_key_arn is not None:
            input_["customer_encryption_key_arn"] = customer_encryption_key_arn
        if idle_session_ttl_in_seconds is not None:
            input_["idle_session_ttl_in_seconds"] = idle_session_ttl_in_seconds
        if action_groups is not None:
            input_["action_groups"] = action_groups
        if knowledge_bases is not None:
            input_["knowledge_bases"] = knowledge_bases
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if prompt_override_configuration is not None:
            input_["prompt_override_configuration"] = prompt_override_configuration
        if agent_collaboration is not None:
            input_["agent_collaboration"] = agent_collaboration
        if collaborator_configurations is not None:
            input_["collaborator_configurations"] = collaborator_configurations
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if end_session is not None:
            input_["end_session"] = end_session
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace
        if input_text is not None:
            input_["input_text"] = input_text
        if streaming_configurations is not None:
            input_["streaming_configurations"] = streaming_configurations
        if prompt_creation_configurations is not None:
            input_["prompt_creation_configurations"] = prompt_creation_configurations
        if inline_session_state is not None:
            input_["inline_session_state"] = inline_session_state
        if collaborators is not None:
            input_["collaborators"] = collaborators
        if bedrock_model_configurations is not None:
            input_["bedrock_model_configurations"] = bedrock_model_configurations
        if orchestration_type is not None:
            input_["orchestration_type"] = orchestration_type
        if custom_orchestration is not None:
            input_["custom_orchestration"] = custom_orchestration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def delete_agent_memory(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        memory_id: Optional[
            "capo_bedrock_agent_runtime.types.memory_id.MemoryId"
        ] = None,
        session_id: Optional[
            "capo_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse":
        """<p>Deletes memory from the specified memory identifier.</p>

        Args:
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_id: <p>The unique identifier of the memory.</p>
            session_id: <p>The unique session identifier of the memory.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.delete_agent_memory_response.DeleteAgentMemoryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_agent_memory.async_delete_agent_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.delete_agent_memory_request.DeleteAgentMemoryRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
        }
        if memory_id is not None:
            input_["memory_id"] = memory_id
        if session_id is not None:
            input_["session_id"] = session_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_agent_memory(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        memory_type: "capo_bedrock_agent_runtime.types.memory_type.MemoryType",
        memory_id: "capo_bedrock_agent_runtime.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_items: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse":
        """<p>Gets the sessions stored in the memory of the agent.</p>

        Args:
            next_token: <p>If the total number of results is greater than the maxItems value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_items: <p>The maximum number of items to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            agent_id: <p>The unique identifier of the agent to which the alias belongs.</p>
            agent_alias_id: <p>The unique identifier of an alias of an agent.</p>
            memory_type: <p>The type of memory.</p>
            memory_id: <p>The unique identifier of the memory. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_agent_memory_response.GetAgentMemoryResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_agent_memory.async_get_agent_memory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_agent_memory_request.GetAgentMemoryRequest = {
            "agent_id": agent_id,
            "agent_alias_id": agent_alias_id,
            "memory_type": memory_type,
            "memory_id": memory_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_agent_memory(
        self,
        agent_id: "capo_bedrock_agent_runtime.types.agent_id.AgentId",
        agent_alias_id: "capo_bedrock_agent_runtime.types.agent_alias_id.AgentAliasId",
        memory_type: "capo_bedrock_agent_runtime.types.memory_type.MemoryType",
        memory_id: "capo_bedrock_agent_runtime.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_items: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_agent_runtime.types.memory.Memory]":
        _token = next_token
        while True:
            _response = await self.get_agent_memory(
                agent_id,
                agent_alias_id,
                memory_type,
                memory_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_items=max_items,
            )
            _page = _resolve_path(_response, ("memory_contents",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    @asynccontextmanager
    async def optimize_prompt(
        self,
        input: "capo_bedrock_agent_runtime.types.input_prompt.InputPrompt",
        target_model_id: str,
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse]":
        """<p>Optimizes a prompt for the task that you specify. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prompt-management-optimize.html">Optimize a prompt</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            input: <p>Contains the prompt to optimize.</p>
            target_model_id: <p>The unique identifier of the model that you want to optimize the prompt for.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.optimize_prompt_response.OptimizePromptResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.optimize_prompt

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.optimize_prompt.async_optimize_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.optimize_prompt_request.OptimizePromptRequest = {
            "input": input,
            "target_model_id": target_model_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def rerank(
        self,
        queries: "capo_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList",
        sources: "capo_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList",
        reranking_configuration: "capo_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.rerank_response.RerankResponse":
        """<p>Reranks the relevance of sources based on queries. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/rerank.html">Improve the relevance of query responses with a reranker model</a>.</p>

        Args:
            queries: <p>An array of objects, each of which contains information about a query to submit to the reranker model.</p>
            sources: <p>An array of objects, each of which contains information about the sources to rerank.</p>
            reranking_configuration: <p>Contains configurations for reranking.</p>
            next_token: <p>If the total number of results was greater than could fit in a response, a token is returned in the <code>nextToken</code> field. You can enter that token in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.rerank_request.RerankRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.rerank_response.RerankResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.rerank.async_rerank(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.rerank_request.RerankRequest = {
            "queries": queries,
            "sources": sources,
            "reranking_configuration": reranking_configuration,
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

    async def iter_rerank(
        self,
        queries: "capo_bedrock_agent_runtime.types.rerank_queries_list.RerankQueriesList",
        sources: "capo_bedrock_agent_runtime.types.rerank_sources_list.RerankSourcesList",
        reranking_configuration: "capo_bedrock_agent_runtime.types.reranking_configuration.RerankingConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_agent_runtime.types.rerank_result.RerankResult]":
        _token = next_token
        while True:
            _response = await self.rerank(
                queries,
                sources,
                reranking_configuration,
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def retrieve_and_generate(
        self,
        input: "capo_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
        retrieve_and_generate_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
        ] = None,
        session_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse":
        """<p>Queries a knowledge base and generates responses based on the retrieved results and using the specified foundation model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a>. The response only cites sources that are relevant to the query.</p> <note> <p>This API cannot be used with managed knowledge bases. Use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html">AgenticRetrieveStream</a> or <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html">Retrieve</a> with managed knowledge bases.</p> </note>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_response.RetrieveAndGenerateResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate.async_retrieve_and_generate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.retrieve_and_generate_request.RetrieveAndGenerateRequest = {
            "input": input
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if retrieve_and_generate_configuration is not None:
            input_["retrieve_and_generate_configuration"] = (
                retrieve_and_generate_configuration
            )
        if session_configuration is not None:
            input_["session_configuration"] = session_configuration
        if user_context is not None:
            input_["user_context"] = user_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    @asynccontextmanager
    async def retrieve_and_generate_stream(
        self,
        input: "capo_bedrock_agent_runtime.types.retrieve_and_generate_input.RetrieveAndGenerateInput",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agent_runtime.types.session_id.SessionId"
        ] = None,
        retrieve_and_generate_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_configuration.RetrieveAndGenerateConfiguration"
        ] = None,
        session_configuration: Optional[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_session_configuration.RetrieveAndGenerateSessionConfiguration"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "AsyncGenerator[capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse]":
        """<p>Queries a knowledge base and generates responses based on the retrieved results, with output in streaming format.</p> <note> <p>This API cannot be used with managed knowledge bases. Use <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_AgenticRetrieveStream.html">AgenticRetrieveStream</a> or <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_Retrieve.html">Retrieve</a> with managed knowledge bases.</p> </note> <note> <p>The CLI doesn't support streaming operations in Amazon Bedrock, including <code>InvokeModelWithResponseStream</code>.</p> </note> <p>This operation requires permission for the <code> bedrock:RetrieveAndGenerate</code> action.</p>

        Args:
            session_id: <p>The unique identifier of the session. When you first make a <code>RetrieveAndGenerate</code> request, Amazon Bedrock automatically generates this value. You must reuse this value for all subsequent requests in the same conversational session. This value allows Amazon Bedrock to maintain context and knowledge from previous interactions. You can't explicitly set the <code>sessionId</code> yourself.</p>
            input: <p>Contains the query to be made to the knowledge base.</p>
            retrieve_and_generate_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>
            session_configuration: <p>Contains details about the session with the knowledge base.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_response.RetrieveAndGenerateStreamResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve_and_generate_stream.async_retrieve_and_generate_stream(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.retrieve_and_generate_stream_request.RetrieveAndGenerateStreamRequest = {
            "input": input
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if retrieve_and_generate_configuration is not None:
            input_["retrieve_and_generate_configuration"] = (
                retrieve_and_generate_configuration
            )
        if session_configuration is not None:
            input_["session_configuration"] = session_configuration
        if user_context is not None:
            input_["user_context"] = user_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def retrieve(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        retrieval_query: "capo_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        retrieval_configuration: Optional[
            "capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse":
        """<p>Queries a knowledge base and retrieves information from it.</p>

        Args:
            knowledge_base_id: <p>The unique identifier of the knowledge base to query.</p>
            retrieval_query: <p>Contains the query to send the knowledge base.</p>
            retrieval_configuration: <p>Contains configurations for the knowledge base query and retrieval process. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/kb-test-config.html">Query configurations</a>.</p>
            guardrail_configuration: <p>Guardrail settings.</p>
            next_token: <p>If there are more results than can fit in the response, the response returns a <code>nextToken</code>. Use this token in the <code>nextToken</code> field of another request to retrieve the next batch of results.</p>
            user_context: <p>Contains information about the user making the request. This is used for access control filtering to ensure that retrieval results only include documents the user is authorized to access.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.bad_gateway_exception.BadGatewayException: <p>There was an issue with a dependency due to a server issue. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.dependency_failed_exception.DependencyFailedException: <p>There was an issue with a dependency. Check the resource configurations and retry the request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.retrieve_response.RetrieveResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.retrieve.async_retrieve(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.retrieve_request.RetrieveRequest = {
            "knowledge_base_id": knowledge_base_id,
            "retrieval_query": retrieval_query,
        }
        if retrieval_configuration is not None:
            input_["retrieval_configuration"] = retrieval_configuration
        if guardrail_configuration is not None:
            input_["guardrail_configuration"] = guardrail_configuration
        if next_token is not None:
            input_["next_token"] = next_token
        if user_context is not None:
            input_["user_context"] = user_context

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_retrieve(
        self,
        knowledge_base_id: "capo_bedrock_agent_runtime.types.knowledge_base_identifier.KnowledgeBaseIdentifier",
        retrieval_query: "capo_bedrock_agent_runtime.types.knowledge_base_query.KnowledgeBaseQuery",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        retrieval_configuration: Optional[
            "capo_bedrock_agent_runtime.types.knowledge_base_retrieval_configuration.KnowledgeBaseRetrievalConfiguration"
        ] = None,
        guardrail_configuration: Optional[
            "capo_bedrock_agent_runtime.types.guardrail_configuration.GuardrailConfiguration"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        user_context: Optional[
            "capo_bedrock_agent_runtime.types.user_context.UserContext"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_agent_runtime.types.knowledge_base_retrieval_result.KnowledgeBaseRetrievalResult]":
        _token = next_token
        while True:
            _response = await self.retrieve(
                knowledge_base_id,
                retrieval_query,
                config_overrides=config_overrides,
                retrieval_configuration=retrieval_configuration,
                guardrail_configuration=guardrail_configuration,
                next_token=_token,
                user_context=user_context,
            )
            _page = _resolve_path(_response, ("retrieval_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_session(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_metadata: Optional[
            "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
        ] = None,
        encryption_key_arn: Optional[
            "capo_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agent_runtime.types.tags_map.TagsMap"] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.create_session_response.CreateSessionResponse"
    ):
        """<p>Creates a session to temporarily store conversations for generative AI (GenAI) applications built with open-source frameworks such as LangGraph and LlamaIndex. Sessions enable you to save the state of conversations at checkpoints, with the added security and infrastructure of Amazon Web Services. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p> <p>By default, Amazon Bedrock uses Amazon Web Services-managed keys for session encryption, including session metadata, or you can use your own KMS key. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>.</p> <note> <p> You use a session to store state and conversation history for generative AI applications built with open-source frameworks. For Amazon Bedrock Agents, the service automatically manages conversation context and associates them with the agent-specific sessionId you specify in the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html">InvokeAgent</a> API operation. </p> </note> <p>Related APIs:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html">ListSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html">GetSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html">EndSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_DeleteSession.html">DeleteSession</a> </p> </li> </ul>

        Args:
            session_metadata: <p>A map of key-value pairs containing attributes to be persisted across the session. For example, the user's ID, their language preference, and the type of device they are using.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key to use to encrypt the session data. The user or role creating the session must have permission to use the key. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/session-encryption.html">Amazon Bedrock session encryption</a>. </p>
            tags: <p>Specify the key-value pairs for the tags that you want to attach to the session.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.create_session_request.CreateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_session.async_create_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.create_session_request.CreateSessionRequest = {}
        if session_metadata is not None:
            input_["session_metadata"] = session_metadata
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_session_response.GetSessionResponse":
        """<p>Retrieves details about a specific session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>A unique identifier for the session to retrieve. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_session_response.GetSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_session_request.GetSessionRequest = {
            "session_identifier": session_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_session(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        session_metadata: Optional[
            "capo_bedrock_agent_runtime.types.session_metadata_map.SessionMetadataMap"
        ] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.update_session_response.UpdateSessionResponse"
    ):
        """<p>Updates the metadata or encryption settings of a session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_metadata: <p>A map of key-value pairs containing attributes to be persisted across the session. For example the user's ID, their language preference, and the type of device they are using.</p>
            session_identifier: <p>The unique identifier of the session to modify. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.update_session_request.UpdateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.update_session_response.UpdateSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.update_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.update_session.async_update_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.update_session_request.UpdateSessionRequest = {
            "session_identifier": session_identifier
        }
        if session_metadata is not None:
            input_["session_metadata"] = session_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_session(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.delete_session_response.DeleteSessionResponse"
    ):
        """<p>Deletes a session that you ended. You can't delete a session with an <code>ACTIVE</code> status. To delete an active session, you must first end it with the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_EndSession.html">EndSession</a> API operation. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>The unique identifier for the session to be deleted. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.delete_session_request.DeleteSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.delete_session_response.DeleteSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.delete_session.async_delete_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.delete_session_request.DeleteSessionRequest = {
            "session_identifier": session_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_sessions(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists all sessions in your Amazon Web Services account. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results. </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_sessions_request.ListSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_sessions

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_sessions.async_list_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_sessions_request.ListSessionsRequest = {}
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

    async def iter_list_sessions(
        self,
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
    ) -> (
        "AsyncIterator[capo_bedrock_agent_runtime.types.session_summary.SessionSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_sessions(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("session_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def end_session(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.end_session_response.EndSessionResponse":
        """<p>Ends the session. After you end a session, you can still access its content but you can’t add to it. To delete the session and it's content, you use the DeleteSession API operation. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            session_identifier: <p>The unique identifier for the session to end. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.end_session_request.EndSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.end_session_response.EndSessionResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.end_session

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.end_session.async_end_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.end_session_request.EndSessionRequest = {
            "session_identifier": session_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_invocation(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        invocation_id: Optional["capo_bedrock_agent_runtime.types.uuid.Uuid"] = None,
        description: Optional[
            "capo_bedrock_agent_runtime.types.invocation_description.InvocationDescription"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.create_invocation_response.CreateInvocationResponse":
        """<p>Creates a new invocation within a session. An invocation groups the related invocation steps that store the content from a conversation. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p> <p>Related APIs</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html">ListInvocations</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListSessions.html">ListSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetSession.html">GetSession</a> </p> </li> </ul>

        Args:
            invocation_id: <p>A unique identifier for the invocation in UUID format.</p>
            description: <p>A description for the interactions in the invocation. For example, "User asking about weather in Seattle".</p>
            session_identifier: <p>The unique identifier for the associated session for the invocation. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN). </p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.create_invocation_request.CreateInvocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.create_invocation_response.CreateInvocationResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_invocation

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.create_invocation.async_create_invocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.create_invocation_request.CreateInvocationRequest = {
            "session_identifier": session_identifier
        }
        if invocation_id is not None:
            input_["invocation_id"] = invocation_id
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_invocations(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_invocations_response.ListInvocationsResponse":
        """<p>Lists all invocations associated with a specific session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results. </p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            session_identifier: <p>The unique identifier for the session to list invocations for. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_invocations_request.ListInvocationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_invocations_response.ListInvocationsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_invocations

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_invocations.async_list_invocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_invocations_request.ListInvocationsRequest = {
            "session_identifier": session_identifier
        }
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

    async def iter_list_invocations(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_agent_runtime.types.invocation_summary.InvocationSummary]":
        _token = next_token
        while True:
            _response = await self.list_invocations(
                session_identifier,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("invocation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_invocation_step(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        invocation_identifier: "capo_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier",
        invocation_step_time: "capo_bedrock_agent_runtime.types.date_timestamp.DateTimestamp",
        payload: "capo_bedrock_agent_runtime.types.invocation_step_payload.InvocationStepPayload",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        invocation_step_id: Optional[
            "capo_bedrock_agent_runtime.types.uuid.Uuid"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.put_invocation_step_response.PutInvocationStepResponse":
        """<p>Add an invocation step to an invocation in a session. An invocation step stores fine-grained state checkpoints, including text and images, for each interaction. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p> <p>Related APIs:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_GetInvocationStep.html">GetInvocationStep</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocationSteps.html">ListInvocationSteps</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html">ListInvocations</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_ListInvocations.html">ListSessions</a> </p> </li> </ul>

        Args:
            session_identifier: <p>The unique identifier for the session to add the invocation step to. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>
            invocation_identifier: <p>The unique identifier (in UUID format) of the invocation to add the invocation step to.</p>
            invocation_step_time: <p>The timestamp for when the invocation step occurred.</p>
            payload: <p>The payload for the invocation step, including text and images for the interaction.</p>
            invocation_step_id: <p>The unique identifier of the invocation step in UUID format.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.conflict_exception.ConflictException: <p>There was a conflict performing an operation. Resolve the conflict and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.put_invocation_step_request.PutInvocationStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.put_invocation_step_response.PutInvocationStepResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.put_invocation_step

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.put_invocation_step.async_put_invocation_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.put_invocation_step_request.PutInvocationStepRequest = {
            "session_identifier": session_identifier,
            "invocation_identifier": invocation_identifier,
            "invocation_step_time": invocation_step_time,
            "payload": payload,
        }
        if invocation_step_id is not None:
            input_["invocation_step_id"] = invocation_step_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_invocation_step(
        self,
        invocation_identifier: "capo_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier",
        invocation_step_id: "capo_bedrock_agent_runtime.types.uuid.Uuid",
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.get_invocation_step_response.GetInvocationStepResponse":
        """<p>Retrieves the details of a specific invocation step within an invocation in a session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            invocation_identifier: <p>The unique identifier for the invocation in UUID format.</p>
            invocation_step_id: <p>The unique identifier (in UUID format) for the specific invocation step to retrieve.</p>
            session_identifier: <p>The unique identifier for the invocation step's associated session. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.get_invocation_step_request.GetInvocationStepRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.get_invocation_step_response.GetInvocationStepResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_invocation_step

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.get_invocation_step.async_get_invocation_step(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.get_invocation_step_request.GetInvocationStepRequest = {
            "invocation_identifier": invocation_identifier,
            "invocation_step_id": invocation_step_id,
            "session_identifier": session_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_invocation_steps(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        invocation_identifier: Optional[
            "capo_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_invocation_steps_response.ListInvocationStepsResponse":
        """<p>Lists all invocation steps associated with a session and optionally, an invocation within the session. For more information about sessions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/sessions.html">Store and retrieve conversation history and context with Amazon Bedrock sessions</a>.</p>

        Args:
            invocation_identifier: <p>The unique identifier (in UUID format) for the invocation to list invocation steps for.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results. </p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            session_identifier: <p>The unique identifier for the session associated with the invocation steps. You can specify either the session's <code>sessionId</code> or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_invocation_steps_request.ListInvocationStepsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_invocation_steps_response.ListInvocationStepsResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_invocation_steps

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_invocation_steps.async_list_invocation_steps(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_invocation_steps_request.ListInvocationStepsRequest = {
            "session_identifier": session_identifier
        }
        if invocation_identifier is not None:
            input_["invocation_identifier"] = invocation_identifier
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

    async def iter_list_invocation_steps(
        self,
        session_identifier: "capo_bedrock_agent_runtime.types.session_identifier.SessionIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
        invocation_identifier: Optional[
            "capo_bedrock_agent_runtime.types.invocation_identifier.InvocationIdentifier"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agent_runtime.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agent_runtime.types.max_results.MaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock_agent_runtime.types.invocation_step_summary.InvocationStepSummary]":
        _token = next_token
        while True:
            _response = await self.list_invocation_steps(
                session_identifier,
                config_overrides=config_overrides,
                invocation_identifier=invocation_identifier,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("invocation_step_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all the tags for the resource you specify.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to list tags.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "capo_bedrock_agent_runtime.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> "capo_bedrock_agent_runtime.types.tag_resource_response.TagResourceResponse":
        """<p>Associate tags with a resource. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the Amazon Bedrock User Guide.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>An object containing key-value pairs that define the tags to attach to the resource.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_bedrock_agent_runtime.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "capo_bedrock_agent_runtime.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockAgentRuntimeClientConfig] = None,
    ) -> (
        "capo_bedrock_agent_runtime.types.untag_resource_response.UntagResourceResponse"
    ):
        """<p>Remove tags from a resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource from which to remove tags.</p>
            tag_keys: <p>A list of keys of the tags to remove from the resource.</p>

        Raises:
            capo_bedrock_agent_runtime.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions. Check your permissions and retry your request.</p>
            capo_bedrock_agent_runtime.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock_agent_runtime.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock_agent_runtime.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock_agent_runtime.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock_agent_runtime.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock_agent_runtime.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock_agent_runtime.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock_agent_runtime._operations.amazon_bedrock_agent_run_time_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agent_runtime.types.untag_resource_request.UntagResourceRequest = {
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
