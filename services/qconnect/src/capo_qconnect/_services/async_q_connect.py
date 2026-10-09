"""Generated from Smithy shape ``com.amazonaws.qconnect#WisdomService``."""

import datetime
import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_qconnect._auth._signers
import capo_qconnect._auth._sigv4
from capo_qconnect._auth._identity import Credentials
from capo_qconnect._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_qconnect._auth._zapros_handler import AuthMiddleware
from capo_qconnect._pagination import resolve_path as _resolve_path
from capo_qconnect._resources.wisdom_service.assistant import AsyncAssistant
from capo_qconnect._resources.wisdom_service.knowledge_base import AsyncKnowledgeBase
from capo_qconnect._services._aws_config import aaws_config
from capo_qconnect._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_qconnect.types.activate_message_template_request
    import capo_qconnect.types.activate_message_template_response
    import capo_qconnect.types.ai_agent_configuration
    import capo_qconnect.types.ai_agent_configuration_data
    import capo_qconnect.types.ai_agent_configuration_map
    import capo_qconnect.types.ai_agent_summary
    import capo_qconnect.types.ai_agent_type
    import capo_qconnect.types.ai_agent_version_summary
    import capo_qconnect.types.ai_guardrail_blocked_messaging
    import capo_qconnect.types.ai_guardrail_content_policy_config
    import capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config
    import capo_qconnect.types.ai_guardrail_description
    import capo_qconnect.types.ai_guardrail_sensitive_information_policy_config
    import capo_qconnect.types.ai_guardrail_summary
    import capo_qconnect.types.ai_guardrail_topic_policy_config
    import capo_qconnect.types.ai_guardrail_version_summary
    import capo_qconnect.types.ai_guardrail_word_policy_config
    import capo_qconnect.types.ai_prompt_api_format
    import capo_qconnect.types.ai_prompt_inference_configuration
    import capo_qconnect.types.ai_prompt_model_identifier
    import capo_qconnect.types.ai_prompt_summary
    import capo_qconnect.types.ai_prompt_template_configuration
    import capo_qconnect.types.ai_prompt_template_type
    import capo_qconnect.types.ai_prompt_type
    import capo_qconnect.types.ai_prompt_version_summary
    import capo_qconnect.types.arn
    import capo_qconnect.types.assistant_association_input_data
    import capo_qconnect.types.assistant_association_summary
    import capo_qconnect.types.assistant_summary
    import capo_qconnect.types.assistant_type
    import capo_qconnect.types.association_type
    import capo_qconnect.types.attachment_file_name
    import capo_qconnect.types.channel_subtype
    import capo_qconnect.types.channels
    import capo_qconnect.types.client_token
    import capo_qconnect.types.contact_attributes
    import capo_qconnect.types.content_association_contents
    import capo_qconnect.types.content_association_summary
    import capo_qconnect.types.content_association_type
    import capo_qconnect.types.content_disposition
    import capo_qconnect.types.content_feedback_data
    import capo_qconnect.types.content_metadata
    import capo_qconnect.types.content_summary
    import capo_qconnect.types.content_title
    import capo_qconnect.types.content_type
    import capo_qconnect.types.conversation_context
    import capo_qconnect.types.create_ai_agent_request
    import capo_qconnect.types.create_ai_agent_response
    import capo_qconnect.types.create_ai_agent_version_request
    import capo_qconnect.types.create_ai_agent_version_response
    import capo_qconnect.types.create_ai_guardrail_request
    import capo_qconnect.types.create_ai_guardrail_response
    import capo_qconnect.types.create_ai_guardrail_version_request
    import capo_qconnect.types.create_ai_guardrail_version_response
    import capo_qconnect.types.create_ai_prompt_request
    import capo_qconnect.types.create_ai_prompt_response
    import capo_qconnect.types.create_ai_prompt_version_request
    import capo_qconnect.types.create_ai_prompt_version_response
    import capo_qconnect.types.create_assistant_association_request
    import capo_qconnect.types.create_assistant_association_response
    import capo_qconnect.types.create_assistant_request
    import capo_qconnect.types.create_assistant_response
    import capo_qconnect.types.create_content_association_request
    import capo_qconnect.types.create_content_association_response
    import capo_qconnect.types.create_content_request
    import capo_qconnect.types.create_content_response
    import capo_qconnect.types.create_knowledge_base_request
    import capo_qconnect.types.create_knowledge_base_response
    import capo_qconnect.types.create_message_template_attachment_request
    import capo_qconnect.types.create_message_template_attachment_response
    import capo_qconnect.types.create_message_template_request
    import capo_qconnect.types.create_message_template_response
    import capo_qconnect.types.create_message_template_version_request
    import capo_qconnect.types.create_message_template_version_response
    import capo_qconnect.types.create_quick_response_request
    import capo_qconnect.types.create_quick_response_response
    import capo_qconnect.types.create_session_request
    import capo_qconnect.types.create_session_response
    import capo_qconnect.types.deactivate_message_template_request
    import capo_qconnect.types.deactivate_message_template_response
    import capo_qconnect.types.delete_ai_agent_request
    import capo_qconnect.types.delete_ai_agent_response
    import capo_qconnect.types.delete_ai_agent_version_request
    import capo_qconnect.types.delete_ai_agent_version_response
    import capo_qconnect.types.delete_ai_guardrail_request
    import capo_qconnect.types.delete_ai_guardrail_response
    import capo_qconnect.types.delete_ai_guardrail_version_request
    import capo_qconnect.types.delete_ai_guardrail_version_response
    import capo_qconnect.types.delete_ai_prompt_request
    import capo_qconnect.types.delete_ai_prompt_response
    import capo_qconnect.types.delete_ai_prompt_version_request
    import capo_qconnect.types.delete_ai_prompt_version_response
    import capo_qconnect.types.delete_assistant_association_request
    import capo_qconnect.types.delete_assistant_association_response
    import capo_qconnect.types.delete_assistant_request
    import capo_qconnect.types.delete_assistant_response
    import capo_qconnect.types.delete_content_association_request
    import capo_qconnect.types.delete_content_association_response
    import capo_qconnect.types.delete_content_request
    import capo_qconnect.types.delete_content_response
    import capo_qconnect.types.delete_import_job_request
    import capo_qconnect.types.delete_import_job_response
    import capo_qconnect.types.delete_knowledge_base_request
    import capo_qconnect.types.delete_knowledge_base_response
    import capo_qconnect.types.delete_message_template_attachment_request
    import capo_qconnect.types.delete_message_template_attachment_response
    import capo_qconnect.types.delete_message_template_request
    import capo_qconnect.types.delete_message_template_response
    import capo_qconnect.types.delete_quick_response_request
    import capo_qconnect.types.delete_quick_response_response
    import capo_qconnect.types.description
    import capo_qconnect.types.external_source_configuration
    import capo_qconnect.types.generic_arn
    import capo_qconnect.types.get_ai_agent_request
    import capo_qconnect.types.get_ai_agent_response
    import capo_qconnect.types.get_ai_guardrail_request
    import capo_qconnect.types.get_ai_guardrail_response
    import capo_qconnect.types.get_ai_prompt_request
    import capo_qconnect.types.get_ai_prompt_response
    import capo_qconnect.types.get_assistant_association_request
    import capo_qconnect.types.get_assistant_association_response
    import capo_qconnect.types.get_assistant_request
    import capo_qconnect.types.get_assistant_response
    import capo_qconnect.types.get_content_association_request
    import capo_qconnect.types.get_content_association_response
    import capo_qconnect.types.get_content_request
    import capo_qconnect.types.get_content_response
    import capo_qconnect.types.get_content_summary_request
    import capo_qconnect.types.get_content_summary_response
    import capo_qconnect.types.get_import_job_request
    import capo_qconnect.types.get_import_job_response
    import capo_qconnect.types.get_knowledge_base_request
    import capo_qconnect.types.get_knowledge_base_response
    import capo_qconnect.types.get_message_template_request
    import capo_qconnect.types.get_message_template_response
    import capo_qconnect.types.get_next_message_request
    import capo_qconnect.types.get_next_message_response
    import capo_qconnect.types.get_quick_response_request
    import capo_qconnect.types.get_quick_response_response
    import capo_qconnect.types.get_recommendations_request
    import capo_qconnect.types.get_recommendations_response
    import capo_qconnect.types.get_session_request
    import capo_qconnect.types.get_session_response
    import capo_qconnect.types.grouping_configuration
    import capo_qconnect.types.import_job_summary
    import capo_qconnect.types.import_job_type
    import capo_qconnect.types.knowledge_base_search_type
    import capo_qconnect.types.knowledge_base_summary
    import capo_qconnect.types.knowledge_base_type
    import capo_qconnect.types.language_code
    import capo_qconnect.types.list_ai_agent_versions_request
    import capo_qconnect.types.list_ai_agent_versions_response
    import capo_qconnect.types.list_ai_agents_request
    import capo_qconnect.types.list_ai_agents_response
    import capo_qconnect.types.list_ai_guardrail_versions_request
    import capo_qconnect.types.list_ai_guardrail_versions_response
    import capo_qconnect.types.list_ai_guardrails_request
    import capo_qconnect.types.list_ai_guardrails_response
    import capo_qconnect.types.list_ai_prompt_versions_request
    import capo_qconnect.types.list_ai_prompt_versions_response
    import capo_qconnect.types.list_ai_prompts_request
    import capo_qconnect.types.list_ai_prompts_response
    import capo_qconnect.types.list_assistant_associations_request
    import capo_qconnect.types.list_assistant_associations_response
    import capo_qconnect.types.list_assistants_request
    import capo_qconnect.types.list_assistants_response
    import capo_qconnect.types.list_content_associations_request
    import capo_qconnect.types.list_content_associations_response
    import capo_qconnect.types.list_contents_request
    import capo_qconnect.types.list_contents_response
    import capo_qconnect.types.list_import_jobs_request
    import capo_qconnect.types.list_import_jobs_response
    import capo_qconnect.types.list_knowledge_bases_request
    import capo_qconnect.types.list_knowledge_bases_response
    import capo_qconnect.types.list_message_template_versions_request
    import capo_qconnect.types.list_message_template_versions_response
    import capo_qconnect.types.list_message_templates_request
    import capo_qconnect.types.list_message_templates_response
    import capo_qconnect.types.list_messages_request
    import capo_qconnect.types.list_messages_response
    import capo_qconnect.types.list_models_request
    import capo_qconnect.types.list_models_response
    import capo_qconnect.types.list_quick_responses_request
    import capo_qconnect.types.list_quick_responses_response
    import capo_qconnect.types.list_spans_request
    import capo_qconnect.types.list_spans_response
    import capo_qconnect.types.list_tags_for_resource_request
    import capo_qconnect.types.list_tags_for_resource_response
    import capo_qconnect.types.max_results
    import capo_qconnect.types.message_configuration
    import capo_qconnect.types.message_filter_type
    import capo_qconnect.types.message_input
    import capo_qconnect.types.message_metadata
    import capo_qconnect.types.message_output
    import capo_qconnect.types.message_template_attributes
    import capo_qconnect.types.message_template_content_provider
    import capo_qconnect.types.message_template_content_sha256
    import capo_qconnect.types.message_template_search_expression
    import capo_qconnect.types.message_template_search_result_data
    import capo_qconnect.types.message_template_source_configuration
    import capo_qconnect.types.message_template_summary
    import capo_qconnect.types.message_template_version_summary
    import capo_qconnect.types.message_type
    import capo_qconnect.types.model_lifecycle
    import capo_qconnect.types.model_summary
    import capo_qconnect.types.name
    import capo_qconnect.types.next_token
    import capo_qconnect.types.non_empty_sensitive_string
    import capo_qconnect.types.non_empty_string
    import capo_qconnect.types.non_empty_unlimited_string
    import capo_qconnect.types.notify_recommendations_received_request
    import capo_qconnect.types.notify_recommendations_received_response
    import capo_qconnect.types.orchestrator_configuration_list
    import capo_qconnect.types.origin
    import capo_qconnect.types.put_feedback_request
    import capo_qconnect.types.put_feedback_response
    import capo_qconnect.types.query_assistant_request
    import capo_qconnect.types.query_assistant_response
    import capo_qconnect.types.query_condition_expression
    import capo_qconnect.types.query_input_data
    import capo_qconnect.types.query_text
    import capo_qconnect.types.quick_response_data_provider
    import capo_qconnect.types.quick_response_description
    import capo_qconnect.types.quick_response_name
    import capo_qconnect.types.quick_response_search_expression
    import capo_qconnect.types.quick_response_search_result_data
    import capo_qconnect.types.quick_response_summary
    import capo_qconnect.types.quick_response_type
    import capo_qconnect.types.recommendation_id_list
    import capo_qconnect.types.recommendation_type
    import capo_qconnect.types.remove_assistant_ai_agent_request
    import capo_qconnect.types.remove_assistant_ai_agent_response
    import capo_qconnect.types.remove_knowledge_base_template_uri_request
    import capo_qconnect.types.remove_knowledge_base_template_uri_response
    import capo_qconnect.types.render_message_template_request
    import capo_qconnect.types.render_message_template_response
    import capo_qconnect.types.rendering_configuration
    import capo_qconnect.types.result_data
    import capo_qconnect.types.retrieval_configuration
    import capo_qconnect.types.retrieve_request
    import capo_qconnect.types.retrieve_response
    import capo_qconnect.types.runtime_session_data_list
    import capo_qconnect.types.search_content_request
    import capo_qconnect.types.search_content_response
    import capo_qconnect.types.search_expression
    import capo_qconnect.types.search_message_templates_request
    import capo_qconnect.types.search_message_templates_response
    import capo_qconnect.types.search_quick_responses_request
    import capo_qconnect.types.search_quick_responses_response
    import capo_qconnect.types.search_sessions_request
    import capo_qconnect.types.search_sessions_response
    import capo_qconnect.types.send_message_request
    import capo_qconnect.types.send_message_response
    import capo_qconnect.types.server_side_encryption_configuration
    import capo_qconnect.types.session_data_namespace
    import capo_qconnect.types.session_summary
    import capo_qconnect.types.short_cut_key
    import capo_qconnect.types.source_configuration
    import capo_qconnect.types.span
    import capo_qconnect.types.start_content_upload_request
    import capo_qconnect.types.start_content_upload_response
    import capo_qconnect.types.start_import_job_request
    import capo_qconnect.types.start_import_job_response
    import capo_qconnect.types.tag_filter
    import capo_qconnect.types.tag_key_list
    import capo_qconnect.types.tag_resource_request
    import capo_qconnect.types.tag_resource_response
    import capo_qconnect.types.tags
    import capo_qconnect.types.target_type
    import capo_qconnect.types.time_to_live
    import capo_qconnect.types.untag_resource_request
    import capo_qconnect.types.untag_resource_response
    import capo_qconnect.types.update_ai_agent_request
    import capo_qconnect.types.update_ai_agent_response
    import capo_qconnect.types.update_ai_guardrail_request
    import capo_qconnect.types.update_ai_guardrail_response
    import capo_qconnect.types.update_ai_prompt_request
    import capo_qconnect.types.update_ai_prompt_response
    import capo_qconnect.types.update_assistant_ai_agent_request
    import capo_qconnect.types.update_assistant_ai_agent_response
    import capo_qconnect.types.update_content_request
    import capo_qconnect.types.update_content_response
    import capo_qconnect.types.update_knowledge_base_template_uri_request
    import capo_qconnect.types.update_knowledge_base_template_uri_response
    import capo_qconnect.types.update_message_template_metadata_request
    import capo_qconnect.types.update_message_template_metadata_response
    import capo_qconnect.types.update_message_template_request
    import capo_qconnect.types.update_message_template_response
    import capo_qconnect.types.update_quick_response_request
    import capo_qconnect.types.update_quick_response_response
    import capo_qconnect.types.update_session_data_request
    import capo_qconnect.types.update_session_data_response
    import capo_qconnect.types.update_session_request
    import capo_qconnect.types.update_session_response
    import capo_qconnect.types.upload_id
    import capo_qconnect.types.uri
    import capo_qconnect.types.uuid
    import capo_qconnect.types.uuid_or_arn
    import capo_qconnect.types.uuid_or_arn_or_either_with_qualifier
    import capo_qconnect.types.vector_ingestion_configuration
    import capo_qconnect.types.version
    import capo_qconnect.types.visibility_status
    import capo_qconnect.types.wait_time_seconds


class AsyncQConnectClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncQConnectClient:
    """A client for the ``QConnect`` service.

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
        self._config = AsyncQConnectClientConfig(
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

        # resources
        self.assistant = AsyncAssistant(self)
        self.knowledge_base = AsyncKnowledgeBase(self)

    def operation_options(
        self, config_overrides: Optional[AsyncQConnectClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncQConnectClientConfig = config_overrides or {}
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

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_qconnect.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_qconnect.types.arn.Arn",
        tags: "capo_qconnect.types.tags.Tags",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tags to the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.too_many_tags_exception.TooManyTagsException: <p>Amazon Q in Connect throws this exception if you have too many tags in your tag set.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_qconnect.types.arn.Arn",
        tag_keys: "capo_qconnect.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>
            tag_keys: <p>The tag keys.</p>

        Raises:
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_assistant(
        self,
        name: "capo_qconnect.types.name.Name",
        type: "capo_qconnect.types.assistant_type.AssistantType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
        server_side_encryption_configuration: Optional[
            "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.create_assistant_response.CreateAssistantResponse":
        """<p>Creates an Amazon Q in Connect assistant.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the assistant.</p>
            type: <p>The type of assistant.</p>
            description: <p>The description of the assistant.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>The customer managed key must have a policy that allows <code>kms:CreateGrant</code>, <code> kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect. To use Amazon Q in Connect with chat, the key policy must also allow <code>kms:Decrypt</code>, <code>kms:GenerateDataKey*</code>, and <code>kms:DescribeKey</code> permissions to the <code>connect.amazonaws.com</code> service principal. </p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_assistant_request.CreateAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_assistant_response.CreateAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_assistant.async_create_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_assistant_request.CreateAssistantRequest = {
            "name": name,
            "type": type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_assistant(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_assistant_response.GetAssistantResponse":
        """<p>Retrieves information about an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_assistant_request.GetAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_assistant_response.GetAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_assistant.async_get_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_assistant_request.GetAssistantRequest = {
            "assistant_id": assistant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_assistant(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_assistant_response.DeleteAssistantResponse":
        """<p>Deletes an assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_assistant_request.DeleteAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_assistant_response.DeleteAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_assistant.async_delete_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_assistant_request.DeleteAssistantRequest = {
            "assistant_id": assistant_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_assistants(
        self,
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_assistants_response.ListAssistantsResponse":
        """<p>Lists information about assistants.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_assistants_request.ListAssistantsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_assistants_response.ListAssistantsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_assistants

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_assistants.async_list_assistants(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_assistants_request.ListAssistantsRequest = {}
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

    async def iter_list_assistants(
        self,
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.assistant_summary.AssistantSummary]":
        _token = next_token
        while True:
            _response = await self.list_assistants(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("assistant_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_recommendations(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        wait_time_seconds: Optional[
            "capo_qconnect.types.wait_time_seconds.WaitTimeSeconds"
        ] = None,
        next_chunk_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        recommendation_type: Optional[
            "capo_qconnect.types.recommendation_type.RecommendationType"
        ] = None,
    ) -> "capo_qconnect.types.get_recommendations_response.GetRecommendationsResponse":
        """<important> <p>This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.</p> </important> <p>Retrieves recommendations for the specified session. To avoid retrieving the same recommendations in subsequent calls, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_NotifyRecommendationsReceived.html">NotifyRecommendationsReceived</a>. This API supports long-polling behavior with the <code>waitTimeSeconds</code> parameter. Short poll is the default behavior and only returns recommendations already available. To perform a manual query against an assistant, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_QueryAssistant.html">QueryAssistant</a>.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            wait_time_seconds: <p>The duration (in seconds) for which the call waits for a recommendation to be made available before returning. If a recommendation is available, the call returns sooner than <code>WaitTimeSeconds</code>. If no messages are available and the wait time expires, the call returns successfully with an empty list.</p>
            next_chunk_token: <p>The token for the next set of chunks. Use the value returned in the previous response in the next request to retrieve the next set of chunks.</p>
            recommendation_type: <p>The type of recommendation being requested.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_recommendations_request.GetRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_recommendations_response.GetRecommendationsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_recommendations

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_recommendations.async_get_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_recommendations_request.GetRecommendationsRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if wait_time_seconds is not None:
            input_["wait_time_seconds"] = wait_time_seconds
        if next_chunk_token is not None:
            input_["next_chunk_token"] = next_chunk_token
        if recommendation_type is not None:
            input_["recommendation_type"] = recommendation_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_models(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        ai_prompt_type: Optional[
            "capo_qconnect.types.ai_prompt_type.AIPromptType"
        ] = None,
        model_lifecycle: Optional[
            "capo_qconnect.types.model_lifecycle.ModelLifecycle"
        ] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_models_response.ListModelsResponse":
        """<p>Lists the models available to an Amazon Q in Connect assistant in the assistant's Amazon Web Services Region. The available models are determined by the region of the specified assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN. The assistant's region determines which models are available.</p>
            ai_prompt_type: <p>The type of the AI Prompt to filter models by. When specified, only models that support the given AI Prompt type are returned.</p>
            model_lifecycle: <p>The lifecycle status of models to filter by. When specified, only models with the given lifecycle status are returned.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_models_request.ListModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_models_response.ListModelsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_models

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_models.async_list_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_models_request.ListModelsRequest = {
            "assistant_id": assistant_id
        }
        if ai_prompt_type is not None:
            input_["ai_prompt_type"] = ai_prompt_type
        if model_lifecycle is not None:
            input_["model_lifecycle"] = model_lifecycle
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

    async def iter_list_models(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        ai_prompt_type: Optional[
            "capo_qconnect.types.ai_prompt_type.AIPromptType"
        ] = None,
        model_lifecycle: Optional[
            "capo_qconnect.types.model_lifecycle.ModelLifecycle"
        ] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.model_summary.ModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_models(
                assistant_id,
                config_overrides=config_overrides,
                ai_prompt_type=ai_prompt_type,
                model_lifecycle=model_lifecycle,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def notify_recommendations_received(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        recommendation_ids: "capo_qconnect.types.recommendation_id_list.RecommendationIdList",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse":
        """<p>Removes the specified recommendations from the specified assistant's queue of newly available recommendations. You can use this API in conjunction with <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a> and a <code>waitTimeSeconds</code> input for long-polling behavior and avoiding duplicate recommendations.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            recommendation_ids: <p>The identifiers of the recommendations.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.notify_recommendations_received_response.NotifyRecommendationsReceivedResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.notify_recommendations_received

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.notify_recommendations_received.async_notify_recommendations_received(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.notify_recommendations_received_request.NotifyRecommendationsReceivedRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
            "recommendation_ids": recommendation_ids,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_feedback(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        target_id: "capo_qconnect.types.uuid.Uuid",
        target_type: "capo_qconnect.types.target_type.TargetType",
        content_feedback: "capo_qconnect.types.content_feedback_data.ContentFeedbackData",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.put_feedback_response.PutFeedbackResponse":
        """<p>Provides feedback against the specified assistant for the specified target. This API only supports generative targets.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant.</p>
            target_id: <p>The identifier of the feedback target.</p>
            target_type: <p>The type of the feedback target.</p>
            content_feedback: <p>Information about the feedback provided.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.put_feedback_request.PutFeedbackRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.put_feedback_response.PutFeedbackResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.put_feedback

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.put_feedback.async_put_feedback(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.put_feedback_request.PutFeedbackRequest = {
            "assistant_id": assistant_id,
            "target_id": target_id,
            "target_type": target_type,
            "content_feedback": content_feedback,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def query_assistant(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        query_text: Optional["capo_qconnect.types.query_text.QueryText"] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        session_id: Optional["capo_qconnect.types.uuid_or_arn.UuidOrArn"] = None,
        query_condition: Optional[
            "capo_qconnect.types.query_condition_expression.QueryConditionExpression"
        ] = None,
        query_input_data: Optional[
            "capo_qconnect.types.query_input_data.QueryInputData"
        ] = None,
        override_knowledge_base_search_type: Optional[
            "capo_qconnect.types.knowledge_base_search_type.KnowledgeBaseSearchType"
        ] = None,
    ) -> "capo_qconnect.types.query_assistant_response.QueryAssistantResponse":
        """<important> <p>This API will be discontinued starting June 1, 2024. To receive generative responses after March 1, 2024, you will need to create a new Assistant in the Connect Customer console and integrate the Amazon Q in Connect JavaScript library (amazon-q-connectjs) into your applications.</p> </important> <p>Performs a manual search against the specified assistant. To retrieve recommendations for an assistant, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetRecommendations.html">GetRecommendations</a>. </p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_text: <p>The text to search for.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            session_id: <p>The identifier of the Amazon Q in Connect session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            query_condition: <p>Information about how to query content.</p>
            query_input_data: <p>Information about the query.</p>
            override_knowledge_base_search_type: <p>The search type to be used against the Knowledge Base for this request. The values can be <code>SEMANTIC</code> which uses vector embeddings or <code>HYBRID</code> which use vector embeddings and raw text.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.query_assistant_request.QueryAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.query_assistant_response.QueryAssistantResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.query_assistant

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.query_assistant.async_query_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.query_assistant_request.QueryAssistantRequest = {
            "assistant_id": assistant_id
        }
        if query_text is not None:
            input_["query_text"] = query_text
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if session_id is not None:
            input_["session_id"] = session_id
        if query_condition is not None:
            input_["query_condition"] = query_condition
        if query_input_data is not None:
            input_["query_input_data"] = query_input_data
        if override_knowledge_base_search_type is not None:
            input_["override_knowledge_base_search_type"] = (
                override_knowledge_base_search_type
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_query_assistant(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        query_text: Optional["capo_qconnect.types.query_text.QueryText"] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        session_id: Optional["capo_qconnect.types.uuid_or_arn.UuidOrArn"] = None,
        query_condition: Optional[
            "capo_qconnect.types.query_condition_expression.QueryConditionExpression"
        ] = None,
        query_input_data: Optional[
            "capo_qconnect.types.query_input_data.QueryInputData"
        ] = None,
        override_knowledge_base_search_type: Optional[
            "capo_qconnect.types.knowledge_base_search_type.KnowledgeBaseSearchType"
        ] = None,
    ) -> "AsyncIterator[capo_qconnect.types.result_data.ResultData]":
        _token = next_token
        while True:
            _response = await self.query_assistant(
                assistant_id,
                config_overrides=config_overrides,
                query_text=query_text,
                next_token=_token,
                max_results=max_results,
                session_id=session_id,
                query_condition=query_condition,
                query_input_data=query_input_data,
                override_knowledge_base_search_type=override_knowledge_base_search_type,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def remove_assistant_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        orchestrator_use_case: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_qconnect.types.remove_assistant_ai_agent_response.RemoveAssistantAIAgentResponse":
        """<p>Removes the AI Agent that is set for use by default on an Amazon Q in Connect Assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_type: <p>The type of the AI Agent being removed for use by default from the Amazon Q in Connect Assistant.</p>
            orchestrator_use_case: <p>The orchestrator use case for the AI Agent being removed.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.remove_assistant_ai_agent_request.RemoveAssistantAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.remove_assistant_ai_agent_response.RemoveAssistantAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.remove_assistant_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.remove_assistant_ai_agent.async_remove_assistant_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.remove_assistant_ai_agent_request.RemoveAssistantAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_type": ai_agent_type,
        }
        if orchestrator_use_case is not None:
            input_["orchestrator_use_case"] = orchestrator_use_case

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def retrieve(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        retrieval_configuration: "capo_qconnect.types.retrieval_configuration.RetrievalConfiguration",
        retrieval_query: "capo_qconnect.types.non_empty_sensitive_string.NonEmptySensitiveString",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.retrieve_response.RetrieveResponse":
        """<p>Retrieves content from knowledge sources based on a query.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant for content retrieval.</p>
            retrieval_configuration: <p>The configuration for the content retrieval operation.</p>
            retrieval_query: <p>The query for content retrieval.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.dependency_failed_exception.DependencyFailedException: <p>The request failed because it depends on another request that failed.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.retrieve_request.RetrieveRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.retrieve_response.RetrieveResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.retrieve

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.retrieve.async_retrieve(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.retrieve_request.RetrieveRequest = {
            "assistant_id": assistant_id,
            "retrieval_configuration": retrieval_configuration,
            "retrieval_query": retrieval_query,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_sessions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_sessions_response.SearchSessionsResponse":
        """<p>Searches for sessions.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_sessions_request.SearchSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_sessions_response.SearchSessionsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_sessions

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_sessions.async_search_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.search_sessions_request.SearchSessionsRequest = {
            "assistant_id": assistant_id,
            "search_expression": search_expression,
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

    async def iter_search_sessions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = await self.search_sessions(
                assistant_id,
                search_expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("session_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_assistant_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_type: "capo_qconnect.types.ai_agent_type.AIAgentType",
        configuration: "capo_qconnect.types.ai_agent_configuration_data.AIAgentConfigurationData",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        orchestrator_use_case: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_qconnect.types.update_assistant_ai_agent_response.UpdateAssistantAIAgentResponse":
        """<p>Updates the AI Agent that is set for use by default on an Amazon Q in Connect Assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_type: <p>The type of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>
            configuration: <p>The configuration of the AI Agent being updated for use by default on the Amazon Q in Connect Assistant.</p>
            orchestrator_use_case: <p>The orchestrator use case for the AI Agent being added.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_assistant_ai_agent_request.UpdateAssistantAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_assistant_ai_agent_response.UpdateAssistantAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_assistant_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_assistant_ai_agent.async_update_assistant_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_assistant_ai_agent_request.UpdateAssistantAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_type": ai_agent_type,
            "configuration": configuration,
        }
        if orchestrator_use_case is not None:
            input_["orchestrator_use_case"] = orchestrator_use_case

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        name: "capo_qconnect.types.name.Name",
        type: "capo_qconnect.types.ai_agent_type.AIAgentType",
        configuration: "capo_qconnect.types.ai_agent_configuration.AIAgentConfiguration",
        visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
    ) -> "capo_qconnect.types.create_ai_agent_response.CreateAIAgentResponse":
        """<p>Creates an Amazon Q in Connect AI Agent.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the AI Agent.</p>
            type: <p>The type of the AI Agent.</p>
            configuration: <p>The configuration of the AI Agent.</p>
            visibility_status: <p>The visibility status of the AI Agent.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            description: <p>The description of the AI Agent.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_ai_agent_request.CreateAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_ai_agent_response.CreateAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_ai_agent.async_create_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_ai_agent_request.CreateAIAgentRequest = {
            "assistant_id": assistant_id,
            "name": name,
            "type": type,
            "configuration": configuration,
            "visibility_status": visibility_status,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_ai_agent_response.GetAIAgentResponse":
        """<p>Gets an Amazon Q in Connect AI Agent.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_id: <p>The identifier of the Amazon Q in Connect AI Agent (with or without a version qualifier). Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_ai_agent_request.GetAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_ai_agent_response.GetAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_ai_agent.async_get_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_ai_agent_request.GetAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_id": ai_agent_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        configuration: Optional[
            "capo_qconnect.types.ai_agent_configuration.AIAgentConfiguration"
        ] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
    ) -> "capo_qconnect.types.update_ai_agent_response.UpdateAIAgentResponse":
        """<p>Updates an AI Agent.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_id: <p>The identifier of the Amazon Q in Connect AI Agent.</p>
            visibility_status: <p>The visbility status of the Amazon Q in Connect AI Agent.</p>
            configuration: <p>The configuration of the Amazon Q in Connect AI Agent.</p>
            description: <p>The description of the Amazon Q in Connect AI Agent.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_ai_agent_request.UpdateAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_ai_agent_response.UpdateAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_ai_agent.async_update_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_ai_agent_request.UpdateAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_id": ai_agent_id,
            "visibility_status": visibility_status,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if configuration is not None:
            input_["configuration"] = configuration
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ai_agent(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_ai_agent_response.DeleteAIAgentResponse":
        """<p>Deletes an Amazon Q in Connect AI Agent.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_id: <p>The identifier of the Amazon Q in Connect AI Agent. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_ai_agent_request.DeleteAIAgentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_ai_agent_response.DeleteAIAgentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_ai_agent

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_ai_agent.async_delete_ai_agent(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_ai_agent_request.DeleteAIAgentRequest = {
            "assistant_id": assistant_id,
            "ai_agent_id": ai_agent_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ai_agents(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "capo_qconnect.types.list_ai_agents_response.ListAIAgentsResponse":
        """<p>Lists AI Agents.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            origin: <p>The origin of the AI Agents to be listed. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_ai_agents_request.ListAIAgentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_ai_agents_response.ListAIAgentsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_ai_agents

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_ai_agents.async_list_ai_agents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_ai_agents_request.ListAIAgentsRequest = {
            "assistant_id": assistant_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if origin is not None:
            input_["origin"] = origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_ai_agents(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.ai_agent_summary.AIAgentSummary]":
        _token = next_token
        while True:
            _response = await self.list_ai_agents(
                assistant_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                origin=origin,
            )
            _page = _resolve_path(_response, ("ai_agent_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_ai_agent_version(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        modified_time: Optional[datetime.datetime] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
    ) -> "capo_qconnect.types.create_ai_agent_version_response.CreateAIAgentVersionResponse":
        """<p>Creates and Amazon Q in Connect AI Agent version.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_id: <p>The identifier of the Amazon Q in Connect AI Agent.</p>
            modified_time: <p>The modification time of the AI Agent should be tracked for version creation. This field should be specified to avoid version creation when simultaneous update to the underlying AI Agent are possible. The value should be the modifiedTime returned from the request to create or update an AI Agent so that version creation can fail if an update to the AI Agent post the specified modification time has been made.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_ai_agent_version_request.CreateAIAgentVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_ai_agent_version_response.CreateAIAgentVersionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_ai_agent_version

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_ai_agent_version.async_create_ai_agent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_ai_agent_version_request.CreateAIAgentVersionRequest = {
            "assistant_id": assistant_id,
            "ai_agent_id": ai_agent_id,
        }
        if modified_time is not None:
            input_["modified_time"] = modified_time
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

    async def delete_ai_agent_version(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        version_number: "capo_qconnect.types.version.Version",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_ai_agent_version_response.DeleteAIAgentVersionResponse":
        """<p>Deletes an Amazon Q in Connect AI Agent Version.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_id: <p>The identifier of the Amazon Q in Connect AI Agent. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            version_number: <p>The version number of the AI Agent version.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_ai_agent_version_request.DeleteAIAgentVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_ai_agent_version_response.DeleteAIAgentVersionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_ai_agent_version

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_ai_agent_version.async_delete_ai_agent_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_ai_agent_version_request.DeleteAIAgentVersionRequest = {
            "assistant_id": assistant_id,
            "ai_agent_id": ai_agent_id,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ai_agent_versions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "capo_qconnect.types.list_ai_agent_versions_response.ListAIAgentVersionsResponse":
        """<p>List AI Agent versions.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_agent_id: <p>The identifier of the Amazon Q in Connect AI Agent for which versions are to be listed.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            origin: <p>The origin of the AI Agent versions to be listed. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_ai_agent_versions_request.ListAIAgentVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_ai_agent_versions_response.ListAIAgentVersionsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_ai_agent_versions

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_ai_agent_versions.async_list_ai_agent_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_ai_agent_versions_request.ListAIAgentVersionsRequest = {
            "assistant_id": assistant_id,
            "ai_agent_id": ai_agent_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if origin is not None:
            input_["origin"] = origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_ai_agent_versions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_agent_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.ai_agent_version_summary.AIAgentVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_ai_agent_versions(
                assistant_id,
                ai_agent_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                origin=origin,
            )
            _page = _resolve_path(_response, ("ai_agent_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_ai_guardrail(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        name: "capo_qconnect.types.name.Name",
        blocked_input_messaging: "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging",
        visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        description: Optional[
            "capo_qconnect.types.ai_guardrail_description.AIGuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_topic_policy_config.AIGuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_content_policy_config.AIGuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_word_policy_config.AIGuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_sensitive_information_policy_config.AIGuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config.AIGuardrailContextualGroundingPolicyConfig"
        ] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> "capo_qconnect.types.create_ai_guardrail_response.CreateAIGuardrailResponse":
        """<p>Creates an Amazon Q in Connect AI Guardrail.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the AI Guardrail.</p>
            blocked_input_messaging: <p>The message to return when the AI Guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the AI Guardrail blocks a model response.</p>
            visibility_status: <p>The visibility status of the AI Guardrail.</p>
            description: <p>A description of the AI Guardrail.</p>
            topic_policy_config: <p>The topic policies to configure for the AI Guardrail.</p>
            content_policy_config: <p>The content filter policies to configure for the AI Guardrail.</p>
            word_policy_config: <p>The word policy you configure for the AI Guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the AI Guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to create an AI Guardrail.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_ai_guardrail_request.CreateAIGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_ai_guardrail_response.CreateAIGuardrailResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_ai_guardrail

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_ai_guardrail.async_create_ai_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_ai_guardrail_request.CreateAIGuardrailRequest = {
            "assistant_id": assistant_id,
            "name": name,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
            "visibility_status": visibility_status,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if topic_policy_config is not None:
            input_["topic_policy_config"] = topic_policy_config
        if content_policy_config is not None:
            input_["content_policy_config"] = content_policy_config
        if word_policy_config is not None:
            input_["word_policy_config"] = word_policy_config
        if sensitive_information_policy_config is not None:
            input_["sensitive_information_policy_config"] = (
                sensitive_information_policy_config
            )
        if contextual_grounding_policy_config is not None:
            input_["contextual_grounding_policy_config"] = (
                contextual_grounding_policy_config
            )
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ai_guardrail(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_ai_guardrail_response.GetAIGuardrailResponse":
        """<p>Gets the Amazon Q in Connect AI Guardrail.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_guardrail_id: <p>The identifier of the Amazon Q in Connect AI Guardrail.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_ai_guardrail_request.GetAIGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_ai_guardrail_response.GetAIGuardrailResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_ai_guardrail

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_ai_guardrail.async_get_ai_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_ai_guardrail_request.GetAIGuardrailRequest = {
            "assistant_id": assistant_id,
            "ai_guardrail_id": ai_guardrail_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ai_guardrail(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus",
        blocked_input_messaging: "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_qconnect.types.ai_guardrail_blocked_messaging.AIGuardrailBlockedMessaging",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        description: Optional[
            "capo_qconnect.types.ai_guardrail_description.AIGuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_topic_policy_config.AIGuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_content_policy_config.AIGuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_word_policy_config.AIGuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_sensitive_information_policy_config.AIGuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_qconnect.types.ai_guardrail_contextual_grounding_policy_config.AIGuardrailContextualGroundingPolicyConfig"
        ] = None,
    ) -> "capo_qconnect.types.update_ai_guardrail_response.UpdateAIGuardrailResponse":
        """<p>Updates an AI Guardrail.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_guardrail_id: <p>The identifier of the Amazon Q in Connect AI Guardrail.</p>
            visibility_status: <p>The visibility status of the Amazon Q in Connect AI Guardrail.</p>
            blocked_input_messaging: <p>The message to return when the AI Guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the AI Guardrail blocks a model response.</p>
            description: <p>A description of the AI Guardrail.</p>
            topic_policy_config: <p>The topic policies to configure for the AI Guardrail.</p>
            content_policy_config: <p>The content filter policies to configure for the AI Guardrail.</p>
            word_policy_config: <p>The word policy you configure for the AI Guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the AI Guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to create an AI Guardrail.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_ai_guardrail_request.UpdateAIGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_ai_guardrail_response.UpdateAIGuardrailResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_ai_guardrail

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_ai_guardrail.async_update_ai_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_ai_guardrail_request.UpdateAIGuardrailRequest = {
            "assistant_id": assistant_id,
            "ai_guardrail_id": ai_guardrail_id,
            "visibility_status": visibility_status,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if topic_policy_config is not None:
            input_["topic_policy_config"] = topic_policy_config
        if content_policy_config is not None:
            input_["content_policy_config"] = content_policy_config
        if word_policy_config is not None:
            input_["word_policy_config"] = word_policy_config
        if sensitive_information_policy_config is not None:
            input_["sensitive_information_policy_config"] = (
                sensitive_information_policy_config
            )
        if contextual_grounding_policy_config is not None:
            input_["contextual_grounding_policy_config"] = (
                contextual_grounding_policy_config
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ai_guardrail(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_ai_guardrail_response.DeleteAIGuardrailResponse":
        """<p>Deletes an Amazon Q in Connect AI Guardrail.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_guardrail_id: <p>The identifier of the Amazon Q in Connect AI Guardrail. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_ai_guardrail_request.DeleteAIGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_ai_guardrail_response.DeleteAIGuardrailResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_ai_guardrail

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_ai_guardrail.async_delete_ai_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_ai_guardrail_request.DeleteAIGuardrailRequest = {
            "assistant_id": assistant_id,
            "ai_guardrail_id": ai_guardrail_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ai_guardrails(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_ai_guardrails_response.ListAIGuardrailsResponse":
        """<p>Lists the AI Guardrails available on the Amazon Q in Connect assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_ai_guardrails_request.ListAIGuardrailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_ai_guardrails_response.ListAIGuardrailsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_ai_guardrails

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_ai_guardrails.async_list_ai_guardrails(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_ai_guardrails_request.ListAIGuardrailsRequest = {
            "assistant_id": assistant_id
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

    async def iter_list_ai_guardrails(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.ai_guardrail_summary.AIGuardrailSummary]":
        _token = next_token
        while True:
            _response = await self.list_ai_guardrails(
                assistant_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("ai_guardrail_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_ai_guardrail_version(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        modified_time: Optional[datetime.datetime] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
    ) -> "capo_qconnect.types.create_ai_guardrail_version_response.CreateAIGuardrailVersionResponse":
        """<p>Creates an Amazon Q in Connect AI Guardrail version.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_guardrail_id: <p>The identifier of the Amazon Q in Connect AI Guardrail.</p>
            modified_time: <p>The time the AI Guardrail was last modified.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_ai_guardrail_version_request.CreateAIGuardrailVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_ai_guardrail_version_response.CreateAIGuardrailVersionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_ai_guardrail_version

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_ai_guardrail_version.async_create_ai_guardrail_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_ai_guardrail_version_request.CreateAIGuardrailVersionRequest = {
            "assistant_id": assistant_id,
            "ai_guardrail_id": ai_guardrail_id,
        }
        if modified_time is not None:
            input_["modified_time"] = modified_time
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

    async def delete_ai_guardrail_version(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        version_number: "capo_qconnect.types.version.Version",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_ai_guardrail_version_response.DeleteAIGuardrailVersionResponse":
        """<p>Delete and Amazon Q in Connect AI Guardrail version.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_guardrail_id: <p>The identifier of the Amazon Q in Connect AI Guardrail.</p>
            version_number: <p>The version number of the AI Guardrail version to be deleted.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_ai_guardrail_version_request.DeleteAIGuardrailVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_ai_guardrail_version_response.DeleteAIGuardrailVersionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_ai_guardrail_version

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_ai_guardrail_version.async_delete_ai_guardrail_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_ai_guardrail_version_request.DeleteAIGuardrailVersionRequest = {
            "assistant_id": assistant_id,
            "ai_guardrail_id": ai_guardrail_id,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ai_guardrail_versions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_ai_guardrail_versions_response.ListAIGuardrailVersionsResponse":
        """<p>Lists AI Guardrail versions.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_guardrail_id: <p>The identifier of the Amazon Q in Connect AI Guardrail for which versions are to be listed.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_ai_guardrail_versions_request.ListAIGuardrailVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_ai_guardrail_versions_response.ListAIGuardrailVersionsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_ai_guardrail_versions

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_ai_guardrail_versions.async_list_ai_guardrail_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_ai_guardrail_versions_request.ListAIGuardrailVersionsRequest = {
            "assistant_id": assistant_id,
            "ai_guardrail_id": ai_guardrail_id,
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

    async def iter_list_ai_guardrail_versions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_guardrail_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.ai_guardrail_version_summary.AIGuardrailVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_ai_guardrail_versions(
                assistant_id,
                ai_guardrail_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("ai_guardrail_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_ai_prompt(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        name: "capo_qconnect.types.name.Name",
        type: "capo_qconnect.types.ai_prompt_type.AIPromptType",
        template_configuration: "capo_qconnect.types.ai_prompt_template_configuration.AIPromptTemplateConfiguration",
        visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus",
        template_type: "capo_qconnect.types.ai_prompt_template_type.AIPromptTemplateType",
        model_id: "capo_qconnect.types.ai_prompt_model_identifier.AIPromptModelIdentifier",
        api_format: "capo_qconnect.types.ai_prompt_api_format.AIPromptAPIFormat",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        inference_configuration: Optional[
            "capo_qconnect.types.ai_prompt_inference_configuration.AIPromptInferenceConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.create_ai_prompt_response.CreateAIPromptResponse":
        """<p>Creates an Amazon Q in Connect AI Prompt.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the AI Prompt.</p>
            type: <p>The type of this AI Prompt.</p>
            template_configuration: <p>The configuration of the prompt template for this AI Prompt.</p>
            visibility_status: <p>The visibility status of the AI Prompt.</p>
            template_type: <p>The type of the prompt template for this AI Prompt.</p>
            model_id: <p>The identifier of the model used for this AI Prompt.</p> <note> <p>For information about which models are supported in each Amazon Web Services Region, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-ai-prompts.html#cli-create-aiprompt">Supported models for system/custom prompts</a>.</p> </note>
            api_format: <p>The API Format of the AI Prompt.</p> <p>Recommended values: <code>MESSAGES | TEXT_COMPLETIONS</code> </p> <note> <p>The values <code>ANTHROPIC_CLAUDE_MESSAGES | ANTHROPIC_CLAUDE_TEXT_COMPLETIONS</code> will be deprecated.</p> </note>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            description: <p>The description of the AI Prompt.</p>
            inference_configuration: <p>The inference configuration for the AI Prompt being created.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_ai_prompt_request.CreateAIPromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_ai_prompt_response.CreateAIPromptResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_ai_prompt

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_ai_prompt.async_create_ai_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_ai_prompt_request.CreateAIPromptRequest = {
            "assistant_id": assistant_id,
            "name": name,
            "type": type,
            "template_configuration": template_configuration,
            "visibility_status": visibility_status,
            "template_type": template_type,
            "model_id": model_id,
            "api_format": api_format,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if description is not None:
            input_["description"] = description
        if inference_configuration is not None:
            input_["inference_configuration"] = inference_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ai_prompt(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_ai_prompt_response.GetAIPromptResponse":
        """<p>Gets and Amazon Q in Connect AI Prompt.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_prompt_id: <p>The identifier of the Amazon Q in Connect AI prompt.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_ai_prompt_request.GetAIPromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_ai_prompt_response.GetAIPromptResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_ai_prompt

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_ai_prompt.async_get_ai_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_ai_prompt_request.GetAIPromptRequest = {
            "assistant_id": assistant_id,
            "ai_prompt_id": ai_prompt_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ai_prompt(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        visibility_status: "capo_qconnect.types.visibility_status.VisibilityStatus",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        template_configuration: Optional[
            "capo_qconnect.types.ai_prompt_template_configuration.AIPromptTemplateConfiguration"
        ] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        model_id: Optional[
            "capo_qconnect.types.ai_prompt_model_identifier.AIPromptModelIdentifier"
        ] = None,
        inference_configuration: Optional[
            "capo_qconnect.types.ai_prompt_inference_configuration.AIPromptInferenceConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.update_ai_prompt_response.UpdateAIPromptResponse":
        """<p>Updates an AI Prompt.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_prompt_id: <p>The identifier of the Amazon Q in Connect AI Prompt.</p>
            visibility_status: <p>The visibility status of the Amazon Q in Connect AI prompt.</p>
            template_configuration: <p>The configuration of the prompt template for this AI Prompt.</p>
            description: <p>The description of the Amazon Q in Connect AI Prompt.</p>
            model_id: <p>The identifier of the model used for this AI Prompt.</p> <note> <p>For information about which models are supported in each Amazon Web Services Region, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/create-ai-prompts.html#cli-create-aiprompt">Supported models for system/custom prompts</a>.</p> </note>
            inference_configuration: <p>The updated inference configuration for the AI Prompt.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_ai_prompt_request.UpdateAIPromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_ai_prompt_response.UpdateAIPromptResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_ai_prompt

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_ai_prompt.async_update_ai_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_ai_prompt_request.UpdateAIPromptRequest = {
            "assistant_id": assistant_id,
            "ai_prompt_id": ai_prompt_id,
            "visibility_status": visibility_status,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if template_configuration is not None:
            input_["template_configuration"] = template_configuration
        if description is not None:
            input_["description"] = description
        if model_id is not None:
            input_["model_id"] = model_id
        if inference_configuration is not None:
            input_["inference_configuration"] = inference_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ai_prompt(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_ai_prompt_response.DeleteAIPromptResponse":
        """<p>Deletes an Amazon Q in Connect AI Prompt.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_prompt_id: <p>The identifier of the Amazon Q in Connect AI prompt. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_ai_prompt_request.DeleteAIPromptRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_ai_prompt_response.DeleteAIPromptResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_ai_prompt

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_ai_prompt.async_delete_ai_prompt(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_ai_prompt_request.DeleteAIPromptRequest = {
            "assistant_id": assistant_id,
            "ai_prompt_id": ai_prompt_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ai_prompts(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "capo_qconnect.types.list_ai_prompts_response.ListAIPromptsResponse":
        """<p>Lists the AI Prompts available on the Amazon Q in Connect assistant.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            origin: <p>The origin of the AI Prompts to be listed. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_ai_prompts_request.ListAIPromptsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_ai_prompts_response.ListAIPromptsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_ai_prompts

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_ai_prompts.async_list_ai_prompts(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_ai_prompts_request.ListAIPromptsRequest = {
            "assistant_id": assistant_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if origin is not None:
            input_["origin"] = origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_ai_prompts(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.ai_prompt_summary.AIPromptSummary]":
        _token = next_token
        while True:
            _response = await self.list_ai_prompts(
                assistant_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                origin=origin,
            )
            _page = _resolve_path(_response, ("ai_prompt_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_ai_prompt_version(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        modified_time: Optional[datetime.datetime] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
    ) -> "capo_qconnect.types.create_ai_prompt_version_response.CreateAIPromptVersionResponse":
        """<p>Creates an Amazon Q in Connect AI Prompt version.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_prompt_id: <p>The identifier of the Amazon Q in Connect AI prompt.</p>
            modified_time: <p>The time the AI Prompt was last modified.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>..</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_ai_prompt_version_request.CreateAIPromptVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_ai_prompt_version_response.CreateAIPromptVersionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_ai_prompt_version

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_ai_prompt_version.async_create_ai_prompt_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_ai_prompt_version_request.CreateAIPromptVersionRequest = {
            "assistant_id": assistant_id,
            "ai_prompt_id": ai_prompt_id,
        }
        if modified_time is not None:
            input_["modified_time"] = modified_time
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

    async def delete_ai_prompt_version(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        version_number: "capo_qconnect.types.version.Version",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_ai_prompt_version_response.DeleteAIPromptVersionResponse":
        """<p>Delete and Amazon Q in Connect AI Prompt version.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_prompt_id: <p>The identifier of the Amazon Q in Connect AI prompt.</p>
            version_number: <p>The version number of the AI Prompt version to be deleted.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_ai_prompt_version_request.DeleteAIPromptVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_ai_prompt_version_response.DeleteAIPromptVersionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_ai_prompt_version

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_ai_prompt_version.async_delete_ai_prompt_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_ai_prompt_version_request.DeleteAIPromptVersionRequest = {
            "assistant_id": assistant_id,
            "ai_prompt_id": ai_prompt_id,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_ai_prompt_versions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "capo_qconnect.types.list_ai_prompt_versions_response.ListAIPromptVersionsResponse":
        """<p>Lists AI Prompt versions.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            ai_prompt_id: <p>The identifier of the Amazon Q in Connect AI prompt for which versions are to be listed.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            origin: <p>The origin of the AI Prompt versions to be listed. <code>SYSTEM</code> for a default AI Agent created by Q in Connect or <code>CUSTOMER</code> for an AI Agent created by calling AI Agent creation APIs. </p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_ai_prompt_versions_request.ListAIPromptVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_ai_prompt_versions_response.ListAIPromptVersionsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_ai_prompt_versions

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_ai_prompt_versions.async_list_ai_prompt_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_ai_prompt_versions_request.ListAIPromptVersionsRequest = {
            "assistant_id": assistant_id,
            "ai_prompt_id": ai_prompt_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if origin is not None:
            input_["origin"] = origin

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_ai_prompt_versions(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        ai_prompt_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        origin: Optional["capo_qconnect.types.origin.Origin"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.ai_prompt_version_summary.AIPromptVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_ai_prompt_versions(
                assistant_id,
                ai_prompt_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                origin=origin,
            )
            _page = _resolve_path(_response, ("ai_prompt_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_assistant_association(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        association_type: "capo_qconnect.types.association_type.AssociationType",
        association: "capo_qconnect.types.assistant_association_input_data.AssistantAssociationInputData",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> "capo_qconnect.types.create_assistant_association_response.CreateAssistantAssociationResponse":
        """<p>Creates an association between an Amazon Q in Connect assistant and another resource. Currently, the only supported association is with a knowledge base. An assistant can have only a single association.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            association_type: <p>The type of association.</p>
            association: <p>The identifier of the associated resource.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_assistant_association_request.CreateAssistantAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_assistant_association_response.CreateAssistantAssociationResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_assistant_association

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_assistant_association.async_create_assistant_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_assistant_association_request.CreateAssistantAssociationRequest = {
            "assistant_id": assistant_id,
            "association_type": association_type,
            "association": association,
        }
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

    async def get_assistant_association(
        self,
        assistant_association_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_assistant_association_response.GetAssistantAssociationResponse":
        """<p>Retrieves information about an assistant association.</p>

        Args:
            assistant_association_id: <p>The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_assistant_association_request.GetAssistantAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_assistant_association_response.GetAssistantAssociationResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_assistant_association

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_assistant_association.async_get_assistant_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_assistant_association_request.GetAssistantAssociationRequest = {
            "assistant_association_id": assistant_association_id,
            "assistant_id": assistant_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_assistant_association(
        self,
        assistant_association_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_assistant_association_response.DeleteAssistantAssociationResponse":
        """<p>Deletes an assistant association.</p>

        Args:
            assistant_association_id: <p>The identifier of the assistant association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_assistant_association_request.DeleteAssistantAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_assistant_association_response.DeleteAssistantAssociationResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_assistant_association

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_assistant_association.async_delete_assistant_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_assistant_association_request.DeleteAssistantAssociationRequest = {
            "assistant_association_id": assistant_association_id,
            "assistant_id": assistant_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_assistant_associations(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_assistant_associations_response.ListAssistantAssociationsResponse":
        """<p>Lists information about assistant associations.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_assistant_associations_request.ListAssistantAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_assistant_associations_response.ListAssistantAssociationsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_assistant_associations

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_assistant_associations.async_list_assistant_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_assistant_associations_request.ListAssistantAssociationsRequest = {
            "assistant_id": assistant_id
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

    async def iter_list_assistant_associations(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.assistant_association_summary.AssistantAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_assistant_associations(
                assistant_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("assistant_association_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_session(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        name: "capo_qconnect.types.name.Name",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
        tag_filter: Optional["capo_qconnect.types.tag_filter.TagFilter"] = None,
        ai_agent_configuration: Optional[
            "capo_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
        ] = None,
        contact_arn: Optional["capo_qconnect.types.generic_arn.GenericArn"] = None,
        orchestrator_configuration_list: Optional[
            "capo_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
        ] = None,
        remove_orchestrator_configuration_list: Optional[bool] = None,
    ) -> "capo_qconnect.types.create_session_response.CreateSessionResponse":
        """<p>Creates a session. A session is a contextual container used for generating recommendations. Connect Customer creates a new Amazon Q in Connect session for each contact on which Amazon Q in Connect is enabled.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the session.</p>
            description: <p>The description.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>
            tag_filter: <p>An object that can be used to specify Tag conditions. </p>
            ai_agent_configuration: <p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.</p>
            contact_arn: <p>The Amazon Resource Name (ARN) of the email contact in Connect Customer. Used to retrieve email content and establish session context for AI-powered email assistance.</p>
            orchestrator_configuration_list: <p>The list of orchestrator configurations for the session being created.</p>
            remove_orchestrator_configuration_list: <p>The list of orchestrator configurations to remove from the session.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.dependency_failed_exception.DependencyFailedException: <p>The request failed because it depends on another request that failed.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_session_request.CreateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_session_response.CreateSessionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_session

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_session.async_create_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_session_request.CreateSessionRequest = {
            "assistant_id": assistant_id,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if tag_filter is not None:
            input_["tag_filter"] = tag_filter
        if ai_agent_configuration is not None:
            input_["ai_agent_configuration"] = ai_agent_configuration
        if contact_arn is not None:
            input_["contact_arn"] = contact_arn
        if orchestrator_configuration_list is not None:
            input_["orchestrator_configuration_list"] = orchestrator_configuration_list
        if remove_orchestrator_configuration_list is not None:
            input_["remove_orchestrator_configuration_list"] = (
                remove_orchestrator_configuration_list
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_session(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_session_response.GetSessionResponse":
        """<p>Retrieves information for a specified session.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_session_request.GetSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_session_response.GetSessionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_session

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_session.async_get_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_session_request.GetSessionRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
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
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tag_filter: Optional["capo_qconnect.types.tag_filter.TagFilter"] = None,
        ai_agent_configuration: Optional[
            "capo_qconnect.types.ai_agent_configuration_map.AIAgentConfigurationMap"
        ] = None,
        orchestrator_configuration_list: Optional[
            "capo_qconnect.types.orchestrator_configuration_list.OrchestratorConfigurationList"
        ] = None,
        remove_orchestrator_configuration_list: Optional[bool] = None,
    ) -> "capo_qconnect.types.update_session_response.UpdateSessionResponse":
        """<p>Updates a session. A session is a contextual container used for generating recommendations. Connect Customer updates the existing Amazon Q in Connect session for each contact on which Amazon Q in Connect is enabled.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            description: <p>The description.</p>
            tag_filter: <p>An object that can be used to specify Tag conditions.</p>
            ai_agent_configuration: <p>The configuration of the AI Agents (mapped by AI Agent Type to AI Agent version) that should be used by Amazon Q in Connect for this Session.</p>
            orchestrator_configuration_list: <p>The updated list of orchestrator configurations for the session.</p>
            remove_orchestrator_configuration_list: <p>The list of orchestrator configurations to remove from the session.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_session_request.UpdateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_session_response.UpdateSessionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_session

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_session.async_update_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_session_request.UpdateSessionRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if description is not None:
            input_["description"] = description
        if tag_filter is not None:
            input_["tag_filter"] = tag_filter
        if ai_agent_configuration is not None:
            input_["ai_agent_configuration"] = ai_agent_configuration
        if orchestrator_configuration_list is not None:
            input_["orchestrator_configuration_list"] = orchestrator_configuration_list
        if remove_orchestrator_configuration_list is not None:
            input_["remove_orchestrator_configuration_list"] = (
                remove_orchestrator_configuration_list
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_next_message(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        next_message_token: "capo_qconnect.types.next_token.NextToken",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_next_message_response.GetNextMessageResponse":
        """<p>Retrieves next message on an Amazon Q in Connect session.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant.</p>
            session_id: <p>The identifier of the Amazon Q in Connect session.</p>
            next_message_token: <p>The token for the next message. Use the value returned in the SendMessage or previous response in the next request to retrieve the next message.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unprocessable_content_exception.UnprocessableContentException: <p>The server has a failure of processing the message</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_next_message_request.GetNextMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_next_message_response.GetNextMessageResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_next_message

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_next_message.async_get_next_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_next_message_request.GetNextMessageRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
            "next_message_token": next_message_token,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_messages(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_qconnect.types.message_filter_type.MessageFilterType"
        ] = None,
    ) -> "capo_qconnect.types.list_messages_response.ListMessagesResponse":
        """<p>Lists messages on an Amazon Q in Connect session.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant.</p>
            session_id: <p>The identifier of the Amazon Q in Connect session.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            filter: <p>The filter criteria for listing messages.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_messages_request.ListMessagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_messages_response.ListMessagesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_messages

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_messages.async_list_messages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_messages_request.ListMessagesRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_messages(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_qconnect.types.message_filter_type.MessageFilterType"
        ] = None,
    ) -> "AsyncIterator[capo_qconnect.types.message_output.MessageOutput]":
        _token = next_token
        while True:
            _response = await self.list_messages(
                assistant_id,
                session_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("messages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_spans(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_spans_response.ListSpansResponse":
        """<p>Retrieves AI agent execution traces for a session, providing granular visibility into agent orchestration flows, LLM interactions, and tool invocations.</p>

        Args:
            assistant_id: <p>UUID or ARN of the Connect AI Assistant resource</p>
            session_id: <p>UUID or ARN of the Connect AI Session resource</p>
            next_token: <p>Pagination token for retrieving the next page of results</p>
            max_results: <p>Maximum number of spans to return per page</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_spans_request.ListSpansRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_spans_response.ListSpansResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_spans

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_spans.async_list_spans(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_spans_request.ListSpansRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
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

    async def iter_list_spans(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.span.Span]":
        _token = next_token
        while True:
            _response = await self.list_spans(
                assistant_id,
                session_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("spans",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def send_message(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        type: "capo_qconnect.types.message_type.MessageType",
        message: "capo_qconnect.types.message_input.MessageInput",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        ai_agent_id: Optional[
            "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier"
        ] = None,
        conversation_context: Optional[
            "capo_qconnect.types.conversation_context.ConversationContext"
        ] = None,
        configuration: Optional[
            "capo_qconnect.types.message_configuration.MessageConfiguration"
        ] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        orchestrator_use_case: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        metadata: Optional[
            "capo_qconnect.types.message_metadata.MessageMetadata"
        ] = None,
        origin_request_id: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_qconnect.types.send_message_response.SendMessageResponse":
        """<p>Submits a message to the Amazon Q in Connect session.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant.</p>
            session_id: <p>The identifier of the Amazon Q in Connect session.</p>
            type: <p>The message type.</p>
            message: <p>The message data to submit to the Amazon Q in Connect session.</p>
            ai_agent_id: <p>The identifier of the AI Agent to use for processing the message.</p>
            conversation_context: <p>The conversation context before the Amazon Q in Connect session.</p>
            configuration: <p>The configuration of the <a href="https://docs.aws.amazon.com/connect/latest/APIReference/API_amazon-q-connect_SendMessage.html">SendMessage</a> request.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field.For more information about idempotency, see Making retries safe with idempotent APIs.</p>
            orchestrator_use_case: <p>The orchestrator use case for message processing.</p>
            metadata: <p>Additional metadata for the message.</p>
            origin_request_id: <p>Request identifier from the origin system, used for end-to-end tracing across spans.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.dependency_failed_exception.DependencyFailedException: <p>The request failed because it depends on another request that failed.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.send_message_request.SendMessageRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.send_message_response.SendMessageResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.send_message

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.send_message.async_send_message(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.send_message_request.SendMessageRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
            "type": type,
            "message": message,
        }
        if ai_agent_id is not None:
            input_["ai_agent_id"] = ai_agent_id
        if conversation_context is not None:
            input_["conversation_context"] = conversation_context
        if configuration is not None:
            input_["configuration"] = configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if orchestrator_use_case is not None:
            input_["orchestrator_use_case"] = orchestrator_use_case
        if metadata is not None:
            input_["metadata"] = metadata
        if origin_request_id is not None:
            input_["origin_request_id"] = origin_request_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_session_data(
        self,
        assistant_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        session_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        data: "capo_qconnect.types.runtime_session_data_list.RuntimeSessionDataList",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        namespace: Optional[
            "capo_qconnect.types.session_data_namespace.SessionDataNamespace"
        ] = None,
    ) -> "capo_qconnect.types.update_session_data_response.UpdateSessionDataResponse":
        """<p>Updates the data stored on an Amazon Q in Connect Session.</p>

        Args:
            assistant_id: <p>The identifier of the Amazon Q in Connect assistant. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            session_id: <p>The identifier of the session. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            namespace: <p>The namespace into which the session data is stored. Supported namespaces are: Custom</p>
            data: <p>The data stored on the Amazon Q in Connect Session.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_session_data_request.UpdateSessionDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_session_data_response.UpdateSessionDataResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_session_data

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_session_data.async_update_session_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_session_data_request.UpdateSessionDataRequest = {
            "assistant_id": assistant_id,
            "session_id": session_id,
            "data": data,
        }
        if namespace is not None:
            input_["namespace"] = namespace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_knowledge_base(
        self,
        name: "capo_qconnect.types.name.Name",
        knowledge_base_type: "capo_qconnect.types.knowledge_base_type.KnowledgeBaseType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        source_configuration: Optional[
            "capo_qconnect.types.source_configuration.SourceConfiguration"
        ] = None,
        rendering_configuration: Optional[
            "capo_qconnect.types.rendering_configuration.RenderingConfiguration"
        ] = None,
        vector_ingestion_configuration: Optional[
            "capo_qconnect.types.vector_ingestion_configuration.VectorIngestionConfiguration"
        ] = None,
        server_side_encryption_configuration: Optional[
            "capo_qconnect.types.server_side_encryption_configuration.ServerSideEncryptionConfiguration"
        ] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> (
        "capo_qconnect.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
    ):
        """<p>Creates a knowledge base.</p> <note> <p>When using this API, you cannot reuse <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, you'll get an <code>InvalidRequestException</code> error. </p> <p>For example, you're programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:</p> <ol> <li> <p>Call <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_DeleteKnowledgeBase.html">DeleteKnowledgeBase</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a>.</p> </li> <li> <p>Call <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> to recreate the DataIntegration or a create different one.</p> </li> <li> <p>Call CreateKnowledgeBase.</p> </li> </ol> </note>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            name: <p>The name of the knowledge base.</p>
            knowledge_base_type: <p>The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically. </p>
            source_configuration: <p>The source of the knowledge base content. Only set this argument for EXTERNAL or Managed knowledge bases.</p>
            rendering_configuration: <p>Information about how to render the content.</p>
            vector_ingestion_configuration: <p>Contains details about how to ingest the documents in a data source.</p>
            server_side_encryption_configuration: <p>The configuration information for the customer managed key used for encryption. </p> <p>This KMS key must have a policy that allows <code>kms:CreateGrant</code>, <code>kms:DescribeKey</code>, <code>kms:Decrypt</code>, and <code>kms:GenerateDataKey*</code> permissions to the IAM identity using the key to invoke Amazon Q in Connect.</p> <p>For more information about setting up a customer managed key for Amazon Q in Connect, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html">Enable Amazon Q in Connect for your instance</a>.</p>
            description: <p>The description.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_knowledge_base_request.CreateKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_knowledge_base_response.CreateKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_knowledge_base

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_knowledge_base.async_create_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_knowledge_base_request.CreateKnowledgeBaseRequest = {
            "name": name,
            "knowledge_base_type": knowledge_base_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if rendering_configuration is not None:
            input_["rendering_configuration"] = rendering_configuration
        if vector_ingestion_configuration is not None:
            input_["vector_ingestion_configuration"] = vector_ingestion_configuration
        if server_side_encryption_configuration is not None:
            input_["server_side_encryption_configuration"] = (
                server_side_encryption_configuration
            )
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

    async def get_knowledge_base(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_knowledge_base_response.GetKnowledgeBaseResponse":
        """<p>Retrieves information about the knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_knowledge_base_request.GetKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_knowledge_base_response.GetKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_knowledge_base

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_knowledge_base.async_get_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_knowledge_base_request.GetKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_knowledge_base(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> (
        "capo_qconnect.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
    ):
        """<p>Deletes the knowledge base.</p> <note> <p>When you use this API to delete an external knowledge base such as Salesforce or ServiceNow, you must also delete the <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html">Amazon AppIntegrations</a> DataIntegration. This is because you can't reuse the DataIntegration after it's been associated with an external knowledge base. However, you can delete and recreate it. See <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html">DeleteDataIntegration</a> and <a href="https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html">CreateDataIntegration</a> in the <i>Amazon AppIntegrations API Reference</i>.</p> </note>

        Args:
            knowledge_base_id: <p>The knowledge base to delete content from. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_knowledge_base_response.DeleteKnowledgeBaseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_knowledge_base

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_knowledge_base.async_delete_knowledge_base(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_knowledge_base_request.DeleteKnowledgeBaseRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_knowledge_bases_response.ListKnowledgeBasesResponse":
        """<p>Lists the knowledge bases.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_knowledge_bases_request.ListKnowledgeBasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_knowledge_bases_response.ListKnowledgeBasesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_knowledge_bases

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_knowledge_bases.async_list_knowledge_bases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_knowledge_bases_request.ListKnowledgeBasesRequest = {}
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

    async def iter_list_knowledge_bases(
        self,
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_qconnect.types.knowledge_base_summary.KnowledgeBaseSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_knowledge_bases(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("knowledge_base_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def delete_import_job(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        import_job_id: "capo_qconnect.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_import_job_response.DeleteImportJobResponse":
        """<p>Deletes the quick response import job.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base.</p>
            import_job_id: <p>The identifier of the import job to be deleted.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_import_job_request.DeleteImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_import_job_response.DeleteImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_import_job

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_import_job.async_delete_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_import_job_request.DeleteImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_id": import_job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_import_job(
        self,
        import_job_id: "capo_qconnect.types.uuid.Uuid",
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_import_job_response.GetImportJobResponse":
        """<p>Retrieves the started import job.</p>

        Args:
            import_job_id: <p>The identifier of the import job to retrieve.</p>
            knowledge_base_id: <p>The identifier of the knowledge base that the import job belongs to.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_import_job_request.GetImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_import_job_response.GetImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_import_job

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_import_job.async_get_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_import_job_request.GetImportJobRequest = {
            "import_job_id": import_job_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_import_jobs(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_import_jobs_response.ListImportJobsResponse":
        """<p>Lists information about import jobs.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_import_jobs_request.ListImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_import_jobs_response.ListImportJobsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_import_jobs

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_import_jobs.async_list_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_import_jobs_request.ListImportJobsRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def iter_list_import_jobs(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.import_job_summary.ImportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_import_jobs(
                knowledge_base_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("import_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def remove_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse":
        """<p>Removes a URI template from a knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.remove_knowledge_base_template_uri_response.RemoveKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.remove_knowledge_base_template_uri

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.remove_knowledge_base_template_uri.async_remove_knowledge_base_template_uri(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.remove_knowledge_base_template_uri_request.RemoveKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def search_content(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_content_response.SearchContentResponse":
        """<p>Searches for content in a specified knowledge base. Can be used to get a specific content resource by its name.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression to filter results.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_content_request.SearchContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_content_response.SearchContentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_content

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_content.async_search_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.search_content_request.SearchContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
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

    async def iter_search_content(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.search_expression.SearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.content_summary.ContentSummary]":
        _token = next_token
        while True:
            _response = await self.search_content(
                knowledge_base_id,
                search_expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("content_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_message_templates(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.message_template_search_expression.MessageTemplateSearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.search_message_templates_response.SearchMessageTemplatesResponse":
        """<p>Searches for Amazon Q in Connect message templates in the specified knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression for querying the message template.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_message_templates_request.SearchMessageTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_message_templates_response.SearchMessageTemplatesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_message_templates

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_message_templates.async_search_message_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.search_message_templates_request.SearchMessageTemplatesRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
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

    async def iter_search_message_templates(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.message_template_search_expression.MessageTemplateSearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.message_template_search_result_data.MessageTemplateSearchResultData]":
        _token = next_token
        while True:
            _response = await self.search_message_templates(
                knowledge_base_id,
                search_expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def search_quick_responses(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.quick_response_search_expression.QuickResponseSearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        attributes: Optional[
            "capo_qconnect.types.contact_attributes.ContactAttributes"
        ] = None,
    ) -> "capo_qconnect.types.search_quick_responses_response.SearchQuickResponsesResponse":
        """<p>Searches existing Amazon Q in Connect quick responses in an Amazon Q in Connect knowledge base.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            search_expression: <p>The search expression for querying the quick response.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            attributes: <p>The <a href="https://docs.aws.amazon.com/connect/latest/adminguide/connect-attrib-list.html#user-defined-attributes">user-defined Connect Customer contact attributes</a> to be resolved when search results are returned.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.request_timeout_exception.RequestTimeoutException: <p>The request reached the service more than 15 minutes after the date stamp on the request or more than 15 minutes after the request expiration date (such as for pre-signed URLs), or the date stamp on the request is more than 15 minutes in the future.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.search_quick_responses_request.SearchQuickResponsesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.search_quick_responses_response.SearchQuickResponsesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.search_quick_responses

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.search_quick_responses.async_search_quick_responses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.search_quick_responses_request.SearchQuickResponsesRequest = {
            "knowledge_base_id": knowledge_base_id,
            "search_expression": search_expression,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if attributes is not None:
            input_["attributes"] = attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_search_quick_responses(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        search_expression: "capo_qconnect.types.quick_response_search_expression.QuickResponseSearchExpression",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
        attributes: Optional[
            "capo_qconnect.types.contact_attributes.ContactAttributes"
        ] = None,
    ) -> "AsyncIterator[capo_qconnect.types.quick_response_search_result_data.QuickResponseSearchResultData]":
        _token = next_token
        while True:
            _response = await self.search_quick_responses(
                knowledge_base_id,
                search_expression,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                attributes=attributes,
            )
            _page = _resolve_path(_response, ("results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_content_upload(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_type: "capo_qconnect.types.content_type.ContentType",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        presigned_url_time_to_live: Optional[
            "capo_qconnect.types.time_to_live.TimeToLive"
        ] = None,
    ) -> "capo_qconnect.types.start_content_upload_response.StartContentUploadResponse":
        """<p>Get a URL to upload content to a knowledge base. To upload content, first make a PUT request to the returned URL with your file, making sure to include the required headers. Then use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_CreateContent.html">CreateContent</a> to finalize the content creation process or <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_UpdateContent.html">UpdateContent</a> to modify an existing resource. You can only upload content to a knowledge base of type CUSTOM.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            content_type: <p>The type of content to upload.</p>
            presigned_url_time_to_live: <p>The expected expiration time of the generated presigned URL, specified in minutes.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.start_content_upload_request.StartContentUploadRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.start_content_upload_response.StartContentUploadResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.start_content_upload

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.start_content_upload.async_start_content_upload(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.start_content_upload_request.StartContentUploadRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_type": content_type,
        }
        if presigned_url_time_to_live is not None:
            input_["presigned_url_time_to_live"] = presigned_url_time_to_live

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_import_job(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        import_job_type: "capo_qconnect.types.import_job_type.ImportJobType",
        upload_id: "capo_qconnect.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        metadata: Optional[
            "capo_qconnect.types.content_metadata.ContentMetadata"
        ] = None,
        external_source_configuration: Optional[
            "capo_qconnect.types.external_source_configuration.ExternalSourceConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.start_import_job_response.StartImportJobResponse":
        """<p>Start an asynchronous job to import Amazon Q in Connect resources from an uploaded source file. Before calling this API, use <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a> to upload an asset that contains the resource data.</p> <ul> <li> <p>For importing Amazon Q in Connect quick responses, you need to upload a csv file including the quick responses. For information about how to format the csv file for importing quick responses, see <a href="https://docs.aws.amazon.com/console/connect/quick-responses/add-data">Import quick responses</a>.</p> </li> </ul>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p> <ul> <li> <p>For importing Amazon Q in Connect quick responses, this should be a <code>QUICK_RESPONSES</code> type knowledge base.</p> </li> </ul>
            import_job_type: <p>The type of the import job.</p> <ul> <li> <p>For importing quick response resource, set the value to <code>QUICK_RESPONSES</code>.</p> </li> </ul>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/wisdom/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>
            client_token: <p>The tags used to organize, track, or control access for this resource.</p>
            metadata: <p>The metadata fields of the imported Amazon Q in Connect resources.</p>
            external_source_configuration: <p>The configuration information of the external source that the resource data are imported from.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.start_import_job_request.StartImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.start_import_job_response.StartImportJobResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.start_import_job

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.start_import_job.async_start_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.start_import_job_request.StartImportJobRequest = {
            "knowledge_base_id": knowledge_base_id,
            "import_job_type": import_job_type,
            "upload_id": upload_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata is not None:
            input_["metadata"] = metadata
        if external_source_configuration is not None:
            input_["external_source_configuration"] = external_source_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_knowledge_base_template_uri(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        template_uri: "capo_qconnect.types.uri.Uri",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse":
        """<p>Updates the template URI of a knowledge base. This is only supported for knowledge bases of type EXTERNAL. Include a single variable in <code>${variable}</code> format; this interpolated by Amazon Q in Connect using ingested content. For example, if you ingest a Salesforce article, it has an <code>Id</code> value, and you can set the template URI to <code>https://myInstanceName.lightning.force.com/lightning/r/Knowledge__kav/*${Id}*/view</code>. </p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            template_uri: <p>The template URI to update.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_knowledge_base_template_uri_response.UpdateKnowledgeBaseTemplateUriResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_knowledge_base_template_uri

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_knowledge_base_template_uri.async_update_knowledge_base_template_uri(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_knowledge_base_template_uri_request.UpdateKnowledgeBaseTemplateUriRequest = {
            "knowledge_base_id": knowledge_base_id,
            "template_uri": template_uri,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_content(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        name: "capo_qconnect.types.name.Name",
        upload_id: "capo_qconnect.types.upload_id.UploadId",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        title: Optional["capo_qconnect.types.content_title.ContentTitle"] = None,
        override_link_out_uri: Optional["capo_qconnect.types.uri.Uri"] = None,
        metadata: Optional[
            "capo_qconnect.types.content_metadata.ContentMetadata"
        ] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> "capo_qconnect.types.create_content_response.CreateContentResponse":
        """<p>Creates Amazon Q in Connect content. Before to calling this API, use <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a> to upload an asset.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the content. Each piece of content in a knowledge base must have a unique name. You can retrieve a piece of content using only its knowledge base and its name with the <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SearchContent.html">SearchContent</a> API.</p>
            title: <p>The title of the content. If not set, the title is equal to the name.</p>
            override_link_out_uri: <p>The URI you want to use for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content.</p>
            metadata: <p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.</p>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_content_request.CreateContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_content_response.CreateContentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_content

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_content.async_create_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_content_request.CreateContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "upload_id": upload_id,
        }
        if title is not None:
            input_["title"] = title
        if override_link_out_uri is not None:
            input_["override_link_out_uri"] = override_link_out_uri
        if metadata is not None:
            input_["metadata"] = metadata
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

    async def get_content(
        self,
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_content_response.GetContentResponse":
        """<p>Retrieves content, including a pre-signed URL to download the content.</p>

        Args:
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_content_request.GetContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_content_response.GetContentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_content

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_content.async_get_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_content_request.GetContentRequest = {
            "content_id": content_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_content(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        revision_id: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        title: Optional["capo_qconnect.types.content_title.ContentTitle"] = None,
        override_link_out_uri: Optional["capo_qconnect.types.uri.Uri"] = None,
        remove_override_link_out_uri: Optional[bool] = None,
        metadata: Optional[
            "capo_qconnect.types.content_metadata.ContentMetadata"
        ] = None,
        upload_id: Optional["capo_qconnect.types.upload_id.UploadId"] = None,
    ) -> "capo_qconnect.types.update_content_response.UpdateContentResponse":
        """<p>Updates information about the content.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN</p>
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            revision_id: <p>The <code>revisionId</code> of the content resource to update, taken from an earlier call to <code>GetContent</code>, <code>GetContentSummary</code>, <code>SearchContent</code>, or <code>ListContents</code>. If included, this argument acts as an optimistic lock to ensure content was not modified since it was last read. If it has been modified, this API throws a <code>PreconditionFailedException</code>.</p>
            title: <p>The title of the content.</p>
            override_link_out_uri: <p>The URI for the article. If the knowledge base has a templateUri, setting this argument overrides it for this piece of content. To remove an existing <code>overrideLinkOurUri</code>, exclude this argument and set <code>removeOverrideLinkOutUri</code> to true.</p>
            remove_override_link_out_uri: <p>Unset the existing <code>overrideLinkOutUri</code> if it exists.</p>
            metadata: <p>A key/value map to store attributes without affecting tagging or recommendations. For example, when synchronizing data between an external system and Amazon Q in Connect, you can store an external version identifier as metadata to utilize for determining drift.</p>
            upload_id: <p>A pointer to the uploaded asset. This value is returned by <a href="https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_StartContentUpload.html">StartContentUpload</a>. </p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.precondition_failed_exception.PreconditionFailedException: <p>The provided <code>revisionId</code> does not match, indicating the content has been modified since it was last read.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_content_request.UpdateContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_content_response.UpdateContentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_content

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_content.async_update_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_content_request.UpdateContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
        }
        if revision_id is not None:
            input_["revision_id"] = revision_id
        if title is not None:
            input_["title"] = title
        if override_link_out_uri is not None:
            input_["override_link_out_uri"] = override_link_out_uri
        if remove_override_link_out_uri is not None:
            input_["remove_override_link_out_uri"] = remove_override_link_out_uri
        if metadata is not None:
            input_["metadata"] = metadata
        if upload_id is not None:
            input_["upload_id"] = upload_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_content(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_content_response.DeleteContentResponse":
        """<p>Deletes the content.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_content_request.DeleteContentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_content_response.DeleteContentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_content

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_content.async_delete_content(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_content_request.DeleteContentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_contents(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_contents_response.ListContentsResponse":
        """<p>Lists the content.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_contents_request.ListContentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_contents_response.ListContentsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_contents

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_contents.async_list_contents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_contents_request.ListContentsRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def iter_list_contents(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.content_summary.ContentSummary]":
        _token = next_token
        while True:
            _response = await self.list_contents(
                knowledge_base_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("content_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_content_summary(
        self,
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_content_summary_response.GetContentSummaryResponse":
        """<p>Retrieves summary information about the content.</p>

        Args:
            content_id: <p>The identifier of the content. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_content_summary_request.GetContentSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_content_summary_response.GetContentSummaryResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_content_summary

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_content_summary.async_get_content_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_content_summary_request.GetContentSummaryRequest = {
            "content_id": content_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_content_association(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        association_type: "capo_qconnect.types.content_association_type.ContentAssociationType",
        association: "capo_qconnect.types.content_association_contents.ContentAssociationContents",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> "capo_qconnect.types.create_content_association_response.CreateContentAssociationResponse":
        """<p>Creates an association between a content resource in a knowledge base and <a href="https://docs.aws.amazon.com/connect/latest/adminguide/step-by-step-guided-experiences.html">step-by-step guides</a>. Step-by-step guides offer instructions to agents for resolving common customer issues. You create a content association to integrate Amazon Q in Connect and step-by-step guides. </p> <p>After you integrate Amazon Q and step-by-step guides, when Amazon Q provides a recommendation to an agent based on the intent that it's detected, it also provides them with the option to start the step-by-step guide that you have associated with the content.</p> <p>Note the following limitations:</p> <ul> <li> <p>You can create only one content association for each content resource in a knowledge base.</p> </li> <li> <p>You can associate a step-by-step guide with multiple content resources.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/integrate-q-with-guides.html">Integrate Amazon Q in Connect with step-by-step guides</a> in the <i>Connect Customer Administrator Guide</i>. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            knowledge_base_id: <p>The identifier of the knowledge base.</p>
            content_id: <p>The identifier of the content.</p>
            association_type: <p>The type of association.</p>
            association: <p>The identifier of the associated resource.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_content_association_request.CreateContentAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_content_association_response.CreateContentAssociationResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_content_association

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_content_association.async_create_content_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_content_association_request.CreateContentAssociationRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
            "association_type": association_type,
            "association": association,
        }
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

    async def get_content_association(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_association_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_content_association_response.GetContentAssociationResponse":
        """<p>Returns the content association.</p> <p>For more information about content associations--what they are and when they are used--see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/integrate-q-with-guides.html">Integrate Amazon Q in Connect with step-by-step guides</a> in the <i>Connect Customer Administrator Guide</i>.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base.</p>
            content_id: <p>The identifier of the content.</p>
            content_association_id: <p>The identifier of the content association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_content_association_request.GetContentAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_content_association_response.GetContentAssociationResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_content_association

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_content_association.async_get_content_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_content_association_request.GetContentAssociationRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
            "content_association_id": content_association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_content_association(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_association_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_content_association_response.DeleteContentAssociationResponse":
        """<p>Deletes the content association. </p> <p>For more information about content associations--what they are and when they are used--see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/integrate-q-with-guides.html">Integrate Amazon Q in Connect with step-by-step guides</a> in the <i>Connect Customer Administrator Guide</i>. </p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base.</p>
            content_id: <p>The identifier of the content.</p>
            content_association_id: <p>The identifier of the content association. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_content_association_request.DeleteContentAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_content_association_response.DeleteContentAssociationResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_content_association

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_content_association.async_delete_content_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_content_association_request.DeleteContentAssociationRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
            "content_association_id": content_association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_content_associations(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_content_associations_response.ListContentAssociationsResponse":
        """<p>Lists the content associations.</p> <p>For more information about content associations--what they are and when they are used--see <a href="https://docs.aws.amazon.com/connect/latest/adminguide/integrate-q-with-guides.html">Integrate Amazon Q in Connect with step-by-step guides</a> in the <i>Connect Customer Administrator Guide</i>.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base.</p>
            content_id: <p>The identifier of the content.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_content_associations_request.ListContentAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_content_associations_response.ListContentAssociationsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_content_associations

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_content_associations.async_list_content_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_content_associations_request.ListContentAssociationsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "content_id": content_id,
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

    async def iter_list_content_associations(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        content_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.content_association_summary.ContentAssociationSummary]":
        _token = next_token
        while True:
            _response = await self.list_content_associations(
                knowledge_base_id,
                content_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("content_association_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_message_template(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        channel_subtype: "capo_qconnect.types.channel_subtype.ChannelSubtype",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        name: Optional["capo_qconnect.types.name.Name"] = None,
        content: Optional[
            "capo_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
        ] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        language: Optional["capo_qconnect.types.language_code.LanguageCode"] = None,
        source_configuration: Optional[
            "capo_qconnect.types.message_template_source_configuration.MessageTemplateSourceConfiguration"
        ] = None,
        default_attributes: Optional[
            "capo_qconnect.types.message_template_attributes.MessageTemplateAttributes"
        ] = None,
        grouping_configuration: Optional[
            "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
        ] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> "capo_qconnect.types.create_message_template_response.CreateMessageTemplateResponse":
        """<p>Creates an Amazon Q in Connect message template. The name of the message template has to be unique for each knowledge base. The channel subtype of the message template is immutable and cannot be modified after creation. After the message template is created, you can use the <code>$LATEST</code> qualifier to reference the created message template.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the message template.</p>
            content: <p>The content of the message template.</p>
            description: <p>The description of the message template.</p>
            channel_subtype: <p>The channel subtype this message template applies to.</p>
            language: <p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>
            source_configuration: <p>The source configuration of the message template. Only set this argument for WHATSAPP channel subtype.</p>
            default_attributes: <p>An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_message_template_request.CreateMessageTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_message_template_response.CreateMessageTemplateResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_message_template

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_message_template.async_create_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_message_template_request.CreateMessageTemplateRequest = {
            "knowledge_base_id": knowledge_base_id,
            "channel_subtype": channel_subtype,
        }
        if name is not None:
            input_["name"] = name
        if content is not None:
            input_["content"] = content
        if description is not None:
            input_["description"] = description
        if language is not None:
            input_["language"] = language
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if default_attributes is not None:
            input_["default_attributes"] = default_attributes
        if grouping_configuration is not None:
            input_["grouping_configuration"] = grouping_configuration
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

    async def get_message_template(
        self,
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_message_template_response.GetMessageTemplateResponse":
        """<p>Retrieves the Amazon Q in Connect message template. The message template identifier can contain an optional qualifier, for example, <code>&lt;message-template-id&gt;:&lt;qualifier&gt;</code>, which is either an actual version number or an Amazon Q Connect managed qualifier <code>$ACTIVE_VERSION</code> | <code>$LATEST</code>. If it is not supplied, then <code>$LATEST</code> is assumed implicitly.</p>

        Args:
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_message_template_request.GetMessageTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_message_template_response.GetMessageTemplateResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_message_template

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_message_template.async_get_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_message_template_request.GetMessageTemplateRequest = {
            "message_template_id": message_template_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_message_template(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        content: Optional[
            "capo_qconnect.types.message_template_content_provider.MessageTemplateContentProvider"
        ] = None,
        language: Optional["capo_qconnect.types.language_code.LanguageCode"] = None,
        source_configuration: Optional[
            "capo_qconnect.types.message_template_source_configuration.MessageTemplateSourceConfiguration"
        ] = None,
        default_attributes: Optional[
            "capo_qconnect.types.message_template_attributes.MessageTemplateAttributes"
        ] = None,
    ) -> "capo_qconnect.types.update_message_template_response.UpdateMessageTemplateResponse":
        """<p>Updates the Amazon Q in Connect message template. Partial update is supported. If any field is not supplied, it will remain unchanged for the message template that is referenced by the <code>$LATEST</code> qualifier. Any modification will only apply to the message template that is referenced by the <code>$LATEST</code> qualifier. The fields for all available versions will remain unchanged.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            content: <p>The content of the message template.</p>
            language: <p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>
            source_configuration: <p>The source configuration of the message template. Only set this argument for WHATSAPP channel subtype.</p>
            default_attributes: <p>An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_message_template_request.UpdateMessageTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_message_template_response.UpdateMessageTemplateResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_message_template

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_message_template.async_update_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_message_template_request.UpdateMessageTemplateRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
        }
        if content is not None:
            input_["content"] = content
        if language is not None:
            input_["language"] = language
        if source_configuration is not None:
            input_["source_configuration"] = source_configuration
        if default_attributes is not None:
            input_["default_attributes"] = default_attributes

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_message_template(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_message_template_response.DeleteMessageTemplateResponse":
        """<p>Deletes an Amazon Q in Connect message template entirely or a specific version of the message template if version is supplied in the request. You can provide the message template identifier as <code>&lt;message-template-id&gt;:&lt;versionNumber&gt;</code> to delete a specific version of the message template. If it is not supplied, the message template and all available versions will be deleted.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_message_template_request.DeleteMessageTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_message_template_response.DeleteMessageTemplateResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_message_template

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_message_template.async_delete_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_message_template_request.DeleteMessageTemplateRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_message_templates(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_message_templates_response.ListMessageTemplatesResponse":
        """<p>Lists all the available Amazon Q in Connect message templates for the specified knowledge base.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_message_templates_request.ListMessageTemplatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_message_templates_response.ListMessageTemplatesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_message_templates

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_message_templates.async_list_message_templates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_message_templates_request.ListMessageTemplatesRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def iter_list_message_templates(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.message_template_summary.MessageTemplateSummary]":
        _token = next_token
        while True:
            _response = await self.list_message_templates(
                knowledge_base_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("message_template_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def activate_message_template(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        version_number: "capo_qconnect.types.version.Version",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.activate_message_template_response.ActivateMessageTemplateResponse":
        """<p>Activates a specific version of the Amazon Q in Connect message template. After the version is activated, the previous active version will be deactivated automatically. You can use the <code>$ACTIVE_VERSION</code> qualifier later to reference the version that is in active status.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            version_number: <p>The version number of the message template version to activate.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.activate_message_template_request.ActivateMessageTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.activate_message_template_response.ActivateMessageTemplateResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.activate_message_template

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.activate_message_template.async_activate_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.activate_message_template_request.ActivateMessageTemplateRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_message_template_attachment(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        content_disposition: "capo_qconnect.types.content_disposition.ContentDisposition",
        name: "capo_qconnect.types.attachment_file_name.AttachmentFileName",
        body: "capo_qconnect.types.non_empty_unlimited_string.NonEmptyUnlimitedString",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        client_token: Optional["capo_qconnect.types.client_token.ClientToken"] = None,
    ) -> "capo_qconnect.types.create_message_template_attachment_response.CreateMessageTemplateAttachmentResponse":
        """<p>Uploads an attachment file to the specified Amazon Q in Connect message template. The name of the message template attachment has to be unique for each message template referenced by the <code>$LATEST</code> qualifier. The body of the attachment file should be encoded using base64 encoding. After the file is uploaded, you can use the pre-signed Amazon S3 URL returned in response to download the uploaded file.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            content_disposition: <p>The presentation information for the attachment file.</p>
            name: <p>The name of the attachment file being uploaded. The name should include the file extension.</p>
            body: <p>The body of the attachment file being uploaded. It should be encoded using base64 encoding.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_message_template_attachment_request.CreateMessageTemplateAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_message_template_attachment_response.CreateMessageTemplateAttachmentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_message_template_attachment

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_message_template_attachment.async_create_message_template_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_message_template_attachment_request.CreateMessageTemplateAttachmentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
            "content_disposition": content_disposition,
            "name": name,
            "body": body,
        }
        if client_token is not None:
            input_["client_token"] = client_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_message_template_version(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        message_template_content_sha256: Optional[
            "capo_qconnect.types.message_template_content_sha256.MessageTemplateContentSha256"
        ] = None,
    ) -> "capo_qconnect.types.create_message_template_version_response.CreateMessageTemplateVersionResponse":
        """<p>Creates a new Amazon Q in Connect message template version from the current content and configuration of a message template. Versions are immutable and monotonically increasing. Once a version is created, you can reference a specific version of the message template by passing in <code>&lt;message-template-id&gt;:&lt;versionNumber&gt;</code> as the message template identifier. An error is displayed if the supplied <code>messageTemplateContentSha256</code> is different from the <code>messageTemplateContentSha256</code> of the message template with <code>$LATEST</code> qualifier. If multiple <code>CreateMessageTemplateVersion</code> requests are made while the message template remains the same, only the first invocation creates a new version and the succeeding requests will return the same response as the first invocation.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            message_template_content_sha256: <p>The checksum value of the message template content that is referenced by the <code>$LATEST</code> qualifier. It can be returned in <code>MessageTemplateData</code> or <code>ExtendedMessageTemplateData</code>. It’s calculated by content, language, <code>defaultAttributes</code> and <code>Attachments</code> of the message template. If not supplied, the message template version will be created based on the message template content that is referenced by the <code>$LATEST</code> qualifier by default.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_message_template_version_request.CreateMessageTemplateVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_message_template_version_response.CreateMessageTemplateVersionResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_message_template_version

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_message_template_version.async_create_message_template_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_message_template_version_request.CreateMessageTemplateVersionRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
        }
        if message_template_content_sha256 is not None:
            input_["message_template_content_sha256"] = message_template_content_sha256

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deactivate_message_template(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        version_number: "capo_qconnect.types.version.Version",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.deactivate_message_template_response.DeactivateMessageTemplateResponse":
        """<p>Deactivates a specific version of the Amazon Q in Connect message template . After the version is deactivated, you can no longer use the <code>$ACTIVE_VERSION</code> qualifier to reference the version in active status.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            version_number: <p>The version number of the message template version to deactivate.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.deactivate_message_template_request.DeactivateMessageTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.deactivate_message_template_response.DeactivateMessageTemplateResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.deactivate_message_template

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.deactivate_message_template.async_deactivate_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.deactivate_message_template_request.DeactivateMessageTemplateRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
            "version_number": version_number,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_message_template_attachment(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        attachment_id: "capo_qconnect.types.uuid.Uuid",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.delete_message_template_attachment_response.DeleteMessageTemplateAttachmentResponse":
        """<p>Deletes the attachment file from the Amazon Q in Connect message template that is referenced by <code>$LATEST</code> qualifier. Attachments on available message template versions will remain unchanged.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            attachment_id: <p>The identifier of the attachment file.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_message_template_attachment_request.DeleteMessageTemplateAttachmentRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_message_template_attachment_response.DeleteMessageTemplateAttachmentResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_message_template_attachment

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_message_template_attachment.async_delete_message_template_attachment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_message_template_attachment_request.DeleteMessageTemplateAttachmentRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
            "attachment_id": attachment_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_message_template_versions(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_message_template_versions_response.ListMessageTemplateVersionsResponse":
        """<p>Lists all the available versions for the specified Amazon Q in Connect message template.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_message_template_versions_request.ListMessageTemplateVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_message_template_versions_response.ListMessageTemplateVersionsResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_message_template_versions

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_message_template_versions.async_list_message_template_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_message_template_versions_request.ListMessageTemplateVersionsRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
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

    async def iter_list_message_template_versions(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional["capo_qconnect.types.next_token.NextToken"] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_qconnect.types.message_template_version_summary.MessageTemplateVersionSummary]":
        _token = next_token
        while True:
            _response = await self.list_message_template_versions(
                knowledge_base_id,
                message_template_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("message_template_version_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def render_message_template(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        attributes: "capo_qconnect.types.message_template_attributes.MessageTemplateAttributes",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.render_message_template_response.RenderMessageTemplateResponse":
        """<p>Renders the Amazon Q in Connect message template based on the attribute values provided and generates the message content. For any variable present in the message template, if the attribute value is neither provided in the attribute request parameter nor the default attribute of the message template, the rendered message content will keep the variable placeholder as it is and return the attribute keys that are missing.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN.</p>
            attributes: <p>An object that specifies the values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the value for that variable.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.render_message_template_request.RenderMessageTemplateRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.render_message_template_response.RenderMessageTemplateResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.render_message_template

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.render_message_template.async_render_message_template(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.render_message_template_request.RenderMessageTemplateRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
            "attributes": attributes,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_message_template_metadata(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        message_template_id: "capo_qconnect.types.uuid_or_arn_or_either_with_qualifier.UuidOrArnOrEitherWithQualifier",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        name: Optional["capo_qconnect.types.name.Name"] = None,
        description: Optional["capo_qconnect.types.description.Description"] = None,
        grouping_configuration: Optional[
            "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
        ] = None,
    ) -> "capo_qconnect.types.update_message_template_metadata_response.UpdateMessageTemplateMetadataResponse":
        """<p>Updates the Amazon Q in Connect message template metadata. Note that any modification to the message template’s name, description and grouping configuration will applied to the message template pointed by the <code>$LATEST</code> qualifier and all available versions. Partial update is supported. If any field is not supplied, it will remain unchanged for the message template.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            message_template_id: <p>The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.</p>
            name: <p>The name of the message template.</p>
            description: <p>The description of the message template.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.throttling_exception.ThrottlingException: <p>The throttling limit has been exceeded.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_message_template_metadata_request.UpdateMessageTemplateMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_message_template_metadata_response.UpdateMessageTemplateMetadataResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_message_template_metadata

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_message_template_metadata.async_update_message_template_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_message_template_metadata_request.UpdateMessageTemplateMetadataRequest = {
            "knowledge_base_id": knowledge_base_id,
            "message_template_id": message_template_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if grouping_configuration is not None:
            input_["grouping_configuration"] = grouping_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_quick_response(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        name: "capo_qconnect.types.quick_response_name.QuickResponseName",
        content: "capo_qconnect.types.quick_response_data_provider.QuickResponseDataProvider",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        content_type: Optional[
            "capo_qconnect.types.quick_response_type.QuickResponseType"
        ] = None,
        grouping_configuration: Optional[
            "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
        ] = None,
        description: Optional[
            "capo_qconnect.types.quick_response_description.QuickResponseDescription"
        ] = None,
        shortcut_key: Optional["capo_qconnect.types.short_cut_key.ShortCutKey"] = None,
        is_active: Optional[bool] = None,
        channels: Optional["capo_qconnect.types.channels.Channels"] = None,
        language: Optional["capo_qconnect.types.language_code.LanguageCode"] = None,
        client_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        tags: Optional["capo_qconnect.types.tags.Tags"] = None,
    ) -> (
        "capo_qconnect.types.create_quick_response_response.CreateQuickResponseResponse"
    ):
        """<p>Creates an Amazon Q in Connect quick response.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            name: <p>The name of the quick response.</p>
            content: <p>The content of the quick response.</p>
            content_type: <p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for a quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for a quick response written in richtext.</p> </li> </ul>
            grouping_configuration: <p>The configuration information of the user groups that the quick response is accessible to.</p>
            description: <p>The description of the quick response.</p>
            shortcut_key: <p>The shortcut key of the quick response. The value should be unique across the knowledge base. </p>
            is_active: <p>Whether the quick response is active.</p>
            channels: <p>The Connect Customer channels this quick response applies to.</p>
            language: <p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="http://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>
            tags: <p>The tags used to organize, track, or control access for this resource.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You've exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use service quotas to request a service quota increase.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.create_quick_response_request.CreateQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.create_quick_response_response.CreateQuickResponseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.create_quick_response

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.create_quick_response.async_create_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.create_quick_response_request.CreateQuickResponseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "name": name,
            "content": content,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if grouping_configuration is not None:
            input_["grouping_configuration"] = grouping_configuration
        if description is not None:
            input_["description"] = description
        if shortcut_key is not None:
            input_["shortcut_key"] = shortcut_key
        if is_active is not None:
            input_["is_active"] = is_active
        if channels is not None:
            input_["channels"] = channels
        if language is not None:
            input_["language"] = language
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

    async def get_quick_response(
        self,
        quick_response_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> "capo_qconnect.types.get_quick_response_response.GetQuickResponseResponse":
        """<p>Retrieves the quick response.</p>

        Args:
            quick_response_id: <p>The identifier of the quick response.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. This should be a QUICK_RESPONSES type knowledge base.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.get_quick_response_request.GetQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.get_quick_response_response.GetQuickResponseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.get_quick_response

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.get_quick_response.async_get_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.get_quick_response_request.GetQuickResponseRequest = {
            "quick_response_id": quick_response_id,
            "knowledge_base_id": knowledge_base_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_quick_response(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        quick_response_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        name: Optional[
            "capo_qconnect.types.quick_response_name.QuickResponseName"
        ] = None,
        content: Optional[
            "capo_qconnect.types.quick_response_data_provider.QuickResponseDataProvider"
        ] = None,
        content_type: Optional[
            "capo_qconnect.types.quick_response_type.QuickResponseType"
        ] = None,
        grouping_configuration: Optional[
            "capo_qconnect.types.grouping_configuration.GroupingConfiguration"
        ] = None,
        remove_grouping_configuration: Optional[bool] = None,
        description: Optional[
            "capo_qconnect.types.quick_response_description.QuickResponseDescription"
        ] = None,
        remove_description: Optional[bool] = None,
        shortcut_key: Optional["capo_qconnect.types.short_cut_key.ShortCutKey"] = None,
        remove_shortcut_key: Optional[bool] = None,
        is_active: Optional[bool] = None,
        channels: Optional["capo_qconnect.types.channels.Channels"] = None,
        language: Optional["capo_qconnect.types.language_code.LanguageCode"] = None,
    ) -> (
        "capo_qconnect.types.update_quick_response_response.UpdateQuickResponseResponse"
    ):
        """<p>Updates an existing Amazon Q in Connect quick response.</p>

        Args:
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>
            quick_response_id: <p>The identifier of the quick response.</p>
            name: <p>The name of the quick response.</p>
            content: <p>The updated content of the quick response.</p>
            content_type: <p>The media type of the quick response content.</p> <ul> <li> <p>Use <code>application/x.quickresponse;format=plain</code> for quick response written in plain text.</p> </li> <li> <p>Use <code>application/x.quickresponse;format=markdown</code> for quick response written in richtext.</p> </li> </ul>
            grouping_configuration: <p>The updated grouping configuration of the quick response.</p>
            remove_grouping_configuration: <p>Whether to remove the grouping configuration of the quick response.</p>
            description: <p>The updated description of the quick response.</p>
            remove_description: <p>Whether to remove the description from the quick response.</p>
            shortcut_key: <p>The shortcut key of the quick response. The value should be unique across the knowledge base.</p>
            remove_shortcut_key: <p>Whether to remove the shortcut key of the quick response.</p>
            is_active: <p>Whether the quick response is active. </p>
            channels: <p>The Connect Customer contact channels this quick response applies to. The supported contact channel types include <code>Chat</code>.</p>
            language: <p>The language code value for the language in which the quick response is written. The supported language codes include <code>de_DE</code>, <code>en_US</code>, <code>es_ES</code>, <code>fr_FR</code>, <code>id_ID</code>, <code>it_IT</code>, <code>ja_JP</code>, <code>ko_KR</code>, <code>pt_BR</code>, <code>zh_CN</code>, <code>zh_TW</code> </p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.conflict_exception.ConflictException: <p>The request could not be processed because of conflict in the current state of the resource. For example, if you're using a <code>Create</code> API (such as <code>CreateAssistant</code>) that accepts name, a conflicting resource (usually with the same name) is being created or mutated.</p>
            capo_qconnect.errors.precondition_failed_exception.PreconditionFailedException: <p>The provided <code>revisionId</code> does not match, indicating the content has been modified since it was last read.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.update_quick_response_request.UpdateQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.update_quick_response_response.UpdateQuickResponseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.update_quick_response

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.update_quick_response.async_update_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.update_quick_response_request.UpdateQuickResponseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "quick_response_id": quick_response_id,
        }
        if name is not None:
            input_["name"] = name
        if content is not None:
            input_["content"] = content
        if content_type is not None:
            input_["content_type"] = content_type
        if grouping_configuration is not None:
            input_["grouping_configuration"] = grouping_configuration
        if remove_grouping_configuration is not None:
            input_["remove_grouping_configuration"] = remove_grouping_configuration
        if description is not None:
            input_["description"] = description
        if remove_description is not None:
            input_["remove_description"] = remove_description
        if shortcut_key is not None:
            input_["shortcut_key"] = shortcut_key
        if remove_shortcut_key is not None:
            input_["remove_shortcut_key"] = remove_shortcut_key
        if is_active is not None:
            input_["is_active"] = is_active
        if channels is not None:
            input_["channels"] = channels
        if language is not None:
            input_["language"] = language

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_quick_response(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        quick_response_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
    ) -> (
        "capo_qconnect.types.delete_quick_response_response.DeleteQuickResponseResponse"
    ):
        """<p>Deletes a quick response.</p>

        Args:
            knowledge_base_id: <p>The knowledge base from which the quick response is deleted. The identifier of the knowledge base.</p>
            quick_response_id: <p>The identifier of the quick response to delete.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.unauthorized_exception.UnauthorizedException: <p>You do not have permission to perform this action.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.delete_quick_response_request.DeleteQuickResponseRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.delete_quick_response_response.DeleteQuickResponseResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.delete_quick_response

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.delete_quick_response.async_delete_quick_response(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.delete_quick_response_request.DeleteQuickResponseRequest = {
            "knowledge_base_id": knowledge_base_id,
            "quick_response_id": quick_response_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_quick_responses(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> "capo_qconnect.types.list_quick_responses_response.ListQuickResponsesResponse":
        """<p>Lists information about quick response.</p>

        Args:
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return per page.</p>
            knowledge_base_id: <p>The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.</p>

        Raises:
            capo_qconnect.errors.access_denied_exception.AccessDeniedException: <p>You do not have sufficient access to perform this action.</p>
            capo_qconnect.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_qconnect.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by a service.</p>
            capo_qconnect.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_qconnect.types.list_quick_responses_request.ListQuickResponsesRequest]",
        ) -> AsyncOperationResponse[
            "capo_qconnect.types.list_quick_responses_response.ListQuickResponsesResponse"
        ]:
            import capo_qconnect._operations.wisdom_service.list_quick_responses

            (
                output,
                http_response,
            ) = await capo_qconnect._operations.wisdom_service.list_quick_responses.async_list_quick_responses(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qconnect.types.list_quick_responses_request.ListQuickResponsesRequest = {
            "knowledge_base_id": knowledge_base_id
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

    async def iter_list_quick_responses(
        self,
        knowledge_base_id: "capo_qconnect.types.uuid_or_arn.UuidOrArn",
        *,
        config_overrides: Optional[AsyncQConnectClientConfig] = None,
        next_token: Optional[
            "capo_qconnect.types.non_empty_string.NonEmptyString"
        ] = None,
        max_results: Optional["capo_qconnect.types.max_results.MaxResults"] = None,
    ) -> (
        "AsyncIterator[capo_qconnect.types.quick_response_summary.QuickResponseSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_quick_responses(
                knowledge_base_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("quick_response_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
