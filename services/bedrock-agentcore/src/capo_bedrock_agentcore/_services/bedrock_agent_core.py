"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#AmazonBedrockAgentCore``."""

import datetime
import uuid
import warnings
from collections.abc import Generator, Iterator
from contextlib import contextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_bedrock_agentcore._auth._signers
import capo_bedrock_agentcore._auth._sigv4
from capo_bedrock_agentcore._auth._identity import Credentials
from capo_bedrock_agentcore._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_agentcore._auth._zapros_handler import AuthMiddleware
from capo_bedrock_agentcore._pagination import resolve_path as _resolve_path
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.agentic_resource import (
    AgenticResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.browser_profile_resource import (
    BrowserProfileResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.browser_session_resource import (
    BrowserSessionResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.capacity_provider_resource import (
    CapacityProviderResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.code_interpreter_session_resource import (
    CodeInterpreterSessionResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.evaluation_resource import (
    EvaluationResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.memory_resource import (
    MemoryResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.payment_instrument_resource import (
    PaymentInstrumentResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.payment_session_resource import (
    PaymentSessionResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.process_payment_resource import (
    ProcessPaymentResource,
)
from capo_bedrock_agentcore._resources.amazon_bedrock_agent_core.registry_record_resource import (
    RegistryRecordResource,
)
from capo_bedrock_agentcore._services._aws_config import aws_config
from capo_bedrock_agentcore._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.ab_test_description
    import capo_bedrock_agentcore.types.ab_test_evaluation_config
    import capo_bedrock_agentcore.types.ab_test_execution_status
    import capo_bedrock_agentcore.types.ab_test_id
    import capo_bedrock_agentcore.types.ab_test_name
    import capo_bedrock_agentcore.types.ab_test_summary
    import capo_bedrock_agentcore.types.actor_id
    import capo_bedrock_agentcore.types.actor_summary
    import capo_bedrock_agentcore.types.audiences_list_type
    import capo_bedrock_agentcore.types.batch_create_memory_records_input
    import capo_bedrock_agentcore.types.batch_create_memory_records_output
    import capo_bedrock_agentcore.types.batch_delete_memory_records_input
    import capo_bedrock_agentcore.types.batch_delete_memory_records_output
    import capo_bedrock_agentcore.types.batch_evaluation_description
    import capo_bedrock_agentcore.types.batch_evaluation_id
    import capo_bedrock_agentcore.types.batch_evaluation_name
    import capo_bedrock_agentcore.types.batch_evaluation_summary
    import capo_bedrock_agentcore.types.batch_update_memory_records_input
    import capo_bedrock_agentcore.types.batch_update_memory_records_output
    import capo_bedrock_agentcore.types.blockchain_chain_id
    import capo_bedrock_agentcore.types.body
    import capo_bedrock_agentcore.types.branch
    import capo_bedrock_agentcore.types.browser_action
    import capo_bedrock_agentcore.types.browser_enterprise_policies
    import capo_bedrock_agentcore.types.browser_extensions
    import capo_bedrock_agentcore.types.browser_profile_configuration
    import capo_bedrock_agentcore.types.browser_profile_id
    import capo_bedrock_agentcore.types.browser_session_id
    import capo_bedrock_agentcore.types.browser_session_status
    import capo_bedrock_agentcore.types.browser_session_timeout
    import capo_bedrock_agentcore.types.capacity_provider_id
    import capo_bedrock_agentcore.types.certificates
    import capo_bedrock_agentcore.types.client_token
    import capo_bedrock_agentcore.types.code_interpreter_session_id
    import capo_bedrock_agentcore.types.code_interpreter_session_status
    import capo_bedrock_agentcore.types.code_interpreter_session_timeout
    import capo_bedrock_agentcore.types.complete_resource_token_auth_request
    import capo_bedrock_agentcore.types.complete_resource_token_auth_response
    import capo_bedrock_agentcore.types.content_source
    import capo_bedrock_agentcore.types.create_ab_test_request
    import capo_bedrock_agentcore.types.create_ab_test_response
    import capo_bedrock_agentcore.types.create_event_input
    import capo_bedrock_agentcore.types.create_event_output
    import capo_bedrock_agentcore.types.create_payment_instrument_request
    import capo_bedrock_agentcore.types.create_payment_instrument_response
    import capo_bedrock_agentcore.types.create_payment_session_request
    import capo_bedrock_agentcore.types.create_payment_session_response
    import capo_bedrock_agentcore.types.credential_provider_name
    import capo_bedrock_agentcore.types.custom_request_parameters_type
    import capo_bedrock_agentcore.types.data_source_config
    import capo_bedrock_agentcore.types.delete_ab_test_request
    import capo_bedrock_agentcore.types.delete_ab_test_response
    import capo_bedrock_agentcore.types.delete_batch_evaluation_request
    import capo_bedrock_agentcore.types.delete_batch_evaluation_response
    import capo_bedrock_agentcore.types.delete_capacity_provider_session_request
    import capo_bedrock_agentcore.types.delete_capacity_provider_session_response
    import capo_bedrock_agentcore.types.delete_event_input
    import capo_bedrock_agentcore.types.delete_event_output
    import capo_bedrock_agentcore.types.delete_memory_record_input
    import capo_bedrock_agentcore.types.delete_memory_record_output
    import capo_bedrock_agentcore.types.delete_payment_instrument_request
    import capo_bedrock_agentcore.types.delete_payment_instrument_response
    import capo_bedrock_agentcore.types.delete_payment_session_request
    import capo_bedrock_agentcore.types.delete_payment_session_response
    import capo_bedrock_agentcore.types.delete_recommendation_request
    import capo_bedrock_agentcore.types.delete_recommendation_response
    import capo_bedrock_agentcore.types.evaluate_request
    import capo_bedrock_agentcore.types.evaluate_response
    import capo_bedrock_agentcore.types.evaluation_input
    import capo_bedrock_agentcore.types.evaluation_metadata
    import capo_bedrock_agentcore.types.evaluation_reference_inputs
    import capo_bedrock_agentcore.types.evaluation_target
    import capo_bedrock_agentcore.types.evaluator_id
    import capo_bedrock_agentcore.types.evaluator_list
    import capo_bedrock_agentcore.types.event
    import capo_bedrock_agentcore.types.event_id
    import capo_bedrock_agentcore.types.extraction_config
    import capo_bedrock_agentcore.types.extraction_job
    import capo_bedrock_agentcore.types.extraction_job_filter_input
    import capo_bedrock_agentcore.types.extraction_job_metadata
    import capo_bedrock_agentcore.types.extraction_mode
    import capo_bedrock_agentcore.types.filter_input
    import capo_bedrock_agentcore.types.gateway_arn
    import capo_bedrock_agentcore.types.gateway_filter
    import capo_bedrock_agentcore.types.get_ab_test_request
    import capo_bedrock_agentcore.types.get_ab_test_response
    import capo_bedrock_agentcore.types.get_agent_card_request
    import capo_bedrock_agentcore.types.get_agent_card_response
    import capo_bedrock_agentcore.types.get_batch_evaluation_request
    import capo_bedrock_agentcore.types.get_batch_evaluation_response
    import capo_bedrock_agentcore.types.get_browser_session_request
    import capo_bedrock_agentcore.types.get_browser_session_response
    import capo_bedrock_agentcore.types.get_code_interpreter_session_request
    import capo_bedrock_agentcore.types.get_code_interpreter_session_response
    import capo_bedrock_agentcore.types.get_event_input
    import capo_bedrock_agentcore.types.get_event_output
    import capo_bedrock_agentcore.types.get_memory_record_input
    import capo_bedrock_agentcore.types.get_memory_record_output
    import capo_bedrock_agentcore.types.get_payment_instrument_balance_request
    import capo_bedrock_agentcore.types.get_payment_instrument_balance_response
    import capo_bedrock_agentcore.types.get_payment_instrument_request
    import capo_bedrock_agentcore.types.get_payment_instrument_response
    import capo_bedrock_agentcore.types.get_payment_session_request
    import capo_bedrock_agentcore.types.get_payment_session_response
    import capo_bedrock_agentcore.types.get_recommendation_request
    import capo_bedrock_agentcore.types.get_recommendation_response
    import capo_bedrock_agentcore.types.get_resource_api_key_request
    import capo_bedrock_agentcore.types.get_resource_api_key_response
    import capo_bedrock_agentcore.types.get_resource_oauth2_token_request
    import capo_bedrock_agentcore.types.get_resource_oauth2_token_response
    import capo_bedrock_agentcore.types.get_resource_payment_token_request
    import capo_bedrock_agentcore.types.get_resource_payment_token_response
    import capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_request
    import capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_response
    import capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_request
    import capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_response
    import capo_bedrock_agentcore.types.get_workload_access_token_request
    import capo_bedrock_agentcore.types.get_workload_access_token_response
    import capo_bedrock_agentcore.types.harness_allowed_tools
    import capo_bedrock_agentcore.types.harness_arn
    import capo_bedrock_agentcore.types.harness_endpoint_name
    import capo_bedrock_agentcore.types.harness_messages
    import capo_bedrock_agentcore.types.harness_model_configuration
    import capo_bedrock_agentcore.types.harness_skills
    import capo_bedrock_agentcore.types.harness_system_prompt
    import capo_bedrock_agentcore.types.harness_tools
    import capo_bedrock_agentcore.types.ingest_data_input
    import capo_bedrock_agentcore.types.ingest_data_output
    import capo_bedrock_agentcore.types.insight_list
    import capo_bedrock_agentcore.types.instrument_balance_token
    import capo_bedrock_agentcore.types.invoke_agent_runtime_command_request
    import capo_bedrock_agentcore.types.invoke_agent_runtime_command_request_body
    import capo_bedrock_agentcore.types.invoke_agent_runtime_command_response
    import capo_bedrock_agentcore.types.invoke_agent_runtime_request
    import capo_bedrock_agentcore.types.invoke_agent_runtime_response
    import capo_bedrock_agentcore.types.invoke_browser_request
    import capo_bedrock_agentcore.types.invoke_browser_response
    import capo_bedrock_agentcore.types.invoke_code_interpreter_request
    import capo_bedrock_agentcore.types.invoke_code_interpreter_response
    import capo_bedrock_agentcore.types.invoke_harness_request
    import capo_bedrock_agentcore.types.invoke_harness_response
    import capo_bedrock_agentcore.types.kms_key_arn
    import capo_bedrock_agentcore.types.list_ab_tests_request
    import capo_bedrock_agentcore.types.list_ab_tests_response
    import capo_bedrock_agentcore.types.list_actors_input
    import capo_bedrock_agentcore.types.list_actors_output
    import capo_bedrock_agentcore.types.list_batch_evaluations_request
    import capo_bedrock_agentcore.types.list_batch_evaluations_response
    import capo_bedrock_agentcore.types.list_browser_sessions_request
    import capo_bedrock_agentcore.types.list_browser_sessions_response
    import capo_bedrock_agentcore.types.list_code_interpreter_sessions_request
    import capo_bedrock_agentcore.types.list_code_interpreter_sessions_response
    import capo_bedrock_agentcore.types.list_events_input
    import capo_bedrock_agentcore.types.list_events_output
    import capo_bedrock_agentcore.types.list_memory_extraction_jobs_input
    import capo_bedrock_agentcore.types.list_memory_extraction_jobs_output
    import capo_bedrock_agentcore.types.list_memory_records_input
    import capo_bedrock_agentcore.types.list_memory_records_output
    import capo_bedrock_agentcore.types.list_payment_instruments_request
    import capo_bedrock_agentcore.types.list_payment_instruments_response
    import capo_bedrock_agentcore.types.list_payment_sessions_request
    import capo_bedrock_agentcore.types.list_payment_sessions_response
    import capo_bedrock_agentcore.types.list_recommendations_request
    import capo_bedrock_agentcore.types.list_recommendations_response
    import capo_bedrock_agentcore.types.list_sessions_input
    import capo_bedrock_agentcore.types.list_sessions_output
    import capo_bedrock_agentcore.types.max_results
    import capo_bedrock_agentcore.types.memory_id
    import capo_bedrock_agentcore.types.memory_metadata_filter_list
    import capo_bedrock_agentcore.types.memory_record_id
    import capo_bedrock_agentcore.types.memory_record_summary
    import capo_bedrock_agentcore.types.memory_records_create_input_list
    import capo_bedrock_agentcore.types.memory_records_delete_input_list
    import capo_bedrock_agentcore.types.memory_records_update_input_list
    import capo_bedrock_agentcore.types.memory_strategy_id
    import capo_bedrock_agentcore.types.metadata_filter_expression
    import capo_bedrock_agentcore.types.metadata_map
    import capo_bedrock_agentcore.types.mime_type
    import capo_bedrock_agentcore.types.name
    import capo_bedrock_agentcore.types.namespace
    import capo_bedrock_agentcore.types.next_token
    import capo_bedrock_agentcore.types.oauth2_flow_type
    import capo_bedrock_agentcore.types.output_config
    import capo_bedrock_agentcore.types.pagination_token
    import capo_bedrock_agentcore.types.payload_type_list
    import capo_bedrock_agentcore.types.payment_agent_name
    import capo_bedrock_agentcore.types.payment_connector_id
    import capo_bedrock_agentcore.types.payment_input
    import capo_bedrock_agentcore.types.payment_instrument_details
    import capo_bedrock_agentcore.types.payment_instrument_id
    import capo_bedrock_agentcore.types.payment_instrument_summary
    import capo_bedrock_agentcore.types.payment_instrument_type
    import capo_bedrock_agentcore.types.payment_manager_arn
    import capo_bedrock_agentcore.types.payment_session_id
    import capo_bedrock_agentcore.types.payment_session_summary
    import capo_bedrock_agentcore.types.payment_token_request_input
    import capo_bedrock_agentcore.types.payment_type
    import capo_bedrock_agentcore.types.process_payment_request
    import capo_bedrock_agentcore.types.process_payment_response
    import capo_bedrock_agentcore.types.proxy_configuration
    import capo_bedrock_agentcore.types.recommendation_config
    import capo_bedrock_agentcore.types.recommendation_description
    import capo_bedrock_agentcore.types.recommendation_id
    import capo_bedrock_agentcore.types.recommendation_name
    import capo_bedrock_agentcore.types.recommendation_status
    import capo_bedrock_agentcore.types.recommendation_summary
    import capo_bedrock_agentcore.types.recommendation_type
    import capo_bedrock_agentcore.types.registry_id_list
    import capo_bedrock_agentcore.types.request_uri
    import capo_bedrock_agentcore.types.resource_oauth2_return_url_type
    import capo_bedrock_agentcore.types.resources_list_type
    import capo_bedrock_agentcore.types.retrieve_memory_records_input
    import capo_bedrock_agentcore.types.retrieve_memory_records_output
    import capo_bedrock_agentcore.types.role_arn
    import capo_bedrock_agentcore.types.save_browser_session_profile_request
    import capo_bedrock_agentcore.types.save_browser_session_profile_response
    import capo_bedrock_agentcore.types.scopes_list_type
    import capo_bedrock_agentcore.types.search_criteria
    import capo_bedrock_agentcore.types.search_registry_records_request
    import capo_bedrock_agentcore.types.search_registry_records_response
    import capo_bedrock_agentcore.types.session_filter
    import capo_bedrock_agentcore.types.session_id
    import capo_bedrock_agentcore.types.session_limits
    import capo_bedrock_agentcore.types.session_summary
    import capo_bedrock_agentcore.types.session_type
    import capo_bedrock_agentcore.types.start_batch_evaluation_request
    import capo_bedrock_agentcore.types.start_batch_evaluation_response
    import capo_bedrock_agentcore.types.start_browser_session_request
    import capo_bedrock_agentcore.types.start_browser_session_response
    import capo_bedrock_agentcore.types.start_code_interpreter_session_request
    import capo_bedrock_agentcore.types.start_code_interpreter_session_response
    import capo_bedrock_agentcore.types.start_memory_extraction_job_input
    import capo_bedrock_agentcore.types.start_memory_extraction_job_output
    import capo_bedrock_agentcore.types.start_recommendation_request
    import capo_bedrock_agentcore.types.start_recommendation_response
    import capo_bedrock_agentcore.types.state
    import capo_bedrock_agentcore.types.stop_batch_evaluation_request
    import capo_bedrock_agentcore.types.stop_batch_evaluation_response
    import capo_bedrock_agentcore.types.stop_browser_session_request
    import capo_bedrock_agentcore.types.stop_browser_session_response
    import capo_bedrock_agentcore.types.stop_code_interpreter_session_request
    import capo_bedrock_agentcore.types.stop_code_interpreter_session_response
    import capo_bedrock_agentcore.types.stop_runtime_session_request
    import capo_bedrock_agentcore.types.stop_runtime_session_response
    import capo_bedrock_agentcore.types.stream_update
    import capo_bedrock_agentcore.types.string_type
    import capo_bedrock_agentcore.types.tags_map
    import capo_bedrock_agentcore.types.tool_arguments
    import capo_bedrock_agentcore.types.tool_name
    import capo_bedrock_agentcore.types.tools_file_system_configurations
    import capo_bedrock_agentcore.types.update_ab_test_request
    import capo_bedrock_agentcore.types.update_ab_test_response
    import capo_bedrock_agentcore.types.update_browser_stream_request
    import capo_bedrock_agentcore.types.update_browser_stream_response
    import capo_bedrock_agentcore.types.user_id
    import capo_bedrock_agentcore.types.user_id_type
    import capo_bedrock_agentcore.types.user_identifier
    import capo_bedrock_agentcore.types.user_token_type
    import capo_bedrock_agentcore.types.variant_list
    import capo_bedrock_agentcore.types.view_port
    import capo_bedrock_agentcore.types.workload_identity_name_type
    import capo_bedrock_agentcore.types.workload_identity_token_type


class BedrockAgentCoreClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class BedrockAgentCoreClient:
    """A client for the ``BedrockAgentCore`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
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
        self._config = BedrockAgentCoreClientConfig(
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
        self.agentic_resource = AgenticResource(self)
        self.browser_profile_resource = BrowserProfileResource(self)
        self.browser_session_resource = BrowserSessionResource(self)
        self.capacity_provider_resource = CapacityProviderResource(self)
        self.code_interpreter_session_resource = CodeInterpreterSessionResource(self)
        self.evaluation_resource = EvaluationResource(self)
        self.memory_resource = MemoryResource(self)
        self.payment_instrument_resource = PaymentInstrumentResource(self)
        self.payment_session_resource = PaymentSessionResource(self)
        self.process_payment_resource = ProcessPaymentResource(self)
        self.registry_record_resource = RegistryRecordResource(self)

    def operation_options(
        self, config_overrides: Optional[BedrockAgentCoreClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockAgentCoreClientConfig = config_overrides or {}
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

    def complete_resource_token_auth(
        self,
        user_identifier: "capo_bedrock_agentcore.types.user_identifier.UserIdentifier",
        session_uri: "capo_bedrock_agentcore.types.request_uri.RequestUri",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.complete_resource_token_auth_response.CompleteResourceTokenAuthResponse":
        """<p>Confirms the user authentication session for obtaining OAuth2.0 tokens for a resource.</p>

        Args:
            user_identifier: <p>The OAuth2.0 token or user ID that was used to generate the workload access token used for initiating the user authorization flow to retrieve OAuth2.0 tokens.</p>
            session_uri: <p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.complete_resource_token_auth_request.CompleteResourceTokenAuthRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.complete_resource_token_auth_response.CompleteResourceTokenAuthResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.complete_resource_token_auth

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.complete_resource_token_auth.complete_resource_token_auth(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.complete_resource_token_auth_request.CompleteResourceTokenAuthRequest = {
            "user_identifier": user_identifier,
            "session_uri": session_uri,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_api_key(
        self,
        workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_resource_api_key_response.GetResourceApiKeyResponse":
        """<p>Retrieves the API key associated with an API key credential provider.</p>

        Args:
            workload_identity_token: <p>The identity token of the workload from which you want to retrieve the API key.</p>
            resource_credential_provider_name: <p>The credential provider name for the resource from which you are retrieving the API key.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_resource_api_key_request.GetResourceApiKeyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_resource_api_key_response.GetResourceApiKeyResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_api_key

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_api_key.get_resource_api_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_resource_api_key_request.GetResourceApiKeyRequest = {
            "workload_identity_token": workload_identity_token,
            "resource_credential_provider_name": resource_credential_provider_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_oauth2_token(
        self,
        workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        scopes: "capo_bedrock_agentcore.types.scopes_list_type.ScopesListType",
        oauth2_flow: "capo_bedrock_agentcore.types.oauth2_flow_type.Oauth2FlowType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_uri: Optional[
            "capo_bedrock_agentcore.types.request_uri.RequestUri"
        ] = None,
        resource_oauth2_return_url: Optional[
            "capo_bedrock_agentcore.types.resource_oauth2_return_url_type.ResourceOauth2ReturnUrlType"
        ] = None,
        force_authentication: Optional[bool] = None,
        custom_parameters: Optional[
            "capo_bedrock_agentcore.types.custom_request_parameters_type.CustomRequestParametersType"
        ] = None,
        custom_state: Optional["capo_bedrock_agentcore.types.state.State"] = None,
        resources: Optional[
            "capo_bedrock_agentcore.types.resources_list_type.ResourcesListType"
        ] = None,
        audiences: Optional[
            "capo_bedrock_agentcore.types.audiences_list_type.AudiencesListType"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_resource_oauth2_token_response.GetResourceOauth2TokenResponse":
        """<p>Returns the OAuth 2.0 token of the provided resource.</p>

        Args:
            workload_identity_token: <p>The identity token of the workload from which you want to retrieve the OAuth2 token.</p>
            resource_credential_provider_name: <p>The name of the resource's credential provider.</p>
            scopes: <p>The OAuth scopes being requested.</p>
            oauth2_flow: <p>The type of flow to be performed.</p>
            session_uri: <p>Unique identifier for the user's authentication session for retrieving OAuth2 tokens. This ID tracks the authorization flow state across multiple requests and responses during the OAuth2 authentication process.</p>
            resource_oauth2_return_url: <p>The callback URL to redirect to after the OAuth 2.0 token retrieval is complete. This URL must be one of the provided URLs configured for the workload identity.</p>
            force_authentication: <p>Indicates whether to always initiate a new three-legged OAuth (3LO) flow, regardless of any existing session.</p>
            custom_parameters: <p>A map of custom parameters to include in the authorization request to the resource credential provider. These parameters are in addition to the standard OAuth 2.0 flow parameters, and will not override them.</p>
            custom_state: <p>An opaque string that will be sent back to the callback URL provided in resourceOauth2ReturnUrl. This state should be used to protect the callback URL of your application against CSRF attacks by ensuring the response corresponds to the original request.</p>
            resources: <p>The resources to include in the token request. These are used to specify the target resources for which the OAuth2 token is being requested.</p>
            audiences: <p>The audiences to include in the token request. These are used to specify the intended recipients of the OAuth2 token.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_resource_oauth2_token_request.GetResourceOauth2TokenRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_resource_oauth2_token_response.GetResourceOauth2TokenResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_oauth2_token

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_oauth2_token.get_resource_oauth2_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_resource_oauth2_token_request.GetResourceOauth2TokenRequest = {
            "workload_identity_token": workload_identity_token,
            "resource_credential_provider_name": resource_credential_provider_name,
            "scopes": scopes,
            "oauth2_flow": oauth2_flow,
        }
        if session_uri is not None:
            input_["session_uri"] = session_uri
        if resource_oauth2_return_url is not None:
            input_["resource_oauth2_return_url"] = resource_oauth2_return_url
        if force_authentication is not None:
            input_["force_authentication"] = force_authentication
        if custom_parameters is not None:
            input_["custom_parameters"] = custom_parameters
        if custom_state is not None:
            input_["custom_state"] = custom_state
        if resources is not None:
            input_["resources"] = resources
        if audiences is not None:
            input_["audiences"] = audiences

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_payment_token(
        self,
        workload_identity_token: "capo_bedrock_agentcore.types.workload_identity_token_type.WorkloadIdentityTokenType",
        resource_credential_provider_name: "capo_bedrock_agentcore.types.credential_provider_name.CredentialProviderName",
        payment_token_request: "capo_bedrock_agentcore.types.payment_token_request_input.PaymentTokenRequestInput",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_resource_payment_token_response.GetResourcePaymentTokenResponse":
        """<p>Generates authentication tokens for payment providers that use vendor-specific authentication mechanisms.</p>

        Args:
            workload_identity_token: <p>Workload access token for authorization.</p>
            resource_credential_provider_name: <p>Name of the payment credential provider to use.</p>
            payment_token_request: <p>Vendor-specific token request input. Contains all request parameters in a type-safe, vendor-specific structure.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_resource_payment_token_request.GetResourcePaymentTokenRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_resource_payment_token_response.GetResourcePaymentTokenResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_payment_token

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_resource_payment_token.get_resource_payment_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_resource_payment_token_request.GetResourcePaymentTokenRequest = {
            "workload_identity_token": workload_identity_token,
            "resource_credential_provider_name": resource_credential_provider_name,
            "payment_token_request": payment_token_request,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workload_access_token(
        self,
        workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_workload_access_token_response.GetWorkloadAccessTokenResponse":
        """<p>Obtains a workload access token for agentic workloads not acting on behalf of a user.</p>

        Args:
            workload_name: <p>The unique identifier for the registered workload.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_workload_access_token_request.GetWorkloadAccessTokenRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_workload_access_token_response.GetWorkloadAccessTokenResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token.get_workload_access_token(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_workload_access_token_request.GetWorkloadAccessTokenRequest = {
            "workload_name": workload_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workload_access_token_for_jwt(
        self,
        workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        user_token: "capo_bedrock_agentcore.types.user_token_type.UserTokenType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_response.GetWorkloadAccessTokenForJWTResponse":
        """<p>Obtains a workload access token for agentic workloads acting on behalf of a user, using a JWT token.</p>

        Args:
            workload_name: <p>The unique identifier for the registered workload.</p>
            user_token: <p>The OAuth 2.0 token issued by the user's identity provider.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_request.GetWorkloadAccessTokenForJWTRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_response.GetWorkloadAccessTokenForJWTResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_jwt

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_jwt.get_workload_access_token_for_jwt(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_workload_access_token_for_jwt_request.GetWorkloadAccessTokenForJWTRequest = {
            "workload_name": workload_name,
            "user_token": user_token,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workload_access_token_for_user_id(
        self,
        workload_name: "capo_bedrock_agentcore.types.workload_identity_name_type.WorkloadIdentityNameType",
        user_id: "capo_bedrock_agentcore.types.user_id_type.UserIdType",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_response.GetWorkloadAccessTokenForUserIdResponse":
        """<p>Obtains a workload access token for agentic workloads acting on behalf of a user, using the user's ID.</p>

        Args:
            workload_name: <p>The name of the workload from which you want to retrieve the access token.</p>
            user_id: <p>The ID of the user for whom you are retrieving the access token.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_request.GetWorkloadAccessTokenForUserIdRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_response.GetWorkloadAccessTokenForUserIdResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_user_id

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_workload_access_token_for_user_id.get_workload_access_token_for_user_id(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_workload_access_token_for_user_id_request.GetWorkloadAccessTokenForUserIdRequest = {
            "workload_name": workload_name,
            "user_id": user_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def invoke_code_interpreter(
        self,
        code_interpreter_identifier: str,
        name: "capo_bedrock_agentcore.types.tool_name.ToolName",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        arguments: Optional[
            "capo_bedrock_agentcore.types.tool_arguments.ToolArguments"
        ] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse]":
        """<p>Executes code within an active code interpreter session in Amazon Bedrock AgentCore. This operation processes the provided code, runs it in a secure environment, and returns the execution results including output, errors, and generated visualizations.</p> <p>To execute code, you must specify the code interpreter identifier, session ID, and the code to run in the arguments parameter. The operation returns a stream containing the execution results, which can include text output, error messages, and data visualizations.</p> <p>This operation is subject to request rate limiting based on your account's service quotas.</p> <p>The following operations are related to <code>InvokeCodeInterpreter</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session. This must match the identifier used when creating the session with <code>StartCodeInterpreterSession</code>.</p>
            session_id: <p>The unique identifier of the code interpreter session to use. This must be an active session created with <code>StartCodeInterpreterSession</code>. If the session has expired or been stopped, the request will fail.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            name: <p>The name of the code interpreter to invoke.</p>
            arguments: <p>The arguments for the code interpreter. This includes the code to execute and any additional parameters such as the programming language, whether to clear the execution context, and other execution options. The structure of this parameter depends on the specific code interpreter being used.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_code_interpreter_response.InvokeCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_code_interpreter.invoke_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_code_interpreter_request.InvokeCodeInterpreterRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "name": name,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if arguments is not None:
            input_["arguments"] = arguments

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    @contextmanager
    def invoke_harness(
        self,
        harness_arn: "capo_bedrock_agentcore.types.harness_arn.HarnessArn",
        runtime_session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        messages: "capo_bedrock_agentcore.types.harness_messages.HarnessMessages",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        qualifier: Optional[
            "capo_bedrock_agentcore.types.harness_endpoint_name.HarnessEndpointName"
        ] = None,
        runtime_user_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        trace_state: Optional[str] = None,
        trace_id: Optional[str] = None,
        baggage: Optional[str] = None,
        model: Optional[
            "capo_bedrock_agentcore.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
        actor_id: Optional[str] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse]":
        """<p>Operation to invoke a Harness.</p>

        Args:
            harness_arn: <p>The ARN of the harness to invoke.</p>
            qualifier: <p>The endpoint name to invoke. If omitted, the DEFAULT endpoint is used.</p>
            runtime_session_id: <p>The session ID for the invocation. Use the same session ID across requests to continue a conversation.</p>
            runtime_user_id: <p>An identifier for the end user making the request. This value is passed through to the runtime container.</p>
            trace_parent: <p>W3C trace context parent header containing version, trace ID, parent span ID, and trace flags.</p>
            trace_state: <p>W3C trace context state header for vendor-specific trace information.</p>
            trace_id: <p>Trace ID for maintaining observability through the operation.</p>
            baggage: <p>W3C Baggage header for user-defined context propagation. Format: key1=value1,key2=value2</p>
            messages: <p>The messages to send to the agent.</p>
            model: <p>The model configuration to use for this invocation. If specified, overrides the harness default.</p>
            system_prompt: <p>The system prompt to use for this invocation. If specified, overrides the harness default.</p>
            tools: <p>The tools available to the agent for this invocation. If specified, overrides the harness default.</p>
            skills: <p>The skills available to the agent for this invocation. If specified, overrides the harness default.</p>
            allowed_tools: <p>The tools that the agent is allowed to use for this invocation. If specified, overrides the harness default.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute. If specified, overrides the harness default.</p>
            max_tokens: <p>The maximum number of tokens the agent can generate per iteration. If specified, overrides the harness default.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution. If specified, overrides the harness default.</p>
            actor_id: <p>The actor ID for memory operations. Overrides the actor ID configured on the harness.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_harness_response.InvokeHarnessResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_harness

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_harness.invoke_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_harness_request.InvokeHarnessRequest = {
            "harness_arn": harness_arn,
            "runtime_session_id": runtime_session_id,
            "messages": messages,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if runtime_user_id is not None:
            input_["runtime_user_id"] = runtime_user_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if trace_state is not None:
            input_["trace_state"] = trace_state
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if baggage is not None:
            input_["baggage"] = baggage
        if model is not None:
            input_["model"] = model
        if system_prompt is not None:
            input_["system_prompt"] = system_prompt
        if tools is not None:
            input_["tools"] = tools
        if skills is not None:
            input_["skills"] = skills
        if allowed_tools is not None:
            input_["allowed_tools"] = allowed_tools
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if actor_id is not None:
            input_["actor_id"] = actor_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def get_agent_card(
        self,
        agent_runtime_arn: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        qualifier: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.get_agent_card_response.GetAgentCardResponse":
        """<p>Retrieves the A2A agent card associated with an AgentCore Runtime agent.</p>

        Args:
            runtime_session_id: <p>The session ID that the AgentCore Runtime agent is using. </p>
            agent_runtime_arn: <p>The ARN of the AgentCore Runtime agent for which you want to get the A2A agent card.</p>
            qualifier: <p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_agent_card_request.GetAgentCardRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_agent_card_response.GetAgentCardResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_card

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_agent_card.get_agent_card(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_agent_card_request.GetAgentCardRequest = {
            "agent_runtime_arn": agent_runtime_arn
        }
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if qualifier is not None:
            input_["qualifier"] = qualifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    @contextmanager
    def invoke_agent_runtime(
        self,
        agent_runtime_arn: str,
        payload: "capo_bedrock_agentcore.types.body.Body",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        content_type: Optional[
            "capo_bedrock_agentcore.types.mime_type.MimeType"
        ] = None,
        accept: Optional["capo_bedrock_agentcore.types.mime_type.MimeType"] = None,
        mcp_session_id: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        mcp_protocol_version: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        mcp_method: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        mcp_name: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        runtime_user_id: Optional[
            "capo_bedrock_agentcore.types.string_type.StringType"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        trace_state: Optional[str] = None,
        baggage: Optional[str] = None,
        qualifier: Optional[str] = None,
        account_id: Optional[str] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse]":
        """<p>Sends a request to an agent or tool hosted in an Amazon Bedrock AgentCore Runtime and receives responses in real-time. </p> <p>To invoke an agent, you can specify either the AgentCore Runtime ARN or the agent ID with an account ID, and provide a payload containing your request. When you use the agent ID instead of the full ARN, you don't need to URL-encode the identifier. You can optionally specify a qualifier to target a specific endpoint of the agent.</p> <p>This operation supports streaming responses, allowing you to receive partial responses as they become available. We recommend using pagination to ensure that the operation returns quickly and successfully when processing large responses.</p> <p>For example code, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-invoke-agent.html">Invoke an AgentCore Runtime agent</a>. </p> <p>If you're integrating your agent with OAuth, you can't use the Amazon Web Services SDK to call <code>InvokeAgentRuntime</code>. Instead, make a HTTPS request to <code>InvokeAgentRuntime</code>. For an example, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-oauth.html">Authenticate and authorize with Inbound Auth and Outbound Auth</a>.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:InvokeAgentRuntime</code> permission. If you are making a call to <code>InvokeAgentRuntime</code> on behalf of a user ID with the <code>X-Amzn-Bedrock-AgentCore-Runtime-User-Id</code> header, You require permissions to both actions (<code>bedrock-agentcore:InvokeAgentRuntime</code> and <code>bedrock-agentcore:InvokeAgentRuntimeForUser</code>). </p>

        Args:
            content_type: <p>The MIME type of the input data in the payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>
            accept: <p>The desired MIME type for the response from the agent runtime. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>
            mcp_session_id: <p>The identifier of the MCP session.</p>
            runtime_session_id: <p>The identifier of the runtime session.</p>
            mcp_protocol_version: <p>The version of the MCP protocol being used.</p>
            mcp_method: <p>The MCP method being invoked. For example, <code>tools/call</code>, <code>resources/read</code>, or <code>prompts/get</code>.</p>
            mcp_name: <p>The name of the MCP resource, tool, or prompt being accessed. The value depends on the method:</p> <ul> <li> <p> <code>tools/call</code> – The tool name.</p> </li> <li> <p> <code>resources/read</code> – The resource URI.</p> </li> <li> <p> <code>prompts/get</code> – The prompt name.</p> </li> </ul>
            runtime_user_id: <p>The identifier of the runtime user.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            trace_state: <p>The trace state information for distributed tracing.</p>
            baggage: <p>Additional context information for distributed tracing.</p>
            agent_runtime_arn: <p>The identifier of the agent runtime to invoke. You can specify either the full Amazon Web Services Resource Name (ARN) or the agent ID. If you use the agent ID, you must also provide the <code>accountId</code> query parameter.</p>
            qualifier: <p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>
            account_id: <p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>
            payload: <p>The input data to send to the agent runtime. The format of this data depends on the specific agent configuration and must match the specified content type. For most agents, this is a JSON object containing the user's request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_agent_runtime_response.InvokeAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime.invoke_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_agent_runtime_request.InvokeAgentRuntimeRequest = {
            "agent_runtime_arn": agent_runtime_arn,
            "payload": payload,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if mcp_session_id is not None:
            input_["mcp_session_id"] = mcp_session_id
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if mcp_protocol_version is not None:
            input_["mcp_protocol_version"] = mcp_protocol_version
        if mcp_method is not None:
            input_["mcp_method"] = mcp_method
        if mcp_name is not None:
            input_["mcp_name"] = mcp_name
        if runtime_user_id is not None:
            input_["runtime_user_id"] = runtime_user_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if trace_state is not None:
            input_["trace_state"] = trace_state
        if baggage is not None:
            input_["baggage"] = baggage
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    @contextmanager
    def invoke_agent_runtime_command(
        self,
        agent_runtime_arn: str,
        body: "capo_bedrock_agentcore.types.invoke_agent_runtime_command_request_body.InvokeAgentRuntimeCommandRequestBody",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        content_type: Optional[
            "capo_bedrock_agentcore.types.mime_type.MimeType"
        ] = None,
        accept: Optional["capo_bedrock_agentcore.types.mime_type.MimeType"] = None,
        runtime_session_id: Optional[
            "capo_bedrock_agentcore.types.session_type.SessionType"
        ] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        trace_state: Optional[str] = None,
        baggage: Optional[str] = None,
        qualifier: Optional[str] = None,
        account_id: Optional[str] = None,
    ) -> "Generator[capo_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse]":
        """<p>Executes a command in a runtime session container and streams the output back to the caller. This operation allows you to run shell commands within the agent runtime environment and receive real-time streaming responses including standard output and standard error.</p> <p>To invoke a command, you must specify the agent runtime ARN and a runtime session ID. The command execution supports streaming responses, allowing you to receive output as it becomes available through <code>contentStart</code>, <code>contentDelta</code>, and <code>contentStop</code> events.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:InvokeAgentRuntimeCommand</code> permission.</p>

        Args:
            content_type: <p>The MIME type of the input data in the request payload. This tells the agent runtime how to interpret the payload data. Common values include application/json for JSON data.</p>
            accept: <p>The desired MIME type for the response from the agent runtime command. This tells the agent runtime what format to use for the response data. Common values include application/json for JSON data.</p>
            runtime_session_id: <p>The unique identifier of the runtime session in which to execute the command. This session ID is used to maintain state and context across multiple command invocations.</p>
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            trace_state: <p>The trace state information for distributed tracing.</p>
            baggage: <p>Additional context information for distributed tracing.</p>
            agent_runtime_arn: <p>The Amazon Resource Name (ARN) of the agent runtime on which to execute the command. This identifies the specific agent runtime environment where the command will run.</p>
            qualifier: <p>The qualifier to use for the agent runtime. This is an endpoint name that points to a specific version. If not specified, Amazon Bedrock AgentCore uses the default endpoint of the agent runtime.</p>
            account_id: <p>The identifier of the Amazon Web Services account for the agent runtime resource. This parameter is required when you specify an agent ID instead of the full ARN for <code>agentRuntimeArn</code>.</p>
            body: <p>The request body containing the command to execute and optional configuration parameters such as timeout settings.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_agent_runtime_command_response.InvokeAgentRuntimeCommandResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime_command

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_agent_runtime_command.invoke_agent_runtime_command(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_agent_runtime_command_request.InvokeAgentRuntimeCommandRequest = {
            "agent_runtime_arn": agent_runtime_arn,
            "body": body,
        }
        if content_type is not None:
            input_["content_type"] = content_type
        if accept is not None:
            input_["accept"] = accept
        if runtime_session_id is None:
            runtime_session_id = str(uuid.uuid4())
        input_["runtime_session_id"] = runtime_session_id
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if trace_state is not None:
            input_["trace_state"] = trace_state
        if baggage is not None:
            input_["baggage"] = baggage
        if qualifier is not None:
            input_["qualifier"] = qualifier
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            response.response.close()

    def stop_runtime_session(
        self,
        runtime_session_id: "capo_bedrock_agentcore.types.session_type.SessionType",
        agent_runtime_arn: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        qualifier: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_runtime_session_response.StopRuntimeSessionResponse":
        """<p>Stops a session that is running in an running AgentCore Runtime agent.</p>

        Args:
            runtime_session_id: <p>The ID of the session that you want to stop.</p>
            agent_runtime_arn: <p>The ARN of the agent that contains the session that you want to stop.</p>
            qualifier: <p>Optional qualifier to specify an agent alias, such as <code>prod</code>code&gt; or <code>dev</code>. If you don't provide a value, the DEFAULT alias is used. </p>
            client_token: <p>Idempotent token used to identify the request. If you use the same token with multiple requests, the same response is returned. Use ClientToken to prevent the same request from being processed more than once.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.runtime_client_error.RuntimeClientError: <p>The exception that occurs when there is an error in the runtime client. This can happen due to network issues, invalid configuration, or other client-side problems. Check the error message for specific details about the error.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_runtime_session_request.StopRuntimeSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_runtime_session_response.StopRuntimeSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_runtime_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_runtime_session.stop_runtime_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_runtime_session_request.StopRuntimeSessionRequest = {
            "runtime_session_id": runtime_session_id,
            "agent_runtime_arn": agent_runtime_arn,
        }
        if qualifier is not None:
            input_["qualifier"] = qualifier
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

    def save_browser_session_profile(
        self,
        profile_identifier: "capo_bedrock_agentcore.types.browser_profile_id.BrowserProfileId",
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse":
        """<p>Saves the current state of a browser session as a reusable profile in Amazon Bedrock AgentCore. A browser profile captures persistent browser data such as cookies and local storage from an active session, enabling you to reuse this data in future browser sessions.</p> <p>To save a browser session profile, you must specify the profile identifier, browser identifier, and session ID. The session must be active when saving the profile. Once saved, the profile can be used with the <code>StartBrowserSession</code> operation to initialize new sessions with the stored browser state.</p> <p>Browser profiles are useful for scenarios that require persistent authentication, maintaining user preferences across sessions, or continuing tasks that depend on previously stored browser data.</p> <p>The following operations are related to <code>SaveBrowserSessionProfile</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            profile_identifier: <p>The unique identifier for the browser profile. This identifier is used to reference the profile when starting new browser sessions. The identifier must follow the pattern of an alphanumeric name (up to 48 characters) followed by a hyphen and a 10-character alphanumeric suffix.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session from which to save the profile.</p>
            session_id: <p>The unique identifier of the browser session from which to save the profile. The session must be active when saving the profile.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.save_browser_session_profile_response.SaveBrowserSessionProfileResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.save_browser_session_profile.save_browser_session_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.save_browser_session_profile_request.SaveBrowserSessionProfileRequest = {
            "profile_identifier": profile_identifier,
            "browser_identifier": browser_identifier,
            "session_id": session_id,
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
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

    def get_browser_session(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse":
        """<p>Retrieves detailed information about a specific browser session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, associated streams, and metadata.</p> <p>To get a browser session, you must specify both the browser identifier and the session ID. The response includes information about the session's viewport configuration, timeout settings, and stream endpoints.</p> <p>The following operations are related to <code>GetBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListBrowserSessions.html">ListBrowserSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_browser_session_response.GetBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_browser_session.get_browser_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_browser_session_request.GetBrowserSessionRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def invoke_browser(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        action: "capo_bedrock_agentcore.types.browser_action.BrowserAction",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse":
        """<p>Invokes an operating system-level action on a browser session in Amazon Bedrock AgentCore. This operation provides direct OS-level control over browser sessions, enabling mouse actions, keyboard input, and screenshots that the WebSocket-based Chrome DevTools Protocol (CDP) cannot handle — such as interacting with print dialogs, context menus, and JavaScript alerts.</p> <p>You send a request with exactly one action in the <code>BrowserAction</code> union, and receive a corresponding result in the <code>BrowserActionResult</code> union.</p> <p>The following operations are related to <code>InvokeBrowser</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser associated with the session. This must match the identifier used when creating the session with <code>StartBrowserSession</code>.</p>
            session_id: <p>The unique identifier of the browser session on which to perform the action. This must be an active session created with <code>StartBrowserSession</code>.</p>
            action: <p>The browser action to perform. Exactly one member of the <code>BrowserAction</code> union must be set per request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.invoke_browser_response.InvokeBrowserResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.invoke_browser.invoke_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.invoke_browser_request.InvokeBrowserRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
            "action": action,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_browser_sessions(
        self,
        browser_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore.types.browser_session_status.BrowserSessionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse":
        """<p>Retrieves a list of browser sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by browser identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListBrowserSessions</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            browser_identifier: <p>The unique identifier of the browser to list sessions for. If specified, only sessions for this browser are returned. If not specified, sessions for all browsers are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the browser sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_browser_sessions_response.ListBrowserSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_browser_sessions.list_browser_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_browser_sessions_request.ListBrowserSessionsRequest = {
            "browser_identifier": browser_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_browser_session(
        self,
        browser_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        name: Optional["capo_bedrock_agentcore.types.name.Name"] = None,
        session_timeout_seconds: Optional[
            "capo_bedrock_agentcore.types.browser_session_timeout.BrowserSessionTimeout"
        ] = None,
        view_port: Optional["capo_bedrock_agentcore.types.view_port.ViewPort"] = None,
        extensions: Optional[
            "capo_bedrock_agentcore.types.browser_extensions.BrowserExtensions"
        ] = None,
        profile_configuration: Optional[
            "capo_bedrock_agentcore.types.browser_profile_configuration.BrowserProfileConfiguration"
        ] = None,
        proxy_configuration: Optional[
            "capo_bedrock_agentcore.types.proxy_configuration.ProxyConfiguration"
        ] = None,
        enterprise_policies: Optional[
            "capo_bedrock_agentcore.types.browser_enterprise_policies.BrowserEnterprisePolicies"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse":
        """<p>Creates and initializes a browser session in Amazon Bedrock AgentCore. The session enables agents to navigate and interact with web content, extract information from websites, and perform web-based tasks as part of their response generation.</p> <p>To create a session, you must specify a browser identifier and a name. You can also configure the viewport dimensions to control the visible area of web content. The session remains active until it times out or you explicitly stop it using the <code>StopBrowserSession</code> operation.</p> <p>The following operations are related to <code>StartBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_UpdateBrowserStream.html">UpdateBrowserStream</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_SaveBrowserSessionProfile.html">SaveBrowserSessionProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopBrowserSession.html">StopBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeBrowser.html">InvokeBrowser</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser to use for this session. This identifier specifies which browser environment to initialize for the session.</p>
            name: <p>The name of the browser session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 3600 seconds (1 hour). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            view_port: <p>The dimensions of the browser viewport for this session. This determines the visible area of the web content and affects how web pages are rendered. If not specified, Amazon Bedrock AgentCore uses a default viewport size.</p>
            extensions: <p>A list of browser extensions to load into the browser session.</p>
            profile_configuration: <p>The browser profile configuration to use for this session. A browser profile contains persistent data such as cookies and local storage that can be reused across multiple browser sessions. If specified, the session initializes with the profile's stored data, enabling continuity for tasks that require authentication or personalized settings.</p>
            proxy_configuration: <p>Optional proxy configuration for routing browser traffic through customer-specified proxy servers. When provided, enables HTTP Basic authentication via Amazon Web Services Secrets Manager and domain-based routing rules. Requires <code>secretsmanager:GetSecretValue</code> IAM permission for the specified secret ARNs.</p>
            enterprise_policies: <p>A list of files containing enterprise policies for the browser.</p>
            certificates: <p>A list of certificates to install in the browser session.</p>
            filesystem_configurations: <p>The file system configurations to mount into the browser session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_browser_session_response.StartBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_browser_session.start_browser_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_browser_session_request.StartBrowserSessionRequest = {
            "browser_identifier": browser_identifier
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if name is not None:
            input_["name"] = name
        if session_timeout_seconds is not None:
            input_["session_timeout_seconds"] = session_timeout_seconds
        if view_port is not None:
            input_["view_port"] = view_port
        if extensions is not None:
            input_["extensions"] = extensions
        if profile_configuration is not None:
            input_["profile_configuration"] = profile_configuration
        if proxy_configuration is not None:
            input_["proxy_configuration"] = proxy_configuration
        if enterprise_policies is not None:
            input_["enterprise_policies"] = enterprise_policies
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    def stop_browser_session(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse":
        """<p>Terminates an active browser session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a browser session, you must specify both the browser identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartBrowserSession</code>.</p> <p>The following operations are related to <code>StopBrowserSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartBrowserSession.html">StartBrowserSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetBrowserSession.html">GetBrowserSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            browser_identifier: <p>The unique identifier of the browser associated with the session.</p>
            session_id: <p>The unique identifier of the browser session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_browser_session_response.StopBrowserSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_browser_session.stop_browser_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_browser_session_request.StopBrowserSessionRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
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

    def update_browser_stream(
        self,
        browser_identifier: str,
        session_id: "capo_bedrock_agentcore.types.browser_session_id.BrowserSessionId",
        stream_update: "capo_bedrock_agentcore.types.stream_update.StreamUpdate",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse":
        """<p>Updates a browser stream. To use this operation, you must have permissions to perform the bedrock:UpdateBrowserStream action.</p>

        Args:
            browser_identifier: <p>The identifier of the browser.</p>
            session_id: <p>The identifier of the browser session.</p>
            stream_update: <p>The update to apply to the browser stream.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.update_browser_stream_response.UpdateBrowserStreamResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_browser_stream.update_browser_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.update_browser_stream_request.UpdateBrowserStreamRequest = {
            "browser_identifier": browser_identifier,
            "session_id": session_id,
            "stream_update": stream_update,
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

    def delete_capacity_provider_session(
        self,
        capacity_provider_id: "capo_bedrock_agentcore.types.capacity_provider_id.CapacityProviderId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_capacity_provider_session_response.DeleteCapacityProviderSessionResponse":
        """<p>Deletes a session associated with a capacity provider in Amazon Bedrock AgentCore and makes the session unavailable for further use. To delete a capacity provider session, specify both the capacity provider identifier and the session ID. After you delete a session, you cannot restart it.</p>

        Args:
            capacity_provider_id: <p>The unique identifier of the capacity provider associated with the session.</p>
            session_id: <p>The unique identifier of the capacity provider session to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_capacity_provider_session_request.DeleteCapacityProviderSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_capacity_provider_session_response.DeleteCapacityProviderSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_capacity_provider_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_capacity_provider_session.delete_capacity_provider_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_capacity_provider_session_request.DeleteCapacityProviderSessionRequest = {
            "capacity_provider_id": capacity_provider_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_code_interpreter_session(
        self,
        code_interpreter_identifier: str,
        session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse":
        """<p>Retrieves detailed information about a specific code interpreter session in Amazon Bedrock AgentCore. This operation returns the session's configuration, current status, and metadata.</p> <p>To get a code interpreter session, you must specify both the code interpreter identifier and the session ID. The response includes information about the session's timeout settings and current status.</p> <p>The following operations are related to <code>GetCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_ListCodeInterpreterSessions.html">ListCodeInterpreterSessions</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_code_interpreter_session_response.GetCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_code_interpreter_session.get_code_interpreter_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_code_interpreter_session_request.GetCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_code_interpreter_sessions(
        self,
        code_interpreter_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_status.CodeInterpreterSessionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse":
        """<p>Retrieves a list of code interpreter sessions in Amazon Bedrock AgentCore that match the specified criteria. This operation returns summary information about each session, including identifiers, status, and timestamps.</p> <p>You can filter the results by code interpreter identifier and session status. The operation supports pagination to handle large result sets efficiently.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully when retrieving large numbers of sessions.</p> <p>The following operations are related to <code>ListCodeInterpreterSessions</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to list sessions for. If specified, only sessions for this code interpreter are returned. If not specified, sessions for all code interpreters are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. Valid values range from 1 to 100. To retrieve the remaining results, make another call with the returned <code>nextToken</code> value.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. If not specified, Amazon Bedrock AgentCore returns the first page of results.</p>
            status: <p>The status of the code interpreter sessions to list. Valid values include ACTIVE, STOPPING, and STOPPED. If not specified, sessions with any status are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_code_interpreter_sessions_response.ListCodeInterpreterSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_code_interpreter_sessions.list_code_interpreter_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_code_interpreter_sessions_request.ListCodeInterpreterSessionsRequest = {
            "code_interpreter_identifier": code_interpreter_identifier
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_code_interpreter_session(
        self,
        code_interpreter_identifier: str,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        name: Optional["capo_bedrock_agentcore.types.name.Name"] = None,
        session_timeout_seconds: Optional[
            "capo_bedrock_agentcore.types.code_interpreter_session_timeout.CodeInterpreterSessionTimeout"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse":
        """<p>Creates and initializes a code interpreter session in Amazon Bedrock AgentCore. The session enables agents to execute code as part of their response generation, supporting programming languages such as Python for data analysis, visualization, and computation tasks.</p> <p>To create a session, you must specify a code interpreter identifier and a name. The session remains active until it times out or you explicitly stop it using the <code>StopCodeInterpreterSession</code> operation.</p> <p>The following operations are related to <code>StartCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_InvokeCodeInterpreter.html">InvokeCodeInterpreter</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StopCodeInterpreterSession.html">StopCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter to use for this session. This identifier specifies which code interpreter environment to initialize for the session.</p>
            name: <p>The name of the code interpreter session. This name helps you identify and manage the session. The name does not need to be unique.</p>
            session_timeout_seconds: <p>The duration in seconds (time-to-live) after which the session automatically terminates, regardless of ongoing activity. Defaults to 900 seconds (15 minutes). Recommended minimum: 60 seconds. Maximum allowed: 28,800 seconds (8 hours).</p>
            certificates: <p>A list of certificates to install in the code interpreter session.</p>
            filesystem_configurations: <p>The file system configurations to mount into the code interpreter session. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your session can then read and write your data. If you don't specify this field, no additional file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error. This parameter helps prevent the creation of duplicate sessions if there are temporary network issues.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_code_interpreter_session_response.StartCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_code_interpreter_session.start_code_interpreter_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_code_interpreter_session_request.StartCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
        if name is not None:
            input_["name"] = name
        if session_timeout_seconds is not None:
            input_["session_timeout_seconds"] = session_timeout_seconds
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    def stop_code_interpreter_session(
        self,
        code_interpreter_identifier: str,
        session_id: "capo_bedrock_agentcore.types.code_interpreter_session_id.CodeInterpreterSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        trace_id: Optional[str] = None,
        trace_parent: Optional[str] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse":
        """<p>Terminates an active code interpreter session in Amazon Bedrock AgentCore. This operation stops the session, releases associated resources, and makes the session unavailable for further use.</p> <p>To stop a code interpreter session, you must specify both the code interpreter identifier and the session ID. Once stopped, a session cannot be restarted; you must create a new session using <code>StartCodeInterpreterSession</code>.</p> <p>The following operations are related to <code>StopCodeInterpreterSession</code>:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_StartCodeInterpreterSession.html">StartCodeInterpreterSession</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/API_GetCodeInterpreterSession.html">GetCodeInterpreterSession</a> </p> </li> </ul>

        Args:
            trace_id: <p>The trace identifier for request tracking.</p>
            trace_parent: <p>The parent trace information for distributed tracing.</p>
            code_interpreter_identifier: <p>The unique identifier of the code interpreter associated with the session.</p>
            session_id: <p>The unique identifier of the code interpreter session to stop.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_code_interpreter_session_response.StopCodeInterpreterSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_code_interpreter_session.stop_code_interpreter_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_code_interpreter_session_request.StopCodeInterpreterSessionRequest = {
            "code_interpreter_identifier": code_interpreter_identifier,
            "session_id": session_id,
        }
        if trace_id is not None:
            input_["trace_id"] = trace_id
        if trace_parent is not None:
            input_["trace_parent"] = trace_parent
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

    def create_ab_test(
        self,
        name: "capo_bedrock_agentcore.types.ab_test_name.ABTestName",
        gateway_arn: "capo_bedrock_agentcore.types.gateway_arn.GatewayArn",
        variants: "capo_bedrock_agentcore.types.variant_list.VariantList",
        evaluation_config: "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig",
        role_arn: "capo_bedrock_agentcore.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
        ] = None,
        gateway_filter: Optional[
            "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
        ] = None,
        enable_on_create: Optional[bool] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse":
        """<p>Creates an A/B test for comparing agent configurations. A/B tests split traffic between a control variant and a treatment variant through a gateway, then evaluate performance using online evaluation configurations to determine which variant performs better.</p>

        Args:
            name: <p>The name of the A/B test. Must be unique within your account.</p>
            description: <p>The description of the A/B test.</p>
            gateway_arn: <p>The Amazon Resource Name (ARN) of the gateway to use for traffic splitting.</p>
            variants: <p>The list of variants for the A/B test. Must contain exactly two variants: a control (C) and a treatment (T1), each with a configuration bundle or target reference and a traffic weight.</p>
            gateway_filter: <p>Optional filter to restrict which gateway target paths are included in the A/B test.</p>
            evaluation_config: <p>The evaluation configuration specifying which online evaluation configurations to use for measuring variant performance.</p>
            role_arn: <p>The IAM role ARN that grants permissions for the A/B test to access gateway and evaluation resources.</p>
            enable_on_create: <p>Whether to enable the A/B test immediately upon creation. If true, traffic splitting begins automatically.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>A map of tag keys and values to associate with the A/B test.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_ab_test_response.CreateABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_ab_test.create_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.create_ab_test_request.CreateABTestRequest = {
            "name": name,
            "gateway_arn": gateway_arn,
            "variants": variants,
            "evaluation_config": evaluation_config,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if gateway_filter is not None:
            input_["gateway_filter"] = gateway_filter
        if enable_on_create is not None:
            input_["enable_on_create"] = enable_on_create
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

    def delete_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse":
        """<p>Deletes an A/B test and its associated gateway rules.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_ab_test_response.DeleteABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_ab_test.delete_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_ab_test_request.DeleteABTestRequest = {
            "ab_test_id": ab_test_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse":
        """<p>Deletes a batch evaluation and its associated results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_batch_evaluation_response.DeleteBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_batch_evaluation.delete_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_batch_evaluation_request.DeleteBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_recommendation(
        self,
        recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse":
        """<p>Deletes a recommendation and its associated results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_recommendation_response.DeleteRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_recommendation.delete_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_recommendation_request.DeleteRecommendationRequest = {
            "recommendation_id": recommendation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def evaluate(
        self,
        evaluator_id: "capo_bedrock_agentcore.types.evaluator_id.EvaluatorId",
        evaluation_input: "capo_bedrock_agentcore.types.evaluation_input.EvaluationInput",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        evaluation_target: Optional[
            "capo_bedrock_agentcore.types.evaluation_target.EvaluationTarget"
        ] = None,
        evaluation_reference_inputs: Optional[
            "capo_bedrock_agentcore.types.evaluation_reference_inputs.EvaluationReferenceInputs"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse":
        """<p> Performs on-demand evaluation of agent traces using a specified evaluator. This synchronous API accepts traces in OpenTelemetry format and returns immediate scoring results with detailed explanations.</p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to use for scoring. Can be a built-in evaluator (e.g., <code>Builtin.Helpfulness</code>, <code>Builtin.Correctness</code>) or a custom evaluator Id created through the control plane API. </p>
            evaluation_input: <p> The input data containing agent session spans to be evaluated. Includes a list of spans in OpenTelemetry format from supported frameworks like Strands (AgentCore Runtime) or LangGraph with OpenInference instrumentation. </p>
            evaluation_target: <p> The specific trace or span IDs to evaluate within the provided input. Allows targeting evaluation at different levels: individual tool calls, single request-response interactions (traces), or entire conversation sessions. </p>
            evaluation_reference_inputs: <p> Ground truth data to compare against agent responses during evaluation. Allows to provide expected responses, assertions, and expected tool trajectories at different evaluation levels. Session-level reference inputs apply to the entire conversation, while trace-level reference inputs target specific request-response interactions identified by trace ID. </p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.duplicate_id_exception.DuplicateIdException: <p> An exception thrown when attempting to create a resource with an identifier that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.evaluate_response.EvaluateResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.evaluate.evaluate(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.evaluate_request.EvaluateRequest = {
            "evaluator_id": evaluator_id,
            "evaluation_input": evaluation_input,
        }
        if evaluation_target is not None:
            input_["evaluation_target"] = evaluation_target
        if evaluation_reference_inputs is not None:
            input_["evaluation_reference_inputs"] = evaluation_reference_inputs

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse":
        """<p>Retrieves detailed information about an A/B test, including its configuration, status, and statistical results.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_ab_test_response.GetABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_ab_test.get_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_ab_test_request.GetABTestRequest = {
            "ab_test_id": ab_test_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse":
        """<p>Retrieves detailed information about a batch evaluation, including its status, configuration, results, and any error details.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_batch_evaluation_response.GetBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_batch_evaluation.get_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_batch_evaluation_request.GetBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_recommendation(
        self,
        recommendation_id: "capo_bedrock_agentcore.types.recommendation_id.RecommendationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse":
        """<p>Retrieves detailed information about a recommendation, including its configuration, status, and results.</p>

        Args:
            recommendation_id: <p>The unique identifier of the recommendation to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_recommendation_response.GetRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_recommendation.get_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_recommendation_request.GetRecommendationRequest = {
            "recommendation_id": recommendation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_ab_tests(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse":
        """<p>Lists all A/B tests in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_ab_tests_response.ListABTestsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_ab_tests.list_ab_tests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_ab_tests_request.ListABTestsRequest = {}
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

    def iter_list_ab_tests(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.ab_test_summary.ABTestSummary]":
        _token = next_token
        while True:
            _response = self.list_ab_tests(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ab_tests",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_batch_evaluations(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse":
        """<p>Lists all batch evaluations in the account, providing summary information about each evaluation's status and configuration.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_batch_evaluations_response.ListBatchEvaluationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_batch_evaluations.list_batch_evaluations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_batch_evaluations_request.ListBatchEvaluationsRequest = {}
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

    def iter_list_batch_evaluations(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.batch_evaluation_summary.BatchEvaluationSummary]":
        _token = next_token
        while True:
            _response = self.list_batch_evaluations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("batch_evaluations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_recommendations(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status_filter: Optional[
            "capo_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse":
        """<p>Lists all recommendations in the account, with optional filtering by status.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status_filter: <p>Optional filter to return only recommendations with the specified status.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_recommendations_response.ListRecommendationsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_recommendations.list_recommendations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_recommendations_request.ListRecommendationsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status_filter is not None:
            input_["status_filter"] = status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_recommendations(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        status_filter: Optional[
            "capo_bedrock_agentcore.types.recommendation_status.RecommendationStatus"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.recommendation_summary.RecommendationSummary]":
        _token = next_token
        while True:
            _response = self.list_recommendations(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status_filter=status_filter,
            )
            _page = _resolve_path(_response, ("recommendation_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_batch_evaluation(
        self,
        batch_evaluation_name: "capo_bedrock_agentcore.types.batch_evaluation_name.BatchEvaluationName",
        data_source_config: "capo_bedrock_agentcore.types.data_source_config.DataSourceConfig",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        evaluators: Optional[
            "capo_bedrock_agentcore.types.evaluator_list.EvaluatorList"
        ] = None,
        insights: Optional[
            "capo_bedrock_agentcore.types.insight_list.InsightList"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        evaluation_metadata: Optional[
            "capo_bedrock_agentcore.types.evaluation_metadata.EvaluationMetadata"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.batch_evaluation_description.BatchEvaluationDescription"
        ] = None,
        output_config: Optional[
            "capo_bedrock_agentcore.types.output_config.OutputConfig"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse":
        """<p>Starts a batch evaluation job that evaluates agent performance across multiple sessions. Batch evaluations pull agent traces from CloudWatch Logs or an existing online evaluation configuration and run specified evaluators and insights against them.</p>

        Args:
            batch_evaluation_name: <p>The name of the batch evaluation. Must be unique within your account.</p>
            evaluators: <p>The list of evaluators to apply during the batch evaluation. Can include both built-in evaluators and custom evaluators. Maximum of 10 evaluators.</p>
            insights: <p>The list of insight analyses to run against sessions during the batch evaluation. Maximum of 10 insights.</p>
            data_source_config: <p>The data source configuration that specifies where to pull agent session traces from for evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            evaluation_metadata: <p>Optional metadata for the evaluation, including session-specific ground truth data and test scenario identifiers.</p>
            tags: <p>A map of tag keys and values to associate with the batch evaluation.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt evaluation data. If provided, customer data is encrypted at rest with the specified key.</p>
            description: <p>The description of the batch evaluation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_batch_evaluation_response.StartBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_batch_evaluation.start_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_batch_evaluation_request.StartBatchEvaluationRequest = {
            "batch_evaluation_name": batch_evaluation_name,
            "data_source_config": data_source_config,
        }
        if evaluators is not None:
            input_["evaluators"] = evaluators
        if insights is not None:
            input_["insights"] = insights
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if evaluation_metadata is not None:
            input_["evaluation_metadata"] = evaluation_metadata
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if description is not None:
            input_["description"] = description
        if output_config is not None:
            input_["output_config"] = output_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_recommendation(
        self,
        name: "capo_bedrock_agentcore.types.recommendation_name.RecommendationName",
        type: "capo_bedrock_agentcore.types.recommendation_type.RecommendationType",
        recommendation_config: "capo_bedrock_agentcore.types.recommendation_config.RecommendationConfig",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.recommendation_description.RecommendationDescription"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore.types.kms_key_arn.KmsKeyArn"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse":
        """<p>Starts a recommendation job that analyzes agent traces and generates optimization suggestions for system prompts or tool descriptions to improve agent performance.</p>

        Args:
            name: <p>The name of the recommendation. Must be unique within your account.</p>
            description: <p>The description of the recommendation.</p>
            type: <p>The type of recommendation to generate. Valid values are <code>SYSTEM_PROMPT_RECOMMENDATION</code> for system prompt optimization or <code>TOOL_DESCRIPTION_RECOMMENDATION</code> for tool description optimization.</p>
            recommendation_config: <p>The configuration for the recommendation, including the input to optimize, agent traces to analyze, and evaluation settings.</p>
            kms_key_arn: <p>The ARN of the KMS key used to encrypt recommendation data. If provided, customer data is encrypted at rest with the specified key.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            tags: <p>A map of tag keys and values to associate with the recommendation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_recommendation_response.StartRecommendationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_recommendation.start_recommendation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_recommendation_request.StartRecommendationRequest = {
            "name": name,
            "type": type,
            "recommendation_config": recommendation_config,
        }
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
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

    def stop_batch_evaluation(
        self,
        batch_evaluation_id: "capo_bedrock_agentcore.types.batch_evaluation_id.BatchEvaluationId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse":
        """<p>Stops a running batch evaluation. Sessions that have already been evaluated retain their results.</p>

        Args:
            batch_evaluation_id: <p>The unique identifier of the batch evaluation to stop.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.stop_batch_evaluation_response.StopBatchEvaluationResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.stop_batch_evaluation.stop_batch_evaluation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.stop_batch_evaluation_request.StopBatchEvaluationRequest = {
            "batch_evaluation_id": batch_evaluation_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_ab_test(
        self,
        ab_test_id: "capo_bedrock_agentcore.types.ab_test_id.ABTestId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
        name: Optional["capo_bedrock_agentcore.types.ab_test_name.ABTestName"] = None,
        description: Optional[
            "capo_bedrock_agentcore.types.ab_test_description.ABTestDescription"
        ] = None,
        variants: Optional[
            "capo_bedrock_agentcore.types.variant_list.VariantList"
        ] = None,
        gateway_filter: Optional[
            "capo_bedrock_agentcore.types.gateway_filter.GatewayFilter"
        ] = None,
        evaluation_config: Optional[
            "capo_bedrock_agentcore.types.ab_test_evaluation_config.ABTestEvaluationConfig"
        ] = None,
        role_arn: Optional["capo_bedrock_agentcore.types.role_arn.RoleArn"] = None,
        execution_status: Optional[
            "capo_bedrock_agentcore.types.ab_test_execution_status.ABTestExecutionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse":
        """<p>Updates an A/B test's configuration, including variants, traffic allocation, evaluation settings, or execution status.</p>

        Args:
            ab_test_id: <p>The unique identifier of the A/B test to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, the service ignores the request, but does not return an error.</p>
            name: <p>The updated name of the A/B test.</p>
            description: <p>The updated description of the A/B test.</p>
            variants: <p>The updated list of variants.</p>
            gateway_filter: <p>The updated gateway filter.</p>
            evaluation_config: <p>The updated evaluation configuration.</p>
            role_arn: <p>The updated IAM role ARN.</p>
            execution_status: <p>The updated execution status to enable or disable the A/B test.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.update_ab_test_response.UpdateABTestResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.update_ab_test.update_ab_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.update_ab_test_request.UpdateABTestRequest = {
            "ab_test_id": ab_test_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if variants is not None:
            input_["variants"] = variants
        if gateway_filter is not None:
            input_["gateway_filter"] = gateway_filter
        if evaluation_config is not None:
            input_["evaluation_config"] = evaluation_config
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if execution_status is not None:
            input_["execution_status"] = execution_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_create_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_create_input_list.MemoryRecordsCreateInputList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput":
        """<p>Creates multiple memory records in a single batch operation for the specified memory with custom content.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be created.</p>
            records: <p>A list of memory record creation inputs to be processed in the batch operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the batch request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.batch_create_memory_records_output.BatchCreateMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_create_memory_records.batch_create_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.batch_create_memory_records_input.BatchCreateMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
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

    def batch_delete_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_delete_input_list.MemoryRecordsDeleteInputList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput":
        """<p>Deletes multiple memory records in a single batch operation from the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be deleted.</p>
            records: <p>A list of memory record deletion inputs to be processed in the batch operation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.batch_delete_memory_records_output.BatchDeleteMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_delete_memory_records.batch_delete_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.batch_delete_memory_records_input.BatchDeleteMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        records: "capo_bedrock_agentcore.types.memory_records_update_input_list.MemoryRecordsUpdateInputList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput":
        """<p>Updates multiple memory records with custom content in a single batch operation within the specified memory.</p>

        Args:
            memory_id: <p>The unique ID of the memory resource where records will be updated.</p>
            records: <p>A list of memory record update inputs to be processed in the batch operation.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.batch_update_memory_records_output.BatchUpdateMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.batch_update_memory_records.batch_update_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.batch_update_memory_records_input.BatchUpdateMemoryRecordsInput = {
            "memory_id": memory_id,
            "records": records,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        event_timestamp: datetime.datetime,
        payload: "capo_bedrock_agentcore.types.payload_type_list.PayloadTypeList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.session_id.SessionId"
        ] = None,
        branch: Optional["capo_bedrock_agentcore.types.branch.Branch"] = None,
        client_token: Optional[str] = None,
        metadata: Optional[
            "capo_bedrock_agentcore.types.metadata_map.MetadataMap"
        ] = None,
        extraction_mode: Optional[
            "capo_bedrock_agentcore.types.extraction_mode.ExtractionMode"
        ] = None,
        extraction_config: Optional[
            "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput":
        """<p>Creates an event in an AgentCore Memory resource. Events represent interactions or activities that occur within a session and are associated with specific actors.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:CreateEvent</code> permission.</p> <p>This operation is subject to request rate limiting.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource in which to create the event.</p>
            actor_id: <p>The identifier of the actor associated with this event. An actor represents an entity that participates in sessions and generates events.</p>
            session_id: <p>The identifier of the session in which this event occurs. A session represents a sequence of related events.</p>
            event_timestamp: <p>The timestamp when the event occurred. If not specified, the current time is used.</p>
            payload: <p>The content payload of the event. This can include conversational data, JSON data, or binary content.</p>
            branch: <p>The branch information for this event. Branches allow for organizing events into different conversation threads or paths.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>
            metadata: <p>The key-value metadata to attach to the event.</p>
            extraction_mode: <p>Controls long-term memory extraction for this event. When set to <code>SKIP</code>, the event is stored in short-term memory but is excluded from long-term memory extraction. If not specified, the event is processed for extraction as usual.</p>
            extraction_config: <p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.retryable_conflict_exception.RetryableConflictException: <p>The exception that occurs when there is a retryable conflict performing an operation. This is a temporary condition that may resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.create_event_input.CreateEventInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_event_output.CreateEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_event.create_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.create_event_input.CreateEventInput = {
            "memory_id": memory_id,
            "actor_id": actor_id,
            "event_timestamp": event_timestamp,
            "payload": payload,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if branch is not None:
            input_["branch"] = branch
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if metadata is not None:
            input_["metadata"] = metadata
        if extraction_mode is not None:
            input_["extraction_mode"] = extraction_mode
        if extraction_config is not None:
            input_["extraction_config"] = extraction_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        event_id: "capo_bedrock_agentcore.types.event_id.EventId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.delete_event_output.DeleteEventOutput":
        """<p>Deletes an event from an AgentCore Memory resource. When you delete an event, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the event.</p>
            session_id: <p>The identifier of the session containing the event to delete.</p>
            event_id: <p>The identifier of the event to delete.</p>
            actor_id: <p>The identifier of the actor associated with the event to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_event_input.DeleteEventInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_event_output.DeleteEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_event.delete_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_event_input.DeleteEventInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "event_id": event_id,
            "actor_id": actor_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_memory_record(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput":
        """<p>Deletes a memory record from an AgentCore Memory resource. When you delete a memory record, it is permanently removed.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:DeleteMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to delete the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to delete.</p>
            namespace: <p>The namespace of the memory record to delete. This value is used for IAM condition key authorization.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_memory_record_output.DeleteMemoryRecordOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_memory_record.delete_memory_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_memory_record_input.DeleteMemoryRecordInput = {
            "memory_id": memory_id,
            "memory_record_id": memory_record_id,
        }
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_event(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        event_id: "capo_bedrock_agentcore.types.event_id.EventId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
    ) -> "capo_bedrock_agentcore.types.get_event_output.GetEventOutput":
        """<p>Retrieves information about a specific event in an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetEvent</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the event.</p>
            session_id: <p>The identifier of the session containing the event.</p>
            actor_id: <p>The identifier of the actor associated with the event.</p>
            event_id: <p>The identifier of the event to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_event_input.GetEventInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_event_output.GetEventOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_event.get_event(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_event_input.GetEventInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "actor_id": actor_id,
            "event_id": event_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_memory_record(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        memory_record_id: "capo_bedrock_agentcore.types.memory_record_id.MemoryRecordId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
    ) -> "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput":
        """<p>Retrieves a specific memory record from an AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:GetMemoryRecord</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource containing the memory record.</p>
            memory_record_id: <p>The identifier of the memory record to retrieve.</p>
            namespace: <p>The namespace of the memory record to retrieve. This value is used for IAM condition key authorization.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_memory_record_output.GetMemoryRecordOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_memory_record.get_memory_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_memory_record_input.GetMemoryRecordInput = {
            "memory_id": memory_id,
            "memory_record_id": memory_record_id,
        }
        if namespace is not None:
            input_["namespace"] = namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def ingest_data(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        source: "capo_bedrock_agentcore.types.content_source.ContentSource",
        content_timestamp: datetime.datetime,
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        session_id: Optional[
            "capo_bedrock_agentcore.types.session_id.SessionId"
        ] = None,
        extraction_config: Optional[
            "capo_bedrock_agentcore.types.extraction_config.ExtractionConfig"
        ] = None,
        metadata: Optional[
            "capo_bedrock_agentcore.types.metadata_map.MetadataMap"
        ] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.ingest_data_output.IngestDataOutput":
        """<p>Submits content directly for ingestion to generate long-term memory records in a AgentCore Memory resource.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:IngestData</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource to ingest content into.</p>
            source: <p>The content to ingest. Only inline content is supported.</p>
            content_timestamp: <p>The timestamp of when the content occurred.</p>
            actor_id: <p>The identifier of the actor associated with this content. An actor represents an entity that participates in sessions and generates content.</p>
            session_id: <p>The identifier of the session that the content belongs to. If not provided, a session identifier is generated and returned in the response.</p>
            extraction_config: <p>The extraction configuration for long-term memory records. Use this parameter to specify namespace variable keys and their values for namespace substitution during extraction.</p>
            metadata: <p>The key-value metadata to attach to the content.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, AgentCore ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.ingest_data_output.IngestDataOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.ingest_data

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.ingest_data.ingest_data(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.ingest_data_input.IngestDataInput = {
            "memory_id": memory_id,
            "source": source,
            "content_timestamp": content_timestamp,
            "actor_id": actor_id,
        }
        if session_id is not None:
            input_["session_id"] = session_id
        if extraction_config is not None:
            input_["extraction_config"] = extraction_config
        if metadata is not None:
            input_["metadata"] = metadata
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

    def list_actors(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_actors_output.ListActorsOutput":
        """<p>Lists all actors in an AgentCore Memory resource. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListActors</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list actors.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_actors_input.ListActorsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_actors_output.ListActorsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_actors.list_actors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_actors_input.ListActorsInput = {
            "memory_id": memory_id
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

    def iter_list_actors(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.actor_summary.ActorSummary]":
        _token = next_token
        while True:
            _response = self.list_actors(
                memory_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("actor_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_events(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        include_payloads: Optional[bool] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.filter_input.FilterInput"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput":
        """<p>Lists events in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListEvents</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list events.</p>
            session_id: <p>The identifier of the session for which to list events.</p>
            actor_id: <p>The identifier of the actor for which to list events.</p>
            include_payloads: <p>Specifies whether to include event payloads in the response. Set to true to include payloads, or false to exclude them.</p>
            filter: <p>Filter criteria to apply when listing events.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_events_input.ListEventsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_events_output.ListEventsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_events.list_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_events_input.ListEventsInput = {
            "memory_id": memory_id,
            "session_id": session_id,
            "actor_id": actor_id,
        }
        if include_payloads is not None:
            input_["include_payloads"] = include_payloads
        if filter is not None:
            input_["filter"] = filter
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

    def iter_list_events(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        session_id: "capo_bedrock_agentcore.types.session_id.SessionId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        include_payloads: Optional[bool] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.filter_input.FilterInput"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.event.Event]":
        _token = next_token
        while True:
            _response = self.list_events(
                memory_id,
                session_id,
                actor_id,
                config_overrides=config_overrides,
                include_payloads=include_payloads,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_memory_extraction_jobs(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput":
        """<p>Lists all long-term memory extraction jobs that are eligible to be started with optional filtering.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryExtractionJobs</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to list extraction jobs for.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            filter: <p>Filter criteria to apply when listing extraction jobs.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_memory_extraction_jobs_output.ListMemoryExtractionJobsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_extraction_jobs.list_memory_extraction_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_memory_extraction_jobs_input.ListMemoryExtractionJobsInput = {
            "memory_id": memory_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_memory_extraction_jobs(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.extraction_job_filter_input.ExtractionJobFilterInput"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.extraction_job_metadata.ExtractionJobMetadata]":
        _token = next_token
        while True:
            _response = self.list_memory_extraction_jobs(
                memory_id,
                config_overrides=config_overrides,
                max_results=max_results,
                filter=filter,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        memory_strategy_id: Optional[
            "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        metadata_filters: Optional[
            "capo_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput":
        """<p>Lists memory records in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Returns all memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            memory_strategy_id: <p>The memory strategy identifier to filter memory records by. If specified, only memory records with this strategy ID are returned.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            metadata_filters: <p>A list of metadata filter expressions to scope the returned memory records.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_memory_records_output.ListMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_memory_records.list_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_memory_records_input.ListMemoryRecordsInput = {
            "memory_id": memory_id
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if namespace_path is not None:
            input_["namespace_path"] = namespace_path
        if memory_strategy_id is not None:
            input_["memory_strategy_id"] = memory_strategy_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if metadata_filters is not None:
            input_["metadata_filters"] = metadata_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        memory_strategy_id: Optional[
            "capo_bedrock_agentcore.types.memory_strategy_id.MemoryStrategyId"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        metadata_filters: Optional[
            "capo_bedrock_agentcore.types.memory_metadata_filter_list.MemoryMetadataFilterList"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.memory_record_summary.MemoryRecordSummary]":
        _token = next_token
        while True:
            _response = self.list_memory_records(
                memory_id,
                config_overrides=config_overrides,
                namespace=namespace,
                namespace_path=namespace_path,
                memory_strategy_id=memory_strategy_id,
                max_results=max_results,
                next_token=_token,
                metadata_filters=metadata_filters,
            )
            _page = _resolve_path(_response, ("memory_record_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sessions(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.session_filter.SessionFilter"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput":
        """<p>Lists sessions in an AgentCore Memory resource based on specified criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>Empty sessions are automatically deleted after one day.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:ListSessions</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource for which to list sessions.</p>
            actor_id: <p>The identifier of the actor for which to list sessions. </p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            filter: <p>Filter criteria to apply when listing sessions.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_sessions_input.ListSessionsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_sessions_output.ListSessionsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_sessions_input.ListSessionsInput = {
            "memory_id": memory_id,
            "actor_id": actor_id,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_sessions(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        actor_id: "capo_bedrock_agentcore.types.actor_id.ActorId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        filter: Optional[
            "capo_bedrock_agentcore.types.session_filter.SessionFilter"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = self.list_sessions(
                memory_id,
                actor_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filter=filter,
            )
            _page = _resolve_path(_response, ("session_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def retrieve_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        search_criteria: "capo_bedrock_agentcore.types.search_criteria.SearchCriteria",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput":
        """<p>Searches for and retrieves memory records from an AgentCore Memory resource based on specified search criteria. We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>To use this operation, you must have the <code>bedrock-agentcore:RetrieveMemoryRecords</code> permission.</p>

        Args:
            memory_id: <p>The identifier of the AgentCore Memory resource from which to retrieve memory records.</p>
            namespace: <p>The namespace prefix to filter memory records by. Searches for memory records in namespaces that start with the provided prefix. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            namespace_path: <p>Use namespacePath for hierarchical retrievals. Return all memory records where namespace falls under the same parent hierarchy. Either <code>namespace</code> or <code>namespacePath</code> is required.</p>
            search_criteria: <p>The search criteria to use for finding relevant memory records. This includes the search query, memory strategy ID, and other search parameters.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            max_results: <p>The maximum number of results to return in a single call. The default value is 20.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.invalid_input_exception.InvalidInputException: <p>The input fails to satisfy the constraints specified by AgentCore. Check your input values and try again.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.retrieve_memory_records_output.RetrieveMemoryRecordsOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.retrieve_memory_records.retrieve_memory_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.retrieve_memory_records_input.RetrieveMemoryRecordsInput = {
            "memory_id": memory_id,
            "search_criteria": search_criteria,
        }
        if namespace is not None:
            input_["namespace"] = namespace
        if namespace_path is not None:
            input_["namespace_path"] = namespace_path
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

    def iter_retrieve_memory_records(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        search_criteria: "capo_bedrock_agentcore.types.search_criteria.SearchCriteria",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        namespace: Optional["capo_bedrock_agentcore.types.namespace.Namespace"] = None,
        namespace_path: Optional[
            "capo_bedrock_agentcore.types.namespace.Namespace"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.memory_record_summary.MemoryRecordSummary]":
        _token = next_token
        while True:
            _response = self.retrieve_memory_records(
                memory_id,
                search_criteria,
                config_overrides=config_overrides,
                namespace=namespace,
                namespace_path=namespace_path,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("memory_record_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_memory_extraction_job(
        self,
        memory_id: "capo_bedrock_agentcore.types.memory_id.MemoryId",
        extraction_job: "capo_bedrock_agentcore.types.extraction_job.ExtractionJob",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        client_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput":
        """<p> Starts a memory extraction job that processes events that failed extraction previously in an AgentCore Memory resource and produces structured memory records. When earlier extraction attempts have left events unprocessed, this job will pick up and extract those as well. </p> <p>To use this operation, you must have the <code>bedrock-agentcore:StartMemoryExtractionJob</code> permission.</p>

        Args:
            memory_id: <p>The unique identifier of the memory for which to start extraction jobs.</p>
            extraction_job: <p>Extraction job to start in this operation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotent processing of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_exception.ServiceException: <p>The service encountered an internal error. Try your request again later.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.throttled_exception.ThrottledException: <p>The request was denied due to request throttling. Reduce the frequency of requests and try again.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.start_memory_extraction_job_output.StartMemoryExtractionJobOutput"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.start_memory_extraction_job.start_memory_extraction_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.start_memory_extraction_job_input.StartMemoryExtractionJobInput = {
            "memory_id": memory_id,
            "extraction_job": extraction_job,
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

    def create_payment_instrument(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_type: "capo_bedrock_agentcore.types.payment_instrument_type.PaymentInstrumentType",
        payment_instrument_details: "capo_bedrock_agentcore.types.payment_instrument_details.PaymentInstrumentDetails",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse":
        """<p>Create a new payment instrument for a connector.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector to use for this instrument.</p>
            payment_instrument_type: <p>The type of payment instrument being created.</p>
            payment_instrument_details: <p>The details of the payment instrument.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.subscription_required_exception.SubscriptionRequiredException: <p>Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_payment_instrument_response.CreatePaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_instrument.create_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.create_payment_instrument_request.CreatePaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_type": payment_instrument_type,
            "payment_instrument_details": payment_instrument_details,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
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

    def get_payment_instrument(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse":
        """<p>Get a payment instrument by ID.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector.</p>
            payment_instrument_id: <p>The ID of the payment instrument to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_payment_instrument_response.GetPaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument.get_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_payment_instrument_request.GetPaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_instrument_id": payment_instrument_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_payment_instrument(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse":
        """<p>Deletes a payment instrument. This is a soft delete operation that preserves the record for audit and compliance purposes.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the instrument's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the instrument's paymentManagerArn.</p>
            payment_connector_id: <p>The payment connector ID. Must match the instrument's paymentConnectorId.</p>
            payment_instrument_id: <p>The payment instrument ID to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_payment_instrument_response.DeletePaymentInstrumentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_instrument.delete_payment_instrument(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_payment_instrument_request.DeletePaymentInstrumentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_id": payment_instrument_id,
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

    def list_payment_instruments(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse":
        """<p>List payment instruments for a manager.</p>

        Args:
            user_id: <p>The user ID associated with the payment instruments.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the payment instruments.</p>
            payment_connector_id: <p>The ID of the payment connector to filter by.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_payment_instruments_response.ListPaymentInstrumentsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_instruments.list_payment_instruments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_payment_instruments_request.ListPaymentInstrumentsRequest = {
            "payment_manager_arn": payment_manager_arn
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if payment_connector_id is not None:
            input_["payment_connector_id"] = payment_connector_id
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

    def iter_list_payment_instruments(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        payment_connector_id: Optional[
            "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.payment_instrument_summary.PaymentInstrumentSummary]":
        _token = next_token
        while True:
            _response = self.list_payment_instruments(
                payment_manager_arn,
                config_overrides=config_overrides,
                user_id=user_id,
                agent_name=agent_name,
                payment_connector_id=payment_connector_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("payment_instruments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_payment_instrument_balance(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_connector_id: "capo_bedrock_agentcore.types.payment_connector_id.PaymentConnectorId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        chain: "capo_bedrock_agentcore.types.blockchain_chain_id.BlockchainChainId",
        token: "capo_bedrock_agentcore.types.instrument_balance_token.InstrumentBalanceToken",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse":
        """<p>Get the balance of a payment instrument.</p>

        Args:
            user_id: <p>The user ID associated with this payment instrument.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this payment instrument.</p>
            payment_connector_id: <p>The ID of the payment connector associated with this instrument.</p>
            payment_instrument_id: <p>The ID of the payment instrument to query balance for.</p>
            chain: <p>The specific blockchain chain to query balance on. Required because balances are chain-specific.</p>
            token: <p>The token to query balance for. Only tokens supported for X402 payments are returned.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_payment_instrument_balance_response.GetPaymentInstrumentBalanceResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_instrument_balance.get_payment_instrument_balance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_payment_instrument_balance_request.GetPaymentInstrumentBalanceRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_connector_id": payment_connector_id,
            "payment_instrument_id": payment_instrument_id,
            "chain": chain,
            "token": token,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_payment_session(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        expiry_time_in_minutes: int,
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        limits: Optional[
            "capo_bedrock_agentcore.types.session_limits.SessionLimits"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse":
        """<p>Create a new payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            limits: <p>The spending limits for this payment session.</p>
            expiry_time_in_minutes: <p>The session expiry time in minutes. Must be between 15 and 480 minutes.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.subscription_required_exception.SubscriptionRequiredException: <p>Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.create_payment_session_response.CreatePaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.create_payment_session.create_payment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.create_payment_session_request.CreatePaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "expiry_time_in_minutes": expiry_time_in_minutes,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
        if limits is not None:
            input_["limits"] = limits
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

    def get_payment_session(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse":
        """<p>Get a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment session.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns this session.</p>
            payment_session_id: <p>The ID of the payment session to retrieve.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.get_payment_session_response.GetPaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.get_payment_session.get_payment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.get_payment_session_request.GetPaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_payment_session(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
    ) -> "capo_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse":
        """<p>Deletes a payment session. This permanently removes the payment session record.</p>

        Args:
            user_id: <p>The user ID making the delete request. Must match the session's userId.</p>
            payment_manager_arn: <p>The payment manager ARN. Must match the session's paymentManagerArn.</p>
            payment_session_id: <p>The payment session ID to delete.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.delete_payment_session_response.DeletePaymentSessionResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.delete_payment_session.delete_payment_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.delete_payment_session_request.DeletePaymentSessionRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
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

    def list_payment_sessions(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse":
        """<p>List payment sessions.</p>

        Args:
            user_id: <p>The user ID associated with the payment sessions.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager that owns the sessions.</p>
            next_token: <p>Token for pagination to retrieve the next set of results.</p>
            max_results: <p>Maximum number of results to return in a single response.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.list_payment_sessions_response.ListPaymentSessionsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.list_payment_sessions.list_payment_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.list_payment_sessions_request.ListPaymentSessionsRequest = {
            "payment_manager_arn": payment_manager_arn
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
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

    def iter_list_payment_sessions(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore.types.next_token.NextToken"
        ] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore.types.payment_session_summary.PaymentSessionSummary]":
        _token = next_token
        while True:
            _response = self.list_payment_sessions(
                payment_manager_arn,
                config_overrides=config_overrides,
                user_id=user_id,
                agent_name=agent_name,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("payment_sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def process_payment(
        self,
        payment_manager_arn: "capo_bedrock_agentcore.types.payment_manager_arn.PaymentManagerArn",
        payment_session_id: "capo_bedrock_agentcore.types.payment_session_id.PaymentSessionId",
        payment_instrument_id: "capo_bedrock_agentcore.types.payment_instrument_id.PaymentInstrumentId",
        payment_type: "capo_bedrock_agentcore.types.payment_type.PaymentType",
        payment_input: "capo_bedrock_agentcore.types.payment_input.PaymentInput",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        user_id: Optional["capo_bedrock_agentcore.types.user_id.UserId"] = None,
        agent_name: Optional[
            "capo_bedrock_agentcore.types.payment_agent_name.PaymentAgentName"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse":
        """<p>Processes a payment using a payment instrument within a payment session.</p>

        Args:
            user_id: <p>The user ID associated with this payment.</p>
            agent_name: <p>The agent name associated with this request, used for observability.</p>
            payment_manager_arn: <p>The ARN of the payment manager.</p>
            payment_session_id: <p>The ID of the payment session.</p>
            payment_instrument_id: <p>The ID of the payment instrument to use.</p>
            payment_type: <p>The type of payment to process.</p>
            payment_input: <p>The payment input details specific to the payment type.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.conflict_exception.ConflictException: <p>The exception that occurs when the request conflicts with the current state of the resource. This can happen when trying to modify a resource that is currently being modified by another request, or when trying to create a resource that already exists.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The exception that occurs when the request would cause a service quota to be exceeded. Review your service quotas and either reduce your request rate or request a quota increase.</p>
            capo_bedrock_agentcore.errors.subscription_required_exception.SubscriptionRequiredException: <p>Returned when you attempt a wallet operation against a Coinbase Marketplace connector whose account does not hold an active Marketplace subscription and is not within the legacy exception period. Subscribe to the Marketplace listing before you retry the operation.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.process_payment_response.ProcessPaymentResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.process_payment.process_payment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.process_payment_request.ProcessPaymentRequest = {
            "payment_manager_arn": payment_manager_arn,
            "payment_session_id": payment_session_id,
            "payment_instrument_id": payment_instrument_id,
            "payment_type": payment_type,
            "payment_input": payment_input,
        }
        if user_id is not None:
            input_["user_id"] = user_id
        if agent_name is not None:
            input_["agent_name"] = agent_name
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

    def search_registry_records(
        self,
        search_query: str,
        registry_ids: "capo_bedrock_agentcore.types.registry_id_list.RegistryIdList",
        *,
        config_overrides: Optional[BedrockAgentCoreClientConfig] = None,
        max_results: Optional[int] = None,
        filters: Optional[
            "capo_bedrock_agentcore.types.metadata_filter_expression.MetadataFilterExpression"
        ] = None,
    ) -> "capo_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse":
        """<p> Searches for registry records using semantic, lexical, or hybrid queries. Returns metadata for matching records ordered by relevance within the specified registry.</p>

        Args:
            search_query: <p> The search query to find matching registry records.</p>
            registry_ids: <p> The list of registry identifiers to search within. Currently, you can specify exactly one registry identifier. You can provide either the full Amazon Web Services Resource Name (ARN) or the 12-character alphanumeric registry ID.</p>
            max_results: <p> The maximum number of records to return in a single call. Valid values are 1 through 20. The default value is 10.</p>
            filters: <p> A metadata filter expression to narrow search results. Uses structured JSON operators including field-level operators (<code>$eq</code>, <code>$ne</code>, <code>$in</code>) and logical operators (<code>$and</code>, <code>$or</code>) on filterable fields (<code>name</code>, <code>descriptorType</code>, <code>version</code>). For example, to filter by descriptor type: <code>{"descriptorType": {"$eq": "MCP"}}</code>. To combine filters: <code>{"$and": [{"descriptorType": {"$eq": "MCP"}}, {"name": {"$eq": "my-tool"}}]}</code>.</p>

        Raises:
            capo_bedrock_agentcore.errors.access_denied_exception.AccessDeniedException: <p>The exception that occurs when you do not have sufficient permissions to perform an action. Verify that your IAM policy includes the necessary permissions for the operation you are trying to perform.</p>
            capo_bedrock_agentcore.errors.internal_server_exception.InternalServerException: <p>The exception that occurs when the service encounters an unexpected internal error. This is a temporary condition that will resolve itself with retries. We recommend implementing exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.resource_not_found_exception.ResourceNotFoundException: <p>The exception that occurs when the specified resource does not exist. This can happen when using an invalid identifier or when trying to access a resource that has been deleted.</p>
            capo_bedrock_agentcore.errors.throttling_exception.ThrottlingException: <p>The exception that occurs when the request was denied due to request throttling. This happens when you exceed the allowed request rate for an operation. Reduce the frequency of requests or implement exponential backoff retry logic in your application.</p>
            capo_bedrock_agentcore.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore.errors.validation_exception.ValidationException: <p>The exception that occurs when the input fails to satisfy the constraints specified by the service. Check the error message for details about which input parameter is invalid and correct your request.</p>
            capo_bedrock_agentcore.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore.types.search_registry_records_response.SearchRegistryRecordsResponse"
        ]:
            import capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records

            output, http_response = (
                capo_bedrock_agentcore._operations.amazon_bedrock_agent_core.search_registry_records.search_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore.types.search_registry_records_request.SearchRegistryRecordsRequest = {
            "search_query": search_query,
            "registry_ids": registry_ids,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
