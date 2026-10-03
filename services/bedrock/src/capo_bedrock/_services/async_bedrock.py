"""Generated from Smithy shape ``com.amazonaws.bedrock#AmazonBedrockControlPlaneService``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_bedrock._auth._signers
import capo_bedrock._auth._sigv4
from capo_bedrock._auth._identity import Credentials
from capo_bedrock._auth._providers import (
    BearerTokenProvider,
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    StaticBearerTokenProvider,
    default_aws_credentials_chain,
)
from capo_bedrock._auth._zapros_handler import AuthMiddleware
from capo_bedrock._pagination import resolve_path as _resolve_path
from capo_bedrock._resources.amazon_bedrock_control_plane_service.advanced_prompt_optimization_job_resource import (
    AsyncAdvancedPromptOptimizationJobResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.allowlist_resource import (
    AsyncAllowlistResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.automated_reasoning_policy_resource import (
    AsyncAutomatedReasoningPolicyResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.bedrock_marketplace_resource import (
    AsyncBedrockMarketplaceResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.custom_model_deployment_resource import (
    AsyncCustomModelDeploymentResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.custom_model_resource import (
    AsyncCustomModelResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.data_retention_resource import (
    AsyncDataRetentionResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.enforced_guardrail_configuration_resource import (
    AsyncEnforcedGuardrailConfigurationResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.evaluation_job_resource import (
    AsyncEvaluationJobResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.guardrails_resource import (
    AsyncGuardrailsResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.inference_profile_resource import (
    AsyncInferenceProfileResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.logging_resource import (
    AsyncLoggingResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.model_copy_resource import (
    AsyncModelCopyResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.model_import_resource import (
    AsyncModelImportResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.model_invocation_job_resource import (
    AsyncModelInvocationJobResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.model_resource import (
    AsyncModelResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.prompt_router_resource import (
    AsyncPromptRouterResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.provisioned_model_throughput_resource import (
    AsyncProvisionedModelThroughputResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.resource_policy_resource import (
    AsyncResourcePolicyResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.subscription_resource import (
    AsyncSubscriptionResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.tagging_resource import (
    AsyncTaggingResource,
)
from capo_bedrock._resources.amazon_bedrock_control_plane_service.training_resource import (
    AsyncTrainingResource,
)
from capo_bedrock._services._aws_config import aaws_config
from capo_bedrock._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_bedrock.types.accept_eula
    import capo_bedrock.types.account_enforced_guardrail_configuration_id
    import capo_bedrock.types.account_enforced_guardrail_inference_input_configuration
    import capo_bedrock.types.account_enforced_guardrail_output_configuration
    import capo_bedrock.types.account_id
    import capo_bedrock.types.acknowledgement_form_data_body
    import capo_bedrock.types.advanced_prompt_optimization_input_config
    import capo_bedrock.types.advanced_prompt_optimization_job_description
    import capo_bedrock.types.advanced_prompt_optimization_job_identifier
    import capo_bedrock.types.advanced_prompt_optimization_job_identifiers
    import capo_bedrock.types.advanced_prompt_optimization_job_name
    import capo_bedrock.types.advanced_prompt_optimization_job_summary
    import capo_bedrock.types.advanced_prompt_optimization_output_config
    import capo_bedrock.types.application_type
    import capo_bedrock.types.arn
    import capo_bedrock.types.automated_reasoning_check_result
    import capo_bedrock.types.automated_reasoning_check_translation_confidence
    import capo_bedrock.types.automated_reasoning_policy_annotation_list
    import capo_bedrock.types.automated_reasoning_policy_arn
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_id
    import capo_bedrock.types.automated_reasoning_policy_build_result_asset_type
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_id
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_source
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_summary
    import capo_bedrock.types.automated_reasoning_policy_build_workflow_type
    import capo_bedrock.types.automated_reasoning_policy_definition
    import capo_bedrock.types.automated_reasoning_policy_description
    import capo_bedrock.types.automated_reasoning_policy_hash
    import capo_bedrock.types.automated_reasoning_policy_name
    import capo_bedrock.types.automated_reasoning_policy_summary
    import capo_bedrock.types.automated_reasoning_policy_test_case
    import capo_bedrock.types.automated_reasoning_policy_test_case_id
    import capo_bedrock.types.automated_reasoning_policy_test_case_id_list
    import capo_bedrock.types.automated_reasoning_policy_test_guard_content
    import capo_bedrock.types.automated_reasoning_policy_test_query_content
    import capo_bedrock.types.automated_reasoning_policy_test_result
    import capo_bedrock.types.base_model_identifier
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request
    import capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response
    import capo_bedrock.types.batch_delete_evaluation_job_request
    import capo_bedrock.types.batch_delete_evaluation_job_response
    import capo_bedrock.types.bedrock_model_id
    import capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.commitment_duration
    import capo_bedrock.types.create_advanced_prompt_optimization_job_request
    import capo_bedrock.types.create_advanced_prompt_optimization_job_response
    import capo_bedrock.types.create_automated_reasoning_policy_request
    import capo_bedrock.types.create_automated_reasoning_policy_response
    import capo_bedrock.types.create_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.create_automated_reasoning_policy_test_case_response
    import capo_bedrock.types.create_automated_reasoning_policy_version_request
    import capo_bedrock.types.create_automated_reasoning_policy_version_response
    import capo_bedrock.types.create_custom_model_deployment_request
    import capo_bedrock.types.create_custom_model_deployment_response
    import capo_bedrock.types.create_custom_model_request
    import capo_bedrock.types.create_custom_model_response
    import capo_bedrock.types.create_evaluation_job_request
    import capo_bedrock.types.create_evaluation_job_response
    import capo_bedrock.types.create_foundation_model_agreement_request
    import capo_bedrock.types.create_foundation_model_agreement_response
    import capo_bedrock.types.create_guardrail_request
    import capo_bedrock.types.create_guardrail_response
    import capo_bedrock.types.create_guardrail_version_request
    import capo_bedrock.types.create_guardrail_version_response
    import capo_bedrock.types.create_inference_profile_request
    import capo_bedrock.types.create_inference_profile_response
    import capo_bedrock.types.create_marketplace_model_endpoint_request
    import capo_bedrock.types.create_marketplace_model_endpoint_response
    import capo_bedrock.types.create_model_copy_job_request
    import capo_bedrock.types.create_model_copy_job_response
    import capo_bedrock.types.create_model_customization_job_request
    import capo_bedrock.types.create_model_customization_job_response
    import capo_bedrock.types.create_model_import_job_request
    import capo_bedrock.types.create_model_import_job_response
    import capo_bedrock.types.create_model_invocation_job_request
    import capo_bedrock.types.create_model_invocation_job_response
    import capo_bedrock.types.create_prompt_router_request
    import capo_bedrock.types.create_prompt_router_response
    import capo_bedrock.types.create_provisioned_model_throughput_request
    import capo_bedrock.types.create_provisioned_model_throughput_response
    import capo_bedrock.types.custom_model_arn
    import capo_bedrock.types.custom_model_data_source
    import capo_bedrock.types.custom_model_deployment_description
    import capo_bedrock.types.custom_model_deployment_identifier
    import capo_bedrock.types.custom_model_deployment_status
    import capo_bedrock.types.custom_model_deployment_summary
    import capo_bedrock.types.custom_model_name
    import capo_bedrock.types.custom_model_summary
    import capo_bedrock.types.customization_config
    import capo_bedrock.types.customization_type
    import capo_bedrock.types.data_retention_mode
    import capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.delete_automated_reasoning_policy_request
    import capo_bedrock.types.delete_automated_reasoning_policy_response
    import capo_bedrock.types.delete_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.delete_automated_reasoning_policy_test_case_response
    import capo_bedrock.types.delete_custom_model_deployment_request
    import capo_bedrock.types.delete_custom_model_deployment_response
    import capo_bedrock.types.delete_custom_model_request
    import capo_bedrock.types.delete_custom_model_response
    import capo_bedrock.types.delete_enforced_guardrail_configuration_request
    import capo_bedrock.types.delete_enforced_guardrail_configuration_response
    import capo_bedrock.types.delete_foundation_model_agreement_request
    import capo_bedrock.types.delete_foundation_model_agreement_response
    import capo_bedrock.types.delete_guardrail_request
    import capo_bedrock.types.delete_guardrail_response
    import capo_bedrock.types.delete_imported_model_request
    import capo_bedrock.types.delete_imported_model_response
    import capo_bedrock.types.delete_inference_profile_request
    import capo_bedrock.types.delete_inference_profile_response
    import capo_bedrock.types.delete_marketplace_model_endpoint_request
    import capo_bedrock.types.delete_marketplace_model_endpoint_response
    import capo_bedrock.types.delete_model_invocation_logging_configuration_request
    import capo_bedrock.types.delete_model_invocation_logging_configuration_response
    import capo_bedrock.types.delete_prompt_router_request
    import capo_bedrock.types.delete_prompt_router_response
    import capo_bedrock.types.delete_provisioned_model_throughput_request
    import capo_bedrock.types.delete_provisioned_model_throughput_response
    import capo_bedrock.types.delete_resource_policy_request
    import capo_bedrock.types.delete_resource_policy_response
    import capo_bedrock.types.deregister_marketplace_model_endpoint_request
    import capo_bedrock.types.deregister_marketplace_model_endpoint_response
    import capo_bedrock.types.endpoint_config
    import capo_bedrock.types.endpoint_name
    import capo_bedrock.types.evaluation_config
    import capo_bedrock.types.evaluation_inference_config
    import capo_bedrock.types.evaluation_job_description
    import capo_bedrock.types.evaluation_job_identifier
    import capo_bedrock.types.evaluation_job_identifiers
    import capo_bedrock.types.evaluation_job_name
    import capo_bedrock.types.evaluation_job_status
    import capo_bedrock.types.evaluation_output_data_config
    import capo_bedrock.types.evaluation_summary
    import capo_bedrock.types.export_automated_reasoning_policy_version_request
    import capo_bedrock.types.export_automated_reasoning_policy_version_response
    import capo_bedrock.types.fine_tuning_job_status
    import capo_bedrock.types.foundation_model_arn
    import capo_bedrock.types.get_account_data_retention_request
    import capo_bedrock.types.get_account_data_retention_response
    import capo_bedrock.types.get_advanced_prompt_optimization_job_request
    import capo_bedrock.types.get_advanced_prompt_optimization_job_response
    import capo_bedrock.types.get_automated_reasoning_policy_annotations_request
    import capo_bedrock.types.get_automated_reasoning_policy_annotations_response
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request
    import capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response
    import capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request
    import capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response
    import capo_bedrock.types.get_automated_reasoning_policy_request
    import capo_bedrock.types.get_automated_reasoning_policy_response
    import capo_bedrock.types.get_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.get_automated_reasoning_policy_test_case_response
    import capo_bedrock.types.get_automated_reasoning_policy_test_result_request
    import capo_bedrock.types.get_automated_reasoning_policy_test_result_response
    import capo_bedrock.types.get_custom_model_deployment_request
    import capo_bedrock.types.get_custom_model_deployment_response
    import capo_bedrock.types.get_custom_model_request
    import capo_bedrock.types.get_custom_model_response
    import capo_bedrock.types.get_evaluation_job_request
    import capo_bedrock.types.get_evaluation_job_response
    import capo_bedrock.types.get_foundation_model_availability_request
    import capo_bedrock.types.get_foundation_model_availability_response
    import capo_bedrock.types.get_foundation_model_identifier
    import capo_bedrock.types.get_foundation_model_request
    import capo_bedrock.types.get_foundation_model_response
    import capo_bedrock.types.get_guardrail_request
    import capo_bedrock.types.get_guardrail_response
    import capo_bedrock.types.get_imported_model_request
    import capo_bedrock.types.get_imported_model_response
    import capo_bedrock.types.get_inference_profile_request
    import capo_bedrock.types.get_inference_profile_response
    import capo_bedrock.types.get_marketplace_model_endpoint_request
    import capo_bedrock.types.get_marketplace_model_endpoint_response
    import capo_bedrock.types.get_model_copy_job_request
    import capo_bedrock.types.get_model_copy_job_response
    import capo_bedrock.types.get_model_customization_job_request
    import capo_bedrock.types.get_model_customization_job_response
    import capo_bedrock.types.get_model_import_job_request
    import capo_bedrock.types.get_model_import_job_response
    import capo_bedrock.types.get_model_invocation_job_request
    import capo_bedrock.types.get_model_invocation_job_response
    import capo_bedrock.types.get_model_invocation_logging_configuration_request
    import capo_bedrock.types.get_model_invocation_logging_configuration_response
    import capo_bedrock.types.get_prompt_router_request
    import capo_bedrock.types.get_prompt_router_response
    import capo_bedrock.types.get_provisioned_model_throughput_request
    import capo_bedrock.types.get_provisioned_model_throughput_response
    import capo_bedrock.types.get_resource_policy_request
    import capo_bedrock.types.get_resource_policy_response
    import capo_bedrock.types.get_use_case_for_model_access_request
    import capo_bedrock.types.get_use_case_for_model_access_response
    import capo_bedrock.types.guardrail_automated_reasoning_policy_config
    import capo_bedrock.types.guardrail_blocked_messaging
    import capo_bedrock.types.guardrail_content_policy_config
    import capo_bedrock.types.guardrail_contextual_grounding_policy_config
    import capo_bedrock.types.guardrail_cross_region_config
    import capo_bedrock.types.guardrail_description
    import capo_bedrock.types.guardrail_identifier
    import capo_bedrock.types.guardrail_name
    import capo_bedrock.types.guardrail_numerical_version
    import capo_bedrock.types.guardrail_sensitive_information_policy_config
    import capo_bedrock.types.guardrail_summary
    import capo_bedrock.types.guardrail_topic_policy_config
    import capo_bedrock.types.guardrail_version
    import capo_bedrock.types.guardrail_word_policy_config
    import capo_bedrock.types.idempotency_token
    import capo_bedrock.types.imported_model_identifier
    import capo_bedrock.types.imported_model_name
    import capo_bedrock.types.imported_model_summary
    import capo_bedrock.types.inference_profile_description
    import capo_bedrock.types.inference_profile_identifier
    import capo_bedrock.types.inference_profile_model_source
    import capo_bedrock.types.inference_profile_name
    import capo_bedrock.types.inference_profile_summary
    import capo_bedrock.types.inference_profile_type
    import capo_bedrock.types.inference_type
    import capo_bedrock.types.job_name
    import capo_bedrock.types.kms_key_arn
    import capo_bedrock.types.kms_key_id
    import capo_bedrock.types.list_advanced_prompt_optimization_jobs_request
    import capo_bedrock.types.list_advanced_prompt_optimization_jobs_response
    import capo_bedrock.types.list_automated_reasoning_policies_request
    import capo_bedrock.types.list_automated_reasoning_policies_response
    import capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request
    import capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response
    import capo_bedrock.types.list_automated_reasoning_policy_test_cases_request
    import capo_bedrock.types.list_automated_reasoning_policy_test_cases_response
    import capo_bedrock.types.list_automated_reasoning_policy_test_results_request
    import capo_bedrock.types.list_automated_reasoning_policy_test_results_response
    import capo_bedrock.types.list_custom_model_deployments_request
    import capo_bedrock.types.list_custom_model_deployments_response
    import capo_bedrock.types.list_custom_models_request
    import capo_bedrock.types.list_custom_models_response
    import capo_bedrock.types.list_enforced_guardrails_configuration_request
    import capo_bedrock.types.list_enforced_guardrails_configuration_response
    import capo_bedrock.types.list_evaluation_jobs_request
    import capo_bedrock.types.list_evaluation_jobs_response
    import capo_bedrock.types.list_foundation_model_agreement_offers_request
    import capo_bedrock.types.list_foundation_model_agreement_offers_response
    import capo_bedrock.types.list_foundation_models_request
    import capo_bedrock.types.list_foundation_models_response
    import capo_bedrock.types.list_guardrails_request
    import capo_bedrock.types.list_guardrails_response
    import capo_bedrock.types.list_imported_models_request
    import capo_bedrock.types.list_imported_models_response
    import capo_bedrock.types.list_inference_profiles_request
    import capo_bedrock.types.list_inference_profiles_response
    import capo_bedrock.types.list_marketplace_model_endpoints_request
    import capo_bedrock.types.list_marketplace_model_endpoints_response
    import capo_bedrock.types.list_model_copy_jobs_request
    import capo_bedrock.types.list_model_copy_jobs_response
    import capo_bedrock.types.list_model_customization_jobs_request
    import capo_bedrock.types.list_model_customization_jobs_response
    import capo_bedrock.types.list_model_import_jobs_request
    import capo_bedrock.types.list_model_import_jobs_response
    import capo_bedrock.types.list_model_invocation_jobs_request
    import capo_bedrock.types.list_model_invocation_jobs_response
    import capo_bedrock.types.list_prompt_routers_request
    import capo_bedrock.types.list_prompt_routers_response
    import capo_bedrock.types.list_provisioned_model_throughputs_request
    import capo_bedrock.types.list_provisioned_model_throughputs_response
    import capo_bedrock.types.list_tags_for_resource_request
    import capo_bedrock.types.list_tags_for_resource_response
    import capo_bedrock.types.logging_config
    import capo_bedrock.types.marketplace_model_endpoint_summary
    import capo_bedrock.types.max_results
    import capo_bedrock.types.model_arn
    import capo_bedrock.types.model_configurations
    import capo_bedrock.types.model_copy_job_arn
    import capo_bedrock.types.model_copy_job_status
    import capo_bedrock.types.model_copy_job_summary
    import capo_bedrock.types.model_customization
    import capo_bedrock.types.model_customization_hyper_parameters
    import capo_bedrock.types.model_customization_job_identifier
    import capo_bedrock.types.model_customization_job_summary
    import capo_bedrock.types.model_data_source
    import capo_bedrock.types.model_deployment_name
    import capo_bedrock.types.model_id
    import capo_bedrock.types.model_identifier
    import capo_bedrock.types.model_import_job_identifier
    import capo_bedrock.types.model_import_job_status
    import capo_bedrock.types.model_import_job_summary
    import capo_bedrock.types.model_invocation_idempotency_token
    import capo_bedrock.types.model_invocation_job_identifier
    import capo_bedrock.types.model_invocation_job_input_data_config
    import capo_bedrock.types.model_invocation_job_name
    import capo_bedrock.types.model_invocation_job_output_data_config
    import capo_bedrock.types.model_invocation_job_status
    import capo_bedrock.types.model_invocation_job_summary
    import capo_bedrock.types.model_invocation_job_timeout_duration_in_hours
    import capo_bedrock.types.model_invocation_type
    import capo_bedrock.types.model_modality
    import capo_bedrock.types.model_source_identifier
    import capo_bedrock.types.model_status
    import capo_bedrock.types.offer_token
    import capo_bedrock.types.offer_type
    import capo_bedrock.types.output_data_config
    import capo_bedrock.types.pagination_token
    import capo_bedrock.types.positive_integer
    import capo_bedrock.types.prompt_router_arn
    import capo_bedrock.types.prompt_router_description
    import capo_bedrock.types.prompt_router_name
    import capo_bedrock.types.prompt_router_summary
    import capo_bedrock.types.prompt_router_target_model
    import capo_bedrock.types.prompt_router_target_models
    import capo_bedrock.types.prompt_router_type
    import capo_bedrock.types.provider
    import capo_bedrock.types.provisioned_model_id
    import capo_bedrock.types.provisioned_model_name
    import capo_bedrock.types.provisioned_model_status
    import capo_bedrock.types.provisioned_model_summary
    import capo_bedrock.types.put_account_data_retention_request
    import capo_bedrock.types.put_account_data_retention_response
    import capo_bedrock.types.put_enforced_guardrail_configuration_request
    import capo_bedrock.types.put_enforced_guardrail_configuration_response
    import capo_bedrock.types.put_model_invocation_logging_configuration_request
    import capo_bedrock.types.put_model_invocation_logging_configuration_response
    import capo_bedrock.types.put_resource_policy_request
    import capo_bedrock.types.put_resource_policy_response
    import capo_bedrock.types.put_use_case_for_model_access_request
    import capo_bedrock.types.put_use_case_for_model_access_response
    import capo_bedrock.types.register_marketplace_model_endpoint_request
    import capo_bedrock.types.register_marketplace_model_endpoint_response
    import capo_bedrock.types.resource_policy_document
    import capo_bedrock.types.resource_policy_resource_arn
    import capo_bedrock.types.role_arn
    import capo_bedrock.types.routing_criteria
    import capo_bedrock.types.sort_by_provisioned_models
    import capo_bedrock.types.sort_jobs_by
    import capo_bedrock.types.sort_models_by
    import capo_bedrock.types.sort_order
    import capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request
    import capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response
    import capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request
    import capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response
    import capo_bedrock.types.stop_advanced_prompt_optimization_job_request
    import capo_bedrock.types.stop_advanced_prompt_optimization_job_response
    import capo_bedrock.types.stop_evaluation_job_request
    import capo_bedrock.types.stop_evaluation_job_response
    import capo_bedrock.types.stop_model_customization_job_request
    import capo_bedrock.types.stop_model_customization_job_response
    import capo_bedrock.types.stop_model_invocation_job_request
    import capo_bedrock.types.stop_model_invocation_job_response
    import capo_bedrock.types.tag_key_list
    import capo_bedrock.types.tag_list
    import capo_bedrock.types.tag_resource_request
    import capo_bedrock.types.tag_resource_response
    import capo_bedrock.types.taggable_resources_arn
    import capo_bedrock.types.timestamp
    import capo_bedrock.types.training_data_config
    import capo_bedrock.types.untag_resource_request
    import capo_bedrock.types.untag_resource_response
    import capo_bedrock.types.update_automated_reasoning_policy_annotations_request
    import capo_bedrock.types.update_automated_reasoning_policy_annotations_response
    import capo_bedrock.types.update_automated_reasoning_policy_request
    import capo_bedrock.types.update_automated_reasoning_policy_response
    import capo_bedrock.types.update_automated_reasoning_policy_test_case_request
    import capo_bedrock.types.update_automated_reasoning_policy_test_case_response
    import capo_bedrock.types.update_custom_model_deployment_request
    import capo_bedrock.types.update_custom_model_deployment_response
    import capo_bedrock.types.update_guardrail_request
    import capo_bedrock.types.update_guardrail_response
    import capo_bedrock.types.update_marketplace_model_endpoint_request
    import capo_bedrock.types.update_marketplace_model_endpoint_response
    import capo_bedrock.types.update_provisioned_model_throughput_request
    import capo_bedrock.types.update_provisioned_model_throughput_response
    import capo_bedrock.types.validation_data_config
    import capo_bedrock.types.vpc_config


class AsyncBedrockClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    bearer_provider: BearerTokenProvider | None


class AsyncBedrockClient:
    """A client for the ``Bedrock`` service.

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
        bearer: Bearer token for authentication.
        bearer_provider: Provider that resolves bearer tokens. Takes precedence over ``bearer``.
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
        bearer: str | None = None,
        bearer_provider: BearerTokenProvider | None = None,
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
        if (
            resolved_credentials_provider is None
            and credentials is None
            and bearer is None
            and bearer_provider is None
        ):
            resolved_credentials_provider = default_aws_credentials_chain(
                AsyncClient(http_handler)
            )
        if bearer is not None and bearer_provider is not None:
            warnings.warn(
                "Both bearer and bearer_provider given; provider takes precedence"
            )
        if bearer_provider is None and bearer is not None:
            bearer_provider = StaticBearerTokenProvider(bearer)
        self._config = AsyncBedrockClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "region": region,
                "use_dual_stack": use_dual_stack,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "credentials_provider": resolved_credentials_provider,
                "bearer_provider": bearer_provider,
            }
        )

        # resources
        self.advanced_prompt_optimization_job_resource = (
            AsyncAdvancedPromptOptimizationJobResource(self)
        )
        self.allowlist_resource = AsyncAllowlistResource(self)
        self.automated_reasoning_policy_resource = (
            AsyncAutomatedReasoningPolicyResource(self)
        )
        self.bedrock_marketplace_resource = AsyncBedrockMarketplaceResource(self)
        self.custom_model_deployment_resource = AsyncCustomModelDeploymentResource(self)
        self.custom_model_resource = AsyncCustomModelResource(self)
        self.data_retention_resource = AsyncDataRetentionResource(self)
        self.enforced_guardrail_configuration_resource = (
            AsyncEnforcedGuardrailConfigurationResource(self)
        )
        self.evaluation_job_resource = AsyncEvaluationJobResource(self)
        self.guardrails_resource = AsyncGuardrailsResource(self)
        self.inference_profile_resource = AsyncInferenceProfileResource(self)
        self.logging_resource = AsyncLoggingResource(self)
        self.model_copy_resource = AsyncModelCopyResource(self)
        self.model_import_resource = AsyncModelImportResource(self)
        self.model_invocation_job_resource = AsyncModelInvocationJobResource(self)
        self.model_resource = AsyncModelResource(self)
        self.prompt_router_resource = AsyncPromptRouterResource(self)
        self.provisioned_model_throughput_resource = (
            AsyncProvisionedModelThroughputResource(self)
        )
        self.resource_policy_resource = AsyncResourcePolicyResource(self)
        self.subscription_resource = AsyncSubscriptionResource(self)
        self.tagging_resource = AsyncTaggingResource(self)
        self.training_resource = AsyncTrainingResource(self)

    def operation_options(
        self, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncBedrockClientConfig = config_overrides or {}
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
            bearer_provider=overrides.get(
                "bearer_provider", self._config.get("bearer_provider")
            ),
        )
        return interceptors_, options_

    async def batch_delete_advanced_prompt_optimization_job(
        self,
        job_identifiers: "capo_bedrock.types.advanced_prompt_optimization_job_identifiers.AdvancedPromptOptimizationJobIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse":
        """<p>Deletes one or more advanced prompt optimization jobs.</p>

        Args:
            job_identifiers: <p>A list of advanced prompt optimization job identifiers (ARNs or IDs) to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_response.BatchDeleteAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_advanced_prompt_optimization_job.async_batch_delete_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.batch_delete_advanced_prompt_optimization_job_request.BatchDeleteAdvancedPromptOptimizationJobRequest = {
            "job_identifiers": job_identifiers
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_advanced_prompt_optimization_job(
        self,
        job_name: "capo_bedrock.types.advanced_prompt_optimization_job_name.AdvancedPromptOptimizationJobName",
        input_config: "capo_bedrock.types.advanced_prompt_optimization_input_config.AdvancedPromptOptimizationInputConfig",
        output_config: "capo_bedrock.types.advanced_prompt_optimization_output_config.AdvancedPromptOptimizationOutputConfig",
        model_configurations: "capo_bedrock.types.model_configurations.ModelConfigurations",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_description: Optional[
            "capo_bedrock.types.advanced_prompt_optimization_job_description.AdvancedPromptOptimizationJobDescription"
        ] = None,
        client_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        encryption_key_arn: Optional["capo_bedrock.types.kms_key_arn.KmsKeyArn"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse":
        """<p>Creates an advanced prompt optimization job. The job optimizes your prompt templates for specific models using your evaluation dataset and criteria.</p>

        Args:
            job_name: <p>A name for the advanced prompt optimization job.</p>
            job_description: <p>A description of the advanced prompt optimization job.</p>
            client_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but does not return an error.</p>
            input_config: <p>Specifies the S3 location of your JSONL input file containing prompt templates and evaluation samples.</p>
            output_config: <p>Specifies the S3 location where optimization results will be stored.</p>
            encryption_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key used for encrypting the output data. If not specified, the output is encrypted with an Amazon-owned KMS key.</p>
            tags: <p>Tags to associate with the advanced prompt optimization job.</p>
            model_configurations: <p>A list of model configurations specifying the target models for prompt optimization. You can specify up to 5 models.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_advanced_prompt_optimization_job_response.CreateAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_advanced_prompt_optimization_job.async_create_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_advanced_prompt_optimization_job_request.CreateAdvancedPromptOptimizationJobRequest = {
            "job_name": job_name,
            "input_config": input_config,
            "output_config": output_config,
            "model_configurations": model_configurations,
        }
        if job_description is not None:
            input_["job_description"] = job_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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

    async def get_advanced_prompt_optimization_job(
        self,
        job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse":
        """<p>Gets information about an advanced prompt optimization job.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_advanced_prompt_optimization_job_response.GetAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_advanced_prompt_optimization_job.async_get_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_advanced_prompt_optimization_job_request.GetAdvancedPromptOptimizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_advanced_prompt_optimization_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse":
        """<p>Lists the advanced prompt optimization jobs in your account.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token in a subsequent request to get the next set of results.</p>
            sort_by: <p>The field to sort the results by.</p>
            sort_order: <p>The sort order for the results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_advanced_prompt_optimization_jobs_response.ListAdvancedPromptOptimizationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_advanced_prompt_optimization_jobs.async_list_advanced_prompt_optimization_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_advanced_prompt_optimization_jobs_request.ListAdvancedPromptOptimizationJobsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_advanced_prompt_optimization_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.advanced_prompt_optimization_job_summary.AdvancedPromptOptimizationJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_advanced_prompt_optimization_jobs(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def stop_advanced_prompt_optimization_job(
        self,
        job_identifier: "capo_bedrock.types.advanced_prompt_optimization_job_identifier.AdvancedPromptOptimizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse":
        """<p>Stops an advanced prompt optimization job that is in progress.</p>

        Args:
            job_identifier: <p>The ARN or ID of the advanced prompt optimization job to stop.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.stop_advanced_prompt_optimization_job_response.StopAdvancedPromptOptimizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_advanced_prompt_optimization_job.async_stop_advanced_prompt_optimization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_advanced_prompt_optimization_job_request.StopAdvancedPromptOptimizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_use_case_for_model_access(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "capo_bedrock.types.get_use_case_for_model_access_response.GetUseCaseForModelAccessResponse":
        """<p>Get usecase for model access.</p>

        Raises:
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_use_case_for_model_access_request.GetUseCaseForModelAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_use_case_for_model_access_response.GetUseCaseForModelAccessResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_use_case_for_model_access

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_use_case_for_model_access.async_get_use_case_for_model_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_use_case_for_model_access_request.GetUseCaseForModelAccessRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_use_case_for_model_access(
        self,
        form_data: "capo_bedrock.types.acknowledgement_form_data_body.AcknowledgementFormDataBody",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_use_case_for_model_access_response.PutUseCaseForModelAccessResponse":
        """<p>Put usecase for model access.</p>

        Args:
            form_data: <p>Put customer profile Request.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_use_case_for_model_access_request.PutUseCaseForModelAccessRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_use_case_for_model_access_response.PutUseCaseForModelAccessResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_use_case_for_model_access

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_use_case_for_model_access.async_put_use_case_for_model_access(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.put_use_case_for_model_access_request.PutUseCaseForModelAccessRequest = {
            "form_data": form_data
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_automated_reasoning_policy(
        self,
        name: "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        policy_definition: Optional[
            "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse":
        """<p>Creates an Automated Reasoning policy for Amazon Bedrock Guardrails. Automated Reasoning policies use mathematical techniques to detect hallucinations, suggest corrections, and highlight unstated assumptions in the responses of your GenAI application.</p> <p>To create a policy, you upload a source document that describes the rules that you're encoding. Automated Reasoning extracts important concepts from the source document that will become variables in the policy and infers policy rules.</p>

        Args:
            name: <p>A unique name for the Automated Reasoning policy. The name must be between 1 and 63 characters and can contain letters, numbers, hyphens, and underscores.</p>
            description: <p>A description of the Automated Reasoning policy. Use this to provide context about the policy's purpose and the types of validations it performs.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>
            policy_definition: <p>The policy definition that contains the formal logic rules, variables, and custom variable types used to validate foundation model responses in your application.</p>
            kms_key_id: <p>The identifier of the KMS key to use for encrypting the automated reasoning policy and its associated artifacts. If you don't specify a KMS key, Amazon Bedrock uses an KMS managed key for encryption. For enhanced security and control, you can specify a customer managed KMS key.</p>
            tags: <p>A list of tags to associate with the Automated Reasoning policy. Tags help you organize and manage your policies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_response.CreateAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy.async_create_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_automated_reasoning_policy_request.CreateAutomatedReasoningPolicyRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if policy_definition is not None:
            input_["policy_definition"] = policy_definition
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse":
        """<p>Retrieves details about an Automated Reasoning policy or policy version. Returns information including the policy definition, metadata, and timestamps.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to retrieve. Can be either the unversioned ARN for the draft policy or an ARN for a specific policy version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_request.GetAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_response.GetAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy.async_get_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_automated_reasoning_policy_request.GetAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_automated_reasoning_policy(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        policy_definition: "capo_bedrock.types.automated_reasoning_policy_definition.AutomatedReasoningPolicyDefinition",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        name: Optional[
            "capo_bedrock.types.automated_reasoning_policy_name.AutomatedReasoningPolicyName"
        ] = None,
        description: Optional[
            "capo_bedrock.types.automated_reasoning_policy_description.AutomatedReasoningPolicyDescription"
        ] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse":
        """<p>Updates an existing Automated Reasoning policy with new rules, variables, or configuration. This creates a new version of the policy while preserving the previous version.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to update. This must be the ARN of a draft policy.</p>
            policy_definition: <p>The updated policy definition containing the formal logic rules, variables, and types.</p>
            name: <p>The updated name for the Automated Reasoning policy.</p>
            description: <p>The updated description for the Automated Reasoning policy.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_response.UpdateAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy.async_update_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.update_automated_reasoning_policy_request.UpdateAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn,
            "policy_definition": policy_definition,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_automated_reasoning_policy(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        force: Optional[bool] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_response.DeleteAutomatedReasoningPolicyResponse":
        """<p>Deletes an Automated Reasoning policy or policy version. This operation is idempotent. If you delete a policy more than once, each call succeeds. Deleting a policy removes it permanently and cannot be undone.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to delete.</p>
            force: <p>Specifies whether to force delete the automated reasoning policy even if it has active resources. When <code>false</code>, Amazon Bedrock validates if all artifacts have been deleted (e.g. policy version, test case, test result) for a policy before deletion. When <code>true</code>, Amazon Bedrock will delete the policy and all its artifacts without validation. Default is <code>false</code>. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_request.DeleteAutomatedReasoningPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_response.DeleteAutomatedReasoningPolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy.async_delete_automated_reasoning_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_automated_reasoning_policy_request.DeleteAutomatedReasoningPolicyRequest = {
            "policy_arn": policy_arn
        }
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_automated_reasoning_policies(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        policy_arn: Optional[
            "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
        ] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse":
        """<p>Lists all Automated Reasoning policies in your account, with optional filtering by policy ARN. This helps you manage and discover existing policies.</p>

        Args:
            policy_arn: <p>Optional filter to list only the policy versions with the specified Amazon Resource Name (ARN). If not provided, the DRAFT versions for all policies are listed.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of policies to return in a single call.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policies_request.ListAutomatedReasoningPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policies_response.ListAutomatedReasoningPoliciesResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policies

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policies.async_list_automated_reasoning_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_automated_reasoning_policies_request.ListAutomatedReasoningPoliciesRequest = {}
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
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

    async def iter_list_automated_reasoning_policies(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        policy_arn: Optional[
            "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn"
        ] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.automated_reasoning_policy_summary.AutomatedReasoningPolicySummary]":
        _token = next_token
        while True:
            _response = await self.list_automated_reasoning_policies(
                config_overrides=config_overrides,
                policy_arn=policy_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("automated_reasoning_policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def cancel_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response.CancelAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Cancels a running Automated Reasoning policy build workflow. This stops the policy generation process and prevents further processing of the source documents.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to cancel.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to cancel. You can get this ID from the StartAutomatedReasoningPolicyBuildWorkflow response or by listing build workflows.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request.CancelAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_response.CancelAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.cancel_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.cancel_automated_reasoning_policy_build_workflow.async_cancel_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.cancel_automated_reasoning_policy_build_workflow_request.CancelAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent",
        expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        query_content: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        confidence_threshold: Optional[
            "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
        ] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_test_case_response.CreateAutomatedReasoningPolicyTestCaseResponse":
        """<p>Creates a test for an Automated Reasoning policy. Tests validate that your policy works as expected by providing sample inputs and expected outcomes. Use tests to verify policy behavior before deploying to production.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create the test.</p>
            guard_content: <p>The output content that's validated by the Automated Reasoning policy. This represents the foundation model response that will be checked for accuracy.</p>
            query_content: <p>The input query or prompt that generated the content. This provides context for the validation.</p>
            expected_aggregated_findings_result: <p>The expected result of the Automated Reasoning check. Valid values include: , TOO_COMPLEX, and NO_TRANSLATIONS.</p> <ul> <li> <p> <code>VALID</code> - The claims are true. The claims are implied by the premises and the Automated Reasoning policy. Given the Automated Reasoning policy and premises, it is not possible for these claims to be false. In other words, there are no alternative answers that are true that contradict the claims.</p> </li> <li> <p> <code>INVALID</code> - The claims are false. The claims are not implied by the premises and Automated Reasoning policy. Furthermore, there exists different claims that are consistent with the premises and Automated Reasoning policy.</p> </li> <li> <p> <code>SATISFIABLE</code> - The claims can be true or false. It depends on what assumptions are made for the claim to be implied from the premises and Automated Reasoning policy rules. In this situation, different assumptions can make input claims false and alternative claims true.</p> </li> <li> <p> <code>IMPOSSIBLE</code> - Automated Reasoning can’t make a statement about the claims. This can happen if the premises are logically incorrect, or if there is a conflict within the Automated Reasoning policy itself.</p> </li> <li> <p> <code>TRANSLATION_AMBIGUOUS</code> - Detected an ambiguity in the translation meant it would be unsound to continue with validity checking. Additional context or follow-up questions might be needed to get translation to succeed.</p> </li> <li> <p> <code>TOO_COMPLEX</code> - The input contains too much information for Automated Reasoning to process within its latency limits.</p> </li> <li> <p> <code>NO_TRANSLATIONS</code> - Identifies that some or all of the input prompt wasn't translated into logic. This can happen if the input isn't relevant to the Automated Reasoning policy, or if the policy doesn't have variables to model relevant input. If Automated Reasoning can't translate anything, you get a single <code>NO_TRANSLATIONS</code> finding. You might also see a <code>NO_TRANSLATIONS</code> (along with other findings) if some part of the validation isn't translated.</p> </li> </ul>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
            confidence_threshold: <p>The minimum confidence level for logic validation. Content that meets the threshold is considered a high-confidence finding that can be validated.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_test_case_response.CreateAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_test_case.async_create_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_automated_reasoning_policy_test_case_request.CreateAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "guard_content": guard_content,
            "expected_aggregated_findings_result": expected_aggregated_findings_result,
        }
        if query_content is not None:
            input_["query_content"] = query_content
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_automated_reasoning_policy_version(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        last_updated_definition_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse":
        """<p>Creates a new version of an existing Automated Reasoning policy. This allows you to iterate on your policy rules while maintaining previous versions for rollback or comparison purposes.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to create a version.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>
            last_updated_definition_hash: <p>The hash of the current policy definition used as a concurrency token to ensure the policy hasn't been modified since you last retrieved it.</p>
            tags: <p>A list of tags to associate with the policy version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_automated_reasoning_policy_version_request.CreateAutomatedReasoningPolicyVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_automated_reasoning_policy_version_response.CreateAutomatedReasoningPolicyVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_version

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_automated_reasoning_policy_version.async_create_automated_reasoning_policy_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_automated_reasoning_policy_version_request.CreateAutomatedReasoningPolicyVersionRequest = {
            "policy_arn": policy_arn,
            "last_updated_definition_hash": last_updated_definition_hash,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response.DeleteAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Deletes an Automated Reasoning policy build workflow and its associated artifacts. This permanently removes the workflow history and any generated assets.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to delete.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to delete.</p>
            last_updated_at: <p>The timestamp when the build workflow was last updated. This is used for optimistic concurrency control to prevent accidental deletion of workflows that have been modified.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request.DeleteAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_response.DeleteAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_build_workflow.async_delete_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_automated_reasoning_policy_build_workflow_request.DeleteAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "last_updated_at": last_updated_at,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_automated_reasoning_policy_test_case_response.DeleteAutomatedReasoningPolicyTestCaseResponse":
        """<p>Deletes an Automated Reasoning policy test. This operation is idempotent; if you delete a test more than once, each call succeeds.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to delete.</p>
            last_updated_at: <p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_automated_reasoning_policy_test_case_request.DeleteAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_automated_reasoning_policy_test_case_response.DeleteAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_automated_reasoning_policy_test_case.async_delete_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_automated_reasoning_policy_test_case_request.DeleteAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
            "last_updated_at": last_updated_at,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def export_automated_reasoning_policy_version(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse":
        """<p>Exports the policy definition for an Automated Reasoning policy version. Returns the complete policy definition including rules, variables, and custom variable types in a structured format.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to export. Can be either the unversioned ARN for the draft policy or a versioned ARN for a specific policy version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.export_automated_reasoning_policy_version_request.ExportAutomatedReasoningPolicyVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.export_automated_reasoning_policy_version_response.ExportAutomatedReasoningPolicyVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.export_automated_reasoning_policy_version

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.export_automated_reasoning_policy_version.async_export_automated_reasoning_policy_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.export_automated_reasoning_policy_version_request.ExportAutomatedReasoningPolicyVersionRequest = {
            "policy_arn": policy_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_annotations(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse":
        """<p>Retrieves the current annotations for an Automated Reasoning policy build workflow. Annotations contain corrections to the rules, variables and types to be applied to the policy.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose annotations you want to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_annotations_request.GetAutomatedReasoningPolicyAnnotationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_annotations_response.GetAutomatedReasoningPolicyAnnotationsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_annotations

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_annotations.async_get_automated_reasoning_policy_annotations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_automated_reasoning_policy_annotations_request.GetAutomatedReasoningPolicyAnnotationsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Retrieves detailed information about an Automated Reasoning policy build workflow, including its status, configuration, and metadata.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request.GetAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_response.GetAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow.async_get_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_automated_reasoning_policy_build_workflow_request.GetAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_build_workflow_result_assets(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        asset_type: "capo_bedrock.types.automated_reasoning_policy_build_result_asset_type.AutomatedReasoningPolicyBuildResultAssetType",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        asset_id: Optional[
            "capo_bedrock.types.automated_reasoning_policy_build_result_asset_id.AutomatedReasoningPolicyBuildResultAssetId"
        ] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse":
        """<p>Retrieves the resulting assets from a completed Automated Reasoning policy build workflow, including build logs, quality reports, and generated policy artifacts.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflow assets you want to retrieve.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose result assets you want to retrieve.</p>
            asset_type: <p>The type of asset to retrieve (e.g., BUILD_LOG, QUALITY_REPORT, POLICY_DEFINITION, GENERATED_TEST_CASES, POLICY_SCENARIOS, FIDELITY_REPORT, ASSET_MANIFEST, SOURCE_DOCUMENT).</p>
            asset_id: <p>The unique identifier of the specific asset to retrieve when multiple assets of the same type exist. This is required when retrieving SOURCE_DOCUMENT assets, as multiple source documents may have been used in the workflow. The asset ID can be obtained from the asset manifest.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_response.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow_result_assets

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_build_workflow_result_assets.async_get_automated_reasoning_policy_build_workflow_result_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_automated_reasoning_policy_build_workflow_result_assets_request.GetAutomatedReasoningPolicyBuildWorkflowResultAssetsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "asset_type": asset_type,
        }
        if asset_id is not None:
            input_["asset_id"] = asset_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_next_scenario(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse":
        """<p>Retrieves the next test scenario for validating an Automated Reasoning policy. This is used during the interactive policy refinement process to test policy behavior.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which you want to get the next test scenario.</p>
            build_workflow_id: <p>The unique identifier of the build workflow associated with the test scenarios.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request.GetAutomatedReasoningPolicyNextScenarioRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_next_scenario_response.GetAutomatedReasoningPolicyNextScenarioResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_next_scenario

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_next_scenario.async_get_automated_reasoning_policy_next_scenario(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_automated_reasoning_policy_next_scenario_request.GetAutomatedReasoningPolicyNextScenarioRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse":
        """<p>Retrieves details about a specific Automated Reasoning policy test.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to retrieve.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_test_case_request.GetAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_test_case_response.GetAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_case.async_get_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_automated_reasoning_policy_test_case_request.GetAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automated_reasoning_policy_test_result(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse":
        """<p>Retrieves the test result for a specific Automated Reasoning policy test. Returns detailed validation findings and execution status.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy.</p>
            build_workflow_id: <p>The build workflow identifier. The build workflow must display a <code>COMPLETED</code> status to get results.</p>
            test_case_id: <p>The unique identifier of the test for which to retrieve results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_automated_reasoning_policy_test_result_request.GetAutomatedReasoningPolicyTestResultRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_automated_reasoning_policy_test_result_response.GetAutomatedReasoningPolicyTestResultResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_result

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_automated_reasoning_policy_test_result.async_get_automated_reasoning_policy_test_result(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_automated_reasoning_policy_test_result_request.GetAutomatedReasoningPolicyTestResultRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "test_case_id": test_case_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_automated_reasoning_policy_build_workflows(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response.ListAutomatedReasoningPolicyBuildWorkflowsResponse":
        """<p>Lists all build workflows for an Automated Reasoning policy, showing the history of policy creation and modification attempts.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose build workflows you want to list.</p>
            next_token: <p>A pagination token from a previous request to continue listing build workflows from where the previous request left off.</p>
            max_results: <p>The maximum number of build workflows to return in a single response. Valid range is 1-100.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request.ListAutomatedReasoningPolicyBuildWorkflowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_build_workflows_response.ListAutomatedReasoningPolicyBuildWorkflowsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_build_workflows

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_build_workflows.async_list_automated_reasoning_policy_build_workflows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_automated_reasoning_policy_build_workflows_request.ListAutomatedReasoningPolicyBuildWorkflowsRequest = {
            "policy_arn": policy_arn
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

    async def iter_list_automated_reasoning_policy_build_workflows(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.automated_reasoning_policy_build_workflow_summary.AutomatedReasoningPolicyBuildWorkflowSummary]":
        _token = next_token
        while True:
            _response = await self.list_automated_reasoning_policy_build_workflows(
                policy_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("automated_reasoning_policy_build_workflow_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automated_reasoning_policy_test_cases(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse":
        """<p>Lists tests for an Automated Reasoning policy. We recommend using pagination to ensure that the operation returns quickly and successfully.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to list tests.</p>
            next_token: <p>The pagination token from a previous request to retrieve the next page of results.</p>
            max_results: <p>The maximum number of tests to return in a single call.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policy_test_cases_request.ListAutomatedReasoningPolicyTestCasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_test_cases_response.ListAutomatedReasoningPolicyTestCasesResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_cases

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_cases.async_list_automated_reasoning_policy_test_cases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_automated_reasoning_policy_test_cases_request.ListAutomatedReasoningPolicyTestCasesRequest = {
            "policy_arn": policy_arn
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

    async def iter_list_automated_reasoning_policy_test_cases(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.automated_reasoning_policy_test_case.AutomatedReasoningPolicyTestCase]":
        _token = next_token
        while True:
            _response = await self.list_automated_reasoning_policy_test_cases(
                policy_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("test_cases",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_automated_reasoning_policy_test_results(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse":
        """<p>Lists test results for an Automated Reasoning policy, showing how the policy performed against various test scenarios and validation checks.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose test results you want to list.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose test results you want to list.</p>
            next_token: <p>A pagination token from a previous request to continue listing test results from where the previous request left off.</p>
            max_results: <p>The maximum number of test results to return in a single response. Valid range is 1-100.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_automated_reasoning_policy_test_results_request.ListAutomatedReasoningPolicyTestResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_automated_reasoning_policy_test_results_response.ListAutomatedReasoningPolicyTestResultsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_results

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_automated_reasoning_policy_test_results.async_list_automated_reasoning_policy_test_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_automated_reasoning_policy_test_results_request.ListAutomatedReasoningPolicyTestResultsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
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

    async def iter_list_automated_reasoning_policy_test_results(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.automated_reasoning_policy_test_result.AutomatedReasoningPolicyTestResult]":
        _token = next_token
        while True:
            _response = await self.list_automated_reasoning_policy_test_results(
                policy_arn,
                build_workflow_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("test_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def start_automated_reasoning_policy_build_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_type: "capo_bedrock.types.automated_reasoning_policy_build_workflow_type.AutomatedReasoningPolicyBuildWorkflowType",
        source_content: "capo_bedrock.types.automated_reasoning_policy_build_workflow_source.AutomatedReasoningPolicyBuildWorkflowSource",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response.StartAutomatedReasoningPolicyBuildWorkflowResponse":
        """<p>Starts a new build workflow for an Automated Reasoning policy. This initiates the process of analyzing source documents and generating policy rules, variables, and types.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy for which to start the build workflow.</p>
            build_workflow_type: <p>The type of build workflow to start (e.g., DOCUMENT_INGESTION for processing new documents, POLICY_REPAIR for fixing existing policies).</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>
            source_content: <p>The source content for the build workflow, such as documents to analyze or repair instructions for existing policies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.start_automated_reasoning_policy_build_workflow_response.StartAutomatedReasoningPolicyBuildWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_build_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_build_workflow.async_start_automated_reasoning_policy_build_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.start_automated_reasoning_policy_build_workflow_request.StartAutomatedReasoningPolicyBuildWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_type": build_workflow_type,
            "source_content": source_content,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_automated_reasoning_policy_test_workflow(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        test_case_ids: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_case_id_list.AutomatedReasoningPolicyTestCaseIdList"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response.StartAutomatedReasoningPolicyTestWorkflowResponse":
        """<p>Initiates a test workflow to validate Automated Reasoning policy tests. The workflow executes the specified tests against the policy and generates validation results.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy to test.</p>
            build_workflow_id: <p>The build workflow identifier. The build workflow must show a <code>COMPLETED</code> status before running tests.</p>
            test_case_ids: <p>The list of test identifiers to run. If not provided, all tests for the policy are run.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request but doesn't return an error.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request.StartAutomatedReasoningPolicyTestWorkflowRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.start_automated_reasoning_policy_test_workflow_response.StartAutomatedReasoningPolicyTestWorkflowResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_test_workflow

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.start_automated_reasoning_policy_test_workflow.async_start_automated_reasoning_policy_test_workflow(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.start_automated_reasoning_policy_test_workflow_request.StartAutomatedReasoningPolicyTestWorkflowRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
        }
        if test_case_ids is not None:
            input_["test_case_ids"] = test_case_ids
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_automated_reasoning_policy_annotations(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        build_workflow_id: "capo_bedrock.types.automated_reasoning_policy_build_workflow_id.AutomatedReasoningPolicyBuildWorkflowId",
        annotations: "capo_bedrock.types.automated_reasoning_policy_annotation_list.AutomatedReasoningPolicyAnnotationList",
        last_updated_annotation_set_hash: "capo_bedrock.types.automated_reasoning_policy_hash.AutomatedReasoningPolicyHash",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_annotations_response.UpdateAutomatedReasoningPolicyAnnotationsResponse":
        """<p>Updates the annotations for an Automated Reasoning policy build workflow. This allows you to modify extracted rules, variables, and types before finalizing the policy.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy whose annotations you want to update.</p>
            build_workflow_id: <p>The unique identifier of the build workflow whose annotations you want to update.</p>
            annotations: <p>The updated annotations containing modified rules, variables, and types for the policy.</p>
            last_updated_annotation_set_hash: <p>The hash value of the annotation set that you're updating. This is used for optimistic concurrency control to prevent conflicting updates.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_annotations_response.UpdateAutomatedReasoningPolicyAnnotationsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_annotations

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_annotations.async_update_automated_reasoning_policy_annotations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.update_automated_reasoning_policy_annotations_request.UpdateAutomatedReasoningPolicyAnnotationsRequest = {
            "policy_arn": policy_arn,
            "build_workflow_id": build_workflow_id,
            "annotations": annotations,
            "last_updated_annotation_set_hash": last_updated_annotation_set_hash,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_automated_reasoning_policy_test_case(
        self,
        policy_arn: "capo_bedrock.types.automated_reasoning_policy_arn.AutomatedReasoningPolicyArn",
        test_case_id: "capo_bedrock.types.automated_reasoning_policy_test_case_id.AutomatedReasoningPolicyTestCaseId",
        guard_content: "capo_bedrock.types.automated_reasoning_policy_test_guard_content.AutomatedReasoningPolicyTestGuardContent",
        last_updated_at: "capo_bedrock.types.timestamp.Timestamp",
        expected_aggregated_findings_result: "capo_bedrock.types.automated_reasoning_check_result.AutomatedReasoningCheckResult",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        query_content: Optional[
            "capo_bedrock.types.automated_reasoning_policy_test_query_content.AutomatedReasoningPolicyTestQueryContent"
        ] = None,
        confidence_threshold: Optional[
            "capo_bedrock.types.automated_reasoning_check_translation_confidence.AutomatedReasoningCheckTranslationConfidence"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.update_automated_reasoning_policy_test_case_response.UpdateAutomatedReasoningPolicyTestCaseResponse":
        """<p>Updates an existing Automated Reasoning policy test. You can modify the content, query, expected result, and confidence threshold.</p>

        Args:
            policy_arn: <p>The Amazon Resource Name (ARN) of the Automated Reasoning policy that contains the test.</p>
            test_case_id: <p>The unique identifier of the test to update.</p>
            guard_content: <p>The updated content to be validated by the Automated Reasoning policy.</p>
            query_content: <p>The updated input query or prompt that generated the content.</p>
            last_updated_at: <p>The timestamp when the test was last updated. This is used as a concurrency token to prevent conflicting modifications.</p>
            expected_aggregated_findings_result: <p>The updated expected result of the Automated Reasoning check.</p>
            confidence_threshold: <p>The updated minimum confidence level for logic validation. If null is provided, the threshold will be removed.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_automated_reasoning_policy_test_case_response.UpdateAutomatedReasoningPolicyTestCaseResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_test_case

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_automated_reasoning_policy_test_case.async_update_automated_reasoning_policy_test_case(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.update_automated_reasoning_policy_test_case_request.UpdateAutomatedReasoningPolicyTestCaseRequest = {
            "policy_arn": policy_arn,
            "test_case_id": test_case_id,
            "guard_content": guard_content,
            "last_updated_at": last_updated_at,
            "expected_aggregated_findings_result": expected_aggregated_findings_result,
        }
        if query_content is not None:
            input_["query_content"] = query_content
        if confidence_threshold is not None:
            input_["confidence_threshold"] = confidence_threshold
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_marketplace_model_endpoint(
        self,
        model_source_identifier: "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig",
        endpoint_name: "capo_bedrock.types.endpoint_name.EndpointName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        accept_eula: Optional["capo_bedrock.types.accept_eula.AcceptEula"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse":
        """<p>Creates an endpoint for a model from Amazon Bedrock Marketplace. The endpoint is hosted by Amazon SageMaker.</p>

        Args:
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that you want to deploy to the endpoint.</p>
            endpoint_config: <p>The configuration for the endpoint, including the number and type of instances to use.</p>
            accept_eula: <p>Indicates whether you accept the end-user license agreement (EULA) for the model. Set to <code>true</code> to accept the EULA.</p>
            endpoint_name: <p>The name of the endpoint. This name must be unique within your Amazon Web Services account and region.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>
            tags: <p>An array of key-value pairs to apply to the underlying Amazon SageMaker endpoint. You can use these tags to organize and identify your Amazon Web Services resources.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_marketplace_model_endpoint_response.CreateMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_marketplace_model_endpoint.async_create_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_marketplace_model_endpoint_request.CreateMarketplaceModelEndpointRequest = {
            "model_source_identifier": model_source_identifier,
            "endpoint_config": endpoint_config,
            "endpoint_name": endpoint_name,
        }
        if accept_eula is not None:
            input_["accept_eula"] = accept_eula
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse":
        """<p>Deletes an endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_marketplace_model_endpoint_response.DeleteMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_marketplace_model_endpoint.async_delete_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_marketplace_model_endpoint_request.DeleteMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse":
        """<p>Deregisters an endpoint for a model from Amazon Bedrock Marketplace. This operation removes the endpoint's association with Amazon Bedrock but does not delete the underlying Amazon SageMaker endpoint.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to deregister.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.deregister_marketplace_model_endpoint_response.DeregisterMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.deregister_marketplace_model_endpoint.async_deregister_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.deregister_marketplace_model_endpoint_request.DeregisterMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse":
        """<p>Retrieves details about a specific endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to get information about.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_marketplace_model_endpoint_response.GetMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_marketplace_model_endpoint.async_get_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_marketplace_model_endpoint_request.GetMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_marketplace_model_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        model_source_equals: Optional[
            "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier"
        ] = None,
    ) -> "capo_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse":
        """<p>Lists the endpoints for models from Amazon Bedrock Marketplace in your Amazon Web Services account.</p>

        Args:
            max_results: <p>The maximum number of results to return in a single call. If more results are available, the operation returns a <code>NextToken</code> value.</p>
            next_token: <p>The token for the next set of results. You receive this token from a previous <code>ListMarketplaceModelEndpoints</code> call.</p>
            model_source_equals: <p>If specified, only endpoints for the given model source identifier are returned.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_marketplace_model_endpoints_response.ListMarketplaceModelEndpointsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_marketplace_model_endpoints.async_list_marketplace_model_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_marketplace_model_endpoints_request.ListMarketplaceModelEndpointsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if model_source_equals is not None:
            input_["model_source_equals"] = model_source_equals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_marketplace_model_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        model_source_equals: Optional[
            "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock.types.marketplace_model_endpoint_summary.MarketplaceModelEndpointSummary]":
        _token = next_token
        while True:
            _response = await self.list_marketplace_model_endpoints(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                model_source_equals=model_source_equals,
            )
            _page = _resolve_path(_response, ("marketplace_model_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def register_marketplace_model_endpoint(
        self,
        endpoint_identifier: "capo_bedrock.types.arn.Arn",
        model_source_identifier: "capo_bedrock.types.model_source_identifier.ModelSourceIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse":
        """<p>Registers an existing Amazon SageMaker endpoint with Amazon Bedrock Marketplace, allowing it to be used with Amazon Bedrock APIs.</p>

        Args:
            endpoint_identifier: <p>The ARN of the Amazon SageMaker endpoint you want to register with Amazon Bedrock Marketplace.</p>
            model_source_identifier: <p>The ARN of the model from Amazon Bedrock Marketplace that is deployed on the endpoint.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_unavailable_exception.ServiceUnavailableException: <p>Returned if the service cannot complete the request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.register_marketplace_model_endpoint_response.RegisterMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.register_marketplace_model_endpoint.async_register_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.register_marketplace_model_endpoint_request.RegisterMarketplaceModelEndpointRequest = {
            "endpoint_identifier": endpoint_identifier,
            "model_source_identifier": model_source_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_marketplace_model_endpoint(
        self,
        endpoint_arn: "capo_bedrock.types.arn.Arn",
        endpoint_config: "capo_bedrock.types.endpoint_config.EndpointConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse":
        """<p>Updates the configuration of an existing endpoint for a model from Amazon Bedrock Marketplace.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) of the endpoint you want to update.</p>
            endpoint_config: <p>The new configuration for the endpoint, including the number and type of instances to use.</p>
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This token is listed as not required because Amazon Web Services SDKs automatically generate it for you and set this parameter. If you're not using the Amazon Web Services SDK or the CLI, you must provide this token or the action will fail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_marketplace_model_endpoint_response.UpdateMarketplaceModelEndpointResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_marketplace_model_endpoint.async_update_marketplace_model_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.update_marketplace_model_endpoint_request.UpdateMarketplaceModelEndpointRequest = {
            "endpoint_arn": endpoint_arn,
            "endpoint_config": endpoint_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_model_deployment(
        self,
        model_deployment_name: "capo_bedrock.types.model_deployment_name.ModelDeploymentName",
        model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.custom_model_deployment_description.CustomModelDeploymentDescription"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_custom_model_deployment_response.CreateCustomModelDeploymentResponse":
        """<p>Deploys a custom model for on-demand inference in Amazon Bedrock. After you deploy your custom model, you use the deployment's Amazon Resource Name (ARN) as the <code>modelId</code> parameter when you submit prompts and generate responses with model inference.</p> <p> For more information about setting up on-demand inference for custom models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-use.html">Set up inference for a custom model</a>. </p> <p>The following actions are related to the <code>CreateCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            model_deployment_name: <p>The name for the custom model deployment. The name must be unique within your Amazon Web Services account and Region.</p>
            model_arn: <p>The Amazon Resource Name (ARN) of the custom model to deploy for on-demand inference. The custom model must be in the <code>Active</code> state.</p>
            description: <p>A description for the custom model deployment to help you identify its purpose.</p>
            tags: <p>Tags to assign to the custom model deployment. You can use tags to organize and track your Amazon Web Services resources for cost allocation and management purposes.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the operation completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_custom_model_deployment_request.CreateCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_custom_model_deployment_response.CreateCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model_deployment.async_create_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_custom_model_deployment_request.CreateCustomModelDeploymentRequest = {
            "model_deployment_name": model_deployment_name,
            "model_arn": model_arn,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_model_deployment(
        self,
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_custom_model_deployment_response.DeleteCustomModelDeploymentResponse":
        """<p>Deletes a custom model deployment. This operation stops the deployment and removes it from your account. After deletion, the deployment ARN can no longer be used for inference requests.</p> <p>The following actions are related to the <code>DeleteCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> </ul>

        Args:
            custom_model_deployment_identifier: <p>The Amazon Resource Name (ARN) or name of the custom model deployment to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_custom_model_deployment_request.DeleteCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_custom_model_deployment_response.DeleteCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model_deployment.async_delete_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_custom_model_deployment_request.DeleteCustomModelDeploymentRequest = {
            "custom_model_deployment_identifier": custom_model_deployment_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_custom_model_deployment(
        self,
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_custom_model_deployment_response.GetCustomModelDeploymentResponse":
        """<p>Retrieves information about a custom model deployment, including its status, configuration, and metadata. Use this operation to monitor the deployment status and retrieve details needed for inference requests.</p> <p>The following actions are related to the <code>GetCustomModelDeployment</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModelDeployments.html">ListCustomModelDeployments</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            custom_model_deployment_identifier: <p>The Amazon Resource Name (ARN) or name of the custom model deployment to retrieve information about.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_custom_model_deployment_request.GetCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_custom_model_deployment_response.GetCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model_deployment.async_get_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_custom_model_deployment_request.GetCustomModelDeploymentRequest = {
            "custom_model_deployment_identifier": custom_model_deployment_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_model_deployments(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        created_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        created_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        status_equals: Optional[
            "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
        ] = None,
        model_arn_equals: Optional[
            "capo_bedrock.types.custom_model_arn.CustomModelArn"
        ] = None,
    ) -> "capo_bedrock.types.list_custom_model_deployments_response.ListCustomModelDeploymentsResponse":
        """<p>Lists custom model deployments in your account. You can filter the results by creation time, name, status, and associated model. Use this operation to manage and monitor your custom model deployments.</p> <p>We recommend using pagination to ensure that the operation returns quickly and successfully.</p> <p>The following actions are related to the <code>ListCustomModelDeployments</code> operation:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_CreateCustomModelDeployment.html">CreateCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModelDeployment.html">GetCustomModelDeployment</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModelDeployment.html">DeleteCustomModelDeployment</a> </p> </li> </ul>

        Args:
            created_before: <p>Filters deployments created before the specified date and time.</p>
            created_after: <p>Filters deployments created after the specified date and time.</p>
            name_contains: <p>Filters deployments whose names contain the specified string. </p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next set of results. Use this token to retrieve additional results when the response is truncated.</p>
            sort_by: <p>The field to sort the results by. The only supported value is <code>CreationTime</code>.</p>
            sort_order: <p>The sort order for the results. Valid values are <code>Ascending</code> and <code>Descending</code>. Default is <code>Descending</code>.</p>
            status_equals: <p>Filters deployments by status. Valid values are <code>CREATING</code>, <code>ACTIVE</code>, and <code>FAILED</code>.</p>
            model_arn_equals: <p>Filters deployments by the Amazon Resource Name (ARN) of the associated custom model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_custom_model_deployments_request.ListCustomModelDeploymentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_custom_model_deployments_response.ListCustomModelDeploymentsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_model_deployments

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_model_deployments.async_list_custom_model_deployments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_custom_model_deployments_request.ListCustomModelDeploymentsRequest = {}
        if created_before is not None:
            input_["created_before"] = created_before
        if created_after is not None:
            input_["created_after"] = created_after
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if model_arn_equals is not None:
            input_["model_arn_equals"] = model_arn_equals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_custom_model_deployments(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        created_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        created_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.model_deployment_name.ModelDeploymentName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        status_equals: Optional[
            "capo_bedrock.types.custom_model_deployment_status.CustomModelDeploymentStatus"
        ] = None,
        model_arn_equals: Optional[
            "capo_bedrock.types.custom_model_arn.CustomModelArn"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock.types.custom_model_deployment_summary.CustomModelDeploymentSummary]":
        _token = next_token
        while True:
            _response = await self.list_custom_model_deployments(
                config_overrides=config_overrides,
                created_before=created_before,
                created_after=created_after,
                name_contains=name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
                status_equals=status_equals,
                model_arn_equals=model_arn_equals,
            )
            _page = _resolve_path(_response, ("model_deployment_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_custom_model_deployment(
        self,
        model_arn: "capo_bedrock.types.custom_model_arn.CustomModelArn",
        custom_model_deployment_identifier: "capo_bedrock.types.custom_model_deployment_identifier.CustomModelDeploymentIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.update_custom_model_deployment_response.UpdateCustomModelDeploymentResponse":
        """<p> Updates a custom model deployment with a new custom model. This allows you to deploy updated models without creating new deployment endpoints. </p>

        Args:
            model_arn: <p> ARN of the new custom model to deploy. This replaces the currently deployed model. </p>
            custom_model_deployment_identifier: <p> Identifier of the custom model deployment to update with the new custom model. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_custom_model_deployment_request.UpdateCustomModelDeploymentRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_custom_model_deployment_response.UpdateCustomModelDeploymentResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_custom_model_deployment

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_custom_model_deployment.async_update_custom_model_deployment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.update_custom_model_deployment_request.UpdateCustomModelDeploymentRequest = {
            "model_arn": model_arn,
            "custom_model_deployment_identifier": custom_model_deployment_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_custom_model(
        self,
        model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        model_source_config: Optional[
            "capo_bedrock.types.model_data_source.ModelDataSource"
        ] = None,
        custom_model_data_source: Optional[
            "capo_bedrock.types.custom_model_data_source.CustomModelDataSource"
        ] = None,
        model_kms_key_arn: Optional["capo_bedrock.types.kms_key_arn.KmsKeyArn"] = None,
        role_arn: Optional["capo_bedrock.types.role_arn.RoleArn"] = None,
        model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_custom_model_response.CreateCustomModelResponse":
        """<p>Creates a new custom model in Amazon Bedrock. After the model is active, you can use it for inference.</p> <p>You can provide the model data source in one of the following ways:</p> <ul> <li> <p> <code>customModelDataSource</code> — Specify a SageMaker AI model package ARN. Amazon Bedrock resolves the model package to retrieve the model artifacts. This is the preferred method for new SageMaker AI training outputs.</p> </li> <li> <p> <code>modelSourceConfig</code> — Specify an Amazon S3 URI pointing to the Amazon-managed Amazon S3 bucket containing your model artifacts.</p> </li> </ul> <p>To use the model for inference, you must purchase Provisioned Throughput for it. You can't use On-demand inference with these custom models. For more information about Provisioned Throughput, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a>.</p> <p>The model appears in <code>ListCustomModels</code> with a <code>customizationType</code> of <code>imported</code>. To track the status of the new model, you use the <code>GetCustomModel</code> API operation. The model can be in the following states:</p> <ul> <li> <p> <code>Creating</code> - Initial state during validation and registration</p> </li> <li> <p> <code>Active</code> - Model is ready for use in inference</p> </li> <li> <p> <code>Failed</code> - Creation process encountered an error</p> </li> </ul> <p> <b>Related APIs</b> </p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GetCustomModel.html">GetCustomModel</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ListCustomModels.html">ListCustomModels</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_DeleteCustomModel.html">DeleteCustomModel</a> </p> </li> </ul>

        Args:
            model_name: <p>A unique name for the custom model.</p>
            model_source_config: <p>The data source for the model. The Amazon S3 URI in the model source must be for the Amazon-managed Amazon S3 bucket containing your model artifacts.</p>
            custom_model_data_source: <p>The data source for the custom model. Use this field to specify a SageMaker AI model package ARN as the source for your custom model. Amazon Bedrock resolves the model package to retrieve the model artifacts.</p> <p>You can specify either <code>customModelDataSource</code> or <code>modelSourceConfig</code>, but not both.</p>
            model_kms_key_arn: <p>The Amazon Resource Name (ARN) of the customer managed KMS key to encrypt the custom model. If you don't provide a KMS key, Amazon Bedrock uses an Amazon Web Services-managed KMS key to encrypt the model. </p> <p>If you provide a customer managed KMS key, your Amazon Bedrock service role must have permissions to use it. For more information see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/encryption-import-model.html">Encryption of imported models</a>. </p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock assumes to perform tasks on your behalf. This role must have permissions to access the Amazon S3 bucket containing your model artifacts and the KMS key (if specified). For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-import-iam-role.html">Setting up an IAM service role for importing models</a> in the Amazon Bedrock User Guide.</p> <p>This field is required when you use <code>modelSourceConfig</code> with an Amazon S3 data source. It is not required when you use <code>customModelDataSource</code> with a model package ARN, because Amazon Bedrock uses its own credentials to access the model artifacts.</p>
            model_tags: <p>A list of key-value pairs to associate with the custom model resource. You can use these tags to organize and identify your resources.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Successful CreateCustomModel API call

            >>> await client.create_custom_model(model_name='SampleModel', model_source_config={'s3DataSource': {'s3Uri': 's3://my-bucket/folder'}}, role_arn='arn:aws:iam::123456789012:role/SampleRole', model_kms_key_arn='arn:aws:kms:us-east-1:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab', model_tags=[{'key': 'foo', 'value': 'foo'}, {'key': 'foo', 'value': 'foo'}], client_request_token='foo')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_custom_model_request.CreateCustomModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_custom_model_response.CreateCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_custom_model.async_create_custom_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_custom_model_request.CreateCustomModelRequest = {
            "model_name": model_name
        }
        if model_source_config is not None:
            input_["model_source_config"] = model_source_config
        if custom_model_data_source is not None:
            input_["custom_model_data_source"] = custom_model_data_source
        if model_kms_key_arn is not None:
            input_["model_kms_key_arn"] = model_kms_key_arn
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if model_tags is not None:
            input_["model_tags"] = model_tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_custom_model(
        self,
        model_identifier: "capo_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_custom_model_response.DeleteCustomModelResponse":
        """<p>Deletes a custom model that you created earlier. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            model_identifier: <p>Name of the model to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_custom_model_request.DeleteCustomModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_custom_model_response.DeleteCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_custom_model.async_delete_custom_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_custom_model_request.DeleteCustomModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_custom_model(
        self,
        model_identifier: "capo_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_custom_model_response.GetCustomModelResponse":
        """<p>Get the properties associated with a Amazon Bedrock custom model that you have created. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            model_identifier: <p>Name or Amazon Resource Name (ARN) of the custom model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_custom_model_request.GetCustomModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_custom_model_response.GetCustomModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_custom_model.async_get_custom_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_custom_model_request.GetCustomModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_custom_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        base_model_arn_equals: Optional["capo_bedrock.types.model_arn.ModelArn"] = None,
        foundation_model_arn_equals: Optional[
            "capo_bedrock.types.foundation_model_arn.FoundationModelArn"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        is_owned: Optional[bool] = None,
        model_status: Optional["capo_bedrock.types.model_status.ModelStatus"] = None,
    ) -> "capo_bedrock.types.list_custom_models_response.ListCustomModelsResponse":
        """<p>Returns a list of the custom models that you have created with the <code>CreateModelCustomizationJob</code> operation.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_before: <p>Return custom models created before the specified time. </p>
            creation_time_after: <p>Return custom models created after the specified time. </p>
            name_contains: <p>Return custom models only if the job name contains these characters.</p>
            base_model_arn_equals: <p>Return custom models only if the base model Amazon Resource Name (ARN) matches this parameter.</p>
            foundation_model_arn_equals: <p>Return custom models only if the foundation model Amazon Resource Name (ARN) matches this parameter.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of models.</p>
            sort_order: <p>The sort order of the results.</p>
            is_owned: <p>Return custom models depending on if the current account owns them (<code>true</code>) or if they were shared with the current account (<code>false</code>).</p>
            model_status: <p>The status of them model to filter results by. Possible values include:</p> <ul> <li> <p> <code>Creating</code> - Include only models that are currently being created and validated.</p> </li> <li> <p> <code>Active</code> - Include only models that have been successfully created and are ready for use.</p> </li> <li> <p> <code>Failed</code> - Include only models where the creation process failed.</p> </li> </ul> <p>If you don't specify a status, the API returns models in all states.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_custom_models_request.ListCustomModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_custom_models_response.ListCustomModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_models

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_custom_models.async_list_custom_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_custom_models_request.ListCustomModelsRequest = {}
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if base_model_arn_equals is not None:
            input_["base_model_arn_equals"] = base_model_arn_equals
        if foundation_model_arn_equals is not None:
            input_["foundation_model_arn_equals"] = foundation_model_arn_equals
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
        if is_owned is not None:
            input_["is_owned"] = is_owned
        if model_status is not None:
            input_["model_status"] = model_status

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_custom_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        base_model_arn_equals: Optional["capo_bedrock.types.model_arn.ModelArn"] = None,
        foundation_model_arn_equals: Optional[
            "capo_bedrock.types.foundation_model_arn.FoundationModelArn"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
        is_owned: Optional[bool] = None,
        model_status: Optional["capo_bedrock.types.model_status.ModelStatus"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.custom_model_summary.CustomModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_custom_models(
                config_overrides=config_overrides,
                creation_time_before=creation_time_before,
                creation_time_after=creation_time_after,
                name_contains=name_contains,
                base_model_arn_equals=base_model_arn_equals,
                foundation_model_arn_equals=foundation_model_arn_equals,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
                is_owned=is_owned,
                model_status=model_status,
            )
            _page = _resolve_path(_response, ("model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_account_data_retention(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "capo_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse":
        """<p>Returns the account-wide data retention mode for Amazon Bedrock.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_account_data_retention_response.GetAccountDataRetentionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_account_data_retention.async_get_account_data_retention(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_account_data_retention_request.GetAccountDataRetentionRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_account_data_retention(
        self,
        mode: "capo_bedrock.types.data_retention_mode.DataRetentionMode",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse":
        """<p>Sets the account-wide data retention mode for Amazon Bedrock.</p>

        Args:
            mode: <p>The data retention mode to set for the account.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_account_data_retention_response.PutAccountDataRetentionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_account_data_retention.async_put_account_data_retention(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.put_account_data_retention_request.PutAccountDataRetentionRequest = {
            "mode": mode
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_enforced_guardrail_configuration(
        self,
        config_id: "capo_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse":
        """<p>Deletes the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_enforced_guardrail_configuration_response.DeleteEnforcedGuardrailConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_enforced_guardrail_configuration.async_delete_enforced_guardrail_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_enforced_guardrail_configuration_request.DeleteEnforcedGuardrailConfigurationRequest = {
            "config_id": config_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_enforced_guardrails_configuration(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse":
        """<p>Lists the account-level enforced guardrail configurations.</p>

        Args:
            next_token: <p>Opaque continuation token of previous paginated response.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_enforced_guardrails_configuration_response.ListEnforcedGuardrailsConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_enforced_guardrails_configuration.async_list_enforced_guardrails_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_enforced_guardrails_configuration_request.ListEnforcedGuardrailsConfigurationRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_enforced_guardrails_configuration(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock.types.account_enforced_guardrail_output_configuration.AccountEnforcedGuardrailOutputConfiguration]":
        _token = next_token
        while True:
            _response = await self.list_enforced_guardrails_configuration(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("guardrails_config",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_enforced_guardrail_configuration(
        self,
        guardrail_inference_config: "capo_bedrock.types.account_enforced_guardrail_inference_input_configuration.AccountEnforcedGuardrailInferenceInputConfiguration",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        config_id: Optional[
            "capo_bedrock.types.account_enforced_guardrail_configuration_id.AccountEnforcedGuardrailConfigurationId"
        ] = None,
    ) -> "capo_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse":
        """<p>Sets the account-level enforced guardrail configuration.</p>

        Args:
            config_id: <p>Unique ID for the account enforced configuration.</p>
            guardrail_inference_config: <p>Account-level enforced guardrail input configuration.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_enforced_guardrail_configuration_response.PutEnforcedGuardrailConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_enforced_guardrail_configuration.async_put_enforced_guardrail_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.put_enforced_guardrail_configuration_request.PutEnforcedGuardrailConfigurationRequest = {
            "guardrail_inference_config": guardrail_inference_config
        }
        if config_id is not None:
            input_["config_id"] = config_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_delete_evaluation_job(
        self,
        job_identifiers: "capo_bedrock.types.evaluation_job_identifiers.EvaluationJobIdentifiers",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse":
        """<p>Deletes a batch of evaluation jobs. An evaluation job can only be deleted if it has following status <code>FAILED</code>, <code>COMPLETED</code>, and <code>STOPPED</code>. You can request up to 25 model evaluation jobs be deleted in a single request.</p>

        Args:
            job_identifiers: <p>A list of one or more evaluation job Amazon Resource Names (ARNs) you want to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete evaluation jobs
            The following example shows a request to delete two model evaluation jobs, where one of the jobs is not found.

            >>> await client.batch_delete_evaluation_job(job_identifiers=['arn:aws:bedrock:us-east-2:123456789012:evaluation-job/12rnxmplqv0v', 'arn:aws:bedrock:us-east-2:123456789012:evaluation-job/rispxmpl12rn'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.batch_delete_evaluation_job_response.BatchDeleteEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.batch_delete_evaluation_job.async_batch_delete_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.batch_delete_evaluation_job_request.BatchDeleteEvaluationJobRequest = {
            "job_identifiers": job_identifiers
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_evaluation_job(
        self,
        job_name: "capo_bedrock.types.evaluation_job_name.EvaluationJobName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        evaluation_config: "capo_bedrock.types.evaluation_config.EvaluationConfig",
        inference_config: "capo_bedrock.types.evaluation_inference_config.EvaluationInferenceConfig",
        output_data_config: "capo_bedrock.types.evaluation_output_data_config.EvaluationOutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_description: Optional[
            "capo_bedrock.types.evaluation_job_description.EvaluationJobDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customer_encryption_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        application_type: Optional[
            "capo_bedrock.types.application_type.ApplicationType"
        ] = None,
    ) -> (
        "capo_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
    ):
        """<p>Creates an evaluation job.</p>

        Args:
            job_name: <p>A name for the evaluation job. Names must unique with your Amazon Web Services account, and your account's Amazon Web Services region.</p>
            job_description: <p>A description of the evaluation job.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. To learn more about the required permissions, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-security.html">Required permissions for model evaluations</a>.</p>
            customer_encryption_key_id: <p>Specify your customer managed encryption key Amazon Resource Name (ARN) that will be used to encrypt your evaluation job.</p>
            job_tags: <p>Tags to attach to the model evaluation job.</p>
            application_type: <p>Specifies whether the evaluation job is for evaluating a model or evaluating a knowledge base (retrieval and response generation).</p>
            evaluation_config: <p>Contains the configuration details of either an automated or human-based evaluation job.</p>
            inference_config: <p>Contains the configuration details of the inference model for the evaluation job.</p> <p>For model evaluation jobs, automated jobs support a single model or <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">inference profile</a>, and jobs that use human workers support two models or inference profiles.</p>
            output_data_config: <p>Contains the configuration details of the Amazon S3 bucket for storing the results of the evaluation job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_evaluation_job_response.CreateEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_evaluation_job.async_create_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_evaluation_job_request.CreateEvaluationJobRequest = {
            "job_name": job_name,
            "role_arn": role_arn,
            "evaluation_config": evaluation_config,
            "inference_config": inference_config,
            "output_data_config": output_data_config,
        }
        if job_description is not None:
            input_["job_description"] = job_description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if customer_encryption_key_id is not None:
            input_["customer_encryption_key_id"] = customer_encryption_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if application_type is not None:
            input_["application_type"] = application_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_evaluation_job(
        self,
        job_identifier: "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse":
        """<p>Gets information about an evaluation job, such as the status of the job.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want get information on.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_evaluation_job_response.GetEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_evaluation_job.async_get_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_evaluation_job_request.GetEvaluationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_evaluation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
        ] = None,
        application_type_equals: Optional[
            "capo_bedrock.types.application_type.ApplicationType"
        ] = None,
        name_contains: Optional[
            "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse":
        """<p>Lists all existing evaluation jobs.</p>

        Args:
            creation_time_after: <p>A filter to only list evaluation jobs created after a specified time.</p>
            creation_time_before: <p>A filter to only list evaluation jobs created before a specified time.</p>
            status_equals: <p>A filter to only list evaluation jobs that are of a certain status.</p>
            application_type_equals: <p>A filter to only list evaluation jobs that are either model evaluations or knowledge base evaluations.</p>
            name_contains: <p>A filter to only list evaluation jobs that contain a specified string in the job name.</p>
            max_results: <p>The maximum number of results to return.</p>
            next_token: <p>Continuation token from the previous response, for Amazon Bedrock to list the next set of results.</p>
            sort_by: <p>Specifies a creation time to sort the list of evaluation jobs by when they were created.</p>
            sort_order: <p>Specifies whether to sort the list of evaluation jobs by either ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_evaluation_jobs_response.ListEvaluationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_evaluation_jobs.async_list_evaluation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_evaluation_jobs_request.ListEvaluationJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if application_type_equals is not None:
            input_["application_type_equals"] = application_type_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_evaluation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.evaluation_job_status.EvaluationJobStatus"
        ] = None,
        application_type_equals: Optional[
            "capo_bedrock.types.application_type.ApplicationType"
        ] = None,
        name_contains: Optional[
            "capo_bedrock.types.evaluation_job_name.EvaluationJobName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.evaluation_summary.EvaluationSummary]":
        _token = next_token
        while True:
            _response = await self.list_evaluation_jobs(
                config_overrides=config_overrides,
                creation_time_after=creation_time_after,
                creation_time_before=creation_time_before,
                status_equals=status_equals,
                application_type_equals=application_type_equals,
                name_contains=name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def stop_evaluation_job(
        self,
        job_identifier: "capo_bedrock.types.evaluation_job_identifier.EvaluationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse":
        """<p>Stops an evaluation job that is current being created or running.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the evaluation job you want to stop.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.stop_evaluation_job_response.StopEvaluationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_evaluation_job.async_stop_evaluation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_evaluation_job_request.StopEvaluationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_guardrail(
        self,
        name: "capo_bedrock.types.guardrail_name.GuardrailName",
        blocked_input_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_bedrock.types.guardrail_topic_policy_config.GuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_bedrock.types.guardrail_content_policy_config.GuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_bedrock.types.guardrail_word_policy_config.GuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_bedrock.types.guardrail_sensitive_information_policy_config.GuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_bedrock.types.guardrail_contextual_grounding_policy_config.GuardrailContextualGroundingPolicyConfig"
        ] = None,
        automated_reasoning_policy_config: Optional[
            "capo_bedrock.types.guardrail_automated_reasoning_policy_config.GuardrailAutomatedReasoningPolicyConfig"
        ] = None,
        cross_region_config: Optional[
            "capo_bedrock.types.guardrail_cross_region_config.GuardrailCrossRegionConfig"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_guardrail_response.CreateGuardrailResponse":
        """<p>Creates a guardrail to block topics and to implement safeguards for your generative AI applications.</p> <p>You can configure the following policies in a guardrail to avoid undesirable and harmful content, filter out denied topics and words, and remove sensitive information for privacy protection.</p> <ul> <li> <p> <b>Content filters</b> - Adjust filter strengths to block input prompts or model responses containing harmful content.</p> </li> <li> <p> <b>Denied topics</b> - Define a set of topics that are undesirable in the context of your application. These topics will be blocked if detected in user queries or model responses.</p> </li> <li> <p> <b>Word filters</b> - Configure filters to block undesirable words, phrases, and profanity. Such words can include offensive terms, competitor names etc.</p> </li> <li> <p> <b>Sensitive information filters</b> - Block or mask sensitive information such as personally identifiable information (PII) or custom regex in user inputs and model responses.</p> </li> </ul> <p>In addition to the above policies, you can also configure the messages to be returned to the user if a user input or model response is in violation of the policies defined in the guardrail.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html">Amazon Bedrock Guardrails</a> in the <i>Amazon Bedrock User Guide</i>.</p>

        Args:
            name: <p>The name to give the guardrail.</p>
            description: <p>A description of the guardrail.</p>
            topic_policy_config: <p>The topic policies to configure for the guardrail.</p>
            content_policy_config: <p>The content filter policies to configure for the guardrail.</p>
            word_policy_config: <p>The word policy you configure for the guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to create a guardrail.</p>
            automated_reasoning_policy_config: <p>Optional configuration for integrating Automated Reasoning policies with the new guardrail.</p>
            cross_region_config: <p>The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">Amazon Bedrock User Guide</a>.</p>
            blocked_input_messaging: <p>The message to return when the guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the guardrail blocks a model response.</p>
            kms_key_id: <p>The ARN of the KMS key that you use to encrypt the guardrail.</p>
            tags: <p>The tags that you want to attach to the guardrail. </p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_guardrail_request.CreateGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_guardrail_response.CreateGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail.async_create_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_guardrail_request.CreateGuardrailRequest = {
            "name": name,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
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
        if automated_reasoning_policy_config is not None:
            input_["automated_reasoning_policy_config"] = (
                automated_reasoning_policy_config
            )
        if cross_region_config is not None:
            input_["cross_region_config"] = cross_region_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_guardrail(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        guardrail_version: Optional[
            "capo_bedrock.types.guardrail_version.GuardrailVersion"
        ] = None,
    ) -> "capo_bedrock.types.get_guardrail_response.GetGuardrailResponse":
        """<p>Gets details about a guardrail. If you don't specify a version, the response returns details for the <code>DRAFT</code> version.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail for which to get details. This can be an ID or the ARN.</p>
            guardrail_version: <p>The version of the guardrail for which to get details. If you don't specify a version, the response returns details for the <code>DRAFT</code> version.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_guardrail_request.GetGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_guardrail_response.GetGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_guardrail.async_get_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_guardrail_request.GetGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_guardrail(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        name: "capo_bedrock.types.guardrail_name.GuardrailName",
        blocked_input_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        blocked_outputs_messaging: "capo_bedrock.types.guardrail_blocked_messaging.GuardrailBlockedMessaging",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        topic_policy_config: Optional[
            "capo_bedrock.types.guardrail_topic_policy_config.GuardrailTopicPolicyConfig"
        ] = None,
        content_policy_config: Optional[
            "capo_bedrock.types.guardrail_content_policy_config.GuardrailContentPolicyConfig"
        ] = None,
        word_policy_config: Optional[
            "capo_bedrock.types.guardrail_word_policy_config.GuardrailWordPolicyConfig"
        ] = None,
        sensitive_information_policy_config: Optional[
            "capo_bedrock.types.guardrail_sensitive_information_policy_config.GuardrailSensitiveInformationPolicyConfig"
        ] = None,
        contextual_grounding_policy_config: Optional[
            "capo_bedrock.types.guardrail_contextual_grounding_policy_config.GuardrailContextualGroundingPolicyConfig"
        ] = None,
        automated_reasoning_policy_config: Optional[
            "capo_bedrock.types.guardrail_automated_reasoning_policy_config.GuardrailAutomatedReasoningPolicyConfig"
        ] = None,
        cross_region_config: Optional[
            "capo_bedrock.types.guardrail_cross_region_config.GuardrailCrossRegionConfig"
        ] = None,
        kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_bedrock.types.update_guardrail_response.UpdateGuardrailResponse":
        """<p>Updates a guardrail with the values you specify.</p> <ul> <li> <p>Specify a <code>name</code> and optional <code>description</code>.</p> </li> <li> <p>Specify messages for when the guardrail successfully blocks a prompt or a model response in the <code>blockedInputMessaging</code> and <code>blockedOutputsMessaging</code> fields.</p> </li> <li> <p>Specify topics for the guardrail to deny in the <code>topicPolicyConfig</code> object. Each <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailTopicConfig.html">GuardrailTopicConfig</a> object in the <code>topicsConfig</code> list pertains to one topic.</p> <ul> <li> <p>Give a <code>name</code> and <code>description</code> so that the guardrail can properly identify the topic.</p> </li> <li> <p>Specify <code>DENY</code> in the <code>type</code> field.</p> </li> <li> <p>(Optional) Provide up to five prompts that you would categorize as belonging to the topic in the <code>examples</code> list.</p> </li> </ul> </li> <li> <p>Specify filter strengths for the harmful categories defined in Amazon Bedrock in the <code>contentPolicyConfig</code> object. Each <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a> object in the <code>filtersConfig</code> list pertains to a harmful category. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-content-filters">Content filters</a>. For more information about the fields in a content filter, see <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a>.</p> <ul> <li> <p>Specify the category in the <code>type</code> field.</p> </li> <li> <p>Specify the strength of the filter for prompts in the <code>inputStrength</code> field and for model responses in the <code>strength</code> field of the <a href="https://docs.aws.amazon.com/bedrock/latest/APIReference/API_GuardrailContentFilterConfig.html">GuardrailContentFilterConfig</a>.</p> </li> </ul> </li> <li> <p>(Optional) For security, include the ARN of a KMS key in the <code>kmsKeyId</code> field.</p> </li> </ul>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            name: <p>A name for the guardrail.</p>
            description: <p>A description of the guardrail.</p>
            topic_policy_config: <p>The topic policy to configure for the guardrail.</p>
            content_policy_config: <p>The content policy to configure for the guardrail.</p>
            word_policy_config: <p>The word policy to configure for the guardrail.</p>
            sensitive_information_policy_config: <p>The sensitive information policy to configure for the guardrail.</p>
            contextual_grounding_policy_config: <p>The contextual grounding policy configuration used to update a guardrail.</p>
            automated_reasoning_policy_config: <p>Updated configuration for Automated Reasoning policies associated with the guardrail.</p>
            cross_region_config: <p>The system-defined guardrail profile that you're using with your guardrail. Guardrail profiles define the destination Amazon Web Services Regions where guardrail inference requests can be automatically routed.</p> <p>For more information, see the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-cross-region.html">Amazon Bedrock User Guide</a>.</p>
            blocked_input_messaging: <p>The message to return when the guardrail blocks a prompt.</p>
            blocked_outputs_messaging: <p>The message to return when the guardrail blocks a model response.</p>
            kms_key_id: <p>The ARN of the KMS key with which to encrypt the guardrail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_guardrail_request.UpdateGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_guardrail_response.UpdateGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_guardrail.async_update_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.update_guardrail_request.UpdateGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier,
            "name": name,
            "blocked_input_messaging": blocked_input_messaging,
            "blocked_outputs_messaging": blocked_outputs_messaging,
        }
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
        if automated_reasoning_policy_config is not None:
            input_["automated_reasoning_policy_config"] = (
                automated_reasoning_policy_config
            )
        if cross_region_config is not None:
            input_["cross_region_config"] = cross_region_config
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_guardrail(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        guardrail_version: Optional[
            "capo_bedrock.types.guardrail_numerical_version.GuardrailNumericalVersion"
        ] = None,
    ) -> "capo_bedrock.types.delete_guardrail_response.DeleteGuardrailResponse":
        """<p>Deletes a guardrail.</p> <ul> <li> <p>To delete a guardrail, only specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field. If you delete a guardrail, all of its versions will be deleted.</p> </li> <li> <p>To delete a version of a guardrail, specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field and the version in the <code>guardrailVersion</code> field.</p> </li> </ul>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            guardrail_version: <p>The version of the guardrail.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_in_use_exception.ResourceInUseException: <p>Thrown when attempting to delete or modify a resource that is currently being used by other resources or operations. For example, trying to delete an Automated Reasoning policy that is referenced by an active guardrail.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_guardrail_request.DeleteGuardrailRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_guardrail_response.DeleteGuardrailResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_guardrail

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_guardrail.async_delete_guardrail(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_guardrail_request.DeleteGuardrailRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if guardrail_version is not None:
            input_["guardrail_version"] = guardrail_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_guardrails(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        guardrail_identifier: Optional[
            "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "capo_bedrock.types.list_guardrails_response.ListGuardrailsResponse":
        """<p>Lists details about all the guardrails in an account. To list the <code>DRAFT</code> version of all your guardrails, don't specify the <code>guardrailIdentifier</code> field. To list all versions of a guardrail, specify the ARN of the guardrail in the <code>guardrailIdentifier</code> field.</p> <p>You can set the maximum number of results to return in a response in the <code>maxResults</code> field. If there are more results than the number you set, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            max_results: <p>The maximum number of results to return in the response.</p>
            next_token: <p>If there are more results than were returned in the response, the response returns a <code>nextToken</code> that you can send in another <code>ListGuardrails</code> request to see the next batch of results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_guardrails_request.ListGuardrailsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_guardrails_response.ListGuardrailsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_guardrails

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_guardrails.async_list_guardrails(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_guardrails_request.ListGuardrailsRequest = {}
        if guardrail_identifier is not None:
            input_["guardrail_identifier"] = guardrail_identifier
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

    async def iter_list_guardrails(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        guardrail_identifier: Optional[
            "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock.types.guardrail_summary.GuardrailSummary]":
        _token = next_token
        while True:
            _response = await self.list_guardrails(
                config_overrides=config_overrides,
                guardrail_identifier=guardrail_identifier,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("guardrails",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_guardrail_version(
        self,
        guardrail_identifier: "capo_bedrock.types.guardrail_identifier.GuardrailIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.guardrail_description.GuardrailDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_guardrail_version_response.CreateGuardrailVersionResponse":
        """<p>Creates a version of the guardrail. Use this API to create a snapshot of the guardrail when you are satisfied with a configuration, or to compare the configuration with another version.</p>

        Args:
            guardrail_identifier: <p>The unique identifier of the guardrail. This can be an ID or the ARN.</p>
            description: <p>A description of the guardrail version.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than once. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the <i>Amazon S3 User Guide</i>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_guardrail_version_request.CreateGuardrailVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_guardrail_version_response.CreateGuardrailVersionResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail_version

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_guardrail_version.async_create_guardrail_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_guardrail_version_request.CreateGuardrailVersionRequest = {
            "guardrail_identifier": guardrail_identifier
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_inference_profile(
        self,
        inference_profile_name: "capo_bedrock.types.inference_profile_name.InferenceProfileName",
        model_source: "capo_bedrock.types.inference_profile_model_source.InferenceProfileModelSource",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        description: Optional[
            "capo_bedrock.types.inference_profile_description.InferenceProfileDescription"
        ] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_inference_profile_response.CreateInferenceProfileResponse":
        """<p>Creates an application inference profile to track metrics and costs when invoking a model. To create an application inference profile for a foundation model in one region, specify the ARN of the model in that region. To create an application inference profile for a foundation model across multiple regions, specify the ARN of the system-defined inference profile that contains the regions that you want to route requests to. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_name: <p>A name for the inference profile.</p>
            description: <p>A description for the inference profile.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            model_source: <p>The foundation model or system-defined inference profile that the inference profile will track metrics and costs for.</p>
            tags: <p>An array of objects, each of which contains a tag and its value. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_inference_profile_request.CreateInferenceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_inference_profile_response.CreateInferenceProfileResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_inference_profile

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_inference_profile.async_create_inference_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_inference_profile_request.CreateInferenceProfileRequest = {
            "inference_profile_name": inference_profile_name,
            "model_source": model_source,
        }
        if description is not None:
            input_["description"] = description
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_inference_profile(
        self,
        inference_profile_identifier: "capo_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> (
        "capo_bedrock.types.get_inference_profile_response.GetInferenceProfileResponse"
    ):
        """<p>Gets information about an inference profile. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_identifier: <p>The ID or Amazon Resource Name (ARN) of the inference profile.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_inference_profile_request.GetInferenceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_inference_profile_response.GetInferenceProfileResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_inference_profile

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_inference_profile.async_get_inference_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_inference_profile_request.GetInferenceProfileRequest = {
            "inference_profile_identifier": inference_profile_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_inference_profile(
        self,
        inference_profile_identifier: "capo_bedrock.types.inference_profile_identifier.InferenceProfileIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_inference_profile_response.DeleteInferenceProfileResponse":
        """<p>Deletes an application inference profile. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            inference_profile_identifier: <p>The Amazon Resource Name (ARN) or ID of the application inference profile to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_inference_profile_request.DeleteInferenceProfileRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_inference_profile_response.DeleteInferenceProfileResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_inference_profile

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_inference_profile.async_delete_inference_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_inference_profile_request.DeleteInferenceProfileRequest = {
            "inference_profile_identifier": inference_profile_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_inference_profiles(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type_equals: Optional[
            "capo_bedrock.types.inference_profile_type.InferenceProfileType"
        ] = None,
    ) -> "capo_bedrock.types.list_inference_profiles_response.ListInferenceProfilesResponse":
        """<p>Returns a list of inference profiles that you can use. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html">Increase throughput and resilience with cross-region inference in Amazon Bedrock</a>. in the Amazon Bedrock User Guide.</p>

        Args:
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            type_equals: <p>Filters for inference profiles that match the type you specify.</p> <ul> <li> <p> <code>SYSTEM_DEFINED</code> – The inference profile is defined by Amazon Bedrock. You can route inference requests across regions with these inference profiles.</p> </li> <li> <p> <code>APPLICATION</code> – The inference profile was created by a user. This type of inference profile can track metrics and costs when invoking the model in it. The inference profile may route requests to one or multiple regions.</p> </li> </ul>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_inference_profiles_request.ListInferenceProfilesRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_inference_profiles_response.ListInferenceProfilesResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_inference_profiles

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_inference_profiles.async_list_inference_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_inference_profiles_request.ListInferenceProfilesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type_equals is not None:
            input_["type_equals"] = type_equals

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_inference_profiles(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type_equals: Optional[
            "capo_bedrock.types.inference_profile_type.InferenceProfileType"
        ] = None,
    ) -> "AsyncIterator[capo_bedrock.types.inference_profile_summary.InferenceProfileSummary]":
        _token = next_token
        while True:
            _response = await self.list_inference_profiles(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                type_equals=type_equals,
            )
            _page = _resolve_path(_response, ("inference_profile_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def delete_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "capo_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse":
        """<p>Delete the invocation logging. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_model_invocation_logging_configuration_response.DeleteModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_model_invocation_logging_configuration.async_delete_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_model_invocation_logging_configuration_request.DeleteModelInvocationLoggingConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_invocation_logging_configuration(
        self, *, config_overrides: Optional[AsyncBedrockClientConfig] = None
    ) -> "capo_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse":
        """<p>Get the current configuration values for model invocation logging.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_invocation_logging_configuration_response.GetModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_logging_configuration.async_get_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_invocation_logging_configuration_request.GetModelInvocationLoggingConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_model_invocation_logging_configuration(
        self,
        logging_config: "capo_bedrock.types.logging_config.LoggingConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse":
        """<p>Set the configuration values for model invocation logging.</p>

        Args:
            logging_config: <p>The logging configuration values to set.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_model_invocation_logging_configuration_response.PutModelInvocationLoggingConfigurationResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_model_invocation_logging_configuration.async_put_model_invocation_logging_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.put_model_invocation_logging_configuration_request.PutModelInvocationLoggingConfigurationRequest = {
            "logging_config": logging_config
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_model_copy_job(
        self,
        source_model_arn: "capo_bedrock.types.model_arn.ModelArn",
        target_model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        model_kms_key_id: Optional["capo_bedrock.types.kms_key_id.KmsKeyId"] = None,
        target_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
    ) -> "capo_bedrock.types.create_model_copy_job_response.CreateModelCopyJobResponse":
        """<p>Copies a model to another region so that it can be used there. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            source_model_arn: <p>The Amazon Resource Name (ARN) of the model to be copied.</p>
            target_model_name: <p>A name for the copied model.</p>
            model_kms_key_id: <p>The ARN of the KMS key that you use to encrypt the model copy.</p>
            target_model_tags: <p>Tags to associate with the target model. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tag resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_model_copy_job_request.CreateModelCopyJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_model_copy_job_response.CreateModelCopyJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_copy_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_copy_job.async_create_model_copy_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_copy_job_request.CreateModelCopyJobRequest = {
            "source_model_arn": source_model_arn,
            "target_model_name": target_model_name,
        }
        if model_kms_key_id is not None:
            input_["model_kms_key_id"] = model_kms_key_id
        if target_model_tags is not None:
            input_["target_model_tags"] = target_model_tags
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_copy_job(
        self,
        job_arn: "capo_bedrock.types.model_copy_job_arn.ModelCopyJobArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_copy_job_response.GetModelCopyJobResponse":
        """<p>Retrieves information about a model copy job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_arn: <p>The Amazon Resource Name (ARN) of the model copy job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_copy_job_request.GetModelCopyJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_copy_job_response.GetModelCopyJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_copy_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_copy_job.async_get_model_copy_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_copy_job_request.GetModelCopyJobRequest = {
            "job_arn": job_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_model_copy_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_copy_job_status.ModelCopyJobStatus"
        ] = None,
        source_account_equals: Optional[
            "capo_bedrock.types.account_id.AccountId"
        ] = None,
        source_model_arn_equals: Optional[
            "capo_bedrock.types.model_arn.ModelArn"
        ] = None,
        target_model_name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_model_copy_jobs_response.ListModelCopyJobsResponse":
        """<p>Returns a list of model copy jobs that you have submitted. You can filter the jobs to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/copy-model.html">Copy models to be used in other regions</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Filters for model copy jobs created after the specified time.</p>
            creation_time_before: <p>Filters for model copy jobs created before the specified time. </p>
            status_equals: <p>Filters for model copy jobs whose status matches the value that you specify.</p>
            source_account_equals: <p>Filters for model copy jobs in which the account that the source model belongs to is equal to the value that you specify.</p>
            source_model_arn_equals: <p>Filters for model copy jobs in which the Amazon Resource Name (ARN) of the source model to is equal to the value that you specify.</p>
            target_model_name_contains: <p>Filters for model copy jobs in which the name of the copied model contains the string that you specify.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of model copy jobs.</p>
            sort_order: <p>Specifies whether to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_model_copy_jobs_request.ListModelCopyJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_model_copy_jobs_response.ListModelCopyJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_copy_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_copy_jobs.async_list_model_copy_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_copy_jobs_request.ListModelCopyJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if source_account_equals is not None:
            input_["source_account_equals"] = source_account_equals
        if source_model_arn_equals is not None:
            input_["source_model_arn_equals"] = source_model_arn_equals
        if target_model_name_contains is not None:
            input_["target_model_name_contains"] = target_model_name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_model_copy_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_copy_job_status.ModelCopyJobStatus"
        ] = None,
        source_account_equals: Optional[
            "capo_bedrock.types.account_id.AccountId"
        ] = None,
        source_model_arn_equals: Optional[
            "capo_bedrock.types.model_arn.ModelArn"
        ] = None,
        target_model_name_contains: Optional[
            "capo_bedrock.types.custom_model_name.CustomModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.model_copy_job_summary.ModelCopyJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_model_copy_jobs(
                config_overrides=config_overrides,
                creation_time_after=creation_time_after,
                creation_time_before=creation_time_before,
                status_equals=status_equals,
                source_account_equals=source_account_equals,
                source_model_arn_equals=source_model_arn_equals,
                target_model_name_contains=target_model_name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("model_copy_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_model_import_job(
        self,
        job_name: "capo_bedrock.types.job_name.JobName",
        imported_model_name: "capo_bedrock.types.imported_model_name.ImportedModelName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        model_data_source: "capo_bedrock.types.model_data_source.ModelDataSource",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        imported_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        vpc_config: Optional["capo_bedrock.types.vpc_config.VpcConfig"] = None,
        imported_model_kms_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
    ) -> "capo_bedrock.types.create_model_import_job_response.CreateModelImportJobResponse":
        """<p>Creates a model import job to import model that you have customized in other environments, such as Amazon SageMaker. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> </p>

        Args:
            job_name: <p>The name of the import job.</p>
            imported_model_name: <p>The name of the imported model.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the model import job.</p>
            model_data_source: <p>The data source for the imported model.</p>
            job_tags: <p>Tags to attach to this import job. </p>
            imported_model_tags: <p>Tags to attach to the imported model.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            vpc_config: <p>VPC configuration parameters for the private Virtual Private Cloud (VPC) that contains the resources you are using for the import job.</p>
            imported_model_kms_key_id: <p>The imported model is encrypted at rest using this key.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_model_import_job_request.CreateModelImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_model_import_job_response.CreateModelImportJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_import_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_import_job.async_create_model_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_import_job_request.CreateModelImportJobRequest = {
            "job_name": job_name,
            "imported_model_name": imported_model_name,
            "role_arn": role_arn,
            "model_data_source": model_data_source,
        }
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if imported_model_tags is not None:
            input_["imported_model_tags"] = imported_model_tags
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if imported_model_kms_key_id is not None:
            input_["imported_model_kms_key_id"] = imported_model_kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_imported_model(
        self,
        model_identifier: "capo_bedrock.types.imported_model_identifier.ImportedModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> (
        "capo_bedrock.types.delete_imported_model_response.DeleteImportedModelResponse"
    ):
        """<p>Deletes a custom model that you imported earlier. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>. </p>

        Args:
            model_identifier: <p>Name of the imported model to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_imported_model_request.DeleteImportedModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_imported_model_response.DeleteImportedModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_imported_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_imported_model.async_delete_imported_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_imported_model_request.DeleteImportedModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_imported_model(
        self,
        model_identifier: "capo_bedrock.types.imported_model_identifier.ImportedModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_imported_model_response.GetImportedModelResponse":
        """<p>Gets properties associated with a customized model you imported. </p>

        Args:
            model_identifier: <p>Name or Amazon Resource Name (ARN) of the imported model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_imported_model_request.GetImportedModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_imported_model_response.GetImportedModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_imported_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_imported_model.async_get_imported_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_imported_model_request.GetImportedModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_import_job(
        self,
        job_identifier: "capo_bedrock.types.model_import_job_identifier.ModelImportJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_import_job_response.GetModelImportJobResponse":
        """<p>Retrieves the properties associated with import model job, including the status of the job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>The identifier of the import job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_import_job_request.GetModelImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_import_job_response.GetModelImportJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_import_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_import_job.async_get_model_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_import_job_request.GetModelImportJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_imported_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.imported_model_name.ImportedModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_imported_models_response.ListImportedModelsResponse":
        """<p>Returns a list of models you've imported. You can filter the results to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_before: <p>Return imported models that created before the specified time.</p>
            creation_time_after: <p>Return imported models that were created after the specified time.</p>
            name_contains: <p>Return imported models only if the model name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of imported models.</p>
            sort_order: <p>Specifies whetehr to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_imported_models_request.ListImportedModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_imported_models_response.ListImportedModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_imported_models

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_imported_models.async_list_imported_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_imported_models_request.ListImportedModelsRequest = {}
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_imported_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        name_contains: Optional[
            "capo_bedrock.types.imported_model_name.ImportedModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_models_by.SortModelsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> (
        "AsyncIterator[capo_bedrock.types.imported_model_summary.ImportedModelSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_imported_models(
                config_overrides=config_overrides,
                creation_time_before=creation_time_before,
                creation_time_after=creation_time_after,
                name_contains=name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_model_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_import_job_status.ModelImportJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> (
        "capo_bedrock.types.list_model_import_jobs_response.ListModelImportJobsResponse"
    ):
        """<p>Returns a list of import jobs you've submitted. You can filter the results to return based on one or more criteria. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-import-model.html">Import a customized model</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Return import jobs that were created after the specified time.</p>
            creation_time_before: <p>Return import jobs that were created before the specified time.</p>
            status_equals: <p>Return imported jobs with the specified status.</p>
            name_contains: <p>Return imported jobs only if the job name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of imported jobs.</p>
            sort_order: <p>Specifies whether to sort the results in ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_model_import_jobs_request.ListModelImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_model_import_jobs_response.ListModelImportJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_import_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_import_jobs.async_list_model_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_import_jobs_request.ListModelImportJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_model_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_import_job_status.ModelImportJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.model_import_job_summary.ModelImportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_model_import_jobs(
                config_overrides=config_overrides,
                creation_time_after=creation_time_after,
                creation_time_before=creation_time_before,
                status_equals=status_equals,
                name_contains=name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("model_import_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_model_invocation_job(
        self,
        job_name: "capo_bedrock.types.model_invocation_job_name.ModelInvocationJobName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        model_id: "capo_bedrock.types.model_id.ModelId",
        input_data_config: "capo_bedrock.types.model_invocation_job_input_data_config.ModelInvocationJobInputDataConfig",
        output_data_config: "capo_bedrock.types.model_invocation_job_output_data_config.ModelInvocationJobOutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.model_invocation_idempotency_token.ModelInvocationIdempotencyToken"
        ] = None,
        vpc_config: Optional["capo_bedrock.types.vpc_config.VpcConfig"] = None,
        timeout_duration_in_hours: Optional[
            "capo_bedrock.types.model_invocation_job_timeout_duration_in_hours.ModelInvocationJobTimeoutDurationInHours"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        model_invocation_type: Optional[
            "capo_bedrock.types.model_invocation_type.ModelInvocationType"
        ] = None,
    ) -> "capo_bedrock.types.create_model_invocation_job_response.CreateModelInvocationJobResponse":
        """<p>Creates a batch inference job to invoke a model on multiple prompts. Format your data according to <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data">Format your inference data</a> and upload it to an Amazon S3 bucket. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference.html">Process multiple prompts with batch inference</a>.</p> <p>The response returns a <code>jobArn</code> that you can use to stop or get details about the job.</p>

        Args:
            job_name: <p>A name to give the batch inference job.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html">Create a service role for batch inference</a>.</p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            model_id: <p>The unique identifier of the foundation model to use for the batch inference job.</p>
            input_data_config: <p>Details about the location of the input to the batch inference job.</p>
            output_data_config: <p>Details about the location of the output of the batch inference job.</p>
            vpc_config: <p>The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc">Protect batch inference jobs using a VPC</a>.</p>
            timeout_duration_in_hours: <p>The number of hours after which to force the batch inference job to time out.</p>
            tags: <p>Any tags to associate with the batch inference job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/tagging.html">Tagging Amazon Bedrock resources</a>.</p>
            model_invocation_type: <p>The invocation endpoint for ModelInvocationJob</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_model_invocation_job_request.CreateModelInvocationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_model_invocation_job_response.CreateModelInvocationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_invocation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_invocation_job.async_create_model_invocation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_invocation_job_request.CreateModelInvocationJobRequest = {
            "job_name": job_name,
            "role_arn": role_arn,
            "model_id": model_id,
            "input_data_config": input_data_config,
            "output_data_config": output_data_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if timeout_duration_in_hours is not None:
            input_["timeout_duration_in_hours"] = timeout_duration_in_hours
        if tags is not None:
            input_["tags"] = tags
        if model_invocation_type is not None:
            input_["model_invocation_type"] = model_invocation_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_invocation_job(
        self,
        job_identifier: "capo_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_invocation_job_response.GetModelInvocationJobResponse":
        """<p>Gets details about a batch inference job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-monitor">Monitor batch inference jobs</a> </p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the batch inference job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_invocation_job_request.GetModelInvocationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_invocation_job_response.GetModelInvocationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_invocation_job.async_get_model_invocation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_invocation_job_request.GetModelInvocationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_model_invocation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        submit_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        submit_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_invocation_job_status.ModelInvocationJobStatus"
        ] = None,
        name_contains: Optional[
            "capo_bedrock.types.model_invocation_job_name.ModelInvocationJobName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_model_invocation_jobs_response.ListModelInvocationJobsResponse":
        """<p>Lists all batch inference jobs in the account. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-view.html">View details about a batch inference job</a>.</p>

        Args:
            submit_time_after: <p>Specify a time to filter for batch inference jobs that were submitted after the time you specify.</p>
            submit_time_before: <p>Specify a time to filter for batch inference jobs that were submitted before the time you specify.</p>
            status_equals: <p>Specify a status to filter for batch inference jobs whose statuses match the string you specify.</p> <p>The following statuses are possible:</p> <ul> <li> <p>Submitted – This job has been submitted to a queue for validation.</p> </li> <li> <p>Validating – This job is being validated for the requirements described in <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html">Format and upload your batch inference data</a>. The criteria include the following:</p> <ul> <li> <p>Your IAM service role has access to the Amazon S3 buckets containing your files.</p> </li> <li> <p>Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesn't check if the <code>modelInput</code> value matches the request body for the model.</p> </li> <li> <p>Your files fulfill the requirements for file size and number of records. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html">Quotas for Amazon Bedrock</a>.</p> </li> </ul> </li> <li> <p>Scheduled – This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.</p> </li> <li> <p>Expired – This job timed out because it was scheduled but didn't begin before the set timeout duration. Submit a new job request.</p> </li> <li> <p>InProgress – This job has begun. You can start viewing the results in the output S3 location.</p> </li> <li> <p>Completed – This job has successfully completed. View the output files in the output S3 location.</p> </li> <li> <p>PartiallyCompleted – This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.</p> </li> <li> <p>Failed – This job has failed. Check the failure message for any further details. For further assistance, reach out to the <a href="https://console.aws.amazon.com/support/home/">Amazon Web Services Support Center</a>.</p> </li> <li> <p>Stopped – This job was stopped by a user.</p> </li> <li> <p>Stopping – This job is being stopped by a user.</p> </li> </ul>
            name_contains: <p>Specify a string to filter for batch inference jobs whose names contain the string.</p>
            max_results: <p>The maximum number of results to return. If there are more results than the number that you specify, a <code>nextToken</code> value is returned. Use the <code>nextToken</code> in a request to return the next batch of results.</p>
            next_token: <p>If there were more results than the value you specified in the <code>maxResults</code> field in a previous <code>ListModelInvocationJobs</code> request, the response would have returned a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another request.</p>
            sort_by: <p>An attribute by which to sort the results.</p>
            sort_order: <p>Specifies whether to sort the results by ascending or descending order.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_model_invocation_jobs_request.ListModelInvocationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_model_invocation_jobs_response.ListModelInvocationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_invocation_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_invocation_jobs.async_list_model_invocation_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_invocation_jobs_request.ListModelInvocationJobsRequest = {}
        if submit_time_after is not None:
            input_["submit_time_after"] = submit_time_after
        if submit_time_before is not None:
            input_["submit_time_before"] = submit_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_model_invocation_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        submit_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        submit_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.model_invocation_job_status.ModelInvocationJobStatus"
        ] = None,
        name_contains: Optional[
            "capo_bedrock.types.model_invocation_job_name.ModelInvocationJobName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.model_invocation_job_summary.ModelInvocationJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_model_invocation_jobs(
                config_overrides=config_overrides,
                submit_time_after=submit_time_after,
                submit_time_before=submit_time_before,
                status_equals=status_equals,
                name_contains=name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("invocation_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def stop_model_invocation_job(
        self,
        job_identifier: "capo_bedrock.types.model_invocation_job_identifier.ModelInvocationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_model_invocation_job_response.StopModelInvocationJobResponse":
        """<p>Stops a batch inference job. You're only charged for tokens that were already processed. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-stop.html">Stop a batch inference job</a>.</p>

        Args:
            job_identifier: <p>The Amazon Resource Name (ARN) of the batch inference job to stop.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.stop_model_invocation_job_request.StopModelInvocationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.stop_model_invocation_job_response.StopModelInvocationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_invocation_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_invocation_job.async_stop_model_invocation_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_model_invocation_job_request.StopModelInvocationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_foundation_model(
        self,
        model_identifier: "capo_bedrock.types.get_foundation_model_identifier.GetFoundationModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_foundation_model_response.GetFoundationModelResponse":
        """<p>Get details about a Amazon Bedrock foundation model.</p>

        Args:
            model_identifier: <p>The model identifier. </p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_foundation_model_request.GetFoundationModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_foundation_model_response.GetFoundationModelResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model.async_get_foundation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_foundation_model_request.GetFoundationModelRequest = {
            "model_identifier": model_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_foundation_models(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        by_provider: Optional["capo_bedrock.types.provider.Provider"] = None,
        by_customization_type: Optional[
            "capo_bedrock.types.model_customization.ModelCustomization"
        ] = None,
        by_output_modality: Optional[
            "capo_bedrock.types.model_modality.ModelModality"
        ] = None,
        by_inference_type: Optional[
            "capo_bedrock.types.inference_type.InferenceType"
        ] = None,
    ) -> "capo_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse":
        """<p>Lists Amazon Bedrock foundation models that you can use. You can filter the results with the request parameters. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/foundation-models.html">Foundation models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            by_provider: <p>Return models belonging to the model provider that you specify.</p>
            by_customization_type: <p>Return models that support the customization type that you specify. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            by_output_modality: <p>Return models that support the output modality that you specify.</p>
            by_inference_type: <p>Return models that support the inference type that you specify. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_foundation_models_response.ListFoundationModelsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_models.async_list_foundation_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_foundation_models_request.ListFoundationModelsRequest = {}
        if by_provider is not None:
            input_["by_provider"] = by_provider
        if by_customization_type is not None:
            input_["by_customization_type"] = by_customization_type
        if by_output_modality is not None:
            input_["by_output_modality"] = by_output_modality
        if by_inference_type is not None:
            input_["by_inference_type"] = by_inference_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_prompt_router(
        self,
        prompt_router_name: "capo_bedrock.types.prompt_router_name.PromptRouterName",
        models: "capo_bedrock.types.prompt_router_target_models.PromptRouterTargetModels",
        routing_criteria: "capo_bedrock.types.routing_criteria.RoutingCriteria",
        fallback_model: "capo_bedrock.types.prompt_router_target_model.PromptRouterTargetModel",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        description: Optional[
            "capo_bedrock.types.prompt_router_description.PromptRouterDescription"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse":
        """<p>Creates a prompt router that manages the routing of requests between multiple foundation models based on the routing criteria.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier that you provide to ensure idempotency of your requests. If not specified, the Amazon Web Services SDK automatically generates one for you.</p>
            prompt_router_name: <p>The name of the prompt router. The name must be unique within your Amazon Web Services account in the current region.</p>
            models: <p>A list of foundation models that the prompt router can route requests to. At least one model must be specified.</p>
            description: <p>An optional description of the prompt router to help identify its purpose.</p>
            routing_criteria: <p>The criteria, which is the response quality difference, used to determine how incoming requests are routed to different models.</p>
            fallback_model: <p>The default model to use when the routing criteria is not met.</p>
            tags: <p>An array of key-value pairs to apply to this resource as tags. You can use tags to categorize and manage your Amazon Web Services resources.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_prompt_router_response.CreatePromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_prompt_router.async_create_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_prompt_router_request.CreatePromptRouterRequest = {
            "prompt_router_name": prompt_router_name,
            "models": models,
            "routing_criteria": routing_criteria,
            "fallback_model": fallback_model,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
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

    async def get_prompt_router(
        self,
        prompt_router_arn: "capo_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse":
        """<p>Retrieves details about a prompt router.</p>

        Args:
            prompt_router_arn: <p>The prompt router's ARN</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_prompt_router_request.GetPromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_prompt_router_response.GetPromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_prompt_router.async_get_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_prompt_router_request.GetPromptRouterRequest = {
            "prompt_router_arn": prompt_router_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_prompt_router(
        self,
        prompt_router_arn: "capo_bedrock.types.prompt_router_arn.PromptRouterArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse":
        """<p>Deletes a specified prompt router. This action cannot be undone.</p>

        Args:
            prompt_router_arn: <p>The Amazon Resource Name (ARN) of the prompt router to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_prompt_router_response.DeletePromptRouterResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_prompt_router.async_delete_prompt_router(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_prompt_router_request.DeletePromptRouterRequest = {
            "prompt_router_arn": prompt_router_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_prompt_routers(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type: Optional["capo_bedrock.types.prompt_router_type.PromptRouterType"] = None,
    ) -> "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse":
        """<p>Retrieves a list of prompt routers.</p>

        Args:
            max_results: <p>The maximum number of prompt routers to return in one page of results.</p>
            next_token: <p>Specify the pagination token from a previous request to retrieve the next page of results.</p>
            type: <p>The type of the prompt routers, such as whether it's default or custom.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_prompt_routers_response.ListPromptRoutersResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_prompt_routers.async_list_prompt_routers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_prompt_routers_request.ListPromptRoutersRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_prompt_routers(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        type: Optional["capo_bedrock.types.prompt_router_type.PromptRouterType"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.prompt_router_summary.PromptRouterSummary]":
        _token = next_token
        while True:
            _response = await self.list_prompt_routers(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                type=type,
            )
            _page = _resolve_path(_response, ("prompt_router_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def create_provisioned_model_throughput(
        self,
        model_units: "capo_bedrock.types.positive_integer.PositiveInteger",
        provisioned_model_name: "capo_bedrock.types.provisioned_model_name.ProvisionedModelName",
        model_id: "capo_bedrock.types.model_identifier.ModelIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        commitment_duration: Optional[
            "capo_bedrock.types.commitment_duration.CommitmentDuration"
        ] = None,
        tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
    ) -> "capo_bedrock.types.create_provisioned_model_throughput_response.CreateProvisionedModelThroughputResponse":
        """<p>Creates dedicated throughput for a base or custom model with the model units and for the duration that you specify. For pricing details, see <a href="http://aws.amazon.com/bedrock/pricing/">Amazon Bedrock Pricing</a>. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a> in the Amazon S3 User Guide.</p>
            model_units: <p>Number of model units to allocate. A model unit delivers a specific throughput level for the specified model. The throughput level of a model unit specifies the total number of input and output tokens that it can process and generate within a span of one minute. By default, your account has no model units for purchasing Provisioned Throughputs with commitment. You must first visit the <a href="https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase">Amazon Web Services support center</a> to request MUs.</p> <p>For model unit quotas, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html#prov-thru-quotas">Provisioned Throughput quotas</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p> <p>For more information about what an MU specifies, contact your Amazon Web Services account manager.</p>
            provisioned_model_name: <p>The name for this Provisioned Throughput.</p>
            model_id: <p>The Amazon Resource Name (ARN) or name of the model to associate with this Provisioned Throughput. For a list of models for which you can purchase Provisioned Throughput, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#prov-throughput-models">Amazon Bedrock model IDs for purchasing Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>
            commitment_duration: <p>The commitment duration requested for the Provisioned Throughput. Billing occurs hourly and is discounted for longer commitment terms. To request a no-commit Provisioned Throughput, omit this field.</p> <p>Custom models support all levels of commitment. To see which base models support no commitment, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/pt-supported.html">Supported regions and models for Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a> </p>
            tags: <p>Tags to associate with this Provisioned Throughput.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_provisioned_model_throughput_request.CreateProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_provisioned_model_throughput_response.CreateProvisionedModelThroughputResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_provisioned_model_throughput.async_create_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_provisioned_model_throughput_request.CreateProvisionedModelThroughputRequest = {
            "model_units": model_units,
            "provisioned_model_name": provisioned_model_name,
            "model_id": model_id,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if commitment_duration is not None:
            input_["commitment_duration"] = commitment_duration
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_provisioned_model_throughput(
        self,
        provisioned_model_id: "capo_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_provisioned_model_throughput_response.DeleteProvisionedModelThroughputResponse":
        """<p>Deletes a Provisioned Throughput. You can't delete a Provisioned Throughput before the commitment term is over. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_provisioned_model_throughput_request.DeleteProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_provisioned_model_throughput_response.DeleteProvisionedModelThroughputResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_provisioned_model_throughput.async_delete_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_provisioned_model_throughput_request.DeleteProvisionedModelThroughputRequest = {
            "provisioned_model_id": provisioned_model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_provisioned_model_throughput(
        self,
        provisioned_model_id: "capo_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_provisioned_model_throughput_response.GetProvisionedModelThroughputResponse":
        """<p>Returns details for a Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_provisioned_model_throughput_request.GetProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_provisioned_model_throughput_response.GetProvisionedModelThroughputResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_provisioned_model_throughput.async_get_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_provisioned_model_throughput_request.GetProvisionedModelThroughputRequest = {
            "provisioned_model_id": provisioned_model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_provisioned_model_throughputs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.provisioned_model_status.ProvisionedModelStatus"
        ] = None,
        model_arn_equals: Optional["capo_bedrock.types.model_arn.ModelArn"] = None,
        name_contains: Optional[
            "capo_bedrock.types.provisioned_model_name.ProvisionedModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_bedrock.types.sort_by_provisioned_models.SortByProvisionedModels"
        ] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse":
        """<p>Lists the Provisioned Throughputs in the account. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>A filter that returns Provisioned Throughputs created after the specified time. </p>
            creation_time_before: <p>A filter that returns Provisioned Throughputs created before the specified time. </p>
            status_equals: <p>A filter that returns Provisioned Throughputs if their statuses matches the value that you specify.</p>
            model_arn_equals: <p>A filter that returns Provisioned Throughputs whose model Amazon Resource Name (ARN) is equal to the value that you specify.</p>
            name_contains: <p>A filter that returns Provisioned Throughputs if their name contains the expression that you specify.</p>
            max_results: <p>THe maximum number of results to return in the response. If there are more results than the number you specified, the response returns a <code>nextToken</code> value. To see the next batch of results, send the <code>nextToken</code> value in another list request.</p>
            next_token: <p>If there are more results than the number you specified in the <code>maxResults</code> field, the response returns a <code>nextToken</code> value. To see the next batch of results, specify the <code>nextToken</code> value in this field.</p>
            sort_by: <p>The field by which to sort the returned list of Provisioned Throughputs.</p>
            sort_order: <p>The sort order of the results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_provisioned_model_throughputs_response.ListProvisionedModelThroughputsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_provisioned_model_throughputs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_provisioned_model_throughputs.async_list_provisioned_model_throughputs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_provisioned_model_throughputs_request.ListProvisionedModelThroughputsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if model_arn_equals is not None:
            input_["model_arn_equals"] = model_arn_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_provisioned_model_throughputs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.provisioned_model_status.ProvisionedModelStatus"
        ] = None,
        model_arn_equals: Optional["capo_bedrock.types.model_arn.ModelArn"] = None,
        name_contains: Optional[
            "capo_bedrock.types.provisioned_model_name.ProvisionedModelName"
        ] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional[
            "capo_bedrock.types.sort_by_provisioned_models.SortByProvisionedModels"
        ] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.provisioned_model_summary.ProvisionedModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_provisioned_model_throughputs(
                config_overrides=config_overrides,
                creation_time_after=creation_time_after,
                creation_time_before=creation_time_before,
                status_equals=status_equals,
                model_arn_equals=model_arn_equals,
                name_contains=name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("provisioned_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def update_provisioned_model_throughput(
        self,
        provisioned_model_id: "capo_bedrock.types.provisioned_model_id.ProvisionedModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        desired_provisioned_model_name: Optional[
            "capo_bedrock.types.provisioned_model_name.ProvisionedModelName"
        ] = None,
        desired_model_id: Optional[
            "capo_bedrock.types.model_identifier.ModelIdentifier"
        ] = None,
    ) -> "capo_bedrock.types.update_provisioned_model_throughput_response.UpdateProvisionedModelThroughputResponse":
        """<p>Updates the name or associated model for a Provisioned Throughput. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html">Provisioned Throughput</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            provisioned_model_id: <p>The Amazon Resource Name (ARN) or name of the Provisioned Throughput to update.</p>
            desired_provisioned_model_name: <p>The new name for this Provisioned Throughput.</p>
            desired_model_id: <p>The Amazon Resource Name (ARN) of the new model to associate with this Provisioned Throughput. You can't specify this field if this Provisioned Throughput is associated with a base model.</p> <p>If this Provisioned Throughput is associated with a custom model, you can specify one of the following options:</p> <ul> <li> <p>The base model from which the custom model was customized.</p> </li> <li> <p>Another custom model that was customized from the same base model as the custom model.</p> </li> </ul>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.update_provisioned_model_throughput_request.UpdateProvisionedModelThroughputRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.update_provisioned_model_throughput_response.UpdateProvisionedModelThroughputResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.update_provisioned_model_throughput

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.update_provisioned_model_throughput.async_update_provisioned_model_throughput(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.update_provisioned_model_throughput_request.UpdateProvisionedModelThroughputRequest = {
            "provisioned_model_id": provisioned_model_id
        }
        if desired_provisioned_model_name is not None:
            input_["desired_provisioned_model_name"] = desired_provisioned_model_name
        if desired_model_id is not None:
            input_["desired_model_id"] = desired_model_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a previously created Bedrock resource policy.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse":
        """<p>Gets the resource policy document for a Bedrock resource</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_resource_policy_response.GetResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_resource_policy.async_get_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_resource_policy_request.GetResourcePolicyRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_bedrock.types.resource_policy_resource_arn.ResourcePolicyResourceArn",
        resource_policy: "capo_bedrock.types.resource_policy_document.ResourcePolicyDocument",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Adds a resource policy for a Bedrock resource.</p>

        Args:
            resource_arn: <p>The ARN of the Bedrock resource to which this resource policy applies.</p>
            resource_policy: <p>The JSON string representing the Bedrock resource policy.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "resource_policy": resource_policy,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_foundation_model_agreement(
        self,
        offer_token: "capo_bedrock.types.offer_token.OfferToken",
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse":
        """<p>Request a model access agreement for the specified model.</p>

        Args:
            offer_token: <p>An offer token encapsulates the information for an offer.</p>
            model_id: <p>Model Id of the model for the access request.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_foundation_model_agreement_response.CreateFoundationModelAgreementResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_foundation_model_agreement.async_create_foundation_model_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_foundation_model_agreement_request.CreateFoundationModelAgreementRequest = {
            "offer_token": offer_token,
            "model_id": model_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_foundation_model_agreement(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse":
        """<p>Delete the model access agreement for the specified model.</p>

        Args:
            model_id: <p>Model Id of the model access to delete.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.delete_foundation_model_agreement_response.DeleteFoundationModelAgreementResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.delete_foundation_model_agreement.async_delete_foundation_model_agreement(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.delete_foundation_model_agreement_request.DeleteFoundationModelAgreementRequest = {
            "model_id": model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_foundation_model_availability(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse":
        """<p>Get information about the Foundation model availability.</p>

        Args:
            model_id: <p>The model Id of the foundation model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_foundation_model_availability_response.GetFoundationModelAvailabilityResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_foundation_model_availability.async_get_foundation_model_availability(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_foundation_model_availability_request.GetFoundationModelAvailabilityRequest = {
            "model_id": model_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_foundation_model_agreement_offers(
        self,
        model_id: "capo_bedrock.types.bedrock_model_id.BedrockModelId",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        offer_type: Optional["capo_bedrock.types.offer_type.OfferType"] = None,
    ) -> "capo_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse":
        """<p>Get the offers associated with the specified model.</p>

        Args:
            model_id: <p>Model Id of the foundation model.</p>
            offer_type: <p>Type of offer associated with the model.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_foundation_model_agreement_offers_response.ListFoundationModelAgreementOffersResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_foundation_model_agreement_offers.async_list_foundation_model_agreement_offers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_foundation_model_agreement_offers_request.ListFoundationModelAgreementOffersRequest = {
            "model_id": model_id
        }
        if offer_type is not None:
            input_["offer_type"] = offer_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> (
        "capo_bedrock.types.list_tags_for_resource_response.ListTagsForResourceResponse"
    ):
        """<p>List the tags associated with the specified resource.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
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
        resource_arn: "capo_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        tags: "capo_bedrock.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.tag_resource_response.TagResourceResponse":
        """<p>Associate tags with a resource. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to tag.</p>
            tags: <p>Tags to associate with the resource.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.tag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_bedrock.types.taggable_resources_arn.TaggableResourcesArn",
        tag_keys: "capo_bedrock.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.untag_resource_response.UntagResourceResponse":
        """<p>Remove one or more tags from a resource. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Tagging resources</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the resource to untag.</p>
            tag_keys: <p>Tag keys of the tags to remove from the resource.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.untag_resource

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.untag_resource_request.UntagResourceRequest = {
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

    async def create_model_customization_job(
        self,
        job_name: "capo_bedrock.types.job_name.JobName",
        custom_model_name: "capo_bedrock.types.custom_model_name.CustomModelName",
        role_arn: "capo_bedrock.types.role_arn.RoleArn",
        base_model_identifier: "capo_bedrock.types.base_model_identifier.BaseModelIdentifier",
        training_data_config: "capo_bedrock.types.training_data_config.TrainingDataConfig",
        output_data_config: "capo_bedrock.types.output_data_config.OutputDataConfig",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        client_request_token: Optional[
            "capo_bedrock.types.idempotency_token.IdempotencyToken"
        ] = None,
        customization_type: Optional[
            "capo_bedrock.types.customization_type.CustomizationType"
        ] = None,
        custom_model_kms_key_id: Optional[
            "capo_bedrock.types.kms_key_id.KmsKeyId"
        ] = None,
        job_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        custom_model_tags: Optional["capo_bedrock.types.tag_list.TagList"] = None,
        validation_data_config: Optional[
            "capo_bedrock.types.validation_data_config.ValidationDataConfig"
        ] = None,
        hyper_parameters: Optional[
            "capo_bedrock.types.model_customization_hyper_parameters.ModelCustomizationHyperParameters"
        ] = None,
        vpc_config: Optional["capo_bedrock.types.vpc_config.VpcConfig"] = None,
        customization_config: Optional[
            "capo_bedrock.types.customization_config.CustomizationConfig"
        ] = None,
    ) -> "capo_bedrock.types.create_model_customization_job_response.CreateModelCustomizationJobResponse":
        """<p>Creates a fine-tuning job to customize a base model.</p> <p>You specify the base foundation model and the location of the training data. After the model-customization job completes successfully, your custom model resource will be ready to use. Amazon Bedrock returns validation loss metrics and output generations after the job completes. </p> <p>For information on the format of training and validation data, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/model-customization-prepare.html">Prepare the datasets</a>.</p> <p> Model-customization jobs are asynchronous and the completion time depends on the base model and the training/validation data size. To monitor a job, use the <code>GetModelCustomizationJob</code> operation to retrieve the job status.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_name: <p>A name for the fine-tuning job.</p>
            custom_model_name: <p>A name for the resulting custom model.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM service role that Amazon Bedrock can assume to perform tasks on your behalf. For example, during model training, Amazon Bedrock needs your permission to read input data from an S3 bucket, write model artifacts to an S3 bucket. To pass this role to Amazon Bedrock, the caller of this API must have the <code>iam:PassRole</code> permission. </p>
            client_request_token: <p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html">Ensuring idempotency</a>.</p>
            base_model_identifier: <p>Name of the base model.</p>
            customization_type: <p>The customization type.</p>
            custom_model_kms_key_id: <p>The custom model is encrypted at rest using this key.</p>
            job_tags: <p>Tags to attach to the job.</p>
            custom_model_tags: <p>Tags to attach to the resulting custom model.</p>
            training_data_config: <p>Information about the training dataset.</p>
            validation_data_config: <p>Information about the validation dataset. </p>
            output_data_config: <p>S3 location for the output data.</p>
            hyper_parameters: <p>Parameters related to tuning the model. For details on the format for different models, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models-hp.html">Custom model hyperparameters</a>.</p>
            vpc_config: <p>The configuration of the Virtual Private Cloud (VPC) that contains the resources that you're using for this job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/vpc-model-customization.html">Protect your model customization jobs using a VPC</a>.</p>
            customization_config: <p>The customization configuration for the model customization job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The number of requests exceeds the service quota. Resubmit your request later.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.too_many_tags_exception.TooManyTagsException: <p>The request contains more tags than can be associated with a resource (50 tags per resource). The maximum number of tags includes both existing tags and those included in your current request. </p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.create_model_customization_job_request.CreateModelCustomizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.create_model_customization_job_response.CreateModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_customization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.create_model_customization_job.async_create_model_customization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.create_model_customization_job_request.CreateModelCustomizationJobRequest = {
            "job_name": job_name,
            "custom_model_name": custom_model_name,
            "role_arn": role_arn,
            "base_model_identifier": base_model_identifier,
            "training_data_config": training_data_config,
            "output_data_config": output_data_config,
        }
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if customization_type is not None:
            input_["customization_type"] = customization_type
        if custom_model_kms_key_id is not None:
            input_["custom_model_kms_key_id"] = custom_model_kms_key_id
        if job_tags is not None:
            input_["job_tags"] = job_tags
        if custom_model_tags is not None:
            input_["custom_model_tags"] = custom_model_tags
        if validation_data_config is not None:
            input_["validation_data_config"] = validation_data_config
        if hyper_parameters is not None:
            input_["hyper_parameters"] = hyper_parameters
        if vpc_config is not None:
            input_["vpc_config"] = vpc_config
        if customization_config is not None:
            input_["customization_config"] = customization_config

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_model_customization_job(
        self,
        job_identifier: "capo_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.get_model_customization_job_response.GetModelCustomizationJobResponse":
        """<p>Retrieves the properties associated with a model-customization job, including the status of the job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>Identifier for the customization job.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.get_model_customization_job_request.GetModelCustomizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.get_model_customization_job_response.GetModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_customization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.get_model_customization_job.async_get_model_customization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.get_model_customization_job_request.GetModelCustomizationJobRequest = {
            "job_identifier": job_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_model_customization_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.fine_tuning_job_status.FineTuningJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "capo_bedrock.types.list_model_customization_jobs_response.ListModelCustomizationJobsResponse":
        """<p>Returns a list of model customization jobs that you have submitted. You can filter the jobs to return based on one or more criteria.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            creation_time_after: <p>Return customization jobs created after the specified time. </p>
            creation_time_before: <p>Return customization jobs created before the specified time. </p>
            status_equals: <p>Return customization jobs with the specified status. </p>
            name_contains: <p>Return customization jobs only if the job name contains these characters.</p>
            max_results: <p>The maximum number of results to return in the response. If the total number of results is greater than this value, use the token returned in the response in the <code>nextToken</code> field when making another request to return the next batch of results.</p>
            next_token: <p>If the total number of results is greater than the <code>maxResults</code> value provided in the request, enter the token returned in the <code>nextToken</code> field in the response in this field to return the next batch of results.</p>
            sort_by: <p>The field to sort by in the returned list of jobs.</p>
            sort_order: <p>The sort order of the results.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.list_model_customization_jobs_request.ListModelCustomizationJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.list_model_customization_jobs_response.ListModelCustomizationJobsResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_customization_jobs

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.list_model_customization_jobs.async_list_model_customization_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.list_model_customization_jobs_request.ListModelCustomizationJobsRequest = {}
        if creation_time_after is not None:
            input_["creation_time_after"] = creation_time_after
        if creation_time_before is not None:
            input_["creation_time_before"] = creation_time_before
        if status_equals is not None:
            input_["status_equals"] = status_equals
        if name_contains is not None:
            input_["name_contains"] = name_contains
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_model_customization_jobs(
        self,
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
        creation_time_after: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        creation_time_before: Optional["capo_bedrock.types.timestamp.Timestamp"] = None,
        status_equals: Optional[
            "capo_bedrock.types.fine_tuning_job_status.FineTuningJobStatus"
        ] = None,
        name_contains: Optional["capo_bedrock.types.job_name.JobName"] = None,
        max_results: Optional["capo_bedrock.types.max_results.MaxResults"] = None,
        next_token: Optional[
            "capo_bedrock.types.pagination_token.PaginationToken"
        ] = None,
        sort_by: Optional["capo_bedrock.types.sort_jobs_by.SortJobsBy"] = None,
        sort_order: Optional["capo_bedrock.types.sort_order.SortOrder"] = None,
    ) -> "AsyncIterator[capo_bedrock.types.model_customization_job_summary.ModelCustomizationJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_model_customization_jobs(
                config_overrides=config_overrides,
                creation_time_after=creation_time_after,
                creation_time_before=creation_time_before,
                status_equals=status_equals,
                name_contains=name_contains,
                max_results=max_results,
                next_token=_token,
                sort_by=sort_by,
                sort_order=sort_order,
            )
            _page = _resolve_path(_response, ("model_customization_job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def stop_model_customization_job(
        self,
        job_identifier: "capo_bedrock.types.model_customization_job_identifier.ModelCustomizationJobIdentifier",
        *,
        config_overrides: Optional[AsyncBedrockClientConfig] = None,
    ) -> "capo_bedrock.types.stop_model_customization_job_response.StopModelCustomizationJobResponse":
        """<p>Stops an active model customization job. For more information, see <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html">Custom models</a> in the <a href="https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html">Amazon Bedrock User Guide</a>.</p>

        Args:
            job_identifier: <p>Job identifier of the job to stop.</p>

        Raises:
            capo_bedrock.errors.access_denied_exception.AccessDeniedException: <p>The request is denied because of missing access permissions.</p>
            capo_bedrock.errors.conflict_exception.ConflictException: <p>Error occurred because of a conflict while performing an operation.</p>
            capo_bedrock.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred. Retry your request.</p>
            capo_bedrock.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource Amazon Resource Name (ARN) was not found. Check the Amazon Resource Name (ARN) and try your request again.</p>
            capo_bedrock.errors.throttling_exception.ThrottlingException: <p>The number of requests exceeds the limit. Resubmit your request later.</p>
            capo_bedrock.errors.validation_exception.ValidationException: <p>Input validation failed. Check your request parameters and retry the request.</p>
            capo_bedrock.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_bedrock.types.stop_model_customization_job_request.StopModelCustomizationJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_bedrock.types.stop_model_customization_job_response.StopModelCustomizationJobResponse"
        ]:
            import capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_customization_job

            (
                output,
                http_response,
            ) = await capo_bedrock._operations.amazon_bedrock_control_plane_service.stop_model_customization_job.async_stop_model_customization_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_bedrock.types.stop_model_customization_job_request.StopModelCustomizationJobRequest = {
            "job_identifier": job_identifier
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
