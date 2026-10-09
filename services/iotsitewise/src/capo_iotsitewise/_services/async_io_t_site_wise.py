"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AWSIoTSiteWise``."""

import datetime
import time
import uuid
import warnings
from collections.abc import AsyncGenerator, AsyncIterator
from contextlib import asynccontextmanager
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_iotsitewise._auth._signers
import capo_iotsitewise._auth._sigv4
from capo_iotsitewise._async import anysleep
from capo_iotsitewise._auth._identity import Credentials
from capo_iotsitewise._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_iotsitewise._auth._zapros_handler import AuthMiddleware
from capo_iotsitewise._pagination import resolve_path as _resolve_path
from capo_iotsitewise._services._aws_config import aaws_config
from capo_iotsitewise._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)
from capo_iotsitewise.errors import ServiceError, WaiterTimeoutError

if TYPE_CHECKING:
    import capo_iotsitewise.types.access_policy_summary
    import capo_iotsitewise.types.action_payload
    import capo_iotsitewise.types.action_summary
    import capo_iotsitewise.types.adaptive_ingestion
    import capo_iotsitewise.types.aggregate_types
    import capo_iotsitewise.types.aggregated_value
    import capo_iotsitewise.types.alarms
    import capo_iotsitewise.types.amazon_resource_name
    import capo_iotsitewise.types.application_id
    import capo_iotsitewise.types.application_name
    import capo_iotsitewise.types.application_summary
    import capo_iotsitewise.types.arn
    import capo_iotsitewise.types.asset_model_composite_model_definitions
    import capo_iotsitewise.types.asset_model_composite_model_summary
    import capo_iotsitewise.types.asset_model_composite_models
    import capo_iotsitewise.types.asset_model_hierarchies
    import capo_iotsitewise.types.asset_model_hierarchy_definitions
    import capo_iotsitewise.types.asset_model_properties
    import capo_iotsitewise.types.asset_model_property_definitions
    import capo_iotsitewise.types.asset_model_property_summary
    import capo_iotsitewise.types.asset_model_summary
    import capo_iotsitewise.types.asset_model_type
    import capo_iotsitewise.types.asset_model_version_filter
    import capo_iotsitewise.types.asset_model_version_type
    import capo_iotsitewise.types.asset_property_alias
    import capo_iotsitewise.types.asset_property_summary
    import capo_iotsitewise.types.asset_property_value
    import capo_iotsitewise.types.asset_relationship_summary
    import capo_iotsitewise.types.asset_summary
    import capo_iotsitewise.types.associate_assets_request
    import capo_iotsitewise.types.associate_data_segment_entries
    import capo_iotsitewise.types.associate_time_series_to_asset_property_request
    import capo_iotsitewise.types.associated_assets_summary
    import capo_iotsitewise.types.auth_mode
    import capo_iotsitewise.types.batch_associate_data_segments_to_dataset_request
    import capo_iotsitewise.types.batch_associate_data_segments_to_dataset_response
    import capo_iotsitewise.types.batch_associate_project_assets_request
    import capo_iotsitewise.types.batch_associate_project_assets_response
    import capo_iotsitewise.types.batch_delete_dataset_data_segments_request
    import capo_iotsitewise.types.batch_delete_dataset_data_segments_response
    import capo_iotsitewise.types.batch_disassociate_data_segments_from_dataset_request
    import capo_iotsitewise.types.batch_disassociate_data_segments_from_dataset_response
    import capo_iotsitewise.types.batch_disassociate_project_assets_request
    import capo_iotsitewise.types.batch_disassociate_project_assets_response
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_entries
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_max_results
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_request
    import capo_iotsitewise.types.batch_get_asset_property_aggregates_response
    import capo_iotsitewise.types.batch_get_asset_property_value_entries
    import capo_iotsitewise.types.batch_get_asset_property_value_history_entries
    import capo_iotsitewise.types.batch_get_asset_property_value_history_max_results
    import capo_iotsitewise.types.batch_get_asset_property_value_history_request
    import capo_iotsitewise.types.batch_get_asset_property_value_history_response
    import capo_iotsitewise.types.batch_get_asset_property_value_request
    import capo_iotsitewise.types.batch_get_asset_property_value_response
    import capo_iotsitewise.types.batch_put_asset_property_value_request
    import capo_iotsitewise.types.batch_put_asset_property_value_response
    import capo_iotsitewise.types.boolean_value
    import capo_iotsitewise.types.bulk_import_job_name
    import capo_iotsitewise.types.cancel_enrichment_job_request
    import capo_iotsitewise.types.cancel_enrichment_job_response
    import capo_iotsitewise.types.cancel_pipeline_execution_request
    import capo_iotsitewise.types.cancel_pipeline_execution_request_reason_string
    import capo_iotsitewise.types.cancel_pipeline_execution_response
    import capo_iotsitewise.types.cancel_query_request
    import capo_iotsitewise.types.cancel_query_response
    import capo_iotsitewise.types.capability_configuration
    import capo_iotsitewise.types.capability_namespace
    import capo_iotsitewise.types.client_token
    import capo_iotsitewise.types.composition_relationship_summary
    import capo_iotsitewise.types.computation_model_configuration
    import capo_iotsitewise.types.computation_model_data_binding
    import capo_iotsitewise.types.computation_model_data_binding_usage_summary
    import capo_iotsitewise.types.computation_model_resolve_to_resource_summary
    import capo_iotsitewise.types.computation_model_summary
    import capo_iotsitewise.types.computation_model_type
    import capo_iotsitewise.types.computation_model_version_filter
    import capo_iotsitewise.types.compute_node_execution_details
    import capo_iotsitewise.types.compute_node_list
    import capo_iotsitewise.types.conversation_id
    import capo_iotsitewise.types.create_access_policy_request
    import capo_iotsitewise.types.create_access_policy_response
    import capo_iotsitewise.types.create_application_request
    import capo_iotsitewise.types.create_application_response
    import capo_iotsitewise.types.create_asset_model_composite_model_request
    import capo_iotsitewise.types.create_asset_model_composite_model_response
    import capo_iotsitewise.types.create_asset_model_request
    import capo_iotsitewise.types.create_asset_model_response
    import capo_iotsitewise.types.create_asset_request
    import capo_iotsitewise.types.create_asset_response
    import capo_iotsitewise.types.create_bulk_import_job_request
    import capo_iotsitewise.types.create_bulk_import_job_response
    import capo_iotsitewise.types.create_computation_model_request
    import capo_iotsitewise.types.create_computation_model_response
    import capo_iotsitewise.types.create_dashboard_request
    import capo_iotsitewise.types.create_dashboard_response
    import capo_iotsitewise.types.create_dataset_export_job_request
    import capo_iotsitewise.types.create_dataset_export_job_response
    import capo_iotsitewise.types.create_dataset_request
    import capo_iotsitewise.types.create_dataset_response
    import capo_iotsitewise.types.create_enrichment_job_request
    import capo_iotsitewise.types.create_enrichment_job_response
    import capo_iotsitewise.types.create_gateway_request
    import capo_iotsitewise.types.create_gateway_response
    import capo_iotsitewise.types.create_pipeline_request
    import capo_iotsitewise.types.create_pipeline_response
    import capo_iotsitewise.types.create_portal_request
    import capo_iotsitewise.types.create_portal_response
    import capo_iotsitewise.types.create_project_request
    import capo_iotsitewise.types.create_project_response
    import capo_iotsitewise.types.create_task_request
    import capo_iotsitewise.types.create_task_response
    import capo_iotsitewise.types.create_workspace_request
    import capo_iotsitewise.types.create_workspace_response
    import capo_iotsitewise.types.custom_id
    import capo_iotsitewise.types.dashboard_definition
    import capo_iotsitewise.types.dashboard_summary
    import capo_iotsitewise.types.data_binding_value_filter
    import capo_iotsitewise.types.data_segment_relationship_summary
    import capo_iotsitewise.types.data_segment_summary
    import capo_iotsitewise.types.dataset_config
    import capo_iotsitewise.types.dataset_export_job_filter
    import capo_iotsitewise.types.dataset_export_job_id
    import capo_iotsitewise.types.dataset_source
    import capo_iotsitewise.types.dataset_source_type
    import capo_iotsitewise.types.dataset_summary
    import capo_iotsitewise.types.dataset_type_enum
    import capo_iotsitewise.types.delete_access_policy_request
    import capo_iotsitewise.types.delete_access_policy_response
    import capo_iotsitewise.types.delete_application_request
    import capo_iotsitewise.types.delete_application_response
    import capo_iotsitewise.types.delete_asset_model_composite_model_request
    import capo_iotsitewise.types.delete_asset_model_composite_model_response
    import capo_iotsitewise.types.delete_asset_model_interface_relationship_request
    import capo_iotsitewise.types.delete_asset_model_interface_relationship_response
    import capo_iotsitewise.types.delete_asset_model_request
    import capo_iotsitewise.types.delete_asset_model_response
    import capo_iotsitewise.types.delete_asset_request
    import capo_iotsitewise.types.delete_asset_response
    import capo_iotsitewise.types.delete_computation_model_request
    import capo_iotsitewise.types.delete_computation_model_response
    import capo_iotsitewise.types.delete_dashboard_request
    import capo_iotsitewise.types.delete_dashboard_response
    import capo_iotsitewise.types.delete_data_segment_entries
    import capo_iotsitewise.types.delete_dataset_request
    import capo_iotsitewise.types.delete_dataset_response
    import capo_iotsitewise.types.delete_files_after_import
    import capo_iotsitewise.types.delete_gateway_request
    import capo_iotsitewise.types.delete_pipeline_request
    import capo_iotsitewise.types.delete_pipeline_response
    import capo_iotsitewise.types.delete_portal_request
    import capo_iotsitewise.types.delete_portal_response
    import capo_iotsitewise.types.delete_project_request
    import capo_iotsitewise.types.delete_project_response
    import capo_iotsitewise.types.delete_task_request
    import capo_iotsitewise.types.delete_task_response
    import capo_iotsitewise.types.delete_time_series_request
    import capo_iotsitewise.types.delete_workspace_request
    import capo_iotsitewise.types.delete_workspace_response
    import capo_iotsitewise.types.describe_access_policy_request
    import capo_iotsitewise.types.describe_access_policy_response
    import capo_iotsitewise.types.describe_action_request
    import capo_iotsitewise.types.describe_action_response
    import capo_iotsitewise.types.describe_application_request
    import capo_iotsitewise.types.describe_application_response
    import capo_iotsitewise.types.describe_asset_composite_model_request
    import capo_iotsitewise.types.describe_asset_composite_model_response
    import capo_iotsitewise.types.describe_asset_model_composite_model_request
    import capo_iotsitewise.types.describe_asset_model_composite_model_response
    import capo_iotsitewise.types.describe_asset_model_interface_relationship_request
    import capo_iotsitewise.types.describe_asset_model_interface_relationship_response
    import capo_iotsitewise.types.describe_asset_model_request
    import capo_iotsitewise.types.describe_asset_model_response
    import capo_iotsitewise.types.describe_asset_property_request
    import capo_iotsitewise.types.describe_asset_property_response
    import capo_iotsitewise.types.describe_asset_request
    import capo_iotsitewise.types.describe_asset_response
    import capo_iotsitewise.types.describe_bulk_import_job_request
    import capo_iotsitewise.types.describe_bulk_import_job_response
    import capo_iotsitewise.types.describe_computation_model_execution_summary_request
    import capo_iotsitewise.types.describe_computation_model_execution_summary_response
    import capo_iotsitewise.types.describe_computation_model_request
    import capo_iotsitewise.types.describe_computation_model_response
    import capo_iotsitewise.types.describe_dashboard_request
    import capo_iotsitewise.types.describe_dashboard_response
    import capo_iotsitewise.types.describe_dataset_export_job_request
    import capo_iotsitewise.types.describe_dataset_export_job_response
    import capo_iotsitewise.types.describe_dataset_request
    import capo_iotsitewise.types.describe_dataset_response
    import capo_iotsitewise.types.describe_default_encryption_configuration_request
    import capo_iotsitewise.types.describe_default_encryption_configuration_response
    import capo_iotsitewise.types.describe_enrichment_job_request
    import capo_iotsitewise.types.describe_enrichment_job_response
    import capo_iotsitewise.types.describe_execution_request
    import capo_iotsitewise.types.describe_execution_response
    import capo_iotsitewise.types.describe_gateway_capability_configuration_request
    import capo_iotsitewise.types.describe_gateway_capability_configuration_response
    import capo_iotsitewise.types.describe_gateway_request
    import capo_iotsitewise.types.describe_gateway_response
    import capo_iotsitewise.types.describe_logging_options_request
    import capo_iotsitewise.types.describe_logging_options_response
    import capo_iotsitewise.types.describe_pipeline_execution_request
    import capo_iotsitewise.types.describe_pipeline_execution_request_max_results_integer
    import capo_iotsitewise.types.describe_pipeline_execution_response
    import capo_iotsitewise.types.describe_pipeline_request
    import capo_iotsitewise.types.describe_pipeline_response
    import capo_iotsitewise.types.describe_portal_request
    import capo_iotsitewise.types.describe_portal_response
    import capo_iotsitewise.types.describe_project_request
    import capo_iotsitewise.types.describe_project_response
    import capo_iotsitewise.types.describe_query_request
    import capo_iotsitewise.types.describe_query_response
    import capo_iotsitewise.types.describe_search_request
    import capo_iotsitewise.types.describe_search_response
    import capo_iotsitewise.types.describe_storage_configuration_request
    import capo_iotsitewise.types.describe_storage_configuration_response
    import capo_iotsitewise.types.describe_task_request
    import capo_iotsitewise.types.describe_task_response
    import capo_iotsitewise.types.describe_time_series_request
    import capo_iotsitewise.types.describe_time_series_response
    import capo_iotsitewise.types.describe_workspace_request
    import capo_iotsitewise.types.describe_workspace_response
    import capo_iotsitewise.types.description
    import capo_iotsitewise.types.disallow_ingest_null_na_n
    import capo_iotsitewise.types.disassociate_assets_request
    import capo_iotsitewise.types.disassociate_data_segment_entries
    import capo_iotsitewise.types.disassociate_time_series_from_asset_property_request
    import capo_iotsitewise.types.disassociated_data_storage_state
    import capo_iotsitewise.types.e_tag
    import capo_iotsitewise.types.email
    import capo_iotsitewise.types.encryption_type
    import capo_iotsitewise.types.enrichment_job_configuration
    import capo_iotsitewise.types.enrichment_job_status
    import capo_iotsitewise.types.enrichment_job_summary
    import capo_iotsitewise.types.environment_variables_map
    import capo_iotsitewise.types.error_report_location
    import capo_iotsitewise.types.exclude_properties
    import capo_iotsitewise.types.execute_action_request
    import capo_iotsitewise.types.execute_action_response
    import capo_iotsitewise.types.execute_query_max_results
    import capo_iotsitewise.types.execute_query_next_token
    import capo_iotsitewise.types.execute_query_request
    import capo_iotsitewise.types.execute_query_response
    import capo_iotsitewise.types.execution_environment_variables
    import capo_iotsitewise.types.execution_priority
    import capo_iotsitewise.types.execution_summary
    import capo_iotsitewise.types.export_error_report_location
    import capo_iotsitewise.types.export_job_summary
    import capo_iotsitewise.types.external_id
    import capo_iotsitewise.types.files
    import capo_iotsitewise.types.format_settings
    import capo_iotsitewise.types.gateway_name
    import capo_iotsitewise.types.gateway_platform
    import capo_iotsitewise.types.gateway_summary
    import capo_iotsitewise.types.gateway_version
    import capo_iotsitewise.types.get_asset_property_aggregates_request
    import capo_iotsitewise.types.get_asset_property_aggregates_response
    import capo_iotsitewise.types.get_asset_property_value_aggregates_max_results
    import capo_iotsitewise.types.get_asset_property_value_history_max_results
    import capo_iotsitewise.types.get_asset_property_value_history_request
    import capo_iotsitewise.types.get_asset_property_value_history_response
    import capo_iotsitewise.types.get_asset_property_value_request
    import capo_iotsitewise.types.get_asset_property_value_response
    import capo_iotsitewise.types.get_capture_data_next_token
    import capo_iotsitewise.types.get_capture_data_request
    import capo_iotsitewise.types.get_capture_data_response
    import capo_iotsitewise.types.get_interpolated_asset_property_values_request
    import capo_iotsitewise.types.get_interpolated_asset_property_values_response
    import capo_iotsitewise.types.get_query_results_request
    import capo_iotsitewise.types.get_query_results_response
    import capo_iotsitewise.types.get_search_results_request
    import capo_iotsitewise.types.get_search_results_request_max_results_integer
    import capo_iotsitewise.types.get_search_results_response
    import capo_iotsitewise.types.group_id
    import capo_iotsitewise.types.i_ds
    import capo_iotsitewise.types.iam_arn
    import capo_iotsitewise.types.id
    import capo_iotsitewise.types.identity
    import capo_iotsitewise.types.identity_id
    import capo_iotsitewise.types.identity_type
    import capo_iotsitewise.types.image
    import capo_iotsitewise.types.image_file
    import capo_iotsitewise.types.interface_relationship_summary
    import capo_iotsitewise.types.interpolated_asset_property_value
    import capo_iotsitewise.types.interpolation_type
    import capo_iotsitewise.types.interval_in_seconds
    import capo_iotsitewise.types.interval_window_in_seconds
    import capo_iotsitewise.types.invoke_assistant_request
    import capo_iotsitewise.types.invoke_assistant_response
    import capo_iotsitewise.types.job_configuration
    import capo_iotsitewise.types.job_summary
    import capo_iotsitewise.types.job_type
    import capo_iotsitewise.types.kms_key_id
    import capo_iotsitewise.types.list_access_policies_request
    import capo_iotsitewise.types.list_access_policies_response
    import capo_iotsitewise.types.list_actions_request
    import capo_iotsitewise.types.list_actions_response
    import capo_iotsitewise.types.list_applications_request
    import capo_iotsitewise.types.list_applications_response
    import capo_iotsitewise.types.list_asset_model_composite_models_request
    import capo_iotsitewise.types.list_asset_model_composite_models_response
    import capo_iotsitewise.types.list_asset_model_properties_filter
    import capo_iotsitewise.types.list_asset_model_properties_request
    import capo_iotsitewise.types.list_asset_model_properties_response
    import capo_iotsitewise.types.list_asset_models_request
    import capo_iotsitewise.types.list_asset_models_response
    import capo_iotsitewise.types.list_asset_models_type_filter
    import capo_iotsitewise.types.list_asset_properties_filter
    import capo_iotsitewise.types.list_asset_properties_request
    import capo_iotsitewise.types.list_asset_properties_response
    import capo_iotsitewise.types.list_asset_relationships_request
    import capo_iotsitewise.types.list_asset_relationships_response
    import capo_iotsitewise.types.list_assets_filter
    import capo_iotsitewise.types.list_assets_request
    import capo_iotsitewise.types.list_assets_response
    import capo_iotsitewise.types.list_associated_assets_request
    import capo_iotsitewise.types.list_associated_assets_response
    import capo_iotsitewise.types.list_bulk_import_jobs_filter
    import capo_iotsitewise.types.list_bulk_import_jobs_request
    import capo_iotsitewise.types.list_bulk_import_jobs_response
    import capo_iotsitewise.types.list_composition_relationships_request
    import capo_iotsitewise.types.list_composition_relationships_response
    import capo_iotsitewise.types.list_computation_model_data_binding_usages_request
    import capo_iotsitewise.types.list_computation_model_data_binding_usages_response
    import capo_iotsitewise.types.list_computation_model_resolve_to_resources_request
    import capo_iotsitewise.types.list_computation_model_resolve_to_resources_response
    import capo_iotsitewise.types.list_computation_models_request
    import capo_iotsitewise.types.list_computation_models_response
    import capo_iotsitewise.types.list_dashboards_request
    import capo_iotsitewise.types.list_dashboards_response
    import capo_iotsitewise.types.list_dataset_data_segment_relationships_request
    import capo_iotsitewise.types.list_dataset_data_segment_relationships_response
    import capo_iotsitewise.types.list_dataset_data_segments_request
    import capo_iotsitewise.types.list_dataset_data_segments_response
    import capo_iotsitewise.types.list_dataset_export_jobs_request
    import capo_iotsitewise.types.list_dataset_export_jobs_response
    import capo_iotsitewise.types.list_datasets_request
    import capo_iotsitewise.types.list_datasets_response
    import capo_iotsitewise.types.list_enrichment_jobs_request
    import capo_iotsitewise.types.list_enrichment_jobs_response
    import capo_iotsitewise.types.list_executions_request
    import capo_iotsitewise.types.list_executions_response
    import capo_iotsitewise.types.list_export_jobs_max_results
    import capo_iotsitewise.types.list_export_jobs_next_token
    import capo_iotsitewise.types.list_gateways_request
    import capo_iotsitewise.types.list_gateways_response
    import capo_iotsitewise.types.list_interface_relationships_request
    import capo_iotsitewise.types.list_interface_relationships_response
    import capo_iotsitewise.types.list_pipeline_executions_request
    import capo_iotsitewise.types.list_pipeline_executions_request_max_results_integer
    import capo_iotsitewise.types.list_pipeline_executions_response
    import capo_iotsitewise.types.list_pipelines_request
    import capo_iotsitewise.types.list_pipelines_request_max_results_integer
    import capo_iotsitewise.types.list_pipelines_response
    import capo_iotsitewise.types.list_portals_request
    import capo_iotsitewise.types.list_portals_response
    import capo_iotsitewise.types.list_project_assets_request
    import capo_iotsitewise.types.list_project_assets_response
    import capo_iotsitewise.types.list_projects_request
    import capo_iotsitewise.types.list_projects_response
    import capo_iotsitewise.types.list_queries_request
    import capo_iotsitewise.types.list_queries_response
    import capo_iotsitewise.types.list_searches_filters
    import capo_iotsitewise.types.list_searches_request
    import capo_iotsitewise.types.list_searches_request_max_results_integer
    import capo_iotsitewise.types.list_searches_response
    import capo_iotsitewise.types.list_tags_for_resource_request
    import capo_iotsitewise.types.list_tags_for_resource_response
    import capo_iotsitewise.types.list_tasks_request
    import capo_iotsitewise.types.list_tasks_request_max_results_integer
    import capo_iotsitewise.types.list_tasks_response
    import capo_iotsitewise.types.list_time_series_request
    import capo_iotsitewise.types.list_time_series_response
    import capo_iotsitewise.types.list_time_series_type
    import capo_iotsitewise.types.list_workspaces_request
    import capo_iotsitewise.types.list_workspaces_response
    import capo_iotsitewise.types.logging_options
    import capo_iotsitewise.types.max_interpolated_results
    import capo_iotsitewise.types.max_results
    import capo_iotsitewise.types.message_input
    import capo_iotsitewise.types.metadata
    import capo_iotsitewise.types.mount_overrides
    import capo_iotsitewise.types.multi_layer_storage
    import capo_iotsitewise.types.name
    import capo_iotsitewise.types.next_token
    import capo_iotsitewise.types.offset_in_nanos
    import capo_iotsitewise.types.pagination_token
    import capo_iotsitewise.types.permission
    import capo_iotsitewise.types.pipeline_execution_state
    import capo_iotsitewise.types.pipeline_execution_summary
    import capo_iotsitewise.types.pipeline_summary
    import capo_iotsitewise.types.portal_summary
    import capo_iotsitewise.types.portal_type
    import capo_iotsitewise.types.portal_type_configuration
    import capo_iotsitewise.types.processing_input
    import capo_iotsitewise.types.project_summary
    import capo_iotsitewise.types.property_alias
    import capo_iotsitewise.types.property_mapping_configuration
    import capo_iotsitewise.types.property_notification_state
    import capo_iotsitewise.types.property_unit
    import capo_iotsitewise.types.put_asset_model_interface_relationship_request
    import capo_iotsitewise.types.put_asset_model_interface_relationship_response
    import capo_iotsitewise.types.put_asset_property_value_entries
    import capo_iotsitewise.types.put_default_encryption_configuration_request
    import capo_iotsitewise.types.put_default_encryption_configuration_response
    import capo_iotsitewise.types.put_logging_options_request
    import capo_iotsitewise.types.put_logging_options_response
    import capo_iotsitewise.types.put_storage_configuration_request
    import capo_iotsitewise.types.put_storage_configuration_response
    import capo_iotsitewise.types.qualities
    import capo_iotsitewise.types.quality
    import capo_iotsitewise.types.query_filter
    import capo_iotsitewise.types.query_id
    import capo_iotsitewise.types.query_list_next_token
    import capo_iotsitewise.types.query_max_results
    import capo_iotsitewise.types.query_next_token
    import capo_iotsitewise.types.query_statement
    import capo_iotsitewise.types.query_string
    import capo_iotsitewise.types.query_summary
    import capo_iotsitewise.types.resolution
    import capo_iotsitewise.types.resolve_to
    import capo_iotsitewise.types.resolve_to_resource_type
    import capo_iotsitewise.types.resource
    import capo_iotsitewise.types.resource_name
    import capo_iotsitewise.types.resource_type
    import capo_iotsitewise.types.restricted_description
    import capo_iotsitewise.types.restricted_name
    import capo_iotsitewise.types.result
    import capo_iotsitewise.types.retention_period
    import capo_iotsitewise.types.row
    import capo_iotsitewise.types.s3_uri
    import capo_iotsitewise.types.search_filters
    import capo_iotsitewise.types.search_id
    import capo_iotsitewise.types.search_query_statement
    import capo_iotsitewise.types.search_result
    import capo_iotsitewise.types.search_summary
    import capo_iotsitewise.types.search_type
    import capo_iotsitewise.types.select_all
    import capo_iotsitewise.types.start_pipeline_execution_request
    import capo_iotsitewise.types.start_pipeline_execution_response
    import capo_iotsitewise.types.start_query_request
    import capo_iotsitewise.types.start_query_response
    import capo_iotsitewise.types.start_search_request
    import capo_iotsitewise.types.start_search_response
    import capo_iotsitewise.types.storage_type
    import capo_iotsitewise.types.tag_key_list
    import capo_iotsitewise.types.tag_map
    import capo_iotsitewise.types.tag_resource_request
    import capo_iotsitewise.types.tag_resource_response
    import capo_iotsitewise.types.target_resource
    import capo_iotsitewise.types.target_resource_type
    import capo_iotsitewise.types.task_configuration
    import capo_iotsitewise.types.task_summary
    import capo_iotsitewise.types.time_in_nanos
    import capo_iotsitewise.types.time_in_seconds
    import capo_iotsitewise.types.time_ordering
    import capo_iotsitewise.types.time_series_id
    import capo_iotsitewise.types.time_series_summary
    import capo_iotsitewise.types.timestamp
    import capo_iotsitewise.types.traversal_direction
    import capo_iotsitewise.types.traversal_type
    import capo_iotsitewise.types.untag_resource_request
    import capo_iotsitewise.types.untag_resource_response
    import capo_iotsitewise.types.update_access_policy_request
    import capo_iotsitewise.types.update_access_policy_response
    import capo_iotsitewise.types.update_asset_model_composite_model_request
    import capo_iotsitewise.types.update_asset_model_composite_model_response
    import capo_iotsitewise.types.update_asset_model_request
    import capo_iotsitewise.types.update_asset_model_response
    import capo_iotsitewise.types.update_asset_property_request
    import capo_iotsitewise.types.update_asset_request
    import capo_iotsitewise.types.update_asset_response
    import capo_iotsitewise.types.update_computation_model_request
    import capo_iotsitewise.types.update_computation_model_response
    import capo_iotsitewise.types.update_dashboard_request
    import capo_iotsitewise.types.update_dashboard_response
    import capo_iotsitewise.types.update_dataset_request
    import capo_iotsitewise.types.update_dataset_response
    import capo_iotsitewise.types.update_gateway_capability_configuration_request
    import capo_iotsitewise.types.update_gateway_capability_configuration_response
    import capo_iotsitewise.types.update_gateway_request
    import capo_iotsitewise.types.update_pipeline_request
    import capo_iotsitewise.types.update_pipeline_response
    import capo_iotsitewise.types.update_portal_request
    import capo_iotsitewise.types.update_portal_response
    import capo_iotsitewise.types.update_project_request
    import capo_iotsitewise.types.update_project_response
    import capo_iotsitewise.types.update_task_request
    import capo_iotsitewise.types.update_task_response
    import capo_iotsitewise.types.update_workspace_request
    import capo_iotsitewise.types.update_workspace_response
    import capo_iotsitewise.types.version
    import capo_iotsitewise.types.warm_tier_retention_period
    import capo_iotsitewise.types.warm_tier_state
    import capo_iotsitewise.types.workspace_encryption_configuration
    import capo_iotsitewise.types.workspace_name
    import capo_iotsitewise.types.workspace_summary


class AsyncIoTSiteWiseClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncIoTSiteWiseClient:
    """A client for the ``IoTSiteWise`` service.

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
        self._config = AsyncIoTSiteWiseClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncIoTSiteWiseClientConfig = config_overrides or {}
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

    async def associate_assets(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        hierarchy_id: "capo_iotsitewise.types.custom_id.CustomID",
        child_asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Associates a child asset with the given parent asset through a hierarchy defined in the parent asset's model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/add-associated-assets.html">Associating assets</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_id: <p>The ID of the parent asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            hierarchy_id: <p>The ID of a hierarchy in the parent asset's model. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.) Hierarchies allow different groupings of assets to be formed that all come from the same asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
            child_asset_id: <p>The ID of the child asset to be associated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.associate_assets_request.AssociateAssetsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.associate_assets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.associate_assets.async_associate_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.associate_assets_request.AssociateAssetsRequest = {
            "asset_id": asset_id,
            "hierarchy_id": hierarchy_id,
            "child_asset_id": child_asset_id,
        }
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

    async def associate_time_series_to_asset_property(
        self,
        alias: "capo_iotsitewise.types.property_alias.PropertyAlias",
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        property_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Associates a time series (data stream) with an asset property.</p>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.associate_time_series_to_asset_property_request.AssociateTimeSeriesToAssetPropertyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.associate_time_series_to_asset_property

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.associate_time_series_to_asset_property.async_associate_time_series_to_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.associate_time_series_to_asset_property_request.AssociateTimeSeriesToAssetPropertyRequest = {
            "alias": alias,
            "asset_id": asset_id,
            "property_id": property_id,
        }
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

    async def batch_associate_data_segments_to_dataset(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        associate_data_segment_entries: "capo_iotsitewise.types.associate_data_segment_entries.AssociateDataSegmentEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_associate_data_segments_to_dataset_response.BatchAssociateDataSegmentsToDatasetResponse":
        """<p>Associates a batch of data segments with a curated dataset. Data segments are time-bounded slices of time series data selected from source session datasets. Data segments that belong to the same time series can't overlap in time, regardless of which dataset they belong to.</p>

        Args:
            dataset_id: <p>The ID of the curated dataset to associate data segments with.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            associate_data_segment_entries: <p>The list of data segment entries to associate with the dataset.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_associate_data_segments_to_dataset_request.BatchAssociateDataSegmentsToDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_associate_data_segments_to_dataset_response.BatchAssociateDataSegmentsToDatasetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_associate_data_segments_to_dataset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_associate_data_segments_to_dataset.async_batch_associate_data_segments_to_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_associate_data_segments_to_dataset_request.BatchAssociateDataSegmentsToDatasetRequest = {
            "dataset_id": dataset_id,
            "workspace_name": workspace_name,
            "associate_data_segment_entries": associate_data_segment_entries,
        }
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

    async def batch_associate_project_assets(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        asset_ids: "capo_iotsitewise.types.i_ds.IDs",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_associate_project_assets_response.BatchAssociateProjectAssetsResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Associates a group (batch) of assets with an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project to which to associate the assets.</p>
            asset_ids: <p>The IDs of the assets to be associated to the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_associate_project_assets_request.BatchAssociateProjectAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_associate_project_assets_response.BatchAssociateProjectAssetsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_associate_project_assets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_associate_project_assets.async_batch_associate_project_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_associate_project_assets_request.BatchAssociateProjectAssetsRequest = {
            "project_id": project_id,
            "asset_ids": asset_ids,
        }
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

    async def batch_delete_dataset_data_segments(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        delete_data_segment_entries: "capo_iotsitewise.types.delete_data_segment_entries.DeleteDataSegmentEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_delete_dataset_data_segments_response.BatchDeleteDatasetDataSegmentsResponse":
        """<p>Deletes a batch of data segments from a session dataset. Deleting a data segment deletes the underlying time series data for the segment's time range.</p>

        Args:
            dataset_id: <p>The ID of the session dataset from which to delete data segments.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            delete_data_segment_entries: <p>The list of data segment entries to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_delete_dataset_data_segments_request.BatchDeleteDatasetDataSegmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_delete_dataset_data_segments_response.BatchDeleteDatasetDataSegmentsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_delete_dataset_data_segments

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_delete_dataset_data_segments.async_batch_delete_dataset_data_segments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_delete_dataset_data_segments_request.BatchDeleteDatasetDataSegmentsRequest = {
            "dataset_id": dataset_id,
            "workspace_name": workspace_name,
            "delete_data_segment_entries": delete_data_segment_entries,
        }
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

    async def batch_disassociate_data_segments_from_dataset(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        disassociate_data_segment_entries: "capo_iotsitewise.types.disassociate_data_segment_entries.DisassociateDataSegmentEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_disassociate_data_segments_from_dataset_response.BatchDisassociateDataSegmentsFromDatasetResponse":
        """<p>Disassociates a batch of data segments from a curated dataset. Disassociating a data segment doesn't delete the underlying data in the source session dataset.</p>

        Args:
            dataset_id: <p>The ID of the curated dataset to disassociate data segments from.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            disassociate_data_segment_entries: <p>The list of data segment entries to disassociate from the dataset.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_disassociate_data_segments_from_dataset_request.BatchDisassociateDataSegmentsFromDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_disassociate_data_segments_from_dataset_response.BatchDisassociateDataSegmentsFromDatasetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_disassociate_data_segments_from_dataset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_disassociate_data_segments_from_dataset.async_batch_disassociate_data_segments_from_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_disassociate_data_segments_from_dataset_request.BatchDisassociateDataSegmentsFromDatasetRequest = {
            "dataset_id": dataset_id,
            "workspace_name": workspace_name,
            "disassociate_data_segment_entries": disassociate_data_segment_entries,
        }
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

    async def batch_disassociate_project_assets(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        asset_ids: "capo_iotsitewise.types.i_ds.IDs",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_disassociate_project_assets_response.BatchDisassociateProjectAssetsResponse":
        """<p>Disassociates a group (batch) of assets from an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project from which to disassociate the assets.</p>
            asset_ids: <p>The IDs of the assets to be disassociated from the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_disassociate_project_assets_request.BatchDisassociateProjectAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_disassociate_project_assets_response.BatchDisassociateProjectAssetsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_disassociate_project_assets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_disassociate_project_assets.async_batch_disassociate_project_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_disassociate_project_assets_request.BatchDisassociateProjectAssetsRequest = {
            "project_id": project_id,
            "asset_ids": asset_ids,
        }
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

    async def batch_get_asset_property_aggregates(
        self,
        entries: "capo_iotsitewise.types.batch_get_asset_property_aggregates_entries.BatchGetAssetPropertyAggregatesEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.batch_get_asset_property_aggregates_max_results.BatchGetAssetPropertyAggregatesMaxResults"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_get_asset_property_aggregates_response.BatchGetAssetPropertyAggregatesResponse":
        """<p>Gets aggregated values (for example, average, minimum, and maximum) for one or more asset properties. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates">Querying aggregates</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            entries: <p>The list of asset property aggregate entries for the batch get request. You can specify up to 16 entries per request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 1 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 4000.</p> </li> </ul>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_get_asset_property_aggregates_request.BatchGetAssetPropertyAggregatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_get_asset_property_aggregates_response.BatchGetAssetPropertyAggregatesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_aggregates

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_aggregates.async_batch_get_asset_property_aggregates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_get_asset_property_aggregates_request.BatchGetAssetPropertyAggregatesRequest = {
            "entries": entries
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

    async def iter_batch_get_asset_property_aggregates(
        self,
        entries: "capo_iotsitewise.types.batch_get_asset_property_aggregates_entries.BatchGetAssetPropertyAggregatesEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.batch_get_asset_property_aggregates_max_results.BatchGetAssetPropertyAggregatesMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.batch_get_asset_property_aggregates_response.BatchGetAssetPropertyAggregatesResponse]":
        _token = next_token
        while True:
            _response = await self.batch_get_asset_property_aggregates(
                entries,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_get_asset_property_value(
        self,
        entries: "capo_iotsitewise.types.batch_get_asset_property_value_entries.BatchGetAssetPropertyValueEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "capo_iotsitewise.types.batch_get_asset_property_value_response.BatchGetAssetPropertyValueResponse":
        """<p>Gets the current value for one or more asset properties. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values">Querying current values</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            entries: <p>The list of asset property value entries for the batch get request. You can specify up to 128 entries per request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_get_asset_property_value_request.BatchGetAssetPropertyValueRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_get_asset_property_value_response.BatchGetAssetPropertyValueResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value.async_batch_get_asset_property_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_get_asset_property_value_request.BatchGetAssetPropertyValueRequest = {
            "entries": entries
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

    async def iter_batch_get_asset_property_value(
        self,
        entries: "capo_iotsitewise.types.batch_get_asset_property_value_entries.BatchGetAssetPropertyValueEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.batch_get_asset_property_value_response.BatchGetAssetPropertyValueResponse]":
        _token = next_token
        while True:
            _response = await self.batch_get_asset_property_value(
                entries,
                config_overrides=config_overrides,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_get_asset_property_value_history(
        self,
        entries: "capo_iotsitewise.types.batch_get_asset_property_value_history_entries.BatchGetAssetPropertyValueHistoryEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.batch_get_asset_property_value_history_max_results.BatchGetAssetPropertyValueHistoryMaxResults"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_get_asset_property_value_history_response.BatchGetAssetPropertyValueHistoryResponse":
        """<p>Gets the historical values for one or more asset properties. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values">Querying historical values</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            entries: <p>The list of asset property historical value entries for the batch get request. You can specify up to 16 entries per request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 4 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 20000.</p> </li> </ul>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_get_asset_property_value_history_request.BatchGetAssetPropertyValueHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_get_asset_property_value_history_response.BatchGetAssetPropertyValueHistoryResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value_history

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_get_asset_property_value_history.async_batch_get_asset_property_value_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_get_asset_property_value_history_request.BatchGetAssetPropertyValueHistoryRequest = {
            "entries": entries
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

    async def iter_batch_get_asset_property_value_history(
        self,
        entries: "capo_iotsitewise.types.batch_get_asset_property_value_history_entries.BatchGetAssetPropertyValueHistoryEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.batch_get_asset_property_value_history_max_results.BatchGetAssetPropertyValueHistoryMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.batch_get_asset_property_value_history_response.BatchGetAssetPropertyValueHistoryResponse]":
        _token = next_token
        while True:
            _response = await self.batch_get_asset_property_value_history(
                entries,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def batch_put_asset_property_value(
        self,
        entries: "capo_iotsitewise.types.put_asset_property_value_entries.PutAssetPropertyValueEntries",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        enable_partial_entry_processing: Optional[
            "capo_iotsitewise.types.boolean_value.BooleanValue"
        ] = None,
    ) -> "capo_iotsitewise.types.batch_put_asset_property_value_response.BatchPutAssetPropertyValueResponse":
        """<p>Sends a list of asset property values to IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html">Ingesting data using the API</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html">UpdateAssetProperty</a>.</p> </li> </ul> <important> <p>With respect to Unix epoch time, IoT SiteWise accepts only TQVs that have a timestamp of no more than 7 days in the past and no more than 10 minutes in the future. IoT SiteWise rejects timestamps outside of the inclusive range of [-7 days, +10 minutes] and returns a <code>TimestampOutOfRangeException</code> error.</p> <p>For each asset property, IoT SiteWise overwrites TQVs with duplicate timestamps unless the newer TQV has a different quality. For example, if you store a TQV <code>{T1, GOOD, V1}</code>, then storing <code>{T1, GOOD, V2}</code> replaces the existing TQV.</p> </important> <p>IoT SiteWise authorizes access to each <code>BatchPutAssetPropertyValue</code> entry individually. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action">BatchPutAssetPropertyValue authorization</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            enable_partial_entry_processing: <p>This setting enables partial ingestion at entry-level. If set to <code>true</code>, we ingest all TQVs not resulting in an error. If set to <code>false</code>, an invalid TQV fails ingestion of the entire entry that contains it.</p>
            entries: <p>The list of asset property value entries for the batch put request. You can specify up to 10 entries per request.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.batch_put_asset_property_value_request.BatchPutAssetPropertyValueRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.batch_put_asset_property_value_response.BatchPutAssetPropertyValueResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.batch_put_asset_property_value

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.batch_put_asset_property_value.async_batch_put_asset_property_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.batch_put_asset_property_value_request.BatchPutAssetPropertyValueRequest = {
            "entries": entries
        }
        if enable_partial_entry_processing is not None:
            input_["enable_partial_entry_processing"] = enable_partial_entry_processing

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_enrichment_job(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        job_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.cancel_enrichment_job_response.CancelEnrichmentJobResponse":
        """<p>Cancels a running or pending enrichment job. This is an idempotent operation—calling it multiple times with the same jobId is safe and returns the current status.</p> <h2>Behavior</h2> <ul> <li>Jobs in PENDING or RUNNING status transition to CANCELLED</li> <li>Jobs in RUNNING state may not be cancellable once they have progressed to certain processing stages</li> <li>Jobs already in terminal states (COMPLETED, FAILED, TIMED_OUT) cannot be cancelled; the operation returns a ConflictingOperationException</li> <li>Cancelling an already-CANCELLED job is a no-op and returns the current status (idempotent behavior)</li> <li>The API responds immediately after recording the cancellation</li> <li>Cleanup of job resources happens asynchronously in the background</li> </ul> <h2>When to Cancel</h2> <p>Cancel a job when:</p> <ul> <li>The job is taking longer than expected</li> <li>The job was created with incorrect parameters</li> <li>You no longer need the results</li> </ul> <h2>Idempotency</h2> <p>You can safely retry cancellation requests. Calling CancelEnrichmentJob multiple times for the same job returns the current status without error as long as the job is not in a terminal state other than CANCELLED.</p>

        Args:
            workspace_name: <p>The name of the IoT SiteWise workspace containing the enrichment job to cancel.</p>
            job_id: <p>The unique identifier of the enrichment job to cancel. This is the jobId returned by CreateEnrichmentJob.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.cancel_enrichment_job_request.CancelEnrichmentJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.cancel_enrichment_job_response.CancelEnrichmentJobResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.cancel_enrichment_job

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.cancel_enrichment_job.async_cancel_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.cancel_enrichment_job_request.CancelEnrichmentJobRequest = {
            "workspace_name": workspace_name,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_pipeline_execution(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        pipeline_execution_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        reason: Optional[
            "capo_iotsitewise.types.cancel_pipeline_execution_request_reason_string.CancelPipelineExecutionRequestReasonString"
        ] = None,
    ) -> "capo_iotsitewise.types.cancel_pipeline_execution_response.CancelPipelineExecutionResponse":
        """<p>Cancels a pipeline execution in the specified workspace. If the execution is not in a terminal state (such as NOT_STARTED or RUNNING), it transitions to CANCELLING and asynchronously to CANCELLED. This operation is idempotent: calling it on an execution that is already CANCELLING or CANCELLED returns success with the current state. Calling it on a terminal execution (SUCCEEDED or FAILED) returns a conflict error. You can optionally provide a reason; it is returned in the stateDetails field when you describe the execution.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            pipeline_name: <p>The name of the pipeline.</p>
            pipeline_execution_id: <p>The unique identifier of the pipeline execution.</p>
            reason: <p>A message describing why the pipeline execution is being cancelled.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.cancel_pipeline_execution_request.CancelPipelineExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.cancel_pipeline_execution_response.CancelPipelineExecutionResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.cancel_pipeline_execution

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.cancel_pipeline_execution.async_cancel_pipeline_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.cancel_pipeline_execution_request.CancelPipelineExecutionRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
            "pipeline_execution_id": pipeline_execution_id,
        }
        if reason is not None:
            input_["reason"] = reason

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_query(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        query_id: "capo_iotsitewise.types.query_id.QueryId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.cancel_query_response.CancelQueryResponse":
        """<p>Cancels a running query.</p>

        Args:
            workspace_name: <p>The name of the workspace associated with the query.</p>
            query_id: <p>The unique identifier for the query execution to cancel.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.cancel_query_request.CancelQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.cancel_query_response.CancelQueryResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.cancel_query

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.cancel_query.async_cancel_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.cancel_query_request.CancelQueryRequest = {
            "workspace_name": workspace_name,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_access_policy(
        self,
        access_policy_identity: "capo_iotsitewise.types.identity.Identity",
        access_policy_resource: "capo_iotsitewise.types.resource.Resource",
        access_policy_permission: "capo_iotsitewise.types.permission.Permission",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_access_policy_response.CreateAccessPolicyResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Creates an access policy that grants the specified identity (IAM Identity Center user, IAM Identity Center group, or IAM user) access to the specified IoT SiteWise Monitor portal or project resource.</p> <note> <p>Support for access policies that use an SSO Group as the identity is not supported at this time.</p> </note>

        Args:
            access_policy_identity: <p>The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.</p>
            access_policy_resource: <p>The IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.</p>
            access_policy_permission: <p>The permission level for this access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the access policy. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_access_policy_request.CreateAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_access_policy_response.CreateAccessPolicyResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_access_policy

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_access_policy.async_create_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_access_policy_request.CreateAccessPolicyRequest = {
            "access_policy_identity": access_policy_identity,
            "access_policy_resource": access_policy_resource,
            "access_policy_permission": access_policy_permission,
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

    async def create_application(
        self,
        idc_instance_arn: "capo_iotsitewise.types.arn.ARN",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        name: "capo_iotsitewise.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        description: Optional["capo_iotsitewise.types.description.Description"] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_application_response.CreateApplicationResponse":
        """<p>Creates a new application for the workspace and IdC application provided</p>

        Args:
            client_token: <p>Unique client token for idempotent request handling</p>
            idc_instance_arn: <p>Identity Center Instance ARN to create the application in</p>
            workspace_name: <p>Name of the workspace to associate with the underlying Application</p>
            name: <p>Name of the application</p>
            description: <p>Description of the application</p>
            tags: <p>A list of key-value pairs that contain metadata for the application.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_application_request.CreateApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_application_response.CreateApplicationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_application

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_application.async_create_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_application_request.CreateApplicationRequest = {
            "idc_instance_arn": idc_instance_arn,
            "workspace_name": workspace_name,
            "name": name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
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

    async def create_asset(
        self,
        asset_name: "capo_iotsitewise.types.name.Name",
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        asset_external_id: Optional[
            "capo_iotsitewise.types.external_id.ExternalId"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
        asset_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
    ) -> "capo_iotsitewise.types.create_asset_response.CreateAssetResponse":
        """<p>Creates an asset from an existing asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-assets.html">Creating assets</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_name: <p>A friendly name for the asset.</p>
            asset_model_id: <p>The ID of the asset model from which to create the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_id: <p>The ID to assign to the asset, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            asset_external_id: <p>An external ID to assign to the asset. The external ID must be unique within your Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the asset. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_description: <p>A description for the asset.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_asset_request.CreateAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_asset_response.CreateAssetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_asset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_asset.async_create_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_asset_request.CreateAssetRequest = {
            "asset_name": asset_name,
            "asset_model_id": asset_model_id,
        }
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if asset_external_id is not None:
            input_["asset_external_id"] = asset_external_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if tags is not None:
            input_["tags"] = tags
        if asset_description is not None:
            input_["asset_description"] = asset_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_asset_model(
        self,
        asset_model_name: "capo_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_type: Optional[
            "capo_iotsitewise.types.asset_model_type.AssetModelType"
        ] = None,
        asset_model_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        asset_model_external_id: Optional[
            "capo_iotsitewise.types.external_id.ExternalId"
        ] = None,
        asset_model_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        asset_model_properties: Optional[
            "capo_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
        ] = None,
        asset_model_hierarchies: Optional[
            "capo_iotsitewise.types.asset_model_hierarchy_definitions.AssetModelHierarchyDefinitions"
        ] = None,
        asset_model_composite_models: Optional[
            "capo_iotsitewise.types.asset_model_composite_model_definitions.AssetModelCompositeModelDefinitions"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_asset_model_response.CreateAssetModelResponse":
        """<p>Creates an asset model from specified property and hierarchy definitions. You create assets from asset models. With asset models, you can easily create assets of the same type that have standardized definitions. Each asset created from a model inherits the asset model's property and hierarchy definitions. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/define-models.html">Defining asset models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can create three types of asset models, <code>ASSET_MODEL</code>, <code>COMPONENT_MODEL</code>, or an <code>INTERFACE</code>.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> <li> <p> <b>INTERFACE</b> – An interface is a type of model that defines a standard structure that can be applied to different asset models.</p> </li> </ul>

        Args:
            asset_model_name: <p>A unique name for the asset model.</p>
            asset_model_type: <p>The type of asset model.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – (default) An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> </ul>
            asset_model_id: <p>The ID to assign to the asset model, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            asset_model_external_id: <p>An external ID to assign to the asset model. The external ID must be unique within your Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_description: <p>A description for the asset model.</p>
            asset_model_properties: <p>The property definitions of the asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html">Asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_hierarchies: <p>The hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 10 hierarchies per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_composite_models: <p>The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.</p> <note> <p>When creating custom composite models, you need to use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html">CreateAssetModelCompositeModel</a>. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html">Creating custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_asset_model_request.CreateAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_asset_model_response.CreateAssetModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_asset_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_asset_model.async_create_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_asset_model_request.CreateAssetModelRequest = {
            "asset_model_name": asset_model_name
        }
        if asset_model_type is not None:
            input_["asset_model_type"] = asset_model_type
        if asset_model_id is not None:
            input_["asset_model_id"] = asset_model_id
        if asset_model_external_id is not None:
            input_["asset_model_external_id"] = asset_model_external_id
        if asset_model_description is not None:
            input_["asset_model_description"] = asset_model_description
        if asset_model_properties is not None:
            input_["asset_model_properties"] = asset_model_properties
        if asset_model_hierarchies is not None:
            input_["asset_model_hierarchies"] = asset_model_hierarchies
        if asset_model_composite_models is not None:
            input_["asset_model_composite_models"] = asset_model_composite_models
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

    async def create_asset_model_composite_model(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_name: "capo_iotsitewise.types.name.Name",
        asset_model_composite_model_type: "capo_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_composite_model_external_id: Optional[
            "capo_iotsitewise.types.external_id.ExternalId"
        ] = None,
        parent_asset_model_composite_model_id: Optional[
            "capo_iotsitewise.types.custom_id.CustomID"
        ] = None,
        asset_model_composite_model_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        asset_model_composite_model_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        composed_asset_model_id: Optional[
            "capo_iotsitewise.types.custom_id.CustomID"
        ] = None,
        asset_model_composite_model_properties: Optional[
            "capo_iotsitewise.types.asset_model_property_definitions.AssetModelPropertyDefinitions"
        ] = None,
        if_match: Optional["capo_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional["capo_iotsitewise.types.select_all.SelectAll"] = None,
        match_for_version_type: Optional[
            "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "capo_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse":
        """<p>Creates a custom composite model from specified property and hierarchy definitions. There are two types of custom composite models, <code>inline</code> and <code>component-model-based</code>. </p> <p>Use component-model-based custom composite models to define standard, reusable components. A component-model-based custom composite model consists of a name, a description, and the ID of the component model it references. A component-model-based custom composite model has no properties of its own; its referenced component model provides its associated properties to any created assets. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html">Custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>Use inline custom composite models to organize the properties of an asset model. The properties of inline custom composite models are local to the asset model where they are included and can't be used to create multiple assets.</p> <p>To create a component-model-based model, specify the <code>composedAssetModelId</code> of an existing asset model with <code>assetModelType</code> of <code>COMPONENT_MODEL</code>.</p> <p>To create an inline model, specify the <code>assetModelCompositeModelProperties</code> and don't include an <code>composedAssetModelId</code>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model this composite model is a part of.</p>
            asset_model_composite_model_external_id: <p>An external ID to assign to the composite model.</p> <p>If the composite model is a derived composite model, or one nested inside a component model, you can only set the external ID using <code>UpdateAssetModelCompositeModel</code> and specifying the derived ID of the model or property from the created model it's a part of.</p>
            parent_asset_model_composite_model_id: <p>The ID of the parent composite model in this asset model relationship.</p>
            asset_model_composite_model_id: <p>The ID of the composite model. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            asset_model_composite_model_description: <p>A description for the composite model.</p>
            asset_model_composite_model_name: <p>A unique name for the composite model.</p>
            asset_model_composite_model_type: <p>The composite model type. Valid values are <code>AWS/ALARM</code>, <code>CUSTOM</code>, or <code> AWS/L4E_ANOMALY</code>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            composed_asset_model_id: <p>The ID of a component model which is reused to create this composite model.</p>
            asset_model_composite_model_properties: <p>The property definitions of the composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models"> Inline custom composite models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The create request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the create request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the create operation.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.precondition_failed_exception.PreconditionFailedException: <p>The precondition in one or more of the request-header fields evaluated to <code>FALSE</code>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_asset_model_composite_model_request.CreateAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_asset_model_composite_model_response.CreateAssetModelCompositeModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_asset_model_composite_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_asset_model_composite_model.async_create_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_asset_model_composite_model_request.CreateAssetModelCompositeModelRequest = {
            "asset_model_id": asset_model_id,
            "asset_model_composite_model_name": asset_model_composite_model_name,
            "asset_model_composite_model_type": asset_model_composite_model_type,
        }
        if asset_model_composite_model_external_id is not None:
            input_["asset_model_composite_model_external_id"] = (
                asset_model_composite_model_external_id
            )
        if parent_asset_model_composite_model_id is not None:
            input_["parent_asset_model_composite_model_id"] = (
                parent_asset_model_composite_model_id
            )
        if asset_model_composite_model_id is not None:
            input_["asset_model_composite_model_id"] = asset_model_composite_model_id
        if asset_model_composite_model_description is not None:
            input_["asset_model_composite_model_description"] = (
                asset_model_composite_model_description
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if composed_asset_model_id is not None:
            input_["composed_asset_model_id"] = composed_asset_model_id
        if asset_model_composite_model_properties is not None:
            input_["asset_model_composite_model_properties"] = (
                asset_model_composite_model_properties
            )
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_bulk_import_job(
        self,
        job_name: "capo_iotsitewise.types.bulk_import_job_name.BulkImportJobName",
        job_role_arn: "capo_iotsitewise.types.arn.ARN",
        files: "capo_iotsitewise.types.files.Files",
        error_report_location: "capo_iotsitewise.types.error_report_location.ErrorReportLocation",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        job_configuration: Optional[
            "capo_iotsitewise.types.job_configuration.JobConfiguration"
        ] = None,
        adaptive_ingestion: Optional[
            "capo_iotsitewise.types.adaptive_ingestion.AdaptiveIngestion"
        ] = None,
        delete_files_after_import: Optional[
            "capo_iotsitewise.types.delete_files_after_import.DeleteFilesAfterImport"
        ] = None,
        dataset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "capo_iotsitewise.types.create_bulk_import_job_response.CreateBulkImportJobResponse":
        """<p>Defines a job to ingest data to IoT SiteWise from Amazon S3. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/CreateBulkImportJob.html">Create a bulk import job (CLI)</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p> <important> <p>Before you create a bulk import job that ingests data into time series outside of a workspace, you must enable IoT SiteWise warm tier or IoT SiteWise cold tier. For more information about how to configure storage settings, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_PutStorageConfiguration.html">PutStorageConfiguration</a>. This requirement doesn't apply to bulk import jobs that ingest data into a session dataset in a workspace (jobs that specify a <code>workspaceName</code> and <code>datasetId</code>). Those jobs don't use IoT SiteWise warm or cold tier storage.</p> <p>Bulk import is designed to store historical data to IoT SiteWise.</p> <ul> <li> <p>Newly ingested data in the hot tier triggers notifications and computations.</p> </li> <li> <p>After data moves from the hot tier to the warm or cold tier based on retention settings, it does not trigger computations or notifications.</p> </li> <li> <p>Data older than 7 days does not trigger computations or notifications.</p> </li> </ul> </important>

        Args:
            job_name: <p>The unique name that helps identify the job request.</p>
            job_role_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the IAM role that allows IoT SiteWise to read Amazon S3 data.</p>
            files: <p>The files in the specified Amazon S3 bucket that contain your data. You can specify up to 100 files for each bulk import job. Each file supports the following size limits:</p> <ul> <li> <p>Parquet files – Up to 256 MiB.</p> </li> <li> <p>Other file formats – Up to 5 GiB.</p> </li> </ul>
            error_report_location: <p>The Amazon S3 destination where errors associated with the job creation request are saved.</p>
            job_configuration: <p>Contains the configuration information of a job, such as the file format used to save data in Amazon S3.</p>
            adaptive_ingestion: <p>If set to true, ingest new data into IoT SiteWise storage. Measurements with notifications, metrics and transforms are computed. If set to false, historical data is ingested into IoT SiteWise as is.</p>
            delete_files_after_import: <p>If set to true, your data files is deleted from S3, after ingestion into IoT SiteWise storage.</p>
            dataset_id: <p>The ID of the session dataset to ingest data into. Specify this field, together with <code>workspaceName</code>, to ingest data into a session dataset in a workspace.</p>
            workspace_name: <p>The name of the workspace that contains the session dataset. Specify this field together with <code>datasetId</code>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_bulk_import_job_request.CreateBulkImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_bulk_import_job_response.CreateBulkImportJobResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_bulk_import_job

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_bulk_import_job.async_create_bulk_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_bulk_import_job_request.CreateBulkImportJobRequest = {
            "job_name": job_name,
            "job_role_arn": job_role_arn,
            "files": files,
            "error_report_location": error_report_location,
        }
        if job_configuration is not None:
            input_["job_configuration"] = job_configuration
        if adaptive_ingestion is not None:
            input_["adaptive_ingestion"] = adaptive_ingestion
        if delete_files_after_import is not None:
            input_["delete_files_after_import"] = delete_files_after_import
        if dataset_id is not None:
            input_["dataset_id"] = dataset_id
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_computation_model(
        self,
        computation_model_name: "capo_iotsitewise.types.restricted_name.RestrictedName",
        computation_model_configuration: "capo_iotsitewise.types.computation_model_configuration.ComputationModelConfiguration",
        computation_model_data_binding: "capo_iotsitewise.types.computation_model_data_binding.ComputationModelDataBinding",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_description: Optional[
            "capo_iotsitewise.types.restricted_description.RestrictedDescription"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_computation_model_response.CreateComputationModelResponse":
        """<p>Create a computation model with a configuration and data binding.</p>

        Args:
            computation_model_name: <p>The name of the computation model.</p>
            computation_model_description: <p>The description of the computation model.</p>
            computation_model_configuration: <p>The configuration for the computation model.</p>
            computation_model_data_binding: <p>The data binding for the computation model. Key is a variable name defined in configuration. Value is a <code>ComputationModelDataBindingValue</code> referenced by the variable.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the asset. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_computation_model_request.CreateComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_computation_model_response.CreateComputationModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_computation_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_computation_model.async_create_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_computation_model_request.CreateComputationModelRequest = {
            "computation_model_name": computation_model_name,
            "computation_model_configuration": computation_model_configuration,
            "computation_model_data_binding": computation_model_data_binding,
        }
        if computation_model_description is not None:
            input_["computation_model_description"] = computation_model_description
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

    async def create_dashboard(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        dashboard_name: "capo_iotsitewise.types.name.Name",
        dashboard_definition: "capo_iotsitewise.types.dashboard_definition.DashboardDefinition",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dashboard_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_dashboard_response.CreateDashboardResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Creates a dashboard in an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project in which to create the dashboard.</p>
            dashboard_name: <p>A friendly name for the dashboard.</p>
            dashboard_description: <p>A description for the dashboard.</p>
            dashboard_definition: <p>The dashboard definition specified in a JSON literal.</p> <ul> <li> <p>IoT SiteWise Monitor (Classic) see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html">Create dashboards (CLI)</a> </p> </li> <li> <p>IoT SiteWise Monitor (AI-aware) see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html">Create dashboards (CLI)</a> </p> </li> </ul> <p>in the <i>IoT SiteWise User Guide</i> </p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the dashboard. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_dashboard_request.CreateDashboardRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_dashboard_response.CreateDashboardResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_dashboard

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_dashboard.async_create_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_dashboard_request.CreateDashboardRequest = {
            "project_id": project_id,
            "dashboard_name": dashboard_name,
            "dashboard_definition": dashboard_definition,
        }
        if dashboard_description is not None:
            input_["dashboard_description"] = dashboard_description
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

    async def create_dataset(
        self,
        dataset_name: "capo_iotsitewise.types.restricted_name.RestrictedName",
        dataset_source: "capo_iotsitewise.types.dataset_source.DatasetSource",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dataset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        dataset_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        dataset_type: Optional[
            "capo_iotsitewise.types.dataset_type_enum.DatasetTypeEnum"
        ] = None,
        dataset_config: Optional[
            "capo_iotsitewise.types.dataset_config.DatasetConfig"
        ] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
        metadata: Optional["capo_iotsitewise.types.metadata.Metadata"] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_dataset_response.CreateDatasetResponse":
        """<p>Creates a dataset. Session and curated datasets are created in a workspace. A session dataset contains data segments of time series data, and a curated dataset curates data segments selected from source session datasets. A dataset that connects to an external datasource is created outside of a workspace.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            dataset_name: <p>The name of the dataset.</p>
            dataset_description: <p>A description about the dataset, and its functionality.</p>
            dataset_type: <p>The type of dataset: a session dataset, a curated dataset, or a connection to an external datasource.</p>
            dataset_config: <p>The configuration for the dataset.</p>
            workspace_name: <p>The name of the workspace that contains the dataset. Required for session and curated datasets. Omit this field for datasets that connect to an external datasource.</p>
            metadata: <p>The metadata for the dataset, provided as key-value pairs.</p>
            dataset_source: <p>The data source for the dataset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the access policy. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_dataset_request.CreateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_dataset_response.CreateDatasetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_dataset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_dataset.async_create_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_dataset_request.CreateDatasetRequest = {
            "dataset_name": dataset_name,
            "dataset_source": dataset_source,
        }
        if dataset_id is not None:
            input_["dataset_id"] = dataset_id
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        if dataset_type is not None:
            input_["dataset_type"] = dataset_type
        if dataset_config is not None:
            input_["dataset_config"] = dataset_config
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
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

    async def create_dataset_export_job(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        destination_s3_uri: "capo_iotsitewise.types.s3_uri.S3Uri",
        input: "capo_iotsitewise.types.processing_input.ProcessingInput",
        error_report_location: "capo_iotsitewise.types.export_error_report_location.ExportErrorReportLocation",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.create_dataset_export_job_response.CreateDatasetExportJobResponse":
        """<p>Starts an asynchronous job that exports dataset and time-series data from a workspace to Amazon S3. The operation returns a jobId immediately; poll DescribeDatasetExportJob to track progress and ListDatasetExportJobs to enumerate a workspace's jobs.</p>

        Args:
            workspace_name: <p>The name of the workspace in which to create the dataset export job.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. The AWS SDKs and CLI populate this automatically.</p>
            destination_s3_uri: <p>The S3 URI where output clips will be written.</p>
            input: <p>The processing input source.</p>
            error_report_location: <p>The location where the error report will be written on failure.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_dataset_export_job_request.CreateDatasetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_dataset_export_job_response.CreateDatasetExportJobResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_dataset_export_job

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_dataset_export_job.async_create_dataset_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_dataset_export_job_request.CreateDatasetExportJobRequest = {
            "workspace_name": workspace_name,
            "destination_s3_uri": destination_s3_uri,
            "input": input,
            "error_report_location": error_report_location,
        }
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

    async def create_enrichment_job(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        job_configuration: "capo_iotsitewise.types.enrichment_job_configuration.EnrichmentJobConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.create_enrichment_job_response.CreateEnrichmentJobResponse":
        """<p>Creates an asynchronous enrichment job to analyze time-series sensor data. The operation returns immediately with job details while processing continues in the background.</p> <h2>Idempotency</h2> <p>Include a clientToken to make the operation idempotent. If you submit the same request with the same token within the idempotency window, you receive the original job details without creating a duplicate.</p> <h2>Prerequisites</h2> <p>Before creating a job, ensure:</p> <ul> <li>The workspace is in ACTIVE state (not being deleted)</li> <li>You have IAM permissions for the workspace, dataset, and time-series resources</li> <li>You have KMS Decrypt permission on the workspace's customer-managed encryption key</li> <li>No duplicate job (same workspace, dataset, property, and job type) is currently running</li> </ul> <h2>Workflow</h2> <ol> <li>Submit the job with configuration specifying which video data to analyze and the time range</li> <li>Capture the jobId from the response</li> <li>Use DescribeEnrichmentJob to monitor progress and check job status</li> <li>When status reaches a terminal state (COMPLETED, FAILED, TIMED_OUT, CANCELLED), check results</li> <li>For COMPLETED jobs, query IoT SiteWise for semantic search on video events</li> </ol> <h2>Error Handling</h2> <ul> <li>ConflictingOperationException: A duplicate job is already running for the same configuration</li> <li>InvalidRequestException: Invalid parameters (e.g., both timeSeriesId and propertyAlias specified)</li> <li>AccessDeniedException: Insufficient IAM or KMS permissions</li> <li>LimitExceededException: Too many concurrent jobs or requests</li> </ul>

        Args:
            workspace_name: <p>The name of the IoT SiteWise workspace containing the video data to analyze.</p>
            job_configuration: <p>Configuration defining the type of enrichment analysis to perform and which video data to analyze. Currently supports eventDetection for generating embeddings from video data for semantic search.</p>
            client_token: <p>Optional unique token that makes the operation idempotent. If you submit the same request with the same token within the idempotency window, the service returns the original job without creating a duplicate. Use a UUID or timestamp-based token for each unique request.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_enrichment_job_request.CreateEnrichmentJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_enrichment_job_response.CreateEnrichmentJobResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_enrichment_job

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_enrichment_job.async_create_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_enrichment_job_request.CreateEnrichmentJobRequest = {
            "workspace_name": workspace_name,
            "job_configuration": job_configuration,
        }
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

    async def create_gateway(
        self,
        gateway_name: "capo_iotsitewise.types.gateway_name.GatewayName",
        gateway_platform: "capo_iotsitewise.types.gateway_platform.GatewayPlatform",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        gateway_version: Optional[
            "capo_iotsitewise.types.gateway_version.GatewayVersion"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_gateway_response.CreateGatewayResponse":
        """<p>Creates a gateway, which is a virtual or edge device that delivers industrial data streams from local servers to IoT SiteWise. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateway-connector.html">Ingesting data using a gateway</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            gateway_name: <p>A unique name for the gateway.</p>
            gateway_platform: <p>The gateway's platform. You can only specify one platform in a gateway.</p>
            gateway_version: <p>The version of the gateway to create. Specify <code>3</code> to create an MQTT-enabled, V3 gateway and <code>2</code> to create a Classic streams, V2 gateway. If not specified, the default is <code>2</code> (Classic streams, V2 gateway).</p> <note> <p>When creating a V3 gateway (<code>gatewayVersion=3</code>) with the <code>GreengrassV2</code> platform, you must also specify the <code>coreDeviceOperatingSystem</code> parameter.</p> </note> <p> We recommend creating an MQTT-enabled gateway for self-hosted gateways and Siemens Industrial Edge gateways. For more information on gateway versions, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html">Use Amazon Web Services IoT SiteWise Edge Edge gateways</a>.</p>
            tags: <p>A list of key-value pairs that contain metadata for the gateway. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_gateway_request.CreateGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_gateway_response.CreateGatewayResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_gateway

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_gateway.async_create_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_gateway_request.CreateGatewayRequest = {
            "gateway_name": gateway_name,
            "gateway_platform": gateway_platform,
        }
        if gateway_version is not None:
            input_["gateway_version"] = gateway_version
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_pipeline(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        computations: "capo_iotsitewise.types.compute_node_list.ComputeNodeList",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        description: Optional["capo_iotsitewise.types.description.Description"] = None,
        environment_variables: Optional[
            "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.create_pipeline_response.CreatePipelineResponse":
        """<p>Creates a new pipeline in the specified workspace. A pipeline defines a directed acyclic graph (DAG) of compute nodes, where each node references a task and can declare dependencies on other nodes. Cyclic dependencies are not allowed. Nodes without dependencies run in parallel, while nodes with dependencies wait for all upstream nodes to complete successfully before starting.</p> <p>You can set environment variables at the pipeline level that are shared across all compute nodes, and override them at the individual compute node level.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            pipeline_name: <p>The name of the pipeline to create. Must be unique within the workspace.</p>
            description: <p>A description of the pipeline.</p>
            environment_variables: <p>Environment variables shared across all compute nodes in the pipeline. Individual compute nodes can override these values with their own environment variables.</p>
            computations: <p>The list of compute nodes that form the pipeline DAG. Each compute node references a task and can declare dependencies on other nodes.</p>
            tags: <p>A list of key-value pairs that contain metadata for the pipeline. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your AWS IoT SiteWise resources</a> in the AWS IoT SiteWise User Guide.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_pipeline_request.CreatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_pipeline_response.CreatePipelineResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_pipeline

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_pipeline.async_create_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_pipeline_request.CreatePipelineRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
            "computations": computations,
        }
        if description is not None:
            input_["description"] = description
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if tags is not None:
            input_["tags"] = tags
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

    async def create_portal(
        self,
        portal_name: "capo_iotsitewise.types.name.Name",
        portal_contact_email: "capo_iotsitewise.types.email.Email",
        role_arn: "capo_iotsitewise.types.iam_arn.IamArn",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        portal_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        portal_logo_image_file: Optional[
            "capo_iotsitewise.types.image_file.ImageFile"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
        portal_auth_mode: Optional["capo_iotsitewise.types.auth_mode.AuthMode"] = None,
        notification_sender_email: Optional[
            "capo_iotsitewise.types.email.Email"
        ] = None,
        alarms: Optional["capo_iotsitewise.types.alarms.Alarms"] = None,
        portal_type: Optional["capo_iotsitewise.types.portal_type.PortalType"] = None,
        portal_type_configuration: Optional[
            "capo_iotsitewise.types.portal_type_configuration.PortalTypeConfiguration"
        ] = None,
    ) -> "capo_iotsitewise.types.create_portal_response.CreatePortalResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Creates a portal, which can contain projects and dashboards. IoT SiteWise Monitor uses IAM Identity Center or IAM to authenticate portal users and manage user permissions.</p> <note> <p>Before you can sign in to a new portal, you must add at least one identity to that portal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/administer-portals.html#portal-change-admins">Adding or removing portal administrators</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>

        Args:
            portal_name: <p>A friendly name for the portal.</p>
            portal_description: <p>A description for the portal.</p>
            portal_contact_email: <p>The Amazon Web Services administrator's contact email address.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            portal_logo_image_file: <p>A logo image to display in the portal. Upload a square, high-resolution image. The image is displayed on a dark background.</p>
            role_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of a service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>
            tags: <p>A list of key-value pairs that contain metadata for the portal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
            portal_auth_mode: <p>The service to use to authenticate users to the portal. Choose from the following options:</p> <ul> <li> <p> <code>SSO</code> – The portal uses IAM Identity Center to authenticate users and manage user permissions. Before you can create a portal that uses IAM Identity Center, you must enable IAM Identity Center. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-get-started.html#mon-gs-sso">Enabling IAM Identity Center</a> in the <i>IoT SiteWise User Guide</i>. This option is only available in Amazon Web Services Regions other than the China Regions.</p> </li> <li> <p> <code>IAM</code> – The portal uses Identity and Access Management to authenticate users and manage user permissions.</p> </li> </ul> <p>You can't change this value after you create a portal.</p> <p>Default: <code>SSO</code> </p>
            notification_sender_email: <p>The email address that sends alarm notifications.</p> <important> <p>If you use the <a href="https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html">IoT Events managed Lambda function</a> to manage your emails, you must <a href="https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html">verify the sender email address in Amazon SES</a>.</p> </important>
            alarms: <p>Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html">Monitoring with alarms</a> in the <i>IoT SiteWise Application Guide</i>.</p>
            portal_type: <p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>
            portal_type_configuration: <p>The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_portal_request.CreatePortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_portal_response.CreatePortalResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_portal

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_portal.async_create_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_portal_request.CreatePortalRequest = {
            "portal_name": portal_name,
            "portal_contact_email": portal_contact_email,
            "role_arn": role_arn,
        }
        if portal_description is not None:
            input_["portal_description"] = portal_description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if portal_logo_image_file is not None:
            input_["portal_logo_image_file"] = portal_logo_image_file
        if tags is not None:
            input_["tags"] = tags
        if portal_auth_mode is not None:
            input_["portal_auth_mode"] = portal_auth_mode
        if notification_sender_email is not None:
            input_["notification_sender_email"] = notification_sender_email
        if alarms is not None:
            input_["alarms"] = alarms
        if portal_type is not None:
            input_["portal_type"] = portal_type
        if portal_type_configuration is not None:
            input_["portal_type_configuration"] = portal_type_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_project(
        self,
        portal_id: "capo_iotsitewise.types.id.ID",
        project_name: "capo_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        project_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
    ) -> "capo_iotsitewise.types.create_project_response.CreateProjectResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Creates a project in the specified portal.</p> <note> <p>Make sure that the project name and description don't contain confidential information.</p> </note>

        Args:
            portal_id: <p>The ID of the portal in which to create the project.</p>
            project_name: <p>A friendly name for the project.</p>
            project_description: <p>A description for the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            tags: <p>A list of key-value pairs that contain metadata for the project. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_project_request.CreateProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_project_response.CreateProjectResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_project

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_project.async_create_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_project_request.CreateProjectRequest = {
            "portal_id": portal_id,
            "project_name": project_name,
        }
        if project_description is not None:
            input_["project_description"] = project_description
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

    async def create_task(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        task_name: "capo_iotsitewise.types.resource_name.ResourceName",
        task_configuration: "capo_iotsitewise.types.task_configuration.TaskConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        description: Optional["capo_iotsitewise.types.description.Description"] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.create_task_response.CreateTaskResponse":
        """<p>Creates a new task in the specified workspace. A task defines a reusable containerized compute workload that can be referenced by one or more pipeline compute nodes.</p> <p>Specify a <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html"><code>containerTaskConfiguration</code></a> for custom container workloads with configurable ECR image, processing type, processing unit, and environment variables.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            task_name: <p>The name of the task to create. Must be unique within the workspace.</p>
            description: <p>A description of the task.</p>
            task_configuration: <p>The task execution configuration. Specify a <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ContainerTaskConfiguration.html">containerTaskConfiguration</a> for custom container workloads.</p>
            tags: <p>A list of key-value pairs that contain metadata for the task. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your AWS IoT SiteWise resources</a> in the AWS IoT SiteWise User Guide.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_task_request.CreateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_task_response.CreateTaskResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_task

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_task.async_create_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_task_request.CreateTaskRequest = {
            "workspace_name": workspace_name,
            "task_name": task_name,
            "task_configuration": task_configuration,
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
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

    async def create_workspace(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        encryption_configuration: "capo_iotsitewise.types.workspace_encryption_configuration.WorkspaceEncryptionConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        tags: Optional["capo_iotsitewise.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.create_workspace_response.CreateWorkspaceResponse":
        """<p>Creates a workspace in IoT SiteWise. A workspace isolates its resources, such as datasets, time series, pipelines, and tasks, and their data from other workspaces, and has its own quotas and throttling limits. You must specify an encryption configuration when you create a workspace. The operation returns immediately with the workspace in the <code>CREATING</code> state. Provisioning completes asynchronously, after which the workspace state is <code>ACTIVE</code>, or <code>FAILED</code> if provisioning doesn't complete.</p>

        Args:
            workspace_name: <p>The name of the workspace to create.</p>
            workspace_description: <p>A description for the workspace.</p>
            encryption_configuration: <p>The encryption configuration for the workspace.</p>
            tags: <p>A list of key-value pairs that contain metadata for the workspace. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.create_workspace_request.CreateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.create_workspace_response.CreateWorkspaceResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.create_workspace

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.create_workspace.async_create_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.create_workspace_request.CreateWorkspaceRequest = {
            "workspace_name": workspace_name,
            "encryption_configuration": encryption_configuration,
        }
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        if tags is not None:
            input_["tags"] = tags
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

    async def delete_access_policy(
        self,
        access_policy_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_access_policy_response.DeleteAccessPolicyResponse":
        """<p>Deletes an access policy that grants the specified identity access to the specified IoT SiteWise Monitor resource. You can use this operation to revoke access to an IoT SiteWise Monitor resource.</p>

        Args:
            access_policy_id: <p>The ID of the access policy to be deleted.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_access_policy_request.DeleteAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_access_policy_response.DeleteAccessPolicyResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_access_policy

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_access_policy.async_delete_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_access_policy_request.DeleteAccessPolicyRequest = {
            "access_policy_id": access_policy_id
        }
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

    async def delete_application(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        id: "capo_iotsitewise.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.delete_application_response.DeleteApplicationResponse":
        """<p>Deletes an application by ID</p>

        Args:
            workspace_name: <p>Name of the workspace to associate with the underlying Application</p>
            id: <p>ID of the Application to delete</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_application_request.DeleteApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_application

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_application.async_delete_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_application_request.DeleteApplicationRequest = {
            "workspace_name": workspace_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_asset_response.DeleteAssetResponse":
        """<p>Deletes an asset. This action can't be undone. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html">Deleting assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p> <note> <p>You can't delete an asset that's associated to another asset. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DisassociateAssets.html">DisassociateAssets</a>.</p> </note>

        Args:
            asset_id: <p>The ID of the asset to delete. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_asset_request.DeleteAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_asset_response.DeleteAssetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset.async_delete_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_asset_request.DeleteAssetRequest = {
            "asset_id": asset_id
        }
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

    async def delete_asset_model(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        if_match: Optional["capo_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional["capo_iotsitewise.types.select_all.SelectAll"] = None,
        match_for_version_type: Optional[
            "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_asset_model_response.DeleteAssetModelResponse":
        """<p>Deletes an asset model. This action can't be undone. You must delete all assets created from an asset model before you can delete the model. Also, you can't delete an asset model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html">Deleting assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model to delete. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The delete request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the delete request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the delete operation.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.precondition_failed_exception.PreconditionFailedException: <p>The precondition in one or more of the request-header fields evaluated to <code>FALSE</code>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_asset_model_request.DeleteAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_asset_model_response.DeleteAssetModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model.async_delete_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_asset_model_request.DeleteAssetModelRequest = {
            "asset_model_id": asset_model_id
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset_model_composite_model(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        if_match: Optional["capo_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional["capo_iotsitewise.types.select_all.SelectAll"] = None,
        match_for_version_type: Optional[
            "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_asset_model_composite_model_response.DeleteAssetModelCompositeModelResponse":
        """<p>Deletes a composite model. This action can't be undone. You must delete all assets created from a composite model before you can delete the model. Also, you can't delete a composite model if a parent asset model exists that contains a property formula expression that depends on the asset model that you want to delete. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/delete-assets-and-models.html">Deleting assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model, in UUID format.</p>
            asset_model_composite_model_id: <p>The ID of a composite model on this asset model.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The delete request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the delete request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the delete operation.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.precondition_failed_exception.PreconditionFailedException: <p>The precondition in one or more of the request-header fields evaluated to <code>FALSE</code>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_asset_model_composite_model_request.DeleteAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_asset_model_composite_model_response.DeleteAssetModelCompositeModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_composite_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_composite_model.async_delete_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_asset_model_composite_model_request.DeleteAssetModelCompositeModelRequest = {
            "asset_model_id": asset_model_id,
            "asset_model_composite_model_id": asset_model_composite_model_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_asset_model_interface_relationship(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_asset_model_interface_relationship_response.DeleteAssetModelInterfaceRelationshipResponse":
        """<p>Deletes an interface relationship between an asset model and an interface asset model.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_asset_model_interface_relationship_request.DeleteAssetModelInterfaceRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_asset_model_interface_relationship_response.DeleteAssetModelInterfaceRelationshipResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_interface_relationship

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_asset_model_interface_relationship.async_delete_asset_model_interface_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_asset_model_interface_relationship_request.DeleteAssetModelInterfaceRelationshipRequest = {
            "asset_model_id": asset_model_id,
            "interface_asset_model_id": interface_asset_model_id,
        }
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

    async def delete_computation_model(
        self,
        computation_model_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_computation_model_response.DeleteComputationModelResponse":
        """<p>Deletes a computation model. This action can't be undone.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_computation_model_request.DeleteComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_computation_model_response.DeleteComputationModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_computation_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_computation_model.async_delete_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_computation_model_request.DeleteComputationModelRequest = {
            "computation_model_id": computation_model_id
        }
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

    async def delete_dashboard(
        self,
        dashboard_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_dashboard_response.DeleteDashboardResponse":
        """<p>Deletes a dashboard from IoT SiteWise Monitor.</p>

        Args:
            dashboard_id: <p>The ID of the dashboard to delete.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_dashboard_request.DeleteDashboardRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_dashboard_response.DeleteDashboardResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_dashboard

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_dashboard.async_delete_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_dashboard_request.DeleteDashboardRequest = {
            "dashboard_id": dashboard_id
        }
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

    async def delete_dataset(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_dataset_response.DeleteDatasetResponse":
        """<p>Deletes a dataset. This can't be undone. Deleting a session dataset also deletes the underlying time series data in the session. You can't delete a session dataset while a curated dataset references its data segments. First delete the curated dataset or disassociate the data segments. Deleting a curated dataset doesn't delete the underlying data in the source session datasets.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_dataset_request.DeleteDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_dataset_response.DeleteDatasetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_dataset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_dataset.async_delete_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_dataset_request.DeleteDatasetRequest = {
            "dataset_id": dataset_id
        }
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
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

    async def delete_gateway(
        self,
        gateway_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> None:
        """<p>Deletes a gateway from IoT SiteWise. When you delete a gateway, some of the gateway's files remain in your gateway's file system.</p>

        Args:
            gateway_id: <p>The ID of the gateway to delete.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_gateway_request.DeleteGatewayRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_gateway

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_gateway.async_delete_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_gateway_request.DeleteGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_pipeline(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.delete_pipeline_response.DeletePipelineResponse":
        """<p>Deletes a pipeline from the specified workspace. A pipeline cannot be deleted if it has any active executions. Wait for all executions to complete before attempting to delete the pipeline, or use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CancelPipelineExecution.html">CancelPipelineExecution</a> to stop a running execution.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            pipeline_name: <p>The name of the pipeline to delete.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_pipeline_request.DeletePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_pipeline_response.DeletePipelineResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_pipeline

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_pipeline.async_delete_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_pipeline_request.DeletePipelineRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_portal(
        self,
        portal_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_portal_response.DeletePortalResponse":
        """<p>Deletes a portal from IoT SiteWise Monitor.</p>

        Args:
            portal_id: <p>The ID of the portal to delete.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_portal_request.DeletePortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_portal_response.DeletePortalResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_portal

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_portal.async_delete_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_portal_request.DeletePortalRequest = {
            "portal_id": portal_id
        }
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

    async def delete_project(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_project_response.DeleteProjectResponse":
        """<p>Deletes a project from IoT SiteWise Monitor.</p>

        Args:
            project_id: <p>The ID of the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_project_request.DeleteProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_project_response.DeleteProjectResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_project

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_project.async_delete_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_project_request.DeleteProjectRequest = {
            "project_id": project_id
        }
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

    async def delete_task(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        task_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.delete_task_response.DeleteTaskResponse":
        """<p>Deletes a task from the specified workspace. A task cannot be deleted if it is currently referenced by any existing pipeline. Remove the task from all pipelines before attempting to delete it.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            task_name: <p>The name of the task to delete.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_task_request.DeleteTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_task_response.DeleteTaskResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_task

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_task.async_delete_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_task_request.DeleteTaskRequest = {
            "workspace_name": workspace_name,
            "task_name": task_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        alias: Optional["capo_iotsitewise.types.property_alias.PropertyAlias"] = None,
        asset_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        property_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> None:
        """<p>Deletes a time series (data stream). If you delete a time series that's associated with an asset property, the asset property still exists, but the time series will no longer be associated with this asset property. You can't delete a time series until all of its data segments have been deleted from session datasets.</p> <p>To identify a time series, do one of the following:</p> <ul> <li> <p>If the time series isn't associated with an asset property, specify the <code>alias</code> of the time series.</p> </li> <li> <p>If the time series is associated with an asset property, specify one of the following: </p> <ul> <li> <p>The <code>alias</code> of the time series.</p> </li> <li> <p>The <code>assetId</code> and <code>propertyId</code> that identifies the asset property.</p> </li> </ul> </li> </ul>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_time_series_request.DeleteTimeSeriesRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_time_series

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_time_series.async_delete_time_series(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_time_series_request.DeleteTimeSeriesRequest = {}
        if alias is not None:
            input_["alias"] = alias
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_workspace(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.delete_workspace_response.DeleteWorkspaceResponse":
        """<p>Deletes a workspace. Before you delete a workspace, you must delete all resources contained in or associated with the workspace, such as datasets, time series, pipelines, and tasks.</p>

        Args:
            workspace_name: <p>The name of the workspace to delete.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.delete_workspace_request.DeleteWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.delete_workspace_response.DeleteWorkspaceResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.delete_workspace

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.delete_workspace.async_delete_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.delete_workspace_request.DeleteWorkspaceRequest = {
            "workspace_name": workspace_name
        }
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

    async def describe_access_policy(
        self,
        access_policy_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_access_policy_response.DescribeAccessPolicyResponse":
        """<p>Describes an access policy, which specifies an identity's access to an IoT SiteWise Monitor portal or project.</p>

        Args:
            access_policy_id: <p>The ID of the access policy.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_access_policy_request.DescribeAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_access_policy_response.DescribeAccessPolicyResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_access_policy

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_access_policy.async_describe_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_access_policy_request.DescribeAccessPolicyRequest = {
            "access_policy_id": access_policy_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_action(
        self,
        action_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_action_response.DescribeActionResponse":
        """<p>Retrieves information about an action.</p>

        Args:
            action_id: <p>The ID of the action.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_action_request.DescribeActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_action_response.DescribeActionResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_action

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_action.async_describe_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_action_request.DescribeActionRequest = {
            "action_id": action_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_application(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        id: "capo_iotsitewise.types.application_id.ApplicationId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_application_response.DescribeApplicationResponse":
        """<p>Retrieves Application details based on the ID</p>

        Args:
            workspace_name: <p>Name of the workspace to associate with the underlying Application</p>
            id: <p>ID of the Application</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_application_request.DescribeApplicationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_application_response.DescribeApplicationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_application

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_application.async_describe_application(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_application_request.DescribeApplicationRequest = {
            "workspace_name": workspace_name,
            "id": id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_asset(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "capo_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_asset_response.DescribeAssetResponse":
        """<p>Retrieves information about an asset.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            exclude_properties: <p> Whether or not to exclude asset properties from the response. </p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_asset_request.DescribeAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_asset_response.DescribeAssetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset.async_describe_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_asset_request.DescribeAssetRequest = {
            "asset_id": asset_id
        }
        if exclude_properties is not None:
            input_["exclude_properties"] = exclude_properties

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_asset_not_exists(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "capo_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
    ) -> ServiceError:
        """Wait for asset_not_exists.

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            exclude_properties: <p> Whether or not to exclude asset properties from the response. </p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_iotsitewise.types.describe_asset_response.DescribeAssetResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_asset(  # noqa: F841
                    asset_id,
                    config_overrides=config_overrides,
                    exclude_properties=exclude_properties,
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("asset_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def describe_asset_composite_model(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_composite_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_asset_composite_model_response.DescribeAssetCompositeModelResponse":
        """<p>Retrieves information about an asset composite model (also known as an asset component). An <code>AssetCompositeModel</code> is an instance of an <code>AssetModelCompositeModel</code>. If you want to see information about the model this is based on, call <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelCompositeModel.html">DescribeAssetModelCompositeModel</a>.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_composite_model_id: <p>The ID of a composite model on this asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_asset_composite_model_request.DescribeAssetCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_asset_composite_model_response.DescribeAssetCompositeModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_composite_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_composite_model.async_describe_asset_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_asset_composite_model_request.DescribeAssetCompositeModelRequest = {
            "asset_id": asset_id,
            "asset_composite_model_id": asset_composite_model_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_asset_model(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "capo_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_asset_model_response.DescribeAssetModelResponse":
        """<p>Retrieves information about an asset model. This includes details about the asset model's properties, hierarchies, composite models, and any interface relationships if the asset model implements interfaces.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            exclude_properties: <p> Whether or not to exclude asset model properties from the response. </p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_asset_model_request.DescribeAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_asset_model_response.DescribeAssetModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model.async_describe_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_asset_model_request.DescribeAssetModelRequest = {
            "asset_model_id": asset_model_id
        }
        if exclude_properties is not None:
            input_["exclude_properties"] = exclude_properties
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_asset_model_not_exists(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        exclude_properties: Optional[
            "capo_iotsitewise.types.exclude_properties.ExcludeProperties"
        ] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> ServiceError:
        """Wait for asset_model_not_exists.

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            exclude_properties: <p> Whether or not to exclude asset model properties from the response. </p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_iotsitewise.types.describe_asset_model_response.DescribeAssetModelResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_asset_model(  # noqa: F841
                    asset_model_id,
                    config_overrides=config_overrides,
                    exclude_properties=exclude_properties,
                    asset_model_version=asset_model_version,
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("asset_model_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def describe_asset_model_composite_model(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_asset_model_composite_model_response.DescribeAssetModelCompositeModelResponse":
        """<p>Retrieves information about an asset model composite model (also known as an asset model component). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html">Custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_composite_model_id: <p>The ID of a composite model on this asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_asset_model_composite_model_request.DescribeAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_asset_model_composite_model_response.DescribeAssetModelCompositeModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_composite_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_composite_model.async_describe_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_asset_model_composite_model_request.DescribeAssetModelCompositeModelRequest = {
            "asset_model_id": asset_model_id,
            "asset_model_composite_model_id": asset_model_composite_model_id,
        }
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_asset_model_interface_relationship(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_asset_model_interface_relationship_response.DescribeAssetModelInterfaceRelationshipResponse":
        """<p>Retrieves information about an interface relationship between an asset model and an interface asset model.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_asset_model_interface_relationship_request.DescribeAssetModelInterfaceRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_asset_model_interface_relationship_response.DescribeAssetModelInterfaceRelationshipResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_interface_relationship

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_model_interface_relationship.async_describe_asset_model_interface_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_asset_model_interface_relationship_request.DescribeAssetModelInterfaceRelationshipRequest = {
            "asset_model_id": asset_model_id,
            "interface_asset_model_id": interface_asset_model_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_asset_property(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        property_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_asset_property_response.DescribeAssetPropertyResponse":
        """<p>Retrieves information about an asset property.</p> <note> <p>When you call this operation for an attribute property, this response includes the default attribute value that you define in the asset model. If you update the default value in the model, this operation's response includes the new default value.</p> </note> <p>This operation doesn't return the value of the asset property. To get the value of an asset property, use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_GetAssetPropertyValue.html">GetAssetPropertyValue</a>.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_asset_property_request.DescribeAssetPropertyRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_asset_property_response.DescribeAssetPropertyResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_property

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_asset_property.async_describe_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_asset_property_request.DescribeAssetPropertyRequest = {
            "asset_id": asset_id,
            "property_id": property_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_bulk_import_job(
        self,
        job_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_bulk_import_job_response.DescribeBulkImportJobResponse":
        """<p>Retrieves information about a bulk import job request. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/DescribeBulkImportJob.html">Describe a bulk import job (CLI)</a> in the <i>Amazon Simple Storage Service User Guide</i>.</p>

        Args:
            job_id: <p>The ID of the job.</p>
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_bulk_import_job_request.DescribeBulkImportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_bulk_import_job_response.DescribeBulkImportJobResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_bulk_import_job

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_bulk_import_job.async_describe_bulk_import_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_bulk_import_job_request.DescribeBulkImportJobRequest = {
            "job_id": job_id
        }
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_computation_model(
        self,
        computation_model_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_version: Optional[
            "capo_iotsitewise.types.computation_model_version_filter.ComputationModelVersionFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_computation_model_response.DescribeComputationModelResponse":
        """<p>Retrieves information about a computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            computation_model_version: <p>The version of the computation model.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_computation_model_request.DescribeComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_computation_model_response.DescribeComputationModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model.async_describe_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_computation_model_request.DescribeComputationModelRequest = {
            "computation_model_id": computation_model_id
        }
        if computation_model_version is not None:
            input_["computation_model_version"] = computation_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_computation_model_execution_summary(
        self,
        computation_model_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        resolve_to_resource_type: Optional[
            "capo_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["capo_iotsitewise.types.id.ID"] = None,
    ) -> "capo_iotsitewise.types.describe_computation_model_execution_summary_response.DescribeComputationModelExecutionSummaryResponse":
        """<p>Retrieves information about the execution summary of a computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            resolve_to_resource_type: <p>The type of the resolved resource.</p>
            resolve_to_resource_id: <p>The ID of the resolved resource.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_computation_model_execution_summary_request.DescribeComputationModelExecutionSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_computation_model_execution_summary_response.DescribeComputationModelExecutionSummaryResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model_execution_summary

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_computation_model_execution_summary.async_describe_computation_model_execution_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_computation_model_execution_summary_request.DescribeComputationModelExecutionSummaryRequest = {
            "computation_model_id": computation_model_id
        }
        if resolve_to_resource_type is not None:
            input_["resolve_to_resource_type"] = resolve_to_resource_type
        if resolve_to_resource_id is not None:
            input_["resolve_to_resource_id"] = resolve_to_resource_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dashboard(
        self,
        dashboard_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_dashboard_response.DescribeDashboardResponse":
        """<p>Retrieves information about a dashboard.</p>

        Args:
            dashboard_id: <p>The ID of the dashboard.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_dashboard_request.DescribeDashboardRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_dashboard_response.DescribeDashboardResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_dashboard

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_dashboard.async_describe_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_dashboard_request.DescribeDashboardRequest = {
            "dashboard_id": dashboard_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
        dataset_version: Optional["capo_iotsitewise.types.version.Version"] = None,
    ) -> "capo_iotsitewise.types.describe_dataset_response.DescribeDatasetResponse":
        """<p>Retrieves information about a dataset.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            dataset_version: <p>The version of the dataset.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_dataset_request.DescribeDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_dataset_response.DescribeDatasetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_dataset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_dataset.async_describe_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_dataset_request.DescribeDatasetRequest = {
            "dataset_id": dataset_id
        }
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if dataset_version is not None:
            input_["dataset_version"] = dataset_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_dataset_export_job(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        job_id: "capo_iotsitewise.types.dataset_export_job_id.DatasetExportJobId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_dataset_export_job_response.DescribeDatasetExportJobResponse":
        """<p>Retrieves information about a dataset export job.</p>

        Args:
            workspace_name: <p>The name of the workspace that contains the dataset export job.</p>
            job_id: <p>The unique identifier for the dataset export job.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_dataset_export_job_request.DescribeDatasetExportJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_dataset_export_job_response.DescribeDatasetExportJobResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_dataset_export_job

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_dataset_export_job.async_describe_dataset_export_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_dataset_export_job_request.DescribeDatasetExportJobRequest = {
            "workspace_name": workspace_name,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_default_encryption_configuration(
        self, *, config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None
    ) -> "capo_iotsitewise.types.describe_default_encryption_configuration_response.DescribeDefaultEncryptionConfigurationResponse":
        """<p>Retrieves information about the default encryption configuration for the Amazon Web Services account in the default or specified Region. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html">Key management</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_default_encryption_configuration_request.DescribeDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_default_encryption_configuration_response.DescribeDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_default_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_default_encryption_configuration.async_describe_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_default_encryption_configuration_request.DescribeDefaultEncryptionConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_enrichment_job(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        job_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_enrichment_job_response.DescribeEnrichmentJobResponse":
        """<p>Retrieves detailed information about a specific enrichment job, including its current status, configuration, and timestamps.</p> <h2>Use Cases</h2> <ul> <li>Monitor job progress by checking status updates with DescribeEnrichmentJob</li> <li>Retrieve the complete job configuration submitted during creation</li> <li>Debug failed jobs by examining the failureMessage field</li> <li>Track job lifecycle with creation, update, completion, and cancellation timestamps</li> </ul> <h2>Status Monitoring</h2> <p>Jobs progress through statuses: PENDING → RUNNING → terminal state</p> <p>Terminal states:</p> <ul> <li>COMPLETED: Job finished successfully; query IoT SiteWise for semantic search results</li> <li>FAILED: Job encountered an error; check failureMessage for details</li> <li>TIMED_OUT: Job exceeded maximum processing time</li> <li>CANCELLED: Job was cancelled via CancelEnrichmentJob</li> </ul> <h2>Response Fields</h2> <p>The response includes:</p> <ul> <li>Current job status and type</li> <li>Full job configuration as originally submitted</li> <li>Lifecycle timestamps (created, updated, completed, cancelled)</li> <li>Failure details if status is FAILED</li> </ul>

        Args:
            workspace_name: <p>The name of the IoT SiteWise workspace containing the enrichment job.</p>
            job_id: <p>The unique identifier of the enrichment job to retrieve. This is the jobId returned by CreateEnrichmentJob.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_enrichment_job_request.DescribeEnrichmentJobRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_enrichment_job_response.DescribeEnrichmentJobResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_enrichment_job

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_enrichment_job.async_describe_enrichment_job(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_enrichment_job_request.DescribeEnrichmentJobRequest = {
            "workspace_name": workspace_name,
            "job_id": job_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_execution(
        self,
        execution_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_execution_response.DescribeExecutionResponse":
        """<p>Retrieves information about the execution.</p>

        Args:
            execution_id: <p>The ID of the execution.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_execution_request.DescribeExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_execution_response.DescribeExecutionResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_execution

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_execution.async_describe_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_execution_request.DescribeExecutionRequest = {
            "execution_id": execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_gateway(
        self,
        gateway_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_gateway_response.DescribeGatewayResponse":
        """<p>Retrieves information about a gateway.</p>

        Args:
            gateway_id: <p>The ID of the gateway device.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_gateway_request.DescribeGatewayRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_gateway_response.DescribeGatewayResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_gateway

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_gateway.async_describe_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_gateway_request.DescribeGatewayRequest = {
            "gateway_id": gateway_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_gateway_capability_configuration(
        self,
        gateway_id: "capo_iotsitewise.types.id.ID",
        capability_namespace: "capo_iotsitewise.types.capability_namespace.CapabilityNamespace",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_gateway_capability_configuration_response.DescribeGatewayCapabilityConfigurationResponse":
        """<p>Each gateway capability defines data sources for a gateway. This is the namespace of the gateway capability.</p> <p>. The namespace follows the format <code>service:capability:version</code>, where:</p> <ul> <li> <p> <code>service</code> - The service providing the capability, or <code>iotsitewise</code>.</p> </li> <li> <p> <code>capability</code> - The specific capability type. Options include: <code>opcuacollector</code> for the OPC UA data source collector, or <code>publisher</code> for data publisher capability.</p> </li> <li> <p> <code>version</code> - The version number of the capability. Option include <code>2</code> for Classic streams, V2 gateways, and <code>3</code> for MQTT-enabled, V3 gateways.</p> </li> </ul> <p>After updating a capability configuration, the sync status becomes <code>OUT_OF_SYNC</code> until the gateway processes the configuration.Use <code>DescribeGatewayCapabilityConfiguration</code> to check the sync status and verify the configuration was applied.</p> <p>A gateway can have multiple capability configurations with different namespaces.</p>

        Args:
            gateway_id: <p>The ID of the gateway that defines the capability configuration.</p>
            capability_namespace: <p>The namespace of the capability configuration. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:3</code>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_gateway_capability_configuration_request.DescribeGatewayCapabilityConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_gateway_capability_configuration_response.DescribeGatewayCapabilityConfigurationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_gateway_capability_configuration

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_gateway_capability_configuration.async_describe_gateway_capability_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_gateway_capability_configuration_request.DescribeGatewayCapabilityConfigurationRequest = {
            "gateway_id": gateway_id,
            "capability_namespace": capability_namespace,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_logging_options(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_logging_options_response.DescribeLoggingOptionsResponse":
        """<p>Retrieves the current IoT SiteWise logging options.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_logging_options_request.DescribeLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_logging_options_response.DescribeLoggingOptionsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_logging_options

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_logging_options.async_describe_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_logging_options_request.DescribeLoggingOptionsRequest = {}
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_pipeline(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        pipeline_version: Optional["capo_iotsitewise.types.version.Version"] = None,
    ) -> "capo_iotsitewise.types.describe_pipeline_response.DescribePipelineResponse":
        """<p>Retrieves detailed information about a specific pipeline in a workspace.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            pipeline_name: <p>The name of the pipeline.</p>
            pipeline_version: <p>The version number of the pipeline to retrieve. If not specified, returns the latest version.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_pipeline_request.DescribePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_pipeline_response.DescribePipelineResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_pipeline

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_pipeline.async_describe_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_pipeline_request.DescribePipelineRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
        }
        if pipeline_version is not None:
            input_["pipeline_version"] = pipeline_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_pipeline_execution(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        pipeline_execution_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.describe_pipeline_execution_request_max_results_integer.DescribePipelineExecutionRequestMaxResultsInteger"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_pipeline_execution_response.DescribePipelineExecutionResponse":
        """<p>Retrieves detailed information about a specific pipeline execution, including the overall execution status and the status of each individual compute node. Use this operation to monitor execution progress and inspect per-node results, environment variables, and error details.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            pipeline_name: <p>The name of the pipeline.</p>
            pipeline_execution_id: <p>The unique identifier of the pipeline execution.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of compute nodes to return per request. This is an upper bound; the actual number of results may be less. Default: 50.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_pipeline_execution_request.DescribePipelineExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_pipeline_execution_response.DescribePipelineExecutionResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_pipeline_execution

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_pipeline_execution.async_describe_pipeline_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_pipeline_execution_request.DescribePipelineExecutionRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
            "pipeline_execution_id": pipeline_execution_id,
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

    async def iter_describe_pipeline_execution(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        pipeline_execution_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.describe_pipeline_execution_request_max_results_integer.DescribePipelineExecutionRequestMaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.compute_node_execution_details.ComputeNodeExecutionDetails]":
        _token = next_token
        while True:
            _response = await self.describe_pipeline_execution(
                workspace_name,
                pipeline_name,
                pipeline_execution_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("compute_node_execution_details",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_portal(
        self,
        portal_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_portal_response.DescribePortalResponse":
        """<p>Retrieves information about a portal.</p>

        Args:
            portal_id: <p>The ID of the portal.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_portal_request.DescribePortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_portal_response.DescribePortalResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_portal

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_portal.async_describe_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_portal_request.DescribePortalRequest = {
            "portal_id": portal_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def wait_until_portal_not_exists(
        self,
        portal_id: "capo_iotsitewise.types.id.ID",
        *,
        max_wait_time: float,
        min_delay: float = 3,
        max_delay: float = 120,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> ServiceError:
        """Wait for portal_not_exists.

        Args:
            portal_id: <p>The ID of the portal.</p>
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_iotsitewise.types.describe_portal_response.DescribePortalResponse | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = await self.describe_portal(  # noqa: F841
                    portal_id, config_overrides=config_overrides
                )
            except ServiceError as e:
                op_error = e
            if op_error is not None and op_error.code == "ResourceNotFoundException":
                return op_error

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("portal_not_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            await anysleep(delay)
            attempt += 1

    async def describe_project(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_project_response.DescribeProjectResponse":
        """<p>Retrieves information about a project.</p>

        Args:
            project_id: <p>The ID of the project.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_project_request.DescribeProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_project_response.DescribeProjectResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_project

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_project.async_describe_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_project_request.DescribeProjectRequest = {
            "project_id": project_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_query(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        query_id: "capo_iotsitewise.types.query_id.QueryId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_query_response.DescribeQueryResponse":
        """<p>Retrieves information about a query, including its status.</p>

        Args:
            workspace_name: <p>The name of the workspace associated with the query.</p>
            query_id: <p>The unique identifier for the query execution.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_query_request.DescribeQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_query_response.DescribeQueryResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_query

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_query.async_describe_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_query_request.DescribeQueryRequest = {
            "workspace_name": workspace_name,
            "query_id": query_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_search(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        search_id: "capo_iotsitewise.types.search_id.SearchId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_search_response.DescribeSearchResponse":
        """<p>Returns the current status and metadata of a single search, including the query that was submitted, the search type, and — when the search has failed — the reason. Use this to poll a search started with <code>StartSearch</code> until it reaches a terminal status (<code>SUCCEEDED</code> or <code>FAILED</code>).</p>

        Args:
            workspace_name: <p>The name of the workspace the search belongs to.</p>
            search_id: <p>The identifier of the search to describe.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_search_request.DescribeSearchRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_search_response.DescribeSearchResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_search

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_search.async_describe_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_search_request.DescribeSearchRequest = {
            "workspace_name": workspace_name,
            "search_id": search_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_storage_configuration(
        self, *, config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None
    ) -> "capo_iotsitewise.types.describe_storage_configuration_response.DescribeStorageConfigurationResponse":
        """<p>Retrieves information about the storage configuration for IoT SiteWise.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_storage_configuration_request.DescribeStorageConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_storage_configuration_response.DescribeStorageConfigurationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_storage_configuration

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_storage_configuration.async_describe_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_storage_configuration_request.DescribeStorageConfigurationRequest = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_task(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        task_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        task_version: Optional["capo_iotsitewise.types.version.Version"] = None,
    ) -> "capo_iotsitewise.types.describe_task_response.DescribeTaskResponse":
        """<p>Retrieves detailed information about a specific task in a workspace.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            task_name: <p>The name of the task.</p>
            task_version: <p>The version number of the task to retrieve. If not specified, returns the latest version.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_task_request.DescribeTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_task_response.DescribeTaskResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_task

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_task.async_describe_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_task_request.DescribeTaskRequest = {
            "workspace_name": workspace_name,
            "task_name": task_name,
        }
        if task_version is not None:
            input_["task_version"] = task_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        alias: Optional["capo_iotsitewise.types.property_alias.PropertyAlias"] = None,
        asset_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        property_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "capo_iotsitewise.types.describe_time_series_response.DescribeTimeSeriesResponse":
        """<p>Retrieves information about a time series (data stream).</p> <p>To identify a time series, do one of the following:</p> <ul> <li> <p>If the time series isn't associated with an asset property, specify the <code>alias</code> of the time series.</p> </li> <li> <p>If the time series is associated with an asset property, specify one of the following: </p> <ul> <li> <p>The <code>alias</code> of the time series.</p> </li> <li> <p>The <code>assetId</code> and <code>propertyId</code> that identifies the asset property.</p> </li> </ul> </li> </ul>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_time_series_request.DescribeTimeSeriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_time_series_response.DescribeTimeSeriesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_time_series

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_time_series.async_describe_time_series(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_time_series_request.DescribeTimeSeriesRequest = {}
        if alias is not None:
            input_["alias"] = alias
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_workspace(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.describe_workspace_response.DescribeWorkspaceResponse":
        """<p>Retrieves information about a workspace.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.describe_workspace_request.DescribeWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.describe_workspace_response.DescribeWorkspaceResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.describe_workspace

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.describe_workspace.async_describe_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.describe_workspace_request.DescribeWorkspaceRequest = {
            "workspace_name": workspace_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def disassociate_assets(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        hierarchy_id: "capo_iotsitewise.types.custom_id.CustomID",
        child_asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Disassociates a child asset from the given parent asset through a hierarchy defined in the parent asset's model.</p>

        Args:
            asset_id: <p>The ID of the parent asset from which to disassociate the child asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            hierarchy_id: <p>The ID of a hierarchy in the parent asset's model. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.) Hierarchies allow different groupings of assets to be formed that all come from the same asset model. You can use the hierarchy ID to identify the correct asset to disassociate. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
            child_asset_id: <p>The ID of the child asset to disassociate. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.disassociate_assets_request.DisassociateAssetsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.disassociate_assets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.disassociate_assets.async_disassociate_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.disassociate_assets_request.DisassociateAssetsRequest = {
            "asset_id": asset_id,
            "hierarchy_id": hierarchy_id,
            "child_asset_id": child_asset_id,
        }
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

    async def disassociate_time_series_from_asset_property(
        self,
        alias: "capo_iotsitewise.types.property_alias.PropertyAlias",
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        property_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> None:
        """<p>Disassociates a time series (data stream) from an asset property.</p>

        Args:
            alias: <p>The alias that identifies the time series.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.disassociate_time_series_from_asset_property_request.DisassociateTimeSeriesFromAssetPropertyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.disassociate_time_series_from_asset_property

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.disassociate_time_series_from_asset_property.async_disassociate_time_series_from_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.disassociate_time_series_from_asset_property_request.DisassociateTimeSeriesFromAssetPropertyRequest = {
            "alias": alias,
            "asset_id": asset_id,
            "property_id": property_id,
        }
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

    async def execute_action(
        self,
        target_resource: "capo_iotsitewise.types.target_resource.TargetResource",
        action_definition_id: "capo_iotsitewise.types.id.ID",
        action_payload: "capo_iotsitewise.types.action_payload.ActionPayload",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        resolve_to: Optional["capo_iotsitewise.types.resolve_to.ResolveTo"] = None,
    ) -> "capo_iotsitewise.types.execute_action_response.ExecuteActionResponse":
        """<p>Executes an action on a target resource.</p>

        Args:
            target_resource: <p>The resource the action will be taken on.</p>
            action_definition_id: <p>The ID of the action definition.</p>
            action_payload: <p>The JSON payload of the action.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            resolve_to: <p>The detailed resource this action resolves to.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.execute_action_request.ExecuteActionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.execute_action_response.ExecuteActionResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.execute_action

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.execute_action.async_execute_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.execute_action_request.ExecuteActionRequest = {
            "target_resource": target_resource,
            "action_definition_id": action_definition_id,
            "action_payload": action_payload,
        }
        if client_token is not None:
            input_["client_token"] = client_token
        if resolve_to is not None:
            input_["resolve_to"] = resolve_to

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def execute_query(
        self,
        query_statement: "capo_iotsitewise.types.query_statement.QueryStatement",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.execute_query_next_token.ExecuteQueryNextToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.execute_query_max_results.ExecuteQueryMaxResults"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.execute_query_response.ExecuteQueryResponse":
        """<p>Run SQL queries to retrieve metadata and time-series data from asset models, assets, measurements, metrics, transforms, and aggregates.</p>

        Args:
            query_statement: <p>The IoT SiteWise query statement.</p>
            next_token: <p>The string that specifies the next page of results.</p>
            max_results: <p>The maximum number of results to return at one time.</p> <ul> <li> <p>Minimum is 1</p> </li> <li> <p>Maximum is 20000</p> </li> <li> <p>Default is 20000</p> </li> </ul>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.query_timeout_exception.QueryTimeoutException: <p>The query timed out.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.validation_exception.ValidationException: <p>The validation failed for this query.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.execute_query_request.ExecuteQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.execute_query_response.ExecuteQueryResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.execute_query

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.execute_query.async_execute_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.execute_query_request.ExecuteQueryRequest = {
            "query_statement": query_statement
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
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

    async def iter_execute_query(
        self,
        query_statement: "capo_iotsitewise.types.query_statement.QueryStatement",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.execute_query_next_token.ExecuteQueryNextToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.execute_query_max_results.ExecuteQueryMaxResults"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.row.Row]":
        _token = next_token
        while True:
            _response = await self.execute_query(
                query_statement,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                client_token=client_token,
            )
            _page = _resolve_path(_response, ("rows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_asset_property_aggregates(
        self,
        aggregate_types: "capo_iotsitewise.types.aggregate_types.AggregateTypes",
        resolution: "capo_iotsitewise.types.resolution.Resolution",
        start_date: "capo_iotsitewise.types.timestamp.Timestamp",
        end_date: "capo_iotsitewise.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        qualities: Optional["capo_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "capo_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.get_asset_property_value_aggregates_max_results.GetAssetPropertyValueAggregatesMaxResults"
        ] = None,
    ) -> "capo_iotsitewise.types.get_asset_property_aggregates_response.GetAssetPropertyAggregatesResponse":
        """<p>Gets aggregated values for an asset property. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#aggregates">Querying aggregates</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>
            aggregate_types: <p>The data aggregating function.</p>
            resolution: <p>The time interval over which to aggregate data.</p>
            qualities: <p>The quality by which to filter asset data.</p>
            start_date: <p>The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            end_date: <p>The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            time_ordering: <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 1 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 2500.</p> </li> </ul>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.get_asset_property_aggregates_request.GetAssetPropertyAggregatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.get_asset_property_aggregates_response.GetAssetPropertyAggregatesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_aggregates

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_aggregates.async_get_asset_property_aggregates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.get_asset_property_aggregates_request.GetAssetPropertyAggregatesRequest = {
            "aggregate_types": aggregate_types,
            "resolution": resolution,
            "start_date": start_date,
            "end_date": end_date,
        }
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if qualities is not None:
            input_["qualities"] = qualities
        if time_ordering is not None:
            input_["time_ordering"] = time_ordering
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

    async def iter_get_asset_property_aggregates(
        self,
        aggregate_types: "capo_iotsitewise.types.aggregate_types.AggregateTypes",
        resolution: "capo_iotsitewise.types.resolution.Resolution",
        start_date: "capo_iotsitewise.types.timestamp.Timestamp",
        end_date: "capo_iotsitewise.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        qualities: Optional["capo_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "capo_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.get_asset_property_value_aggregates_max_results.GetAssetPropertyValueAggregatesMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.aggregated_value.AggregatedValue]":
        _token = next_token
        while True:
            _response = await self.get_asset_property_aggregates(
                aggregate_types,
                resolution,
                start_date,
                end_date,
                config_overrides=config_overrides,
                asset_id=asset_id,
                property_id=property_id,
                property_alias=property_alias,
                qualities=qualities,
                time_ordering=time_ordering,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("aggregated_values",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_asset_property_value(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
    ) -> "capo_iotsitewise.types.get_asset_property_value_response.GetAssetPropertyValueResponse":
        """<p>Gets an asset property's current value. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#current-values">Querying current values</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.get_asset_property_value_request.GetAssetPropertyValueRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.get_asset_property_value_response.GetAssetPropertyValueResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value.async_get_asset_property_value(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.get_asset_property_value_request.GetAssetPropertyValueRequest = {}
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_asset_property_value_history(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_date: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        end_date: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        qualities: Optional["capo_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "capo_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.get_asset_property_value_history_max_results.GetAssetPropertyValueHistoryMaxResults"
        ] = None,
    ) -> "capo_iotsitewise.types.get_asset_property_value_history_response.GetAssetPropertyValueHistoryResponse":
        """<p>Gets the history of an asset property's values. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/query-industrial-data.html#historical-values">Querying historical values</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>
            start_date: <p>The exclusive start of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            end_date: <p>The inclusive end of the range from which to query historical data, expressed in seconds in Unix epoch time.</p>
            qualities: <p>The quality by which to filter asset data.</p>
            time_ordering: <p>The chronological sorting order of the requested information.</p> <p>Default: <code>ASCENDING</code> </p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. A result set is returned in the two cases, whichever occurs first.</p> <ul> <li> <p>The size of the result set is equal to 4 MB.</p> </li> <li> <p>The number of data points in the result set is equal to the value of <code>maxResults</code>. The maximum value of <code>maxResults</code> is 20000.</p> </li> </ul>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.get_asset_property_value_history_request.GetAssetPropertyValueHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.get_asset_property_value_history_response.GetAssetPropertyValueHistoryResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value_history

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.get_asset_property_value_history.async_get_asset_property_value_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.get_asset_property_value_history_request.GetAssetPropertyValueHistoryRequest = {}
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if qualities is not None:
            input_["qualities"] = qualities
        if time_ordering is not None:
            input_["time_ordering"] = time_ordering
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

    async def iter_get_asset_property_value_history(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_date: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        end_date: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        qualities: Optional["capo_iotsitewise.types.qualities.Qualities"] = None,
        time_ordering: Optional[
            "capo_iotsitewise.types.time_ordering.TimeOrdering"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.get_asset_property_value_history_max_results.GetAssetPropertyValueHistoryMaxResults"
        ] = None,
    ) -> (
        "AsyncIterator[capo_iotsitewise.types.asset_property_value.AssetPropertyValue]"
    ):
        _token = next_token
        while True:
            _response = await self.get_asset_property_value_history(
                config_overrides=config_overrides,
                asset_id=asset_id,
                property_id=property_id,
                property_alias=property_alias,
                start_date=start_date,
                end_date=end_date,
                qualities=qualities,
                time_ordering=time_ordering,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_property_value_history",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_capture_data(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        start_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos",
        end_time: "capo_iotsitewise.types.time_in_nanos.TimeInNanos",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        time_series_id: Optional[
            "capo_iotsitewise.types.time_series_id.TimeSeriesId"
        ] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        format_settings: Optional[
            "capo_iotsitewise.types.format_settings.FormatSettings"
        ] = None,
        next_token: Optional[
            "capo_iotsitewise.types.get_capture_data_next_token.GetCaptureDataNextToken"
        ] = None,
    ) -> "capo_iotsitewise.types.get_capture_data_response.GetCaptureDataResponse":
        """<p>Retrieves video data for a specific time range.</p>

        Args:
            workspace_name: <p>The name of the workspace that contains the capture source.</p>
            start_time: <p>The start time for the video data range.</p>
            end_time: <p>The end time for the video data range. Must be greater than startTime.</p>
            time_series_id: <p>The time series ID that identifies the capture source. Mutually exclusive with propertyAlias.</p>
            property_alias: <p>The property alias that identifies the capture source. Mutually exclusive with timeSeriesId.</p>
            format_settings: <p>The optional format settings for the output.</p>
            next_token: <p>The token from a previous response used to continue retrieving data.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.get_capture_data_request.GetCaptureDataRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.get_capture_data_response.GetCaptureDataResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.get_capture_data

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.get_capture_data.async_get_capture_data(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.get_capture_data_request.GetCaptureDataRequest = {
            "workspace_name": workspace_name,
            "start_time": start_time,
            "end_time": end_time,
        }
        if time_series_id is not None:
            input_["time_series_id"] = time_series_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if format_settings is not None:
            input_["format_settings"] = format_settings
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_interpolated_asset_property_values(
        self,
        start_time_in_seconds: "capo_iotsitewise.types.time_in_seconds.TimeInSeconds",
        end_time_in_seconds: "capo_iotsitewise.types.time_in_seconds.TimeInSeconds",
        quality: "capo_iotsitewise.types.quality.Quality",
        interval_in_seconds: "capo_iotsitewise.types.interval_in_seconds.IntervalInSeconds",
        type: "capo_iotsitewise.types.interpolation_type.InterpolationType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_time_offset_in_nanos: Optional[
            "capo_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        end_time_offset_in_nanos: Optional[
            "capo_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.max_interpolated_results.MaxInterpolatedResults"
        ] = None,
        interval_window_in_seconds: Optional[
            "capo_iotsitewise.types.interval_window_in_seconds.IntervalWindowInSeconds"
        ] = None,
    ) -> "capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse":
        """<p>Get interpolated values for an asset property for a specified time interval, during a period of time. If your time series is missing data points during the specified time interval, you can use interpolation to estimate the missing data.</p> <p>For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days.</p> <p>To identify an asset property, you must specify one of the following:</p> <ul> <li> <p>The <code>assetId</code> and <code>propertyId</code> of an asset property.</p> </li> <li> <p>A <code>propertyAlias</code>, which is a data stream alias (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). To define an asset property's alias, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html">UpdateAssetProperty</a>.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset, in UUID format.</p>
            property_id: <p>The ID of the asset property, in UUID format.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p>
            start_time_in_seconds: <p>The exclusive start of the range from which to interpolate data, expressed in seconds in Unix epoch time.</p>
            start_time_offset_in_nanos: <p>The nanosecond offset converted from <code>startTimeInSeconds</code>.</p>
            end_time_in_seconds: <p>The inclusive end of the range from which to interpolate data, expressed in seconds in Unix epoch time.</p>
            end_time_offset_in_nanos: <p>The nanosecond offset converted from <code>endTimeInSeconds</code>.</p>
            quality: <p>The quality of the asset property value. You can use this parameter as a filter to choose only the asset property values that have a specific quality.</p>
            interval_in_seconds: <p>The time interval in seconds over which to interpolate data. Each interval starts when the previous one ends.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. If not specified, the default value is 10.</p>
            type: <p>The interpolation type.</p> <p>Valid values: <code>LINEAR_INTERPOLATION | LOCF_INTERPOLATION</code> </p> <ul> <li> <p> <code>LINEAR_INTERPOLATION</code> – Estimates missing data using <a href="https://en.wikipedia.org/wiki/Linear_interpolation">linear interpolation</a>.</p> <p>For example, you can use this operation to return the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the first interpolated value on July 2, 2021, at 9 AM, the second interpolated value on July 3, 2021, at 9 AM, and so on.</p> </li> <li> <p> <code>LOCF_INTERPOLATION</code> – Estimates missing data using last observation carried forward interpolation</p> <p>If no data point is found for an interval, IoT SiteWise returns the last observed data point for the previous interval and carries forward this interpolated value until a new data point is found.</p> <p>For example, you can get the state of an on-off valve every 24 hours over a duration of 7 days. If the interpolation starts July 1, 2021, at 9 AM, IoT SiteWise returns the last observed data point between July 1, 2021, at 9 AM and July 2, 2021, at 9 AM as the first interpolated value. If a data point isn't found after 9 AM on July 2, 2021, IoT SiteWise uses the same interpolated value for the rest of the days.</p> </li> </ul>
            interval_window_in_seconds: <p>The query interval for the window, in seconds. IoT SiteWise computes each interpolated value by using data points from the timestamp of each interval, minus the window to the timestamp of each interval plus the window. If not specified, the window ranges between the start time minus the interval and the end time plus the interval.</p> <note> <ul> <li> <p>If you specify a value for the <code>intervalWindowInSeconds</code> parameter, the value for the <code>type</code> parameter must be <code>LINEAR_INTERPOLATION</code>.</p> </li> <li> <p>If a data point isn't found during the specified query window, IoT SiteWise won't return an interpolated value for the interval. This indicates that there's a gap in the ingested data points.</p> </li> </ul> </note> <p>For example, you can get the interpolated temperature values for a wind turbine every 24 hours over a duration of 7 days. If the interpolation starts on July 1, 2021, at 9 AM with a window of 2 hours, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 2, 2021 to compute the first interpolated value. Next, IoT SiteWise uses the data points from 7 AM (9 AM minus 2 hours) to 11 AM (9 AM plus 2 hours) on July 3, 2021 to compute the second interpolated value, and so on. </p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.service_unavailable_exception.ServiceUnavailableException: <p>The requested service is unavailable.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.get_interpolated_asset_property_values_response.GetInterpolatedAssetPropertyValuesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.get_interpolated_asset_property_values

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.get_interpolated_asset_property_values.async_get_interpolated_asset_property_values(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.get_interpolated_asset_property_values_request.GetInterpolatedAssetPropertyValuesRequest = {
            "start_time_in_seconds": start_time_in_seconds,
            "end_time_in_seconds": end_time_in_seconds,
            "quality": quality,
            "interval_in_seconds": interval_in_seconds,
            "type": type,
        }
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if property_id is not None:
            input_["property_id"] = property_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if start_time_offset_in_nanos is not None:
            input_["start_time_offset_in_nanos"] = start_time_offset_in_nanos
        if end_time_offset_in_nanos is not None:
            input_["end_time_offset_in_nanos"] = end_time_offset_in_nanos
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if interval_window_in_seconds is not None:
            input_["interval_window_in_seconds"] = interval_window_in_seconds

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_interpolated_asset_property_values(
        self,
        start_time_in_seconds: "capo_iotsitewise.types.time_in_seconds.TimeInSeconds",
        end_time_in_seconds: "capo_iotsitewise.types.time_in_seconds.TimeInSeconds",
        quality: "capo_iotsitewise.types.quality.Quality",
        interval_in_seconds: "capo_iotsitewise.types.interval_in_seconds.IntervalInSeconds",
        type: "capo_iotsitewise.types.interpolation_type.InterpolationType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        start_time_offset_in_nanos: Optional[
            "capo_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        end_time_offset_in_nanos: Optional[
            "capo_iotsitewise.types.offset_in_nanos.OffsetInNanos"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.max_interpolated_results.MaxInterpolatedResults"
        ] = None,
        interval_window_in_seconds: Optional[
            "capo_iotsitewise.types.interval_window_in_seconds.IntervalWindowInSeconds"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.interpolated_asset_property_value.InterpolatedAssetPropertyValue]":
        _token = next_token
        while True:
            _response = await self.get_interpolated_asset_property_values(
                start_time_in_seconds,
                end_time_in_seconds,
                quality,
                interval_in_seconds,
                type,
                config_overrides=config_overrides,
                asset_id=asset_id,
                property_id=property_id,
                property_alias=property_alias,
                start_time_offset_in_nanos=start_time_offset_in_nanos,
                end_time_offset_in_nanos=end_time_offset_in_nanos,
                next_token=_token,
                max_results=max_results,
                interval_window_in_seconds=interval_window_in_seconds,
            )
            _page = _resolve_path(_response, ("interpolated_asset_property_values",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_query_results(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        query_id: "capo_iotsitewise.types.query_id.QueryId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional[
            "capo_iotsitewise.types.query_max_results.QueryMaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsitewise.types.query_next_token.QueryNextToken"
        ] = None,
    ) -> "capo_iotsitewise.types.get_query_results_response.GetQueryResultsResponse":
        """<p>Retrieves the paginated results of a query. Returns empty rows if the query is not yet complete.</p>

        Args:
            workspace_name: <p>The name of the workspace associated with the query.</p>
            query_id: <p>The unique identifier for the query execution.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.get_query_results_request.GetQueryResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.get_query_results_response.GetQueryResultsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.get_query_results

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.get_query_results.async_get_query_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.get_query_results_request.GetQueryResultsRequest = {
            "workspace_name": workspace_name,
            "query_id": query_id,
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

    async def iter_get_query_results(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        query_id: "capo_iotsitewise.types.query_id.QueryId",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional[
            "capo_iotsitewise.types.query_max_results.QueryMaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsitewise.types.query_next_token.QueryNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.result.Result]":
        _token = next_token
        while True:
            _response = await self.get_query_results(
                workspace_name,
                query_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("rows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_search_results(
        self,
        search_id: "capo_iotsitewise.types.search_id.SearchId",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional[
            "capo_iotsitewise.types.get_search_results_request_max_results_integer.GetSearchResultsRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "capo_iotsitewise.types.get_search_results_response.GetSearchResultsResponse":
        """<p>Retrieves the ranked results of a search, ordered by descending relevance score. Results are available only after the search has reached the <code>SUCCEEDED</code> status. Calling this on a search that exists but has not yet completed returns <code>InvalidRequestException</code>, while calling it on a search that does not exist returns <code>ResourceNotFoundException</code>. The response is paginated: when <code>nextToken</code> is present, pass it on a subsequent call to retrieve the next page.</p>

        Args:
            search_id: <p>The identifier of the search whose results are retrieved.</p>
            workspace_name: <p>The name of the workspace the search belongs to.</p>
            max_results: <p>The maximum number of results to return in a single page. Valid range is 1 to 10,000; if omitted, a service-defined default is used.</p>
            next_token: <p>The pagination token returned by a previous GetSearchResults call. Provide it to retrieve the next page of results; omit it to retrieve the first page.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.get_search_results_request.GetSearchResultsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.get_search_results_response.GetSearchResultsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.get_search_results

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.get_search_results.async_get_search_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.get_search_results_request.GetSearchResultsRequest = {
            "search_id": search_id,
            "workspace_name": workspace_name,
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

    async def iter_get_search_results(
        self,
        search_id: "capo_iotsitewise.types.search_id.SearchId",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional[
            "capo_iotsitewise.types.get_search_results_request_max_results_integer.GetSearchResultsRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.search_result.SearchResult]":
        _token = next_token
        while True:
            _response = await self.get_search_results(
                search_id,
                workspace_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("search_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    @asynccontextmanager
    async def invoke_assistant(
        self,
        message: "capo_iotsitewise.types.message_input.MessageInput",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        conversation_id: Optional[
            "capo_iotsitewise.types.conversation_id.ConversationId"
        ] = None,
        enable_trace: Optional[bool] = None,
    ) -> "AsyncGenerator[capo_iotsitewise.types.invoke_assistant_response.InvokeAssistantResponse]":
        """<p>Invokes SiteWise Assistant to start or continue a conversation.</p>

        Args:
            conversation_id: <p>The ID assigned to a conversation. IoT SiteWise automatically generates a unique ID for you, and this parameter is never required. However, if you prefer to have your own ID, you must specify it here in UUID format. If you specify your own ID, it must be globally unique.</p>
            message: <p>A text message sent to the SiteWise Assistant by the user.</p>
            enable_trace: <p>Specifies if to turn trace on or not. It is used to track the SiteWise Assistant's reasoning, and data access process.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.invoke_assistant_request.InvokeAssistantRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.invoke_assistant_response.InvokeAssistantResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.invoke_assistant

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.invoke_assistant.async_invoke_assistant(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.invoke_assistant_request.InvokeAssistantRequest = {
            "message": message
        }
        if conversation_id is not None:
            input_["conversation_id"] = conversation_id
        if enable_trace is not None:
            input_["enable_trace"] = enable_trace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        try:
            yield response.output
        finally:
            await response.response.aclose()

    async def list_access_policies(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        identity_type: Optional[
            "capo_iotsitewise.types.identity_type.IdentityType"
        ] = None,
        identity_id: Optional["capo_iotsitewise.types.identity_id.IdentityId"] = None,
        resource_type: Optional[
            "capo_iotsitewise.types.resource_type.ResourceType"
        ] = None,
        resource_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        iam_arn: Optional["capo_iotsitewise.types.iam_arn.IamArn"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_access_policies_response.ListAccessPoliciesResponse":
        """<p>Retrieves a paginated list of access policies for an identity (an IAM Identity Center user, an IAM Identity Center group, or an IAM user) or an IoT SiteWise Monitor resource (a portal or project).</p>

        Args:
            identity_type: <p>The type of identity (IAM Identity Center user, IAM Identity Center group, or IAM user). This parameter is required if you specify <code>identityId</code>.</p>
            identity_id: <p>The ID of the identity. This parameter is required if you specify <code>USER</code> or <code>GROUP</code> for <code>identityType</code>.</p>
            resource_type: <p>The type of resource (portal or project). This parameter is required if you specify <code>resourceId</code>.</p>
            resource_id: <p>The ID of the resource. This parameter is required if you specify <code>resourceType</code>.</p>
            iam_arn: <p>The ARN of the IAM user. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html">IAM ARNs</a> in the <i>IAM User Guide</i>. This parameter is required if you specify <code>IAM</code> for <code>identityType</code>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_access_policies_request.ListAccessPoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_access_policies_response.ListAccessPoliciesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_access_policies

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_access_policies.async_list_access_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_access_policies_request.ListAccessPoliciesRequest = {}
        if identity_type is not None:
            input_["identity_type"] = identity_type
        if identity_id is not None:
            input_["identity_id"] = identity_id
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if resource_id is not None:
            input_["resource_id"] = resource_id
        if iam_arn is not None:
            input_["iam_arn"] = iam_arn
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

    async def iter_list_access_policies(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        identity_type: Optional[
            "capo_iotsitewise.types.identity_type.IdentityType"
        ] = None,
        identity_id: Optional["capo_iotsitewise.types.identity_id.IdentityId"] = None,
        resource_type: Optional[
            "capo_iotsitewise.types.resource_type.ResourceType"
        ] = None,
        resource_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        iam_arn: Optional["capo_iotsitewise.types.iam_arn.IamArn"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.access_policy_summary.AccessPolicySummary]":
        _token = next_token
        while True:
            _response = await self.list_access_policies(
                config_overrides=config_overrides,
                identity_type=identity_type,
                identity_id=identity_id,
                resource_type=resource_type,
                resource_id=resource_id,
                iam_arn=iam_arn,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("access_policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_actions(
        self,
        target_resource_type: "capo_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        resolve_to_resource_type: Optional[
            "capo_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["capo_iotsitewise.types.id.ID"] = None,
    ) -> "capo_iotsitewise.types.list_actions_response.ListActionsResponse":
        """<p>Retrieves a paginated list of actions for a specific target resource.</p>

        Args:
            target_resource_type: <p>The type of resource.</p>
            target_resource_id: <p>The ID of the target resource.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            resolve_to_resource_type: <p>The type of the resolved resource.</p>
            resolve_to_resource_id: <p>The ID of the resolved resource.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_actions_request.ListActionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_actions_response.ListActionsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_actions

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_actions.async_list_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_actions_request.ListActionsRequest = {
            "target_resource_type": target_resource_type,
            "target_resource_id": target_resource_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if resolve_to_resource_type is not None:
            input_["resolve_to_resource_type"] = resolve_to_resource_type
        if resolve_to_resource_id is not None:
            input_["resolve_to_resource_id"] = resolve_to_resource_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_actions(
        self,
        target_resource_type: "capo_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        resolve_to_resource_type: Optional[
            "capo_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["capo_iotsitewise.types.id.ID"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.action_summary.ActionSummary]":
        _token = next_token
        while True:
            _response = await self.list_actions(
                target_resource_type,
                target_resource_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                resolve_to_resource_type=resolve_to_resource_type,
                resolve_to_resource_id=resolve_to_resource_id,
            )
            _page = _resolve_path(_response, ("action_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_applications(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "capo_iotsitewise.types.list_applications_response.ListApplicationsResponse":
        """<p>Retrieves a paginated list of existing applications</p>

        Args:
            max_results: <p>Maximum number of results to return</p>
            next_token: <p>Next Page Token</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_applications_request.ListApplicationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_applications

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_applications.async_list_applications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_applications_request.ListApplicationsRequest = {}
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

    async def iter_list_applications(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.application_summary.ApplicationSummary]":
        _token = next_token
        while True:
            _response = await self.list_applications(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("applications",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_model_composite_models(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.list_asset_model_composite_models_response.ListAssetModelCompositeModelsResponse":
        """<p>Retrieves a paginated list of composite models associated with the asset model</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_asset_model_composite_models_request.ListAssetModelCompositeModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_asset_model_composite_models_response.ListAssetModelCompositeModelsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_composite_models

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_composite_models.async_list_asset_model_composite_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_asset_model_composite_models_request.ListAssetModelCompositeModelsRequest = {
            "asset_model_id": asset_model_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_asset_model_composite_models(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.asset_model_composite_model_summary.AssetModelCompositeModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_model_composite_models(
                asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                asset_model_version=asset_model_version,
            )
            _page = _resolve_path(_response, ("asset_model_composite_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_model_properties(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_asset_model_properties_filter.ListAssetModelPropertiesFilter"
        ] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.list_asset_model_properties_response.ListAssetModelPropertiesResponse":
        """<p>Retrieves a paginated list of properties associated with an asset model. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. If not specified, the default value is 50.</p>
            filter: <p> Filters the requested list of asset model properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset model properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset model properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_asset_model_properties_request.ListAssetModelPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_asset_model_properties_response.ListAssetModelPropertiesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_properties

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_model_properties.async_list_asset_model_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_asset_model_properties_request.ListAssetModelPropertiesRequest = {
            "asset_model_id": asset_model_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_asset_model_properties(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_asset_model_properties_filter.ListAssetModelPropertiesFilter"
        ] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.asset_model_property_summary.AssetModelPropertySummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_model_properties(
                asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
                asset_model_version=asset_model_version,
            )
            _page = _resolve_path(_response, ("asset_model_property_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_types: Optional[
            "capo_iotsitewise.types.list_asset_models_type_filter.ListAssetModelsTypeFilter"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.list_asset_models_response.ListAssetModelsResponse":
        """<p>Retrieves a paginated list of summaries of all asset models.</p>

        Args:
            asset_model_types: <p>The type of asset model. If you don't provide an <code>assetModelTypes</code>, all types of asset models are returned.</p> <ul> <li> <p> <b>ASSET_MODEL</b> – An asset model that you can use to create assets. Can't be included as a component in another asset model.</p> </li> <li> <p> <b>COMPONENT_MODEL</b> – A reusable component that you can include in the composite models of other asset models. You can't create assets directly from this type of asset model. </p> </li> <li> <p> <b>INTERFACE</b> – An interface is a type of model that defines a standard structure that can be applied to different asset models.</p> </li> </ul>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
            asset_model_version: <p>The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is <code>LATEST</code>. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html"> Asset model versions</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_asset_models_request.ListAssetModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_asset_models_response.ListAssetModelsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_models

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_models.async_list_asset_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_asset_models_request.ListAssetModelsRequest = {}
        if asset_model_types is not None:
            input_["asset_model_types"] = asset_model_types
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_model_version is not None:
            input_["asset_model_version"] = asset_model_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_asset_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_types: Optional[
            "capo_iotsitewise.types.list_asset_models_type_filter.ListAssetModelsTypeFilter"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_model_version: Optional[
            "capo_iotsitewise.types.asset_model_version_filter.AssetModelVersionFilter"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.asset_model_summary.AssetModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_models(
                config_overrides=config_overrides,
                asset_model_types=asset_model_types,
                next_token=_token,
                max_results=max_results,
                asset_model_version=asset_model_version,
            )
            _page = _resolve_path(_response, ("asset_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_properties(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_asset_properties_filter.ListAssetPropertiesFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.list_asset_properties_response.ListAssetPropertiesResponse":
        """<p>Retrieves a paginated list of properties associated with an asset. If you update properties associated with the model before you finish listing all the properties, you need to start all over again.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. If not specified, the default value is 50.</p>
            filter: <p> Filters the requested list of asset properties. You can choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all asset properties for a given asset model ID. </p> </li> <li> <p> <code>BASE</code> – The list includes only base asset properties for a given asset model ID. </p> </li> </ul> <p>Default: <code>BASE</code> </p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_asset_properties_request.ListAssetPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_asset_properties_response.ListAssetPropertiesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_properties

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_properties.async_list_asset_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_asset_properties_request.ListAssetPropertiesRequest = {
            "asset_id": asset_id
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

    async def iter_list_asset_properties(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_asset_properties_filter.ListAssetPropertiesFilter"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.asset_property_summary.AssetPropertySummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_properties(
                asset_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
            )
            _page = _resolve_path(_response, ("asset_property_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_asset_relationships(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        traversal_type: "capo_iotsitewise.types.traversal_type.TraversalType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_asset_relationships_response.ListAssetRelationshipsResponse":
        """<p>Retrieves a paginated list of asset relationships for an asset. You can use this operation to identify an asset's root asset and all associated assets between that asset and its root.</p>

        Args:
            asset_id: <p>The ID of the asset. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            traversal_type: <p>The type of traversal to use to identify asset relationships. Choose the following option:</p> <ul> <li> <p> <code>PATH_TO_ROOT</code> – Identify the asset's parent assets up to the root asset. The asset that you specify in <code>assetId</code> is the first result in the list of <code>assetRelationshipSummaries</code>, and the root asset is the last result.</p> </li> </ul>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_asset_relationships_request.ListAssetRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_asset_relationships_response.ListAssetRelationshipsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_relationships

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_asset_relationships.async_list_asset_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_asset_relationships_request.ListAssetRelationshipsRequest = {
            "asset_id": asset_id,
            "traversal_type": traversal_type,
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

    async def iter_list_asset_relationships(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        traversal_type: "capo_iotsitewise.types.traversal_type.TraversalType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.asset_relationship_summary.AssetRelationshipSummary]":
        _token = next_token
        while True:
            _response = await self.list_asset_relationships(
                asset_id,
                traversal_type,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_relationship_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_assets(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_model_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_assets_filter.ListAssetsFilter"
        ] = None,
    ) -> "capo_iotsitewise.types.list_assets_response.ListAssetsResponse":
        """<p>Retrieves a paginated list of asset summaries.</p> <p>You can use this operation to do the following:</p> <ul> <li> <p>List assets based on a specific asset model.</p> </li> <li> <p>List top-level assets.</p> </li> </ul> <p>You can't use this operation to list all assets. To retrieve summaries for all of your assets, use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ListAssetModels.html">ListAssetModels</a> to get all of your asset model IDs. Then, use ListAssets to get all assets for each asset model.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>
            asset_model_id: <p>The ID of the asset model by which to filter the list of assets. This parameter is required if you choose <code>ALL</code> for <code>filter</code>. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            filter: <p>The filter for the requested list of assets. Choose one of the following options:</p> <ul> <li> <p> <code>ALL</code> – The list includes all assets for a given asset model ID. The <code>assetModelId</code> parameter is required if you filter by <code>ALL</code>.</p> </li> <li> <p> <code>TOP_LEVEL</code> – The list includes only top-level assets in the asset hierarchy tree.</p> </li> </ul> <p>Default: <code>ALL</code> </p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_assets_request.ListAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_assets_response.ListAssetsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_assets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_assets.async_list_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_assets_request.ListAssetsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_model_id is not None:
            input_["asset_model_id"] = asset_model_id
        if filter is not None:
            input_["filter"] = filter

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_assets(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_model_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_assets_filter.ListAssetsFilter"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.asset_summary.AssetSummary]":
        _token = next_token
        while True:
            _response = await self.list_assets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                asset_model_id=asset_model_id,
                filter=filter,
            )
            _page = _resolve_path(_response, ("asset_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_associated_assets(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        hierarchy_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        traversal_direction: Optional[
            "capo_iotsitewise.types.traversal_direction.TraversalDirection"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_associated_assets_response.ListAssociatedAssetsResponse":
        """<p>Retrieves a paginated list of associated assets.</p> <p>You can use this operation to do the following:</p> <ul> <li> <p> <code>CHILD</code> - List all child assets associated to the asset.</p> </li> <li> <p> <code>PARENT</code> - List the asset's parent asset.</p> </li> </ul>

        Args:
            asset_id: <p>The ID of the asset to query. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            hierarchy_id: <p>(Optional) If you don't provide a <code>hierarchyId</code>, all the immediate assets in the <code>traversalDirection</code> will be returned. </p> <p> The ID of the hierarchy by which child assets are associated to the asset. (This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.)</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p>
            traversal_direction: <p>The direction to list associated assets. Choose one of the following options:</p> <ul> <li> <p> <code>CHILD</code> – The list includes all child assets associated to the asset.</p> </li> <li> <p> <code>PARENT</code> – The list includes the asset's parent asset.</p> </li> </ul> <p>Default: <code>CHILD</code> </p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_associated_assets_request.ListAssociatedAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_associated_assets_response.ListAssociatedAssetsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_associated_assets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_associated_assets.async_list_associated_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_associated_assets_request.ListAssociatedAssetsRequest = {
            "asset_id": asset_id
        }
        if hierarchy_id is not None:
            input_["hierarchy_id"] = hierarchy_id
        if traversal_direction is not None:
            input_["traversal_direction"] = traversal_direction
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

    async def iter_list_associated_assets(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        hierarchy_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        traversal_direction: Optional[
            "capo_iotsitewise.types.traversal_direction.TraversalDirection"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.associated_assets_summary.AssociatedAssetsSummary]":
        _token = next_token
        while True:
            _response = await self.list_associated_assets(
                asset_id,
                config_overrides=config_overrides,
                hierarchy_id=hierarchy_id,
                traversal_direction=traversal_direction,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_bulk_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_bulk_import_jobs_filter.ListBulkImportJobsFilter"
        ] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "capo_iotsitewise.types.list_bulk_import_jobs_response.ListBulkImportJobsResponse":
        """<p>Retrieves a paginated list of bulk import job requests. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ListBulkImportJobs.html">List bulk import jobs (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            filter: <p>You can use a filter to select the bulk import jobs that you want to retrieve.</p>
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_bulk_import_jobs_request.ListBulkImportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_bulk_import_jobs_response.ListBulkImportJobsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_bulk_import_jobs

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_bulk_import_jobs.async_list_bulk_import_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_bulk_import_jobs_request.ListBulkImportJobsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filter is not None:
            input_["filter"] = filter
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_bulk_import_jobs(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        filter: Optional[
            "capo_iotsitewise.types.list_bulk_import_jobs_filter.ListBulkImportJobsFilter"
        ] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = await self.list_bulk_import_jobs(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                filter=filter,
                workspace_name=workspace_name,
            )
            _page = _resolve_path(_response, ("job_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_composition_relationships(
        self,
        asset_model_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_composition_relationships_response.ListCompositionRelationshipsResponse":
        """<p>Retrieves a paginated list of composition relationships for an asset model of type <code>COMPONENT_MODEL</code>.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_composition_relationships_request.ListCompositionRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_composition_relationships_response.ListCompositionRelationshipsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_composition_relationships

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_composition_relationships.async_list_composition_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_composition_relationships_request.ListCompositionRelationshipsRequest = {
            "asset_model_id": asset_model_id
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

    async def iter_list_composition_relationships(
        self,
        asset_model_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.composition_relationship_summary.CompositionRelationshipSummary]":
        _token = next_token
        while True:
            _response = await self.list_composition_relationships(
                asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("composition_relationship_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_computation_model_data_binding_usages(
        self,
        data_binding_value_filter: "capo_iotsitewise.types.data_binding_value_filter.DataBindingValueFilter",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_computation_model_data_binding_usages_response.ListComputationModelDataBindingUsagesResponse":
        """<p> Lists all data binding usages for computation models. This allows to identify where specific data bindings are being utilized across the computation models. This track dependencies between data sources and computation models. </p>

        Args:
            data_binding_value_filter: <p>A filter used to limit the returned data binding usages based on specific data binding values. You can filter by asset, asset model, asset property, or asset model property to find all computation models using these specific data sources.</p>
            next_token: <p>The token used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results returned for each paginated request.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_computation_model_data_binding_usages_request.ListComputationModelDataBindingUsagesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_computation_model_data_binding_usages_response.ListComputationModelDataBindingUsagesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_data_binding_usages

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_data_binding_usages.async_list_computation_model_data_binding_usages(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_computation_model_data_binding_usages_request.ListComputationModelDataBindingUsagesRequest = {
            "data_binding_value_filter": data_binding_value_filter
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

    async def iter_list_computation_model_data_binding_usages(
        self,
        data_binding_value_filter: "capo_iotsitewise.types.data_binding_value_filter.DataBindingValueFilter",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.computation_model_data_binding_usage_summary.ComputationModelDataBindingUsageSummary]":
        _token = next_token
        while True:
            _response = await self.list_computation_model_data_binding_usages(
                data_binding_value_filter,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("data_binding_usage_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_computation_model_resolve_to_resources(
        self,
        computation_model_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_computation_model_resolve_to_resources_response.ListComputationModelResolveToResourcesResponse":
        """<p>Lists all distinct resources that are resolved from the executed actions of the computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model for which to list resolved resources.</p>
            next_token: <p>The token used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results returned for each paginated request.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_computation_model_resolve_to_resources_request.ListComputationModelResolveToResourcesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_computation_model_resolve_to_resources_response.ListComputationModelResolveToResourcesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_resolve_to_resources

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_computation_model_resolve_to_resources.async_list_computation_model_resolve_to_resources(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_computation_model_resolve_to_resources_request.ListComputationModelResolveToResourcesRequest = {
            "computation_model_id": computation_model_id
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

    async def iter_list_computation_model_resolve_to_resources(
        self,
        computation_model_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.computation_model_resolve_to_resource_summary.ComputationModelResolveToResourceSummary]":
        _token = next_token
        while True:
            _response = await self.list_computation_model_resolve_to_resources(
                computation_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(
                _response, ("computation_model_resolve_to_resource_summaries",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_computation_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_type: Optional[
            "capo_iotsitewise.types.computation_model_type.ComputationModelType"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_computation_models_response.ListComputationModelsResponse":
        """<p>Retrieves a paginated list of summaries of all computation models.</p>

        Args:
            computation_model_type: <p>The type of computation model. If a <code>computationModelType</code> is not provided, all types of computation models are returned.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_computation_models_request.ListComputationModelsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_computation_models_response.ListComputationModelsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_computation_models

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_computation_models.async_list_computation_models(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_computation_models_request.ListComputationModelsRequest = {}
        if computation_model_type is not None:
            input_["computation_model_type"] = computation_model_type
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

    async def iter_list_computation_models(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_type: Optional[
            "capo_iotsitewise.types.computation_model_type.ComputationModelType"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.computation_model_summary.ComputationModelSummary]":
        _token = next_token
        while True:
            _response = await self.list_computation_models(
                config_overrides=config_overrides,
                computation_model_type=computation_model_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("computation_model_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dashboards(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_dashboards_response.ListDashboardsResponse":
        """<p>Retrieves a paginated list of dashboards for an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_dashboards_request.ListDashboardsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_dashboards_response.ListDashboardsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_dashboards

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_dashboards.async_list_dashboards(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_dashboards_request.ListDashboardsRequest = {
            "project_id": project_id
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

    async def iter_list_dashboards(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.dashboard_summary.DashboardSummary]":
        _token = next_token
        while True:
            _response = await self.list_dashboards(
                project_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dashboard_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dataset_data_segment_relationships(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "capo_iotsitewise.types.list_dataset_data_segment_relationships_response.ListDatasetDataSegmentRelationshipsResponse":
        """<p>Retrieves a paginated list of data segment relationships for a session dataset. Use this operation to find the curated datasets that reference data segments of the specified session dataset. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            dataset_id: <p>The ID of the session dataset to list data segment relationships for.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            max_results: <p>The maximum number of results to return for each paginated request. Default: 50.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_dataset_data_segment_relationships_request.ListDatasetDataSegmentRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_dataset_data_segment_relationships_response.ListDatasetDataSegmentRelationshipsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_dataset_data_segment_relationships

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_dataset_data_segment_relationships.async_list_dataset_data_segment_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_dataset_data_segment_relationships_request.ListDatasetDataSegmentRelationshipsRequest = {
            "dataset_id": dataset_id,
            "workspace_name": workspace_name,
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

    async def iter_list_dataset_data_segment_relationships(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.data_segment_relationship_summary.DataSegmentRelationshipSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_data_segment_relationships(
                dataset_id,
                workspace_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("data_segment_relationship_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dataset_data_segments(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dataset_version: Optional["capo_iotsitewise.types.version.Version"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "capo_iotsitewise.types.list_dataset_data_segments_response.ListDatasetDataSegmentsResponse":
        """<p>Retrieves a paginated list of data segments associated with a dataset. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            dataset_version: <p>The version of the dataset to list data segments for.</p>
            max_results: <p>The maximum number of results to return for each paginated request. Default: 50.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_dataset_data_segments_request.ListDatasetDataSegmentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_dataset_data_segments_response.ListDatasetDataSegmentsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_dataset_data_segments

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_dataset_data_segments.async_list_dataset_data_segments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_dataset_data_segments_request.ListDatasetDataSegmentsRequest = {
            "dataset_id": dataset_id,
            "workspace_name": workspace_name,
        }
        if dataset_version is not None:
            input_["dataset_version"] = dataset_version
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

    async def iter_list_dataset_data_segments(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dataset_version: Optional["capo_iotsitewise.types.version.Version"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[capo_iotsitewise.types.data_segment_summary.DataSegmentSummary]"
    ):
        _token = next_token
        while True:
            _response = await self.list_dataset_data_segments(
                dataset_id,
                workspace_name,
                config_overrides=config_overrides,
                dataset_version=dataset_version,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("data_segments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_dataset_export_jobs(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        filter: Optional[
            "capo_iotsitewise.types.dataset_export_job_filter.DatasetExportJobFilter"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_export_jobs_max_results.ListExportJobsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsitewise.types.list_export_jobs_next_token.ListExportJobsNextToken"
        ] = None,
    ) -> "capo_iotsitewise.types.list_dataset_export_jobs_response.ListDatasetExportJobsResponse":
        """<p>Retrieves a paginated list of dataset export jobs for a workspace.</p>

        Args:
            workspace_name: <p>The name of the workspace whose dataset export jobs should be listed.</p>
            filter: <p>The optional filter that returns only jobs matching the given filter value. Defaults to ALL.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_dataset_export_jobs_request.ListDatasetExportJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_dataset_export_jobs_response.ListDatasetExportJobsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_dataset_export_jobs

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_dataset_export_jobs.async_list_dataset_export_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_dataset_export_jobs_request.ListDatasetExportJobsRequest = {
            "workspace_name": workspace_name
        }
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_dataset_export_jobs(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        filter: Optional[
            "capo_iotsitewise.types.dataset_export_job_filter.DatasetExportJobFilter"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_export_jobs_max_results.ListExportJobsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsitewise.types.list_export_jobs_next_token.ListExportJobsNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.export_job_summary.ExportJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_dataset_export_jobs(
                workspace_name,
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_datasets(
        self,
        source_type: "capo_iotsitewise.types.dataset_source_type.DatasetSourceType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
        dataset_type: Optional[
            "capo_iotsitewise.types.dataset_type_enum.DatasetTypeEnum"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_datasets_response.ListDatasetsResponse":
        """<p>Retrieves a paginated list of datasets for a specific target resource.</p>

        Args:
            source_type: <p>The type of data source for the dataset.</p>
            workspace_name: <p>The name of the workspace to filter datasets by.</p>
            dataset_type: <p>The type of dataset to filter by: a session dataset, a curated dataset, or a connection to an external datasource.</p>
            next_token: <p>The token for the next set of results, or null if there are no additional results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_datasets_request.ListDatasetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_datasets_response.ListDatasetsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_datasets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_datasets.async_list_datasets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_datasets_request.ListDatasetsRequest = {
            "source_type": source_type
        }
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if dataset_type is not None:
            input_["dataset_type"] = dataset_type
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

    async def iter_list_datasets(
        self,
        source_type: "capo_iotsitewise.types.dataset_source_type.DatasetSourceType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
        dataset_type: Optional[
            "capo_iotsitewise.types.dataset_type_enum.DatasetTypeEnum"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.dataset_summary.DatasetSummary]":
        _token = next_token
        while True:
            _response = await self.list_datasets(
                source_type,
                config_overrides=config_overrides,
                workspace_name=workspace_name,
                dataset_type=dataset_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dataset_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_enrichment_jobs(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dataset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        time_series_id: Optional[
            "capo_iotsitewise.types.time_series_id.TimeSeriesId"
        ] = None,
        status: Optional[
            "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus"
        ] = None,
        job_type: Optional["capo_iotsitewise.types.job_type.JobType"] = None,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse":
        """<p>Lists enrichment jobs within a workspace with optional filtering and pagination. Results are ordered by createdAt timestamp descending (newest first).</p> <h2>Filtering</h2> <p>Combine filters to narrow results:</p> <ul> <li><strong>datasetId</strong>: Filter by dataset</li> <li><strong>propertyAlias</strong> OR <strong>timeSeriesId</strong>: Filter by time series (specify one, not both)</li> <li><strong>status</strong>: Filter by job status (e.g., RUNNING to find active jobs)</li> <li><strong>jobType</strong>: Filter by enrichment type (currently only EVENT_DETECTION)</li> <li><strong>startDate</strong> and <strong>endDate</strong>: Filter by job creation time range</li> </ul> <h2>Important Constraints</h2> <ul> <li>You must specify either propertyAlias OR timeSeriesId, but not both</li> <li>Attempting to specify both results in an InvalidRequestException</li> <li>Date filters use ISO 8601 format</li> <li>startDate is exclusive, endDate is inclusive</li> </ul> <h2>Pagination</h2> <p>The operation returns up to maxResults jobs per page (default 50). If more results exist, the response includes a nextToken. Submit this token in a subsequent request to retrieve the next page.</p> <h2>Common Use Cases</h2> <ul> <li>Find all running jobs: Filter by status=RUNNING</li> <li>List recent jobs for a dataset: Filter by datasetId with optional date range</li> <li>Monitor jobs for a specific sensor: Filter by propertyAlias or timeSeriesId</li> <li>Track all event detection jobs: Filter by jobType=EVENT_DETECTION</li> </ul> <h2>Performance</h2> <p>Performance is optimal when filtering by supported fields (datasetId, propertyAlias, timeSeriesId, status, jobType).</p>

        Args:
            workspace_name: <p>The name of the IoT SiteWise workspace to list enrichment jobs from.</p>
            dataset_id: <p>Filter jobs by dataset ID. Returns only jobs analyzing data from the specified dataset.</p>
            property_alias: <p>Filter by property alias (human-readable sensor name). Specify either propertyAlias or timeSeriesId, but not both. Returns only jobs analyzing the specified property alias.</p>
            time_series_id: <p>Filter by time series ID (system identifier). Specify either timeSeriesId or propertyAlias, but not both. Returns only jobs analyzing the specified time series.</p>
            status: <p>Filter by job status. Returns only jobs in the specified status. Use RUNNING to find active jobs, or FAILED to identify jobs requiring attention.</p>
            job_type: <p>Filter by enrichment job type. Currently only EVENT_DETECTION is supported. Use this filter to future-proof queries when additional job types are added.</p>
            start_date: <p>The exclusive start of the date range for filtering jobs by creation time. Jobs created after this timestamp are included. Use ISO 8601 format (e.g., 2024-01-01T00:00:00Z).</p>
            end_date: <p>The inclusive end of the date range for filtering jobs by creation time. Jobs created on or before this timestamp are included. Use ISO 8601 format (e.g., 2024-01-31T23:59:59Z).</p>
            max_results: <p>Maximum number of jobs to return per page. Defaults to 50 if not specified. Use smaller values for faster responses, larger values to reduce API calls.</p>
            next_token: <p>Pagination token from a previous ListEnrichmentJobs response. Include this token to retrieve the next page of results. Omit for the first request.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_enrichment_jobs_request.ListEnrichmentJobsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_enrichment_jobs_response.ListEnrichmentJobsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_enrichment_jobs

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_enrichment_jobs.async_list_enrichment_jobs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_enrichment_jobs_request.ListEnrichmentJobsRequest = {
            "workspace_name": workspace_name
        }
        if dataset_id is not None:
            input_["dataset_id"] = dataset_id
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if time_series_id is not None:
            input_["time_series_id"] = time_series_id
        if status is not None:
            input_["status"] = status
        if job_type is not None:
            input_["job_type"] = job_type
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
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

    async def iter_list_enrichment_jobs(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dataset_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.asset_property_alias.AssetPropertyAlias"
        ] = None,
        time_series_id: Optional[
            "capo_iotsitewise.types.time_series_id.TimeSeriesId"
        ] = None,
        status: Optional[
            "capo_iotsitewise.types.enrichment_job_status.EnrichmentJobStatus"
        ] = None,
        job_type: Optional["capo_iotsitewise.types.job_type.JobType"] = None,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.enrichment_job_summary.EnrichmentJobSummary]":
        _token = next_token
        while True:
            _response = await self.list_enrichment_jobs(
                workspace_name,
                config_overrides=config_overrides,
                dataset_id=dataset_id,
                property_alias=property_alias,
                time_series_id=time_series_id,
                status=status,
                job_type=job_type,
                start_date=start_date,
                end_date=end_date,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_executions(
        self,
        target_resource_type: "capo_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        resolve_to_resource_type: Optional[
            "capo_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        action_type: Optional["capo_iotsitewise.types.name.Name"] = None,
    ) -> "capo_iotsitewise.types.list_executions_response.ListExecutionsResponse":
        """<p>Retrieves a paginated list of summaries of all executions.</p>

        Args:
            target_resource_type: <p>The type of the target resource.</p>
            target_resource_id: <p>The ID of the target resource.</p>
            resolve_to_resource_type: <p>The type of the resolved resource.</p>
            resolve_to_resource_id: <p>The ID of the resolved resource.</p>
            next_token: <p>The token used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results returned for each paginated request.</p>
            action_type: <p>The type of action exectued.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_executions_request.ListExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_executions_response.ListExecutionsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_executions

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_executions.async_list_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_executions_request.ListExecutionsRequest = {
            "target_resource_type": target_resource_type,
            "target_resource_id": target_resource_id,
        }
        if resolve_to_resource_type is not None:
            input_["resolve_to_resource_type"] = resolve_to_resource_type
        if resolve_to_resource_id is not None:
            input_["resolve_to_resource_id"] = resolve_to_resource_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if action_type is not None:
            input_["action_type"] = action_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_executions(
        self,
        target_resource_type: "capo_iotsitewise.types.target_resource_type.TargetResourceType",
        target_resource_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        resolve_to_resource_type: Optional[
            "capo_iotsitewise.types.resolve_to_resource_type.ResolveToResourceType"
        ] = None,
        resolve_to_resource_id: Optional["capo_iotsitewise.types.id.ID"] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        action_type: Optional["capo_iotsitewise.types.name.Name"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.execution_summary.ExecutionSummary]":
        _token = next_token
        while True:
            _response = await self.list_executions(
                target_resource_type,
                target_resource_id,
                config_overrides=config_overrides,
                resolve_to_resource_type=resolve_to_resource_type,
                resolve_to_resource_id=resolve_to_resource_id,
                next_token=_token,
                max_results=max_results,
                action_type=action_type,
            )
            _page = _resolve_path(_response, ("execution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_gateways(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_gateways_response.ListGatewaysResponse":
        """<p>Retrieves a paginated list of gateways.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_gateways_request.ListGatewaysRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_gateways_response.ListGatewaysResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_gateways

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_gateways.async_list_gateways(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_gateways_request.ListGatewaysRequest = {}
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

    async def iter_list_gateways(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.gateway_summary.GatewaySummary]":
        _token = next_token
        while True:
            _response = await self.list_gateways(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("gateway_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_interface_relationships(
        self,
        interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_interface_relationships_response.ListInterfaceRelationshipsResponse":
        """<p>Retrieves a paginated list of asset models that have a specific interface asset model applied to them.</p>

        Args:
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_interface_relationships_request.ListInterfaceRelationshipsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_interface_relationships_response.ListInterfaceRelationshipsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_interface_relationships

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_interface_relationships.async_list_interface_relationships(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_interface_relationships_request.ListInterfaceRelationshipsRequest = {
            "interface_asset_model_id": interface_asset_model_id
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

    async def iter_list_interface_relationships(
        self,
        interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.interface_relationship_summary.InterfaceRelationshipSummary]":
        _token = next_token
        while True:
            _response = await self.list_interface_relationships(
                interface_asset_model_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("interface_relationship_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipeline_executions(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_pipeline_executions_request_max_results_integer.ListPipelineExecutionsRequestMaxResultsInteger"
        ] = None,
        state: Optional[
            "capo_iotsitewise.types.pipeline_execution_state.PipelineExecutionState"
        ] = None,
        start_time_after: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        start_time_before: Optional[
            "capo_iotsitewise.types.timestamp.Timestamp"
        ] = None,
        end_time_after: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        end_time_before: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
    ) -> "capo_iotsitewise.types.list_pipeline_executions_response.ListPipelineExecutionsResponse":
        """<p>Lists pipeline executions for a specific pipeline in a workspace. Supports filtering by state and time range. State can be combined with either startTime or endTime filters. Time range filters are grouped: use startTime filters (startTimeAfter, startTimeBefore) or endTime filters (endTimeAfter, endTimeBefore), but not both. Combining startTime and endTime filters returns an InvalidRequestException. Note: endTime filters only return executions in terminal states, as in-progress executions have no endTime.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            pipeline_name: <p>The name of the pipeline.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return per request. This is an upper bound; the actual number of results may be less. Default: 50.</p>
            state: <p>Filter by execution state. If not specified, executions in all states are returned.</p>
            start_time_after: <p>Inclusive lower bound on execution start time (ISO-8601). Only executions with startTime &gt;= startTimeAfter are returned. Cannot be combined with endTimeAfter or endTimeBefore.</p>
            start_time_before: <p>Exclusive upper bound on execution start time (ISO-8601). Only executions with startTime &lt; startTimeBefore are returned. Cannot be combined with endTimeAfter or endTimeBefore.</p>
            end_time_after: <p>Inclusive lower bound on execution end time (ISO-8601). Only executions with endTime &gt;= endTimeAfter are returned. Cannot be combined with startTimeAfter or startTimeBefore. Only matches executions in terminal states.</p>
            end_time_before: <p>Exclusive upper bound on execution end time (ISO-8601). Only executions with endTime &lt; endTimeBefore are returned. Cannot be combined with startTimeAfter or startTimeBefore. Only matches executions in terminal states.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_pipeline_executions_request.ListPipelineExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_pipeline_executions_response.ListPipelineExecutionsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_pipeline_executions

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_pipeline_executions.async_list_pipeline_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_pipeline_executions_request.ListPipelineExecutionsRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if state is not None:
            input_["state"] = state
        if start_time_after is not None:
            input_["start_time_after"] = start_time_after
        if start_time_before is not None:
            input_["start_time_before"] = start_time_before
        if end_time_after is not None:
            input_["end_time_after"] = end_time_after
        if end_time_before is not None:
            input_["end_time_before"] = end_time_before

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_pipeline_executions(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_pipeline_executions_request_max_results_integer.ListPipelineExecutionsRequestMaxResultsInteger"
        ] = None,
        state: Optional[
            "capo_iotsitewise.types.pipeline_execution_state.PipelineExecutionState"
        ] = None,
        start_time_after: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        start_time_before: Optional[
            "capo_iotsitewise.types.timestamp.Timestamp"
        ] = None,
        end_time_after: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
        end_time_before: Optional["capo_iotsitewise.types.timestamp.Timestamp"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.pipeline_execution_summary.PipelineExecutionSummary]":
        _token = next_token
        while True:
            _response = await self.list_pipeline_executions(
                workspace_name,
                pipeline_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                state=state,
                start_time_after=start_time_after,
                start_time_before=start_time_before,
                end_time_after=end_time_after,
                end_time_before=end_time_before,
            )
            _page = _resolve_path(_response, ("pipeline_execution_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_pipelines(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_pipelines_request_max_results_integer.ListPipelinesRequestMaxResultsInteger"
        ] = None,
    ) -> "capo_iotsitewise.types.list_pipelines_response.ListPipelinesResponse":
        """<p>Lists pipelines in a workspace. To get complete details about a pipeline, use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribePipeline.html">DescribePipeline</a>.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. Default: 50.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_pipelines_request.ListPipelinesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_pipelines_response.ListPipelinesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_pipelines

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_pipelines.async_list_pipelines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_pipelines_request.ListPipelinesRequest = {
            "workspace_name": workspace_name
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

    async def iter_list_pipelines(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_pipelines_request_max_results_integer.ListPipelinesRequestMaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.pipeline_summary.PipelineSummary]":
        _token = next_token
        while True:
            _response = await self.list_pipelines(
                workspace_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("pipeline_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_portals(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_portals_response.ListPortalsResponse":
        """<p>Retrieves a paginated list of IoT SiteWise Monitor portals.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_portals_request.ListPortalsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_portals_response.ListPortalsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_portals

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_portals.async_list_portals(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_portals_request.ListPortalsRequest = {}
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

    async def iter_list_portals(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.portal_summary.PortalSummary]":
        _token = next_token
        while True:
            _response = await self.list_portals(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("portal_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_project_assets(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_iotsitewise.types.list_project_assets_response.ListProjectAssetsResponse"
    ):
        """<p>Retrieves a paginated list of assets associated with an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_project_assets_request.ListProjectAssetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_project_assets_response.ListProjectAssetsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_project_assets

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_project_assets.async_list_project_assets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_project_assets_request.ListProjectAssetsRequest = {
            "project_id": project_id
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

    async def iter_list_project_assets(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.id.ID]":
        _token = next_token
        while True:
            _response = await self.list_project_assets(
                project_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("asset_ids",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_projects(
        self,
        portal_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_projects_response.ListProjectsResponse":
        """<p>Retrieves a paginated list of projects for an IoT SiteWise Monitor portal.</p>

        Args:
            portal_id: <p>The ID of the portal.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p> <p>Default: 50</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_projects_request.ListProjectsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_projects_response.ListProjectsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_projects

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_projects.async_list_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_projects_request.ListProjectsRequest = {
            "portal_id": portal_id
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

    async def iter_list_projects(
        self,
        portal_id: "capo_iotsitewise.types.id.ID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.project_summary.ProjectSummary]":
        _token = next_token
        while True:
            _response = await self.list_projects(
                portal_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("project_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_queries(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        filter: Optional["capo_iotsitewise.types.query_filter.QueryFilter"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.query_max_results.QueryMaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsitewise.types.query_list_next_token.QueryListNextToken"
        ] = None,
    ) -> "capo_iotsitewise.types.list_queries_response.ListQueriesResponse":
        """<p>Retrieves a paginated list of queries for a workspace.</p>

        Args:
            workspace_name: <p>The name of the workspace to list queries for.</p>
            filter: <p>An optional filter to return only queries with the specified status. The value must be one of the supported query statuses: SUBMITTED, RUNNING, COMPLETED, FAILED, CANCELED, or CANCELING.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_queries_request.ListQueriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_queries_response.ListQueriesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_queries

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_queries.async_list_queries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_queries_request.ListQueriesRequest = {
            "workspace_name": workspace_name
        }
        if filter is not None:
            input_["filter"] = filter
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

    async def iter_list_queries(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        filter: Optional["capo_iotsitewise.types.query_filter.QueryFilter"] = None,
        max_results: Optional[
            "capo_iotsitewise.types.query_max_results.QueryMaxResults"
        ] = None,
        next_token: Optional[
            "capo_iotsitewise.types.query_list_next_token.QueryListNextToken"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.query_summary.QuerySummary]":
        _token = next_token
        while True:
            _response = await self.list_queries(
                workspace_name,
                config_overrides=config_overrides,
                filter=filter,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("queries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_searches(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_searches_request_max_results_integer.ListSearchesRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        list_searches_filters: Optional[
            "capo_iotsitewise.types.list_searches_filters.ListSearchesFilters"
        ] = None,
    ) -> "capo_iotsitewise.types.list_searches_response.ListSearchesResponse":
        """<p>Lists the searches in a workspace, most recently started first. Results can be narrowed with optional filters (status, search type, group, and started-at time range) and are paginated: when <code>nextToken</code> is present, pass it on a subsequent call to retrieve the next page.</p>

        Args:
            workspace_name: <p>The name of the workspace whose searches are listed.</p>
            max_results: <p>The maximum number of searches to return in a single page. Valid range is 1 to 1,000; if omitted, a service-defined default is used.</p>
            next_token: <p>The pagination token returned by a previous ListSearches call. Provide it to retrieve the next page; omit it to retrieve the first page.</p>
            list_searches_filters: <p>Optional filters that restrict which searches are returned.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_searches_request.ListSearchesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_searches_response.ListSearchesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_searches

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_searches.async_list_searches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_searches_request.ListSearchesRequest = {
            "workspace_name": workspace_name
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if list_searches_filters is not None:
            input_["list_searches_filters"] = list_searches_filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_searches(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_searches_request_max_results_integer.ListSearchesRequestMaxResultsInteger"
        ] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        list_searches_filters: Optional[
            "capo_iotsitewise.types.list_searches_filters.ListSearchesFilters"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.search_summary.SearchSummary]":
        _token = next_token
        while True:
            _response = await self.list_searches(
                workspace_name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                list_searches_filters=list_searches_filters,
            )
            _page = _resolve_path(_response, ("search_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_arn: "capo_iotsitewise.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Retrieves the list of tags for an IoT SiteWise resource.</p>

        Args:
            resource_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tasks(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_tasks_request_max_results_integer.ListTasksRequestMaxResultsInteger"
        ] = None,
    ) -> "capo_iotsitewise.types.list_tasks_response.ListTasksResponse":
        """<p>Lists tasks in a workspace. To get complete details about a task, use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeTask.html">DescribeTask</a>.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. Default: 50.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_tasks_request.ListTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_tasks_response.ListTasksResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_tasks

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_tasks.async_list_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_tasks_request.ListTasksRequest = {
            "workspace_name": workspace_name
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

    async def iter_list_tasks(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional[
            "capo_iotsitewise.types.pagination_token.PaginationToken"
        ] = None,
        max_results: Optional[
            "capo_iotsitewise.types.list_tasks_request_max_results_integer.ListTasksRequestMaxResultsInteger"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.task_summary.TaskSummary]":
        _token = next_token
        while True:
            _response = await self.list_tasks(
                workspace_name,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("task_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        alias_prefix: Optional[
            "capo_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        time_series_type: Optional[
            "capo_iotsitewise.types.list_time_series_type.ListTimeSeriesType"
        ] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "capo_iotsitewise.types.list_time_series_response.ListTimeSeriesResponse":
        """<p>Retrieves a paginated list of time series (data streams).</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request.</p>
            asset_id: <p>The ID of the asset in which the asset property was created. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            alias_prefix: <p>The alias prefix of the time series.</p>
            time_series_type: <p>The type of the time series. The time series type can be one of the following values:</p> <ul> <li> <p> <code>ASSOCIATED</code> – The time series is associated with an asset property.</p> </li> <li> <p> <code>DISASSOCIATED</code> – The time series isn't associated with any asset property.</p> </li> </ul>
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_time_series_request.ListTimeSeriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_time_series_response.ListTimeSeriesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_time_series

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_time_series.async_list_time_series(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_time_series_request.ListTimeSeriesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if asset_id is not None:
            input_["asset_id"] = asset_id
        if alias_prefix is not None:
            input_["alias_prefix"] = alias_prefix
        if time_series_type is not None:
            input_["time_series_type"] = time_series_type
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_time_series(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
        asset_id: Optional["capo_iotsitewise.types.custom_id.CustomID"] = None,
        alias_prefix: Optional[
            "capo_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        time_series_type: Optional[
            "capo_iotsitewise.types.list_time_series_type.ListTimeSeriesType"
        ] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.time_series_summary.TimeSeriesSummary]":
        _token = next_token
        while True:
            _response = await self.list_time_series(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                asset_id=asset_id,
                alias_prefix=alias_prefix,
                time_series_type=time_series_type,
                workspace_name=workspace_name,
            )
            _page = _resolve_path(_response, ("time_series_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "capo_iotsitewise.types.list_workspaces_response.ListWorkspacesResponse":
        """<p>Retrieves a paginated list of workspaces. Use the <code>nextToken</code> parameter to retrieve additional results.</p>

        Args:
            next_token: <p>The token to be used for the next set of paginated results.</p>
            max_results: <p>The maximum number of results to return for each paginated request. Default: 50.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.list_workspaces_request.ListWorkspacesRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.list_workspaces_response.ListWorkspacesResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.list_workspaces

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.list_workspaces.async_list_workspaces(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.list_workspaces_request.ListWorkspacesRequest = {}
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

    async def iter_list_workspaces(
        self,
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        next_token: Optional["capo_iotsitewise.types.next_token.NextToken"] = None,
        max_results: Optional["capo_iotsitewise.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_iotsitewise.types.workspace_summary.WorkspaceSummary]":
        _token = next_token
        while True:
            _response = await self.list_workspaces(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workspace_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def put_asset_model_interface_relationship(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        interface_asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        property_mapping_configuration: "capo_iotsitewise.types.property_mapping_configuration.PropertyMappingConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.put_asset_model_interface_relationship_response.PutAssetModelInterfaceRelationshipResponse":
        """<p>Creates or updates an interface relationship between an asset model and an interface asset model. This operation applies an interface to an asset model.</p>

        Args:
            asset_model_id: <p>The ID of the asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            interface_asset_model_id: <p>The ID of the interface asset model. This can be either the actual ID in UUID format, or else externalId: followed by the external ID.</p>
            property_mapping_configuration: <p>The configuration for mapping properties from the interface asset model to the asset model where the interface is applied. This configuration controls how properties are matched and created during the interface application process.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.put_asset_model_interface_relationship_request.PutAssetModelInterfaceRelationshipRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.put_asset_model_interface_relationship_response.PutAssetModelInterfaceRelationshipResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.put_asset_model_interface_relationship

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.put_asset_model_interface_relationship.async_put_asset_model_interface_relationship(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.put_asset_model_interface_relationship_request.PutAssetModelInterfaceRelationshipRequest = {
            "asset_model_id": asset_model_id,
            "interface_asset_model_id": interface_asset_model_id,
            "property_mapping_configuration": property_mapping_configuration,
        }
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

    async def put_default_encryption_configuration(
        self,
        encryption_type: "capo_iotsitewise.types.encryption_type.EncryptionType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        kms_key_id: Optional["capo_iotsitewise.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_iotsitewise.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse":
        """<p>Sets the default encryption configuration for the Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/key-management.html">Key management</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            encryption_type: <p>The type of encryption used for the encryption configuration.</p>
            kms_key_id: <p>The Key ID of the customer managed key used for KMS encryption. This is required if you use <code>KMS_BASED_ENCRYPTION</code>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.put_default_encryption_configuration_response.PutDefaultEncryptionConfigurationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.put_default_encryption_configuration

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.put_default_encryption_configuration.async_put_default_encryption_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.put_default_encryption_configuration_request.PutDefaultEncryptionConfigurationRequest = {
            "encryption_type": encryption_type
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_logging_options(
        self,
        logging_options: "capo_iotsitewise.types.logging_options.LoggingOptions",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
    ) -> (
        "capo_iotsitewise.types.put_logging_options_response.PutLoggingOptionsResponse"
    ):
        """<p>Sets logging options for IoT SiteWise.</p>

        Args:
            logging_options: <p>The logging options to set.</p>
            workspace_name: <p>The name of the workspace.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.put_logging_options_request.PutLoggingOptionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.put_logging_options_response.PutLoggingOptionsResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.put_logging_options

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.put_logging_options.async_put_logging_options(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.put_logging_options_request.PutLoggingOptionsRequest = {
            "logging_options": logging_options
        }
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_storage_configuration(
        self,
        storage_type: "capo_iotsitewise.types.storage_type.StorageType",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        multi_layer_storage: Optional[
            "capo_iotsitewise.types.multi_layer_storage.MultiLayerStorage"
        ] = None,
        disassociated_data_storage: Optional[
            "capo_iotsitewise.types.disassociated_data_storage_state.DisassociatedDataStorageState"
        ] = None,
        retention_period: Optional[
            "capo_iotsitewise.types.retention_period.RetentionPeriod"
        ] = None,
        warm_tier: Optional[
            "capo_iotsitewise.types.warm_tier_state.WarmTierState"
        ] = None,
        warm_tier_retention_period: Optional[
            "capo_iotsitewise.types.warm_tier_retention_period.WarmTierRetentionPeriod"
        ] = None,
        disallow_ingest_null_na_n: Optional[
            "capo_iotsitewise.types.disallow_ingest_null_na_n.DisallowIngestNullNaN"
        ] = None,
    ) -> "capo_iotsitewise.types.put_storage_configuration_response.PutStorageConfigurationResponse":
        """<p>Configures storage settings for IoT SiteWise.</p>

        Args:
            storage_type: <p>The storage tier that you specified for your data. The <code>storageType</code> parameter can be one of the following values:</p> <ul> <li> <p> <code>SITEWISE_DEFAULT_STORAGE</code> – IoT SiteWise saves your data into the hot tier. The hot tier is a service-managed database.</p> </li> <li> <p> <code>MULTI_LAYER_STORAGE</code> – IoT SiteWise saves your data in both the cold tier and the hot tier. The cold tier is a customer-managed Amazon S3 bucket.</p> </li> </ul>
            multi_layer_storage: <p>Identifies a storage destination. If you specified <code>MULTI_LAYER_STORAGE</code> for the storage type, you must specify a <code>MultiLayerStorage</code> object.</p>
            disassociated_data_storage: <p>Contains the storage configuration for time series (data streams) that aren't associated with asset properties. The <code>disassociatedDataStorage</code> can be one of the following values:</p> <ul> <li> <p> <code>ENABLED</code> – IoT SiteWise accepts time series that aren't associated with asset properties.</p> <important> <p>After the <code>disassociatedDataStorage</code> is enabled, you can't disable it.</p> </important> </li> <li> <p> <code>DISABLED</code> – IoT SiteWise doesn't accept time series (data streams) that aren't associated with asset properties.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/data-streams.html">Data streams</a> in the <i>IoT SiteWise User Guide</i>.</p>
            warm_tier: <p>A service managed storage tier optimized for analytical queries. It stores periodically uploaded, buffered and historical data ingested with the CreaeBulkImportJob API.</p>
            warm_tier_retention_period: <p>Set this period to specify how long your data is stored in the warm tier before it is deleted. You can set this only if cold tier is enabled.</p>
            disallow_ingest_null_na_n: <p>Describes the configuration for ingesting NULL and NaN data. By default the feature is allowed. The feature is disallowed if the value is <code>true</code>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.put_storage_configuration_request.PutStorageConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.put_storage_configuration_response.PutStorageConfigurationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.put_storage_configuration

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.put_storage_configuration.async_put_storage_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.put_storage_configuration_request.PutStorageConfigurationRequest = {
            "storage_type": storage_type
        }
        if multi_layer_storage is not None:
            input_["multi_layer_storage"] = multi_layer_storage
        if disassociated_data_storage is not None:
            input_["disassociated_data_storage"] = disassociated_data_storage
        if retention_period is not None:
            input_["retention_period"] = retention_period
        if warm_tier is not None:
            input_["warm_tier"] = warm_tier
        if warm_tier_retention_period is not None:
            input_["warm_tier_retention_period"] = warm_tier_retention_period
        if disallow_ingest_null_na_n is not None:
            input_["disallow_ingest_null_na_n"] = disallow_ingest_null_na_n

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_pipeline_execution(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        execution_environment_variable_overrides: Optional[
            "capo_iotsitewise.types.execution_environment_variables.ExecutionEnvironmentVariables"
        ] = None,
        execution_mount_overrides: Optional[
            "capo_iotsitewise.types.mount_overrides.MountOverrides"
        ] = None,
        execution_priority: Optional[
            "capo_iotsitewise.types.execution_priority.ExecutionPriority"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.start_pipeline_execution_response.StartPipelineExecutionResponse":
        """<p>Starts execution of a pipeline in the specified workspace. Each compute node runs according to the DAG dependency order defined in the pipeline. Nodes without dependencies start immediately, while dependent nodes wait for all upstream nodes to complete successfully.</p> <p>You can provide runtime environment variable overrides that take the highest priority in the environment variable hierarchy, without modifying the pipeline definition.</p>

        Args:
            workspace_name: <p>The name of the workspace containing the pipeline.</p>
            pipeline_name: <p>The name of the pipeline to execute.</p>
            execution_environment_variable_overrides: <p>Runtime environment variable overrides for the execution. Includes global variables that apply to all compute nodes and computeNodes for per-node overrides. These take the highest priority in the environment variable hierarchy.</p>
            execution_mount_overrides: <p>Runtime mount overrides for the execution. Overrides are merged by mount name into each listed compute node's task-defined mounts: a matching name replaces the task-defined mount, a new name adds a mount, and task-defined mounts not referenced remain unchanged. Compute nodes not listed use their task-defined mounts as-is.</p>
            execution_priority: <p>Scheduling priority for the execution. Lower values indicate higher priority. Defaults to 2 when not specified.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token, the server returns the cached result from the original successful request without performing the operation again.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.start_pipeline_execution_request.StartPipelineExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.start_pipeline_execution_response.StartPipelineExecutionResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.start_pipeline_execution

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.start_pipeline_execution.async_start_pipeline_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.start_pipeline_execution_request.StartPipelineExecutionRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
        }
        if execution_environment_variable_overrides is not None:
            input_["execution_environment_variable_overrides"] = (
                execution_environment_variable_overrides
            )
        if execution_mount_overrides is not None:
            input_["execution_mount_overrides"] = execution_mount_overrides
        if execution_priority is not None:
            input_["execution_priority"] = execution_priority
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

    async def start_query(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        query_statement: "capo_iotsitewise.types.query_string.QueryString",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.start_query_response.StartQueryResponse":
        """<p>Starts an asynchronous SQL query against workspace telemetry, annotations, data segment, and dataset data.</p>

        Args:
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            workspace_name: <p>The name of the workspace to query.</p>
            query_statement: <p>The SQL query to execute against the workspace telemetry, annotations, data segment, and dataset data.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.start_query_request.StartQueryRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.start_query_response.StartQueryResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.start_query

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.start_query.async_start_query(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.start_query_request.StartQueryRequest = {
            "workspace_name": workspace_name,
            "query_statement": query_statement,
        }
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

    async def start_search(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        query_statement: "capo_iotsitewise.types.search_query_statement.SearchQueryStatement",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        search_type: Optional["capo_iotsitewise.types.search_type.SearchType"] = None,
        search_filters: Optional[
            "capo_iotsitewise.types.search_filters.SearchFilters"
        ] = None,
        group_id: Optional["capo_iotsitewise.types.group_id.GroupId"] = None,
    ) -> "capo_iotsitewise.types.start_search_response.StartSearchResponse":
        """<p>Starts an asynchronous search over the data in a workspace. The search runs in the background; the response returns immediately with a <code>searchId</code> and an initial status of <code>QUEUED</code>. Use <code>DescribeSearch</code> to poll for completion and <code>GetSearchResults</code> to retrieve the results once the search reaches <code>SUCCEEDED</code>. The request is idempotent on <code>clientToken</code>: repeating a call with the same token returns the original search instead of starting a new one.</p>

        Args:
            workspace_name: <p>The name of the workspace whose data is searched.</p>
            query_statement: <p>The natural-language query describing the data to search for.</p>
            client_token: <p>A unique, case-sensitive identifier you provide to ensure the request is idempotent. Repeating a StartSearch call with the same <code>clientToken</code> returns the original search rather than starting a new one. If omitted, the SDK autogenerates one.</p>
            search_type: <p>The search strategy to use. Defaults to <code>QUICK</code> when omitted.</p>
            search_filters: <p>Optional filters that restrict the search to a subset of the workspace's data.</p>
            group_id: <p>An optional caller-supplied identifier used to group related searches together.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.start_search_request.StartSearchRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.start_search_response.StartSearchResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.start_search

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.start_search.async_start_search(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.start_search_request.StartSearchRequest = {
            "workspace_name": workspace_name,
            "query_statement": query_statement,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if search_type is not None:
            input_["search_type"] = search_type
        if search_filters is not None:
            input_["search_filters"] = search_filters
        if group_id is not None:
            input_["group_id"] = group_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def tag_resource(
        self,
        resource_arn: "capo_iotsitewise.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_iotsitewise.types.tag_map.TagMap",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to an IoT SiteWise resource. If a tag already exists for the resource, this operation updates the tag's value.</p>

        Args:
            resource_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource to tag.</p>
            tags: <p>A list of key-value pairs that contain metadata for the resource. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/tag-resources.html">Tagging your IoT SiteWise resources</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.too_many_tags_exception.TooManyTagsException: <p>You've reached the quota for the number of tags allowed for a resource. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html#tag-conventions">Tag naming limits and requirements</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_iotsitewise.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.tag_resource_request.TagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.tag_resource

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.tag_resource.async_tag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_iotsitewise.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_iotsitewise.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from an IoT SiteWise resource.</p>

        Args:
            resource_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of the resource to untag.</p>
            tag_keys: <p>A list of keys for tags to remove from the resource.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.unauthorized_exception.UnauthorizedException: <p>You are not authorized.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.untag_resource_request.UntagResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.untag_resource

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.untag_resource.async_untag_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.untag_resource_request.UntagResourceRequest = {
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

    async def update_access_policy(
        self,
        access_policy_id: "capo_iotsitewise.types.id.ID",
        access_policy_identity: "capo_iotsitewise.types.identity.Identity",
        access_policy_resource: "capo_iotsitewise.types.resource.Resource",
        access_policy_permission: "capo_iotsitewise.types.permission.Permission",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.update_access_policy_response.UpdateAccessPolicyResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Updates an existing access policy that specifies an identity's access to an IoT SiteWise Monitor portal or project resource.</p>

        Args:
            access_policy_id: <p>The ID of the access policy.</p>
            access_policy_identity: <p>The identity for this access policy. Choose an IAM Identity Center user, an IAM Identity Center group, or an IAM user.</p>
            access_policy_resource: <p>The IoT SiteWise Monitor resource for this access policy. Choose either a portal or a project.</p>
            access_policy_permission: <p>The permission level for this access policy. Note that a project <code>ADMINISTRATOR</code> is also known as a project owner.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_access_policy_request.UpdateAccessPolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_access_policy_response.UpdateAccessPolicyResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_access_policy

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_access_policy.async_update_access_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_access_policy_request.UpdateAccessPolicyRequest = {
            "access_policy_id": access_policy_id,
            "access_policy_identity": access_policy_identity,
            "access_policy_resource": access_policy_resource,
            "access_policy_permission": access_policy_permission,
        }
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

    async def update_asset(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_name: "capo_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_external_id: Optional[
            "capo_iotsitewise.types.external_id.ExternalId"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        asset_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
    ) -> "capo_iotsitewise.types.update_asset_response.UpdateAssetResponse":
        """<p>Updates an asset's name. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html">Updating assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Args:
            asset_id: <p>The ID of the asset to update. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_external_id: <p>An external ID to assign to the asset. The asset must not already have an external ID. The external ID must be unique within your Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_name: <p>A friendly name for the asset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            asset_description: <p>A description for the asset.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_asset_request.UpdateAssetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_asset_response.UpdateAssetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_asset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_asset.async_update_asset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_asset_request.UpdateAssetRequest = {
            "asset_id": asset_id,
            "asset_name": asset_name,
        }
        if asset_external_id is not None:
            input_["asset_external_id"] = asset_external_id
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if asset_description is not None:
            input_["asset_description"] = asset_description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_asset_model(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_model_name: "capo_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_external_id: Optional[
            "capo_iotsitewise.types.external_id.ExternalId"
        ] = None,
        asset_model_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        asset_model_properties: Optional[
            "capo_iotsitewise.types.asset_model_properties.AssetModelProperties"
        ] = None,
        asset_model_hierarchies: Optional[
            "capo_iotsitewise.types.asset_model_hierarchies.AssetModelHierarchies"
        ] = None,
        asset_model_composite_models: Optional[
            "capo_iotsitewise.types.asset_model_composite_models.AssetModelCompositeModels"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        if_match: Optional["capo_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional["capo_iotsitewise.types.select_all.SelectAll"] = None,
        match_for_version_type: Optional[
            "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "capo_iotsitewise.types.update_asset_model_response.UpdateAssetModelResponse":
        """<p>Updates an asset model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model's property and hierarchy definitions. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html">Updating assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p> <important> <p>If you remove a property from an asset model, IoT SiteWise deletes all previous data for that property. You can’t change the type or data type of an existing property.</p> <p>To replace an existing asset model property with a new one with the same <code>name</code>, do the following:</p> <ol> <li> <p>Submit an <code>UpdateAssetModel</code> request with the entire existing property removed.</p> </li> <li> <p>Submit a second <code>UpdateAssetModel</code> request that includes the new property. The new asset property will have the same <code>name</code> as the previous one and IoT SiteWise will generate a new unique <code>id</code>.</p> </li> </ol> </important>

        Args:
            asset_model_id: <p>The ID of the asset model to update. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_external_id: <p>An external ID to assign to the asset model. The asset model must not already have an external ID. The external ID must be unique within your Amazon Web Services account. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids">Using external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_name: <p>A unique name for the asset model.</p>
            asset_model_description: <p>A description for the asset model.</p>
            asset_model_properties: <p>The updated property definitions of the asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-properties.html">Asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_hierarchies: <p>The updated hierarchy definitions of the asset model. Each hierarchy specifies an asset model whose assets can be children of any other assets created from this asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html">Asset hierarchies</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 10 hierarchies per asset model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            asset_model_composite_models: <p>The composite models that are part of this asset model. It groups properties (such as attributes, measurements, transforms, and metrics) and child composite models that model parts of your industrial equipment. Each composite model has a type that defines the properties that the composite model supports. Use composite models to define alarms on this asset model.</p> <note> <p>When creating custom composite models, you need to use <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModelCompositeModel.html">CreateAssetModelCompositeModel</a>. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-custom-composite-models.html">Creating custom composite models (Components)</a> in the <i>IoT SiteWise User Guide</i>.</p> </note>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The update request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the update request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the update operation.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.precondition_failed_exception.PreconditionFailedException: <p>The precondition in one or more of the request-header fields evaluated to <code>FALSE</code>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_asset_model_request.UpdateAssetModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_asset_model_response.UpdateAssetModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_asset_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_asset_model.async_update_asset_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_asset_model_request.UpdateAssetModelRequest = {
            "asset_model_id": asset_model_id,
            "asset_model_name": asset_model_name,
        }
        if asset_model_external_id is not None:
            input_["asset_model_external_id"] = asset_model_external_id
        if asset_model_description is not None:
            input_["asset_model_description"] = asset_model_description
        if asset_model_properties is not None:
            input_["asset_model_properties"] = asset_model_properties
        if asset_model_hierarchies is not None:
            input_["asset_model_hierarchies"] = asset_model_hierarchies
        if asset_model_composite_models is not None:
            input_["asset_model_composite_models"] = asset_model_composite_models
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_asset_model_composite_model(
        self,
        asset_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_id: "capo_iotsitewise.types.custom_id.CustomID",
        asset_model_composite_model_name: "capo_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        asset_model_composite_model_external_id: Optional[
            "capo_iotsitewise.types.external_id.ExternalId"
        ] = None,
        asset_model_composite_model_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        asset_model_composite_model_properties: Optional[
            "capo_iotsitewise.types.asset_model_properties.AssetModelProperties"
        ] = None,
        if_match: Optional["capo_iotsitewise.types.e_tag.ETag"] = None,
        if_none_match: Optional["capo_iotsitewise.types.select_all.SelectAll"] = None,
        match_for_version_type: Optional[
            "capo_iotsitewise.types.asset_model_version_type.AssetModelVersionType"
        ] = None,
    ) -> "capo_iotsitewise.types.update_asset_model_composite_model_response.UpdateAssetModelCompositeModelResponse":
        """<p>Updates a composite model and all of the assets that were created from the model. Each asset created from the model inherits the updated asset model's property and hierarchy definitions. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-assets-and-models.html">Updating assets and models</a> in the <i>IoT SiteWise User Guide</i>.</p> <important> <p>If you remove a property from a composite asset model, IoT SiteWise deletes all previous data for that property. You can’t change the type or data type of an existing property.</p> <p>To replace an existing composite asset model property with a new one with the same <code>name</code>, do the following:</p> <ol> <li> <p>Submit an <code>UpdateAssetModelCompositeModel</code> request with the entire existing property removed.</p> </li> <li> <p>Submit a second <code>UpdateAssetModelCompositeModel</code> request that includes the new property. The new asset property will have the same <code>name</code> as the previous one and IoT SiteWise will generate a new unique <code>id</code>.</p> </li> </ol> </important>

        Args:
            asset_model_id: <p>The ID of the asset model, in UUID format.</p>
            asset_model_composite_model_id: <p>The ID of a composite model on this asset model.</p>
            asset_model_composite_model_external_id: <p>An external ID to assign to the asset model. You can only set the external ID of the asset model if it wasn't set when it was created, or you're setting it to the exact same thing as when it was created.</p>
            asset_model_composite_model_description: <p>A description for the composite model.</p>
            asset_model_composite_model_name: <p>A unique name for the composite model.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            asset_model_composite_model_properties: <p>The property definitions of the composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/custom-composite-models.html#inline-composite-models"> Inline custom composite models</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>You can specify up to 200 properties per composite model. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_match: <p>The expected current entity tag (ETag) for the asset model’s latest or active version (specified using <code>matchForVersionType</code>). The update request is rejected if the tag does not match the latest or active version's current entity tag. See <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html">Optimistic locking for asset model writes</a> in the <i>IoT SiteWise User Guide</i>.</p>
            if_none_match: <p>Accepts <b>*</b> to reject the update request if an active version (specified using <code>matchForVersionType</code> as <code>ACTIVE</code>) already exists for the asset model.</p>
            match_for_version_type: <p>Specifies the asset model version type (<code>LATEST</code> or <code>ACTIVE</code>) used in conjunction with <code>If-Match</code> or <code>If-None-Match</code> headers to determine the target ETag for the update operation.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.precondition_failed_exception.PreconditionFailedException: <p>The precondition in one or more of the request-header fields evaluated to <code>FALSE</code>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_asset_model_composite_model_request.UpdateAssetModelCompositeModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_asset_model_composite_model_response.UpdateAssetModelCompositeModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_asset_model_composite_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_asset_model_composite_model.async_update_asset_model_composite_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_asset_model_composite_model_request.UpdateAssetModelCompositeModelRequest = {
            "asset_model_id": asset_model_id,
            "asset_model_composite_model_id": asset_model_composite_model_id,
            "asset_model_composite_model_name": asset_model_composite_model_name,
        }
        if asset_model_composite_model_external_id is not None:
            input_["asset_model_composite_model_external_id"] = (
                asset_model_composite_model_external_id
            )
        if asset_model_composite_model_description is not None:
            input_["asset_model_composite_model_description"] = (
                asset_model_composite_model_description
            )
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if asset_model_composite_model_properties is not None:
            input_["asset_model_composite_model_properties"] = (
                asset_model_composite_model_properties
            )
        if if_match is not None:
            input_["if_match"] = if_match
        if if_none_match is not None:
            input_["if_none_match"] = if_none_match
        if match_for_version_type is not None:
            input_["match_for_version_type"] = match_for_version_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_asset_property(
        self,
        asset_id: "capo_iotsitewise.types.custom_id.CustomID",
        property_id: "capo_iotsitewise.types.custom_id.CustomID",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        property_alias: Optional[
            "capo_iotsitewise.types.property_alias.PropertyAlias"
        ] = None,
        property_notification_state: Optional[
            "capo_iotsitewise.types.property_notification_state.PropertyNotificationState"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        property_unit: Optional[
            "capo_iotsitewise.types.property_unit.PropertyUnit"
        ] = None,
    ) -> None:
        """<p>Updates an asset property's alias and notification state.</p> <important> <p>This operation overwrites the property's existing alias and notification state. To keep your existing property's alias or notification state, you must include the existing values in the UpdateAssetProperty request. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetProperty.html">DescribeAssetProperty</a>.</p> </important>

        Args:
            asset_id: <p>The ID of the asset to be updated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_id: <p>The ID of the asset property to be updated. This can be either the actual ID in UUID format, or else <code>externalId:</code> followed by the external ID, if it has one. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references">Referencing objects with external IDs</a> in the <i>IoT SiteWise User Guide</i>.</p>
            property_alias: <p>The alias that identifies the property, such as an OPC-UA server data stream path (for example, <code>/company/windfarm/3/turbine/7/temperature</code>). For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html">Mapping industrial data streams to asset properties</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>If you omit this parameter, the alias is removed from the property.</p>
            property_notification_state: <p>The MQTT notification state (enabled or disabled) for this asset property. When the notification state is enabled, IoT SiteWise publishes property value updates to a unique MQTT topic. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/interact-with-other-services.html">Interacting with other services</a> in the <i>IoT SiteWise User Guide</i>.</p> <p>If you omit this parameter, the notification state is set to <code>DISABLED</code>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            property_unit: <p>The unit of measure (such as Newtons or RPM) of the asset property. If you don't specify a value for this parameter, the service uses the value of the <code>assetModelProperty</code> in the asset model.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_asset_property_request.UpdateAssetPropertyRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_asset_property

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_asset_property.async_update_asset_property(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_asset_property_request.UpdateAssetPropertyRequest = {
            "asset_id": asset_id,
            "property_id": property_id,
        }
        if property_alias is not None:
            input_["property_alias"] = property_alias
        if property_notification_state is not None:
            input_["property_notification_state"] = property_notification_state
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if property_unit is not None:
            input_["property_unit"] = property_unit

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_computation_model(
        self,
        computation_model_id: "capo_iotsitewise.types.id.ID",
        computation_model_name: "capo_iotsitewise.types.restricted_name.RestrictedName",
        computation_model_configuration: "capo_iotsitewise.types.computation_model_configuration.ComputationModelConfiguration",
        computation_model_data_binding: "capo_iotsitewise.types.computation_model_data_binding.ComputationModelDataBinding",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        computation_model_description: Optional[
            "capo_iotsitewise.types.restricted_description.RestrictedDescription"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.update_computation_model_response.UpdateComputationModelResponse":
        """<p>Updates the computation model.</p>

        Args:
            computation_model_id: <p>The ID of the computation model.</p>
            computation_model_name: <p>The name of the computation model.</p>
            computation_model_description: <p>The description of the computation model.</p>
            computation_model_configuration: <p>The configuration for the computation model.</p>
            computation_model_data_binding: <p>The data binding for the computation model. Key is a variable name defined in configuration. Value is a <code>ComputationModelDataBindingValue</code> referenced by the variable.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_computation_model_request.UpdateComputationModelRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_computation_model_response.UpdateComputationModelResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_computation_model

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_computation_model.async_update_computation_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_computation_model_request.UpdateComputationModelRequest = {
            "computation_model_id": computation_model_id,
            "computation_model_name": computation_model_name,
            "computation_model_configuration": computation_model_configuration,
            "computation_model_data_binding": computation_model_data_binding,
        }
        if computation_model_description is not None:
            input_["computation_model_description"] = computation_model_description
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

    async def update_dashboard(
        self,
        dashboard_id: "capo_iotsitewise.types.id.ID",
        dashboard_name: "capo_iotsitewise.types.name.Name",
        dashboard_definition: "capo_iotsitewise.types.dashboard_definition.DashboardDefinition",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        dashboard_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.update_dashboard_response.UpdateDashboardResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Updates an IoT SiteWise Monitor dashboard.</p>

        Args:
            dashboard_id: <p>The ID of the dashboard to update.</p>
            dashboard_name: <p>A new friendly name for the dashboard.</p>
            dashboard_description: <p>A new description for the dashboard.</p>
            dashboard_definition: <p>The new dashboard definition, as specified in a JSON literal.</p> <ul> <li> <p>IoT SiteWise Monitor (Classic) see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-using-aws-cli.html">Create dashboards (CLI)</a> </p> </li> <li> <p>IoT SiteWise Monitor (AI-aware) see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/create-dashboards-ai-dashboard-cli.html">Create dashboards (CLI)</a> </p> </li> </ul> <p>in the <i>IoT SiteWise User Guide</i> </p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_dashboard_request.UpdateDashboardRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_dashboard_response.UpdateDashboardResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_dashboard

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_dashboard.async_update_dashboard(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_dashboard_request.UpdateDashboardRequest = {
            "dashboard_id": dashboard_id,
            "dashboard_name": dashboard_name,
            "dashboard_definition": dashboard_definition,
        }
        if dashboard_description is not None:
            input_["dashboard_description"] = dashboard_description
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

    async def update_dataset(
        self,
        dataset_id: "capo_iotsitewise.types.id.ID",
        dataset_name: "capo_iotsitewise.types.restricted_name.RestrictedName",
        dataset_source: "capo_iotsitewise.types.dataset_source.DatasetSource",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_name: Optional[
            "capo_iotsitewise.types.workspace_name.WorkspaceName"
        ] = None,
        dataset_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        dataset_config: Optional[
            "capo_iotsitewise.types.dataset_config.DatasetConfig"
        ] = None,
        metadata: Optional["capo_iotsitewise.types.metadata.Metadata"] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.update_dataset_response.UpdateDatasetResponse":
        """<p>Updates a dataset.</p>

        Args:
            dataset_id: <p>The ID of the dataset.</p>
            workspace_name: <p>The name of the workspace that contains the dataset.</p>
            dataset_name: <p>The name of the dataset.</p>
            dataset_description: <p>A description about the dataset, and its functionality.</p>
            dataset_config: <p>The updated configuration for the dataset.</p>
            metadata: <p>The updated metadata for the dataset.</p>
            dataset_source: <p>The data source for the dataset.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The resource already exists.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_dataset_request.UpdateDatasetRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_dataset_response.UpdateDatasetResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_dataset

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_dataset.async_update_dataset(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_dataset_request.UpdateDatasetRequest = {
            "dataset_id": dataset_id,
            "dataset_name": dataset_name,
            "dataset_source": dataset_source,
        }
        if workspace_name is not None:
            input_["workspace_name"] = workspace_name
        if dataset_description is not None:
            input_["dataset_description"] = dataset_description
        if dataset_config is not None:
            input_["dataset_config"] = dataset_config
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

    async def update_gateway(
        self,
        gateway_id: "capo_iotsitewise.types.id.ID",
        gateway_name: "capo_iotsitewise.types.gateway_name.GatewayName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> None:
        """<p>Updates a gateway's name.</p>

        Args:
            gateway_id: <p>The ID of the gateway to update.</p>
            gateway_name: <p>A unique name for the gateway.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_gateway_request.UpdateGatewayRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_gateway

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_gateway.async_update_gateway(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_gateway_request.UpdateGatewayRequest = {
            "gateway_id": gateway_id,
            "gateway_name": gateway_name,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_gateway_capability_configuration(
        self,
        gateway_id: "capo_iotsitewise.types.id.ID",
        capability_namespace: "capo_iotsitewise.types.capability_namespace.CapabilityNamespace",
        capability_configuration: "capo_iotsitewise.types.capability_configuration.CapabilityConfiguration",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
    ) -> "capo_iotsitewise.types.update_gateway_capability_configuration_response.UpdateGatewayCapabilityConfigurationResponse":
        """<p>Updates a gateway capability configuration or defines a new capability configuration. Each gateway capability defines data sources for a gateway.</p> <p>Important workflow notes:</p> <p>Each gateway capability defines data sources for a gateway. This is the namespace of the gateway capability.</p> <p>. The namespace follows the format <code>service:capability:version</code>, where:</p> <ul> <li> <p> <code>service</code> - The service providing the capability, or <code>iotsitewise</code>.</p> </li> <li> <p> <code>capability</code> - The specific capability type. Options include: <code>opcuacollector</code> for the OPC UA data source collector, or <code>publisher</code> for data publisher capability.</p> </li> <li> <p> <code>version</code> - The version number of the capability. Option include <code>2</code> for Classic streams, V2 gateways, and <code>3</code> for MQTT-enabled, V3 gateways.</p> </li> </ul> <p>After updating a capability configuration, the sync status becomes <code>OUT_OF_SYNC</code> until the gateway processes the configuration.Use <code>DescribeGatewayCapabilityConfiguration</code> to check the sync status and verify the configuration was applied.</p> <p>A gateway can have multiple capability configurations with different namespaces.</p>

        Args:
            gateway_id: <p>The ID of the gateway to be updated.</p>
            capability_namespace: <p>The namespace of the gateway capability configuration to be updated. For example, if you configure OPC UA sources for an MQTT-enabled gateway, your OPC-UA capability configuration has the namespace <code>iotsitewise:opcuacollector:3</code>.</p>
            capability_configuration: <p>The JSON document that defines the configuration for the gateway capability. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-sources.html#configure-source-cli">Configuring data sources (CLI)</a> in the <i>IoT SiteWise User Guide</i>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_gateway_capability_configuration_request.UpdateGatewayCapabilityConfigurationRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_gateway_capability_configuration_response.UpdateGatewayCapabilityConfigurationResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_gateway_capability_configuration

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_gateway_capability_configuration.async_update_gateway_capability_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_gateway_capability_configuration_request.UpdateGatewayCapabilityConfigurationRequest = {
            "gateway_id": gateway_id,
            "capability_namespace": capability_namespace,
            "capability_configuration": capability_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_pipeline(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        pipeline_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        description: Optional["capo_iotsitewise.types.description.Description"] = None,
        environment_variables: Optional[
            "capo_iotsitewise.types.environment_variables_map.EnvironmentVariablesMap"
        ] = None,
        computations: Optional[
            "capo_iotsitewise.types.compute_node_list.ComputeNodeList"
        ] = None,
    ) -> "capo_iotsitewise.types.update_pipeline_response.UpdatePipelineResponse":
        """<p>Updates an existing pipeline in the specified workspace. Only the fields provided in the request are updated; fields not included in the request are preserved unchanged. You can update the pipeline description, environment variables, and the list of compute nodes independently.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            pipeline_name: <p>The name of the pipeline to update.</p>
            description: <p>A new description for the pipeline.</p>
            environment_variables: <p>Updated environment variables shared across all compute nodes.</p>
            computations: <p>Updated list of compute nodes forming the pipeline DAG.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.limit_exceeded_exception.LimitExceededException: <p>You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_pipeline_request.UpdatePipelineRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_pipeline_response.UpdatePipelineResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_pipeline

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_pipeline.async_update_pipeline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_pipeline_request.UpdatePipelineRequest = {
            "workspace_name": workspace_name,
            "pipeline_name": pipeline_name,
        }
        if description is not None:
            input_["description"] = description
        if environment_variables is not None:
            input_["environment_variables"] = environment_variables
        if computations is not None:
            input_["computations"] = computations

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_portal(
        self,
        portal_id: "capo_iotsitewise.types.id.ID",
        portal_name: "capo_iotsitewise.types.name.Name",
        portal_contact_email: "capo_iotsitewise.types.email.Email",
        role_arn: "capo_iotsitewise.types.iam_arn.IamArn",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        portal_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        portal_logo_image: Optional["capo_iotsitewise.types.image.Image"] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
        notification_sender_email: Optional[
            "capo_iotsitewise.types.email.Email"
        ] = None,
        alarms: Optional["capo_iotsitewise.types.alarms.Alarms"] = None,
        portal_type: Optional["capo_iotsitewise.types.portal_type.PortalType"] = None,
        portal_type_configuration: Optional[
            "capo_iotsitewise.types.portal_type_configuration.PortalTypeConfiguration"
        ] = None,
    ) -> "capo_iotsitewise.types.update_portal_response.UpdatePortalResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Updates an IoT SiteWise Monitor portal.</p>

        Args:
            portal_id: <p>The ID of the portal to update.</p>
            portal_name: <p>A new friendly name for the portal.</p>
            portal_description: <p>A new description for the portal.</p>
            portal_contact_email: <p>The Amazon Web Services administrator's contact email address.</p>
            role_arn: <p>The <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html">ARN</a> of a service role that allows the portal's users to access your IoT SiteWise resources on your behalf. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/monitor-service-role.html">Using service roles for IoT SiteWise Monitor</a> in the <i>IoT SiteWise User Guide</i>.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>
            notification_sender_email: <p>The email address that sends alarm notifications.</p>
            alarms: <p>Contains the configuration information of an alarm created in an IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/monitor-alarms.html">Monitoring with alarms</a> in the <i>IoT SiteWise Application Guide</i>.</p>
            portal_type: <p>Define the type of portal. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>
            portal_type_configuration: <p>The configuration entry associated with the specific portal type. The value for IoT SiteWise Monitor (Classic) is <code>SITEWISE_PORTAL_V1</code>. The value for IoT SiteWise Monitor (AI-aware) is <code>SITEWISE_PORTAL_V2</code>.</p>

        Raises:
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_portal_request.UpdatePortalRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_portal_response.UpdatePortalResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_portal

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_portal.async_update_portal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_portal_request.UpdatePortalRequest = {
            "portal_id": portal_id,
            "portal_name": portal_name,
            "portal_contact_email": portal_contact_email,
            "role_arn": role_arn,
        }
        if portal_description is not None:
            input_["portal_description"] = portal_description
        if portal_logo_image is not None:
            input_["portal_logo_image"] = portal_logo_image
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if notification_sender_email is not None:
            input_["notification_sender_email"] = notification_sender_email
        if alarms is not None:
            input_["alarms"] = alarms
        if portal_type is not None:
            input_["portal_type"] = portal_type
        if portal_type_configuration is not None:
            input_["portal_type_configuration"] = portal_type_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_project(
        self,
        project_id: "capo_iotsitewise.types.id.ID",
        project_name: "capo_iotsitewise.types.name.Name",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        project_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.update_project_response.UpdateProjectResponse":
        """<important> <p>The IoT SiteWise Monitor feature will no longer be open to new customers starting November 7, 2025. If you would like to use the IoT SiteWise Monitor feature, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html">IoT SiteWise Monitor availability change</a>.</p> </important> <p>Updates an IoT SiteWise Monitor project.</p>

        Args:
            project_id: <p>The ID of the project to update.</p>
            project_name: <p>A new friendly name for the project.</p>
            project_description: <p>A new description for the project.</p>
            client_token: <p>A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.</p>

        Raises:
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_project_request.UpdateProjectRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_project_response.UpdateProjectResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_project

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_project.async_update_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_project_request.UpdateProjectRequest = {
            "project_id": project_id,
            "project_name": project_name,
        }
        if project_description is not None:
            input_["project_description"] = project_description
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

    async def update_task(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        task_name: "capo_iotsitewise.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        description: Optional["capo_iotsitewise.types.description.Description"] = None,
        task_configuration: Optional[
            "capo_iotsitewise.types.task_configuration.TaskConfiguration"
        ] = None,
    ) -> "capo_iotsitewise.types.update_task_response.UpdateTaskResponse":
        """<p>Updates an existing task in the specified workspace. Only the fields provided in the request are updated; fields not included in the request are preserved unchanged.</p>

        Args:
            workspace_name: <p>The name of the workspace.</p>
            task_name: <p>The name of the task to update.</p>
            description: <p>A new description for the task.</p>
            task_configuration: <p>The updated task execution configuration.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_task_request.UpdateTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_task_response.UpdateTaskResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_task

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_task.async_update_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_task_request.UpdateTaskRequest = {
            "workspace_name": workspace_name,
            "task_name": task_name,
        }
        if description is not None:
            input_["description"] = description
        if task_configuration is not None:
            input_["task_configuration"] = task_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_workspace(
        self,
        workspace_name: "capo_iotsitewise.types.workspace_name.WorkspaceName",
        *,
        config_overrides: Optional[AsyncIoTSiteWiseClientConfig] = None,
        workspace_description: Optional[
            "capo_iotsitewise.types.description.Description"
        ] = None,
        encryption_configuration: Optional[
            "capo_iotsitewise.types.workspace_encryption_configuration.WorkspaceEncryptionConfiguration"
        ] = None,
        client_token: Optional[
            "capo_iotsitewise.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_iotsitewise.types.update_workspace_response.UpdateWorkspaceResponse":
        """<p>Updates a workspace. You can update only workspaces in the <code>ACTIVE</code> or <code>FAILED</code> state. Fields that you omit from the request are left unchanged. To recover a workspace in the <code>FAILED</code> state, call this operation and supply its encryption configuration again.</p>

        Args:
            workspace_name: <p>The name of the workspace to update.</p>
            workspace_description: <p>A new description for the workspace.</p>
            encryption_configuration: <p>The encryption configuration for the workspace. Omit this field to leave encryption unchanged. After a customer managed key configuration becomes active, the key can't be changed; supplying the same key is accepted.</p>
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure that the request is idempotent. If you retry a request that completed successfully using the same client token, the retry succeeds without performing any further actions.</p>

        Raises:
            capo_iotsitewise.errors.access_denied_exception.AccessDeniedException: <p>Access is denied.</p>
            capo_iotsitewise.errors.conflicting_operation_exception.ConflictingOperationException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_iotsitewise.errors.internal_failure_exception.InternalFailureException: <p>IoT SiteWise can't process your request right now. Try again later.</p>
            capo_iotsitewise.errors.invalid_request_exception.InvalidRequestException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.</p>
            capo_iotsitewise.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_iotsitewise.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a rate limit. For example, you might have exceeded the number of IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html">Quotas</a> in the <i>IoT SiteWise User Guide</i>.</p>
            capo_iotsitewise.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_iotsitewise.types.update_workspace_request.UpdateWorkspaceRequest]",
        ) -> AsyncOperationResponse[
            "capo_iotsitewise.types.update_workspace_response.UpdateWorkspaceResponse"
        ]:
            import capo_iotsitewise._operations.aws_io_t_site_wise.update_workspace

            (
                output,
                http_response,
            ) = await capo_iotsitewise._operations.aws_io_t_site_wise.update_workspace.async_update_workspace(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_iotsitewise.types.update_workspace_request.UpdateWorkspaceRequest = {
            "workspace_name": workspace_name
        }
        if workspace_description is not None:
            input_["workspace_description"] = workspace_description
        if encryption_configuration is not None:
            input_["encryption_configuration"] = encryption_configuration
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

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
