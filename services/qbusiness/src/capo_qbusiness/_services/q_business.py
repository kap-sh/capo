"""Generated from Smithy shape ``com.amazonaws.qbusiness#ExpertQ``."""

import uuid
import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_qbusiness._auth._signers
import capo_qbusiness._auth._sigv4
from capo_qbusiness._auth._identity import Credentials
from capo_qbusiness._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_qbusiness._auth._zapros_handler import AuthMiddleware
from capo_qbusiness._iter import ensure_sync_iterator
from capo_qbusiness._pagination import resolve_path as _resolve_path
from capo_qbusiness._resources.expert_q.application_resource import ApplicationResource
from capo_qbusiness._services._aws_config import aws_config
from capo_qbusiness._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_qbusiness.types.action_configuration_list
    import capo_qbusiness.types.action_execution
    import capo_qbusiness.types.action_summary
    import capo_qbusiness.types.amazon_resource_name
    import capo_qbusiness.types.application
    import capo_qbusiness.types.application_id
    import capo_qbusiness.types.application_name
    import capo_qbusiness.types.associate_permission_request
    import capo_qbusiness.types.associate_permission_response
    import capo_qbusiness.types.attachment
    import capo_qbusiness.types.attachment_id
    import capo_qbusiness.types.attachments_configuration
    import capo_qbusiness.types.attachments_input
    import capo_qbusiness.types.attribute_filter
    import capo_qbusiness.types.auth_challenge_response
    import capo_qbusiness.types.auto_subscription_configuration
    import capo_qbusiness.types.batch_delete_document_request
    import capo_qbusiness.types.batch_delete_document_response
    import capo_qbusiness.types.batch_put_document_request
    import capo_qbusiness.types.batch_put_document_response
    import capo_qbusiness.types.blocked_phrases_configuration_update
    import capo_qbusiness.types.browser_extension_configuration
    import capo_qbusiness.types.cancel_subscription_request
    import capo_qbusiness.types.cancel_subscription_response
    import capo_qbusiness.types.chat_input
    import capo_qbusiness.types.chat_input_stream
    import capo_qbusiness.types.chat_mode
    import capo_qbusiness.types.chat_mode_configuration
    import capo_qbusiness.types.chat_output
    import capo_qbusiness.types.chat_response_configuration
    import capo_qbusiness.types.chat_response_configuration_id
    import capo_qbusiness.types.chat_sync_input
    import capo_qbusiness.types.chat_sync_output
    import capo_qbusiness.types.check_document_access_request
    import capo_qbusiness.types.check_document_access_response
    import capo_qbusiness.types.client_ids_for_oidc
    import capo_qbusiness.types.client_token
    import capo_qbusiness.types.content_source
    import capo_qbusiness.types.conversation
    import capo_qbusiness.types.conversation_id
    import capo_qbusiness.types.create_anonymous_web_experience_url_request
    import capo_qbusiness.types.create_anonymous_web_experience_url_response
    import capo_qbusiness.types.create_application_request
    import capo_qbusiness.types.create_application_response
    import capo_qbusiness.types.create_chat_response_configuration_request
    import capo_qbusiness.types.create_chat_response_configuration_response
    import capo_qbusiness.types.create_data_accessor_request
    import capo_qbusiness.types.create_data_accessor_response
    import capo_qbusiness.types.create_data_source_request
    import capo_qbusiness.types.create_data_source_response
    import capo_qbusiness.types.create_index_request
    import capo_qbusiness.types.create_index_response
    import capo_qbusiness.types.create_plugin_request
    import capo_qbusiness.types.create_plugin_response
    import capo_qbusiness.types.create_retriever_request
    import capo_qbusiness.types.create_retriever_response
    import capo_qbusiness.types.create_subscription_request
    import capo_qbusiness.types.create_subscription_response
    import capo_qbusiness.types.create_user_request
    import capo_qbusiness.types.create_user_response
    import capo_qbusiness.types.create_web_experience_request
    import capo_qbusiness.types.create_web_experience_response
    import capo_qbusiness.types.creator_mode_configuration
    import capo_qbusiness.types.custom_plugin_configuration
    import capo_qbusiness.types.customization_configuration
    import capo_qbusiness.types.data_accessor
    import capo_qbusiness.types.data_accessor_authentication_detail
    import capo_qbusiness.types.data_accessor_id
    import capo_qbusiness.types.data_accessor_name
    import capo_qbusiness.types.data_source
    import capo_qbusiness.types.data_source_configuration
    import capo_qbusiness.types.data_source_id
    import capo_qbusiness.types.data_source_ids
    import capo_qbusiness.types.data_source_name
    import capo_qbusiness.types.data_source_sync_job
    import capo_qbusiness.types.data_source_sync_job_status
    import capo_qbusiness.types.data_source_vpc_configuration
    import capo_qbusiness.types.delete_application_request
    import capo_qbusiness.types.delete_application_response
    import capo_qbusiness.types.delete_attachment_request
    import capo_qbusiness.types.delete_attachment_response
    import capo_qbusiness.types.delete_chat_controls_configuration_request
    import capo_qbusiness.types.delete_chat_controls_configuration_response
    import capo_qbusiness.types.delete_chat_response_configuration_request
    import capo_qbusiness.types.delete_chat_response_configuration_response
    import capo_qbusiness.types.delete_conversation_request
    import capo_qbusiness.types.delete_conversation_response
    import capo_qbusiness.types.delete_data_accessor_request
    import capo_qbusiness.types.delete_data_accessor_response
    import capo_qbusiness.types.delete_data_source_request
    import capo_qbusiness.types.delete_data_source_response
    import capo_qbusiness.types.delete_documents
    import capo_qbusiness.types.delete_group_request
    import capo_qbusiness.types.delete_group_response
    import capo_qbusiness.types.delete_index_request
    import capo_qbusiness.types.delete_index_response
    import capo_qbusiness.types.delete_plugin_request
    import capo_qbusiness.types.delete_plugin_response
    import capo_qbusiness.types.delete_retriever_request
    import capo_qbusiness.types.delete_retriever_response
    import capo_qbusiness.types.delete_user_request
    import capo_qbusiness.types.delete_user_response
    import capo_qbusiness.types.delete_web_experience_request
    import capo_qbusiness.types.delete_web_experience_response
    import capo_qbusiness.types.description
    import capo_qbusiness.types.disassociate_permission_request
    import capo_qbusiness.types.disassociate_permission_response
    import capo_qbusiness.types.display_name
    import capo_qbusiness.types.document_attribute_configurations
    import capo_qbusiness.types.document_details
    import capo_qbusiness.types.document_enrichment_configuration
    import capo_qbusiness.types.document_id
    import capo_qbusiness.types.documents
    import capo_qbusiness.types.encryption_configuration
    import capo_qbusiness.types.execution_id
    import capo_qbusiness.types.get_application_request
    import capo_qbusiness.types.get_application_response
    import capo_qbusiness.types.get_chat_controls_configuration_request
    import capo_qbusiness.types.get_chat_controls_configuration_response
    import capo_qbusiness.types.get_chat_response_configuration_request
    import capo_qbusiness.types.get_chat_response_configuration_response
    import capo_qbusiness.types.get_data_accessor_request
    import capo_qbusiness.types.get_data_accessor_response
    import capo_qbusiness.types.get_data_source_request
    import capo_qbusiness.types.get_data_source_response
    import capo_qbusiness.types.get_document_content_request
    import capo_qbusiness.types.get_document_content_response
    import capo_qbusiness.types.get_group_request
    import capo_qbusiness.types.get_group_response
    import capo_qbusiness.types.get_index_request
    import capo_qbusiness.types.get_index_response
    import capo_qbusiness.types.get_media_request
    import capo_qbusiness.types.get_media_response
    import capo_qbusiness.types.get_plugin_request
    import capo_qbusiness.types.get_plugin_response
    import capo_qbusiness.types.get_policy_request
    import capo_qbusiness.types.get_policy_response
    import capo_qbusiness.types.get_retriever_request
    import capo_qbusiness.types.get_retriever_response
    import capo_qbusiness.types.get_user_request
    import capo_qbusiness.types.get_user_response
    import capo_qbusiness.types.get_web_experience_request
    import capo_qbusiness.types.get_web_experience_response
    import capo_qbusiness.types.group_members
    import capo_qbusiness.types.group_name
    import capo_qbusiness.types.group_summary
    import capo_qbusiness.types.hallucination_reduction_configuration
    import capo_qbusiness.types.iam_identity_provider_arn
    import capo_qbusiness.types.identity_provider_configuration
    import capo_qbusiness.types.identity_type
    import capo_qbusiness.types.index
    import capo_qbusiness.types.index_capacity_configuration
    import capo_qbusiness.types.index_id
    import capo_qbusiness.types.index_name
    import capo_qbusiness.types.index_type
    import capo_qbusiness.types.instance_arn
    import capo_qbusiness.types.integer
    import capo_qbusiness.types.list_applications_request
    import capo_qbusiness.types.list_applications_response
    import capo_qbusiness.types.list_attachments_request
    import capo_qbusiness.types.list_attachments_response
    import capo_qbusiness.types.list_chat_response_configurations_request
    import capo_qbusiness.types.list_chat_response_configurations_response
    import capo_qbusiness.types.list_conversations_request
    import capo_qbusiness.types.list_conversations_response
    import capo_qbusiness.types.list_data_accessors_request
    import capo_qbusiness.types.list_data_accessors_response
    import capo_qbusiness.types.list_data_source_sync_jobs_request
    import capo_qbusiness.types.list_data_source_sync_jobs_response
    import capo_qbusiness.types.list_data_sources_request
    import capo_qbusiness.types.list_data_sources_response
    import capo_qbusiness.types.list_documents_request
    import capo_qbusiness.types.list_documents_response
    import capo_qbusiness.types.list_groups_request
    import capo_qbusiness.types.list_groups_response
    import capo_qbusiness.types.list_indices_request
    import capo_qbusiness.types.list_indices_response
    import capo_qbusiness.types.list_messages_request
    import capo_qbusiness.types.list_messages_response
    import capo_qbusiness.types.list_plugin_actions_request
    import capo_qbusiness.types.list_plugin_actions_response
    import capo_qbusiness.types.list_plugin_type_actions_request
    import capo_qbusiness.types.list_plugin_type_actions_response
    import capo_qbusiness.types.list_plugin_type_metadata_request
    import capo_qbusiness.types.list_plugin_type_metadata_response
    import capo_qbusiness.types.list_plugins_request
    import capo_qbusiness.types.list_plugins_response
    import capo_qbusiness.types.list_retrievers_request
    import capo_qbusiness.types.list_retrievers_response
    import capo_qbusiness.types.list_subscriptions_request
    import capo_qbusiness.types.list_subscriptions_response
    import capo_qbusiness.types.list_tags_for_resource_request
    import capo_qbusiness.types.list_tags_for_resource_response
    import capo_qbusiness.types.list_web_experiences_request
    import capo_qbusiness.types.list_web_experiences_response
    import capo_qbusiness.types.max_results
    import capo_qbusiness.types.max_results_integer_for_get_topic_configurations
    import capo_qbusiness.types.max_results_integer_for_list_applications
    import capo_qbusiness.types.max_results_integer_for_list_attachments
    import capo_qbusiness.types.max_results_integer_for_list_conversations
    import capo_qbusiness.types.max_results_integer_for_list_data_accessors
    import capo_qbusiness.types.max_results_integer_for_list_data_sources
    import capo_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs
    import capo_qbusiness.types.max_results_integer_for_list_documents
    import capo_qbusiness.types.max_results_integer_for_list_groups_request
    import capo_qbusiness.types.max_results_integer_for_list_indices
    import capo_qbusiness.types.max_results_integer_for_list_messages
    import capo_qbusiness.types.max_results_integer_for_list_plugin_actions
    import capo_qbusiness.types.max_results_integer_for_list_plugin_type_actions
    import capo_qbusiness.types.max_results_integer_for_list_plugin_type_metadata
    import capo_qbusiness.types.max_results_integer_for_list_plugins
    import capo_qbusiness.types.max_results_integer_for_list_retrievers_request
    import capo_qbusiness.types.max_results_integer_for_list_subscriptions
    import capo_qbusiness.types.max_results_integer_for_list_web_experiences_request
    import capo_qbusiness.types.media_extraction_configuration
    import capo_qbusiness.types.media_id
    import capo_qbusiness.types.membership_type
    import capo_qbusiness.types.message
    import capo_qbusiness.types.message_id
    import capo_qbusiness.types.message_usefulness_feedback
    import capo_qbusiness.types.next_token
    import capo_qbusiness.types.next_token1500
    import capo_qbusiness.types.orchestration_configuration
    import capo_qbusiness.types.output_format
    import capo_qbusiness.types.permission_conditions
    import capo_qbusiness.types.personalization_configuration
    import capo_qbusiness.types.plugin
    import capo_qbusiness.types.plugin_auth_configuration
    import capo_qbusiness.types.plugin_id
    import capo_qbusiness.types.plugin_name
    import capo_qbusiness.types.plugin_state
    import capo_qbusiness.types.plugin_type
    import capo_qbusiness.types.plugin_type_metadata_summary
    import capo_qbusiness.types.principal_role_arn
    import capo_qbusiness.types.put_feedback_request
    import capo_qbusiness.types.put_group_request
    import capo_qbusiness.types.put_group_response
    import capo_qbusiness.types.q_apps_configuration
    import capo_qbusiness.types.q_iam_actions
    import capo_qbusiness.types.query_text
    import capo_qbusiness.types.quick_sight_configuration
    import capo_qbusiness.types.relevant_content
    import capo_qbusiness.types.response_configurations
    import capo_qbusiness.types.response_scope
    import capo_qbusiness.types.retriever
    import capo_qbusiness.types.retriever_configuration
    import capo_qbusiness.types.retriever_id
    import capo_qbusiness.types.retriever_name
    import capo_qbusiness.types.retriever_type
    import capo_qbusiness.types.role_arn
    import capo_qbusiness.types.search_relevant_content_request
    import capo_qbusiness.types.search_relevant_content_response
    import capo_qbusiness.types.session_duration_in_minutes
    import capo_qbusiness.types.start_data_source_sync_job_request
    import capo_qbusiness.types.start_data_source_sync_job_response
    import capo_qbusiness.types.statement_id
    import capo_qbusiness.types.stop_data_source_sync_job_request
    import capo_qbusiness.types.stop_data_source_sync_job_response
    import capo_qbusiness.types.string
    import capo_qbusiness.types.subscription
    import capo_qbusiness.types.subscription_id
    import capo_qbusiness.types.subscription_principal
    import capo_qbusiness.types.subscription_type
    import capo_qbusiness.types.sync_schedule
    import capo_qbusiness.types.system_message_id
    import capo_qbusiness.types.tag_keys
    import capo_qbusiness.types.tag_resource_request
    import capo_qbusiness.types.tag_resource_response
    import capo_qbusiness.types.tags
    import capo_qbusiness.types.timestamp
    import capo_qbusiness.types.topic_configuration
    import capo_qbusiness.types.topic_configurations
    import capo_qbusiness.types.untag_resource_request
    import capo_qbusiness.types.untag_resource_response
    import capo_qbusiness.types.update_application_request
    import capo_qbusiness.types.update_application_response
    import capo_qbusiness.types.update_chat_controls_configuration_request
    import capo_qbusiness.types.update_chat_controls_configuration_response
    import capo_qbusiness.types.update_chat_response_configuration_request
    import capo_qbusiness.types.update_chat_response_configuration_response
    import capo_qbusiness.types.update_data_accessor_request
    import capo_qbusiness.types.update_data_accessor_response
    import capo_qbusiness.types.update_data_source_request
    import capo_qbusiness.types.update_data_source_response
    import capo_qbusiness.types.update_index_request
    import capo_qbusiness.types.update_index_response
    import capo_qbusiness.types.update_plugin_request
    import capo_qbusiness.types.update_plugin_response
    import capo_qbusiness.types.update_retriever_request
    import capo_qbusiness.types.update_retriever_response
    import capo_qbusiness.types.update_subscription_request
    import capo_qbusiness.types.update_subscription_response
    import capo_qbusiness.types.update_user_request
    import capo_qbusiness.types.update_user_response
    import capo_qbusiness.types.update_web_experience_request
    import capo_qbusiness.types.update_web_experience_response
    import capo_qbusiness.types.url
    import capo_qbusiness.types.user_aliases
    import capo_qbusiness.types.user_groups
    import capo_qbusiness.types.user_id
    import capo_qbusiness.types.user_message
    import capo_qbusiness.types.web_experience
    import capo_qbusiness.types.web_experience_auth_configuration
    import capo_qbusiness.types.web_experience_id
    import capo_qbusiness.types.web_experience_origins
    import capo_qbusiness.types.web_experience_sample_prompts_control_mode
    import capo_qbusiness.types.web_experience_subtitle
    import capo_qbusiness.types.web_experience_title
    import capo_qbusiness.types.web_experience_welcome_message


class QBusinessClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class QBusinessClient:
    """A client for the ``QBusiness`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        region: The value of the ``AWS::Region`` endpoint parameter.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        credentials: Credentials | None = None,
        credentials_provider: CredentialsProvider | None = None,
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
        self._config = QBusinessClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.application_resource = ApplicationResource(self)

    def operation_options(
        self, config_overrides: Optional[QBusinessClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: QBusinessClientConfig = config_overrides or {}
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
            region=overrides.get("region", self._config.get("region")),
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def associate_permission(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        statement_id: "capo_qbusiness.types.statement_id.StatementId",
        actions: "capo_qbusiness.types.q_iam_actions.QIamActions",
        principal: "capo_qbusiness.types.principal_role_arn.PrincipalRoleArn",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        conditions: Optional[
            "capo_qbusiness.types.permission_conditions.PermissionConditions"
        ] = None,
    ) -> (
        "capo_qbusiness.types.associate_permission_response.AssociatePermissionResponse"
    ):
        """<p>Adds or updates a permission policy for a Amazon Q Business application, allowing cross-account access for an ISV. This operation creates a new policy statement for the specified Amazon Q Business application. The policy statement defines the IAM actions that the ISV is allowed to perform on the Amazon Q Business application's resources.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            statement_id: <p>A unique identifier for the policy statement.</p>
            actions: <p>The list of Amazon Q Business actions that the ISV is allowed to perform.</p>
            conditions: <p>The conditions that restrict when the permission is effective. These conditions can be used to limit the permission based on specific attributes of the request.</p>
            principal: <p>The Amazon Resource Name of the IAM role for the ISV that is being granted permission.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.associate_permission_request.AssociatePermissionRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.associate_permission_response.AssociatePermissionResponse"
        ]:
            import capo_qbusiness._operations.expert_q.associate_permission

            output, http_response = (
                capo_qbusiness._operations.expert_q.associate_permission.associate_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.associate_permission_request.AssociatePermissionRequest = {
            "application_id": application_id,
            "statement_id": statement_id,
            "actions": actions,
            "principal": principal,
        }
        if conditions is not None:
            input_["conditions"] = conditions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_delete_document(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        documents: "capo_qbusiness.types.delete_documents.DeleteDocuments",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_sync_id: Optional[
            "capo_qbusiness.types.execution_id.ExecutionId"
        ] = None,
    ) -> "capo_qbusiness.types.batch_delete_document_response.BatchDeleteDocumentResponse":
        """<p>Asynchronously deletes one or more documents added using the <code>BatchPutDocument</code> API from an Amazon Q Business index.</p> <p>You can see the progress of the deletion, and any error messages related to the process, by using CloudWatch.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            index_id: <p>The identifier of the Amazon Q Business index that contains the documents to delete.</p>
            documents: <p>Documents deleted from the Amazon Q Business index.</p>
            data_source_sync_id: <p>The identifier of the data source sync during which the documents were deleted.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.batch_delete_document_request.BatchDeleteDocumentRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.batch_delete_document_response.BatchDeleteDocumentResponse"
        ]:
            import capo_qbusiness._operations.expert_q.batch_delete_document

            output, http_response = (
                capo_qbusiness._operations.expert_q.batch_delete_document.batch_delete_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.batch_delete_document_request.BatchDeleteDocumentRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "documents": documents,
        }
        if data_source_sync_id is not None:
            input_["data_source_sync_id"] = data_source_sync_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_put_document(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        documents: "capo_qbusiness.types.documents.Documents",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        data_source_sync_id: Optional[
            "capo_qbusiness.types.execution_id.ExecutionId"
        ] = None,
    ) -> "capo_qbusiness.types.batch_put_document_response.BatchPutDocumentResponse":
        """<p>Adds one or more documents to an Amazon Q Business index.</p> <p>You use this API to:</p> <ul> <li> <p>ingest your structured and unstructured documents and documents stored in an Amazon S3 bucket into an Amazon Q Business index.</p> </li> <li> <p>add custom attributes to documents in an Amazon Q Business index.</p> </li> <li> <p>attach an access control list to the documents added to an Amazon Q Business index.</p> </li> </ul> <p>You can see the progress of the deletion, and any error messages related to the process, by using CloudWatch.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            index_id: <p>The identifier of the Amazon Q Business index to add the documents to. </p>
            documents: <p>One or more documents to add to the index.</p> <important> <p>Ensure that the name of your document doesn't contain any confidential information. Amazon Q Business returns document names in chat responses and citations when relevant.</p> </important>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access your S3 bucket.</p>
            data_source_sync_id: <p>The identifier of the data source sync during which the documents were added.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.batch_put_document_request.BatchPutDocumentRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.batch_put_document_response.BatchPutDocumentResponse"
        ]:
            import capo_qbusiness._operations.expert_q.batch_put_document

            output, http_response = (
                capo_qbusiness._operations.expert_q.batch_put_document.batch_put_document(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.batch_put_document_request.BatchPutDocumentRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "documents": documents,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if data_source_sync_id is not None:
            input_["data_source_sync_id"] = data_source_sync_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_subscription(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        subscription_id: "capo_qbusiness.types.subscription_id.SubscriptionId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.cancel_subscription_response.CancelSubscriptionResponse":
        """<p>Unsubscribes a user or a group from their pricing tier in an Amazon Q Business application. An unsubscribed user or group loses all Amazon Q Business feature access at the start of next month. </p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application for which the subscription is being cancelled.</p>
            subscription_id: <p>The identifier of the Amazon Q Business subscription being cancelled.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.cancel_subscription_request.CancelSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.cancel_subscription_response.CancelSubscriptionResponse"
        ]:
            import capo_qbusiness._operations.expert_q.cancel_subscription

            output, http_response = (
                capo_qbusiness._operations.expert_q.cancel_subscription.cancel_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.cancel_subscription_request.CancelSubscriptionRequest = {
            "application_id": application_id,
            "subscription_id": subscription_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def chat(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        user_groups: Optional["capo_qbusiness.types.user_groups.UserGroups"] = None,
        conversation_id: Optional[
            "capo_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        parent_message_id: Optional["capo_qbusiness.types.message_id.MessageId"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        input_stream: Optional[
            "Iterator[capo_qbusiness.types.chat_input_stream._ChatInputStream] | capo_qbusiness.types.chat_input_stream._ChatInputStream"
        ] = None,
    ) -> "Generator[capo_qbusiness.types.chat_output.ChatOutput]":
        """<p>Starts or continues a streaming Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to a streaming Amazon Q Business conversation.</p>
            user_id: <p>The identifier of the user attached to the chat input. </p>
            user_groups: <p>The group names that a user associated with the chat input belongs to.</p>
            conversation_id: <p>The identifier of the Amazon Q Business conversation.</p>
            parent_message_id: <p>The identifier used to associate a user message with a AI generated response.</p>
            client_token: <p>A token that you provide to identify the chat input.</p>
            input_stream: <p>The streaming input for the <code>Chat</code> API.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.external_resource_exception.ExternalResourceException: <p>An external resource that you configured with your application is returning errors and preventing this operation from succeeding. Fix those errors and try again. </p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.chat_input.ChatInput]",
        ) -> OperationResponse["capo_qbusiness.types.chat_output.ChatOutput"]:
            import capo_qbusiness._operations.expert_q.chat

            output, http_response = capo_qbusiness._operations.expert_q.chat.chat(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.chat_input.ChatInput = {
            "application_id": application_id
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if user_groups is not None:
            input_["user_groups"] = user_groups
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        if parent_message_id is not None:
            input_["parent_message_id"] = parent_message_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if input_stream is not None:
            input_["input_stream"] = ensure_sync_iterator(input_stream)

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def chat_sync(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        user_groups: Optional["capo_qbusiness.types.user_groups.UserGroups"] = None,
        user_message: Optional["capo_qbusiness.types.user_message.UserMessage"] = None,
        attachments: Optional[
            "capo_qbusiness.types.attachments_input.AttachmentsInput"
        ] = None,
        action_execution: Optional[
            "capo_qbusiness.types.action_execution.ActionExecution"
        ] = None,
        auth_challenge_response: Optional[
            "capo_qbusiness.types.auth_challenge_response.AuthChallengeResponse"
        ] = None,
        conversation_id: Optional[
            "capo_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        parent_message_id: Optional["capo_qbusiness.types.message_id.MessageId"] = None,
        attribute_filter: Optional[
            "capo_qbusiness.types.attribute_filter.AttributeFilter"
        ] = None,
        chat_mode: Optional["capo_qbusiness.types.chat_mode.ChatMode"] = None,
        chat_mode_configuration: Optional[
            "capo_qbusiness.types.chat_mode_configuration.ChatModeConfiguration"
        ] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
    ) -> "capo_qbusiness.types.chat_sync_output.ChatSyncOutput":
        """<p>Starts or continues a non-streaming Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the Amazon Q Business conversation.</p>
            user_id: <p>The identifier of the user attached to the chat input.</p>
            user_groups: <p>The group names that a user associated with the chat input belongs to.</p>
            user_message: <p>A end user message in a conversation.</p>
            attachments: <p>A list of files uploaded directly during chat. You can upload a maximum of 5 files of upto 10 MB each.</p>
            action_execution: <p>A request from an end user to perform an Amazon Q Business plugin action.</p>
            auth_challenge_response: <p>An authentication verification event response by a third party authentication server to Amazon Q Business.</p>
            conversation_id: <p>The identifier of the Amazon Q Business conversation.</p>
            parent_message_id: <p>The identifier of the previous system message in a conversation.</p>
            attribute_filter: <p>Enables filtering of Amazon Q Business web experience responses based on document attributes or metadata fields.</p>
            chat_mode: <p>The <code>chatMode</code> parameter determines the chat modes available to Amazon Q Business users:</p> <ul> <li> <p> <code>RETRIEVAL_MODE</code> - If you choose this mode, Amazon Q generates responses solely from the data sources connected and indexed by the application. If an answer is not found in the data sources or there are no data sources available, Amazon Q will respond with a "<i>No Answer Found</i>" message, unless LLM knowledge has been enabled. In that case, Amazon Q will generate a response from the LLM knowledge</p> </li> <li> <p> <code>CREATOR_MODE</code> - By selecting this mode, you can choose to generate responses only from the LLM knowledge. You can also attach files and have Amazon Q generate a response based on the data in those files. If the attached files do not contain an answer for the query, Amazon Q will automatically fall back to generating a response from the LLM knowledge.</p> </li> <li> <p> <code>PLUGIN_MODE</code> - By selecting this mode, users can choose to use plugins in chat to get their responses.</p> </li> </ul> <note> <p>If none of the modes are selected, Amazon Q will only respond using the information from the attached files.</p> </note> <p>For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/guardrails.html">Admin controls and guardrails</a>, <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/plugins.html">Plugins</a>, and <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/using-web-experience.html#chat-source-scope">Response sources</a>.</p>
            chat_mode_configuration: <p>The chat mode configuration for an Amazon Q Business application.</p>
            client_token: <p>A token that you provide to identify a chat request.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.external_resource_exception.ExternalResourceException: <p>An external resource that you configured with your application is returning errors and preventing this operation from succeeding. Fix those errors and try again. </p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.chat_sync_input.ChatSyncInput]",
        ) -> OperationResponse["capo_qbusiness.types.chat_sync_output.ChatSyncOutput"]:
            import capo_qbusiness._operations.expert_q.chat_sync

            output, http_response = (
                capo_qbusiness._operations.expert_q.chat_sync.chat_sync(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.chat_sync_input.ChatSyncInput = {
            "application_id": application_id
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if user_groups is not None:
            input_["user_groups"] = user_groups
        if user_message is not None:
            input_["user_message"] = user_message
        if attachments is not None:
            input_["attachments"] = attachments
        if action_execution is not None:
            input_["action_execution"] = action_execution
        if auth_challenge_response is not None:
            input_["auth_challenge_response"] = auth_challenge_response
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        if parent_message_id is not None:
            input_["parent_message_id"] = parent_message_id
        if attribute_filter is not None:
            input_["attribute_filter"] = attribute_filter
        if chat_mode is not None:
            input_["chat_mode"] = chat_mode
        if chat_mode_configuration is not None:
            input_["chat_mode_configuration"] = chat_mode_configuration
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

    def check_document_access(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        user_id: "capo_qbusiness.types.string.String",
        document_id: "capo_qbusiness.types.document_id.DocumentId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_id: Optional[
            "capo_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
    ) -> "capo_qbusiness.types.check_document_access_response.CheckDocumentAccessResponse":
        """<p>Verifies if a user has access permissions for a specified document and returns the actual ACL attached to the document. Resolves user access on the document via user aliases and groups when verifying user access.</p>

        Args:
            application_id: <p>The unique identifier of the application. This is required to identify the specific Amazon Q Business application context for the document access check.</p>
            index_id: <p>The unique identifier of the index. Used to locate the correct index within the application where the document is stored.</p>
            user_id: <p>The unique identifier of the user. Used to check the access permissions for this specific user against the document's ACL.</p>
            document_id: <p>The unique identifier of the document. Specifies which document's access permissions are being checked.</p>
            data_source_id: <p>The unique identifier of the data source. Identifies the specific data source from which the document originates. Should not be used when a document is uploaded directly with BatchPutDocument, as no dataSourceId is available or necessary. </p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.check_document_access_request.CheckDocumentAccessRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.check_document_access_response.CheckDocumentAccessResponse"
        ]:
            import capo_qbusiness._operations.expert_q.check_document_access

            output, http_response = (
                capo_qbusiness._operations.expert_q.check_document_access.check_document_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.check_document_access_request.CheckDocumentAccessRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "user_id": user_id,
            "document_id": document_id,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_anonymous_web_experience_url(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        web_experience_id: "capo_qbusiness.types.web_experience_id.WebExperienceId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        session_duration_in_minutes: Optional[
            "capo_qbusiness.types.session_duration_in_minutes.SessionDurationInMinutes"
        ] = None,
    ) -> "capo_qbusiness.types.create_anonymous_web_experience_url_response.CreateAnonymousWebExperienceUrlResponse":
        """<p>Creates a unique URL for anonymous Amazon Q Business web experience. This URL can only be used once and must be used within 5 minutes after it's generated.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application environment attached to the web experience.</p>
            web_experience_id: <p>The identifier of the web experience.</p>
            session_duration_in_minutes: <p>The duration of the session associated with the unique URL for the web experience.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_anonymous_web_experience_url_request.CreateAnonymousWebExperienceUrlRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_anonymous_web_experience_url_response.CreateAnonymousWebExperienceUrlResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_anonymous_web_experience_url

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_anonymous_web_experience_url.create_anonymous_web_experience_url(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_anonymous_web_experience_url_request.CreateAnonymousWebExperienceUrlRequest = {
            "application_id": application_id,
            "web_experience_id": web_experience_id,
        }
        if session_duration_in_minutes is not None:
            input_["session_duration_in_minutes"] = session_duration_in_minutes

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_chat_response_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        display_name: "capo_qbusiness.types.display_name.DisplayName",
        response_configurations: "capo_qbusiness.types.response_configurations.ResponseConfigurations",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        client_token: Optional["capo_qbusiness.types.string.String"] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
    ) -> "capo_qbusiness.types.create_chat_response_configuration_response.CreateChatResponseConfigurationResponse":
        """<p>Creates a new chat response configuration for an Amazon Q Business application. This operation establishes a set of parameters that define how the system generates and formats responses to user queries in chat interactions.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application for which to create the new chat response configuration.</p>
            display_name: <p>A human-readable name for the new chat response configuration, making it easier to identify and manage among multiple configurations.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same configuration from being created multiple times if retries occur.</p>
            response_configurations: <p>A collection of response configuration settings that define how Amazon Q Business will generate and format responses to user queries in chat interactions.</p>
            tags: <p>A list of key-value pairs to apply as tags to the new chat response configuration, enabling categorization and management of resources across Amazon Web Services services.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_chat_response_configuration_request.CreateChatResponseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_chat_response_configuration_response.CreateChatResponseConfigurationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_chat_response_configuration

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_chat_response_configuration.create_chat_response_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_chat_response_configuration_request.CreateChatResponseConfigurationRequest = {
            "application_id": application_id,
            "display_name": display_name,
            "response_configurations": response_configurations,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_subscription(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        principal: "capo_qbusiness.types.subscription_principal.SubscriptionPrincipal",
        type: "capo_qbusiness.types.subscription_type.SubscriptionType",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
    ) -> "capo_qbusiness.types.create_subscription_response.CreateSubscriptionResponse":
        """<p>Subscribes an IAM Identity Center user or a group to a pricing tier for an Amazon Q Business application.</p> <p>Amazon Q Business offers two subscription tiers: <code>Q_LITE</code> and <code>Q_BUSINESS</code>. Subscription tier determines feature access for the user. For more information on subscriptions and pricing tiers, see <a href="https://aws.amazon.com/q/business/pricing/">Amazon Q Business pricing</a>.</p> <note> <p>For an example IAM role policy for assigning subscriptions, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/setting-up.html#permissions">Set up required permissions</a> in the Amazon Q Business User Guide.</p> </note>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application the subscription should be added to.</p>
            principal: <p>The IAM Identity Center <code>UserId</code> or <code>GroupId</code> of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application.</p>
            type: <p>The type of Amazon Q Business subscription you want to create.</p>
            client_token: <p>A token that you provide to identify the request to create a subscription for your Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_subscription_request.CreateSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_subscription_response.CreateSubscriptionResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_subscription

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_subscription.create_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_subscription_request.CreateSubscriptionRequest = {
            "application_id": application_id,
            "principal": principal,
            "type": type,
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

    def create_user(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        user_id: "capo_qbusiness.types.string.String",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_aliases: Optional["capo_qbusiness.types.user_aliases.UserAliases"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
    ) -> "capo_qbusiness.types.create_user_response.CreateUserResponse":
        """<p>Creates a universally unique identifier (UUID) mapped to a list of local user ids within an application.</p>

        Args:
            application_id: <p>The identifier of the application for which the user mapping will be created.</p>
            user_id: <p>The user emails attached to a user mapping.</p>
            user_aliases: <p>The list of user aliases in the mapping.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Q Business user mapping.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_user_request.CreateUserRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_user_response.CreateUserResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_user

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_user.create_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_user_request.CreateUserRequest = {
            "application_id": application_id,
            "user_id": user_id,
        }
        if user_aliases is not None:
            input_["user_aliases"] = user_aliases
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

    def delete_attachment(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        conversation_id: "capo_qbusiness.types.conversation_id.ConversationId",
        attachment_id: "capo_qbusiness.types.attachment_id.AttachmentId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
    ) -> "capo_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse":
        """<p>Deletes an attachment associated with a specific Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The unique identifier for the Amazon Q Business application environment.</p>
            conversation_id: <p>The unique identifier of the conversation.</p>
            attachment_id: <p>The unique identifier for the attachment.</p>
            user_id: <p>The unique identifier of the user involved in the conversation.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_attachment_request.DeleteAttachmentRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_attachment_response.DeleteAttachmentResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_attachment

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_attachment.delete_attachment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_attachment_request.DeleteAttachmentRequest = {
            "application_id": application_id,
            "conversation_id": conversation_id,
            "attachment_id": attachment_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_chat_controls_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_chat_controls_configuration_response.DeleteChatControlsConfigurationResponse":
        """<p>Deletes chat controls configured for an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the application the chat controls have been configured for.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_chat_controls_configuration_request.DeleteChatControlsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_chat_controls_configuration_response.DeleteChatControlsConfigurationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_chat_controls_configuration

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_chat_controls_configuration.delete_chat_controls_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_chat_controls_configuration_request.DeleteChatControlsConfigurationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_chat_response_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        chat_response_configuration_id: "capo_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_chat_response_configuration_response.DeleteChatResponseConfigurationResponse":
        """<p>Deletes a specified chat response configuration from an Amazon Q Business application.</p>

        Args:
            application_id: <p>The unique identifier of theAmazon Q Business application from which to delete the chat response configuration.</p>
            chat_response_configuration_id: <p>The unique identifier of the chat response configuration to delete from the specified application. </p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_chat_response_configuration_request.DeleteChatResponseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_chat_response_configuration_response.DeleteChatResponseConfigurationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_chat_response_configuration

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_chat_response_configuration.delete_chat_response_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_chat_response_configuration_request.DeleteChatResponseConfigurationRequest = {
            "application_id": application_id,
            "chat_response_configuration_id": chat_response_configuration_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_conversation(
        self,
        conversation_id: "capo_qbusiness.types.conversation_id.ConversationId",
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
    ) -> "capo_qbusiness.types.delete_conversation_response.DeleteConversationResponse":
        """<p>Deletes an Amazon Q Business web experience conversation.</p>

        Args:
            conversation_id: <p>The identifier of the Amazon Q Business web experience conversation being deleted.</p>
            application_id: <p>The identifier of the Amazon Q Business application associated with the conversation.</p>
            user_id: <p>The identifier of the user who is deleting the conversation.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_conversation_request.DeleteConversationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_conversation_response.DeleteConversationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_conversation

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_conversation.delete_conversation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_conversation_request.DeleteConversationRequest = {
            "conversation_id": conversation_id,
            "application_id": application_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_group(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        group_name: "capo_qbusiness.types.group_name.GroupName",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_id: Optional[
            "capo_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
    ) -> "capo_qbusiness.types.delete_group_response.DeleteGroupResponse":
        """<p>Deletes a group so that all users and sub groups that belong to the group can no longer access documents only available to that group. For example, after deleting the group "Summer Interns", all interns who belonged to that group no longer see intern-only documents in their chat results. </p> <p>If you want to delete, update, or replace users or sub groups of a group, you need to use the <code>PutGroup</code> operation. For example, if a user in the group "Engineering" leaves the engineering team and another user takes their place, you provide an updated list of users or sub groups that belong to the "Engineering" group when calling <code>PutGroup</code>.</p>

        Args:
            application_id: <p>The identifier of the application in which the group mapping belongs.</p>
            index_id: <p>The identifier of the index you want to delete the group from.</p>
            group_name: <p>The name of the group you want to delete.</p>
            data_source_id: <p>The identifier of the data source linked to the group</p> <p>A group can be tied to multiple data sources. You can delete a group from accessing documents in a certain data source. For example, the groups "Research", "Engineering", and "Sales and Marketing" are all tied to the company's documents stored in the data sources Confluence and Salesforce. You want to delete "Research" and "Engineering" groups from Salesforce, so that these groups cannot access customer-related documents stored in Salesforce. Only "Sales and Marketing" should access documents in the Salesforce data source.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_group_request.DeleteGroupRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_group_response.DeleteGroupResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_group

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_group.delete_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_group_request.DeleteGroupRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "group_name": group_name,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_user(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        user_id: "capo_qbusiness.types.string.String",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_user_response.DeleteUserResponse":
        """<p>Deletes a user by email id.</p>

        Args:
            application_id: <p>The identifier of the application from which the user is being deleted.</p>
            user_id: <p>The user email being deleted.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_user_request.DeleteUserRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_user_response.DeleteUserResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_user

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_user.delete_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_user_request.DeleteUserRequest = {
            "application_id": application_id,
            "user_id": user_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_permission(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        statement_id: "capo_qbusiness.types.string.String",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.disassociate_permission_response.DisassociatePermissionResponse":
        """<p>Removes a permission policy from a Amazon Q Business application, revoking the cross-account access that was previously granted to an ISV. This operation deletes the specified policy statement from the application's permission policy.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            statement_id: <p>The statement ID of the permission to remove.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.disassociate_permission_request.DisassociatePermissionRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.disassociate_permission_response.DisassociatePermissionResponse"
        ]:
            import capo_qbusiness._operations.expert_q.disassociate_permission

            output, http_response = (
                capo_qbusiness._operations.expert_q.disassociate_permission.disassociate_permission(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.disassociate_permission_request.DisassociatePermissionRequest = {
            "application_id": application_id,
            "statement_id": statement_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_chat_controls_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_get_topic_configurations.MaxResultsIntegerForGetTopicConfigurations"
        ] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
    ) -> "capo_qbusiness.types.get_chat_controls_configuration_response.GetChatControlsConfigurationResponse":
        """<p>Gets information about chat controls configured for an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the application for which the chat controls are configured.</p>
            max_results: <p>The maximum number of configured chat controls to return.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business chat controls configured.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_chat_controls_configuration_request.GetChatControlsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_chat_controls_configuration_response.GetChatControlsConfigurationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_chat_controls_configuration

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_chat_controls_configuration.get_chat_controls_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_chat_controls_configuration_request.GetChatControlsConfigurationRequest = {
            "application_id": application_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_chat_controls_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_get_topic_configurations.MaxResultsIntegerForGetTopicConfigurations"
        ] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_qbusiness.types.topic_configuration.TopicConfiguration]":
        _token = next_token
        while True:
            _response = self.get_chat_controls_configuration(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("topic_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_chat_response_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        chat_response_configuration_id: "capo_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_chat_response_configuration_response.GetChatResponseConfigurationResponse":
        """<p>Retrieves detailed information about a specific chat response configuration from an Amazon Q Business application. This operation returns the complete configuration settings and metadata.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application containing the chat response configuration to retrieve.</p>
            chat_response_configuration_id: <p>The unique identifier of the chat response configuration to retrieve from the specified application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_chat_response_configuration_request.GetChatResponseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_chat_response_configuration_response.GetChatResponseConfigurationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_chat_response_configuration

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_chat_response_configuration.get_chat_response_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_chat_response_configuration_request.GetChatResponseConfigurationRequest = {
            "application_id": application_id,
            "chat_response_configuration_id": chat_response_configuration_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_document_content(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        document_id: "capo_qbusiness.types.document_id.DocumentId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_id: Optional[
            "capo_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        output_format: Optional[
            "capo_qbusiness.types.output_format.OutputFormat"
        ] = None,
    ) -> (
        "capo_qbusiness.types.get_document_content_response.GetDocumentContentResponse"
    ):
        """<p>Retrieves the content of a document that was ingested into Amazon Q Business. This API validates user authorization against document ACLs before returning a pre-signed URL for secure document access. You can download or view source documents referenced in chat responses through the URL.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application containing the document. This ensures the request is scoped to the correct application environment and its associated security policies.</p>
            index_id: <p>The identifier of the index where documents are indexed.</p>
            data_source_id: <p>The identifier of the data source from which the document was ingested. This field is not present if the document is ingested by directly calling the BatchPutDocument API. If the document is from a file-upload data source, the datasource will be "uploaded-docs-file-stat-datasourceid".</p>
            document_id: <p>The unique identifier of the document that is indexed via BatchPutDocument API or file-upload or connector sync. It is also found in chat or chatSync response.</p>
            output_format: <p>Document outputFormat. Defaults to RAW if not selected.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_document_content_request.GetDocumentContentRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_document_content_response.GetDocumentContentResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_document_content

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_document_content.get_document_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_document_content_request.GetDocumentContentRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "document_id": document_id,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        if output_format is not None:
            input_["output_format"] = output_format

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_group(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        group_name: "capo_qbusiness.types.group_name.GroupName",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_id: Optional[
            "capo_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
    ) -> "capo_qbusiness.types.get_group_response.GetGroupResponse":
        """<p>Describes a group by group name.</p>

        Args:
            application_id: <p>The identifier of the application id the group is attached to.</p>
            index_id: <p>The identifier of the index the group is attached to.</p>
            group_name: <p>The name of the group.</p>
            data_source_id: <p>The identifier of the data source the group is attached to.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_group_request.GetGroupRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_group_response.GetGroupResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_group

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_group.get_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_group_request.GetGroupRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "group_name": group_name,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_media(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        conversation_id: "capo_qbusiness.types.conversation_id.ConversationId",
        message_id: "capo_qbusiness.types.message_id.MessageId",
        media_id: "capo_qbusiness.types.media_id.MediaId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_media_response.GetMediaResponse":
        """<p>Returns the image bytes corresponding to a media object. If you have implemented your own application with the Chat and ChatSync APIs, and have enabled content extraction from visual data in Amazon Q Business, you use the GetMedia API operation to download the images so you can show them in your UI with responses.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/extracting-meaning-from-images.html">Extracting semantic meaning from images and visuals</a>.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business which contains the media object.</p>
            conversation_id: <p>The identifier of the Amazon Q Business conversation.</p>
            message_id: <p>The identifier of the Amazon Q Business message.</p>
            media_id: <p>The identifier of the media object. You can find this in the <code>sourceAttributions</code> returned by the <code>Chat</code>, <code>ChatSync</code>, and <code>ListMessages</code> API responses.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.media_too_large_exception.MediaTooLargeException: <p>The requested media object is too large to be returned.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_media_request.GetMediaRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_media_response.GetMediaResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_media

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_media.get_media(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_media_request.GetMediaRequest = {
            "application_id": application_id,
            "conversation_id": conversation_id,
            "message_id": message_id,
            "media_id": media_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves the current permission policy for a Amazon Q Business application. The policy is returned as a JSON-formatted string and defines the IAM actions that are allowed or denied for the application's resources.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_policy_request.GetPolicyRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_policy

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_policy_request.GetPolicyRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_user(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        user_id: "capo_qbusiness.types.string.String",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_user_response.GetUserResponse":
        """<p>Describes the universally unique identifier (UUID) associated with a local user in a data source.</p>

        Args:
            application_id: <p>The identifier of the application connected to the user.</p>
            user_id: <p>The user email address attached to the user.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_user_request.GetUserRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_user_response.GetUserResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_user

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_user.get_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_user_request.GetUserRequest = {
            "application_id": application_id,
            "user_id": user_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_attachments(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        conversation_id: Optional[
            "capo_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_attachments.MaxResultsIntegerForListAttachments"
        ] = None,
    ) -> "capo_qbusiness.types.list_attachments_response.ListAttachmentsResponse":
        """<p>Gets a list of attachments associated with an Amazon Q Business web experience or a list of attachements associated with a specific Amazon Q Business conversation.</p>

        Args:
            application_id: <p>The unique identifier for the Amazon Q Business application.</p>
            conversation_id: <p>The unique identifier of the Amazon Q Business web experience conversation.</p>
            user_id: <p>The unique identifier of the user involved in the Amazon Q Business web experience conversation.</p>
            next_token: <p>If the number of attachments returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of attachments.</p>
            max_results: <p>The maximum number of attachements to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_attachments_request.ListAttachmentsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_attachments_response.ListAttachmentsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_attachments

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_attachments.list_attachments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_attachments_request.ListAttachmentsRequest = {
            "application_id": application_id
        }
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        if user_id is not None:
            input_["user_id"] = user_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_attachments(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        conversation_id: Optional[
            "capo_qbusiness.types.conversation_id.ConversationId"
        ] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_attachments.MaxResultsIntegerForListAttachments"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.attachment.Attachment]":
        _token = next_token
        while True:
            _response = self.list_attachments(
                application_id,
                config_overrides=config_overrides,
                conversation_id=conversation_id,
                user_id=user_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("attachments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_chat_response_configurations(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        max_results: Optional["capo_qbusiness.types.integer.Integer"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
    ) -> "capo_qbusiness.types.list_chat_response_configurations_response.ListChatResponseConfigurationsResponse":
        """<p>Retrieves a list of all chat response configurations available in a specified Amazon Q Business application. This operation returns summary information about each configuration to help administrators manage and select appropriate response settings.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application for which to list available chat response configurations.</p>
            max_results: <p>The maximum number of chat response configurations to return in a single response. This parameter helps control pagination of results when many configurations exist.</p>
            next_token: <p>A pagination token used to retrieve the next set of results when the number of configurations exceeds the specified <code>maxResults</code> value.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_chat_response_configurations_request.ListChatResponseConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_chat_response_configurations_response.ListChatResponseConfigurationsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_chat_response_configurations

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_chat_response_configurations.list_chat_response_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_chat_response_configurations_request.ListChatResponseConfigurationsRequest = {
            "application_id": application_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_chat_response_configurations(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        max_results: Optional["capo_qbusiness.types.integer.Integer"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_qbusiness.types.chat_response_configuration.ChatResponseConfiguration]":
        _token = next_token
        while True:
            _response = self.list_chat_response_configurations(
                application_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("chat_response_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_conversations(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_conversations.MaxResultsIntegerForListConversations"
        ] = None,
    ) -> "capo_qbusiness.types.list_conversations_response.ListConversationsResponse":
        """<p>Lists one or more Amazon Q Business conversations.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            user_id: <p>The identifier of the user involved in the Amazon Q Business web experience conversation. </p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business conversations.</p>
            max_results: <p>The maximum number of Amazon Q Business conversations to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_conversations_request.ListConversationsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_conversations_response.ListConversationsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_conversations

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_conversations.list_conversations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_conversations_request.ListConversationsRequest = {
            "application_id": application_id
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_conversations(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_conversations.MaxResultsIntegerForListConversations"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.conversation.Conversation]":
        _token = next_token
        while True:
            _response = self.list_conversations(
                application_id,
                config_overrides=config_overrides,
                user_id=user_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("conversations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_data_source_sync_jobs(
        self,
        data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId",
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs.MaxResultsIntegerForListDataSourcesSyncJobs"
        ] = None,
        start_time: Optional["capo_qbusiness.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_qbusiness.types.timestamp.Timestamp"] = None,
        status_filter: Optional[
            "capo_qbusiness.types.data_source_sync_job_status.DataSourceSyncJobStatus"
        ] = None,
    ) -> "capo_qbusiness.types.list_data_source_sync_jobs_response.ListDataSourceSyncJobsResponse":
        """<p>Get information about an Amazon Q Business data source connector synchronization.</p>

        Args:
            data_source_id: <p> The identifier of the data source connector.</p>
            application_id: <p>The identifier of the Amazon Q Business application connected to the data source.</p>
            index_id: <p>The identifier of the index used with the Amazon Q Business data source connector.</p>
            next_token: <p>If the <code>maxResults</code> response was incpmplete because there is more data to retriever, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of responses.</p>
            max_results: <p>The maximum number of synchronization jobs to return in the response.</p>
            start_time: <p> The start time of the data source connector sync. </p>
            end_time: <p> The end time of the data source connector sync.</p>
            status_filter: <p>Only returns synchronization jobs with the <code>Status</code> field equal to the specified status.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_data_source_sync_jobs_request.ListDataSourceSyncJobsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_data_source_sync_jobs_response.ListDataSourceSyncJobsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_data_source_sync_jobs

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_data_source_sync_jobs.list_data_source_sync_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_data_source_sync_jobs_request.ListDataSourceSyncJobsRequest = {
            "data_source_id": data_source_id,
            "application_id": application_id,
            "index_id": index_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_source_sync_jobs(
        self,
        data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId",
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_data_sources_sync_jobs.MaxResultsIntegerForListDataSourcesSyncJobs"
        ] = None,
        start_time: Optional["capo_qbusiness.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_qbusiness.types.timestamp.Timestamp"] = None,
        status_filter: Optional[
            "capo_qbusiness.types.data_source_sync_job_status.DataSourceSyncJobStatus"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.data_source_sync_job.DataSourceSyncJob]":
        _token = next_token
        while True:
            _response = self.list_data_source_sync_jobs(
                data_source_id,
                application_id,
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                start_time=start_time,
                end_time=end_time,
                status_filter=status_filter,
            )
            _page = _resolve_path(_response, ("history",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_documents(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_ids: Optional[
            "capo_qbusiness.types.data_source_ids.DataSourceIds"
        ] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_documents.MaxResultsIntegerForListDocuments"
        ] = None,
    ) -> "capo_qbusiness.types.list_documents_response.ListDocumentsResponse":
        """<p>A list of documents attached to an index.</p>

        Args:
            application_id: <p>The identifier of the application id the documents are attached to.</p>
            index_id: <p>The identifier of the index the documents are attached to.</p>
            data_source_ids: <p>The identifier of the data sources the documents are attached to.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of documents.</p>
            max_results: <p>The maximum number of documents to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_documents_request.ListDocumentsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_documents_response.ListDocumentsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_documents

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_documents.list_documents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_documents_request.ListDocumentsRequest = {
            "application_id": application_id,
            "index_id": index_id,
        }
        if data_source_ids is not None:
            input_["data_source_ids"] = data_source_ids
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_documents(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_ids: Optional[
            "capo_qbusiness.types.data_source_ids.DataSourceIds"
        ] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_documents.MaxResultsIntegerForListDocuments"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.document_details.DocumentDetails]":
        _token = next_token
        while True:
            _response = self.list_documents(
                application_id,
                index_id,
                config_overrides=config_overrides,
                data_source_ids=data_source_ids,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("document_detail_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_groups(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        updated_earlier_than: "capo_qbusiness.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_id: Optional[
            "capo_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_groups_request.MaxResultsIntegerForListGroupsRequest"
        ] = None,
    ) -> "capo_qbusiness.types.list_groups_response.ListGroupsResponse":
        """<p>Provides a list of groups that are mapped to users.</p>

        Args:
            application_id: <p>The identifier of the application for getting a list of groups mapped to users.</p>
            index_id: <p>The identifier of the index for getting a list of groups mapped to users.</p>
            updated_earlier_than: <p>The timestamp identifier used for the latest <code>PUT</code> or <code>DELETE</code> action for mapping users to their groups.</p>
            data_source_id: <p>The identifier of the data source for getting a list of groups mapped to users.</p>
            next_token: <p>If the previous response was incomplete (because there is more data to retrieve), Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of groups that are mapped to users.</p>
            max_results: <p>The maximum number of returned groups that are mapped to users.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_groups_request.ListGroupsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_groups_response.ListGroupsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_groups

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_groups.list_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_groups_request.ListGroupsRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "updated_earlier_than": updated_earlier_than,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_groups(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        updated_earlier_than: "capo_qbusiness.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_id: Optional[
            "capo_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_groups_request.MaxResultsIntegerForListGroupsRequest"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.group_summary.GroupSummary]":
        _token = next_token
        while True:
            _response = self.list_groups(
                application_id,
                index_id,
                updated_earlier_than,
                config_overrides=config_overrides,
                data_source_id=data_source_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_messages(
        self,
        conversation_id: "capo_qbusiness.types.conversation_id.ConversationId",
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_messages.MaxResultsIntegerForListMessages"
        ] = None,
    ) -> "capo_qbusiness.types.list_messages_response.ListMessagesResponse":
        """<p>Gets a list of messages associated with an Amazon Q Business web experience.</p>

        Args:
            conversation_id: <p>The identifier of the Amazon Q Business web experience conversation.</p>
            application_id: <p>The identifier for the Amazon Q Business application.</p>
            user_id: <p>The identifier of the user involved in the Amazon Q Business web experience conversation.</p>
            next_token: <p>If the number of messages returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of messages.</p>
            max_results: <p>The maximum number of messages to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_messages_request.ListMessagesRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_messages_response.ListMessagesResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_messages

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_messages.list_messages(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_messages_request.ListMessagesRequest = {
            "conversation_id": conversation_id,
            "application_id": application_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_messages(
        self,
        conversation_id: "capo_qbusiness.types.conversation_id.ConversationId",
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_messages.MaxResultsIntegerForListMessages"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.message.Message]":
        _token = next_token
        while True:
            _response = self.list_messages(
                conversation_id,
                application_id,
                config_overrides=config_overrides,
                user_id=user_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("messages",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_plugin_actions(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        plugin_id: "capo_qbusiness.types.plugin_id.PluginId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugin_actions.MaxResultsIntegerForListPluginActions"
        ] = None,
    ) -> "capo_qbusiness.types.list_plugin_actions_response.ListPluginActionsResponse":
        """<p>Lists configured Amazon Q Business actions for a specific plugin in an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application the plugin is attached to.</p>
            plugin_id: <p>The identifier of the Amazon Q Business plugin.</p>
            next_token: <p>If the number of plugin actions returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of plugin actions.</p>
            max_results: <p>The maximum number of plugin actions to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_plugin_actions_request.ListPluginActionsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_plugin_actions_response.ListPluginActionsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_plugin_actions

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_plugin_actions.list_plugin_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_plugin_actions_request.ListPluginActionsRequest = {
            "application_id": application_id,
            "plugin_id": plugin_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_plugin_actions(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        plugin_id: "capo_qbusiness.types.plugin_id.PluginId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugin_actions.MaxResultsIntegerForListPluginActions"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = self.list_plugin_actions(
                application_id,
                plugin_id,
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

    def list_plugin_type_actions(
        self,
        plugin_type: "capo_qbusiness.types.plugin_type.PluginType",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugin_type_actions.MaxResultsIntegerForListPluginTypeActions"
        ] = None,
    ) -> "capo_qbusiness.types.list_plugin_type_actions_response.ListPluginTypeActionsResponse":
        """<p>Lists configured Amazon Q Business actions for any plugin type—both built-in and custom.</p>

        Args:
            plugin_type: <p>The type of the plugin.</p>
            next_token: <p>If the number of plugins returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of plugins.</p>
            max_results: <p>The maximum number of plugins to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_plugin_type_actions_request.ListPluginTypeActionsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_plugin_type_actions_response.ListPluginTypeActionsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_plugin_type_actions

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_plugin_type_actions.list_plugin_type_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_plugin_type_actions_request.ListPluginTypeActionsRequest = {
            "plugin_type": plugin_type
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_plugin_type_actions(
        self,
        plugin_type: "capo_qbusiness.types.plugin_type.PluginType",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugin_type_actions.MaxResultsIntegerForListPluginTypeActions"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = self.list_plugin_type_actions(
                plugin_type,
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

    def list_plugin_type_metadata(
        self,
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugin_type_metadata.MaxResultsIntegerForListPluginTypeMetadata"
        ] = None,
    ) -> "capo_qbusiness.types.list_plugin_type_metadata_response.ListPluginTypeMetadataResponse":
        """<p>Lists metadata for all Amazon Q Business plugin types.</p>

        Args:
            next_token: <p>If the metadata returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of metadata.</p>
            max_results: <p>The maximum number of plugin metadata items to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_plugin_type_metadata_request.ListPluginTypeMetadataRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_plugin_type_metadata_response.ListPluginTypeMetadataResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_plugin_type_metadata

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_plugin_type_metadata.list_plugin_type_metadata(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_plugin_type_metadata_request.ListPluginTypeMetadataRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_plugin_type_metadata(
        self,
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugin_type_metadata.MaxResultsIntegerForListPluginTypeMetadata"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.plugin_type_metadata_summary.PluginTypeMetadataSummary]":
        _token = next_token
        while True:
            _response = self.list_plugin_type_metadata(
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

    def list_subscriptions(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_subscriptions.MaxResultsIntegerForListSubscriptions"
        ] = None,
    ) -> "capo_qbusiness.types.list_subscriptions_response.ListSubscriptionsResponse":
        """<p> Lists all subscriptions created in an Amazon Q Business application. </p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the subscription.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business subscriptions.</p>
            max_results: <p>The maximum number of Amazon Q Business subscriptions to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_subscriptions_request.ListSubscriptionsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_subscriptions_response.ListSubscriptionsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_subscriptions

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_subscriptions.list_subscriptions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_subscriptions_request.ListSubscriptionsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_subscriptions(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_subscriptions.MaxResultsIntegerForListSubscriptions"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.subscription.Subscription]":
        _token = next_token
        while True:
            _response = self.list_subscriptions(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("subscriptions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_qbusiness.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Gets a list of tags associated with a specified resource. Amazon Q Business applications and data sources can have tags associated with them.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Q Business application or data source to get a list of tags for.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_tags_for_resource

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_feedback(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        conversation_id: "capo_qbusiness.types.conversation_id.ConversationId",
        message_id: "capo_qbusiness.types.system_message_id.SystemMessageId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_id: Optional["capo_qbusiness.types.user_id.UserId"] = None,
        message_copied_at: Optional["capo_qbusiness.types.timestamp.Timestamp"] = None,
        message_usefulness: Optional[
            "capo_qbusiness.types.message_usefulness_feedback.MessageUsefulnessFeedback"
        ] = None,
    ) -> None:
        """<p>Enables your end user to provide feedback on their Amazon Q Business generated chat responses.</p>

        Args:
            application_id: <p>The identifier of the application associated with the feedback.</p>
            user_id: <p>The identifier of the user giving the feedback.</p>
            conversation_id: <p>The identifier of the conversation the feedback is attached to.</p>
            message_id: <p>The identifier of the chat message that the feedback was given for.</p>
            message_copied_at: <p>The timestamp for when the feedback was recorded.</p>
            message_usefulness: <p>The feedback usefulness value given by the user to the chat message.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.put_feedback_request.PutFeedbackRequest]",
        ) -> OperationResponse[None]:
            import capo_qbusiness._operations.expert_q.put_feedback

            output, http_response = (
                capo_qbusiness._operations.expert_q.put_feedback.put_feedback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.put_feedback_request.PutFeedbackRequest = {
            "application_id": application_id,
            "conversation_id": conversation_id,
            "message_id": message_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if message_copied_at is not None:
            input_["message_copied_at"] = message_copied_at
        if message_usefulness is not None:
            input_["message_usefulness"] = message_usefulness

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_group(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        group_name: "capo_qbusiness.types.group_name.GroupName",
        type: "capo_qbusiness.types.membership_type.MembershipType",
        group_members: "capo_qbusiness.types.group_members.GroupMembers",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        data_source_id: Optional[
            "capo_qbusiness.types.data_source_id.DataSourceId"
        ] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
    ) -> "capo_qbusiness.types.put_group_response.PutGroupResponse":
        """<p>Create, or updates, a mapping of users—who have access to a document—to groups.</p> <p>You can also map sub groups to groups. For example, the group "Company Intellectual Property Teams" includes sub groups "Research" and "Engineering". These sub groups include their own list of users or people who work in these teams. Only users who work in research and engineering, and therefore belong in the intellectual property group, can see top-secret company documents in their Amazon Q Business chat results.</p> <p>There are two options for creating groups, either passing group members inline or using an S3 file via the S3PathForGroupMembers field. For inline groups, there is a limit of 1000 members per group and for provided S3 files there is a limit of 100 thousand members. When creating a group using an S3 file, you provide both an S3 file and a <code>RoleArn</code> for Amazon Q Buisness to access the file.</p>

        Args:
            application_id: <p>The identifier of the application in which the user and group mapping belongs.</p>
            index_id: <p>The identifier of the index in which you want to map users to their groups.</p>
            group_name: <p>The list that contains your users or sub groups that belong the same group. For example, the group "Company" includes the user "CEO" and the sub groups "Research", "Engineering", and "Sales and Marketing".</p>
            data_source_id: <p>The identifier of the data source for which you want to map users to their groups. This is useful if a group is tied to multiple data sources, but you only want the group to access documents of a certain data source. For example, the groups "Research", "Engineering", and "Sales and Marketing" are all tied to the company's documents stored in the data sources Confluence and Salesforce. However, "Sales and Marketing" team only needs access to customer-related documents stored in Salesforce.</p>
            type: <p>The type of the group.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that has access to the S3 file that contains your list of users that belong to a group.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.put_group_request.PutGroupRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.put_group_response.PutGroupResponse"
        ]:
            import capo_qbusiness._operations.expert_q.put_group

            output, http_response = (
                capo_qbusiness._operations.expert_q.put_group.put_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.put_group_request.PutGroupRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "group_name": group_name,
            "type": type,
            "group_members": group_members,
        }
        if data_source_id is not None:
            input_["data_source_id"] = data_source_id
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_relevant_content(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        query_text: "capo_qbusiness.types.query_text.QueryText",
        content_source: "capo_qbusiness.types.content_source.ContentSource",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        attribute_filter: Optional[
            "capo_qbusiness.types.attribute_filter.AttributeFilter"
        ] = None,
        max_results: Optional["capo_qbusiness.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
    ) -> "capo_qbusiness.types.search_relevant_content_response.SearchRelevantContentResponse":
        """<p>Searches for relevant content in a Amazon Q Business application based on a query. This operation takes a search query text, the Amazon Q Business application identifier, and optional filters (such as content source and maximum results) as input. It returns a list of relevant content items, where each item includes the content text, the unique document identifier, the document title, the document URI, any relevant document attributes, and score attributes indicating the confidence level of the relevance.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application to search.</p>
            query_text: <p>The text to search for.</p>
            content_source: <p>The source of content to search in.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>The token for the next set of results. (You received this token from a previous call.)</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.license_not_found_exception.LicenseNotFoundException: <p>You don't have permissions to perform the action because your license is inactive. Ask your admin to activate your license and try again after your licence is active.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.search_relevant_content_request.SearchRelevantContentRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.search_relevant_content_response.SearchRelevantContentResponse"
        ]:
            import capo_qbusiness._operations.expert_q.search_relevant_content

            output, http_response = (
                capo_qbusiness._operations.expert_q.search_relevant_content.search_relevant_content(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.search_relevant_content_request.SearchRelevantContentRequest = {
            "application_id": application_id,
            "query_text": query_text,
            "content_source": content_source,
        }
        if attribute_filter is not None:
            input_["attribute_filter"] = attribute_filter
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_search_relevant_content(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        query_text: "capo_qbusiness.types.query_text.QueryText",
        content_source: "capo_qbusiness.types.content_source.ContentSource",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        attribute_filter: Optional[
            "capo_qbusiness.types.attribute_filter.AttributeFilter"
        ] = None,
        max_results: Optional["capo_qbusiness.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_qbusiness.types.relevant_content.RelevantContent]":
        _token = next_token
        while True:
            _response = self.search_relevant_content(
                application_id,
                query_text,
                content_source,
                config_overrides=config_overrides,
                attribute_filter=attribute_filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("relevant_content",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_data_source_sync_job(
        self,
        data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId",
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.start_data_source_sync_job_response.StartDataSourceSyncJobResponse":
        """<p>Starts a data source connector synchronization job. If a synchronization job is already in progress, Amazon Q Business returns a <code>ConflictException</code>.</p>

        Args:
            data_source_id: <p> The identifier of the data source connector. </p>
            application_id: <p>The identifier of Amazon Q Business application the data source is connected to.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.start_data_source_sync_job_request.StartDataSourceSyncJobRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.start_data_source_sync_job_response.StartDataSourceSyncJobResponse"
        ]:
            import capo_qbusiness._operations.expert_q.start_data_source_sync_job

            output, http_response = (
                capo_qbusiness._operations.expert_q.start_data_source_sync_job.start_data_source_sync_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.start_data_source_sync_job_request.StartDataSourceSyncJobRequest = {
            "data_source_id": data_source_id,
            "application_id": application_id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_data_source_sync_job(
        self,
        data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId",
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.stop_data_source_sync_job_response.StopDataSourceSyncJobResponse":
        """<p>Stops an Amazon Q Business data source connector synchronization job already in progress.</p>

        Args:
            data_source_id: <p> The identifier of the data source connector. </p>
            application_id: <p>The identifier of the Amazon Q Business application that the data source is connected to.</p>
            index_id: <p>The identifier of the index used with the Amazon Q Business data source connector.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.stop_data_source_sync_job_request.StopDataSourceSyncJobRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.stop_data_source_sync_job_response.StopDataSourceSyncJobResponse"
        ]:
            import capo_qbusiness._operations.expert_q.stop_data_source_sync_job

            output, http_response = (
                capo_qbusiness._operations.expert_q.stop_data_source_sync_job.stop_data_source_sync_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.stop_data_source_sync_job_request.StopDataSourceSyncJobRequest = {
            "data_source_id": data_source_id,
            "application_id": application_id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_qbusiness.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_qbusiness.types.tags.Tags",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.tag_resource_response.TagResourceResponse":
        """<p>Adds the specified tag to the specified Amazon Q Business application or data source resource. If the tag already exists, the existing value is replaced with the new value.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Q Business application or data source to tag.</p>
            tags: <p>A list of tag keys to add to the Amazon Q Business application or data source. If a tag already exists, the existing value is replaced with the new value.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.tag_resource

            output, http_response = (
                capo_qbusiness._operations.expert_q.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn,
            "tags": tags,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_resource(
        self,
        resource_arn: "capo_qbusiness.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_qbusiness.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from an Amazon Q Business application or a data source.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the Amazon Q Business application, or data source to remove the tag from.</p>
            tag_keys: <p>A list of tag keys to remove from the Amazon Q Business application or data source. If a tag key does not exist on the resource, it is ignored.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.untag_resource

            output, http_response = (
                capo_qbusiness._operations.expert_q.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.untag_resource_request.UntagResourceRequest = {
            "resource_arn": resource_arn,
            "tag_keys": tag_keys,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_chat_controls_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        response_scope: Optional[
            "capo_qbusiness.types.response_scope.ResponseScope"
        ] = None,
        orchestration_configuration: Optional[
            "capo_qbusiness.types.orchestration_configuration.OrchestrationConfiguration"
        ] = None,
        blocked_phrases_configuration_update: Optional[
            "capo_qbusiness.types.blocked_phrases_configuration_update.BlockedPhrasesConfigurationUpdate"
        ] = None,
        topic_configurations_to_create_or_update: Optional[
            "capo_qbusiness.types.topic_configurations.TopicConfigurations"
        ] = None,
        topic_configurations_to_delete: Optional[
            "capo_qbusiness.types.topic_configurations.TopicConfigurations"
        ] = None,
        creator_mode_configuration: Optional[
            "capo_qbusiness.types.creator_mode_configuration.CreatorModeConfiguration"
        ] = None,
        hallucination_reduction_configuration: Optional[
            "capo_qbusiness.types.hallucination_reduction_configuration.HallucinationReductionConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.update_chat_controls_configuration_response.UpdateChatControlsConfigurationResponse":
        """<p>Updates a set of chat controls configured for an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the application for which the chat controls are configured.</p>
            client_token: <p>A token that you provide to identify the request to update a Amazon Q Business application chat configuration.</p>
            response_scope: <p>The response scope configured for your application. This determines whether your application uses its retrieval augmented generation (RAG) system to generate answers only from your enterprise data, or also uses the large language models (LLM) knowledge to respons to end user questions in chat.</p>
            orchestration_configuration: <p> The chat response orchestration settings for your application.</p>
            blocked_phrases_configuration_update: <p>The phrases blocked from chat by your chat control configuration.</p>
            topic_configurations_to_create_or_update: <p>The configured topic specific chat controls you want to update.</p>
            topic_configurations_to_delete: <p>The configured topic specific chat controls you want to delete.</p>
            creator_mode_configuration: <p>The configuration details for <code>CREATOR_MODE</code>.</p>
            hallucination_reduction_configuration: <p> The hallucination reduction settings for your application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_chat_controls_configuration_request.UpdateChatControlsConfigurationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_chat_controls_configuration_response.UpdateChatControlsConfigurationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_chat_controls_configuration

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_chat_controls_configuration.update_chat_controls_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_chat_controls_configuration_request.UpdateChatControlsConfigurationRequest = {
            "application_id": application_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if response_scope is not None:
            input_["response_scope"] = response_scope
        if orchestration_configuration is not None:
            input_["orchestration_configuration"] = orchestration_configuration
        if blocked_phrases_configuration_update is not None:
            input_["blocked_phrases_configuration_update"] = (
                blocked_phrases_configuration_update
            )
        if topic_configurations_to_create_or_update is not None:
            input_["topic_configurations_to_create_or_update"] = (
                topic_configurations_to_create_or_update
            )
        if topic_configurations_to_delete is not None:
            input_["topic_configurations_to_delete"] = topic_configurations_to_delete
        if creator_mode_configuration is not None:
            input_["creator_mode_configuration"] = creator_mode_configuration
        if hallucination_reduction_configuration is not None:
            input_["hallucination_reduction_configuration"] = (
                hallucination_reduction_configuration
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_chat_response_configuration(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        chat_response_configuration_id: "capo_qbusiness.types.chat_response_configuration_id.ChatResponseConfigurationId",
        response_configurations: "capo_qbusiness.types.response_configurations.ResponseConfigurations",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        display_name: Optional["capo_qbusiness.types.display_name.DisplayName"] = None,
        client_token: Optional["capo_qbusiness.types.string.String"] = None,
    ) -> "capo_qbusiness.types.update_chat_response_configuration_response.UpdateChatResponseConfigurationResponse":
        """<p>Updates an existing chat response configuration in an Amazon Q Business application. This operation allows administrators to modify configuration settings, display name, and response parameters to refine how the system generates responses.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application containing the chat response configuration to update.</p>
            chat_response_configuration_id: <p>The unique identifier of the chat response configuration to update within the specified application.</p>
            display_name: <p>The new human-readable name to assign to the chat response configuration, making it easier to identify among multiple configurations.</p>
            response_configurations: <p>The updated collection of response configuration settings that define how Amazon Q Business generates and formats responses to user queries.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request. This helps prevent the same update from being processed multiple times if retries occur.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_chat_response_configuration_request.UpdateChatResponseConfigurationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_chat_response_configuration_response.UpdateChatResponseConfigurationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_chat_response_configuration

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_chat_response_configuration.update_chat_response_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_chat_response_configuration_request.UpdateChatResponseConfigurationRequest = {
            "application_id": application_id,
            "chat_response_configuration_id": chat_response_configuration_id,
            "response_configurations": response_configurations,
        }
        if display_name is not None:
            input_["display_name"] = display_name
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

    def update_subscription(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        subscription_id: "capo_qbusiness.types.subscription_id.SubscriptionId",
        type: "capo_qbusiness.types.subscription_type.SubscriptionType",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.update_subscription_response.UpdateSubscriptionResponse":
        """<p>Updates the pricing tier for an Amazon Q Business subscription. Upgrades are instant. Downgrades apply at the start of the next month. Subscription tier determines feature access for the user. For more information on subscriptions and pricing tiers, see <a href="https://aws.amazon.com/q/business/pricing/">Amazon Q Business pricing</a>.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application where the subscription update should take effect.</p>
            subscription_id: <p>The identifier of the Amazon Q Business subscription to be updated.</p>
            type: <p>The type of the Amazon Q Business subscription to be updated.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_subscription_request.UpdateSubscriptionRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_subscription_response.UpdateSubscriptionResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_subscription

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_subscription.update_subscription(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_subscription_request.UpdateSubscriptionRequest = {
            "application_id": application_id,
            "subscription_id": subscription_id,
            "type": type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_user(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        user_id: "capo_qbusiness.types.string.String",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        user_aliases_to_update: Optional[
            "capo_qbusiness.types.user_aliases.UserAliases"
        ] = None,
        user_aliases_to_delete: Optional[
            "capo_qbusiness.types.user_aliases.UserAliases"
        ] = None,
    ) -> "capo_qbusiness.types.update_user_response.UpdateUserResponse":
        """<p>Updates a information associated with a user id.</p>

        Args:
            application_id: <p>The identifier of the application the user is attached to.</p>
            user_id: <p>The email id attached to the user.</p>
            user_aliases_to_update: <p>The user aliases attached to the user id that are to be updated.</p>
            user_aliases_to_delete: <p>The user aliases attached to the user id that are to be deleted.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_user_request.UpdateUserRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_user_response.UpdateUserResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_user

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_user.update_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_user_request.UpdateUserRequest = {
            "application_id": application_id,
            "user_id": user_id,
        }
        if user_aliases_to_update is not None:
            input_["user_aliases_to_update"] = user_aliases_to_update
        if user_aliases_to_delete is not None:
            input_["user_aliases_to_delete"] = user_aliases_to_delete

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_application(
        self,
        display_name: "capo_qbusiness.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        identity_type: Optional[
            "capo_qbusiness.types.identity_type.IdentityType"
        ] = None,
        iam_identity_provider_arn: Optional[
            "capo_qbusiness.types.iam_identity_provider_arn.IAMIdentityProviderArn"
        ] = None,
        identity_center_instance_arn: Optional[
            "capo_qbusiness.types.instance_arn.InstanceArn"
        ] = None,
        client_ids_for_oidc: Optional[
            "capo_qbusiness.types.client_ids_for_oidc.ClientIdsForOIDC"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        encryption_configuration: Optional[
            "capo_qbusiness.types.encryption_configuration.EncryptionConfiguration"
        ] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        attachments_configuration: Optional[
            "capo_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
        ] = None,
        q_apps_configuration: Optional[
            "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
        ] = None,
        personalization_configuration: Optional[
            "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
        ] = None,
        quick_sight_configuration: Optional[
            "capo_qbusiness.types.quick_sight_configuration.QuickSightConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.create_application_response.CreateApplicationResponse":
        """<p>Creates an Amazon Q Business application.</p> <note> <p>There are new tiers for Amazon Q Business. Not all features in Amazon Q Business Pro are also available in Amazon Q Business Lite. For information on what's included in Amazon Q Business Lite and what's included in Amazon Q Business Pro, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#user-sub-tiers">Amazon Q Business tiers</a>. You must use the Amazon Q Business console to assign subscription tiers to users. </p> <p>An Amazon Q Apps service linked role will be created if it's absent in the Amazon Web Services account when <code>QAppsConfiguration</code> is enabled in the request. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html"> Using service-linked roles for Q Apps</a>.</p> <p>When you create an application, Amazon Q Business may securely transmit data for processing from your selected Amazon Web Services region, but within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note>

        Args:
            display_name: <p>A name for the Amazon Q Business application. </p>
            role_arn: <p> The Amazon Resource Name (ARN) of an IAM role with permissions to access your Amazon CloudWatch logs and metrics. If this property is not specified, Amazon Q Business will create a <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles.html#slr-permissions">service linked role (SLR)</a> and use it as the application's role.</p>
            identity_type: <p>The authentication type being used by a Amazon Q Business application.</p>
            iam_identity_provider_arn: <p>The Amazon Resource Name (ARN) of an identity provider being used by an Amazon Q Business application.</p>
            identity_center_instance_arn: <p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>
            client_ids_for_oidc: <p>The OIDC client ID for a Amazon Q Business application.</p>
            description: <p>A description for the Amazon Q Business application. </p>
            encryption_configuration: <p>The identifier of the KMS key that is used to encrypt your data. Amazon Q Business doesn't support asymmetric keys.</p>
            tags: <p>A list of key-value pairs that identify or categorize your Amazon Q Business application. You can also use tags to help control access to the application. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Q Business application.</p>
            attachments_configuration: <p>An option to allow end users to upload files directly during chat.</p>
            q_apps_configuration: <p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>
            personalization_configuration: <p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a> </p>
            quick_sight_configuration: <p>The Amazon Quick Suite configuration for an Amazon Q Business application that uses Quick Suite for authentication. This configuration is required if your application uses Quick Suite as the identity provider. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html">Creating an Amazon Quick Suite integrated application</a>.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_application_request.CreateApplicationRequest = {
            "display_name": display_name
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if iam_identity_provider_arn is not None:
            input_["iam_identity_provider_arn"] = iam_identity_provider_arn
        if identity_center_instance_arn is not None:
            input_["identity_center_instance_arn"] = identity_center_instance_arn
        if client_ids_for_oidc is not None:
            input_["client_ids_for_oidc"] = client_ids_for_oidc
        if description is not None:
            input_["description"] = description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if attachments_configuration is not None:
            input_["attachments_configuration"] = attachments_configuration
        if q_apps_configuration is not None:
            input_["q_apps_configuration"] = q_apps_configuration
        if personalization_configuration is not None:
            input_["personalization_configuration"] = personalization_configuration
        if quick_sight_configuration is not None:
            input_["quick_sight_configuration"] = quick_sight_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_application(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_application_response.GetApplicationResponse":
        """<p>Gets information about an existing Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_application_request.GetApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_application_response.GetApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_application.get_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_application_request.GetApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        identity_center_instance_arn: Optional[
            "capo_qbusiness.types.instance_arn.InstanceArn"
        ] = None,
        display_name: Optional[
            "capo_qbusiness.types.application_name.ApplicationName"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        attachments_configuration: Optional[
            "capo_qbusiness.types.attachments_configuration.AttachmentsConfiguration"
        ] = None,
        q_apps_configuration: Optional[
            "capo_qbusiness.types.q_apps_configuration.QAppsConfiguration"
        ] = None,
        personalization_configuration: Optional[
            "capo_qbusiness.types.personalization_configuration.PersonalizationConfiguration"
        ] = None,
        auto_subscription_configuration: Optional[
            "capo_qbusiness.types.auto_subscription_configuration.AutoSubscriptionConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.update_application_response.UpdateApplicationResponse":
        """<p>Updates an existing Amazon Q Business application.</p> <note> <p>Amazon Q Business applications may securely transmit data for processing across Amazon Web Services Regions within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note> <note> <p>An Amazon Q Apps service-linked role will be created if it's absent in the Amazon Web Services account when <code>QAppsConfiguration</code> is enabled in the request. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/using-service-linked-roles-qapps.html">Using service-linked roles for Q Apps</a>. </p> </note>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            identity_center_instance_arn: <p> The Amazon Resource Name (ARN) of the IAM Identity Center instance you are either creating for—or connecting to—your Amazon Q Business application.</p>
            display_name: <p>A name for the Amazon Q Business application.</p>
            description: <p>A description for the Amazon Q Business application.</p>
            role_arn: <p>An Amazon Web Services Identity and Access Management (IAM) role that gives Amazon Q Business permission to access Amazon CloudWatch logs and metrics.</p>
            attachments_configuration: <p>An option to allow end users to upload files directly during chat.</p>
            q_apps_configuration: <p>An option to allow end users to create and use Amazon Q Apps in the web experience.</p>
            personalization_configuration: <p>Configuration information about chat response personalization. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/personalizing-chat-responses.html">Personalizing chat responses</a>.</p>
            auto_subscription_configuration: <p>An option to enable updating the default subscription type assigned to an Amazon Q Business application using IAM identity federation for user management.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_application_response.UpdateApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if identity_center_instance_arn is not None:
            input_["identity_center_instance_arn"] = identity_center_instance_arn
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if attachments_configuration is not None:
            input_["attachments_configuration"] = attachments_configuration
        if q_apps_configuration is not None:
            input_["q_apps_configuration"] = q_apps_configuration
        if personalization_configuration is not None:
            input_["personalization_configuration"] = personalization_configuration
        if auto_subscription_configuration is not None:
            input_["auto_subscription_configuration"] = auto_subscription_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_application

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_applications(
        self,
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_applications.MaxResultsIntegerForListApplications"
        ] = None,
    ) -> "capo_qbusiness.types.list_applications_response.ListApplicationsResponse":
        """<p>Lists Amazon Q Business applications.</p> <note> <p>Amazon Q Business applications may securely transmit data for processing across Amazon Web Services Regions within your geography. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/cross-region-inference.html">Cross region inference in Amazon Q Business</a>.</p> </note>

        Args:
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business applications.</p>
            max_results: <p>The maximum number of Amazon Q Business applications to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_applications

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_applications_request.ListApplicationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_applications(
        self,
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_applications.MaxResultsIntegerForListApplications"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.application.Application]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_data_accessor(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        principal: "capo_qbusiness.types.principal_role_arn.PrincipalRoleArn",
        action_configurations: "capo_qbusiness.types.action_configuration_list.ActionConfigurationList",
        display_name: "capo_qbusiness.types.data_accessor_name.DataAccessorName",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        authentication_detail: Optional[
            "capo_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
        ] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
    ) -> (
        "capo_qbusiness.types.create_data_accessor_response.CreateDataAccessorResponse"
    ):
        """<p>Creates a new data accessor for an ISV to access data from a Amazon Q Business application. The data accessor is an entity that represents the ISV's access to the Amazon Q Business application's data. It includes the IAM role ARN for the ISV, a friendly name, and a set of action configurations that define the specific actions the ISV is allowed to perform and any associated data filters. When the data accessor is created, an IAM Identity Center application is also created to manage the ISV's identity and authentication for accessing the Amazon Q Business application.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            principal: <p>The Amazon Resource Name (ARN) of the IAM role for the ISV that will be accessing the data.</p>
            action_configurations: <p>A list of action configurations specifying the allowed actions and any associated filters.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure idempotency of the request.</p>
            display_name: <p>A friendly name for the data accessor.</p>
            authentication_detail: <p>The authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.</p>
            tags: <p>The tags to associate with the data accessor.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_data_accessor_request.CreateDataAccessorRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_data_accessor_response.CreateDataAccessorResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_data_accessor

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_data_accessor.create_data_accessor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_data_accessor_request.CreateDataAccessorRequest = {
            "application_id": application_id,
            "principal": principal,
            "action_configurations": action_configurations,
            "display_name": display_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if authentication_detail is not None:
            input_["authentication_detail"] = authentication_detail
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_accessor(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        data_accessor_id: "capo_qbusiness.types.data_accessor_id.DataAccessorId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_data_accessor_response.GetDataAccessorResponse":
        """<p>Retrieves information about a specified data accessor. This operation returns details about the data accessor, including its display name, unique identifier, Amazon Resource Name (ARN), the associated Amazon Q Business application and IAM Identity Center application, the IAM role for the ISV, the action configurations, and the timestamps for when the data accessor was created and last updated.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            data_accessor_id: <p>The unique identifier of the data accessor to retrieve.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_data_accessor_request.GetDataAccessorRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_data_accessor_response.GetDataAccessorResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_data_accessor

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_data_accessor.get_data_accessor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_data_accessor_request.GetDataAccessorRequest = {
            "application_id": application_id,
            "data_accessor_id": data_accessor_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_accessor(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        data_accessor_id: "capo_qbusiness.types.data_accessor_id.DataAccessorId",
        action_configurations: "capo_qbusiness.types.action_configuration_list.ActionConfigurationList",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        authentication_detail: Optional[
            "capo_qbusiness.types.data_accessor_authentication_detail.DataAccessorAuthenticationDetail"
        ] = None,
        display_name: Optional[
            "capo_qbusiness.types.data_accessor_name.DataAccessorName"
        ] = None,
    ) -> (
        "capo_qbusiness.types.update_data_accessor_response.UpdateDataAccessorResponse"
    ):
        """<p>Updates an existing data accessor. This operation allows modifying the action configurations (the allowed actions and associated filters) and the display name of the data accessor. It does not allow changing the IAM role associated with the data accessor or other core properties of the data accessor.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            data_accessor_id: <p>The unique identifier of the data accessor to update.</p>
            action_configurations: <p>The updated list of action configurations specifying the allowed actions and any associated filters.</p>
            authentication_detail: <p>The updated authentication configuration details for the data accessor. This specifies how the ISV will authenticate when accessing data through this data accessor.</p>
            display_name: <p>The updated friendly name for the data accessor.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_data_accessor_request.UpdateDataAccessorRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_data_accessor_response.UpdateDataAccessorResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_data_accessor

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_data_accessor.update_data_accessor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_data_accessor_request.UpdateDataAccessorRequest = {
            "application_id": application_id,
            "data_accessor_id": data_accessor_id,
            "action_configurations": action_configurations,
        }
        if authentication_detail is not None:
            input_["authentication_detail"] = authentication_detail
        if display_name is not None:
            input_["display_name"] = display_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_accessor(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        data_accessor_id: "capo_qbusiness.types.data_accessor_id.DataAccessorId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> (
        "capo_qbusiness.types.delete_data_accessor_response.DeleteDataAccessorResponse"
    ):
        """<p>Deletes a specified data accessor. This operation permanently removes the data accessor and its associated IAM Identity Center application. Any access granted to the ISV through this data accessor will be revoked.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            data_accessor_id: <p>The unique identifier of the data accessor to delete.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_data_accessor_request.DeleteDataAccessorRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_data_accessor_response.DeleteDataAccessorResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_data_accessor

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_data_accessor.delete_data_accessor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_data_accessor_request.DeleteDataAccessorRequest = {
            "application_id": application_id,
            "data_accessor_id": data_accessor_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_accessors(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional[
            "capo_qbusiness.types.next_token1500.NextToken1500"
        ] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_data_accessors.MaxResultsIntegerForListDataAccessors"
        ] = None,
    ) -> "capo_qbusiness.types.list_data_accessors_response.ListDataAccessorsResponse":
        """<p>Lists the data accessors for a Amazon Q Business application. This operation returns a paginated list of data accessor summaries, including the friendly name, unique identifier, ARN, associated IAM role, and creation/update timestamps for each data accessor.</p>

        Args:
            application_id: <p>The unique identifier of the Amazon Q Business application.</p>
            next_token: <p>The token for the next set of results. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_data_accessors_request.ListDataAccessorsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_data_accessors_response.ListDataAccessorsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_data_accessors

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_data_accessors.list_data_accessors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_data_accessors_request.ListDataAccessorsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_accessors(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional[
            "capo_qbusiness.types.next_token1500.NextToken1500"
        ] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_data_accessors.MaxResultsIntegerForListDataAccessors"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.data_accessor.DataAccessor]":
        _token = next_token
        while True:
            _response = self.list_data_accessors(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_accessors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_index(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        display_name: "capo_qbusiness.types.index_name.IndexName",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        type: Optional["capo_qbusiness.types.index_type.IndexType"] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
        capacity_configuration: Optional[
            "capo_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
        ] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
    ) -> "capo_qbusiness.types.create_index_response.CreateIndexResponse":
        """<p>Creates an Amazon Q Business index.</p> <p>To determine if index creation has completed, check the <code>Status</code> field returned from a call to <code>DescribeIndex</code>. The <code>Status</code> field is set to <code>ACTIVE</code> when the index is ready to use.</p> <p>Once the index is active, you can index your documents using the <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_BatchPutDocument.html"> <code>BatchPutDocument</code> </a> API or the <a href="https://docs.aws.amazon.com/amazonq/latest/api-reference/API_CreateDataSource.html"> <code>CreateDataSource</code> </a> API.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application using the index.</p>
            display_name: <p>A name for the Amazon Q Business index.</p>
            description: <p>A description for the Amazon Q Business index.</p>
            type: <p>The index type that's suitable for your needs. For more information on what's included in each type of index, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/tiers.html#index-tiers">Amazon Q Business tiers</a>.</p>
            tags: <p>A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            capacity_configuration: <p>The capacity units you want to provision for your index. You can add and remove capacity to fit your usage needs.</p>
            client_token: <p>A token that you provide to identify the request to create an index. Multiple calls to the <code>CreateIndex</code> API with the same client token will create only one index.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_index_request.CreateIndexRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_index_response.CreateIndexResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_index

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_index.create_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_index_request.CreateIndexRequest = {
            "application_id": application_id,
            "display_name": display_name,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if tags is not None:
            input_["tags"] = tags
        if capacity_configuration is not None:
            input_["capacity_configuration"] = capacity_configuration
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

    def get_index(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_index_response.GetIndexResponse":
        """<p>Gets information about an existing Amazon Q Business index.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application connected to the index.</p>
            index_id: <p>The identifier of the Amazon Q Business index you want information on.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_index_request.GetIndexRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_index_response.GetIndexResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_index

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_index.get_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_index_request.GetIndexRequest = {
            "application_id": application_id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_index(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        display_name: Optional[
            "capo_qbusiness.types.application_name.ApplicationName"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        capacity_configuration: Optional[
            "capo_qbusiness.types.index_capacity_configuration.IndexCapacityConfiguration"
        ] = None,
        document_attribute_configurations: Optional[
            "capo_qbusiness.types.document_attribute_configurations.DocumentAttributeConfigurations"
        ] = None,
    ) -> "capo_qbusiness.types.update_index_response.UpdateIndexResponse":
        """<p>Updates an Amazon Q Business index.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application connected to the index.</p>
            index_id: <p>The identifier of the Amazon Q Business index.</p>
            display_name: <p>The name of the Amazon Q Business index.</p>
            description: <p>The description of the Amazon Q Business index.</p>
            capacity_configuration: <p>The storage capacity units you want to provision for your Amazon Q Business index. You can add and remove capacity to fit your usage needs.</p>
            document_attribute_configurations: <p>Configuration information for document metadata or fields. Document metadata are fields or attributes associated with your documents. For example, the company department name associated with each document. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/doc-attributes-types.html#doc-attributes">Understanding document attributes</a>.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_index_request.UpdateIndexRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_index_response.UpdateIndexResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_index

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_index.update_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_index_request.UpdateIndexRequest = {
            "application_id": application_id,
            "index_id": index_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if capacity_configuration is not None:
            input_["capacity_configuration"] = capacity_configuration
        if document_attribute_configurations is not None:
            input_["document_attribute_configurations"] = (
                document_attribute_configurations
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_index(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_index_response.DeleteIndexResponse":
        """<p>Deletes an Amazon Q Business index.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application the Amazon Q Business index is linked to.</p>
            index_id: <p>The identifier of the Amazon Q Business index.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_index_request.DeleteIndexRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_index_response.DeleteIndexResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_index

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_index.delete_index(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_index_request.DeleteIndexRequest = {
            "application_id": application_id,
            "index_id": index_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_indices(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_indices.MaxResultsIntegerForListIndices"
        ] = None,
    ) -> "capo_qbusiness.types.list_indices_response.ListIndicesResponse":
        """<p>Lists the Amazon Q Business indices you have created.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application connected to the index.</p>
            next_token: <p>If the maxResults response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business indices.</p>
            max_results: <p>The maximum number of indices to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_indices_request.ListIndicesRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_indices_response.ListIndicesResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_indices

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_indices.list_indices(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_indices_request.ListIndicesRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_indices(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_indices.MaxResultsIntegerForListIndices"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.index.Index]":
        _token = next_token
        while True:
            _response = self.list_indices(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("indices",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_data_source(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        display_name: "capo_qbusiness.types.data_source_name.DataSourceName",
        configuration: "capo_qbusiness.types.data_source_configuration.DataSourceConfiguration",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        vpc_configuration: Optional[
            "capo_qbusiness.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
        sync_schedule: Optional[
            "capo_qbusiness.types.sync_schedule.SyncSchedule"
        ] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        document_enrichment_configuration: Optional[
            "capo_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
        ] = None,
        media_extraction_configuration: Optional[
            "capo_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.create_data_source_response.CreateDataSourceResponse":
        """<p>Creates a data source connector for an Amazon Q Business application.</p> <p> <code>CreateDataSource</code> is a synchronous operation. The operation returns 200 if the data source was successfully created. Otherwise, an exception is raised.</p>

        Args:
            application_id: <p> The identifier of the Amazon Q Business application the data source will be attached to.</p>
            index_id: <p>The identifier of the index that you want to use with the data source connector.</p>
            display_name: <p>A name for the data source connector.</p>
            configuration: <p>Configuration information to connect your data source repository to Amazon Q Business. Use this parameter to provide a JSON schema with configuration information specific to your data source connector.</p> <p>Each data source has a JSON schema provided by Amazon Q Business that you must use. For example, the Amazon S3 and Web Crawler connectors require the following JSON schemas:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/s3-api.html">Amazon S3 JSON schema</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/web-crawler-api.html">Web Crawler JSON schema</a> </p> </li> </ul> <p>You can find configuration templates for your specific data source using the following steps:</p> <ol> <li> <p>Navigate to the <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connectors-list.html">Supported connectors</a> page in the Amazon Q Business User Guide, and select the data source of your choice.</p> </li> <li> <p>Then, from your specific data source connector page, select <b>Using the API</b>. You will find the JSON schema for your data source, including parameter descriptions, in this section.</p> </li> </ol>
            vpc_configuration: <p>Configuration information for an Amazon VPC (Virtual Private Cloud) to connect to your data source. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/business-use-dg/connector-vpc.html">Using Amazon VPC with Amazon Q Business connectors</a>.</p>
            description: <p>A description for the data source connector.</p>
            tags: <p>A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            sync_schedule: <p>Sets the frequency for Amazon Q Business to check the documents in your data source repository and update your index. If you don't set a schedule, Amazon Q Business won't periodically update the index.</p> <p>Specify a <code>cron-</code> format schedule string or an empty string to indicate that the index is updated on demand. You can't specify the <code>Schedule</code> parameter when the <code>Type</code> parameter is set to <code>CUSTOM</code>. If you do, you receive a <code>ValidationException</code> exception. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. This field is required for all connector types except custom connectors, where it is optional.</p>
            client_token: <p>A token you provide to identify a request to create a data source connector. Multiple calls to the <code>CreateDataSource</code> API with the same client token will create only one data source connector. </p>
            media_extraction_configuration: <p>The configuration for extracting information from media in documents during ingestion.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_data_source_request.CreateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_data_source_response.CreateDataSourceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_data_source

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_data_source.create_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_data_source_request.CreateDataSourceRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "display_name": display_name,
            "configuration": configuration,
        }
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if sync_schedule is not None:
            input_["sync_schedule"] = sync_schedule
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if document_enrichment_configuration is not None:
            input_["document_enrichment_configuration"] = (
                document_enrichment_configuration
            )
        if media_extraction_configuration is not None:
            input_["media_extraction_configuration"] = media_extraction_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_data_source(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_data_source_response.GetDataSourceResponse":
        """<p>Gets information about an existing Amazon Q Business data source connector.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application.</p>
            index_id: <p>The identfier of the index used with the data source connector.</p>
            data_source_id: <p>The identifier of the data source connector.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_data_source_request.GetDataSourceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_data_source_response.GetDataSourceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_data_source

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_data_source.get_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_data_source_request.GetDataSourceRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "data_source_id": data_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_data_source(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        display_name: Optional[
            "capo_qbusiness.types.data_source_name.DataSourceName"
        ] = None,
        configuration: Optional[
            "capo_qbusiness.types.data_source_configuration.DataSourceConfiguration"
        ] = None,
        vpc_configuration: Optional[
            "capo_qbusiness.types.data_source_vpc_configuration.DataSourceVpcConfiguration"
        ] = None,
        description: Optional["capo_qbusiness.types.description.Description"] = None,
        sync_schedule: Optional[
            "capo_qbusiness.types.sync_schedule.SyncSchedule"
        ] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        document_enrichment_configuration: Optional[
            "capo_qbusiness.types.document_enrichment_configuration.DocumentEnrichmentConfiguration"
        ] = None,
        media_extraction_configuration: Optional[
            "capo_qbusiness.types.media_extraction_configuration.MediaExtractionConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.update_data_source_response.UpdateDataSourceResponse":
        """<p>Updates an existing Amazon Q Business data source connector.</p>

        Args:
            application_id: <p> The identifier of the Amazon Q Business application the data source is attached to.</p>
            index_id: <p>The identifier of the index attached to the data source connector.</p>
            data_source_id: <p>The identifier of the data source connector.</p>
            display_name: <p>A name of the data source connector.</p>
            description: <p>The description of the data source connector.</p>
            sync_schedule: <p>The chosen update frequency for your data source.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources.</p>
            media_extraction_configuration: <p>The configuration for extracting information from media in documents for your data source.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_data_source_request.UpdateDataSourceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_data_source_response.UpdateDataSourceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_data_source

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_data_source.update_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_data_source_request.UpdateDataSourceRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "data_source_id": data_source_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if configuration is not None:
            input_["configuration"] = configuration
        if vpc_configuration is not None:
            input_["vpc_configuration"] = vpc_configuration
        if description is not None:
            input_["description"] = description
        if sync_schedule is not None:
            input_["sync_schedule"] = sync_schedule
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if document_enrichment_configuration is not None:
            input_["document_enrichment_configuration"] = (
                document_enrichment_configuration
            )
        if media_extraction_configuration is not None:
            input_["media_extraction_configuration"] = media_extraction_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_source(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        data_source_id: "capo_qbusiness.types.data_source_id.DataSourceId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_data_source_response.DeleteDataSourceResponse":
        """<p>Deletes an Amazon Q Business data source connector. While the data source is being deleted, the <code>Status</code> field returned by a call to the <code>DescribeDataSource</code> API is set to <code>DELETING</code>. </p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application used with the data source connector.</p>
            index_id: <p>The identifier of the index used with the data source connector.</p>
            data_source_id: <p>The identifier of the data source connector that you want to delete. </p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_data_source_request.DeleteDataSourceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_data_source_response.DeleteDataSourceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_data_source

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_data_source.delete_data_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_data_source_request.DeleteDataSourceRequest = {
            "application_id": application_id,
            "index_id": index_id,
            "data_source_id": data_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_data_sources(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_data_sources.MaxResultsIntegerForListDataSources"
        ] = None,
    ) -> "capo_qbusiness.types.list_data_sources_response.ListDataSourcesResponse":
        """<p>Lists the Amazon Q Business data source connectors that you have created.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the data source connectors.</p>
            index_id: <p>The identifier of the index used with one or more data source connectors.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business data source connectors.</p>
            max_results: <p>The maximum number of data source connectors to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_data_sources_request.ListDataSourcesRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_data_sources_response.ListDataSourcesResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_data_sources

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_data_sources.list_data_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_data_sources_request.ListDataSourcesRequest = {
            "application_id": application_id,
            "index_id": index_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_data_sources(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        index_id: "capo_qbusiness.types.index_id.IndexId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_data_sources.MaxResultsIntegerForListDataSources"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.data_source.DataSource]":
        _token = next_token
        while True:
            _response = self.list_data_sources(
                application_id,
                index_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_plugin(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        display_name: "capo_qbusiness.types.plugin_name.PluginName",
        type: "capo_qbusiness.types.plugin_type.PluginType",
        auth_configuration: "capo_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        server_url: Optional["capo_qbusiness.types.url.Url"] = None,
        custom_plugin_configuration: Optional[
            "capo_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
        ] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
    ) -> "capo_qbusiness.types.create_plugin_response.CreatePluginResponse":
        """<p>Creates an Amazon Q Business plugin.</p>

        Args:
            application_id: <p>The identifier of the application that will contain the plugin.</p>
            display_name: <p>A the name for your plugin.</p>
            type: <p>The type of plugin you want to create.</p>
            server_url: <p>The source URL used for plugin configuration.</p>
            custom_plugin_configuration: <p>Contains configuration for a custom plugin.</p>
            tags: <p>A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Q Business plugin.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_plugin_request.CreatePluginRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_plugin_response.CreatePluginResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_plugin

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_plugin.create_plugin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_plugin_request.CreatePluginRequest = {
            "application_id": application_id,
            "display_name": display_name,
            "type": type,
            "auth_configuration": auth_configuration,
        }
        if server_url is not None:
            input_["server_url"] = server_url
        if custom_plugin_configuration is not None:
            input_["custom_plugin_configuration"] = custom_plugin_configuration
        if tags is not None:
            input_["tags"] = tags
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

    def get_plugin(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        plugin_id: "capo_qbusiness.types.plugin_id.PluginId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_plugin_response.GetPluginResponse":
        """<p>Gets information about an existing Amazon Q Business plugin.</p>

        Args:
            application_id: <p>The identifier of the application which contains the plugin.</p>
            plugin_id: <p>The identifier of the plugin.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_plugin_request.GetPluginRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_plugin_response.GetPluginResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_plugin

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_plugin.get_plugin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_plugin_request.GetPluginRequest = {
            "application_id": application_id,
            "plugin_id": plugin_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_plugin(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        plugin_id: "capo_qbusiness.types.plugin_id.PluginId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        display_name: Optional["capo_qbusiness.types.plugin_name.PluginName"] = None,
        state: Optional["capo_qbusiness.types.plugin_state.PluginState"] = None,
        server_url: Optional["capo_qbusiness.types.url.Url"] = None,
        custom_plugin_configuration: Optional[
            "capo_qbusiness.types.custom_plugin_configuration.CustomPluginConfiguration"
        ] = None,
        auth_configuration: Optional[
            "capo_qbusiness.types.plugin_auth_configuration.PluginAuthConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.update_plugin_response.UpdatePluginResponse":
        """<p>Updates an Amazon Q Business plugin.</p>

        Args:
            application_id: <p>The identifier of the application the plugin is attached to.</p>
            plugin_id: <p>The identifier of the plugin.</p>
            display_name: <p>The name of the plugin.</p>
            state: <p>The status of the plugin. </p>
            server_url: <p>The source URL used for plugin configuration.</p>
            custom_plugin_configuration: <p>The configuration for a custom plugin.</p>
            auth_configuration: <p>The authentication configuration the plugin is using.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_plugin_request.UpdatePluginRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_plugin_response.UpdatePluginResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_plugin

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_plugin.update_plugin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_plugin_request.UpdatePluginRequest = {
            "application_id": application_id,
            "plugin_id": plugin_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if state is not None:
            input_["state"] = state
        if server_url is not None:
            input_["server_url"] = server_url
        if custom_plugin_configuration is not None:
            input_["custom_plugin_configuration"] = custom_plugin_configuration
        if auth_configuration is not None:
            input_["auth_configuration"] = auth_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_plugin(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        plugin_id: "capo_qbusiness.types.plugin_id.PluginId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_plugin_response.DeletePluginResponse":
        """<p>Deletes an Amazon Q Business plugin.</p>

        Args:
            application_id: <p>The identifier the application attached to the Amazon Q Business plugin.</p>
            plugin_id: <p>The identifier of the plugin being deleted.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_plugin_request.DeletePluginRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_plugin_response.DeletePluginResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_plugin

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_plugin.delete_plugin(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_plugin_request.DeletePluginRequest = {
            "application_id": application_id,
            "plugin_id": plugin_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_plugins(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugins.MaxResultsIntegerForListPlugins"
        ] = None,
    ) -> "capo_qbusiness.types.list_plugins_response.ListPluginsResponse":
        """<p>Lists configured Amazon Q Business plugins.</p>

        Args:
            application_id: <p>The identifier of the application the plugin is attached to.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of plugins.</p>
            max_results: <p>The maximum number of documents to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_plugins_request.ListPluginsRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_plugins_response.ListPluginsResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_plugins

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_plugins.list_plugins(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_plugins_request.ListPluginsRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_plugins(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_plugins.MaxResultsIntegerForListPlugins"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.plugin.Plugin]":
        _token = next_token
        while True:
            _response = self.list_plugins(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("plugins",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_retriever(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        type: "capo_qbusiness.types.retriever_type.RetrieverType",
        display_name: "capo_qbusiness.types.retriever_name.RetrieverName",
        configuration: "capo_qbusiness.types.retriever_configuration.RetrieverConfiguration",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
    ) -> "capo_qbusiness.types.create_retriever_response.CreateRetrieverResponse":
        """<p>Adds a retriever to your Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of your Amazon Q Business application.</p>
            type: <p>The type of retriever you are using.</p>
            display_name: <p>The name of your retriever.</p>
            role_arn: <p>The ARN of an IAM role used by Amazon Q Business to access the basic authentication credentials stored in a Secrets Manager secret.</p>
            client_token: <p>A token that you provide to identify the request to create your Amazon Q Business application retriever.</p>
            tags: <p>A list of key-value pairs that identify or categorize the retriever. You can also use tags to help control access to the retriever. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_retriever_request.CreateRetrieverRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_retriever_response.CreateRetrieverResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_retriever

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_retriever.create_retriever(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_retriever_request.CreateRetrieverRequest = {
            "application_id": application_id,
            "type": type,
            "display_name": display_name,
            "configuration": configuration,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_retriever(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        retriever_id: "capo_qbusiness.types.retriever_id.RetrieverId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_retriever_response.GetRetrieverResponse":
        """<p>Gets information about an existing retriever used by an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application using the retriever.</p>
            retriever_id: <p>The identifier of the retriever.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_retriever_request.GetRetrieverRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_retriever_response.GetRetrieverResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_retriever

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_retriever.get_retriever(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_retriever_request.GetRetrieverRequest = {
            "application_id": application_id,
            "retriever_id": retriever_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_retriever(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        retriever_id: "capo_qbusiness.types.retriever_id.RetrieverId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        configuration: Optional[
            "capo_qbusiness.types.retriever_configuration.RetrieverConfiguration"
        ] = None,
        display_name: Optional[
            "capo_qbusiness.types.retriever_name.RetrieverName"
        ] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
    ) -> "capo_qbusiness.types.update_retriever_response.UpdateRetrieverResponse":
        """<p>Updates the retriever used for your Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of your Amazon Q Business application.</p>
            retriever_id: <p>The identifier of your retriever.</p>
            display_name: <p>The name of your retriever.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role with permission to access the retriever and required resources. </p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_retriever_request.UpdateRetrieverRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_retriever_response.UpdateRetrieverResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_retriever

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_retriever.update_retriever(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_retriever_request.UpdateRetrieverRequest = {
            "application_id": application_id,
            "retriever_id": retriever_id,
        }
        if configuration is not None:
            input_["configuration"] = configuration
        if display_name is not None:
            input_["display_name"] = display_name
        if role_arn is not None:
            input_["role_arn"] = role_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_retriever(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        retriever_id: "capo_qbusiness.types.retriever_id.RetrieverId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_retriever_response.DeleteRetrieverResponse":
        """<p>Deletes the retriever used by an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application using the retriever.</p>
            retriever_id: <p>The identifier of the retriever being deleted.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_retriever_request.DeleteRetrieverRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_retriever_response.DeleteRetrieverResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_retriever

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_retriever.delete_retriever(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_retriever_request.DeleteRetrieverRequest = {
            "application_id": application_id,
            "retriever_id": retriever_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_retrievers(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_retrievers_request.MaxResultsIntegerForListRetrieversRequest"
        ] = None,
    ) -> "capo_qbusiness.types.list_retrievers_response.ListRetrieversResponse":
        """<p>Lists the retriever used by an Amazon Q Business application.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application using the retriever.</p>
            next_token: <p>If the number of retrievers returned exceeds <code>maxResults</code>, Amazon Q Business returns a next token as a pagination token to retrieve the next set of retrievers.</p>
            max_results: <p>The maximum number of retrievers returned.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_retrievers_request.ListRetrieversRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_retrievers_response.ListRetrieversResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_retrievers

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_retrievers.list_retrievers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_retrievers_request.ListRetrieversRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_retrievers(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_retrievers_request.MaxResultsIntegerForListRetrieversRequest"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.retriever.Retriever]":
        _token = next_token
        while True:
            _response = self.list_retrievers(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("retrievers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_web_experience(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        title: Optional[
            "capo_qbusiness.types.web_experience_title.WebExperienceTitle"
        ] = None,
        subtitle: Optional[
            "capo_qbusiness.types.web_experience_subtitle.WebExperienceSubtitle"
        ] = None,
        welcome_message: Optional[
            "capo_qbusiness.types.web_experience_welcome_message.WebExperienceWelcomeMessage"
        ] = None,
        sample_prompts_control_mode: Optional[
            "capo_qbusiness.types.web_experience_sample_prompts_control_mode.WebExperienceSamplePromptsControlMode"
        ] = None,
        origins: Optional[
            "capo_qbusiness.types.web_experience_origins.WebExperienceOrigins"
        ] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        tags: Optional["capo_qbusiness.types.tags.Tags"] = None,
        client_token: Optional["capo_qbusiness.types.client_token.ClientToken"] = None,
        identity_provider_configuration: Optional[
            "capo_qbusiness.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
        browser_extension_configuration: Optional[
            "capo_qbusiness.types.browser_extension_configuration.BrowserExtensionConfiguration"
        ] = None,
        customization_configuration: Optional[
            "capo_qbusiness.types.customization_configuration.CustomizationConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.create_web_experience_response.CreateWebExperienceResponse":
        """<p>Creates an Amazon Q Business web experience.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business web experience.</p>
            title: <p>The title for your Amazon Q Business web experience.</p>
            subtitle: <p>A subtitle to personalize your Amazon Q Business web experience.</p>
            welcome_message: <p>The customized welcome message for end users of an Amazon Q Business web experience.</p>
            sample_prompts_control_mode: <p>Determines whether sample prompts are enabled in the web experience for an end user.</p>
            origins: <p>Sets the website domain origins that are allowed to embed the Amazon Q Business web experience. The <i>domain origin</i> refers to the base URL for accessing a website including the protocol (<code>http/https</code>), the domain name, and the port number (if specified). </p> <note> <p>You must only submit a <i>base URL</i> and not a full path. For example, <code>https://docs.aws.amazon.com</code>.</p> </note>
            role_arn: <p>The Amazon Resource Name (ARN) of the service role attached to your web experience.</p> <note> <p>The <code>roleArn</code> parameter is required when your Amazon Q Business application is created with IAM Identity Center. It is not required for SAML-based applications.</p> </note>
            tags: <p>A list of key-value pairs that identify or categorize your Amazon Q Business web experience. You can also use tags to help control access to the web experience. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.</p>
            client_token: <p>A token you provide to identify a request to create an Amazon Q Business web experience. </p>
            identity_provider_configuration: <p>Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.</p>
            browser_extension_configuration: <p>The browser extension configuration for an Amazon Q Business web experience.</p> <note> <p> For Amazon Q Business application using external OIDC-compliant identity providers (IdPs). The IdP administrator must add the browser extension sign-in redirect URLs to the IdP application. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html">Configure external OIDC identity provider for your browser extensions.</a>. </p> </note>
            customization_configuration: <p>Sets the custom logo, favicon, font, and color used in the Amazon Q web experience. </p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You have exceeded the set limits for your Amazon Q Business service. </p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.create_web_experience_request.CreateWebExperienceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.create_web_experience_response.CreateWebExperienceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.create_web_experience

            output, http_response = (
                capo_qbusiness._operations.expert_q.create_web_experience.create_web_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.create_web_experience_request.CreateWebExperienceRequest = {
            "application_id": application_id
        }
        if title is not None:
            input_["title"] = title
        if subtitle is not None:
            input_["subtitle"] = subtitle
        if welcome_message is not None:
            input_["welcome_message"] = welcome_message
        if sample_prompts_control_mode is not None:
            input_["sample_prompts_control_mode"] = sample_prompts_control_mode
        if origins is not None:
            input_["origins"] = origins
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration
        if browser_extension_configuration is not None:
            input_["browser_extension_configuration"] = browser_extension_configuration
        if customization_configuration is not None:
            input_["customization_configuration"] = customization_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_web_experience(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        web_experience_id: "capo_qbusiness.types.web_experience_id.WebExperienceId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.get_web_experience_response.GetWebExperienceResponse":
        """<p>Gets information about an existing Amazon Q Business web experience.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the web experience.</p>
            web_experience_id: <p>The identifier of the Amazon Q Business web experience. </p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.get_web_experience_request.GetWebExperienceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.get_web_experience_response.GetWebExperienceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.get_web_experience

            output, http_response = (
                capo_qbusiness._operations.expert_q.get_web_experience.get_web_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.get_web_experience_request.GetWebExperienceRequest = {
            "application_id": application_id,
            "web_experience_id": web_experience_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_web_experience(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        web_experience_id: "capo_qbusiness.types.web_experience_id.WebExperienceId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        role_arn: Optional["capo_qbusiness.types.role_arn.RoleArn"] = None,
        authentication_configuration: Optional[
            "capo_qbusiness.types.web_experience_auth_configuration.WebExperienceAuthConfiguration"
        ] = None,
        title: Optional[
            "capo_qbusiness.types.web_experience_title.WebExperienceTitle"
        ] = None,
        subtitle: Optional[
            "capo_qbusiness.types.web_experience_subtitle.WebExperienceSubtitle"
        ] = None,
        welcome_message: Optional[
            "capo_qbusiness.types.web_experience_welcome_message.WebExperienceWelcomeMessage"
        ] = None,
        sample_prompts_control_mode: Optional[
            "capo_qbusiness.types.web_experience_sample_prompts_control_mode.WebExperienceSamplePromptsControlMode"
        ] = None,
        identity_provider_configuration: Optional[
            "capo_qbusiness.types.identity_provider_configuration.IdentityProviderConfiguration"
        ] = None,
        origins: Optional[
            "capo_qbusiness.types.web_experience_origins.WebExperienceOrigins"
        ] = None,
        browser_extension_configuration: Optional[
            "capo_qbusiness.types.browser_extension_configuration.BrowserExtensionConfiguration"
        ] = None,
        customization_configuration: Optional[
            "capo_qbusiness.types.customization_configuration.CustomizationConfiguration"
        ] = None,
    ) -> "capo_qbusiness.types.update_web_experience_response.UpdateWebExperienceResponse":
        """<p>Updates an Amazon Q Business web experience. </p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application attached to the web experience.</p>
            web_experience_id: <p>The identifier of the Amazon Q Business web experience.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the role with permission to access the Amazon Q Business web experience and required resources.</p>
            authentication_configuration: <p>The authentication configuration of the Amazon Q Business web experience.</p>
            title: <p>The title of the Amazon Q Business web experience.</p>
            subtitle: <p>The subtitle of the Amazon Q Business web experience.</p>
            welcome_message: <p>A customized welcome message for an end user in an Amazon Q Business web experience.</p>
            sample_prompts_control_mode: <p>Determines whether sample prompts are enabled in the web experience for an end user.</p>
            identity_provider_configuration: <p>Information about the identity provider (IdP) used to authenticate end users of an Amazon Q Business web experience.</p>
            origins: <p>Updates the website domain origins that are allowed to embed the Amazon Q Business web experience. The <i>domain origin</i> refers to the <i>base URL</i> for accessing a website including the protocol (<code>http/https</code>), the domain name, and the port number (if specified).</p> <note> <ul> <li> <p>Any values except <code>null</code> submitted as part of this update will replace all previous values.</p> </li> <li> <p>You must only submit a <i>base URL</i> and not a full path. For example, <code>https://docs.aws.amazon.com</code>.</p> </li> </ul> </note>
            browser_extension_configuration: <p>The browser extension configuration for an Amazon Q Business web experience.</p> <note> <p> For Amazon Q Business application using external OIDC-compliant identity providers (IdPs). The IdP administrator must add the browser extension sign-in redirect URLs to the IdP application. For more information, see <a href="https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/browser-extensions.html">Configure external OIDC identity provider for your browser extensions.</a>. </p> </note>
            customization_configuration: <p>Updates the custom logo, favicon, font, and color used in the Amazon Q web experience. </p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.update_web_experience_request.UpdateWebExperienceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.update_web_experience_response.UpdateWebExperienceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.update_web_experience

            output, http_response = (
                capo_qbusiness._operations.expert_q.update_web_experience.update_web_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.update_web_experience_request.UpdateWebExperienceRequest = {
            "application_id": application_id,
            "web_experience_id": web_experience_id,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if authentication_configuration is not None:
            input_["authentication_configuration"] = authentication_configuration
        if title is not None:
            input_["title"] = title
        if subtitle is not None:
            input_["subtitle"] = subtitle
        if welcome_message is not None:
            input_["welcome_message"] = welcome_message
        if sample_prompts_control_mode is not None:
            input_["sample_prompts_control_mode"] = sample_prompts_control_mode
        if identity_provider_configuration is not None:
            input_["identity_provider_configuration"] = identity_provider_configuration
        if origins is not None:
            input_["origins"] = origins
        if browser_extension_configuration is not None:
            input_["browser_extension_configuration"] = browser_extension_configuration
        if customization_configuration is not None:
            input_["customization_configuration"] = customization_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_web_experience(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        web_experience_id: "capo_qbusiness.types.web_experience_id.WebExperienceId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
    ) -> "capo_qbusiness.types.delete_web_experience_response.DeleteWebExperienceResponse":
        """<p>Deletes an Amazon Q Business web experience.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the Amazon Q Business web experience.</p>
            web_experience_id: <p>The identifier of the Amazon Q Business web experience being deleted.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.conflict_exception.ConflictException: <p>You are trying to perform an action that conflicts with the current status of your resource. Fix any inconsistencies with your resources and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.delete_web_experience_request.DeleteWebExperienceRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.delete_web_experience_response.DeleteWebExperienceResponse"
        ]:
            import capo_qbusiness._operations.expert_q.delete_web_experience

            output, http_response = (
                capo_qbusiness._operations.expert_q.delete_web_experience.delete_web_experience(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.delete_web_experience_request.DeleteWebExperienceRequest = {
            "application_id": application_id,
            "web_experience_id": web_experience_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_web_experiences(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_web_experiences_request.MaxResultsIntegerForListWebExperiencesRequest"
        ] = None,
    ) -> (
        "capo_qbusiness.types.list_web_experiences_response.ListWebExperiencesResponse"
    ):
        """<p>Lists one or more Amazon Q Business Web Experiences.</p>

        Args:
            application_id: <p>The identifier of the Amazon Q Business application linked to the listed web experiences.</p>
            next_token: <p>If the <code>maxResults</code> response was incomplete because there is more data to retrieve, Amazon Q Business returns a pagination token in the response. You can use this pagination token to retrieve the next set of Amazon Q Business conversations.</p>
            max_results: <p>The maximum number of Amazon Q Business Web Experiences to return.</p>

        Raises:
            capo_qbusiness.errors.access_denied_exception.AccessDeniedException: <p> You don't have access to perform this action. Make sure you have the required permission policies and user accounts and try again.</p>
            capo_qbusiness.errors.internal_server_exception.InternalServerException: <p>An issue occurred with the internal server used for your Amazon Q Business service. Wait some minutes and try again, or contact <a href="http://aws.amazon.com/contact-us/">Support</a> for help.</p>
            capo_qbusiness.errors.resource_not_found_exception.ResourceNotFoundException: <p>The application or plugin resource you want to use doesn’t exist. Make sure you have provided the correct resource and try again.</p>
            capo_qbusiness.errors.throttling_exception.ThrottlingException: <p>The request was denied due to throttling. Reduce the number of requests and try again.</p>
            capo_qbusiness.errors.validation_exception.ValidationException: <p>The input doesn't meet the constraints set by the Amazon Q Business service. Provide the correct input and try again.</p>
            capo_qbusiness.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_qbusiness.types.list_web_experiences_request.ListWebExperiencesRequest]",
        ) -> OperationResponse[
            "capo_qbusiness.types.list_web_experiences_response.ListWebExperiencesResponse"
        ]:
            import capo_qbusiness._operations.expert_q.list_web_experiences

            output, http_response = (
                capo_qbusiness._operations.expert_q.list_web_experiences.list_web_experiences(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_qbusiness.types.list_web_experiences_request.ListWebExperiencesRequest = {
            "application_id": application_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_web_experiences(
        self,
        application_id: "capo_qbusiness.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[QBusinessClientConfig] = None,
        next_token: Optional["capo_qbusiness.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_qbusiness.types.max_results_integer_for_list_web_experiences_request.MaxResultsIntegerForListWebExperiencesRequest"
        ] = None,
    ) -> "Iterator[capo_qbusiness.types.web_experience.WebExperience]":
        _token = next_token
        while True:
            _response = self.list_web_experiences(
                application_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("web_experiences",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
