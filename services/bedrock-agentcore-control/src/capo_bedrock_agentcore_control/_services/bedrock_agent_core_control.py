"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#AmazonBedrockAgentCoreControl``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_bedrock_agentcore_control._auth._signers
import capo_bedrock_agentcore_control._auth._sigv4
from capo_bedrock_agentcore_control._auth._identity import Credentials
from capo_bedrock_agentcore_control._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_bedrock_agentcore_control._auth._zapros_handler import AuthMiddleware
from capo_bedrock_agentcore_control._pagination import resolve_path as _resolve_path
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.agent_endpoint_resource import (
    AgentEndpointResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.agent_resource import (
    AgentResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.api_key_credential_provider import (
    ApiKeyCredentialProvider,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.browser_profile_resource import (
    BrowserProfileResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.browser_resource import (
    BrowserResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.capacity_provider_resource import (
    CapacityProviderResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.code_interpreter_resource import (
    CodeInterpreterResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.configuration_bundle import (
    ConfigurationBundle,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.consent_portal import (
    ConsentPortal,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.dataset import (
    Dataset,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.evaluator import (
    Evaluator,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_rate_limit_resource import (
    GatewayRateLimitResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_resource import (
    GatewayResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_rule_resource import (
    GatewayRuleResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.gateway_target_resource import (
    GatewayTargetResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.harness_endpoint_resource import (
    HarnessEndpointResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.harness_resource import (
    HarnessResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.memory_resource import (
    MemoryResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.oauth2_credential_provider import (
    Oauth2CredentialProvider,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.online_evaluation_config import (
    OnlineEvaluationConfig,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.payment_connection_resource import (
    PaymentConnectionResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.payment_credential_provider import (
    PaymentCredentialProvider,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.payment_manager_resource import (
    PaymentManagerResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_engine_resource import (
    PolicyEngineResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_generation_resource import (
    PolicyGenerationResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.policy_resource import (
    PolicyResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.registry_record_resource import (
    RegistryRecordResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.registry_resource import (
    RegistryResource,
)
from capo_bedrock_agentcore_control._resources.amazon_bedrock_agent_core_control.workload_identity import (
    WorkloadIdentity,
)
from capo_bedrock_agentcore_control._services._aws_config import aws_config
from capo_bedrock_agentcore_control._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.actions
    import capo_bedrock_agentcore_control.types.add_dataset_examples_request
    import capo_bedrock_agentcore_control.types.add_dataset_examples_response
    import capo_bedrock_agentcore_control.types.agent_endpoint_description
    import capo_bedrock_agentcore_control.types.agent_runtime
    import capo_bedrock_agentcore_control.types.agent_runtime_artifact
    import capo_bedrock_agentcore_control.types.agent_runtime_endpoint
    import capo_bedrock_agentcore_control.types.agent_runtime_id
    import capo_bedrock_agentcore_control.types.agent_runtime_name
    import capo_bedrock_agentcore_control.types.agent_runtime_version
    import capo_bedrock_agentcore_control.types.agent_runtime_version_summary
    import capo_bedrock_agentcore_control.types.api_key_credential_provider_item
    import capo_bedrock_agentcore_control.types.approval_configuration
    import capo_bedrock_agentcore_control.types.arn
    import capo_bedrock_agentcore_control.types.authorizer_configuration
    import capo_bedrock_agentcore_control.types.authorizer_type
    import capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request
    import capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response
    import capo_bedrock_agentcore_control.types.batch_put_limit_entries
    import capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn
    import capo_bedrock_agentcore_control.types.branch_name
    import capo_bedrock_agentcore_control.types.browser_enterprise_policies
    import capo_bedrock_agentcore_control.types.browser_id
    import capo_bedrock_agentcore_control.types.browser_network_configuration
    import capo_bedrock_agentcore_control.types.browser_profile_id
    import capo_bedrock_agentcore_control.types.browser_profile_name
    import capo_bedrock_agentcore_control.types.browser_profile_summary
    import capo_bedrock_agentcore_control.types.browser_signing_config_input
    import capo_bedrock_agentcore_control.types.browser_summary
    import capo_bedrock_agentcore_control.types.capacity_provider_configuration
    import capo_bedrock_agentcore_control.types.capacity_provider_id
    import capo_bedrock_agentcore_control.types.capacity_provider_name
    import capo_bedrock_agentcore_control.types.capacity_provider_summary
    import capo_bedrock_agentcore_control.types.certificate_configuration_list
    import capo_bedrock_agentcore_control.types.certificates
    import capo_bedrock_agentcore_control.types.client_token
    import capo_bedrock_agentcore_control.types.clustering_config
    import capo_bedrock_agentcore_control.types.code_interpreter_id
    import capo_bedrock_agentcore_control.types.code_interpreter_network_configuration
    import capo_bedrock_agentcore_control.types.code_interpreter_summary
    import capo_bedrock_agentcore_control.types.component_configuration_map
    import capo_bedrock_agentcore_control.types.compute_configuration
    import capo_bedrock_agentcore_control.types.conditions
    import capo_bedrock_agentcore_control.types.configuration_bundle_description
    import capo_bedrock_agentcore_control.types.configuration_bundle_id
    import capo_bedrock_agentcore_control.types.configuration_bundle_name
    import capo_bedrock_agentcore_control.types.configuration_bundle_summary
    import capo_bedrock_agentcore_control.types.configuration_bundle_version
    import capo_bedrock_agentcore_control.types.configuration_bundle_version_list
    import capo_bedrock_agentcore_control.types.configuration_bundle_version_summary
    import capo_bedrock_agentcore_control.types.consent_portal_description_type
    import capo_bedrock_agentcore_control.types.consent_portal_identifier
    import capo_bedrock_agentcore_control.types.consent_portal_idp_config
    import capo_bedrock_agentcore_control.types.consent_portal_name_type
    import capo_bedrock_agentcore_control.types.consent_portal_sources
    import capo_bedrock_agentcore_control.types.consent_portal_summary
    import capo_bedrock_agentcore_control.types.content
    import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response
    import capo_bedrock_agentcore_control.types.create_agent_runtime_request
    import capo_bedrock_agentcore_control.types.create_agent_runtime_response
    import capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response
    import capo_bedrock_agentcore_control.types.create_browser_profile_request
    import capo_bedrock_agentcore_control.types.create_browser_profile_response
    import capo_bedrock_agentcore_control.types.create_browser_request
    import capo_bedrock_agentcore_control.types.create_browser_response
    import capo_bedrock_agentcore_control.types.create_capacity_provider_input
    import capo_bedrock_agentcore_control.types.create_capacity_provider_output
    import capo_bedrock_agentcore_control.types.create_code_interpreter_request
    import capo_bedrock_agentcore_control.types.create_code_interpreter_response
    import capo_bedrock_agentcore_control.types.create_configuration_bundle_request
    import capo_bedrock_agentcore_control.types.create_configuration_bundle_response
    import capo_bedrock_agentcore_control.types.create_consent_portal_request
    import capo_bedrock_agentcore_control.types.create_consent_portal_response
    import capo_bedrock_agentcore_control.types.create_dataset_request
    import capo_bedrock_agentcore_control.types.create_dataset_response
    import capo_bedrock_agentcore_control.types.create_dataset_version_request
    import capo_bedrock_agentcore_control.types.create_dataset_version_response
    import capo_bedrock_agentcore_control.types.create_evaluator_request
    import capo_bedrock_agentcore_control.types.create_evaluator_response
    import capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response
    import capo_bedrock_agentcore_control.types.create_gateway_request
    import capo_bedrock_agentcore_control.types.create_gateway_response
    import capo_bedrock_agentcore_control.types.create_gateway_rule_request
    import capo_bedrock_agentcore_control.types.create_gateway_rule_response
    import capo_bedrock_agentcore_control.types.create_gateway_target_request
    import capo_bedrock_agentcore_control.types.create_gateway_target_response
    import capo_bedrock_agentcore_control.types.create_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.create_harness_endpoint_response
    import capo_bedrock_agentcore_control.types.create_harness_request
    import capo_bedrock_agentcore_control.types.create_harness_response
    import capo_bedrock_agentcore_control.types.create_memory_input
    import capo_bedrock_agentcore_control.types.create_memory_output
    import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response
    import capo_bedrock_agentcore_control.types.create_online_evaluation_config_request
    import capo_bedrock_agentcore_control.types.create_online_evaluation_config_response
    import capo_bedrock_agentcore_control.types.create_payment_connector_request
    import capo_bedrock_agentcore_control.types.create_payment_connector_response
    import capo_bedrock_agentcore_control.types.create_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.create_payment_credential_provider_response
    import capo_bedrock_agentcore_control.types.create_payment_manager_request
    import capo_bedrock_agentcore_control.types.create_payment_manager_response
    import capo_bedrock_agentcore_control.types.create_policy_engine_request
    import capo_bedrock_agentcore_control.types.create_policy_engine_response
    import capo_bedrock_agentcore_control.types.create_policy_request
    import capo_bedrock_agentcore_control.types.create_policy_response
    import capo_bedrock_agentcore_control.types.create_registry_record_request
    import capo_bedrock_agentcore_control.types.create_registry_record_response
    import capo_bedrock_agentcore_control.types.create_registry_request
    import capo_bedrock_agentcore_control.types.create_registry_response
    import capo_bedrock_agentcore_control.types.create_workload_identity_request
    import capo_bedrock_agentcore_control.types.create_workload_identity_response
    import capo_bedrock_agentcore_control.types.credential_provider_configurations
    import capo_bedrock_agentcore_control.types.credential_provider_name
    import capo_bedrock_agentcore_control.types.credential_provider_vendor_type
    import capo_bedrock_agentcore_control.types.credential_rotation_config
    import capo_bedrock_agentcore_control.types.credentials_provider_configurations
    import capo_bedrock_agentcore_control.types.custom_evaluator_name
    import capo_bedrock_agentcore_control.types.custom_transform_configuration
    import capo_bedrock_agentcore_control.types.data_source_config
    import capo_bedrock_agentcore_control.types.data_source_type
    import capo_bedrock_agentcore_control.types.dataset_example_list
    import capo_bedrock_agentcore_control.types.dataset_id
    import capo_bedrock_agentcore_control.types.dataset_name
    import capo_bedrock_agentcore_control.types.dataset_schema_type
    import capo_bedrock_agentcore_control.types.dataset_summary
    import capo_bedrock_agentcore_control.types.dataset_version
    import capo_bedrock_agentcore_control.types.dataset_version_summary
    import capo_bedrock_agentcore_control.types.default_api_key_type
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_request
    import capo_bedrock_agentcore_control.types.delete_agent_runtime_response
    import capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response
    import capo_bedrock_agentcore_control.types.delete_browser_profile_request
    import capo_bedrock_agentcore_control.types.delete_browser_profile_response
    import capo_bedrock_agentcore_control.types.delete_browser_request
    import capo_bedrock_agentcore_control.types.delete_browser_response
    import capo_bedrock_agentcore_control.types.delete_capacity_provider_input
    import capo_bedrock_agentcore_control.types.delete_capacity_provider_output
    import capo_bedrock_agentcore_control.types.delete_code_interpreter_request
    import capo_bedrock_agentcore_control.types.delete_code_interpreter_response
    import capo_bedrock_agentcore_control.types.delete_configuration_bundle_request
    import capo_bedrock_agentcore_control.types.delete_configuration_bundle_response
    import capo_bedrock_agentcore_control.types.delete_consent_portal_request
    import capo_bedrock_agentcore_control.types.delete_consent_portal_response
    import capo_bedrock_agentcore_control.types.delete_dataset_examples_request
    import capo_bedrock_agentcore_control.types.delete_dataset_examples_response
    import capo_bedrock_agentcore_control.types.delete_dataset_request
    import capo_bedrock_agentcore_control.types.delete_dataset_response
    import capo_bedrock_agentcore_control.types.delete_evaluator_request
    import capo_bedrock_agentcore_control.types.delete_evaluator_response
    import capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response
    import capo_bedrock_agentcore_control.types.delete_gateway_request
    import capo_bedrock_agentcore_control.types.delete_gateway_response
    import capo_bedrock_agentcore_control.types.delete_gateway_rule_request
    import capo_bedrock_agentcore_control.types.delete_gateway_rule_response
    import capo_bedrock_agentcore_control.types.delete_gateway_target_request
    import capo_bedrock_agentcore_control.types.delete_gateway_target_response
    import capo_bedrock_agentcore_control.types.delete_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.delete_harness_endpoint_response
    import capo_bedrock_agentcore_control.types.delete_harness_request
    import capo_bedrock_agentcore_control.types.delete_harness_response
    import capo_bedrock_agentcore_control.types.delete_memory_input
    import capo_bedrock_agentcore_control.types.delete_memory_output
    import capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response
    import capo_bedrock_agentcore_control.types.delete_online_evaluation_config_request
    import capo_bedrock_agentcore_control.types.delete_online_evaluation_config_response
    import capo_bedrock_agentcore_control.types.delete_payment_connector_request
    import capo_bedrock_agentcore_control.types.delete_payment_connector_response
    import capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response
    import capo_bedrock_agentcore_control.types.delete_payment_manager_request
    import capo_bedrock_agentcore_control.types.delete_payment_manager_response
    import capo_bedrock_agentcore_control.types.delete_policy_engine_request
    import capo_bedrock_agentcore_control.types.delete_policy_engine_response
    import capo_bedrock_agentcore_control.types.delete_policy_request
    import capo_bedrock_agentcore_control.types.delete_policy_response
    import capo_bedrock_agentcore_control.types.delete_registry_record_request
    import capo_bedrock_agentcore_control.types.delete_registry_record_response
    import capo_bedrock_agentcore_control.types.delete_registry_request
    import capo_bedrock_agentcore_control.types.delete_registry_response
    import capo_bedrock_agentcore_control.types.delete_resource_policy_request
    import capo_bedrock_agentcore_control.types.delete_resource_policy_response
    import capo_bedrock_agentcore_control.types.delete_workload_identity_request
    import capo_bedrock_agentcore_control.types.delete_workload_identity_response
    import capo_bedrock_agentcore_control.types.description
    import capo_bedrock_agentcore_control.types.descriptor_type
    import capo_bedrock_agentcore_control.types.descriptors
    import capo_bedrock_agentcore_control.types.dimension_keys
    import capo_bedrock_agentcore_control.types.endpoint_name
    import capo_bedrock_agentcore_control.types.enforcement_mode
    import capo_bedrock_agentcore_control.types.environment_variables_map
    import capo_bedrock_agentcore_control.types.evaluation_config_description
    import capo_bedrock_agentcore_control.types.evaluation_config_name
    import capo_bedrock_agentcore_control.types.evaluator_config
    import capo_bedrock_agentcore_control.types.evaluator_description
    import capo_bedrock_agentcore_control.types.evaluator_id
    import capo_bedrock_agentcore_control.types.evaluator_level
    import capo_bedrock_agentcore_control.types.evaluator_list
    import capo_bedrock_agentcore_control.types.evaluator_summary
    import capo_bedrock_agentcore_control.types.example_id_list
    import capo_bedrock_agentcore_control.types.exception_level
    import capo_bedrock_agentcore_control.types.execution_role_arn_type
    import capo_bedrock_agentcore_control.types.filesystem_configurations
    import capo_bedrock_agentcore_control.types.gateway_description
    import capo_bedrock_agentcore_control.types.gateway_identifier
    import capo_bedrock_agentcore_control.types.gateway_interceptor_configurations
    import capo_bedrock_agentcore_control.types.gateway_max_results
    import capo_bedrock_agentcore_control.types.gateway_name
    import capo_bedrock_agentcore_control.types.gateway_next_token
    import capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration
    import capo_bedrock_agentcore_control.types.gateway_protocol_configuration
    import capo_bedrock_agentcore_control.types.gateway_protocol_type
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_description
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_detail
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_id
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results
    import capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token
    import capo_bedrock_agentcore_control.types.gateway_rule_description
    import capo_bedrock_agentcore_control.types.gateway_rule_detail
    import capo_bedrock_agentcore_control.types.gateway_rule_id
    import capo_bedrock_agentcore_control.types.gateway_rule_max_results
    import capo_bedrock_agentcore_control.types.gateway_rule_next_token
    import capo_bedrock_agentcore_control.types.gateway_rule_priority
    import capo_bedrock_agentcore_control.types.gateway_summary
    import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response
    import capo_bedrock_agentcore_control.types.get_agent_runtime_request
    import capo_bedrock_agentcore_control.types.get_agent_runtime_response
    import capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response
    import capo_bedrock_agentcore_control.types.get_browser_profile_request
    import capo_bedrock_agentcore_control.types.get_browser_profile_response
    import capo_bedrock_agentcore_control.types.get_browser_request
    import capo_bedrock_agentcore_control.types.get_browser_response
    import capo_bedrock_agentcore_control.types.get_capacity_provider_input
    import capo_bedrock_agentcore_control.types.get_capacity_provider_output
    import capo_bedrock_agentcore_control.types.get_code_interpreter_request
    import capo_bedrock_agentcore_control.types.get_code_interpreter_response
    import capo_bedrock_agentcore_control.types.get_configuration_bundle_request
    import capo_bedrock_agentcore_control.types.get_configuration_bundle_response
    import capo_bedrock_agentcore_control.types.get_configuration_bundle_version_request
    import capo_bedrock_agentcore_control.types.get_configuration_bundle_version_response
    import capo_bedrock_agentcore_control.types.get_consent_portal_request
    import capo_bedrock_agentcore_control.types.get_consent_portal_response
    import capo_bedrock_agentcore_control.types.get_dataset_request
    import capo_bedrock_agentcore_control.types.get_dataset_response
    import capo_bedrock_agentcore_control.types.get_evaluator_request
    import capo_bedrock_agentcore_control.types.get_evaluator_response
    import capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response
    import capo_bedrock_agentcore_control.types.get_gateway_request
    import capo_bedrock_agentcore_control.types.get_gateway_response
    import capo_bedrock_agentcore_control.types.get_gateway_rule_request
    import capo_bedrock_agentcore_control.types.get_gateway_rule_response
    import capo_bedrock_agentcore_control.types.get_gateway_target_request
    import capo_bedrock_agentcore_control.types.get_gateway_target_response
    import capo_bedrock_agentcore_control.types.get_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.get_harness_endpoint_response
    import capo_bedrock_agentcore_control.types.get_harness_request
    import capo_bedrock_agentcore_control.types.get_harness_response
    import capo_bedrock_agentcore_control.types.get_memory_input
    import capo_bedrock_agentcore_control.types.get_memory_output
    import capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response
    import capo_bedrock_agentcore_control.types.get_online_evaluation_config_request
    import capo_bedrock_agentcore_control.types.get_online_evaluation_config_response
    import capo_bedrock_agentcore_control.types.get_payment_connector_request
    import capo_bedrock_agentcore_control.types.get_payment_connector_response
    import capo_bedrock_agentcore_control.types.get_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.get_payment_credential_provider_response
    import capo_bedrock_agentcore_control.types.get_payment_manager_request
    import capo_bedrock_agentcore_control.types.get_payment_manager_response
    import capo_bedrock_agentcore_control.types.get_policy_engine_request
    import capo_bedrock_agentcore_control.types.get_policy_engine_response
    import capo_bedrock_agentcore_control.types.get_policy_engine_summary_request
    import capo_bedrock_agentcore_control.types.get_policy_engine_summary_response
    import capo_bedrock_agentcore_control.types.get_policy_generation_request
    import capo_bedrock_agentcore_control.types.get_policy_generation_response
    import capo_bedrock_agentcore_control.types.get_policy_generation_summary_request
    import capo_bedrock_agentcore_control.types.get_policy_generation_summary_response
    import capo_bedrock_agentcore_control.types.get_policy_request
    import capo_bedrock_agentcore_control.types.get_policy_response
    import capo_bedrock_agentcore_control.types.get_policy_summary_request
    import capo_bedrock_agentcore_control.types.get_policy_summary_response
    import capo_bedrock_agentcore_control.types.get_registry_record_request
    import capo_bedrock_agentcore_control.types.get_registry_record_response
    import capo_bedrock_agentcore_control.types.get_registry_request
    import capo_bedrock_agentcore_control.types.get_registry_response
    import capo_bedrock_agentcore_control.types.get_resource_policy_request
    import capo_bedrock_agentcore_control.types.get_resource_policy_response
    import capo_bedrock_agentcore_control.types.get_token_vault_request
    import capo_bedrock_agentcore_control.types.get_token_vault_response
    import capo_bedrock_agentcore_control.types.get_workload_identity_request
    import capo_bedrock_agentcore_control.types.get_workload_identity_response
    import capo_bedrock_agentcore_control.types.harness_allowed_tools
    import capo_bedrock_agentcore_control.types.harness_endpoint
    import capo_bedrock_agentcore_control.types.harness_endpoint_description
    import capo_bedrock_agentcore_control.types.harness_endpoint_name
    import capo_bedrock_agentcore_control.types.harness_environment_artifact
    import capo_bedrock_agentcore_control.types.harness_environment_provider_request
    import capo_bedrock_agentcore_control.types.harness_hooks
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_memory_configuration
    import capo_bedrock_agentcore_control.types.harness_model_configuration
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_skills
    import capo_bedrock_agentcore_control.types.harness_summary
    import capo_bedrock_agentcore_control.types.harness_system_prompt
    import capo_bedrock_agentcore_control.types.harness_tools
    import capo_bedrock_agentcore_control.types.harness_truncation_configuration
    import capo_bedrock_agentcore_control.types.harness_version
    import capo_bedrock_agentcore_control.types.harness_version_summary
    import capo_bedrock_agentcore_control.types.included_data
    import capo_bedrock_agentcore_control.types.indexed_keys_list
    import capo_bedrock_agentcore_control.types.insight_list
    import capo_bedrock_agentcore_control.types.kms_configuration
    import capo_bedrock_agentcore_control.types.kms_key_arn
    import capo_bedrock_agentcore_control.types.lifecycle_configuration
    import capo_bedrock_agentcore_control.types.limit_entries
    import capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request
    import capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response
    import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_by_capacity_provider_input
    import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_by_capacity_provider_output
    import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request
    import capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response
    import capo_bedrock_agentcore_control.types.list_agent_runtimes_request
    import capo_bedrock_agentcore_control.types.list_agent_runtimes_response
    import capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request
    import capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response
    import capo_bedrock_agentcore_control.types.list_browser_profiles_request
    import capo_bedrock_agentcore_control.types.list_browser_profiles_response
    import capo_bedrock_agentcore_control.types.list_browsers_request
    import capo_bedrock_agentcore_control.types.list_browsers_response
    import capo_bedrock_agentcore_control.types.list_capacity_providers_input
    import capo_bedrock_agentcore_control.types.list_capacity_providers_output
    import capo_bedrock_agentcore_control.types.list_code_interpreters_request
    import capo_bedrock_agentcore_control.types.list_code_interpreters_response
    import capo_bedrock_agentcore_control.types.list_configuration_bundle_versions_request
    import capo_bedrock_agentcore_control.types.list_configuration_bundle_versions_response
    import capo_bedrock_agentcore_control.types.list_configuration_bundles_request
    import capo_bedrock_agentcore_control.types.list_configuration_bundles_response
    import capo_bedrock_agentcore_control.types.list_consent_portals_request
    import capo_bedrock_agentcore_control.types.list_consent_portals_response
    import capo_bedrock_agentcore_control.types.list_dataset_examples_request
    import capo_bedrock_agentcore_control.types.list_dataset_examples_response
    import capo_bedrock_agentcore_control.types.list_dataset_versions_request
    import capo_bedrock_agentcore_control.types.list_dataset_versions_response
    import capo_bedrock_agentcore_control.types.list_datasets_request
    import capo_bedrock_agentcore_control.types.list_datasets_response
    import capo_bedrock_agentcore_control.types.list_evaluators_request
    import capo_bedrock_agentcore_control.types.list_evaluators_response
    import capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request
    import capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response
    import capo_bedrock_agentcore_control.types.list_gateway_rules_request
    import capo_bedrock_agentcore_control.types.list_gateway_rules_response
    import capo_bedrock_agentcore_control.types.list_gateway_targets_request
    import capo_bedrock_agentcore_control.types.list_gateway_targets_response
    import capo_bedrock_agentcore_control.types.list_gateways_request
    import capo_bedrock_agentcore_control.types.list_gateways_response
    import capo_bedrock_agentcore_control.types.list_harness_endpoints_request
    import capo_bedrock_agentcore_control.types.list_harness_endpoints_response
    import capo_bedrock_agentcore_control.types.list_harness_versions_request
    import capo_bedrock_agentcore_control.types.list_harness_versions_response
    import capo_bedrock_agentcore_control.types.list_harnesses_request
    import capo_bedrock_agentcore_control.types.list_harnesses_response
    import capo_bedrock_agentcore_control.types.list_memories_input
    import capo_bedrock_agentcore_control.types.list_memories_output
    import capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request
    import capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response
    import capo_bedrock_agentcore_control.types.list_online_evaluation_configs_request
    import capo_bedrock_agentcore_control.types.list_online_evaluation_configs_response
    import capo_bedrock_agentcore_control.types.list_payment_connectors_request
    import capo_bedrock_agentcore_control.types.list_payment_connectors_response
    import capo_bedrock_agentcore_control.types.list_payment_credential_providers_request
    import capo_bedrock_agentcore_control.types.list_payment_credential_providers_response
    import capo_bedrock_agentcore_control.types.list_payment_managers_request
    import capo_bedrock_agentcore_control.types.list_payment_managers_response
    import capo_bedrock_agentcore_control.types.list_policies_request
    import capo_bedrock_agentcore_control.types.list_policies_response
    import capo_bedrock_agentcore_control.types.list_policy_engine_summaries_request
    import capo_bedrock_agentcore_control.types.list_policy_engine_summaries_response
    import capo_bedrock_agentcore_control.types.list_policy_engines_request
    import capo_bedrock_agentcore_control.types.list_policy_engines_response
    import capo_bedrock_agentcore_control.types.list_policy_generation_assets_request
    import capo_bedrock_agentcore_control.types.list_policy_generation_assets_response
    import capo_bedrock_agentcore_control.types.list_policy_generation_summaries_request
    import capo_bedrock_agentcore_control.types.list_policy_generation_summaries_response
    import capo_bedrock_agentcore_control.types.list_policy_generations_request
    import capo_bedrock_agentcore_control.types.list_policy_generations_response
    import capo_bedrock_agentcore_control.types.list_policy_summaries_request
    import capo_bedrock_agentcore_control.types.list_policy_summaries_response
    import capo_bedrock_agentcore_control.types.list_registries_request
    import capo_bedrock_agentcore_control.types.list_registries_response
    import capo_bedrock_agentcore_control.types.list_registry_records_request
    import capo_bedrock_agentcore_control.types.list_registry_records_response
    import capo_bedrock_agentcore_control.types.list_tags_for_resource_request
    import capo_bedrock_agentcore_control.types.list_tags_for_resource_response
    import capo_bedrock_agentcore_control.types.list_workload_identities_request
    import capo_bedrock_agentcore_control.types.list_workload_identities_response
    import capo_bedrock_agentcore_control.types.max_results
    import capo_bedrock_agentcore_control.types.memory_id
    import capo_bedrock_agentcore_control.types.memory_strategy_input_list
    import capo_bedrock_agentcore_control.types.memory_summary
    import capo_bedrock_agentcore_control.types.memory_view
    import capo_bedrock_agentcore_control.types.metadata_configuration
    import capo_bedrock_agentcore_control.types.modify_memory_strategies
    import capo_bedrock_agentcore_control.types.name
    import capo_bedrock_agentcore_control.types.namespace_keys_list
    import capo_bedrock_agentcore_control.types.network_configuration
    import capo_bedrock_agentcore_control.types.next_token
    import capo_bedrock_agentcore_control.types.non_empty_string
    import capo_bedrock_agentcore_control.types.oauth2_credential_provider_item
    import capo_bedrock_agentcore_control.types.oauth2_provider_config_input
    import capo_bedrock_agentcore_control.types.online_evaluation_config_id
    import capo_bedrock_agentcore_control.types.online_evaluation_config_summary
    import capo_bedrock_agentcore_control.types.online_evaluation_execution_status
    import capo_bedrock_agentcore_control.types.output_config
    import capo_bedrock_agentcore_control.types.payment_connector_id
    import capo_bedrock_agentcore_control.types.payment_connector_name
    import capo_bedrock_agentcore_control.types.payment_connector_provision_mode
    import capo_bedrock_agentcore_control.types.payment_connector_summary
    import capo_bedrock_agentcore_control.types.payment_connector_type
    import capo_bedrock_agentcore_control.types.payment_credential_provider_item
    import capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type
    import capo_bedrock_agentcore_control.types.payment_manager_id
    import capo_bedrock_agentcore_control.types.payment_manager_name
    import capo_bedrock_agentcore_control.types.payment_manager_summary
    import capo_bedrock_agentcore_control.types.payment_provider_configuration_input
    import capo_bedrock_agentcore_control.types.payments_authorizer_type
    import capo_bedrock_agentcore_control.types.payments_description
    import capo_bedrock_agentcore_control.types.permissions_configuration
    import capo_bedrock_agentcore_control.types.platform_version
    import capo_bedrock_agentcore_control.types.policy
    import capo_bedrock_agentcore_control.types.policy_definition
    import capo_bedrock_agentcore_control.types.policy_engine
    import capo_bedrock_agentcore_control.types.policy_engine_name
    import capo_bedrock_agentcore_control.types.policy_engine_summary
    import capo_bedrock_agentcore_control.types.policy_generation
    import capo_bedrock_agentcore_control.types.policy_generation_asset
    import capo_bedrock_agentcore_control.types.policy_generation_name
    import capo_bedrock_agentcore_control.types.policy_generation_summary
    import capo_bedrock_agentcore_control.types.policy_name
    import capo_bedrock_agentcore_control.types.policy_summary
    import capo_bedrock_agentcore_control.types.policy_validation_mode
    import capo_bedrock_agentcore_control.types.private_endpoint
    import capo_bedrock_agentcore_control.types.protocol_configuration
    import capo_bedrock_agentcore_control.types.put_resource_policy_request
    import capo_bedrock_agentcore_control.types.put_resource_policy_response
    import capo_bedrock_agentcore_control.types.record_identifier
    import capo_bedrock_agentcore_control.types.recording_config
    import capo_bedrock_agentcore_control.types.registry_authorizer_type
    import capo_bedrock_agentcore_control.types.registry_identifier
    import capo_bedrock_agentcore_control.types.registry_name
    import capo_bedrock_agentcore_control.types.registry_record_name
    import capo_bedrock_agentcore_control.types.registry_record_status
    import capo_bedrock_agentcore_control.types.registry_record_summary
    import capo_bedrock_agentcore_control.types.registry_record_version
    import capo_bedrock_agentcore_control.types.registry_status
    import capo_bedrock_agentcore_control.types.registry_summary
    import capo_bedrock_agentcore_control.types.request_header_configuration
    import capo_bedrock_agentcore_control.types.resource
    import capo_bedrock_agentcore_control.types.resource_id
    import capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type
    import capo_bedrock_agentcore_control.types.resource_policy_body
    import capo_bedrock_agentcore_control.types.resource_type
    import capo_bedrock_agentcore_control.types.role_arn
    import capo_bedrock_agentcore_control.types.rotate_payment_connector_credentials_request
    import capo_bedrock_agentcore_control.types.rotate_payment_connector_credentials_response
    import capo_bedrock_agentcore_control.types.rule
    import capo_bedrock_agentcore_control.types.runtime_metadata_configuration
    import capo_bedrock_agentcore_control.types.sandbox_name
    import capo_bedrock_agentcore_control.types.secret_reference
    import capo_bedrock_agentcore_control.types.secret_source_type
    import capo_bedrock_agentcore_control.types.sensitive_json
    import capo_bedrock_agentcore_control.types.set_token_vault_cmk_request
    import capo_bedrock_agentcore_control.types.set_token_vault_cmk_response
    import capo_bedrock_agentcore_control.types.start_policy_generation_request
    import capo_bedrock_agentcore_control.types.start_policy_generation_response
    import capo_bedrock_agentcore_control.types.stream_delivery_resources
    import capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request
    import capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response
    import capo_bedrock_agentcore_control.types.synchronization_configuration
    import capo_bedrock_agentcore_control.types.synchronization_type
    import capo_bedrock_agentcore_control.types.synchronize_gateway_targets_request
    import capo_bedrock_agentcore_control.types.synchronize_gateway_targets_response
    import capo_bedrock_agentcore_control.types.tag_key_list
    import capo_bedrock_agentcore_control.types.tag_resource_request
    import capo_bedrock_agentcore_control.types.tag_resource_response
    import capo_bedrock_agentcore_control.types.taggable_resources_arn
    import capo_bedrock_agentcore_control.types.tags_map
    import capo_bedrock_agentcore_control.types.target_configuration
    import capo_bedrock_agentcore_control.types.target_description
    import capo_bedrock_agentcore_control.types.target_id
    import capo_bedrock_agentcore_control.types.target_id_list
    import capo_bedrock_agentcore_control.types.target_max_results
    import capo_bedrock_agentcore_control.types.target_name
    import capo_bedrock_agentcore_control.types.target_next_token
    import capo_bedrock_agentcore_control.types.target_summary
    import capo_bedrock_agentcore_control.types.token_vault_id_type
    import capo_bedrock_agentcore_control.types.tools_file_system_configurations
    import capo_bedrock_agentcore_control.types.untag_resource_request
    import capo_bedrock_agentcore_control.types.untag_resource_response
    import capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request
    import capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response
    import capo_bedrock_agentcore_control.types.update_agent_runtime_request
    import capo_bedrock_agentcore_control.types.update_agent_runtime_response
    import capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request
    import capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response
    import capo_bedrock_agentcore_control.types.update_capacity_provider_input
    import capo_bedrock_agentcore_control.types.update_capacity_provider_output
    import capo_bedrock_agentcore_control.types.update_configuration_bundle_request
    import capo_bedrock_agentcore_control.types.update_configuration_bundle_response
    import capo_bedrock_agentcore_control.types.update_consent_portal_request
    import capo_bedrock_agentcore_control.types.update_consent_portal_response
    import capo_bedrock_agentcore_control.types.update_dataset_examples_request
    import capo_bedrock_agentcore_control.types.update_dataset_examples_response
    import capo_bedrock_agentcore_control.types.update_dataset_request
    import capo_bedrock_agentcore_control.types.update_dataset_response
    import capo_bedrock_agentcore_control.types.update_evaluator_request
    import capo_bedrock_agentcore_control.types.update_evaluator_response
    import capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request
    import capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response
    import capo_bedrock_agentcore_control.types.update_gateway_request
    import capo_bedrock_agentcore_control.types.update_gateway_response
    import capo_bedrock_agentcore_control.types.update_gateway_rule_request
    import capo_bedrock_agentcore_control.types.update_gateway_rule_response
    import capo_bedrock_agentcore_control.types.update_gateway_target_request
    import capo_bedrock_agentcore_control.types.update_gateway_target_response
    import capo_bedrock_agentcore_control.types.update_harness_endpoint_request
    import capo_bedrock_agentcore_control.types.update_harness_endpoint_response
    import capo_bedrock_agentcore_control.types.update_harness_request
    import capo_bedrock_agentcore_control.types.update_harness_response
    import capo_bedrock_agentcore_control.types.update_memory_input
    import capo_bedrock_agentcore_control.types.update_memory_output
    import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request
    import capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response
    import capo_bedrock_agentcore_control.types.update_online_evaluation_config_request
    import capo_bedrock_agentcore_control.types.update_online_evaluation_config_response
    import capo_bedrock_agentcore_control.types.update_payment_connector_request
    import capo_bedrock_agentcore_control.types.update_payment_connector_response
    import capo_bedrock_agentcore_control.types.update_payment_credential_provider_request
    import capo_bedrock_agentcore_control.types.update_payment_credential_provider_response
    import capo_bedrock_agentcore_control.types.update_payment_manager_request
    import capo_bedrock_agentcore_control.types.update_payment_manager_response
    import capo_bedrock_agentcore_control.types.update_policy_engine_request
    import capo_bedrock_agentcore_control.types.update_policy_engine_response
    import capo_bedrock_agentcore_control.types.update_policy_request
    import capo_bedrock_agentcore_control.types.update_policy_response
    import capo_bedrock_agentcore_control.types.update_registry_record_request
    import capo_bedrock_agentcore_control.types.update_registry_record_response
    import capo_bedrock_agentcore_control.types.update_registry_record_status_request
    import capo_bedrock_agentcore_control.types.update_registry_record_status_response
    import capo_bedrock_agentcore_control.types.update_registry_request
    import capo_bedrock_agentcore_control.types.update_registry_response
    import capo_bedrock_agentcore_control.types.update_workload_identity_request
    import capo_bedrock_agentcore_control.types.update_workload_identity_response
    import capo_bedrock_agentcore_control.types.updated_approval_configuration
    import capo_bedrock_agentcore_control.types.updated_authorizer_configuration
    import capo_bedrock_agentcore_control.types.updated_description
    import capo_bedrock_agentcore_control.types.updated_descriptors
    import capo_bedrock_agentcore_control.types.updated_harness_environment_artifact
    import capo_bedrock_agentcore_control.types.updated_harness_memory_configuration
    import capo_bedrock_agentcore_control.types.updated_synchronization_configuration
    import capo_bedrock_agentcore_control.types.updated_synchronization_type
    import capo_bedrock_agentcore_control.types.version_created_by_source
    import capo_bedrock_agentcore_control.types.version_filter
    import capo_bedrock_agentcore_control.types.waf_configuration
    import capo_bedrock_agentcore_control.types.workload_identity_name_type
    import capo_bedrock_agentcore_control.types.workload_identity_type


class BedrockAgentCoreControlClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class BedrockAgentCoreControlClient:
    """A client for the ``BedrockAgentCoreControl`` service.

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
        self._config = BedrockAgentCoreControlClientConfig(
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
        self.agent_endpoint_resource = AgentEndpointResource(self)
        self.agent_resource = AgentResource(self)
        self.api_key_credential_provider = ApiKeyCredentialProvider(self)
        self.browser_profile_resource = BrowserProfileResource(self)
        self.browser_resource = BrowserResource(self)
        self.capacity_provider_resource = CapacityProviderResource(self)
        self.code_interpreter_resource = CodeInterpreterResource(self)
        self.configuration_bundle = ConfigurationBundle(self)
        self.consent_portal = ConsentPortal(self)
        self.dataset = Dataset(self)
        self.evaluator = Evaluator(self)
        self.gateway_rate_limit_resource = GatewayRateLimitResource(self)
        self.gateway_resource = GatewayResource(self)
        self.gateway_rule_resource = GatewayRuleResource(self)
        self.gateway_target_resource = GatewayTargetResource(self)
        self.harness_endpoint_resource = HarnessEndpointResource(self)
        self.harness_resource = HarnessResource(self)
        self.memory_resource = MemoryResource(self)
        self.oauth2_credential_provider = Oauth2CredentialProvider(self)
        self.online_evaluation_config = OnlineEvaluationConfig(self)
        self.payment_connection_resource = PaymentConnectionResource(self)
        self.payment_credential_provider = PaymentCredentialProvider(self)
        self.payment_manager_resource = PaymentManagerResource(self)
        self.policy_engine_resource = PolicyEngineResource(self)
        self.policy_generation_resource = PolicyGenerationResource(self)
        self.policy_resource = PolicyResource(self)
        self.registry_record_resource = RegistryRecordResource(self)
        self.registry_resource = RegistryResource(self)
        self.workload_identity = WorkloadIdentity(self)

    def operation_options(
        self, config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: BedrockAgentCoreControlClientConfig = config_overrides or {}
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

    def delete_resource_policy(
        self,
        resource_arn: "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes the resource-based policy for a specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to delete the resource policy.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_resource_policy

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_resource_policy(
        self,
        resource_arn: "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Retrieves the resource-based policy for a specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to retrieve the resource policy.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_resource_policy

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_resource_policy.get_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_token_vault(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        token_vault_id: Optional[
            "capo_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_token_vault_response.GetTokenVaultResponse":
        """<p>Retrieves information about a token vault.</p>

        Args:
            token_vault_id: <p>The unique identifier of the token vault to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_token_vault_request.GetTokenVaultRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_token_vault_response.GetTokenVaultResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_token_vault

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_token_vault.get_token_vault(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_token_vault_request.GetTokenVaultRequest = {}
        if token_vault_id is not None:
            input_["token_vault_id"] = token_vault_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags associated with the specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which you want to list tags.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_tags_for_resource

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        resource_arn: "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn",
        policy: "capo_bedrock_agentcore_control.types.resource_policy_body.ResourcePolicyBody",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates a resource-based policy for a resource with the specified resourceArn.</p> <note> <p>This feature is currently available only for AgentCore Runtime and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource for which to create or update the resource policy.</p>
            policy: <p>The resource policy to create or update.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.put_resource_policy

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_token_vault_cmk(
        self,
        kms_configuration: "capo_bedrock_agentcore_control.types.kms_configuration.KmsConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        token_vault_id: Optional[
            "capo_bedrock_agentcore_control.types.token_vault_id_type.TokenVaultIdType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.set_token_vault_cmk_response.SetTokenVaultCMKResponse":
        """<p>Sets the customer master key (CMK) for a token vault.</p>

        Args:
            token_vault_id: <p>The unique identifier of the token vault to update.</p>
            kms_configuration: <p>The KMS configuration for the token vault, including the key type and KMS key ARN.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.concurrent_modification_exception.ConcurrentModificationException: <p>Exception thrown when a resource is modified concurrently by multiple requests.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.set_token_vault_cmk_request.SetTokenVaultCMKRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.set_token_vault_cmk_response.SetTokenVaultCMKResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.set_token_vault_cmk

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.set_token_vault_cmk.set_token_vault_cmk(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.set_token_vault_cmk_request.SetTokenVaultCMKRequest = {
            "kms_configuration": kms_configuration
        }
        if token_vault_id is not None:
            input_["token_vault_id"] = token_vault_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "capo_bedrock_agentcore_control.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> (
        "capo_bedrock_agentcore_control.types.tag_resource_response.TagResourceResponse"
    ):
        """<p>Associates the specified tags to a resource with the specified resourceArn. If existing tags on a resource are not specified in the request parameters, they are not changed. When a resource is deleted, the tags associated with that resource are also deleted.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to tag.</p>
            tags: <p>The tags to add to the resource. A tag is a key-value pair.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.tag_resource

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_bedrock_agentcore_control.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "capo_bedrock_agentcore_control.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes the specified tags from the specified resource.</p> <note> <p>This feature is currently available only for AgentCore Runtime, Browser, Browser Profile, Code Interpreter tool, and Gateway.</p> </note>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource that you want to untag.</p>
            tag_keys: <p>The tag keys of the tags to remove from the resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.untag_resource

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.untag_resource_request.UntagResourceRequest = {
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

    def create_agent_runtime_endpoint(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse":
        """<p>Creates an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to create an endpoint for.</p>
            name: <p>The name of the AgentCore Runtime endpoint.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to use for the endpoint.</p>
            description: <p>The description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime endpoint. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_response.CreateAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime_endpoint.create_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_agent_runtime_endpoint_request.CreateAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "name": name,
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input_["description"] = description
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

    def get_agent_runtime_endpoint(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse":
        """<p>Gets information about an Amazon Secure AgentEndpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_response.GetAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime_endpoint.get_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_agent_runtime_endpoint_request.GetAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_agent_runtime_endpoint(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse":
        """<p>Updates an existing Amazon Bedrock AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to update.</p>
            agent_runtime_version: <p>The updated version of the AgentCore Runtime for the endpoint.</p>
            description: <p>The updated description of the AgentCore Runtime endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_response.UpdateAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime_endpoint.update_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_agent_runtime_endpoint_request.UpdateAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
        if description is not None:
            input_["description"] = description
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

    def delete_agent_runtime_endpoint(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        endpoint_name: "capo_bedrock_agentcore_control.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse":
        """<p>Deletes an AgentCore Runtime endpoint.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime associated with the endpoint.</p>
            endpoint_name: <p>The name of the AgentCore Runtime endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_response.DeleteAgentRuntimeEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime_endpoint.delete_agent_runtime_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_agent_runtime_endpoint_request.DeleteAgentRuntimeEndpointRequest = {
            "agent_runtime_id": agent_runtime_id,
            "endpoint_name": endpoint_name,
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

    def list_agent_runtime_endpoints(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse":
        """<p>Lists all endpoints for a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list endpoints for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_response.ListAgentRuntimeEndpointsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_endpoints.list_agent_runtime_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_agent_runtime_endpoints_request.ListAgentRuntimeEndpointsRequest = {
            "agent_runtime_id": agent_runtime_id
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

    def iter_list_agent_runtime_endpoints(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.agent_runtime_endpoint.AgentRuntimeEndpoint]":
        _token = next_token
        while True:
            _response = self.list_agent_runtime_endpoints(
                agent_runtime_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("runtime_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_agent_runtime(
        self,
        agent_runtime_name: "capo_bedrock_agentcore_control.types.agent_runtime_name.AgentRuntimeName",
        agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        network_configuration: Optional[
            "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        request_header_configuration: Optional[
            "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
        ] = None,
        lifecycle_configuration: Optional[
            "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
        ] = None,
        capacity_provider_configuration: Optional[
            "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
        platform_version: Optional[
            "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse":
        """<p>Creates an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_name: <p>The name of the AgentCore Runtime.</p>
            agent_runtime_artifact: <p>The artifact of the AgentCore Runtime.</p>
            role_arn: <p>The IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The network configuration for the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            description: <p>The description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>Configuration for HTTP request headers that will be passed through to the runtime.</p>
            lifecycle_configuration: <p>The life cycle configuration for the AgentCore Runtime.</p>
            environment_variables: <p>Environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The filesystem configurations to mount into the AgentCore Runtime. Use filesystem configurations to provide persistent storage to your AgentCore Runtime sessions.</p>
            capacity_provider_configuration: <p>The capacity provider configuration for the AgentCore Runtime. Use a capacity provider to run the AgentCore Runtime on the Instances compute type, which provisions Amazon Web Services managed compute in your account.</p>
            tags: <p>A map of tag keys and values to assign to the agent runtime. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>
            platform_version: <p>The version of the runtime platform to use for the AgentCore Runtime.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_agent_runtime_response.CreateAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_agent_runtime.create_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_agent_runtime_request.CreateAgentRuntimeRequest = {
            "agent_runtime_name": agent_runtime_name,
            "agent_runtime_artifact": agent_runtime_artifact,
            "role_arn": role_arn,
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input_["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input_["lifecycle_configuration"] = lifecycle_configuration
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
        if capacity_provider_configuration is not None:
            input_["capacity_provider_configuration"] = capacity_provider_configuration
        if tags is not None:
            input_["tags"] = tags
        if platform_version is not None:
            input_["platform_version"] = platform_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_agent_runtime(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse":
        """<p>Gets an Amazon Bedrock AgentCore Runtime.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to retrieve.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_agent_runtime_response.GetAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_agent_runtime.get_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_agent_runtime_request.GetAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_agent_runtime(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        agent_runtime_artifact: "capo_bedrock_agentcore_control.types.agent_runtime_artifact.AgentRuntimeArtifact",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        network_configuration: Optional[
            "capo_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        request_header_configuration: Optional[
            "capo_bedrock_agentcore_control.types.request_header_configuration.RequestHeaderConfiguration"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.protocol_configuration.ProtocolConfiguration"
        ] = None,
        lifecycle_configuration: Optional[
            "capo_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
        ] = None,
        metadata_configuration: Optional[
            "capo_bedrock_agentcore_control.types.runtime_metadata_configuration.RuntimeMetadataConfiguration"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
        ] = None,
        capacity_provider_configuration: Optional[
            "capo_bedrock_agentcore_control.types.capacity_provider_configuration.CapacityProviderConfiguration"
        ] = None,
        platform_version: Optional[
            "capo_bedrock_agentcore_control.types.platform_version.PlatformVersion"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse":
        """<p>Updates an existing Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to update.</p>
            agent_runtime_artifact: <p>The updated artifact of the AgentCore Runtime.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the AgentCore Runtime.</p>
            network_configuration: <p>The updated network configuration for the AgentCore Runtime.</p>
            description: <p>The updated description of the AgentCore Runtime.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the AgentCore Runtime.</p>
            request_header_configuration: <p>The updated configuration for HTTP request headers that will be passed through to the runtime.</p>
            lifecycle_configuration: <p>The updated life cycle configuration for the AgentCore Runtime.</p>
            metadata_configuration: <p>The updated configuration for microVM Metadata Service (MMDS) settings for the AgentCore Runtime.</p>
            environment_variables: <p>Updated environment variables to set in the AgentCore Runtime environment.</p>
            filesystem_configurations: <p>The updated filesystem configurations to mount into the AgentCore Runtime.</p>
            capacity_provider_configuration: <p>The updated capacity provider configuration for the AgentCore Runtime.</p>
            platform_version: <p>The updated version of the runtime platform to use for the AgentCore Runtime.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_agent_runtime_response.UpdateAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_agent_runtime.update_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_agent_runtime_request.UpdateAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id,
            "agent_runtime_artifact": agent_runtime_artifact,
            "role_arn": role_arn,
        }
        if network_configuration is not None:
            input_["network_configuration"] = network_configuration
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if request_header_configuration is not None:
            input_["request_header_configuration"] = request_header_configuration
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if lifecycle_configuration is not None:
            input_["lifecycle_configuration"] = lifecycle_configuration
        if metadata_configuration is not None:
            input_["metadata_configuration"] = metadata_configuration
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
        if capacity_provider_configuration is not None:
            input_["capacity_provider_configuration"] = capacity_provider_configuration
        if platform_version is not None:
            input_["platform_version"] = platform_version
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

    def delete_agent_runtime(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        agent_runtime_version: Optional[
            "capo_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse":
        """<p>Deletes an Amazon Bedrock AgentCore Runtime, or a single version of an AgentCore Runtime when you provide the version qualifier.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to delete.</p>
            agent_runtime_version: <p>The version of the AgentCore Runtime to delete. When you provide this value, only that version is deleted. When you omit it, the entire AgentCore Runtime and all of its versions are deleted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, the service ignores the request but does not return an error.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_agent_runtime_response.DeleteAgentRuntimeResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_agent_runtime.delete_agent_runtime(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_agent_runtime_request.DeleteAgentRuntimeRequest = {
            "agent_runtime_id": agent_runtime_id
        }
        if agent_runtime_version is not None:
            input_["agent_runtime_version"] = agent_runtime_version
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

    def list_agent_runtimes(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse":
        """<p>Lists all Amazon Secure Agents in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtimes_response.ListAgentRuntimesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtimes.list_agent_runtimes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_agent_runtimes_request.ListAgentRuntimesRequest = {}
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

    def iter_list_agent_runtimes(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.agent_runtime.AgentRuntime]":
        _token = next_token
        while True:
            _response = self.list_agent_runtimes(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_runtimes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_agent_runtime_versions(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse":
        """<p>Lists all versions of a specific Amazon Secure Agent.</p>

        Args:
            agent_runtime_id: <p>The unique identifier of the AgentCore Runtime to list versions for.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_response.ListAgentRuntimeVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions.list_agent_runtime_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_agent_runtime_versions_request.ListAgentRuntimeVersionsRequest = {
            "agent_runtime_id": agent_runtime_id
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

    def iter_list_agent_runtime_versions(
        self,
        agent_runtime_id: "capo_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.agent_runtime.AgentRuntime]":
        _token = next_token
        while True:
            _response = self.list_agent_runtime_versions(
                agent_runtime_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_runtimes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_api_key_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "capo_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse":
        """<p>Creates a new API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider. The name must be unique within your account.</p>
            api_key: <p>The API key to use for authentication. This value is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>
            tags: <p>A map of tag keys and values to assign to the API key credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Exception thrown when a resource limit is exceeded.</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_api_key_credential_provider_response.CreateApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_api_key_credential_provider.create_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_api_key_credential_provider_request.CreateApiKeyCredentialProviderRequest = {
            "name": name
        }
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_api_key_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse":
        """<p>Retrieves information about an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_api_key_credential_provider_response.GetApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_api_key_credential_provider.get_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_api_key_credential_provider_request.GetApiKeyCredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_api_key_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        api_key: Optional[
            "capo_bedrock_agentcore_control.types.default_api_key_type.DefaultApiKeyType"
        ] = None,
        api_key_secret_config: Optional[
            "capo_bedrock_agentcore_control.types.secret_reference.SecretReference"
        ] = None,
        api_key_secret_source: Optional[
            "capo_bedrock_agentcore_control.types.secret_source_type.SecretSourceType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse":
        """<p>Updates an existing API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to update.</p>
            api_key: <p>The new API key to use for authentication. This value replaces the existing API key and is encrypted and stored securely.</p>
            api_key_secret_config: <p>A reference to the Amazon Web Services Secrets Manager secret that stores the API key. This includes the secret ID and the JSON key used to extract the API key value from the secret. Required when <code>apiKeySecretSource</code> is set to <code>EXTERNAL</code>.</p>
            api_key_secret_source: <p>The source type of the API key secret. Use <code>MANAGED</code> if the secret is managed by the service, or <code>EXTERNAL</code> if you manage the secret yourself in Amazon Web Services Secrets Manager.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_api_key_credential_provider_response.UpdateApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_api_key_credential_provider.update_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_api_key_credential_provider_request.UpdateApiKeyCredentialProviderRequest = {
            "name": name
        }
        if api_key is not None:
            input_["api_key"] = api_key
        if api_key_secret_config is not None:
            input_["api_key_secret_config"] = api_key_secret_config
        if api_key_secret_source is not None:
            input_["api_key_secret_source"] = api_key_secret_source

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_api_key_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse":
        """<p>Deletes an API key credential provider.</p>

        Args:
            name: <p>The name of the API key credential provider to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_response.DeleteApiKeyCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_api_key_credential_provider.delete_api_key_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_api_key_credential_provider_request.DeleteApiKeyCredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_api_key_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse":
        """<p>Lists all API key credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_api_key_credential_providers_response.ListApiKeyCredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_api_key_credential_providers.list_api_key_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_api_key_credential_providers_request.ListApiKeyCredentialProvidersRequest = {}
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

    def iter_list_api_key_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.api_key_credential_provider_item.ApiKeyCredentialProviderItem]":
        _token = next_token
        while True:
            _response = self.list_api_key_credential_providers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("credential_providers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_browser_profile(
        self,
        name: "capo_bedrock_agentcore_control.types.browser_profile_name.BrowserProfileName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_browser_profile_response.CreateBrowserProfileResponse":
        """<p>Creates a browser profile in Amazon Bedrock AgentCore. A browser profile stores persistent browser data such as cookies, local storage, session storage, and browsing history that can be saved from browser sessions and reused in subsequent sessions.</p>

        Args:
            name: <p>The name of the browser profile. The name must be unique within your account and can contain alphanumeric characters and underscores.</p>
            description: <p>A description of the browser profile. Use this field to describe the purpose or contents of the profile.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the browser profile. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_browser_profile_request.CreateBrowserProfileRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_browser_profile_response.CreateBrowserProfileResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser_profile

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser_profile.create_browser_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_browser_profile_request.CreateBrowserProfileRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
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

    def get_browser_profile(
        self,
        profile_id: "capo_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_browser_profile_response.GetBrowserProfileResponse":
        """<p>Gets information about a browser profile.</p>

        Args:
            profile_id: <p>The unique identifier of the browser profile to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_browser_profile_request.GetBrowserProfileRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_browser_profile_response.GetBrowserProfileResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser_profile

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser_profile.get_browser_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_browser_profile_request.GetBrowserProfileRequest = {
            "profile_id": profile_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_browser_profile(
        self,
        profile_id: "capo_bedrock_agentcore_control.types.browser_profile_id.BrowserProfileId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_browser_profile_response.DeleteBrowserProfileResponse":
        """<p>Deletes a browser profile.</p>

        Args:
            profile_id: <p>The unique identifier of the browser profile to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_browser_profile_request.DeleteBrowserProfileRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_browser_profile_response.DeleteBrowserProfileResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser_profile

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser_profile.delete_browser_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_browser_profile_request.DeleteBrowserProfileRequest = {
            "profile_id": profile_id
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

    def list_browser_profiles(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.browser_profile_name.BrowserProfileName"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_browser_profiles_response.ListBrowserProfilesResponse":
        """<p>Lists all browser profiles in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
            name: <p>The name of the browser profile to filter results by.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_browser_profiles_request.ListBrowserProfilesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_browser_profiles_response.ListBrowserProfilesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browser_profiles

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browser_profiles.list_browser_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_browser_profiles_request.ListBrowserProfilesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_browser_profiles(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.browser_profile_name.BrowserProfileName"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.browser_profile_summary.BrowserProfileSummary]":
        _token = next_token
        while True:
            _response = self.list_browser_profiles(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
            )
            _page = _resolve_path(_response, ("profile_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_browser(
        self,
        name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "capo_bedrock_agentcore_control.types.browser_network_configuration.BrowserNetworkConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        recording: Optional[
            "capo_bedrock_agentcore_control.types.recording_config.RecordingConfig"
        ] = None,
        browser_signing: Optional[
            "capo_bedrock_agentcore_control.types.browser_signing_config_input.BrowserSigningConfigInput"
        ] = None,
        enterprise_policies: Optional[
            "capo_bedrock_agentcore_control.types.browser_enterprise_policies.BrowserEnterprisePolicies"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore_control.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_browser_response.CreateBrowserResponse":
        """<p>Creates a custom browser.</p>

        Args:
            name: <p>The name of the browser. The name must be unique within your account.</p>
            description: <p>The description of the browser.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the browser to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the browser. This configuration specifies the network mode for the browser.</p>
            recording: <p>The recording configuration for the browser. When enabled, browser sessions are recorded and stored in the specified Amazon S3 location.</p>
            browser_signing: <p>The browser signing configuration that enables cryptographic agent identification using HTTP message signatures for web bot authentication.</p>
            enterprise_policies: <p>A list of enterprise policy files for the browser.</p>
            certificates: <p>A list of certificates to install in the browser.</p>
            filesystem_configurations: <p>The file system configurations to mount into the browser. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the browser. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_browser_response.CreateBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_browser.create_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_browser_request.CreateBrowserRequest = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if recording is not None:
            input_["recording"] = recording
        if browser_signing is not None:
            input_["browser_signing"] = browser_signing
        if enterprise_policies is not None:
            input_["enterprise_policies"] = enterprise_policies
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    def get_browser(
        self,
        browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse":
        """<p>Gets information about a custom browser.</p>

        Args:
            browser_id: <p>The unique identifier of the browser to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_browser_request.GetBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_browser_response.GetBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_browser.get_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_browser_request.GetBrowserRequest = {
            "browser_id": browser_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_browser(
        self,
        browser_id: "capo_bedrock_agentcore_control.types.browser_id.BrowserId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_browser_response.DeleteBrowserResponse":
        """<p>Deletes a custom browser.</p>

        Args:
            browser_id: <p>The unique identifier of the browser to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_browser_request.DeleteBrowserRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_browser_response.DeleteBrowserResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_browser.delete_browser(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_browser_request.DeleteBrowserRequest = {
            "browser_id": browser_id
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

    def list_browsers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "capo_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse":
        """<p>Lists all custom browsers in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>
            type: <p>The type of browsers to list. If not specified, all browser types are returned.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_browsers_request.ListBrowsersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_browsers_response.ListBrowsersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browsers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_browsers.list_browsers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_browsers_request.ListBrowsersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_browsers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "capo_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> (
        "Iterator[capo_bedrock_agentcore_control.types.browser_summary.BrowserSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_browsers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                type=type,
            )
            _page = _resolve_path(_response, ("browser_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_capacity_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.capacity_provider_name.CapacityProviderName",
        permissions_configuration: "capo_bedrock_agentcore_control.types.permissions_configuration.PermissionsConfiguration",
        compute_configuration: "capo_bedrock_agentcore_control.types.compute_configuration.ComputeConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_capacity_provider_output.CreateCapacityProviderOutput":
        """<p>Creates a capacity provider. A capacity provider defines the Amazon EC2 infrastructure for AgentCore Runtime, including the operating system, allowed instance types, networking, and storage. It also specifies the IAM permissions that AgentCore uses to manage those instances.</p> <p>The capacity provider name must be unique within your account. After you create the capacity provider, it enters a <code>CREATING</code> state and transitions to <code>READY</code> when it is available for use.</p>

        Args:
            name: <p>The name of the capacity provider. The name must be unique within your account.</p>
            description: <p>An optional description of the capacity provider. If you don't specify a description, the service creates the capacity provider without one.</p>
            permissions_configuration: <p>The permissions configuration for the capacity provider. This specifies the IAM role that AgentCore uses to manage the Amazon EC2 instances on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>A map of tag keys and values to associate with the capacity provider. If you don't specify tags, the capacity provider is created with no tags.</p>
            compute_configuration: <p>The compute configuration for the capacity provider. This defines the Amazon EC2 compute resources used to launch instances: the operating system, allowed instance types, networking, and storage.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.retryable_conflict_exception.RetryableConflictException: <p>The operation failed because of a conflicting request. Retry the request.</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_capacity_provider_input.CreateCapacityProviderInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_capacity_provider_output.CreateCapacityProviderOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_capacity_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_capacity_provider.create_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_capacity_provider_input.CreateCapacityProviderInput = {
            "name": name,
            "permissions_configuration": permissions_configuration,
            "compute_configuration": compute_configuration,
        }
        if description is not None:
            input_["description"] = description
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

    def get_capacity_provider(
        self,
        capacity_provider_id: "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_capacity_provider_output.GetCapacityProviderOutput":
        """<p>Retrieves information about a capacity provider, including its status, permissions configuration, and compute configuration.</p>

        Args:
            capacity_provider_id: <p>The unique identifier of the capacity provider.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_capacity_provider_input.GetCapacityProviderInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_capacity_provider_output.GetCapacityProviderOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_capacity_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_capacity_provider.get_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_capacity_provider_input.GetCapacityProviderInput = {
            "capacity_provider_id": capacity_provider_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_capacity_provider(
        self,
        capacity_provider_id: "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_capacity_provider_output.UpdateCapacityProviderOutput":
        """<p>Updates a capacity provider. Only the description can be changed. To change other configuration, such as instance types, networking, or storage, create a new capacity provider.</p>

        Args:
            capacity_provider_id: <p>The unique identifier of the capacity provider to update.</p>
            description: <p>The updated description of the capacity provider.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.retryable_conflict_exception.RetryableConflictException: <p>The operation failed because of a conflicting request. Retry the request.</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_capacity_provider_input.UpdateCapacityProviderInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_capacity_provider_output.UpdateCapacityProviderOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_capacity_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_capacity_provider.update_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_capacity_provider_input.UpdateCapacityProviderInput = {
            "capacity_provider_id": capacity_provider_id
        }
        if description is not None:
            input_["description"] = description
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

    def delete_capacity_provider(
        self,
        capacity_provider_id: "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_capacity_provider_output.DeleteCapacityProviderOutput":
        """<p>Deletes a capacity provider. Before you delete a capacity provider, disassociate all agent runtimes and runtime versions that reference it. If any references remain, the operation fails.</p>

        Args:
            capacity_provider_id: <p>The unique identifier of the capacity provider to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.retryable_conflict_exception.RetryableConflictException: <p>The operation failed because of a conflicting request. Retry the request.</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_capacity_provider_input.DeleteCapacityProviderInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_capacity_provider_output.DeleteCapacityProviderOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_capacity_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_capacity_provider.delete_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_capacity_provider_input.DeleteCapacityProviderInput = {
            "capacity_provider_id": capacity_provider_id
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

    def list_capacity_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_capacity_providers_output.ListCapacityProvidersOutput":
        """<p>Lists the capacity providers in your account and returns summary information for each one. To retrieve the full configuration for a specific capacity provider, use <code>GetCapacityProvider</code>. Results are paginated; use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_capacity_providers_input.ListCapacityProvidersInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_capacity_providers_output.ListCapacityProvidersOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_capacity_providers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_capacity_providers.list_capacity_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_capacity_providers_input.ListCapacityProvidersInput = {}
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

    def iter_list_capacity_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.capacity_provider_summary.CapacityProviderSummary]":
        _token = next_token
        while True:
            _response = self.list_capacity_providers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("capacity_providers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_agent_runtime_versions_by_capacity_provider(
        self,
        capacity_provider_id: "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_by_capacity_provider_output.ListAgentRuntimeVersionsByCapacityProviderOutput":
        """<p>Lists the agent runtime versions that are associated with a capacity provider. Use this operation to identify the runtimes you must disassociate before you can delete the capacity provider. Results are paginated; use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            capacity_provider_id: <p>The unique identifier of the capacity provider.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_agent_runtime_versions_by_capacity_provider_input.ListAgentRuntimeVersionsByCapacityProviderInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_agent_runtime_versions_by_capacity_provider_output.ListAgentRuntimeVersionsByCapacityProviderOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions_by_capacity_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_agent_runtime_versions_by_capacity_provider.list_agent_runtime_versions_by_capacity_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_agent_runtime_versions_by_capacity_provider_input.ListAgentRuntimeVersionsByCapacityProviderInput = {
            "capacity_provider_id": capacity_provider_id
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

    def iter_list_agent_runtime_versions_by_capacity_provider(
        self,
        capacity_provider_id: "capo_bedrock_agentcore_control.types.capacity_provider_id.CapacityProviderId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.agent_runtime_version_summary.AgentRuntimeVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_agent_runtime_versions_by_capacity_provider(
                capacity_provider_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("agent_runtimes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_code_interpreter(
        self,
        name: "capo_bedrock_agentcore_control.types.sandbox_name.SandboxName",
        network_configuration: "capo_bedrock_agentcore_control.types.code_interpreter_network_configuration.CodeInterpreterNetworkConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        certificates: Optional[
            "capo_bedrock_agentcore_control.types.certificates.Certificates"
        ] = None,
        filesystem_configurations: Optional[
            "capo_bedrock_agentcore_control.types.tools_file_system_configurations.ToolsFileSystemConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse":
        """<p>Creates a custom code interpreter.</p>

        Args:
            name: <p>The name of the code interpreter. The name must be unique within your account.</p>
            description: <p>The description of the code interpreter.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the code interpreter to access Amazon Web Services services.</p>
            network_configuration: <p>The network configuration for the code interpreter. This configuration specifies the network mode for the code interpreter.</p>
            certificates: <p>A list of certificates to install in the code interpreter.</p>
            filesystem_configurations: <p>The file system configurations to mount into the code interpreter. Use these configurations to mount your own Amazon Simple Storage Service (Amazon S3) Files or Amazon Elastic File System (Amazon EFS) access points. Your sessions can then access your data. If you don't specify this field, no file systems are mounted.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock AgentCore ignores the request but does not return an error.</p>
            tags: <p>A map of tag keys and values to assign to the code interpreter. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_code_interpreter_response.CreateCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_code_interpreter.create_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_code_interpreter_request.CreateCodeInterpreterRequest = {
            "name": name,
            "network_configuration": network_configuration,
        }
        if description is not None:
            input_["description"] = description
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if certificates is not None:
            input_["certificates"] = certificates
        if filesystem_configurations is not None:
            input_["filesystem_configurations"] = filesystem_configurations
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

    def get_code_interpreter(
        self,
        code_interpreter_id: "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse":
        """<p>Gets information about a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_code_interpreter_response.GetCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_code_interpreter.get_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_code_interpreter_request.GetCodeInterpreterRequest = {
            "code_interpreter_id": code_interpreter_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_code_interpreter(
        self,
        code_interpreter_id: "capo_bedrock_agentcore_control.types.code_interpreter_id.CodeInterpreterId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse":
        """<p>Deletes a custom code interpreter.</p>

        Args:
            code_interpreter_id: <p>The unique identifier of the code interpreter to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_code_interpreter_response.DeleteCodeInterpreterResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_code_interpreter.delete_code_interpreter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_code_interpreter_request.DeleteCodeInterpreterRequest = {
            "code_interpreter_id": code_interpreter_id
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

    def list_code_interpreters(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "capo_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse":
        """<p>Lists all custom code interpreters in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>A token to retrieve the next page of results.</p>
            type: <p>The type of code interpreters to list.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_code_interpreters_response.ListCodeInterpretersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_code_interpreters.list_code_interpreters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_code_interpreters_request.ListCodeInterpretersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_code_interpreters(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        type: Optional[
            "capo_bedrock_agentcore_control.types.resource_type.ResourceType"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.code_interpreter_summary.CodeInterpreterSummary]":
        _token = next_token
        while True:
            _response = self.list_code_interpreters(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                type=type,
            )
            _page = _resolve_path(_response, ("code_interpreter_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_configuration_bundle(
        self,
        bundle_name: "capo_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName",
        components: "capo_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
        ] = None,
        branch_name: Optional[
            "capo_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
        commit_message: Optional[str] = None,
        created_by: Optional[
            "capo_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_configuration_bundle_response.CreateConfigurationBundleResponse":
        """<p>Creates a new configuration bundle resource. A configuration bundle stores versioned component configurations for agent evaluation workflows.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            bundle_name: <p>The name for the configuration bundle. Names must be unique within your account.</p>
            description: <p>The description for the configuration bundle.</p>
            components: <p>A map of component identifiers to their configurations. Each component represents a configurable element within the bundle.</p>
            branch_name: <p>The branch name for version tracking. Defaults to <code>mainline</code> if not specified.</p>
            commit_message: <p>A commit message describing the initial version of the configuration bundle.</p>
            created_by: <p>The source that created this version, including the source name and optional ARN.</p>
            kms_key_arn: <p>Optional KMS key ARN for encrypting component configurations.</p>
            tags: <p>A map of tag keys and values to assign to the configuration bundle. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_configuration_bundle_request.CreateConfigurationBundleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_configuration_bundle_response.CreateConfigurationBundleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_configuration_bundle

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_configuration_bundle.create_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_configuration_bundle_request.CreateConfigurationBundleRequest = {
            "bundle_name": bundle_name,
            "components": components,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if commit_message is not None:
            input_["commit_message"] = commit_message
        if created_by is not None:
            input_["created_by"] = created_by
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_configuration_bundle(
        self,
        bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        branch_name: Optional[
            "capo_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_configuration_bundle_response.GetConfigurationBundleResponse":
        """<p>Gets the latest version of a configuration bundle. By default, returns the latest version on the mainline branch. Use <code>GetConfigurationBundleVersion</code> to retrieve a specific historical version.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to retrieve.</p>
            branch_name: <p>The branch name to get the latest version from. If not specified, returns the latest version on the mainline branch.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_configuration_bundle_request.GetConfigurationBundleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_configuration_bundle_response.GetConfigurationBundleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle.get_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_configuration_bundle_request.GetConfigurationBundleRequest = {
            "bundle_id": bundle_id
        }
        if branch_name is not None:
            input_["branch_name"] = branch_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_configuration_bundle(
        self,
        bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        parent_version_ids: "capo_bedrock_agentcore_control.types.configuration_bundle_version_list.ConfigurationBundleVersionList",
        commit_message: str,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        bundle_name: Optional[
            "capo_bedrock_agentcore_control.types.configuration_bundle_name.ConfigurationBundleName"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.configuration_bundle_description.ConfigurationBundleDescription"
        ] = None,
        components: Optional[
            "capo_bedrock_agentcore_control.types.component_configuration_map.ComponentConfigurationMap"
        ] = None,
        branch_name: Optional[
            "capo_bedrock_agentcore_control.types.branch_name.BranchName"
        ] = None,
        created_by: Optional[
            "capo_bedrock_agentcore_control.types.version_created_by_source.VersionCreatedBySource"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_configuration_bundle_response.UpdateConfigurationBundleResponse":
        """<p>Updates a configuration bundle by creating a new version with the specified changes. Each update creates a new version in the version history.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            bundle_id: <p>The unique identifier of the configuration bundle to update.</p>
            bundle_name: <p>The updated name for the configuration bundle.</p>
            description: <p>The updated description for the configuration bundle.</p>
            components: <p>The updated component configurations. Creates a new version of the bundle.</p>
            parent_version_ids: <p>A list of parent version identifiers for lineage tracking. Regular commits have a single parent. Merge commits have two parents: the target branch parent and the source branch parent. If the branch already exists, the first parent must be the latest version on that branch.</p>
            branch_name: <p>The branch name for this version. If not specified, inherits the parent's branch or defaults to <code>mainline</code>.</p>
            commit_message: <p>A commit message describing the changes in this version.</p>
            created_by: <p>The source that created this version, including the source name and optional ARN.</p>
            kms_key_arn: <p>Optional KMS key ARN for encrypting component configurations. If provided, components will be encrypted with this key. If the bundle already has a KMS key, this rotates to the new key.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_configuration_bundle_request.UpdateConfigurationBundleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_configuration_bundle_response.UpdateConfigurationBundleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_configuration_bundle

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_configuration_bundle.update_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_configuration_bundle_request.UpdateConfigurationBundleRequest = {
            "bundle_id": bundle_id,
            "parent_version_ids": parent_version_ids,
            "commit_message": commit_message,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if bundle_name is not None:
            input_["bundle_name"] = bundle_name
        if description is not None:
            input_["description"] = description
        if components is not None:
            input_["components"] = components
        if branch_name is not None:
            input_["branch_name"] = branch_name
        if created_by is not None:
            input_["created_by"] = created_by
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_configuration_bundle(
        self,
        bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_configuration_bundle_response.DeleteConfigurationBundleResponse":
        """<p>Deletes a configuration bundle and all of its versions.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_configuration_bundle_request.DeleteConfigurationBundleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_configuration_bundle_response.DeleteConfigurationBundleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_configuration_bundle

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_configuration_bundle.delete_configuration_bundle(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_configuration_bundle_request.DeleteConfigurationBundleRequest = {
            "bundle_id": bundle_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_configuration_bundles(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_configuration_bundles_response.ListConfigurationBundlesResponse":
        """<p>Lists all configuration bundles in the account.</p>

        Args:
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_configuration_bundles_request.ListConfigurationBundlesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_configuration_bundles_response.ListConfigurationBundlesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundles

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundles.list_configuration_bundles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_configuration_bundles_request.ListConfigurationBundlesRequest = {}
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

    def iter_list_configuration_bundles(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.configuration_bundle_summary.ConfigurationBundleSummary]":
        _token = next_token
        while True:
            _response = self.list_configuration_bundles(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("bundles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_configuration_bundle_version(
        self,
        bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        version_id: "capo_bedrock_agentcore_control.types.configuration_bundle_version.ConfigurationBundleVersion",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_configuration_bundle_version_response.GetConfigurationBundleVersionResponse":
        """<p>Gets a specific version of a configuration bundle by its version identifier.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle.</p>
            version_id: <p>The version identifier of the configuration bundle version to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_configuration_bundle_version_request.GetConfigurationBundleVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_configuration_bundle_version_response.GetConfigurationBundleVersionResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle_version

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_configuration_bundle_version.get_configuration_bundle_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_configuration_bundle_version_request.GetConfigurationBundleVersionRequest = {
            "bundle_id": bundle_id,
            "version_id": version_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_configuration_bundle_versions(
        self,
        bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_bedrock_agentcore_control.types.version_filter.VersionFilter"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_configuration_bundle_versions_response.ListConfigurationBundleVersionsResponse":
        """<p>Lists all versions of a configuration bundle, with optional filtering by branch name or creation source.</p>

        Args:
            bundle_id: <p>The unique identifier of the configuration bundle to list versions for.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            filter: <p>An optional filter for listing versions, including branch name, creation source, and whether to return only the latest version per branch.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_configuration_bundle_versions_request.ListConfigurationBundleVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_configuration_bundle_versions_response.ListConfigurationBundleVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundle_versions

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_configuration_bundle_versions.list_configuration_bundle_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_configuration_bundle_versions_request.ListConfigurationBundleVersionsRequest = {
            "bundle_id": bundle_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_configuration_bundle_versions(
        self,
        bundle_id: "capo_bedrock_agentcore_control.types.configuration_bundle_id.ConfigurationBundleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
        filter: Optional[
            "capo_bedrock_agentcore_control.types.version_filter.VersionFilter"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.configuration_bundle_version_summary.ConfigurationBundleVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_configuration_bundle_versions(
                bundle_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_consent_portal(
        self,
        execution_role_arn: "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType",
        idp_config: "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig",
        name: "capo_bedrock_agentcore_control.types.consent_portal_name_type.ConsentPortalNameType",
        sources: "capo_bedrock_agentcore_control.types.consent_portal_sources.ConsentPortalSources",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_consent_portal_response.CreateConsentPortalResponse":
        """<p>Creates a new consent portal.</p>

        Args:
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>
            idp_config: <p>The identity provider configuration that the consent portal uses to authenticate end users.</p>
            name: <p>The name of the consent portal. The name must be unique within your account.</p>
            sources: <p>The resources served by the consent portal. Currently, we only support type <code>agentcore-gateway</code>.</p>
            description: <p>The description of the consent portal.</p>
            tags: <p>A map of tag keys and values to assign to the consent portal. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_consent_portal_request.CreateConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_consent_portal_response.CreateConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_consent_portal.create_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_consent_portal_request.CreateConsentPortalRequest = {
            "execution_role_arn": execution_role_arn,
            "idp_config": idp_config,
            "name": name,
            "sources": sources,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_consent_portal(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_consent_portal_response.GetConsentPortalResponse":
        """<p>Retrieves information about a consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_consent_portal_request.GetConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_consent_portal_response.GetConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_consent_portal.get_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_consent_portal_request.GetConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_consent_portal(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.execution_role_arn_type.ExecutionRoleArnType"
        ] = None,
        idp_config: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_idp_config.ConsentPortalIdpConfig"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.consent_portal_description_type.ConsentPortalDescriptionType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_consent_portal_response.UpdateConsentPortalResponse":
        """<p>Updates an existing consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the consent portal assumes to access the resources defined in its sources.</p>
            idp_config: <p>The identity provider configuration that the consent portal uses to authenticate end users.</p>
            description: <p>The description of the consent portal.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_consent_portal_request.UpdateConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_consent_portal_response.UpdateConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_consent_portal.update_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_consent_portal_request.UpdateConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if idp_config is not None:
            input_["idp_config"] = idp_config
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_consent_portal(
        self,
        consent_portal_identifier: "capo_bedrock_agentcore_control.types.consent_portal_identifier.ConsentPortalIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_consent_portal_response.DeleteConsentPortalResponse":
        """<p>Deletes a consent portal.</p>

        Args:
            consent_portal_identifier: <p>The identifier of the consent portal. You can specify either the consent portal ID or its Amazon Resource Name (ARN).</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_consent_portal_request.DeleteConsentPortalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_consent_portal_response.DeleteConsentPortalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_consent_portal

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_consent_portal.delete_consent_portal(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_consent_portal_request.DeleteConsentPortalRequest = {
            "consent_portal_identifier": consent_portal_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_consent_portals(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_consent_portals_response.ListConsentPortalsResponse":
        """<p>Lists all of the consent portals in your account.</p>

        Args:
            max_results: <p>The maximum number of consent portals to return in a single call.</p>
            next_token: <p>A token to retrieve the next page of results. Use the value returned in a previous response to request the next page.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_consent_portals_request.ListConsentPortalsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_consent_portals_response.ListConsentPortalsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_consent_portals

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_consent_portals.list_consent_portals(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_consent_portals_request.ListConsentPortalsRequest = {}
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

    def iter_list_consent_portals(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.consent_portal_summary.ConsentPortalSummary]":
        _token = next_token
        while True:
            _response = self.list_consent_portals(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("consent_portals",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_dataset(
        self,
        dataset_name: "capo_bedrock_agentcore_control.types.dataset_name.DatasetName",
        source: "capo_bedrock_agentcore_control.types.data_source_type.DataSourceType",
        schema_type: "capo_bedrock_agentcore_control.types.dataset_schema_type.DatasetSchemaType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[str] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_dataset_response.CreateDatasetResponse":
        """<p> Creates a new dataset resource asynchronously. Returns immediately with status CREATING. Poll <code>GetDataset</code> until status transitions to ACTIVE or CREATE_FAILED. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            dataset_name: <p> Human-readable name for the dataset. Must be unique within the account. Immutable after creation. </p>
            description: <p> A description of the dataset. </p>
            source: <p> Source of initial examples. Provide either inline examples or an S3 URI pointing to a JSONL file. </p>
            schema_type: <p> Versioned schema type governing the structure of examples. Immutable after creation. </p>
            kms_key_arn: <p> Optional KMS key ARN for server-side encryption on service Amazon S3 writes. </p>
            tags: <p> A map of tag keys and values to assign to the dataset. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_dataset_request.CreateDatasetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_dataset

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_dataset.create_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_dataset_request.CreateDatasetRequest = {
            "dataset_name": dataset_name,
            "source": source,
            "schema_type": schema_type,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dataset(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        dataset_version: Optional[
            "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_dataset_response.GetDatasetResponse":
        """<p> Retrieves dataset metadata. Use the <code>datasetVersion</code> query parameter to retrieve a specific version's metadata. If absent, defaults to DRAFT. For paginated example content, use <code>ListDatasetExamples</code>. </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset to retrieve. </p>
            dataset_version: <p> Version to retrieve: "DRAFT" or a version number. Defaults to DRAFT if absent. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_dataset_request.GetDatasetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_dataset_response.GetDatasetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_dataset

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_dataset.get_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_dataset_request.GetDatasetRequest = {
            "dataset_id": dataset_id
        }
        if dataset_version is not None:
            input_["dataset_version"] = dataset_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_dataset(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_dataset_response.UpdateDatasetResponse":
        """<p> Updates a dataset's metadata. Synchronous operation. Only provided fields are updated; omitted fields remain unchanged. To modify dataset content, use <code>AddDatasetExamples</code>, <code>UpdateDatasetExamples</code>, or <code>DeleteDatasetExamples</code>. </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset to update. </p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            description: <p> The updated description for the dataset. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_dataset_request.UpdateDatasetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_dataset_response.UpdateDatasetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_dataset

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_dataset.update_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_dataset_request.UpdateDatasetRequest = {
            "dataset_id": dataset_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_dataset(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        dataset_version: Optional[
            "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_dataset_response.DeleteDatasetResponse":
        """<p> Deletes a dataset version or an entire dataset asynchronously. If <code>datasetVersion</code> is absent, deletes all versions and the dataset record itself. If provided, deletes only that specific version. </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset to delete. </p>
            dataset_version: <p> Optional version to delete. If absent, deletes the entire dataset. If provided, deletes only that specific version. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_dataset

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_dataset.delete_dataset(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_dataset_request.DeleteDatasetRequest = {
            "dataset_id": dataset_id
        }
        if dataset_version is not None:
            input_["dataset_version"] = dataset_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_datasets(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_datasets_response.ListDatasetsResponse":
        """<p> Lists all datasets in the caller's account, paginated. </p>

        Args:
            next_token: <p> The token for the next page of results. </p>
            max_results: <p> The maximum number of datasets to return per page. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_datasets_request.ListDatasetsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_datasets

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_datasets.list_datasets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_datasets_request.ListDatasetsRequest = {}
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

    def iter_list_datasets(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> (
        "Iterator[capo_bedrock_agentcore_control.types.dataset_summary.DatasetSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_datasets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("datasets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def add_dataset_examples(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        source: "capo_bedrock_agentcore_control.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.add_dataset_examples_response.AddDatasetExamplesResponse":
        """<p> Adds examples to the dataset's DRAFT. All examples are validated against the dataset's schema type before any writes occur. If any example fails validation, the entire batch is rejected (all-or-nothing semantics). </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset to add examples to. </p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            source: <p> Source of examples to add. Provide either inline examples or an S3 URI pointing to a JSONL file. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.add_dataset_examples_request.AddDatasetExamplesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.add_dataset_examples_response.AddDatasetExamplesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.add_dataset_examples

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.add_dataset_examples.add_dataset_examples(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.add_dataset_examples_request.AddDatasetExamplesRequest = {
            "dataset_id": dataset_id,
            "source": source,
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

    def create_dataset_version(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_dataset_version_response.CreateDatasetVersionResponse":
        """<p> Publishes the current DRAFT as a new numbered version. The DRAFT is preserved and remains editable after publishing. Returns immediately with status UPDATING. Poll <code>GetDataset</code> until status transitions to ACTIVE or UPDATE_FAILED. </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset to publish a version for. </p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_dataset_version_request.CreateDatasetVersionRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_dataset_version_response.CreateDatasetVersionResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_dataset_version

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_dataset_version.create_dataset_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_dataset_version_request.CreateDatasetVersionRequest = {
            "dataset_id": dataset_id
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

    def delete_dataset_examples(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        example_ids: "capo_bedrock_agentcore_control.types.example_id_list.ExampleIdList",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_dataset_examples_response.DeleteDatasetExamplesResponse":
        """<p> Deletes specific examples by ID from DRAFT. All example IDs are validated before any deletes occur. If any ID does not exist in DRAFT, the entire batch is rejected (all-or-nothing semantics). </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset. </p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            example_ids: <p> The IDs of the examples to delete. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_dataset_examples_request.DeleteDatasetExamplesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_dataset_examples_response.DeleteDatasetExamplesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_dataset_examples

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_dataset_examples.delete_dataset_examples(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_dataset_examples_request.DeleteDatasetExamplesRequest = {
            "dataset_id": dataset_id,
            "example_ids": example_ids,
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

    def list_dataset_examples(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        dataset_version: Optional[
            "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_dataset_examples_response.ListDatasetExamplesResponse":
        """<p> Returns paginated examples from the dataset. The server embeds the resolved version in the pagination token. Once pagination begins, all subsequent pages are pinned to that version regardless of concurrent mutations. </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset. </p>
            dataset_version: <p> Version to paginate: "DRAFT" or a version number. Defaults to DRAFT if absent. Only used on the first request; for subsequent pages, the version is extracted from the pagination token. </p>
            max_results: <p> Maximum number of examples to return per page. </p>
            next_token: <p> The token for the next page of results. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_dataset_examples_request.ListDatasetExamplesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_dataset_examples_response.ListDatasetExamplesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_dataset_examples

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_dataset_examples.list_dataset_examples(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_dataset_examples_request.ListDatasetExamplesRequest = {
            "dataset_id": dataset_id
        }
        if dataset_version is not None:
            input_["dataset_version"] = dataset_version
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

    def iter_list_dataset_examples(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        dataset_version: Optional[
            "capo_bedrock_agentcore_control.types.dataset_version.DatasetVersion"
        ] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.sensitive_json.SensitiveJson]":
        _token = next_token
        while True:
            _response = self.list_dataset_examples(
                dataset_id,
                config_overrides=config_overrides,
                dataset_version=dataset_version,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("examples",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_dataset_versions(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_dataset_versions_response.ListDatasetVersionsResponse":
        """<p> Lists all published versions of a dataset, sorted by version number descending (newest first). Does not include the DRAFT working copy. </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset. </p>
            next_token: <p> The token for the next page of results. </p>
            max_results: <p> The maximum number of versions to return per page. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_dataset_versions_request.ListDatasetVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_dataset_versions_response.ListDatasetVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_dataset_versions

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_dataset_versions.list_dataset_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_dataset_versions_request.ListDatasetVersionsRequest = {
            "dataset_id": dataset_id
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

    def iter_list_dataset_versions(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.dataset_version_summary.DatasetVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_dataset_versions(
                dataset_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_dataset_examples(
        self,
        dataset_id: "capo_bedrock_agentcore_control.types.dataset_id.DatasetId",
        examples: "capo_bedrock_agentcore_control.types.dataset_example_list.DatasetExampleList",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_dataset_examples_response.UpdateDatasetExamplesResponse":
        """<p> Updates multiple existing examples in-place on DRAFT. All examples are validated against the dataset's schema type before any writes occur. If any example fails validation, the entire batch is rejected (all-or-nothing semantics). </p>

        Args:
            dataset_id: <p> The unique identifier of the dataset. </p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            examples: <p> Examples to update. Each element is a JSON object containing a required <code>exampleId</code> field identifying the existing example, plus the replacement fields. Maximum 1000 examples per call. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_dataset_examples_request.UpdateDatasetExamplesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_dataset_examples_response.UpdateDatasetExamplesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_dataset_examples

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_dataset_examples.update_dataset_examples(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_dataset_examples_request.UpdateDatasetExamplesRequest = {
            "dataset_id": dataset_id,
            "examples": examples,
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

    def create_evaluator(
        self,
        evaluator_name: "capo_bedrock_agentcore_control.types.custom_evaluator_name.CustomEvaluatorName",
        evaluator_config: "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig",
        level: "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_evaluator_response.CreateEvaluatorResponse":
        """<p> Creates a custom evaluator for agent quality assessment. Custom evaluators can use either LLM-as-a-Judge configurations with user-defined prompts, rating scales, and model settings, or code-based configurations with customer-managed Lambda functions to evaluate agent performance at tool call, trace, or session levels. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            evaluator_name: <p> The name of the evaluator. Must be unique within your account. </p>
            description: <p> The description of the evaluator that explains its purpose and evaluation criteria. </p>
            evaluator_config: <p> The configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>
            level: <p> The evaluation level that determines the scope of evaluation. Valid values are <code>TOOL_CALL</code> for individual tool invocations, <code>TRACE</code> for single request-response interactions, or <code>SESSION</code> for entire conversation sessions. </p>
            kms_key_arn: <p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data, including instructions and rating scale. If you don't specify a KMS key, the evaluator data is encrypted with an Amazon Web Services owned key. Only symmetric encryption KMS keys are supported. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Evaluator. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_evaluator_request.CreateEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_evaluator_response.CreateEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_evaluator.create_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_evaluator_request.CreateEvaluatorRequest = {
            "evaluator_name": evaluator_name,
            "evaluator_config": evaluator_config,
            "level": level,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_evaluator(
        self,
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        included_data: Optional[
            "capo_bedrock_agentcore_control.types.included_data.IncludedData"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_evaluator_response.GetEvaluatorResponse":
        """<p> Retrieves detailed information about an evaluator, including its configuration, status, and metadata. Works with both built-in and custom evaluators. </p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to retrieve. Can be a built-in evaluator ID (e.g., Builtin.Helpfulness) or a custom evaluator ID. </p>
            included_data: <p> Controls which data is returned in the response. <code>ALL_DATA</code> (default) returns the full evaluator including decrypted instructions and rating scale. For evaluators encrypted with a customer managed KMS key, this requires <code>kms:Decrypt</code> permission on the key. <code>METADATA_ONLY</code> returns evaluator metadata and model configuration without instructions or rating scale, and does not require any KMS permissions. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_evaluator_request.GetEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_evaluator_response.GetEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_evaluator.get_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_evaluator_request.GetEvaluatorRequest = {
            "evaluator_id": evaluator_id
        }
        if included_data is not None:
            input_["included_data"] = included_data

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_evaluator(
        self,
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_description.EvaluatorDescription"
        ] = None,
        evaluator_config: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_config.EvaluatorConfig"
        ] = None,
        level: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_level.EvaluatorLevel"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_evaluator_response.UpdateEvaluatorResponse":
        """<p> Updates a custom evaluator's configuration, description, or evaluation level. Built-in evaluators cannot be updated. The evaluator must not be locked for modification. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            evaluator_id: <p> The unique identifier of the evaluator to update. </p>
            description: <p> The updated description of the evaluator. </p>
            evaluator_config: <p> The updated configuration for the evaluator. Specify either LLM-as-a-Judge settings with instructions, rating scale, and model configuration, or code-based settings with a customer-managed Lambda function. </p>
            level: <p> The updated evaluation level (<code>TOOL_CALL</code>, <code>TRACE</code>, or <code>SESSION</code>) that determines the scope of evaluation. </p>
            kms_key_arn: <p> The Amazon Resource Name (ARN) of a customer managed KMS key to use for encrypting sensitive evaluator data. Specify a new key ARN to rotate the encryption key, or specify a key ARN to add encryption to an evaluator that was previously created without one. When you rotate to a new key, the service decrypts the existing data with the old key and re-encrypts it with the new key. Only symmetric encryption KMS keys are supported. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_evaluator_request.UpdateEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_evaluator_response.UpdateEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_evaluator.update_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_evaluator_request.UpdateEvaluatorRequest = {
            "evaluator_id": evaluator_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if evaluator_config is not None:
            input_["evaluator_config"] = evaluator_config
        if level is not None:
            input_["level"] = level
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_evaluator(
        self,
        evaluator_id: "capo_bedrock_agentcore_control.types.evaluator_id.EvaluatorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_evaluator_response.DeleteEvaluatorResponse":
        """<p> Deletes a custom evaluator. Builtin evaluators cannot be deleted. The evaluator must not be referenced by any active online evaluation configurations. </p>

        Args:
            evaluator_id: <p> The unique identifier of the evaluator to delete. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_evaluator_request.DeleteEvaluatorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_evaluator_response.DeleteEvaluatorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_evaluator

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_evaluator.delete_evaluator(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_evaluator_request.DeleteEvaluatorRequest = {
            "evaluator_id": evaluator_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_evaluators(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_evaluators_response.ListEvaluatorsResponse":
        """<p> Lists all available evaluators, including both builtin evaluators provided by the service and custom evaluators created by the user. </p>

        Args:
            next_token: <p> The pagination token from a previous request to retrieve the next page of results. </p>
            max_results: <p> The maximum number of evaluators to return in a single response. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_evaluators_request.ListEvaluatorsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_evaluators_response.ListEvaluatorsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_evaluators

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_evaluators.list_evaluators(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_evaluators_request.ListEvaluatorsRequest = {}
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

    def iter_list_evaluators(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.evaluator_summary.EvaluatorSummary]":
        _token = next_token
        while True:
            _response = self.list_evaluators(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("evaluators",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def batch_put_gateway_rate_limits(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limits: "capo_bedrock_agentcore_control.types.batch_put_limit_entries.BatchPutLimitEntries",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response.BatchPutGatewayRateLimitsResponse":
        """<p>Atomically creates or updates multiple rate limits for a gateway. The operation updates existing limits with matching keys and creates new limits for new keys. If the operation fails, the service applies no changes. Retry the request after resolving the issue.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            rate_limits: <p>The complete set of rate limits for this gateway. This operation replaces all existing rate limits in a single request. If the operation fails, no rate limits are changed.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request.BatchPutGatewayRateLimitsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_response.BatchPutGatewayRateLimitsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.batch_put_gateway_rate_limits

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.batch_put_gateway_rate_limits.batch_put_gateway_rate_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.batch_put_gateway_rate_limits_request.BatchPutGatewayRateLimitsRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limits": rate_limits,
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

    def create_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        dimension_keys: "capo_bedrock_agentcore_control.types.dimension_keys.DimensionKeys",
        entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        rate_limit_id: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response.CreateGatewayRateLimitResponse":
        """<p>Creates a rate limit for a gateway. Rate limits define throttling rules for each dimension that control request rates, token consumption rates, and concurrent connections through the gateway.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway to create the rate limit for.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            rate_limit_id: <p>An optional customer-defined identifier for the rate limit. If not provided, the system generates one.</p>
            description: <p>An optional human-readable description for this rate limit. If not provided, the rate limit is created without a description.</p>
            dimension_keys: <p>The ordered list of dimension key names that define the scope of this rate limit. Must be unique per gateway—no two rate limits can share the same dimension keys.</p>
            entries: <p>The rule entries that map dimension values to rate configurations.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request.CreateGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_rate_limit_response.CreateGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rate_limit.create_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_rate_limit_request.CreateGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "dimension_keys": dimension_keys,
            "entries": entries,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if rate_limit_id is not None:
            input_["rate_limit_id"] = rate_limit_id
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response.DeleteGatewayRateLimitResponse":
        """<p>Deletes a gateway rate limit.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request.DeleteGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_response.DeleteGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rate_limit.delete_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_rate_limit_request.DeleteGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response.GetGatewayRateLimitResponse":
        """<p>Retrieves information about a gateway rate limit.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request.GetGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_rate_limit_response.GetGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rate_limit.get_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_rate_limit_request.GetGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_rate_limits(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results.GatewayRateLimitMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token.GatewayRateLimitNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response.ListGatewayRateLimitsResponse":
        """<p>Lists all rate limits for a gateway. Results are paginated. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>The token to use to retrieve the next page of results. Use the value returned in a previous <code>ListGatewayRateLimits</code> response.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request.ListGatewayRateLimitsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateway_rate_limits_response.ListGatewayRateLimitsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rate_limits

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rate_limits.list_gateway_rate_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateway_rate_limits_request.ListGatewayRateLimitsRequest = {
            "gateway_identifier": gateway_identifier
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

    def iter_list_gateway_rate_limits(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_max_results.GatewayRateLimitMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_next_token.GatewayRateLimitNextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.gateway_rate_limit_detail.GatewayRateLimitDetail]":
        _token = next_token
        while True:
            _response = self.list_gateway_rate_limits(
                gateway_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rate_limits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_gateway_rate_limit(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rate_limit_id: "capo_bedrock_agentcore_control.types.gateway_rate_limit_id.GatewayRateLimitId",
        entries: "capo_bedrock_agentcore_control.types.limit_entries.LimitEntries",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rate_limit_description.GatewayRateLimitDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response.UpdateGatewayRateLimitResponse":
        """<p>Updates the entries of a gateway rate limit. The dimension keys are immutable after creation.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway.</p>
            rate_limit_id: <p>The unique identifier of the rate limit to update.</p>
            description: <p>The updated human-readable description for this rate limit.</p>
            entries: <p>The updated rule entries. The dimension keys are immutable after creation and cannot be changed.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request.UpdateGatewayRateLimitRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_rate_limit_response.UpdateGatewayRateLimitResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rate_limit

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rate_limit.update_gateway_rate_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_rate_limit_request.UpdateGatewayRateLimitRequest = {
            "gateway_identifier": gateway_identifier,
            "rate_limit_id": rate_limit_id,
            "entries": entries,
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_gateway(
        self,
        name: "capo_bedrock_agentcore_control.types.gateway_name.GatewayName",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        authorizer_type: "capo_bedrock_agentcore_control.types.authorizer_type.AuthorizerType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        protocol_type: Optional[
            "capo_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        interceptor_configurations: Optional[
            "capo_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
        ] = None,
        policy_engine_configuration: Optional[
            "capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
        ] = None,
        exception_level: Optional[
            "capo_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_response.CreateGatewayResponse":
        """<p>Creates a gateway for Amazon Bedrock Agent. A gateway serves as an integration point between your agent and external services.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the gateway. The name must be unique within your account.</p>
            description: <p>The description of the gateway.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the gateway to access Amazon Web Services services.</p>
            protocol_type: <p>The protocol type for the gateway.</p>
            protocol_configuration: <p>The configuration settings for the protocol specified in the <code>protocolType</code> parameter.</p>
            authorizer_type: <p>The type of authorizer to use for the gateway.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> <li> <p> <code>NONE</code> - No authorization</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the gateway. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt data associated with the gateway.</p>
            interceptor_configurations: <p>A list of configuration settings for a gateway interceptor. Gateway interceptors allow custom code to be invoked during gateway invocations.</p>
            policy_engine_configuration: <p>The policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>
            exception_level: <p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>
            tags: <p>A map of key-value pairs to associate with the gateway as metadata tags.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_gateway_request.CreateGatewayRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway.create_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_request.CreateGatewayRequest = {
            "name": name,
            "role_arn": role_arn,
            "authorizer_type": authorizer_type,
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if protocol_type is not None:
            input_["protocol_type"] = protocol_type
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if interceptor_configurations is not None:
            input_["interceptor_configurations"] = interceptor_configurations
        if policy_engine_configuration is not None:
            input_["policy_engine_configuration"] = policy_engine_configuration
        if exception_level is not None:
            input_["exception_level"] = exception_level
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_response.DeleteGatewayResponse":
        """<p>Deletes a gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_response.DeleteGatewayResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway.delete_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_request.DeleteGatewayRequest = {
            "gateway_identifier": gateway_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_response.GetGatewayResponse":
        """<p>Retrieves information about a specific Gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_gateway_request.GetGatewayRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_response.GetGatewayResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway.get_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_request.GetGatewayRequest = {
            "gateway_identifier": gateway_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateways(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_max_results.GatewayMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_next_token.GatewayNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateways_response.ListGatewaysResponse":
        """<p>Lists all gateways in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_gateways_request.ListGatewaysRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateways

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateways.list_gateways(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateways_request.ListGatewaysRequest = {}
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

    def iter_list_gateways(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_max_results.GatewayMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_next_token.GatewayNextToken"
        ] = None,
    ) -> (
        "Iterator[capo_bedrock_agentcore_control.types.gateway_summary.GatewaySummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_gateways(
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

    def update_gateway(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        name: "capo_bedrock_agentcore_control.types.gateway_name.GatewayName",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        authorizer_type: "capo_bedrock_agentcore_control.types.authorizer_type.AuthorizerType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_description.GatewayDescription"
        ] = None,
        protocol_type: Optional[
            "capo_bedrock_agentcore_control.types.gateway_protocol_type.GatewayProtocolType"
        ] = None,
        protocol_configuration: Optional[
            "capo_bedrock_agentcore_control.types.gateway_protocol_configuration.GatewayProtocolConfiguration"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        custom_transform_configuration: Optional[
            "capo_bedrock_agentcore_control.types.custom_transform_configuration.CustomTransformConfiguration"
        ] = None,
        interceptor_configurations: Optional[
            "capo_bedrock_agentcore_control.types.gateway_interceptor_configurations.GatewayInterceptorConfigurations"
        ] = None,
        policy_engine_configuration: Optional[
            "capo_bedrock_agentcore_control.types.gateway_policy_engine_configuration.GatewayPolicyEngineConfiguration"
        ] = None,
        exception_level: Optional[
            "capo_bedrock_agentcore_control.types.exception_level.ExceptionLevel"
        ] = None,
        waf_configuration: Optional[
            "capo_bedrock_agentcore_control.types.waf_configuration.WafConfiguration"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_response.UpdateGatewayResponse":
        """<p>Updates an existing gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to update.</p>
            name: <p>The name of the gateway. This name must be the same as the one when the gateway was created.</p>
            description: <p>The updated description for the gateway.</p>
            role_arn: <p>The updated IAM role ARN that provides permissions for the gateway.</p>
            protocol_type: <p>The updated protocol type for the gateway.</p>
            authorizer_type: <p>The updated authorizer type for the gateway.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the gateway.</p>
            kms_key_arn: <p>The updated ARN of the KMS key used to encrypt the gateway.</p>
            custom_transform_configuration: <p>The updated custom transformation configuration for the gateway. This configuration defines how the gateway transforms requests and responses.</p>
            interceptor_configurations: <p>The updated interceptor configurations for the gateway.</p>
            policy_engine_configuration: <p>The updated policy engine configuration for the gateway. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with a gateway, the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies.</p>
            exception_level: <p>The level of detail in error messages returned when invoking the gateway.</p> <ul> <li> <p>If the value is <code>DEBUG</code>, granular exception messages are returned to help a user debug the gateway.</p> </li> <li> <p>If the value is omitted, a generic error message is returned to the end user.</p> </li> </ul>
            waf_configuration: <p>The updated Amazon Web Services WAF configuration for the gateway.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_gateway_request.UpdateGatewayRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_response.UpdateGatewayResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway.update_gateway(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_request.UpdateGatewayRequest = {
            "gateway_identifier": gateway_identifier,
            "name": name,
            "role_arn": role_arn,
            "authorizer_type": authorizer_type,
        }
        if description is not None:
            input_["description"] = description
        if protocol_type is not None:
            input_["protocol_type"] = protocol_type
        if protocol_configuration is not None:
            input_["protocol_configuration"] = protocol_configuration
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if custom_transform_configuration is not None:
            input_["custom_transform_configuration"] = custom_transform_configuration
        if interceptor_configurations is not None:
            input_["interceptor_configurations"] = interceptor_configurations
        if policy_engine_configuration is not None:
            input_["policy_engine_configuration"] = policy_engine_configuration
        if exception_level is not None:
            input_["exception_level"] = exception_level
        if waf_configuration is not None:
            input_["waf_configuration"] = waf_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        priority: "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority",
        actions: "capo_bedrock_agentcore_control.types.actions.Actions",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        conditions: Optional[
            "capo_bedrock_agentcore_control.types.conditions.Conditions"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_rule_response.CreateGatewayRuleResponse":
        """<p>Creates a rule for a gateway. Rules define conditions and actions that control how requests are routed and processed through the gateway, including principal-based access control and path-based routing.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to create a rule for.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            priority: <p>The priority of the rule. Rules are evaluated in order of priority, with lower numbers evaluated first. Must be between 1 and 1,000,000.</p>
            conditions: <p>The conditions that must be met for the rule to apply. Conditions can match on principals (IAM ARNs) or request paths.</p>
            actions: <p>The actions to take when the rule conditions are met. Actions can route to a specific target or apply a configuration bundle override.</p>
            description: <p>The description of the gateway rule.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_gateway_rule_request.CreateGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_rule_response.CreateGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_rule.create_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_rule_request.CreateGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "priority": priority,
            "actions": actions,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if conditions is not None:
            input_["conditions"] = conditions
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_rule_response.DeleteGatewayRuleResponse":
        """<p>Deletes a gateway rule.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_rule_request.DeleteGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_rule_response.DeleteGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_rule.delete_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_rule_request.DeleteGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_rule_response.GetGatewayRuleResponse":
        """<p>Retrieves detailed information about a specific gateway rule.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_gateway_rule_request.GetGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_rule_response.GetGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_rule.get_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_rule_request.GetGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_rules(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_max_results.GatewayRuleMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_next_token.GatewayRuleNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateway_rules_response.ListGatewayRulesResponse":
        """<p>Lists all rules for a gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to list rules for.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>The pagination token from a previous request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_gateway_rules_request.ListGatewayRulesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateway_rules_response.ListGatewayRulesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rules

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_rules.list_gateway_rules(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateway_rules_request.ListGatewayRulesRequest = {
            "gateway_identifier": gateway_identifier
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

    def iter_list_gateway_rules(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_max_results.GatewayRuleMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_next_token.GatewayRuleNextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.gateway_rule_detail.GatewayRuleDetail]":
        _token = next_token
        while True:
            _response = self.list_gateway_rules(
                gateway_identifier,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("gateway_rules",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_gateway_rule(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        rule_id: "capo_bedrock_agentcore_control.types.gateway_rule_id.GatewayRuleId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        priority: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_priority.GatewayRulePriority"
        ] = None,
        conditions: Optional[
            "capo_bedrock_agentcore_control.types.conditions.Conditions"
        ] = None,
        actions: Optional[
            "capo_bedrock_agentcore_control.types.actions.Actions"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.gateway_rule_description.GatewayRuleDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_rule_response.UpdateGatewayRuleResponse":
        """<p>Updates a gateway rule's priority, conditions, actions, or description.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway containing the rule.</p>
            rule_id: <p>The unique identifier of the rule to update.</p>
            priority: <p>The updated priority of the rule.</p>
            conditions: <p>The updated conditions for the rule.</p>
            actions: <p>The updated actions for the rule.</p>
            description: <p>The updated description of the rule.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_gateway_rule_request.UpdateGatewayRuleRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_rule_response.UpdateGatewayRuleResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rule

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_rule.update_gateway_rule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_rule_request.UpdateGatewayRuleRequest = {
            "gateway_identifier": gateway_identifier,
            "rule_id": rule_id,
        }
        if priority is not None:
            input_["priority"] = priority
        if conditions is not None:
            input_["conditions"] = conditions
        if actions is not None:
            input_["actions"] = actions
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_gateway_target(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        target_configuration: "capo_bedrock_agentcore_control.types.target_configuration.TargetConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.target_name.TargetName"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.target_description.TargetDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        credential_provider_configurations: Optional[
            "capo_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"
        ] = None,
        metadata_configuration: Optional[
            "capo_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"
        ] = None,
        private_endpoint: Optional[
            "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
        ] = None,
        certificate_configurations: Optional[
            "capo_bedrock_agentcore_control.types.certificate_configuration_list.CertificateConfigurationList"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_gateway_target_response.CreateGatewayTargetResponse":
        """<p>Creates a target for a gateway. A target defines an endpoint that the gateway can connect to.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to create a target for.</p>
            name: <p>The name of the gateway target. The name must be unique within the gateway.</p>
            description: <p>The description of the gateway target.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            target_configuration: <p>The configuration settings for the target, including endpoint information and schema definitions.</p>
            credential_provider_configurations: <p>The credential provider configurations for the target. These configurations specify how the gateway authenticates with the target endpoint.</p>
            metadata_configuration: <p>Optional configuration for HTTP header and query parameter propagation to and from the gateway target.</p>
            private_endpoint: <p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>
            certificate_configurations: <p>The private certificate authority (CA) configurations for the gateway target. Use this to have the gateway trust a private CA when it establishes TLS connections to the target endpoint. Provide each certificate by reference to an Amazon S3 object or an Amazon Web Services Secrets Manager secret. You can specify only one certificate authority configuration in this list.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_gateway_target_request.CreateGatewayTargetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_gateway_target_response.CreateGatewayTargetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_target

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_gateway_target.create_gateway_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_gateway_target_request.CreateGatewayTargetRequest = {
            "gateway_identifier": gateway_identifier,
            "target_configuration": target_configuration,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if credential_provider_configurations is not None:
            input_["credential_provider_configurations"] = (
                credential_provider_configurations
            )
        if metadata_configuration is not None:
            input_["metadata_configuration"] = metadata_configuration
        if private_endpoint is not None:
            input_["private_endpoint"] = private_endpoint
        if certificate_configurations is not None:
            input_["certificate_configurations"] = certificate_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_gateway_target(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_gateway_target_response.DeleteGatewayTargetResponse":
        """<p>Deletes a gateway target.</p> <p>You cannot delete a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before deleting the target.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway associated with the target.</p>
            target_id: <p>The unique identifier of the gateway target to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_gateway_target_request.DeleteGatewayTargetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_gateway_target_response.DeleteGatewayTargetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_target

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_gateway_target.delete_gateway_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_gateway_target_request.DeleteGatewayTargetRequest = {
            "gateway_identifier": gateway_identifier,
            "target_id": target_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_gateway_target(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_gateway_target_response.GetGatewayTargetResponse":
        """<p>Retrieves information about a specific gateway target.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway that contains the target.</p>
            target_id: <p>The unique identifier of the target to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_gateway_target_request.GetGatewayTargetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_gateway_target_response.GetGatewayTargetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_target

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_gateway_target.get_gateway_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_gateway_target_request.GetGatewayTargetRequest = {
            "gateway_identifier": gateway_identifier,
            "target_id": target_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_gateway_targets(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.target_max_results.TargetMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.target_next_token.TargetNextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_gateway_targets_response.ListGatewayTargetsResponse":
        """<p>Lists all targets for a specific gateway.</p>

        Args:
            gateway_identifier: <p>The identifier of the gateway to list targets for.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_gateway_targets_request.ListGatewayTargetsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_gateway_targets_response.ListGatewayTargetsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_targets

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_gateway_targets.list_gateway_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_gateway_targets_request.ListGatewayTargetsRequest = {
            "gateway_identifier": gateway_identifier
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

    def iter_list_gateway_targets(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.target_max_results.TargetMaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.target_next_token.TargetNextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.target_summary.TargetSummary]":
        _token = next_token
        while True:
            _response = self.list_gateway_targets(
                gateway_identifier,
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

    def synchronize_gateway_targets(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        target_id_list: "capo_bedrock_agentcore_control.types.target_id_list.TargetIdList",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.synchronize_gateway_targets_response.SynchronizeGatewayTargetsResponse":
        """<p>Synchronizes the gateway targets by fetching the latest tool definitions from the target endpoints.</p> <p>You cannot synchronize a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before synchronizing.</p> <p>You cannot synchronize a target that has a static tool schema (<code>mcpToolSchema</code>) configured. Remove the static schema through an <code>UpdateGatewayTarget</code> call to enable dynamic tool synchronization.</p>

        Args:
            gateway_identifier: <p>The gateway Identifier.</p>
            target_id_list: <p>The target ID list.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.synchronize_gateway_targets_request.SynchronizeGatewayTargetsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.synchronize_gateway_targets_response.SynchronizeGatewayTargetsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.synchronize_gateway_targets

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.synchronize_gateway_targets.synchronize_gateway_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.synchronize_gateway_targets_request.SynchronizeGatewayTargetsRequest = {
            "gateway_identifier": gateway_identifier,
            "target_id_list": target_id_list,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_gateway_target(
        self,
        gateway_identifier: "capo_bedrock_agentcore_control.types.gateway_identifier.GatewayIdentifier",
        target_id: "capo_bedrock_agentcore_control.types.target_id.TargetId",
        target_configuration: "capo_bedrock_agentcore_control.types.target_configuration.TargetConfiguration",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.target_name.TargetName"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.target_description.TargetDescription"
        ] = None,
        credential_provider_configurations: Optional[
            "capo_bedrock_agentcore_control.types.credential_provider_configurations.CredentialProviderConfigurations"
        ] = None,
        metadata_configuration: Optional[
            "capo_bedrock_agentcore_control.types.metadata_configuration.MetadataConfiguration"
        ] = None,
        private_endpoint: Optional[
            "capo_bedrock_agentcore_control.types.private_endpoint.PrivateEndpoint"
        ] = None,
        certificate_configurations: Optional[
            "capo_bedrock_agentcore_control.types.certificate_configuration_list.CertificateConfigurationList"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_gateway_target_response.UpdateGatewayTargetResponse":
        """<p>Updates an existing gateway target.</p> <p>You cannot update a target that is in a pending authorization state (<code>CREATE_PENDING_AUTH</code>, <code>UPDATE_PENDING_AUTH</code>, or <code>SYNCHRONIZE_PENDING_AUTH</code>). Wait for the authorization to complete or fail before updating the target.</p>

        Args:
            gateway_identifier: <p>The unique identifier of the gateway associated with the target.</p>
            target_id: <p>The unique identifier of the gateway target to update.</p>
            name: <p>The updated name for the gateway target.</p>
            description: <p>The updated description for the gateway target.</p>
            credential_provider_configurations: <p>The updated credential provider configurations for the gateway target.</p>
            metadata_configuration: <p>Configuration for HTTP header and query parameter propagation to the gateway target.</p>
            private_endpoint: <p>The private endpoint configuration for the gateway target. Use this to connect the gateway to private resources in your VPC.</p>
            certificate_configurations: <p>The private certificate authority (CA) configurations for the gateway target. Use this to have the gateway trust a private CA when it establishes TLS connections to the target endpoint. Provide each certificate by reference to an Amazon S3 object or an Amazon Web Services Secrets Manager secret. You can specify only one certificate authority configuration in this list. To remove a previously configured certificate authority, omit this field on update.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_gateway_target_request.UpdateGatewayTargetRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_gateway_target_response.UpdateGatewayTargetResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_target

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_gateway_target.update_gateway_target(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_gateway_target_request.UpdateGatewayTargetRequest = {
            "gateway_identifier": gateway_identifier,
            "target_id": target_id,
            "target_configuration": target_configuration,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if credential_provider_configurations is not None:
            input_["credential_provider_configurations"] = (
                credential_provider_configurations
            )
        if metadata_configuration is not None:
            input_["metadata_configuration"] = metadata_configuration
        if private_endpoint is not None:
            input_["private_endpoint"] = private_endpoint
        if certificate_configurations is not None:
            input_["certificate_configurations"] = certificate_configurations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        target_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_harness_endpoint_response.CreateHarnessEndpointResponse":
        """<p>Operation to create a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness to create an endpoint for.</p>
            endpoint_name: <p>The name of the endpoint. Must start with a letter and contain only alphanumeric characters and underscores.</p>
            target_version: <p>The harness version that the endpoint points to and serves invocations from.</p>
            description: <p>A description of the endpoint.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            tags: <p>Tags to apply to the endpoint resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_harness_endpoint_request.CreateHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_harness_endpoint_response.CreateHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness_endpoint.create_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_harness_endpoint_request.CreateHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }
        if target_version is not None:
            input_["target_version"] = target_version
        if description is not None:
            input_["description"] = description
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

    def delete_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_harness_endpoint_response.DeleteHarnessEndpointResponse":
        """<p>Operation to delete a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_harness_endpoint_request.DeleteHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_harness_endpoint_response.DeleteHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness_endpoint.delete_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_harness_endpoint_request.DeleteHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
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

    def get_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_harness_endpoint_response.GetHarnessEndpointResponse":
        """<p>Operation to get a single harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_harness_endpoint_request.GetHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_harness_endpoint_response.GetHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness_endpoint.get_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_harness_endpoint_request.GetHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_harness_endpoints(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harness_endpoints_response.ListHarnessEndpointsResponse":
        """<p>Operation to list the endpoints of a harness.</p>

        Args:
            harness_id: <p>The ID of the harness whose endpoints are listed.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_harness_endpoints_request.ListHarnessEndpointsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_harness_endpoints_response.ListHarnessEndpointsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_endpoints

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_endpoints.list_harness_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_harness_endpoints_request.ListHarnessEndpointsRequest = {
            "harness_id": harness_id
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

    def iter_list_harness_endpoints(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.harness_endpoint.HarnessEndpoint]":
        _token = next_token
        while True:
            _response = self.list_harness_endpoints(
                harness_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_harness_endpoint(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        endpoint_name: "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        target_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_harness_endpoint_response.UpdateHarnessEndpointResponse":
        """<p>Operation to update a harness endpoint.</p>

        Args:
            harness_id: <p>The ID of the harness that the endpoint belongs to.</p>
            endpoint_name: <p>The name of the endpoint to update.</p>
            target_version: <p>The harness version that the endpoint points to. If not specified, the existing value is retained.</p>
            description: <p>A description of the endpoint. If not specified, the existing value is retained.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_harness_endpoint_request.UpdateHarnessEndpointRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_harness_endpoint_response.UpdateHarnessEndpointResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness_endpoint

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness_endpoint.update_harness_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_harness_endpoint_request.UpdateHarnessEndpointRequest = {
            "harness_id": harness_id,
            "endpoint_name": endpoint_name,
        }
        if target_version is not None:
            input_["target_version"] = target_version
        if description is not None:
            input_["description"] = description
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

    def create_harness(
        self,
        harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName",
        execution_role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        environment: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
        ] = None,
        environment_artifact: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        model: Optional[
            "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        memory: Optional[
            "capo_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
        ] = None,
        truncation: Optional[
            "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
        ] = None,
        hooks: Optional[
            "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse":
        """<p>Operation to create a harness.</p>

        Args:
            harness_name: <p>The name of the harness. Must start with a letter and contain only alphanumeric characters and underscores.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            execution_role_arn: <p>The ARN of the IAM role that the harness assumes when running. This role must have permissions for the services the agent needs to access, such as Amazon Bedrock for model invocation.</p>
            environment: <p>The compute environment configuration for the harness, including network and lifecycle settings.</p>
            environment_artifact: <p>The environment artifact for the harness, such as a custom container image containing additional dependencies.</p>
            environment_variables: <p>Environment variables to set in the harness runtime environment.</p>
            model: <p>The model configuration for the harness. Supports Amazon Bedrock, OpenAI, and Google Gemini model providers.</p>
            system_prompt: <p>The system prompt that defines the agent's behavior and instructions.</p>
            tools: <p>The tools available to the agent, such as remote MCP servers, AgentCore Gateway, AgentCore Browser, Code Interpreter, or inline functions.</p>
            skills: <p>The skills available to the agent. Skills are bundles of files that the agent can pull into its context on demand.</p>
            allowed_tools: <p>The tools that the agent is allowed to use. Supports glob patterns such as * for all tools, @builtin for all built-in tools, or @serverName/toolName for specific MCP server tools.</p>
            memory: <p>The AgentCore Memory configuration for persisting conversation context across sessions.</p>
            truncation: <p>The truncation configuration for managing conversation context when it exceeds model limits.</p>
            hooks: <p>The lifecycle hooks to run at defined points in the agent loop.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute per invocation.</p>
            max_tokens: <p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution per invocation.</p>
            tags: <p>Tags to apply to the harness resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_harness_response.CreateHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_harness.create_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_harness_request.CreateHarnessRequest = {
            "harness_name": harness_name,
            "execution_role_arn": execution_role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if environment is not None:
            input_["environment"] = environment
        if environment_artifact is not None:
            input_["environment_artifact"] = environment_artifact
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
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
        if memory is not None:
            input_["memory"] = memory
        if truncation is not None:
            input_["truncation"] = truncation
        if hooks is not None:
            input_["hooks"] = hooks
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        delete_managed_memory: Optional[bool] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse":
        """<p>Operation to delete a Harness.</p>

        Args:
            harness_id: <p>The ID of the harness to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            delete_managed_memory: <p>Whether to delete the managed memory on harness deletion. Default: true. If false, the memory is disassociated and becomes a regular customer-owned resource.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_harness_request.DeleteHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_harness_response.DeleteHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_harness.delete_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_harness_request.DeleteHarnessRequest = {
            "harness_id": harness_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if delete_managed_memory is not None:
            input_["delete_managed_memory"] = delete_managed_memory

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        harness_version: Optional[
            "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse":
        """<p>Operation to get a single harness.</p>

        Args:
            harness_id: <p>The ID of the harness to retrieve.</p>
            harness_version: <p>Specific version of the harness to retrieve. If omitted, returns the current Harness configuration, including its status.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_harness_request.GetHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_harness_response.GetHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_harness.get_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_harness_request.GetHarnessRequest = {
            "harness_id": harness_id
        }
        if harness_version is not None:
            input_["harness_version"] = harness_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_harnesses(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harnesses_response.ListHarnessesResponse":
        """<p>Operation to list harnesses.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_harnesses_request.ListHarnessesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_harnesses_response.ListHarnessesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harnesses

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harnesses.list_harnesses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_harnesses_request.ListHarnessesRequest = {}
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

    def iter_list_harnesses(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> (
        "Iterator[capo_bedrock_agentcore_control.types.harness_summary.HarnessSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_harnesses(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("harnesses",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_harness_versions(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_harness_versions_response.ListHarnessVersionsResponse":
        """<p>Operation to list the versions of a Harness.</p>

        Args:
            harness_id: <p>The ID of the harness whose versions are listed.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_harness_versions_request.ListHarnessVersionsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_harness_versions_response.ListHarnessVersionsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_versions

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_harness_versions.list_harness_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_harness_versions_request.ListHarnessVersionsRequest = {
            "harness_id": harness_id
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

    def iter_list_harness_versions(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.harness_version_summary.HarnessVersionSummary]":
        _token = next_token
        while True:
            _response = self.list_harness_versions(
                harness_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("harness_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_harness(
        self,
        harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        environment: Optional[
            "capo_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
        ] = None,
        environment_artifact: Optional[
            "capo_bedrock_agentcore_control.types.updated_harness_environment_artifact.UpdatedHarnessEnvironmentArtifact"
        ] = None,
        environment_variables: Optional[
            "capo_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"
        ] = None,
        model: Optional[
            "capo_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
        ] = None,
        system_prompt: Optional[
            "capo_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
        ] = None,
        tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_tools.HarnessTools"
        ] = None,
        skills: Optional[
            "capo_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
        ] = None,
        allowed_tools: Optional[
            "capo_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
        ] = None,
        memory: Optional[
            "capo_bedrock_agentcore_control.types.updated_harness_memory_configuration.UpdatedHarnessMemoryConfiguration"
        ] = None,
        truncation: Optional[
            "capo_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
        ] = None,
        hooks: Optional[
            "capo_bedrock_agentcore_control.types.harness_hooks.HarnessHooks"
        ] = None,
        max_iterations: Optional[int] = None,
        max_tokens: Optional[int] = None,
        timeout_seconds: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse":
        """<p>Operation to update a harness.</p>

        Args:
            harness_id: <p>The ID of the harness to update.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>
            execution_role_arn: <p>The ARN of the IAM role that the harness assumes when running. If not specified, the existing value is retained.</p>
            environment: <p>The compute environment configuration for the harness. If not specified, the existing value is retained.</p>
            environment_artifact: <p>The environment artifact for the harness. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>
            environment_variables: <p>Environment variables to set in the harness runtime environment. If specified, this replaces all existing environment variables. If not specified, the existing value is retained.</p>
            model: <p>The model configuration for the harness. If not specified, the existing value is retained.</p>
            system_prompt: <p>The system prompt that defines the agent's behavior. If not specified, the existing value is retained.</p>
            tools: <p>The tools available to the agent. If specified, this replaces all existing tools. If not specified, the existing value is retained.</p>
            skills: <p>The skills available to the agent. If specified, this replaces all existing skills. If not specified, the existing value is retained.</p>
            allowed_tools: <p>The tools that the agent is allowed to use. If specified, this replaces all existing allowed tools. If not specified, the existing value is retained.</p>
            memory: <p>The AgentCore Memory configuration. Use the optionalValue wrapper to set a new value, or set it to null to clear the existing configuration.</p>
            truncation: <p>The truncation configuration for managing conversation context. If not specified, the existing value is retained.</p>
            hooks: <p>The lifecycle hooks to run at defined points in the agent loop. If specified, this replaces all existing hooks. If not specified, the existing hooks are retained.</p>
            max_iterations: <p>The maximum number of iterations the agent loop can execute per invocation. If not specified, the existing value is retained.</p>
            max_tokens: <p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation. If not specified, the existing value is retained.</p>
            timeout_seconds: <p>The maximum duration in seconds for the agent loop execution per invocation. If not specified, the existing value is retained.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_harness_response.UpdateHarnessResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_harness.update_harness(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_harness_request.UpdateHarnessRequest = {
            "harness_id": harness_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if environment is not None:
            input_["environment"] = environment
        if environment_artifact is not None:
            input_["environment_artifact"] = environment_artifact
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
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
        if memory is not None:
            input_["memory"] = memory
        if truncation is not None:
            input_["truncation"] = truncation
        if hooks is not None:
            input_["hooks"] = hooks
        if max_iterations is not None:
            input_["max_iterations"] = max_iterations
        if max_tokens is not None:
            input_["max_tokens"] = max_tokens
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_memory(
        self,
        name: "capo_bedrock_agentcore_control.types.name.Name",
        event_expiry_duration: int,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        encryption_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "capo_bedrock_agentcore_control.types.memory_strategy_input_list.MemoryStrategyInputList"
        ] = None,
        indexed_keys: Optional[
            "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        namespace_keys: Optional[
            "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput":
        """<p>Creates a new Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            name: <p>The name of the memory. The name must be unique within your account.</p>
            description: <p>The description of the memory.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the memory data.</p>
            memory_execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that provides permissions for the memory to access Amazon Web Services services.</p>
            event_expiry_duration: <p>The duration after which memory events expire. Specified as an ISO 8601 duration.</p>
            memory_strategies: <p>The memory strategies to use for this memory. Strategies define how information is extracted, processed, and consolidated.</p>
            indexed_keys: <p>Metadata keys to index for filtering. Once declared, indexed keys cannot be removed.</p>
            namespace_keys: <p>The namespace variable key definitions with optional validation rules. Use these <code>namespaceKeys</code> in <code>namespaceTemplates</code> to control namespace hierarchy.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Memory. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_memory_output.CreateMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_memory.create_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_memory_input.CreateMemoryInput = {
            "name": name,
            "event_expiry_duration": event_expiry_duration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if indexed_keys is not None:
            input_["indexed_keys"] = indexed_keys
        if namespace_keys is not None:
            input_["namespace_keys"] = namespace_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_memory(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        view: Optional[
            "capo_bedrock_agentcore_control.types.memory_view.MemoryView"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput":
        """<p>Retrieve an existing Amazon Bedrock AgentCore Memory resource.</p>

        Args:
            memory_id: <p>The unique identifier of the memory to retrieve.</p>
            view: <p>The level of detail to return for the memory.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_memory_output.GetMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_memory.get_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_memory_input.GetMemoryInput = {
            "memory_id": memory_id
        }
        if view is not None:
            input_["view"] = view

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_memory(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        event_expiry_duration: Optional[int] = None,
        memory_execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.arn.Arn"
        ] = None,
        memory_strategies: Optional[
            "capo_bedrock_agentcore_control.types.modify_memory_strategies.ModifyMemoryStrategies"
        ] = None,
        add_indexed_keys: Optional[
            "capo_bedrock_agentcore_control.types.indexed_keys_list.IndexedKeysList"
        ] = None,
        namespace_keys: Optional[
            "capo_bedrock_agentcore_control.types.namespace_keys_list.NamespaceKeysList"
        ] = None,
        stream_delivery_resources: Optional[
            "capo_bedrock_agentcore_control.types.stream_delivery_resources.StreamDeliveryResources"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput":
        """<p>Update an Amazon Bedrock AgentCore Memory resource memory.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>
            memory_id: <p>The unique identifier of the memory to update.</p>
            description: <p>The updated description of the AgentCore Memory resource.</p>
            event_expiry_duration: <p>The number of days after which memory events will expire, between 7 and 365 days.</p>
            memory_execution_role_arn: <p>The ARN of the IAM role that provides permissions for the AgentCore Memory resource.</p>
            memory_strategies: <p>The memory strategies to add, modify, or delete.</p>
            add_indexed_keys: <p>Additional metadata keys to index. Previously indexed keys cannot be removed.</p>
            namespace_keys: <p>The namespace variable key definitions with validation rules for this memory. This value fully replaces the existing set — any key you omit is removed. Any referenced <code>namespaceKey</code> omission will throw ValidationException.</p>
            stream_delivery_resources: <p>Configuration for streaming memory record data to external resources.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_memory_output.UpdateMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_memory.update_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_memory_input.UpdateMemoryInput = {
            "memory_id": memory_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if event_expiry_duration is not None:
            input_["event_expiry_duration"] = event_expiry_duration
        if memory_execution_role_arn is not None:
            input_["memory_execution_role_arn"] = memory_execution_role_arn
        if memory_strategies is not None:
            input_["memory_strategies"] = memory_strategies
        if add_indexed_keys is not None:
            input_["add_indexed_keys"] = add_indexed_keys
        if namespace_keys is not None:
            input_["namespace_keys"] = namespace_keys
        if stream_delivery_resources is not None:
            input_["stream_delivery_resources"] = stream_delivery_resources

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_memory(
        self,
        memory_id: "capo_bedrock_agentcore_control.types.memory_id.MemoryId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.non_empty_string.NonEmptyString"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput":
        """<p>Deletes an Amazon Bedrock AgentCore Memory resource. When you delete a memory resource, it is permanently removed.</p>

        Args:
            client_token: <p>A client token is used for keeping track of idempotent requests. It can contain a session id which can be around 250 chars, combined with a unique AWS identifier.</p>
            memory_id: <p>The unique identifier of the memory to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_memory_output.DeleteMemoryOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_memory.delete_memory(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_memory_input.DeleteMemoryInput = {
            "memory_id": memory_id
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

    def list_memories(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput":
        """<p>Lists the available Amazon Bedrock AgentCore Memory resources in the current Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. The default value is 10. The maximum value is 50.</p>
            next_token: <p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_exception.ServiceException: <p>An internal error occurred.</p>
            capo_bedrock_agentcore_control.errors.throttled_exception.ThrottledException: <p>API rate limit has been exceeded.</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_memories_output.ListMemoriesOutput"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_memories.list_memories(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_memories_input.ListMemoriesInput = {}
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

    def iter_list_memories(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[int] = None,
        next_token: Optional[str] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.memory_summary.MemorySummary]":
        _token = next_token
        while True:
            _response = self.list_memories(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("memories",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_oauth2_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "capo_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse":
        """<p>Creates a new OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider. The name must be unique within your account.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider. This specifies which OAuth2 implementation to use.</p>
            oauth2_provider_config_input: <p>The configuration settings for the OAuth2 provider, including client ID, client secret, and other vendor-specific settings.</p>
            tags: <p>A map of tag keys and values to assign to the OAuth2 credential provider. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Exception thrown when a resource limit is exceeded.</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_response.CreateOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_oauth2_credential_provider.create_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_oauth2_credential_provider_request.CreateOauth2CredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "oauth2_provider_config_input": oauth2_provider_config_input,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_oauth2_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse":
        """<p>Retrieves information about an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_response.GetOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_oauth2_credential_provider.get_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_oauth2_credential_provider_request.GetOauth2CredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_oauth2_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.credential_provider_vendor_type.CredentialProviderVendorType",
        oauth2_provider_config_input: "capo_bedrock_agentcore_control.types.oauth2_provider_config_input.Oauth2ProviderConfigInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse":
        """<p>Updates an existing OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to update.</p>
            credential_provider_vendor: <p>The vendor of the OAuth2 credential provider.</p>
            oauth2_provider_config_input: <p>The configuration input for the OAuth2 provider.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_response.UpdateOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_oauth2_credential_provider.update_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_oauth2_credential_provider_request.UpdateOauth2CredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "oauth2_provider_config_input": oauth2_provider_config_input,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_oauth2_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse":
        """<p>Deletes an OAuth2 credential provider.</p>

        Args:
            name: <p>The name of the OAuth2 credential provider to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_response.DeleteOauth2CredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_oauth2_credential_provider.delete_oauth2_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_oauth2_credential_provider_request.DeleteOauth2CredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_oauth2_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse":
        """<p>Lists all OAuth2 credential providers in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_response.ListOauth2CredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_oauth2_credential_providers.list_oauth2_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_oauth2_credential_providers_request.ListOauth2CredentialProvidersRequest = {}
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

    def iter_list_oauth2_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.oauth2_credential_provider_item.Oauth2CredentialProviderItem]":
        _token = next_token
        while True:
            _response = self.list_oauth2_credential_providers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("credential_providers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_online_evaluation_config(
        self,
        online_evaluation_config_name: "capo_bedrock_agentcore_control.types.evaluation_config_name.EvaluationConfigName",
        rule: "capo_bedrock_agentcore_control.types.rule.Rule",
        data_source_config: "capo_bedrock_agentcore_control.types.data_source_config.DataSourceConfig",
        evaluation_execution_role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        enable_on_create: bool,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
        ] = None,
        evaluators: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
        ] = None,
        insights: Optional[
            "capo_bedrock_agentcore_control.types.insight_list.InsightList"
        ] = None,
        clustering_config: Optional[
            "capo_bedrock_agentcore_control.types.clustering_config.ClusteringConfig"
        ] = None,
        output_config: Optional[
            "capo_bedrock_agentcore_control.types.output_config.OutputConfig"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_online_evaluation_config_response.CreateOnlineEvaluationConfigResponse":
        """<p> Creates an online evaluation configuration for continuous monitoring of agent performance. Online evaluation automatically samples live traffic from CloudWatch logs at specified rates and applies evaluators to assess agent quality in production. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            online_evaluation_config_name: <p> The name of the online evaluation configuration. Must be unique within your account. </p>
            description: <p> The description of the online evaluation configuration that explains its monitoring purpose and scope. </p>
            rule: <p> The evaluation rule that defines sampling configuration, filters, and session detection settings for the online evaluation. </p>
            data_source_config: <p> The data source configuration that specifies CloudWatch log groups and service names to monitor for agent traces. </p>
            evaluators: <p> The list of evaluators to apply during online evaluation. Can include both built-in evaluators and custom evaluators created with <code>CreateEvaluator</code>. </p>
            insights: <p>The list of insight types to run against agent sessions.</p>
            clustering_config: <p>Configuration for periodic batch evaluation clustering of insight results.</p>
            evaluation_execution_role_arn: <p> The Amazon Resource Name (ARN) of the IAM role that grants permissions to read from CloudWatch logs, write evaluation results, and invoke Amazon Bedrock models for evaluation. If the configuration references evaluators encrypted with a customer managed KMS key, this role must also have <code>kms:Decrypt</code> permission on the KMS key. The service validates this permission at configuration creation time. For more information, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/evaluations-encryption.html">Encryption at rest for AgentCore Evaluations</a>. </p>
            enable_on_create: <p> Whether to enable the online evaluation configuration immediately upon creation. If true, evaluation begins automatically. </p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Online Evaluation Config. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_online_evaluation_config_request.CreateOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_online_evaluation_config_response.CreateOnlineEvaluationConfigResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_online_evaluation_config

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_online_evaluation_config.create_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_online_evaluation_config_request.CreateOnlineEvaluationConfigRequest = {
            "online_evaluation_config_name": online_evaluation_config_name,
            "rule": rule,
            "data_source_config": data_source_config,
            "evaluation_execution_role_arn": evaluation_execution_role_arn,
            "enable_on_create": enable_on_create,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if evaluators is not None:
            input_["evaluators"] = evaluators
        if insights is not None:
            input_["insights"] = insights
        if clustering_config is not None:
            input_["clustering_config"] = clustering_config
        if output_config is not None:
            input_["output_config"] = output_config
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_online_evaluation_config(
        self,
        online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_online_evaluation_config_response.GetOnlineEvaluationConfigResponse":
        """<p> Retrieves detailed information about an online evaluation configuration, including its rules, data sources, evaluators, and execution status. </p>

        Args:
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to retrieve. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_online_evaluation_config_request.GetOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_online_evaluation_config_response.GetOnlineEvaluationConfigResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_online_evaluation_config

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_online_evaluation_config.get_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_online_evaluation_config_request.GetOnlineEvaluationConfigRequest = {
            "online_evaluation_config_id": online_evaluation_config_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_online_evaluation_config(
        self,
        online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.evaluation_config_description.EvaluationConfigDescription"
        ] = None,
        rule: Optional["capo_bedrock_agentcore_control.types.rule.Rule"] = None,
        data_source_config: Optional[
            "capo_bedrock_agentcore_control.types.data_source_config.DataSourceConfig"
        ] = None,
        evaluators: Optional[
            "capo_bedrock_agentcore_control.types.evaluator_list.EvaluatorList"
        ] = None,
        insights: Optional[
            "capo_bedrock_agentcore_control.types.insight_list.InsightList"
        ] = None,
        clustering_config: Optional[
            "capo_bedrock_agentcore_control.types.clustering_config.ClusteringConfig"
        ] = None,
        output_config: Optional[
            "capo_bedrock_agentcore_control.types.output_config.OutputConfig"
        ] = None,
        evaluation_execution_role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        execution_status: Optional[
            "capo_bedrock_agentcore_control.types.online_evaluation_execution_status.OnlineEvaluationExecutionStatus"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_online_evaluation_config_response.UpdateOnlineEvaluationConfigResponse":
        """<p> Updates an online evaluation configuration's settings, including rules, data sources, evaluators, and execution status. Changes take effect immediately for ongoing evaluations. </p>

        Args:
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to update. </p>
            description: <p> The updated description of the online evaluation configuration. </p>
            rule: <p> The updated evaluation rule containing sampling configuration, filters, and session settings. </p>
            data_source_config: <p> The updated data source configuration specifying CloudWatch log groups and service names to monitor. </p>
            evaluators: <p> The updated list of evaluators to apply during online evaluation. </p>
            insights: <p>The updated list of insight types to run against agent sessions.</p>
            clustering_config: <p>The updated clustering configuration for periodic batch evaluation.</p>
            evaluation_execution_role_arn: <p> The updated Amazon Resource Name (ARN) of the IAM role used for evaluation execution. </p>
            execution_status: <p> The updated execution status to enable or disable the online evaluation. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_online_evaluation_config_request.UpdateOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_online_evaluation_config_response.UpdateOnlineEvaluationConfigResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_online_evaluation_config

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_online_evaluation_config.update_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_online_evaluation_config_request.UpdateOnlineEvaluationConfigRequest = {
            "online_evaluation_config_id": online_evaluation_config_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if rule is not None:
            input_["rule"] = rule
        if data_source_config is not None:
            input_["data_source_config"] = data_source_config
        if evaluators is not None:
            input_["evaluators"] = evaluators
        if insights is not None:
            input_["insights"] = insights
        if clustering_config is not None:
            input_["clustering_config"] = clustering_config
        if output_config is not None:
            input_["output_config"] = output_config
        if evaluation_execution_role_arn is not None:
            input_["evaluation_execution_role_arn"] = evaluation_execution_role_arn
        if execution_status is not None:
            input_["execution_status"] = execution_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_online_evaluation_config(
        self,
        online_evaluation_config_id: "capo_bedrock_agentcore_control.types.online_evaluation_config_id.OnlineEvaluationConfigId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_online_evaluation_config_response.DeleteOnlineEvaluationConfigResponse":
        """<p> Deletes an online evaluation configuration and stops any ongoing evaluation processes associated with it. </p>

        Args:
            online_evaluation_config_id: <p> The unique identifier of the online evaluation configuration to delete. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_online_evaluation_config_request.DeleteOnlineEvaluationConfigRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_online_evaluation_config_response.DeleteOnlineEvaluationConfigResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_online_evaluation_config

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_online_evaluation_config.delete_online_evaluation_config(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_online_evaluation_config_request.DeleteOnlineEvaluationConfigRequest = {
            "online_evaluation_config_id": online_evaluation_config_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_online_evaluation_configs(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_online_evaluation_configs_response.ListOnlineEvaluationConfigsResponse":
        """<p> Lists all online evaluation configurations in the account, providing summary information about each configuration's status and settings. </p>

        Args:
            next_token: <p> The pagination token from a previous request to retrieve the next page of results. </p>
            max_results: <p> The maximum number of online evaluation configurations to return in a single response. </p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_online_evaluation_configs_request.ListOnlineEvaluationConfigsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_online_evaluation_configs_response.ListOnlineEvaluationConfigsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_online_evaluation_configs

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_online_evaluation_configs.list_online_evaluation_configs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_online_evaluation_configs_request.ListOnlineEvaluationConfigsRequest = {}
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

    def iter_list_online_evaluation_configs(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.online_evaluation_config_summary.OnlineEvaluationConfigSummary]":
        _token = next_token
        while True:
            _response = self.list_online_evaluation_configs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("online_evaluation_configs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_payment_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType",
        provider_configuration_input: "capo_bedrock_agentcore_control.types.payment_provider_configuration_input.PaymentProviderConfigurationInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_payment_credential_provider_response.CreatePaymentCredentialProviderResponse":
        """<p>Creates a new payment credential provider for storing authentication credentials used by payment connectors to communicate with external payment providers.</p>

        Args:
            name: <p>Unique name for the payment credential provider.</p>
            credential_provider_vendor: <p>The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).</p>
            provider_configuration_input: <p>Configuration specific to the vendor, including API credentials.</p>
            tags: <p>Optional tags for resource organization.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Exception thrown when a resource limit is exceeded.</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_payment_credential_provider_response.CreatePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_credential_provider.create_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_payment_credential_provider_request.CreatePaymentCredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "provider_configuration_input": provider_configuration_input,
        }
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_payment_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_payment_credential_provider_response.GetPaymentCredentialProviderResponse":
        """<p>Retrieves information about a specific payment credential provider.</p>

        Args:
            name: <p>The name of the payment credential provider to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_payment_credential_provider_request.GetPaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_payment_credential_provider_response.GetPaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_credential_provider.get_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_payment_credential_provider_request.GetPaymentCredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_payment_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        credential_provider_vendor: "capo_bedrock_agentcore_control.types.payment_credential_provider_vendor_type.PaymentCredentialProviderVendorType",
        provider_configuration_input: "capo_bedrock_agentcore_control.types.payment_provider_configuration_input.PaymentProviderConfigurationInput",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_payment_credential_provider_response.UpdatePaymentCredentialProviderResponse":
        """<p>Updates an existing payment credential provider with new authentication credentials.</p>

        Args:
            name: <p>The name of the payment credential provider to update.</p>
            credential_provider_vendor: <p>The vendor type for the payment credential provider (e.g., CoinbaseCDP, StripePrivy).</p>
            provider_configuration_input: <p>Configuration specific to the vendor, including API credentials.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.decryption_failure.DecryptionFailure: <p>Exception thrown when decryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.encryption_failure.EncryptionFailure: <p>Exception thrown when encryption of a secret fails.</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_payment_credential_provider_response.UpdatePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_credential_provider.update_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_payment_credential_provider_request.UpdatePaymentCredentialProviderRequest = {
            "name": name,
            "credential_provider_vendor": credential_provider_vendor,
            "provider_configuration_input": provider_configuration_input,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_payment_credential_provider(
        self,
        name: "capo_bedrock_agentcore_control.types.credential_provider_name.CredentialProviderName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response.DeletePaymentCredentialProviderResponse":
        """<p>Deletes a payment credential provider and its associated stored credentials.</p>

        Args:
            name: <p>The name of the payment credential provider to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request.DeletePaymentCredentialProviderRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_payment_credential_provider_response.DeletePaymentCredentialProviderResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_credential_provider

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_credential_provider.delete_payment_credential_provider(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_payment_credential_provider_request.DeletePaymentCredentialProviderRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_payment_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_payment_credential_providers_response.ListPaymentCredentialProvidersResponse":
        """<p>Lists all payment credential providers in the account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_payment_credential_providers_request.ListPaymentCredentialProvidersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_payment_credential_providers_response.ListPaymentCredentialProvidersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_credential_providers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_credential_providers.list_payment_credential_providers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_payment_credential_providers_request.ListPaymentCredentialProvidersRequest = {}
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

    def iter_list_payment_credential_providers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.payment_credential_provider_item.PaymentCredentialProviderItem]":
        _token = next_token
        while True:
            _response = self.list_payment_credential_providers(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("credential_providers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_payment_manager(
        self,
        name: "capo_bedrock_agentcore_control.types.payment_manager_name.PaymentManagerName",
        authorizer_type: "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType",
        role_arn: "capo_bedrock_agentcore_control.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse":
        """<p>Creates a new payment manager in your Amazon Web Services account. A payment manager serves as the top-level resource for managing payment processing capabilities, including payment connectors that integrate with supported payment providers.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the payment manager.</p>
            description: <p>A description of the payment manager.</p>
            authorizer_type: <p>The type of authorizer to use for the payment manager.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the payment manager.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the payment manager assumes to access resources on your behalf.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            tags: <p>A map of tag keys and values to assign to the payment manager.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer managed KMS key to use for encrypting sensitive payment manager data at rest. If you don't specify a key, the data is encrypted with an Amazon Web Services owned key.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_payment_manager_response.CreatePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_manager.create_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_payment_manager_request.CreatePaymentManagerRequest = {
            "name": name,
            "authorizer_type": authorizer_type,
            "role_arn": role_arn,
        }
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_payment_manager(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse":
        """<p>Retrieves information about a specific payment manager.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_payment_manager_response.GetPaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_manager.get_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_payment_manager_request.GetPaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_payment_manager(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        authorizer_type: Optional[
            "capo_bedrock_agentcore_control.types.payments_authorizer_type.PaymentsAuthorizerType"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        role_arn: Optional[
            "capo_bedrock_agentcore_control.types.role_arn.RoleArn"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        kms_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse":
        """<p>Updates an existing payment manager. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to update.</p>
            description: <p>The updated description of the payment manager.</p>
            authorizer_type: <p>The updated authorizer type for the payment manager.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the payment manager.</p>
            role_arn: <p>The updated Amazon Resource Name (ARN) of the IAM role for the payment manager.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            kms_key_arn: <p>The updated Amazon Resource Name (ARN) of the customer managed KMS key used to encrypt sensitive payment manager data at rest.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_payment_manager_response.UpdatePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_manager.update_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_payment_manager_request.UpdatePaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
        }
        if description is not None:
            input_["description"] = description
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_payment_manager(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse":
        """<p>Deletes a payment manager. All payment connectors associated with the payment manager must be deleted before the payment manager can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_payment_manager_response.DeletePaymentManagerResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_manager.delete_payment_manager(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_payment_manager_request.DeletePaymentManagerRequest = {
            "payment_manager_id": payment_manager_id
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

    def list_payment_managers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse":
        """<p>Lists all payment managers in the account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_payment_managers_response.ListPaymentManagersResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_managers.list_payment_managers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_payment_managers_request.ListPaymentManagersRequest = {}
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

    def iter_list_payment_managers(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.payment_manager_summary.PaymentManagerSummary]":
        _token = next_token
        while True:
            _response = self.list_payment_managers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("payment_managers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_payment_connector(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        name: "capo_bedrock_agentcore_control.types.payment_connector_name.PaymentConnectorName",
        type: "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType",
        credential_provider_configurations: "capo_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        provision_mode: Optional[
            "capo_bedrock_agentcore_control.types.payment_connector_provision_mode.PaymentConnectorProvisionMode"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_payment_connector_response.CreatePaymentConnectorResponse":
        """<p>Creates a new payment connector for a payment manager. A payment connector integrates with a supported payment provider to enable payment processing capabilities.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager to create the connector for.</p>
            name: <p>The name of the payment connector.</p>
            description: <p>A description of the payment connector.</p>
            type: <p>The type of payment connector, which determines the payment provider integration.</p>
            credential_provider_configurations: <p>The credential provider configurations for the payment connector. These configurations specify how the connector authenticates with the payment provider.</p>
            provision_mode: <p>The provision mode for creating the payment connector. If you don't specify a value, the default is <code>MANUAL</code>.</p> <ul> <li> <p> <code>MANUAL</code> - You provide the credential provider configurations directly.</p> </li> <li> <p> <code>QUICK_CREATE</code> - The service orchestrates OAuth consent and provisions the credential provider for you.</p> </li> </ul>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.subscription_required_exception.SubscriptionRequiredException: <p>The request failed because it requires an active Amazon Web Services Marketplace subscription that is not present. Subscribe to the required product in Amazon Web Services Marketplace and try again.</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_payment_connector_request.CreatePaymentConnectorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_payment_connector_response.CreatePaymentConnectorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_connector

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_payment_connector.create_payment_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_payment_connector_request.CreatePaymentConnectorRequest = {
            "payment_manager_id": payment_manager_id,
            "name": name,
            "type": type,
            "credential_provider_configurations": credential_provider_configurations,
        }
        if description is not None:
            input_["description"] = description
        if provision_mode is not None:
            input_["provision_mode"] = provision_mode
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

    def get_payment_connector(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        payment_connector_id: "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_payment_connector_response.GetPaymentConnectorResponse":
        """<p>Retrieves information about a specific payment connector.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the parent payment manager.</p>
            payment_connector_id: <p>The unique identifier of the payment connector to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_payment_connector_request.GetPaymentConnectorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_payment_connector_response.GetPaymentConnectorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_connector

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_payment_connector.get_payment_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_payment_connector_request.GetPaymentConnectorRequest = {
            "payment_manager_id": payment_manager_id,
            "payment_connector_id": payment_connector_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_payment_connector(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        payment_connector_id: "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.payments_description.PaymentsDescription"
        ] = None,
        type: Optional[
            "capo_bedrock_agentcore_control.types.payment_connector_type.PaymentConnectorType"
        ] = None,
        credential_provider_configurations: Optional[
            "capo_bedrock_agentcore_control.types.credentials_provider_configurations.CredentialsProviderConfigurations"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_payment_connector_response.UpdatePaymentConnectorResponse":
        """<p>Updates an existing payment connector. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the parent payment manager.</p>
            payment_connector_id: <p>The unique identifier of the payment connector to update.</p>
            description: <p>The updated description of the payment connector.</p>
            type: <p>The updated type of the payment connector.</p>
            credential_provider_configurations: <p>The updated credential provider configurations for the payment connector.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.subscription_required_exception.SubscriptionRequiredException: <p>The request failed because it requires an active Amazon Web Services Marketplace subscription that is not present. Subscribe to the required product in Amazon Web Services Marketplace and try again.</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_payment_connector_request.UpdatePaymentConnectorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_payment_connector_response.UpdatePaymentConnectorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_connector

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_payment_connector.update_payment_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_payment_connector_request.UpdatePaymentConnectorRequest = {
            "payment_manager_id": payment_manager_id,
            "payment_connector_id": payment_connector_id,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if credential_provider_configurations is not None:
            input_["credential_provider_configurations"] = (
                credential_provider_configurations
            )
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

    def delete_payment_connector(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        payment_connector_id: "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_payment_connector_response.DeletePaymentConnectorResponse":
        """<p>Deletes a payment connector.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the parent payment manager.</p>
            payment_connector_id: <p>The unique identifier of the payment connector to delete.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_payment_connector_request.DeletePaymentConnectorRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_payment_connector_response.DeletePaymentConnectorResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_connector

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_payment_connector.delete_payment_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_payment_connector_request.DeletePaymentConnectorRequest = {
            "payment_manager_id": payment_manager_id,
            "payment_connector_id": payment_connector_id,
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

    def list_payment_connectors(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_payment_connectors_response.ListPaymentConnectorsResponse":
        """<p>Lists all payment connectors for a specified payment manager.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the payment manager whose connectors to list.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_payment_connectors_request.ListPaymentConnectorsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_payment_connectors_response.ListPaymentConnectorsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_connectors

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_payment_connectors.list_payment_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_payment_connectors_request.ListPaymentConnectorsRequest = {
            "payment_manager_id": payment_manager_id
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

    def iter_list_payment_connectors(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.payment_connector_summary.PaymentConnectorSummary]":
        _token = next_token
        while True:
            _response = self.list_payment_connectors(
                payment_manager_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("payment_connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def rotate_payment_connector_credentials(
        self,
        payment_manager_id: "capo_bedrock_agentcore_control.types.payment_manager_id.PaymentManagerId",
        payment_connector_id: "capo_bedrock_agentcore_control.types.payment_connector_id.PaymentConnectorId",
        credentials_to_rotate: "capo_bedrock_agentcore_control.types.credential_rotation_config.CredentialRotationConfig",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.rotate_payment_connector_credentials_response.RotatePaymentConnectorCredentialsResponse":
        """<p>Replaces the service-managed credentials of a payment connector with newly issued credentials.</p> <p>Use this operation only for payment connectors with a <code>provisionMode</code> of <code>QUICK_CREATE</code>. For payment connectors with a <code>provisionMode</code> of <code>MANUAL</code>, call <code>UpdatePaymentCredentialProvider</code> instead after rotating credentials with the payment provider directly.</p> <p>The rotation finishes before the response is returned, and only one rotation runs at a time for a given payment connector. When it succeeds, the new credential is in effect and the payment connector stays in the <code>READY</code> state. When it fails, an error is returned, the payment connector and its existing credential are left unchanged, and you can retry the request.</p> <p>Rotation replaces the credential on the connector's credential provider, so every payment connector that uses that provider is affected. Replace any copy of the previous credential that you use outside AgentCore.</p>

        Args:
            payment_manager_id: <p>The unique identifier of the parent payment manager.</p>
            payment_connector_id: <p>The unique identifier of the payment connector whose credentials you want to rotate.</p>
            credentials_to_rotate: <p>The credentials to rotate. Specify the member that matches the payment connector's <code>type</code>. Each credential that you select is rotated independently.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.rotate_payment_connector_credentials_request.RotatePaymentConnectorCredentialsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.rotate_payment_connector_credentials_response.RotatePaymentConnectorCredentialsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.rotate_payment_connector_credentials

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.rotate_payment_connector_credentials.rotate_payment_connector_credentials(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.rotate_payment_connector_credentials_request.RotatePaymentConnectorCredentialsRequest = {
            "payment_manager_id": payment_manager_id,
            "payment_connector_id": payment_connector_id,
            "credentials_to_rotate": credentials_to_rotate,
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

    def create_policy_engine(
        self,
        name: "capo_bedrock_agentcore_control.types.policy_engine_name.PolicyEngineName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        encryption_key_arn: Optional[
            "capo_bedrock_agentcore_control.types.kms_key_arn.KmsKeyArn"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_policy_engine_response.CreatePolicyEngineResponse":
        """<p>Creates a new policy engine within the AgentCore Policy system. A policy engine is a collection of policies that evaluates and authorizes agent tool calls. When associated with Gateways (each Gateway can be associated with at most one policy engine, but multiple Gateways can be associated with the same engine), the policy engine intercepts all agent requests and determines whether to allow or deny each action based on the defined policies. This is an asynchronous operation. Use the <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicyEngine.html">GetPolicyEngine</a> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            name: <p>The customer-assigned immutable name for the policy engine. This name identifies the policy engine and cannot be changed after creation.</p>
            description: <p>A human-readable description of the policy engine's purpose and scope (1-4,096 characters). This helps administrators understand the policy engine's role in the overall governance strategy. Document which Gateway this engine will be associated with, what types of tools or workflows it governs, and the team or service responsible for maintaining it. Clear descriptions are essential when managing multiple policy engines across different services or environments.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy engine.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used to encrypt the policy engine data.</p>
            tags: <p>A map of tag keys and values to assign to an AgentCore Policy. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_policy_engine_request.CreatePolicyEngineRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_policy_engine_response.CreatePolicyEngineResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy_engine

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy_engine.create_policy_engine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_policy_engine_request.CreatePolicyEngineRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if encryption_key_arn is not None:
            input_["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy_engine(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_policy_engine_response.GetPolicyEngineResponse":
        """<p>Retrieves detailed information about a specific policy engine within the AgentCore Policy system. This operation returns the complete policy engine configuration, metadata, and current status, allowing administrators to review and manage policy engine settings.</p>

        Args:
            policy_engine_id: <p>The unique identifier of the policy engine to be retrieved. This must be a valid policy engine ID that exists within the account.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_policy_engine_request.GetPolicyEngineRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_policy_engine_response.GetPolicyEngineResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_engine

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_engine.get_policy_engine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_policy_engine_request.GetPolicyEngineRequest = {
            "policy_engine_id": policy_engine_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_policy_engine(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_policy_engine_response.UpdatePolicyEngineResponse":
        """<p>Updates an existing policy engine within the AgentCore Policy system. This operation allows modification of the policy engine description while maintaining its identity. This is an asynchronous operation. Use the <code>GetPolicyEngine</code> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            policy_engine_id: <p>The unique identifier of the policy engine to be updated.</p>
            description: <p>The new description for the policy engine.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_policy_engine_request.UpdatePolicyEngineRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_policy_engine_response.UpdatePolicyEngineResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy_engine

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy_engine.update_policy_engine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_policy_engine_request.UpdatePolicyEngineRequest = {
            "policy_engine_id": policy_engine_id
        }
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy_engine(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_policy_engine_response.DeletePolicyEngineResponse":
        """<p>Deletes an existing policy engine from the AgentCore Policy system. The policy engine must not have any associated policies before deletion. Once deleted, the policy engine and all its configurations become unavailable for policy management and evaluation. This is an asynchronous operation. Use the <code>GetPolicyEngine</code> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            policy_engine_id: <p>The unique identifier of the policy engine to be deleted. This must be a valid policy engine ID that exists within the account.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_policy_engine_request.DeletePolicyEngineRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_policy_engine_response.DeletePolicyEngineResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy_engine

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy_engine.delete_policy_engine(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_policy_engine_request.DeletePolicyEngineRequest = {
            "policy_engine_id": policy_engine_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_engines(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_policy_engines_response.ListPolicyEnginesResponse":
        """<p>Retrieves a list of policy engines within the AgentCore Policy system. This operation supports pagination to help administrators discover and manage policy engines across their account. Each policy engine serves as a container for related policies.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngines.html">ListPolicyEngines</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy engines to return in a single response. If not specified, the default is 10 policy engines per page, with a maximum of 100 per page.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_policy_engines_request.ListPolicyEnginesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_policy_engines_response.ListPolicyEnginesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_engines

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_engines.list_policy_engines(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_policy_engines_request.ListPolicyEnginesRequest = {}
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

    def iter_list_policy_engines(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.policy_engine.PolicyEngine]":
        _token = next_token
        while True:
            _response = self.list_policy_engines(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_engines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_policy_engine_summary(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_policy_engine_summary_response.GetPolicyEngineSummaryResponse":
        """<p>Retrieves a metadata-only summary of a specific policy engine without decrypting customer content. This lightweight read operation returns resource identifiers, status, timestamps, and the encryption key ARN, but does not include the description or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            policy_engine_id: <p>The unique identifier of the policy engine to retrieve the summary for. This must be a valid policy engine ID that exists within the account.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_policy_engine_summary_request.GetPolicyEngineSummaryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_policy_engine_summary_response.GetPolicyEngineSummaryResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_engine_summary

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_engine_summary.get_policy_engine_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_policy_engine_summary_request.GetPolicyEngineSummaryRequest = {
            "policy_engine_id": policy_engine_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_engine_summaries(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_policy_engine_summaries_response.ListPolicyEngineSummariesResponse":
        """<p>Retrieves a paginated list of metadata-only policy engine summaries without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps for each policy engine, but does not include descriptions or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyEngineSummaries.html">ListPolicyEngineSummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy engine summaries to return in a single response.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_policy_engine_summaries_request.ListPolicyEngineSummariesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_policy_engine_summaries_response.ListPolicyEngineSummariesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_engine_summaries

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_engine_summaries.list_policy_engine_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_policy_engine_summaries_request.ListPolicyEngineSummariesRequest = {}
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

    def iter_list_policy_engine_summaries(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.policy_engine_summary.PolicyEngineSummary]":
        _token = next_token
        while True:
            _response = self.list_policy_engine_summaries(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_engines",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_policy_generation(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        resource: "capo_bedrock_agentcore_control.types.resource.Resource",
        content: "capo_bedrock_agentcore_control.types.content.Content",
        name: "capo_bedrock_agentcore_control.types.policy_generation_name.PolicyGenerationName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.start_policy_generation_response.StartPolicyGenerationResponse":
        """<p>Initiates the AI-powered generation of Dogwood policies from natural language descriptions within the AgentCore Policy system. This feature enables both technical and non-technical users to create policies by describing their authorization requirements in plain English, which is then automatically translated into formal Dogwood policy statements. The generation process analyzes the natural language input along with the Gateway's tool context to produce validated policy options. Generated policy assets are automatically deleted after 7 days, so you should review and create policies from the generated assets within this timeframe. Once created, policies are permanent and not subject to this expiration. Generated policies should be reviewed and tested in log-only mode before deploying to production. Use this when you want to describe policy intent naturally rather than learning Dogwood syntax, though generated policies may require refinement for complex scenarios.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that provides the context for policy generation. This engine's schema and tool context are used to ensure generated policies are valid and applicable.</p>
            resource: <p>The resource information that provides context for policy generation. This helps the AI understand the target resources and generate appropriate access control rules.</p>
            content: <p>The natural language description of the desired policy behavior. This content is processed by AI to generate corresponding Dogwood policy statements that match the described intent.</p>
            name: <p>A customer-assigned name for the policy generation request. This helps track and identify generation operations, especially when running multiple generations simultaneously.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without starting a duplicate generation.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.start_policy_generation_request.StartPolicyGenerationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.start_policy_generation_response.StartPolicyGenerationResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.start_policy_generation

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.start_policy_generation.start_policy_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.start_policy_generation_request.StartPolicyGenerationRequest = {
            "policy_engine_id": policy_engine_id,
            "resource": resource,
            "content": content,
            "name": name,
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

    def get_policy_generation(
        self,
        policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_policy_generation_response.GetPolicyGenerationResponse":
        """<p>Retrieves information about a policy generation request within the AgentCore Policy system. Policy generation converts natural language descriptions into Dogwood policy statements using AI-powered translation, enabling non-technical users to create policies.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request to be retrieved. This must be a valid generation ID from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html">StartPolicyGeneration</a> call.</p>
            policy_engine_id: <p>The identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and schema validation.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_policy_generation_request.GetPolicyGenerationRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_policy_generation_response.GetPolicyGenerationResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation.get_policy_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_policy_generation_request.GetPolicyGenerationRequest = {
            "policy_generation_id": policy_generation_id,
            "policy_engine_id": policy_engine_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_generations(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_policy_generations_response.ListPolicyGenerationsResponse":
        """<p>Retrieves a list of policy generation requests within the AgentCore Policy system. This operation supports pagination and filtering to help track and manage AI-powered policy generation operations.</p>

        Args:
            next_token: <p>A pagination token for retrieving additional policy generations when results are paginated.</p>
            max_results: <p>The maximum number of policy generations to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy generations to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_policy_generations_request.ListPolicyGenerationsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_policy_generations_response.ListPolicyGenerationsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generations

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generations.list_policy_generations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_policy_generations_request.ListPolicyGenerationsRequest = {
            "policy_engine_id": policy_engine_id
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

    def iter_list_policy_generations(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.policy_generation.PolicyGeneration]":
        _token = next_token
        while True:
            _response = self.list_policy_generations(
                policy_engine_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_generations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_policy_generation_summary(
        self,
        policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_policy_generation_summary_response.GetPolicyGenerationSummaryResponse":
        """<p>Retrieves a metadata-only summary of a specific policy generation request without decrypting customer content. This lightweight read operation returns resource identifiers, status, timestamps, and findings, but does not include status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request to retrieve the summary for.</p>
            policy_engine_id: <p>The identifier of the policy engine associated with the policy generation request.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_policy_generation_summary_request.GetPolicyGenerationSummaryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_policy_generation_summary_response.GetPolicyGenerationSummaryResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation_summary

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_generation_summary.get_policy_generation_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_policy_generation_summary_request.GetPolicyGenerationSummaryRequest = {
            "policy_generation_id": policy_generation_id,
            "policy_engine_id": policy_engine_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_generation_assets(
        self,
        policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_policy_generation_assets_response.ListPolicyGenerationAssetsResponse":
        """<p>Retrieves a list of generated policy assets from a policy generation request within the AgentCore Policy system. This operation returns the actual Dogwood policies and related artifacts produced by the AI-powered policy generation process, allowing users to review and select from multiple generated policy options.</p>

        Args:
            policy_generation_id: <p>The unique identifier of the policy generation request whose assets are to be retrieved. This must be a valid generation ID from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_StartPolicyGeneration.html">StartPolicyGeneration</a> call that has completed processing.</p>
            policy_engine_id: <p>The unique identifier of the policy engine associated with the policy generation request. This provides the context for the generation operation and ensures assets are retrieved from the correct policy engine.</p>
            next_token: <p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationAssets.html">ListPolicyGenerationAssets</a> call. Use this token to retrieve the next page of assets when the response is paginated due to large numbers of generated policy options.</p>
            max_results: <p>The maximum number of policy generation assets to return in a single response. If not specified, the default is 10 assets per page, with a maximum of 100 per page. This helps control response size when dealing with policy generations that produce many alternative policy options.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_policy_generation_assets_request.ListPolicyGenerationAssetsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_policy_generation_assets_response.ListPolicyGenerationAssetsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_assets

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_assets.list_policy_generation_assets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_policy_generation_assets_request.ListPolicyGenerationAssetsRequest = {
            "policy_generation_id": policy_generation_id,
            "policy_engine_id": policy_engine_id,
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

    def iter_list_policy_generation_assets(
        self,
        policy_generation_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.policy_generation_asset.PolicyGenerationAsset]":
        _token = next_token
        while True:
            _response = self.list_policy_generation_assets(
                policy_generation_id,
                policy_engine_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_generation_assets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_policy_generation_summaries(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_policy_generation_summaries_response.ListPolicyGenerationSummariesResponse":
        """<p>Retrieves a paginated list of metadata-only policy generation summaries within a policy engine without decrypting customer content. This lightweight read operation returns resource identifiers, status, timestamps, and findings for each policy generation, but does not include status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicyGenerationSummaries.html">ListPolicyGenerationSummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy generation summaries to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy generation summaries to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_policy_generation_summaries_request.ListPolicyGenerationSummariesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_policy_generation_summaries_response.ListPolicyGenerationSummariesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_summaries

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_generation_summaries.list_policy_generation_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_policy_generation_summaries_request.ListPolicyGenerationSummariesRequest = {
            "policy_engine_id": policy_engine_id
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

    def iter_list_policy_generation_summaries(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.policy_generation_summary.PolicyGenerationSummary]":
        _token = next_token
        while True:
            _response = self.list_policy_generation_summaries(
                policy_engine_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policy_generations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_policy(
        self,
        name: "capo_bedrock_agentcore_control.types.policy_name.PolicyName",
        definition: "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition",
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        validation_mode: Optional[
            "capo_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"
        ] = None,
        enforcement_mode: Optional[
            "capo_bedrock_agentcore_control.types.enforcement_mode.EnforcementMode"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_policy_response.CreatePolicyResponse":
        """<p>Creates a policy within the AgentCore Policy system. Policies provide real-time, deterministic control over agentic interactions with AgentCore Gateway. Using Cedar or Dogwood, you can define fine-grained policies that specify which interactions with Gateway tools are permitted based on input parameters and OAuth claims, ensuring agents operate within defined boundaries and business rules. The policy is validated during creation against the Cedar schema generated from the Gateway's tools' input schemas, which defines the available tools, their parameters, and expected data types. This is an asynchronous operation. Use the <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_GetPolicy.html">GetPolicy</a> operation to poll the <code>status</code> field to track completion.</p> <p>If the new policy is a temporal policy, creating it invalidates the policy engine's active temporal sessions. For more information about temporal policy sessions, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-session-based-temporal.html">session-based temporal policies</a>. The policy engine returns an HTTP 409 <code>ConflictException</code> to in-flight sessions. To resume, you must start a new session with a new session ID.</p>

        Args:
            name: <p>The customer-assigned immutable name for the policy. Must be unique within the account. This name is used for policy identification and cannot be changed after creation.</p>
            definition: <p>The Cedar or Dogwood policy statement that defines the access control rules. This contains the actual policy logic written in Cedar or Dogwood, specifying effect (permit or forbid), principals, actions, resources, and conditions for agent behavior control.</p>
            description: <p>A human-readable description of the policy's purpose and functionality (1-4,096 characters). This helps policy administrators understand the policy's intent, business rules, and operational scope. Use this field to document why the policy exists, what business requirement it addresses, and any special considerations for maintenance. Clear descriptions are essential for policy governance, auditing, and troubleshooting.</p>
            validation_mode: <p>The validation mode for the policy creation. Determines how Cedar analyzer validation results are handled during policy creation. FAIL_ON_ANY_FINDINGS (default) runs the Cedar analyzer to validate the policy against the Cedar schema and tool context, failing creation if the analyzer detects any validation issues to ensure strict conformance. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows policy creation even if validation issues are detected, useful for testing or when the policy schema is evolving. Use FAIL_ON_ANY_FINDINGS for production policies to ensure correctness, and IGNORE_ALL_FINDINGS only when you understand and accept the analyzer findings.</p>
            enforcement_mode: <p>The enforcement mode for the policy. Run this policy in <code>LOG_ONLY</code> mode to collect data on how it affects your application. Once you are satisfied with the data gathered, switch the policy to <code>ACTIVE</code>. Defaults to <code>ACTIVE</code>.</p>
            policy_engine_id: <p>The identifier of the policy engine which contains this policy. Policy engines group related policies and provide the execution context for policy evaluation.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure the idempotency of the request. The AWS SDK automatically generates this token, so you don't need to provide it in most cases. If you retry a request with the same client token, the service returns the same response without creating a duplicate policy.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_policy_request.CreatePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_policy_response.CreatePolicyResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_policy.create_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_policy_request.CreatePolicyRequest = {
            "name": name,
            "definition": definition,
            "policy_engine_id": policy_engine_id,
        }
        if description is not None:
            input_["description"] = description
        if validation_mode is not None:
            input_["validation_mode"] = validation_mode
        if enforcement_mode is not None:
            input_["enforcement_mode"] = enforcement_mode
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

    def get_policy(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves detailed information about a specific policy within the AgentCore Policy system. This operation returns the complete policy definition, metadata, and current status, allowing administrators to review and manage policy configurations.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be retrieved.</p>
            policy_id: <p>The unique identifier of the policy to be retrieved. This must be a valid policy ID that exists within the specified policy engine.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_policy_request.GetPolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_policy_request.GetPolicyRequest = {
            "policy_engine_id": policy_engine_id,
            "policy_id": policy_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_policy(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
        ] = None,
        definition: Optional[
            "capo_bedrock_agentcore_control.types.policy_definition.PolicyDefinition"
        ] = None,
        validation_mode: Optional[
            "capo_bedrock_agentcore_control.types.policy_validation_mode.PolicyValidationMode"
        ] = None,
        enforcement_mode: Optional[
            "capo_bedrock_agentcore_control.types.enforcement_mode.EnforcementMode"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_policy_response.UpdatePolicyResponse":
        """<p>Updates an existing policy within the AgentCore Policy system. This operation allows modification of the policy description and definition while maintaining the policy's identity. The updated policy is validated against the Cedar schema before being applied. This is an asynchronous operation. Use the <code>GetPolicy</code> operation to poll the <code>status</code> field to track completion.</p> <p>If the updated policy is a temporal policy, the policy engine invalidates all active temporal sessions. If the update adds or removes temporal operators, the policy engine also invalidates active temporal sessions. For more information about temporal policy sessions, see <a href="https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-session-based-temporal.html">session-based temporal policies</a>. The policy engine returns an HTTP 409 <code>ConflictException</code> to in-flight sessions. To resume, you must start a new session with a new session ID.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be updated. This ensures the policy is updated within the correct policy engine context.</p>
            policy_id: <p>The unique identifier of the policy to be updated. This must be a valid policy ID that exists within the specified policy engine.</p>
            description: <p>The new human-readable description for the policy. This optional field allows updating the policy's documentation while keeping the same policy logic.</p>
            definition: <p>The new Cedar or Dogwood policy statement that defines the access control rules. This replaces the existing policy definition with new logic while maintaining the policy's identity.</p>
            validation_mode: <p>The validation mode for the policy update. Determines how Cedar analyzer validation results are handled during policy updates. FAIL_ON_ANY_FINDINGS runs the Cedar analyzer and fails the update if validation issues are detected, ensuring the policy conforms to the Cedar schema and tool context. IGNORE_ALL_FINDINGS runs the Cedar analyzer but allows updates despite validation warnings. Use FAIL_ON_ANY_FINDINGS to ensure policy correctness during updates, especially when modifying policy logic or conditions.</p>
            enforcement_mode: <p>The enforcement mode for the policy. Run this policy in <code>LOG_ONLY</code> mode to collect data on how it affects your application. Once you are satisfied with the data gathered, switch the policy to <code>ACTIVE</code>. If you omit this field, the policy's existing enforcement mode is unchanged.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_policy_request.UpdatePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_policy_response.UpdatePolicyResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_policy.update_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_policy_request.UpdatePolicyRequest = {
            "policy_engine_id": policy_engine_id,
            "policy_id": policy_id,
        }
        if description is not None:
            input_["description"] = description
        if definition is not None:
            input_["definition"] = definition
        if validation_mode is not None:
            input_["validation_mode"] = validation_mode
        if enforcement_mode is not None:
            input_["enforcement_mode"] = enforcement_mode

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_policy_response.DeletePolicyResponse":
        """<p>Deletes an existing policy from the AgentCore Policy system. Once deleted, the policy can no longer be used for agent behavior control and all references to it become invalid. This is an asynchronous operation. Use the <code>GetPolicy</code> operation to poll the <code>status</code> field to track completion.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to be deleted. This ensures the policy is deleted from the correct policy engine context.</p>
            policy_id: <p>The unique identifier of the policy to be deleted. This must be a valid policy ID that exists within the specified policy engine.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_policy_request.DeletePolicyRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_policy_response.DeletePolicyResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_policy_request.DeletePolicyRequest = {
            "policy_engine_id": policy_engine_id,
            "policy_id": policy_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policies(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        target_resource_scope: Optional[
            "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_policies_response.ListPoliciesResponse":
        """<p>Retrieves a list of policies within the AgentCore Policy engine. This operation supports pagination and filtering to help administrators manage and discover policies across policy engines. Results can be filtered by policy engine or resource associations.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicies.html">ListPolicies</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policies to return in a single response. If not specified, the default is 10 policies per page, with a maximum of 100 per page.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policies to retrieve.</p>
            target_resource_scope: <p>Optional filter to list policies that apply to a specific resource scope or resource type. This helps narrow down policy results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_policies_request.ListPoliciesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_policies_response.ListPoliciesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policies

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policies.list_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_policies_request.ListPoliciesRequest = {
            "policy_engine_id": policy_engine_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if target_resource_scope is not None:
            input_["target_resource_scope"] = target_resource_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_policies(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        target_resource_scope: Optional[
            "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.policy.Policy]":
        _token = next_token
        while True:
            _response = self.list_policies(
                policy_engine_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                target_resource_scope=target_resource_scope,
            )
            _page = _resolve_path(_response, ("policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_policy_summary(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        policy_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_policy_summary_response.GetPolicySummaryResponse":
        """<p>Retrieves a metadata-only summary of a specific policy without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps, but does not include the policy definition, description, or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            policy_engine_id: <p>The identifier of the policy engine that manages the policy to retrieve the summary for.</p>
            policy_id: <p>The unique identifier of the policy to retrieve the summary for. This must be a valid policy ID that exists within the specified policy engine.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_policy_summary_request.GetPolicySummaryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_policy_summary_response.GetPolicySummaryResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_summary

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_policy_summary.get_policy_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_policy_summary_request.GetPolicySummaryRequest = {
            "policy_engine_id": policy_engine_id,
            "policy_id": policy_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_policy_summaries(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        target_resource_scope: Optional[
            "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_policy_summaries_response.ListPolicySummariesResponse":
        """<p>Retrieves a paginated list of metadata-only policy summaries within a policy engine without decrypting customer content. This lightweight read operation returns resource identifiers, status, and timestamps for each policy, but does not include policy definitions, descriptions, or status reasons. Because this operation does not require access to the customer's KMS key, it is suitable for resource discovery, inventory, and integration scenarios where only metadata is needed.</p>

        Args:
            next_token: <p>A pagination token returned from a previous <a href="https://docs.aws.amazon.com/bedrock-agentcore-control/latest/APIReference/API_ListPolicySummaries.html">ListPolicySummaries</a> call. Use this token to retrieve the next page of results when the response is paginated.</p>
            max_results: <p>The maximum number of policy summaries to return in a single response.</p>
            policy_engine_id: <p>The identifier of the policy engine whose policy summaries to retrieve.</p>
            target_resource_scope: <p>Optional filter to list policy summaries that apply to a specific resource scope or resource type. This helps narrow down results to those relevant for particular Amazon Web Services resources, agent tools, or operational contexts within the policy engine ecosystem.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_policy_summaries_request.ListPolicySummariesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_policy_summaries_response.ListPolicySummariesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_summaries

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_policy_summaries.list_policy_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_policy_summaries_request.ListPolicySummariesRequest = {
            "policy_engine_id": policy_engine_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if target_resource_scope is not None:
            input_["target_resource_scope"] = target_resource_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_policy_summaries(
        self,
        policy_engine_id: "capo_bedrock_agentcore_control.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        target_resource_scope: Optional[
            "capo_bedrock_agentcore_control.types.bedrock_agentcore_resource_arn.BedrockAgentcoreResourceArn"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.policy_summary.PolicySummary]":
        _token = next_token
        while True:
            _response = self.list_policy_summaries(
                policy_engine_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                target_resource_scope=target_resource_scope,
            )
            _page = _resolve_path(_response, ("policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_registry_record(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        name: "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName",
        descriptor_type: "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        descriptors: Optional[
            "capo_bedrock_agentcore_control.types.descriptors.Descriptors"
        ] = None,
        record_version: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        synchronization_type: Optional[
            "capo_bedrock_agentcore_control.types.synchronization_type.SynchronizationType"
        ] = None,
        synchronization_configuration: Optional[
            "capo_bedrock_agentcore_control.types.synchronization_configuration.SynchronizationConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_registry_record_response.CreateRegistryRecordResponse":
        """<p>Creates a new registry record within the specified registry. A registry record represents an individual AI resource's metadata in the registry. This could be an MCP server (and associated tools), A2A agent, agent skill, or a custom resource with a custom schema.</p> <p>The record is processed asynchronously and returns HTTP 202 Accepted.</p>

        Args:
            registry_id: <p>The identifier of the registry where the record will be created. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            name: <p>The name of the registry record.</p>
            description: <p>A description of the registry record.</p>
            descriptor_type: <p>The descriptor type of the registry record.</p> <ul> <li> <p> <code>MCP</code> - Model Context Protocol descriptor for MCP-compatible servers and tools.</p> </li> <li> <p> <code>A2A</code> - Agent-to-Agent protocol descriptor.</p> </li> <li> <p> <code>CUSTOM</code> - Custom descriptor type for resources such as APIs, Lambda functions, or servers not conforming to a standard protocol.</p> </li> <li> <p> <code>AGENT_SKILLS</code> - Agent skills descriptor for defining agent skill definitions.</p> </li> </ul>
            descriptors: <p>The descriptor-type-specific configuration containing the resource schema and metadata. The structure of this field depends on the <code>descriptorType</code> you specify.</p>
            record_version: <p>The version of the registry record. Use this to track different versions of the record's content.</p>
            synchronization_type: <p>The type of synchronization to use for keeping the record metadata up to date from an external source. Possible values include <code>FROM_URL</code> and <code>NONE</code>.</p>
            synchronization_configuration: <p>The configuration for synchronizing registry record metadata from an external source, such as a URL-based MCP server.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_registry_record_request.CreateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_registry_record_response.CreateRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry_record.create_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_registry_record_request.CreateRegistryRecordRequest = {
            "registry_id": registry_id,
            "name": name,
            "descriptor_type": descriptor_type,
        }
        if description is not None:
            input_["description"] = description
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if synchronization_type is not None:
            input_["synchronization_type"] = synchronization_type
        if synchronization_configuration is not None:
            input_["synchronization_configuration"] = synchronization_configuration
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

    def get_registry_record(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_registry_record_response.GetRegistryRecordResponse":
        """<p>Retrieves information about a specific registry record.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_registry_record_request.GetRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_registry_record_response.GetRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry_record.get_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_registry_record_request.GetRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry_record(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
        ] = None,
        descriptor_type: Optional[
            "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
        ] = None,
        descriptors: Optional[
            "capo_bedrock_agentcore_control.types.updated_descriptors.UpdatedDescriptors"
        ] = None,
        record_version: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_version.RegistryRecordVersion"
        ] = None,
        synchronization_type: Optional[
            "capo_bedrock_agentcore_control.types.updated_synchronization_type.UpdatedSynchronizationType"
        ] = None,
        synchronization_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_synchronization_configuration.UpdatedSynchronizationConfiguration"
        ] = None,
        trigger_synchronization: Optional[bool] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_registry_record_response.UpdateRegistryRecordResponse":
        """<p>Updates an existing registry record. This operation uses PATCH semantics, so you only need to specify the fields you want to change. The update is processed asynchronously and returns HTTP 202 Accepted.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to update. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>
            name: <p>The updated name for the registry record.</p>
            description: <p>The updated description for the registry record. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>
            descriptor_type: <p>The updated descriptor type for the registry record. Changing the descriptor type may require updating the <code>descriptors</code> field to match the new type's schema requirements.</p>
            descriptors: <p>The updated descriptor-type-specific configuration containing the resource schema and metadata. Uses PATCH semantics where individual descriptor fields can be updated independently.</p>
            record_version: <p>The version of the registry record for optimistic locking. If provided, it must match the current version of the record. The service automatically increments the version after a successful update.</p>
            synchronization_type: <p>The updated synchronization type for the registry record.</p>
            synchronization_configuration: <p>The updated synchronization configuration for the registry record.</p>
            trigger_synchronization: <p>Whether to trigger synchronization using the stored or provided configuration. When set to <code>true</code>, the service will synchronize the record metadata from the configured external source.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_registry_record_request.UpdateRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_registry_record_response.UpdateRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record.update_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_registry_record_request.UpdateRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if descriptor_type is not None:
            input_["descriptor_type"] = descriptor_type
        if descriptors is not None:
            input_["descriptors"] = descriptors
        if record_version is not None:
            input_["record_version"] = record_version
        if synchronization_type is not None:
            input_["synchronization_type"] = synchronization_type
        if synchronization_configuration is not None:
            input_["synchronization_configuration"] = synchronization_configuration
        if trigger_synchronization is not None:
            input_["trigger_synchronization"] = trigger_synchronization

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_registry_record(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_registry_record_response.DeleteRegistryRecordResponse":
        """<p>Deletes a registry record. The record's status transitions to <code>DELETING</code> and the record is removed asynchronously.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_registry_record_request.DeleteRegistryRecordRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_registry_record_response.DeleteRegistryRecordResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry_record

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry_record.delete_registry_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_registry_record_request.DeleteRegistryRecordRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_registry_records(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
        ] = None,
        descriptor_type: Optional[
            "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_registry_records_response.ListRegistryRecordsResponse":
        """<p>Lists registry records within a registry. You can optionally filter results using the <code>name</code>, <code>status</code>, and <code>descriptorType</code> parameters. When multiple filters are specified, they are combined using AND logic.</p>

        Args:
            registry_id: <p>The identifier of the registry to list records from. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            name: <p>Filter registry records by name.</p>
            status: <p>Filter registry records by their current status. Possible values include <code>CREATING</code>, <code>DRAFT</code>, <code>APPROVED</code>, <code>PENDING_APPROVAL</code>, <code>REJECTED</code>, <code>DEPRECATED</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, and <code>UPDATE_FAILED</code>.</p>
            descriptor_type: <p>Filter registry records by their descriptor type. Possible values are <code>MCP</code>, <code>A2A</code>, <code>CUSTOM</code>, and <code>AGENT_SKILLS</code>.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_registry_records_request.ListRegistryRecordsRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_registry_records_response.ListRegistryRecordsResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registry_records

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registry_records.list_registry_records(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_registry_records_request.ListRegistryRecordsRequest = {
            "registry_id": registry_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if name is not None:
            input_["name"] = name
        if status is not None:
            input_["status"] = status
        if descriptor_type is not None:
            input_["descriptor_type"] = descriptor_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_registry_records(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_name.RegistryRecordName"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus"
        ] = None,
        descriptor_type: Optional[
            "capo_bedrock_agentcore_control.types.descriptor_type.DescriptorType"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.registry_record_summary.RegistryRecordSummary]":
        _token = next_token
        while True:
            _response = self.list_registry_records(
                registry_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                name=name,
                status=status,
                descriptor_type=descriptor_type,
            )
            _page = _resolve_path(_response, ("registry_records",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def submit_registry_record_for_approval(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse":
        """<p>Submits a registry record for approval. This transitions the record from <code>DRAFT</code> status to <code>PENDING_APPROVAL</code> status. If the registry has auto-approval enabled, the record is automatically approved.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to submit for approval. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_response.SubmitRegistryRecordForApprovalResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.submit_registry_record_for_approval

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.submit_registry_record_for_approval.submit_registry_record_for_approval(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.submit_registry_record_for_approval_request.SubmitRegistryRecordForApprovalRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry_record_status(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        record_id: "capo_bedrock_agentcore_control.types.record_identifier.RecordIdentifier",
        status: "capo_bedrock_agentcore_control.types.registry_record_status.RegistryRecordStatus",
        status_reason: str,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse":
        """<p>Updates the status of a registry record. Use this operation to approve, reject, or deprecate a registry record.</p>

        Args:
            registry_id: <p>The identifier of the registry containing the record. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            record_id: <p>The identifier of the registry record to update the status for. You can specify either the Amazon Resource Name (ARN) or the ID of the record.</p>
            status: <p>The target status for the registry record.</p>
            status_reason: <p>The reason for the status change, such as why the record was approved or rejected.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_registry_record_status_response.UpdateRegistryRecordStatusResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record_status

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry_record_status.update_registry_record_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_registry_record_status_request.UpdateRegistryRecordStatusRequest = {
            "registry_id": registry_id,
            "record_id": record_id,
            "status": status,
            "status_reason": status_reason,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_registry(
        self,
        name: "capo_bedrock_agentcore_control.types.registry_name.RegistryName",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.description.Description"
        ] = None,
        authorizer_type: Optional[
            "capo_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
        ] = None,
        client_token: Optional[
            "capo_bedrock_agentcore_control.types.client_token.ClientToken"
        ] = None,
        approval_configuration: Optional[
            "capo_bedrock_agentcore_control.types.approval_configuration.ApprovalConfiguration"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_registry_response.CreateRegistryResponse":
        """<p>Creates a new registry in your Amazon Web Services account. A registry serves as a centralized catalog for organizing and managing registry records, including MCP servers, A2A agents, agent skills, and custom resource types.</p> <p>If you specify <code>CUSTOM_JWT</code> as the <code>authorizerType</code>, you must provide an <code>authorizerConfiguration</code>.</p>

        Args:
            name: <p>The name of the registry. The name must be unique within your account and can contain alphanumeric characters and underscores.</p>
            description: <p>A description of the registry.</p>
            authorizer_type: <p>The type of authorizer to use for the registry. This controls the authorization method for the Search and Invoke APIs used by consumers, and does not affect the standard CRUDL APIs for registry and registry record management used by administrators.</p> <ul> <li> <p> <code>CUSTOM_JWT</code> - Authorize with a bearer token.</p> </li> <li> <p> <code>AWS_IAM</code> - Authorize with your Amazon Web Services IAM credentials.</p> </li> </ul>
            authorizer_configuration: <p>The authorizer configuration for the registry. Required if <code>authorizerType</code> is <code>CUSTOM_JWT</code>. For details, see the <code>AuthorizerConfiguration</code> data type.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don't specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn't return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            approval_configuration: <p>The approval configuration for registry records. Controls whether records require explicit approval before becoming active. See the <code>ApprovalConfiguration</code> data type for supported configuration options.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_registry_request.CreateRegistryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_registry_response.CreateRegistryResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_registry.create_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_registry_request.CreateRegistryRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_registry(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> (
        "capo_bedrock_agentcore_control.types.get_registry_response.GetRegistryResponse"
    ):
        """<p>Retrieves information about a specific registry.</p>

        Args:
            registry_id: <p>The identifier of the registry to retrieve. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_registry_request.GetRegistryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_registry_response.GetRegistryResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_registry.get_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_registry_request.GetRegistryRequest = {
            "registry_id": registry_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_registry(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        name: Optional[
            "capo_bedrock_agentcore_control.types.registry_name.RegistryName"
        ] = None,
        description: Optional[
            "capo_bedrock_agentcore_control.types.updated_description.UpdatedDescription"
        ] = None,
        authorizer_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_authorizer_configuration.UpdatedAuthorizerConfiguration"
        ] = None,
        approval_configuration: Optional[
            "capo_bedrock_agentcore_control.types.updated_approval_configuration.UpdatedApprovalConfiguration"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_registry_response.UpdateRegistryResponse":
        """<p>Updates an existing registry. This operation uses PATCH semantics, so you only need to specify the fields you want to change.</p>

        Args:
            registry_id: <p>The identifier of the registry to update. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>
            name: <p>The updated name of the registry.</p>
            description: <p>The updated description of the registry. To clear the description, include the <code>UpdatedDescription</code> wrapper with <code>optionalValue</code> not specified.</p>
            authorizer_configuration: <p>The updated authorizer configuration for the registry. Changing the authorizer configuration can break existing consumers of the registry who are using the authorization type prior to the update.</p>
            approval_configuration: <p>The updated approval configuration for registry records. The updated configuration only affects new records that move to <code>PENDING_APPROVAL</code> status after the change. Existing records already in <code>PENDING_APPROVAL</code> status are not affected.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This exception is thrown when a request is made beyond the service quota</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_registry_request.UpdateRegistryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_registry_response.UpdateRegistryResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_registry.update_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_registry_request.UpdateRegistryRequest = {
            "registry_id": registry_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if authorizer_configuration is not None:
            input_["authorizer_configuration"] = authorizer_configuration
        if approval_configuration is not None:
            input_["approval_configuration"] = approval_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_registry(
        self,
        registry_id: "capo_bedrock_agentcore_control.types.registry_identifier.RegistryIdentifier",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_registry_response.DeleteRegistryResponse":
        """<p>Deletes a registry. The registry must contain zero records before it can be deleted. This operation initiates the deletion process asynchronously.</p>

        Args:
            registry_id: <p>The identifier of the registry to delete. You can specify either the Amazon Resource Name (ARN) or the ID of the registry.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.conflict_exception.ConflictException: <p>This exception is thrown when there is a conflict performing an operation</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_registry_request.DeleteRegistryRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_registry_response.DeleteRegistryResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_registry.delete_registry(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_registry_request.DeleteRegistryRequest = {
            "registry_id": registry_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_registries(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore_control.types.registry_status.RegistryStatus"
        ] = None,
        authorizer_type: Optional[
            "capo_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_registries_response.ListRegistriesResponse":
        """<p>Lists all registries in the account. You can optionally filter results by status using the <code>status</code> parameter, or by authorizer type using the <code>authorizerType</code> parameter.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            status: <p>Filter registries by their current status. Possible values include <code>CREATING</code>, <code>READY</code>, <code>UPDATING</code>, <code>CREATE_FAILED</code>, <code>UPDATE_FAILED</code>, <code>DELETING</code>, and <code>DELETE_FAILED</code>.</p>
            authorizer_type: <p>Filter registries by their authorizer type. Possible values are <code>CUSTOM_JWT</code> and <code>AWS_IAM</code>. For more information about authorizer types, see the <code>RegistryAuthorizerType</code> enum.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_registries_request.ListRegistriesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_registries_response.ListRegistriesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registries

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_registries.list_registries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_registries_request.ListRegistriesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if status is not None:
            input_["status"] = status
        if authorizer_type is not None:
            input_["authorizer_type"] = authorizer_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_registries(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        max_results: Optional[
            "capo_bedrock_agentcore_control.types.max_results.MaxResults"
        ] = None,
        next_token: Optional[
            "capo_bedrock_agentcore_control.types.next_token.NextToken"
        ] = None,
        status: Optional[
            "capo_bedrock_agentcore_control.types.registry_status.RegistryStatus"
        ] = None,
        authorizer_type: Optional[
            "capo_bedrock_agentcore_control.types.registry_authorizer_type.RegistryAuthorizerType"
        ] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.registry_summary.RegistrySummary]":
        _token = next_token
        while True:
            _response = self.list_registries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                status=status,
                authorizer_type=authorizer_type,
            )
            _page = _resolve_path(_response, ("registries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_workload_identity(
        self,
        name: "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        allowed_resource_oauth2_return_urls: Optional[
            "capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"
        ] = None,
        tags: Optional["capo_bedrock_agentcore_control.types.tags_map.TagsMap"] = None,
    ) -> "capo_bedrock_agentcore_control.types.create_workload_identity_response.CreateWorkloadIdentityResponse":
        """<p>Creates a new workload identity.</p>

        Args:
            name: <p>The name of the workload identity. The name must be unique within your account.</p>
            allowed_resource_oauth2_return_urls: <p>The list of allowed OAuth2 return URLs for resources associated with this workload identity.</p>
            tags: <p>A map of tag keys and values to assign to the workload identity. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.create_workload_identity_request.CreateWorkloadIdentityRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.create_workload_identity_response.CreateWorkloadIdentityResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_workload_identity

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.create_workload_identity.create_workload_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.create_workload_identity_request.CreateWorkloadIdentityRequest = {
            "name": name
        }
        if allowed_resource_oauth2_return_urls is not None:
            input_["allowed_resource_oauth2_return_urls"] = (
                allowed_resource_oauth2_return_urls
            )
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_workload_identity(
        self,
        name: "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.get_workload_identity_response.GetWorkloadIdentityResponse":
        """<p>Retrieves information about a workload identity.</p>

        Args:
            name: <p>The name of the workload identity to retrieve.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.get_workload_identity_request.GetWorkloadIdentityRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.get_workload_identity_response.GetWorkloadIdentityResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_workload_identity

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.get_workload_identity.get_workload_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.get_workload_identity_request.GetWorkloadIdentityRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_workload_identity(
        self,
        name: "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        allowed_resource_oauth2_return_urls: Optional[
            "capo_bedrock_agentcore_control.types.resource_oauth2_return_url_list_type.ResourceOauth2ReturnUrlListType"
        ] = None,
    ) -> "capo_bedrock_agentcore_control.types.update_workload_identity_response.UpdateWorkloadIdentityResponse":
        """<p>Updates an existing workload identity.</p>

        Args:
            name: <p>The name of the workload identity to update.</p>
            allowed_resource_oauth2_return_urls: <p>The new list of allowed OAuth2 return URLs for resources associated with this workload identity. This list replaces the existing list.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.update_workload_identity_request.UpdateWorkloadIdentityRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.update_workload_identity_response.UpdateWorkloadIdentityResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_workload_identity

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.update_workload_identity.update_workload_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.update_workload_identity_request.UpdateWorkloadIdentityRequest = {
            "name": name
        }
        if allowed_resource_oauth2_return_urls is not None:
            input_["allowed_resource_oauth2_return_urls"] = (
                allowed_resource_oauth2_return_urls
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_workload_identity(
        self,
        name: "capo_bedrock_agentcore_control.types.workload_identity_name_type.WorkloadIdentityNameType",
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
    ) -> "capo_bedrock_agentcore_control.types.delete_workload_identity_response.DeleteWorkloadIdentityResponse":
        """<p>Deletes a workload identity.</p>

        Args:
            name: <p>The name of the workload identity to delete.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.delete_workload_identity_request.DeleteWorkloadIdentityRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.delete_workload_identity_response.DeleteWorkloadIdentityResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_workload_identity

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.delete_workload_identity.delete_workload_identity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.delete_workload_identity_request.DeleteWorkloadIdentityRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workload_identities(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "capo_bedrock_agentcore_control.types.list_workload_identities_response.ListWorkloadIdentitiesResponse":
        """<p>Lists all workload identities in your account.</p>

        Args:
            next_token: <p>Pagination token.</p>
            max_results: <p>Maximum number of results to return.</p>

        Raises:
            capo_bedrock_agentcore_control.errors.access_denied_exception.AccessDeniedException: <p>This exception is thrown when a request is denied per access permissions</p>
            capo_bedrock_agentcore_control.errors.internal_server_exception.InternalServerException: <p>This exception is thrown if there was an unexpected error during processing of request</p>
            capo_bedrock_agentcore_control.errors.resource_not_found_exception.ResourceNotFoundException: <p>This exception is thrown when a resource referenced by the operation does not exist</p>
            capo_bedrock_agentcore_control.errors.throttling_exception.ThrottlingException: <p>This exception is thrown when the number of requests exceeds the limit</p>
            capo_bedrock_agentcore_control.errors.unauthorized_exception.UnauthorizedException: <p>This exception is thrown when the JWT bearer token is invalid or not found for OAuth bearer token based access</p>
            capo_bedrock_agentcore_control.errors.validation_exception.ValidationException: <p>The input fails to satisfy the constraints specified by the service.</p>
            capo_bedrock_agentcore_control.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_bedrock_agentcore_control.types.list_workload_identities_request.ListWorkloadIdentitiesRequest]",
        ) -> OperationResponse[
            "capo_bedrock_agentcore_control.types.list_workload_identities_response.ListWorkloadIdentitiesResponse"
        ]:
            import capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_workload_identities

            output, http_response = (
                capo_bedrock_agentcore_control._operations.amazon_bedrock_agent_core_control.list_workload_identities.list_workload_identities(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock_agentcore_control.types.list_workload_identities_request.ListWorkloadIdentitiesRequest = {}
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

    def iter_list_workload_identities(
        self,
        *,
        config_overrides: Optional[BedrockAgentCoreControlClientConfig] = None,
        next_token: Optional[str] = None,
        max_results: Optional[int] = None,
    ) -> "Iterator[capo_bedrock_agentcore_control.types.workload_identity_type.WorkloadIdentityType]":
        _token = next_token
        while True:
            _response = self.list_workload_identities(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workload_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
