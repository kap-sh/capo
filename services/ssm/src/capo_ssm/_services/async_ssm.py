"""Generated from Smithy shape ``com.amazonaws.ssm#AmazonSSM``."""

import uuid
import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_ssm._auth._signers
import capo_ssm._auth._sigv4
from capo_ssm._auth._identity import Credentials
from capo_ssm._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_ssm._auth._zapros_handler import AuthMiddleware
from capo_ssm._pagination import resolve_path as _resolve_path
from capo_ssm._services._aws_config import aaws_config
from capo_ssm._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_ssm.types.access_request_id
    import capo_ssm.types.account_id_list
    import capo_ssm.types.activation
    import capo_ssm.types.activation_description
    import capo_ssm.types.activation_id
    import capo_ssm.types.add_tags_to_resource_request
    import capo_ssm.types.add_tags_to_resource_result
    import capo_ssm.types.aggregator_schema_only
    import capo_ssm.types.alarm_configuration
    import capo_ssm.types.allowed_pattern
    import capo_ssm.types.apply_only_at_cron_interval
    import capo_ssm.types.associate_ops_item_related_item_request
    import capo_ssm.types.associate_ops_item_related_item_response
    import capo_ssm.types.association
    import capo_ssm.types.association_compliance_severity
    import capo_ssm.types.association_dispatch_assume_role_arn
    import capo_ssm.types.association_execution
    import capo_ssm.types.association_execution_filter_list
    import capo_ssm.types.association_execution_id
    import capo_ssm.types.association_execution_target
    import capo_ssm.types.association_execution_targets_filter_list
    import capo_ssm.types.association_filter_list
    import capo_ssm.types.association_id
    import capo_ssm.types.association_id_list
    import capo_ssm.types.association_name
    import capo_ssm.types.association_status
    import capo_ssm.types.association_sync_compliance
    import capo_ssm.types.association_version
    import capo_ssm.types.association_version_info
    import capo_ssm.types.attachments_source_list
    import capo_ssm.types.automation_execution_filter_list
    import capo_ssm.types.automation_execution_id
    import capo_ssm.types.automation_execution_metadata
    import capo_ssm.types.automation_parameter_key
    import capo_ssm.types.automation_parameter_map
    import capo_ssm.types.automation_target_parameter_name
    import capo_ssm.types.automation_targets
    import capo_ssm.types.baseline_description
    import capo_ssm.types.baseline_id
    import capo_ssm.types.baseline_name
    import capo_ssm.types.baseline_override
    import capo_ssm.types.boolean
    import capo_ssm.types.calendar_name_or_arn_list
    import capo_ssm.types.cancel_command_request
    import capo_ssm.types.cancel_command_result
    import capo_ssm.types.cancel_maintenance_window_execution_request
    import capo_ssm.types.cancel_maintenance_window_execution_result
    import capo_ssm.types.change_details_value
    import capo_ssm.types.change_request_name
    import capo_ssm.types.client_token
    import capo_ssm.types.cloud_connector_configuration
    import capo_ssm.types.cloud_connector_description
    import capo_ssm.types.cloud_connector_filter_list
    import capo_ssm.types.cloud_connector_iam_role_arn
    import capo_ssm.types.cloud_connector_id
    import capo_ssm.types.cloud_connector_max_results
    import capo_ssm.types.cloud_connector_summary
    import capo_ssm.types.cloud_watch_output_config
    import capo_ssm.types.command
    import capo_ssm.types.command_filter_list
    import capo_ssm.types.command_id
    import capo_ssm.types.command_invocation
    import capo_ssm.types.command_max_results
    import capo_ssm.types.command_plugin_name
    import capo_ssm.types.comment
    import capo_ssm.types.compliance_execution_summary
    import capo_ssm.types.compliance_item
    import capo_ssm.types.compliance_item_content_hash
    import capo_ssm.types.compliance_item_entry_list
    import capo_ssm.types.compliance_resource_id
    import capo_ssm.types.compliance_resource_id_list
    import capo_ssm.types.compliance_resource_type
    import capo_ssm.types.compliance_resource_type_list
    import capo_ssm.types.compliance_string_filter_list
    import capo_ssm.types.compliance_summary_item
    import capo_ssm.types.compliance_type_name
    import capo_ssm.types.compliance_upload_type
    import capo_ssm.types.config_connector_arn
    import capo_ssm.types.create_activation_request
    import capo_ssm.types.create_activation_result
    import capo_ssm.types.create_association_batch_request
    import capo_ssm.types.create_association_batch_request_entries
    import capo_ssm.types.create_association_batch_result
    import capo_ssm.types.create_association_request
    import capo_ssm.types.create_association_result
    import capo_ssm.types.create_cloud_connector_request
    import capo_ssm.types.create_cloud_connector_result
    import capo_ssm.types.create_document_request
    import capo_ssm.types.create_document_result
    import capo_ssm.types.create_maintenance_window_request
    import capo_ssm.types.create_maintenance_window_result
    import capo_ssm.types.create_ops_item_request
    import capo_ssm.types.create_ops_item_response
    import capo_ssm.types.create_ops_metadata_request
    import capo_ssm.types.create_ops_metadata_result
    import capo_ssm.types.create_patch_baseline_request
    import capo_ssm.types.create_patch_baseline_result
    import capo_ssm.types.create_resource_data_sync_request
    import capo_ssm.types.create_resource_data_sync_result
    import capo_ssm.types.date_time
    import capo_ssm.types.default_instance_name
    import capo_ssm.types.delete_activation_request
    import capo_ssm.types.delete_activation_result
    import capo_ssm.types.delete_association_request
    import capo_ssm.types.delete_association_result
    import capo_ssm.types.delete_cloud_connector_request
    import capo_ssm.types.delete_cloud_connector_result
    import capo_ssm.types.delete_document_request
    import capo_ssm.types.delete_document_result
    import capo_ssm.types.delete_inventory_request
    import capo_ssm.types.delete_inventory_result
    import capo_ssm.types.delete_maintenance_window_request
    import capo_ssm.types.delete_maintenance_window_result
    import capo_ssm.types.delete_ops_item_request
    import capo_ssm.types.delete_ops_item_response
    import capo_ssm.types.delete_ops_metadata_request
    import capo_ssm.types.delete_ops_metadata_result
    import capo_ssm.types.delete_parameter_request
    import capo_ssm.types.delete_parameter_result
    import capo_ssm.types.delete_parameters_request
    import capo_ssm.types.delete_parameters_result
    import capo_ssm.types.delete_patch_baseline_request
    import capo_ssm.types.delete_patch_baseline_result
    import capo_ssm.types.delete_resource_data_sync_request
    import capo_ssm.types.delete_resource_data_sync_result
    import capo_ssm.types.delete_resource_policy_request
    import capo_ssm.types.delete_resource_policy_response
    import capo_ssm.types.deletion_mode
    import capo_ssm.types.deregister_managed_instance_request
    import capo_ssm.types.deregister_managed_instance_result
    import capo_ssm.types.deregister_patch_baseline_for_patch_group_request
    import capo_ssm.types.deregister_patch_baseline_for_patch_group_result
    import capo_ssm.types.deregister_target_from_maintenance_window_request
    import capo_ssm.types.deregister_target_from_maintenance_window_result
    import capo_ssm.types.deregister_task_from_maintenance_window_request
    import capo_ssm.types.deregister_task_from_maintenance_window_result
    import capo_ssm.types.describe_activations_filter_list
    import capo_ssm.types.describe_activations_request
    import capo_ssm.types.describe_activations_result
    import capo_ssm.types.describe_association_execution_targets_request
    import capo_ssm.types.describe_association_execution_targets_result
    import capo_ssm.types.describe_association_executions_request
    import capo_ssm.types.describe_association_executions_result
    import capo_ssm.types.describe_association_request
    import capo_ssm.types.describe_association_result
    import capo_ssm.types.describe_automation_executions_request
    import capo_ssm.types.describe_automation_executions_result
    import capo_ssm.types.describe_automation_step_executions_request
    import capo_ssm.types.describe_automation_step_executions_result
    import capo_ssm.types.describe_available_patches_request
    import capo_ssm.types.describe_available_patches_result
    import capo_ssm.types.describe_document_permission_request
    import capo_ssm.types.describe_document_permission_response
    import capo_ssm.types.describe_document_request
    import capo_ssm.types.describe_document_result
    import capo_ssm.types.describe_effective_instance_associations_request
    import capo_ssm.types.describe_effective_instance_associations_result
    import capo_ssm.types.describe_effective_patches_for_patch_baseline_request
    import capo_ssm.types.describe_effective_patches_for_patch_baseline_result
    import capo_ssm.types.describe_instance_associations_status_request
    import capo_ssm.types.describe_instance_associations_status_result
    import capo_ssm.types.describe_instance_information_request
    import capo_ssm.types.describe_instance_information_result
    import capo_ssm.types.describe_instance_patch_states_for_patch_group_request
    import capo_ssm.types.describe_instance_patch_states_for_patch_group_result
    import capo_ssm.types.describe_instance_patch_states_request
    import capo_ssm.types.describe_instance_patch_states_result
    import capo_ssm.types.describe_instance_patches_request
    import capo_ssm.types.describe_instance_patches_result
    import capo_ssm.types.describe_instance_properties_max_results
    import capo_ssm.types.describe_instance_properties_request
    import capo_ssm.types.describe_instance_properties_result
    import capo_ssm.types.describe_inventory_deletions_request
    import capo_ssm.types.describe_inventory_deletions_result
    import capo_ssm.types.describe_maintenance_window_execution_task_invocations_request
    import capo_ssm.types.describe_maintenance_window_execution_task_invocations_result
    import capo_ssm.types.describe_maintenance_window_execution_tasks_request
    import capo_ssm.types.describe_maintenance_window_execution_tasks_result
    import capo_ssm.types.describe_maintenance_window_executions_request
    import capo_ssm.types.describe_maintenance_window_executions_result
    import capo_ssm.types.describe_maintenance_window_schedule_request
    import capo_ssm.types.describe_maintenance_window_schedule_result
    import capo_ssm.types.describe_maintenance_window_targets_request
    import capo_ssm.types.describe_maintenance_window_targets_result
    import capo_ssm.types.describe_maintenance_window_tasks_request
    import capo_ssm.types.describe_maintenance_window_tasks_result
    import capo_ssm.types.describe_maintenance_windows_for_target_request
    import capo_ssm.types.describe_maintenance_windows_for_target_result
    import capo_ssm.types.describe_maintenance_windows_request
    import capo_ssm.types.describe_maintenance_windows_result
    import capo_ssm.types.describe_ops_items_request
    import capo_ssm.types.describe_ops_items_response
    import capo_ssm.types.describe_parameters_request
    import capo_ssm.types.describe_parameters_result
    import capo_ssm.types.describe_patch_baselines_request
    import capo_ssm.types.describe_patch_baselines_result
    import capo_ssm.types.describe_patch_group_state_request
    import capo_ssm.types.describe_patch_group_state_result
    import capo_ssm.types.describe_patch_groups_request
    import capo_ssm.types.describe_patch_groups_result
    import capo_ssm.types.describe_patch_properties_request
    import capo_ssm.types.describe_patch_properties_result
    import capo_ssm.types.describe_sessions_request
    import capo_ssm.types.describe_sessions_response
    import capo_ssm.types.disassociate_ops_item_related_item_request
    import capo_ssm.types.disassociate_ops_item_related_item_response
    import capo_ssm.types.display_name
    import capo_ssm.types.document_arn
    import capo_ssm.types.document_content
    import capo_ssm.types.document_display_name
    import capo_ssm.types.document_filter_list
    import capo_ssm.types.document_format
    import capo_ssm.types.document_hash
    import capo_ssm.types.document_hash_type
    import capo_ssm.types.document_identifier
    import capo_ssm.types.document_key_values_filter_list
    import capo_ssm.types.document_metadata_enum
    import capo_ssm.types.document_name
    import capo_ssm.types.document_permission_max_results
    import capo_ssm.types.document_permission_type
    import capo_ssm.types.document_requires_list
    import capo_ssm.types.document_reviews
    import capo_ssm.types.document_type
    import capo_ssm.types.document_version
    import capo_ssm.types.document_version_info
    import capo_ssm.types.document_version_name
    import capo_ssm.types.document_version_number
    import capo_ssm.types.dry_run
    import capo_ssm.types.duration
    import capo_ssm.types.effective_instance_association_max_results
    import capo_ssm.types.effective_patch
    import capo_ssm.types.execution_inputs
    import capo_ssm.types.execution_mode
    import capo_ssm.types.execution_preview_id
    import capo_ssm.types.expiration_date
    import capo_ssm.types.get_access_token_request
    import capo_ssm.types.get_access_token_response
    import capo_ssm.types.get_automation_execution_request
    import capo_ssm.types.get_automation_execution_result
    import capo_ssm.types.get_calendar_state_request
    import capo_ssm.types.get_calendar_state_response
    import capo_ssm.types.get_cloud_connector_request
    import capo_ssm.types.get_cloud_connector_result
    import capo_ssm.types.get_command_invocation_request
    import capo_ssm.types.get_command_invocation_result
    import capo_ssm.types.get_connection_status_request
    import capo_ssm.types.get_connection_status_response
    import capo_ssm.types.get_default_patch_baseline_request
    import capo_ssm.types.get_default_patch_baseline_result
    import capo_ssm.types.get_deployable_patch_snapshot_for_instance_request
    import capo_ssm.types.get_deployable_patch_snapshot_for_instance_result
    import capo_ssm.types.get_document_request
    import capo_ssm.types.get_document_result
    import capo_ssm.types.get_execution_preview_request
    import capo_ssm.types.get_execution_preview_response
    import capo_ssm.types.get_inventory_request
    import capo_ssm.types.get_inventory_result
    import capo_ssm.types.get_inventory_schema_max_results
    import capo_ssm.types.get_inventory_schema_request
    import capo_ssm.types.get_inventory_schema_result
    import capo_ssm.types.get_maintenance_window_execution_request
    import capo_ssm.types.get_maintenance_window_execution_result
    import capo_ssm.types.get_maintenance_window_execution_task_invocation_request
    import capo_ssm.types.get_maintenance_window_execution_task_invocation_result
    import capo_ssm.types.get_maintenance_window_execution_task_request
    import capo_ssm.types.get_maintenance_window_execution_task_result
    import capo_ssm.types.get_maintenance_window_request
    import capo_ssm.types.get_maintenance_window_result
    import capo_ssm.types.get_maintenance_window_task_request
    import capo_ssm.types.get_maintenance_window_task_result
    import capo_ssm.types.get_ops_item_request
    import capo_ssm.types.get_ops_item_response
    import capo_ssm.types.get_ops_metadata_max_results
    import capo_ssm.types.get_ops_metadata_request
    import capo_ssm.types.get_ops_metadata_result
    import capo_ssm.types.get_ops_summary_request
    import capo_ssm.types.get_ops_summary_result
    import capo_ssm.types.get_parameter_history_request
    import capo_ssm.types.get_parameter_history_result
    import capo_ssm.types.get_parameter_request
    import capo_ssm.types.get_parameter_result
    import capo_ssm.types.get_parameters_by_path_max_results
    import capo_ssm.types.get_parameters_by_path_request
    import capo_ssm.types.get_parameters_by_path_result
    import capo_ssm.types.get_parameters_request
    import capo_ssm.types.get_parameters_result
    import capo_ssm.types.get_patch_baseline_for_patch_group_request
    import capo_ssm.types.get_patch_baseline_for_patch_group_result
    import capo_ssm.types.get_patch_baseline_request
    import capo_ssm.types.get_patch_baseline_result
    import capo_ssm.types.get_resource_policies_request
    import capo_ssm.types.get_resource_policies_response
    import capo_ssm.types.get_resource_policies_response_entry
    import capo_ssm.types.get_service_setting_request
    import capo_ssm.types.get_service_setting_result
    import capo_ssm.types.iam_role
    import capo_ssm.types.idempotency_token
    import capo_ssm.types.instance_association
    import capo_ssm.types.instance_association_output_location
    import capo_ssm.types.instance_association_status_info
    import capo_ssm.types.instance_id
    import capo_ssm.types.instance_id_list
    import capo_ssm.types.instance_information
    import capo_ssm.types.instance_information_filter_list
    import capo_ssm.types.instance_information_string_filter_list
    import capo_ssm.types.instance_patch_state
    import capo_ssm.types.instance_patch_state_filter_list
    import capo_ssm.types.instance_property
    import capo_ssm.types.instance_property_filter_list
    import capo_ssm.types.instance_property_string_filter_list
    import capo_ssm.types.inventory_aggregator_list
    import capo_ssm.types.inventory_deletion_status_item
    import capo_ssm.types.inventory_filter_list
    import capo_ssm.types.inventory_item_list
    import capo_ssm.types.inventory_item_schema
    import capo_ssm.types.inventory_item_type_name
    import capo_ssm.types.inventory_item_type_name_filter
    import capo_ssm.types.inventory_result_entity
    import capo_ssm.types.inventory_schema_delete_option
    import capo_ssm.types.is_sub_type_schema
    import capo_ssm.types.iso8601_string
    import capo_ssm.types.key_list
    import capo_ssm.types.label_parameter_version_request
    import capo_ssm.types.label_parameter_version_result
    import capo_ssm.types.list_association_versions_request
    import capo_ssm.types.list_association_versions_result
    import capo_ssm.types.list_associations_request
    import capo_ssm.types.list_associations_result
    import capo_ssm.types.list_cloud_connectors_request
    import capo_ssm.types.list_cloud_connectors_result
    import capo_ssm.types.list_command_invocations_request
    import capo_ssm.types.list_command_invocations_result
    import capo_ssm.types.list_commands_request
    import capo_ssm.types.list_commands_result
    import capo_ssm.types.list_compliance_items_request
    import capo_ssm.types.list_compliance_items_result
    import capo_ssm.types.list_compliance_summaries_request
    import capo_ssm.types.list_compliance_summaries_result
    import capo_ssm.types.list_document_metadata_history_request
    import capo_ssm.types.list_document_metadata_history_response
    import capo_ssm.types.list_document_versions_request
    import capo_ssm.types.list_document_versions_result
    import capo_ssm.types.list_documents_request
    import capo_ssm.types.list_documents_result
    import capo_ssm.types.list_inventory_entries_request
    import capo_ssm.types.list_inventory_entries_result
    import capo_ssm.types.list_nodes_request
    import capo_ssm.types.list_nodes_result
    import capo_ssm.types.list_nodes_summary_request
    import capo_ssm.types.list_nodes_summary_result
    import capo_ssm.types.list_ops_item_events_request
    import capo_ssm.types.list_ops_item_events_response
    import capo_ssm.types.list_ops_item_related_items_request
    import capo_ssm.types.list_ops_item_related_items_response
    import capo_ssm.types.list_ops_metadata_max_results
    import capo_ssm.types.list_ops_metadata_request
    import capo_ssm.types.list_ops_metadata_result
    import capo_ssm.types.list_resource_compliance_summaries_request
    import capo_ssm.types.list_resource_compliance_summaries_result
    import capo_ssm.types.list_resource_data_sync_request
    import capo_ssm.types.list_resource_data_sync_result
    import capo_ssm.types.list_tags_for_resource_request
    import capo_ssm.types.list_tags_for_resource_result
    import capo_ssm.types.logging_info
    import capo_ssm.types.maintenance_window_allow_unassociated_targets
    import capo_ssm.types.maintenance_window_cutoff
    import capo_ssm.types.maintenance_window_description
    import capo_ssm.types.maintenance_window_duration_hours
    import capo_ssm.types.maintenance_window_enabled
    import capo_ssm.types.maintenance_window_execution
    import capo_ssm.types.maintenance_window_execution_id
    import capo_ssm.types.maintenance_window_execution_task_id
    import capo_ssm.types.maintenance_window_execution_task_identity
    import capo_ssm.types.maintenance_window_execution_task_invocation_id
    import capo_ssm.types.maintenance_window_execution_task_invocation_identity
    import capo_ssm.types.maintenance_window_filter_list
    import capo_ssm.types.maintenance_window_id
    import capo_ssm.types.maintenance_window_identity
    import capo_ssm.types.maintenance_window_identity_for_target
    import capo_ssm.types.maintenance_window_max_results
    import capo_ssm.types.maintenance_window_name
    import capo_ssm.types.maintenance_window_offset
    import capo_ssm.types.maintenance_window_resource_type
    import capo_ssm.types.maintenance_window_schedule
    import capo_ssm.types.maintenance_window_search_max_results
    import capo_ssm.types.maintenance_window_string_date_time
    import capo_ssm.types.maintenance_window_target
    import capo_ssm.types.maintenance_window_target_id
    import capo_ssm.types.maintenance_window_task
    import capo_ssm.types.maintenance_window_task_arn
    import capo_ssm.types.maintenance_window_task_cutoff_behavior
    import capo_ssm.types.maintenance_window_task_id
    import capo_ssm.types.maintenance_window_task_invocation_parameters
    import capo_ssm.types.maintenance_window_task_parameters
    import capo_ssm.types.maintenance_window_task_priority
    import capo_ssm.types.maintenance_window_task_type
    import capo_ssm.types.maintenance_window_timezone
    import capo_ssm.types.managed_instance_id
    import capo_ssm.types.max_concurrency
    import capo_ssm.types.max_errors
    import capo_ssm.types.max_results
    import capo_ssm.types.max_results_ec2_compatible
    import capo_ssm.types.metadata_keys_to_delete_list
    import capo_ssm.types.metadata_map
    import capo_ssm.types.modify_document_permission_request
    import capo_ssm.types.modify_document_permission_response
    import capo_ssm.types.next_token
    import capo_ssm.types.node
    import capo_ssm.types.node_aggregator_list
    import capo_ssm.types.node_filter_list
    import capo_ssm.types.node_summary
    import capo_ssm.types.notification_config
    import capo_ssm.types.operating_system
    import capo_ssm.types.ops_aggregator_list
    import capo_ssm.types.ops_entity
    import capo_ssm.types.ops_filter_list
    import capo_ssm.types.ops_item_account_id
    import capo_ssm.types.ops_item_arn
    import capo_ssm.types.ops_item_category
    import capo_ssm.types.ops_item_description
    import capo_ssm.types.ops_item_event_filters
    import capo_ssm.types.ops_item_event_max_results
    import capo_ssm.types.ops_item_event_summary
    import capo_ssm.types.ops_item_filters
    import capo_ssm.types.ops_item_id
    import capo_ssm.types.ops_item_max_results
    import capo_ssm.types.ops_item_notifications
    import capo_ssm.types.ops_item_operational_data
    import capo_ssm.types.ops_item_ops_data_keys_list
    import capo_ssm.types.ops_item_priority
    import capo_ssm.types.ops_item_related_item_association_id
    import capo_ssm.types.ops_item_related_item_association_resource_type
    import capo_ssm.types.ops_item_related_item_association_resource_uri
    import capo_ssm.types.ops_item_related_item_association_type
    import capo_ssm.types.ops_item_related_item_summary
    import capo_ssm.types.ops_item_related_items_filters
    import capo_ssm.types.ops_item_related_items_max_results
    import capo_ssm.types.ops_item_severity
    import capo_ssm.types.ops_item_source
    import capo_ssm.types.ops_item_status
    import capo_ssm.types.ops_item_summary
    import capo_ssm.types.ops_item_title
    import capo_ssm.types.ops_item_type
    import capo_ssm.types.ops_metadata
    import capo_ssm.types.ops_metadata_arn
    import capo_ssm.types.ops_metadata_filter_list
    import capo_ssm.types.ops_metadata_resource_id
    import capo_ssm.types.ops_result_attribute_list
    import capo_ssm.types.owner_information
    import capo_ssm.types.parameter_data_type
    import capo_ssm.types.parameter_description
    import capo_ssm.types.parameter_key_id
    import capo_ssm.types.parameter_label_list
    import capo_ssm.types.parameter_name_list
    import capo_ssm.types.parameter_policies
    import capo_ssm.types.parameter_string_filter_list
    import capo_ssm.types.parameter_tier
    import capo_ssm.types.parameter_type
    import capo_ssm.types.parameters
    import capo_ssm.types.parameters_filter_list
    import capo_ssm.types.patch
    import capo_ssm.types.patch_action
    import capo_ssm.types.patch_baseline_identity
    import capo_ssm.types.patch_baseline_max_results
    import capo_ssm.types.patch_compliance_data
    import capo_ssm.types.patch_compliance_level
    import capo_ssm.types.patch_compliance_max_results
    import capo_ssm.types.patch_compliance_status
    import capo_ssm.types.patch_filter_group
    import capo_ssm.types.patch_group
    import capo_ssm.types.patch_group_patch_baseline_mapping
    import capo_ssm.types.patch_id_list
    import capo_ssm.types.patch_orchestrator_filter_list
    import capo_ssm.types.patch_property
    import capo_ssm.types.patch_property_entry
    import capo_ssm.types.patch_rule_group
    import capo_ssm.types.patch_set
    import capo_ssm.types.patch_source_list
    import capo_ssm.types.policy
    import capo_ssm.types.policy_hash
    import capo_ssm.types.policy_id
    import capo_ssm.types.ps_parameter_name
    import capo_ssm.types.ps_parameter_value
    import capo_ssm.types.ps_parameter_version
    import capo_ssm.types.put_compliance_items_request
    import capo_ssm.types.put_compliance_items_result
    import capo_ssm.types.put_inventory_request
    import capo_ssm.types.put_inventory_result
    import capo_ssm.types.put_parameter_request
    import capo_ssm.types.put_parameter_result
    import capo_ssm.types.put_resource_policy_request
    import capo_ssm.types.put_resource_policy_response
    import capo_ssm.types.register_default_patch_baseline_request
    import capo_ssm.types.register_default_patch_baseline_result
    import capo_ssm.types.register_patch_baseline_for_patch_group_request
    import capo_ssm.types.register_patch_baseline_for_patch_group_result
    import capo_ssm.types.register_target_with_maintenance_window_request
    import capo_ssm.types.register_target_with_maintenance_window_result
    import capo_ssm.types.register_task_with_maintenance_window_request
    import capo_ssm.types.register_task_with_maintenance_window_result
    import capo_ssm.types.registration_limit
    import capo_ssm.types.registration_metadata_list
    import capo_ssm.types.related_ops_items
    import capo_ssm.types.remove_tags_from_resource_request
    import capo_ssm.types.remove_tags_from_resource_result
    import capo_ssm.types.reset_service_setting_request
    import capo_ssm.types.reset_service_setting_result
    import capo_ssm.types.resource_arn_string
    import capo_ssm.types.resource_compliance_summary_item
    import capo_ssm.types.resource_data_sync_item
    import capo_ssm.types.resource_data_sync_name
    import capo_ssm.types.resource_data_sync_s3_destination
    import capo_ssm.types.resource_data_sync_source
    import capo_ssm.types.resource_data_sync_type
    import capo_ssm.types.resource_id
    import capo_ssm.types.resource_policy_max_results
    import capo_ssm.types.resource_type_for_tagging
    import capo_ssm.types.result_attribute_list
    import capo_ssm.types.resume_session_request
    import capo_ssm.types.resume_session_response
    import capo_ssm.types.runbooks
    import capo_ssm.types.s3_bucket_name
    import capo_ssm.types.s3_key_prefix
    import capo_ssm.types.s3_region
    import capo_ssm.types.schedule_expression
    import capo_ssm.types.schedule_offset
    import capo_ssm.types.scheduled_window_execution
    import capo_ssm.types.send_automation_signal_request
    import capo_ssm.types.send_automation_signal_result
    import capo_ssm.types.send_command_request
    import capo_ssm.types.send_command_result
    import capo_ssm.types.service_role
    import capo_ssm.types.service_setting_id
    import capo_ssm.types.service_setting_value
    import capo_ssm.types.session
    import capo_ssm.types.session_filter_list
    import capo_ssm.types.session_id
    import capo_ssm.types.session_manager_parameters
    import capo_ssm.types.session_max_results
    import capo_ssm.types.session_reason
    import capo_ssm.types.session_state
    import capo_ssm.types.session_target
    import capo_ssm.types.shared_document_version
    import capo_ssm.types.signal_type
    import capo_ssm.types.snapshot_id
    import capo_ssm.types.start_access_request_request
    import capo_ssm.types.start_access_request_response
    import capo_ssm.types.start_associations_once_request
    import capo_ssm.types.start_associations_once_result
    import capo_ssm.types.start_automation_execution_request
    import capo_ssm.types.start_automation_execution_result
    import capo_ssm.types.start_change_request_execution_request
    import capo_ssm.types.start_change_request_execution_result
    import capo_ssm.types.start_execution_preview_request
    import capo_ssm.types.start_execution_preview_response
    import capo_ssm.types.start_session_request
    import capo_ssm.types.start_session_response
    import capo_ssm.types.step_execution
    import capo_ssm.types.step_execution_filter_list
    import capo_ssm.types.stop_automation_execution_request
    import capo_ssm.types.stop_automation_execution_result
    import capo_ssm.types.stop_type
    import capo_ssm.types.string
    import capo_ssm.types.string1to256
    import capo_ssm.types.tag_list
    import capo_ssm.types.target_locations
    import capo_ssm.types.target_locations_url
    import capo_ssm.types.target_maps
    import capo_ssm.types.target_type
    import capo_ssm.types.targets
    import capo_ssm.types.terminate_session_request
    import capo_ssm.types.terminate_session_response
    import capo_ssm.types.timeout_seconds
    import capo_ssm.types.unlabel_parameter_version_request
    import capo_ssm.types.unlabel_parameter_version_result
    import capo_ssm.types.update_association_request
    import capo_ssm.types.update_association_result
    import capo_ssm.types.update_association_status_request
    import capo_ssm.types.update_association_status_result
    import capo_ssm.types.update_cloud_connector_request
    import capo_ssm.types.update_cloud_connector_result
    import capo_ssm.types.update_document_default_version_request
    import capo_ssm.types.update_document_default_version_result
    import capo_ssm.types.update_document_metadata_request
    import capo_ssm.types.update_document_metadata_response
    import capo_ssm.types.update_document_request
    import capo_ssm.types.update_document_result
    import capo_ssm.types.update_maintenance_window_request
    import capo_ssm.types.update_maintenance_window_result
    import capo_ssm.types.update_maintenance_window_target_request
    import capo_ssm.types.update_maintenance_window_target_result
    import capo_ssm.types.update_maintenance_window_task_request
    import capo_ssm.types.update_maintenance_window_task_result
    import capo_ssm.types.update_managed_instance_role_request
    import capo_ssm.types.update_managed_instance_role_result
    import capo_ssm.types.update_ops_item_request
    import capo_ssm.types.update_ops_item_response
    import capo_ssm.types.update_ops_metadata_request
    import capo_ssm.types.update_ops_metadata_result
    import capo_ssm.types.update_patch_baseline_request
    import capo_ssm.types.update_patch_baseline_result
    import capo_ssm.types.update_resource_data_sync_request
    import capo_ssm.types.update_resource_data_sync_result
    import capo_ssm.types.update_service_setting_request
    import capo_ssm.types.update_service_setting_result
    import capo_ssm.types.uuid
    import capo_ssm.types.validate_cloud_connector_max_results
    import capo_ssm.types.validate_cloud_connector_request
    import capo_ssm.types.validate_cloud_connector_result
    import capo_ssm.types.validation_finding


class AsyncSSMClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncSSMClient:
    """A client for the ``SSM`` service.

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
        self._config = AsyncSSMClientConfig(
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
        self, config_overrides: Optional[AsyncSSMClientConfig] = None
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncSSMClientConfig = config_overrides or {}
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

    async def add_tags_to_resource(
        self,
        resource_type: "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging",
        resource_id: "capo_ssm.types.resource_id.ResourceId",
        tags: "capo_ssm.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.add_tags_to_resource_result.AddTagsToResourceResult":
        """<p>Adds or overwrites one or more tags for the specified resource. <i>Tags</i> are metadata that you can assign to your automations, documents, managed nodes, maintenance windows, Parameter Store parameters, and patch baselines. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. For example, you could define a set of tags for your account's managed nodes that helps you track each node's owner and stack level. For example:</p> <ul> <li> <p> <code>Key=Owner,Value=DbAdmin</code> </p> </li> <li> <p> <code>Key=Owner,Value=SysAdmin</code> </p> </li> <li> <p> <code>Key=Owner,Value=Dev</code> </p> </li> <li> <p> <code>Key=Stack,Value=Production</code> </p> </li> <li> <p> <code>Key=Stack,Value=Pre-Production</code> </p> </li> <li> <p> <code>Key=Stack,Value=Test</code> </p> </li> </ul> <p>Most resources can have a maximum of 50 tags. Automations can have a maximum of 5 tags.</p> <p>We recommend that you devise a set of tag keys that meets your needs for each resource type. Using a consistent set of tag keys makes it easier for you to manage your resources. You can search and filter the resources based on the tags you add. Tags don't have any semantic meaning to and are interpreted strictly as a string of characters.</p> <p>For more information about using tags with Amazon Elastic Compute Cloud (Amazon EC2) instances, see <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html">Tag your Amazon EC2 resources</a> in the <i>Amazon EC2 User Guide</i>.</p>

        Args:
            resource_type: <p>Specifies the type of resource you are tagging.</p> <note> <p>The <code>ManagedInstance</code> type for this API operation is for on-premises managed nodes. You must specify the name of the managed node in the following format: <code>mi-<i>ID_number</i> </code>. For example, <code>mi-1a2b3c4d5e6f</code>.</p> </note>
            resource_id: <p>The resource ID you want to tag.</p> <p>Use the ID of the resource. Here are some examples:</p> <p> <code>MaintenanceWindow</code>: <code>mw-012345abcde</code> </p> <p> <code>PatchBaseline</code>: <code>pb-012345abcde</code> </p> <p> <code>Automation</code>: <code>example-c160-4567-8519-012345abcde</code> </p> <p> <code>OpsMetadata</code> object: <code>ResourceID</code> for tagging is created from the Amazon Resource Name (ARN) for the object. Specifically, <code>ResourceID</code> is created from the strings that come after the word <code>opsmetadata</code> in the ARN. For example, an OpsMetadata object with an ARN of <code>arn:aws:ssm:us-east-2:1234567890:opsmetadata/aws/ssm/MyGroup/appmanager</code> has a <code>ResourceID</code> of either <code>aws/ssm/MyGroup/appmanager</code> or <code>/aws/ssm/MyGroup/appmanager</code>.</p> <p>For the <code>Document</code> and <code>Parameter</code> values, use the name of the resource. If you're tagging a shared document, you must use the full ARN of the document.</p> <p> <code>ManagedInstance</code>: <code>mi-012345abcde</code> </p> <note> <p>The <code>ManagedInstance</code> type for this API operation is only for on-premises managed nodes. You must specify the name of the managed node in the following format: <code>mi-<i>ID_number</i> </code>. For example, <code>mi-1a2b3c4d5e6f</code>.</p> </note>
            tags: <p>One or more tags. The value parameter is required.</p> <important> <p>Don't enter personally identifiable information in this field.</p> </important>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.invalid_resource_type.InvalidResourceType: <p>The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.</p>
            capo_ssm.errors.too_many_tags_error.TooManyTagsError: <p>The <code>Targets</code> parameter includes too many tags. Remove one or more tags and try the command again.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.add_tags_to_resource_request.AddTagsToResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.add_tags_to_resource_result.AddTagsToResourceResult"
        ]:
            import capo_ssm._operations.amazon_ssm.add_tags_to_resource

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.add_tags_to_resource.async_add_tags_to_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.add_tags_to_resource_request.AddTagsToResourceRequest = {
            "resource_type": resource_type,
            "resource_id": resource_id,
            "tags": tags,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def associate_ops_item_related_item(
        self,
        ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId",
        association_type: "capo_ssm.types.ops_item_related_item_association_type.OpsItemRelatedItemAssociationType",
        resource_type: "capo_ssm.types.ops_item_related_item_association_resource_type.OpsItemRelatedItemAssociationResourceType",
        resource_uri: "capo_ssm.types.ops_item_related_item_association_resource_uri.OpsItemRelatedItemAssociationResourceUri",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.associate_ops_item_related_item_response.AssociateOpsItemRelatedItemResponse":
        """<p>Associates a related item to a Systems Manager OpsCenter OpsItem. For example, you can associate an Incident Manager incident or analysis with an OpsItem. Incident Manager and OpsCenter are tools in Amazon Web Services Systems Manager.</p>

        Args:
            ops_item_id: <p>The ID of the OpsItem to which you want to associate a resource as a related item.</p>
            association_type: <p>The type of association that you want to create between an OpsItem and a resource. OpsCenter supports <code>IsParentOf</code> and <code>RelatesTo</code> association types.</p>
            resource_type: <p>The type of resource that you want to associate with an OpsItem. OpsCenter supports the following types:</p> <p> <code>AWS::SSMIncidents::IncidentRecord</code>: an Incident Manager incident. </p> <p> <code>AWS::SSM::Document</code>: a Systems Manager (SSM) document.</p>
            resource_uri: <p>The Amazon Resource Name (ARN) of the Amazon Web Services resource that you want to associate with the OpsItem.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_conflict_exception.OpsItemConflictException: <p>The specified OpsItem is in the process of being deleted.</p>
            capo_ssm.errors.ops_item_invalid_parameter_exception.OpsItemInvalidParameterException: <p>A specified parameter argument isn't valid. Verify the available arguments and try again.</p>
            capo_ssm.errors.ops_item_limit_exceeded_exception.OpsItemLimitExceededException: <p>The request caused OpsItems to exceed one or more quotas.</p>
            capo_ssm.errors.ops_item_not_found_exception.OpsItemNotFoundException: <p>The specified OpsItem ID doesn't exist. Verify the ID and try again.</p>
            capo_ssm.errors.ops_item_related_item_already_exists_exception.OpsItemRelatedItemAlreadyExistsException: <p>The Amazon Resource Name (ARN) is already associated with the OpsItem.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.associate_ops_item_related_item_request.AssociateOpsItemRelatedItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.associate_ops_item_related_item_response.AssociateOpsItemRelatedItemResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.associate_ops_item_related_item

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.associate_ops_item_related_item.async_associate_ops_item_related_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.associate_ops_item_related_item_request.AssociateOpsItemRelatedItemRequest = {
            "ops_item_id": ops_item_id,
            "association_type": association_type,
            "resource_type": resource_type,
            "resource_uri": resource_uri,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_command(
        self,
        command_id: "capo_ssm.types.command_id.CommandId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        instance_ids: Optional["capo_ssm.types.instance_id_list.InstanceIdList"] = None,
    ) -> "capo_ssm.types.cancel_command_result.CancelCommandResult":
        """<p>Attempts to cancel the command specified by the Command ID. There is no guarantee that the command will be terminated and the underlying process stopped.</p>

        Args:
            command_id: <p>The ID of the command you want to cancel.</p>
            instance_ids: <p>(Optional) A list of managed node IDs on which you want to cancel the command. If not provided, the command is canceled on every node on which it was requested.</p>

        Raises:
            capo_ssm.errors.duplicate_instance_id.DuplicateInstanceId: <p>You can't specify a managed node ID in more than one association.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_command_id.InvalidCommandId: <p>The specified command ID isn't valid. Verify the ID and try again.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.cancel_command_request.CancelCommandRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.cancel_command_result.CancelCommandResult"
        ]:
            import capo_ssm._operations.amazon_ssm.cancel_command

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.cancel_command.async_cancel_command(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.cancel_command_request.CancelCommandRequest = {
            "command_id": command_id
        }
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_maintenance_window_execution(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.cancel_maintenance_window_execution_result.CancelMaintenanceWindowExecutionResult":
        """<p>Stops a maintenance window execution that is already in progress and cancels any tasks in the window that haven't already starting running. Tasks already in progress will continue to completion.</p>

        Args:
            window_execution_id: <p>The ID of the maintenance window execution to stop.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.cancel_maintenance_window_execution_request.CancelMaintenanceWindowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.cancel_maintenance_window_execution_result.CancelMaintenanceWindowExecutionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.cancel_maintenance_window_execution

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.cancel_maintenance_window_execution.async_cancel_maintenance_window_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.cancel_maintenance_window_execution_request.CancelMaintenanceWindowExecutionRequest = {
            "window_execution_id": window_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_activation(
        self,
        iam_role: "capo_ssm.types.iam_role.IamRole",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        description: Optional[
            "capo_ssm.types.activation_description.ActivationDescription"
        ] = None,
        default_instance_name: Optional[
            "capo_ssm.types.default_instance_name.DefaultInstanceName"
        ] = None,
        registration_limit: Optional[
            "capo_ssm.types.registration_limit.RegistrationLimit"
        ] = None,
        expiration_date: Optional[
            "capo_ssm.types.expiration_date.ExpirationDate"
        ] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
        registration_metadata: Optional[
            "capo_ssm.types.registration_metadata_list.RegistrationMetadataList"
        ] = None,
    ) -> "capo_ssm.types.create_activation_result.CreateActivationResult":
        """<p>Generates an activation code and activation ID you can use to register your on-premises servers, edge devices, or virtual machine (VM) with Amazon Web Services Systems Manager. Registering these machines with Systems Manager makes it possible to manage them using Systems Manager tools. You use the activation code and ID when installing SSM Agent on machines in your hybrid environment. For more information about requirements for managing on-premises machines using Systems Manager, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-hybrid-multicloud.html">Using Amazon Web Services Systems Manager in hybrid and multicloud environments</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p> <note> <p>Amazon Elastic Compute Cloud (Amazon EC2) instances, edge devices, and on-premises servers and VMs that are configured for Systems Manager are all called <i>managed nodes</i>.</p> </note>

        Args:
            description: <p>A user-defined description of the resource that you want to register with Systems Manager. </p> <important> <p>Don't enter personally identifiable information in this field.</p> </important>
            default_instance_name: <p>The name of the registered, managed node as it will appear in the Amazon Web Services Systems Manager console or when you use the Amazon Web Services command line tools to list Systems Manager resources.</p> <important> <p>Don't enter personally identifiable information in this field.</p> </important>
            iam_role: <p>The name of the Identity and Access Management (IAM) role that you want to assign to the managed node. This IAM role must provide AssumeRole permissions for the Amazon Web Services Systems Manager service principal <code>ssm.amazonaws.com</code>. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html">Create the IAM service role required for Systems Manager in a hybrid and multicloud environments</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <note> <p>You can't specify an IAM service-linked role for this parameter. You must create a unique role.</p> </note>
            registration_limit: <p>Specify the maximum number of managed nodes you want to register. The default value is <code>1</code>.</p>
            expiration_date: <p>The date by which this activation request should expire, in timestamp format, such as "2024-07-07T00:00:00". You can specify a date up to 30 days in advance. If you don't provide an expiration date, the activation code expires in 24 hours.</p>
            tags: <p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an activation to identify which servers or virtual machines (VMs) in your on-premises environment you intend to activate. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> </ul> <important> <p>When you install SSM Agent on your on-premises servers and VMs, you specify an activation ID and code. When you specify the activation ID and code, tags assigned to the activation are automatically applied to the on-premises servers or VMs.</p> </important> <p>You can't add tags to or delete tags from an existing activation. You can tag your on-premises servers, edge devices, and VMs after they connect to Systems Manager for the first time and are assigned a managed node ID. This means they are listed in the Amazon Web Services Systems Manager console with an ID that is prefixed with "mi-". For information about how to add tags to your managed nodes, see <a>AddTagsToResource</a>. For information about how to remove tags from your managed nodes, see <a>RemoveTagsFromResource</a>.</p>
            registration_metadata: <p>Reserved for internal use.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_parameters.InvalidParameters: <p>You must specify values for all required parameters in the Amazon Web Services Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_activation_request.CreateActivationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_activation_result.CreateActivationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_activation

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_activation.async_create_activation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_activation_request.CreateActivationRequest = {
            "iam_role": iam_role
        }
        if description is not None:
            input_["description"] = description
        if default_instance_name is not None:
            input_["default_instance_name"] = default_instance_name
        if registration_limit is not None:
            input_["registration_limit"] = registration_limit
        if expiration_date is not None:
            input_["expiration_date"] = expiration_date
        if tags is not None:
            input_["tags"] = tags
        if registration_metadata is not None:
            input_["registration_metadata"] = registration_metadata

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_association(
        self,
        name: "capo_ssm.types.document_arn.DocumentARN",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        instance_id: Optional["capo_ssm.types.instance_id.InstanceId"] = None,
        parameters: Optional["capo_ssm.types.parameters.Parameters"] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        schedule_expression: Optional[
            "capo_ssm.types.schedule_expression.ScheduleExpression"
        ] = None,
        output_location: Optional[
            "capo_ssm.types.instance_association_output_location.InstanceAssociationOutputLocation"
        ] = None,
        association_name: Optional[
            "capo_ssm.types.association_name.AssociationName"
        ] = None,
        automation_target_parameter_name: Optional[
            "capo_ssm.types.automation_target_parameter_name.AutomationTargetParameterName"
        ] = None,
        max_errors: Optional["capo_ssm.types.max_errors.MaxErrors"] = None,
        max_concurrency: Optional[
            "capo_ssm.types.max_concurrency.MaxConcurrency"
        ] = None,
        compliance_severity: Optional[
            "capo_ssm.types.association_compliance_severity.AssociationComplianceSeverity"
        ] = None,
        sync_compliance: Optional[
            "capo_ssm.types.association_sync_compliance.AssociationSyncCompliance"
        ] = None,
        apply_only_at_cron_interval: Optional[
            "capo_ssm.types.apply_only_at_cron_interval.ApplyOnlyAtCronInterval"
        ] = None,
        calendar_names: Optional[
            "capo_ssm.types.calendar_name_or_arn_list.CalendarNameOrARNList"
        ] = None,
        target_locations: Optional[
            "capo_ssm.types.target_locations.TargetLocations"
        ] = None,
        schedule_offset: Optional[
            "capo_ssm.types.schedule_offset.ScheduleOffset"
        ] = None,
        duration: Optional["capo_ssm.types.duration.Duration"] = None,
        target_maps: Optional["capo_ssm.types.target_maps.TargetMaps"] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
        alarm_configuration: Optional[
            "capo_ssm.types.alarm_configuration.AlarmConfiguration"
        ] = None,
        association_dispatch_assume_role: Optional[
            "capo_ssm.types.association_dispatch_assume_role_arn.AssociationDispatchAssumeRoleArn"
        ] = None,
    ) -> "capo_ssm.types.create_association_result.CreateAssociationResult":
        """<p>A State Manager association defines the state that you want to maintain on your managed nodes. For example, an association can specify that anti-virus software must be installed and running on your managed nodes, or that certain ports must be closed. For static targets, the association specifies a schedule for when the configuration is reapplied. For dynamic targets, such as an Amazon Web Services resource group or an Amazon Web Services autoscaling group, State Manager, a tool in Amazon Web Services Systems Manager applies the configuration when new managed nodes are added to the group. The association also specifies actions to take when applying the configuration. For example, an association for anti-virus software might run once a day. If the software isn't installed, then State Manager installs it. If the software is installed, but the service isn't running, then the association might instruct State Manager to start the service. </p>

        Args:
            name: <p>The name of the SSM Command document or Automation runbook that contains the configuration information for the managed node.</p> <p>You can specify Amazon Web Services-predefined documents, documents you created, or a document that is shared with you from another Amazon Web Services account.</p> <p>For Systems Manager documents (SSM documents) that are shared with you from other Amazon Web Services accounts, you must specify the complete SSM document ARN, in the following format:</p> <p> <code>arn:<i>partition</i>:ssm:<i>region</i>:<i>account-id</i>:document/<i>document-name</i> </code> </p> <p>For example:</p> <p> <code>arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document</code> </p> <p>For Amazon Web Services-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, <code>AWS-ApplyPatchBaseline</code> or <code>My-Document</code>.</p>
            document_version: <p>The document version you want to associate with the targets. Can be a specific version or the default version.</p> <important> <p>State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the <code>default</code> version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to <code>default</code>.</p> </important>
            instance_id: <p>The managed node ID.</p> <note> <p> <code>InstanceId</code> has been deprecated. To specify a managed node ID for an association, use the <code>Targets</code> parameter. Requests that include the parameter <code>InstanceID</code> with Systems Manager documents (SSM documents) that use schema version 2.0 or later will fail. In addition, if you use the parameter <code>InstanceId</code>, you can't use the parameters <code>AssociationName</code>, <code>DocumentVersion</code>, <code>MaxErrors</code>, <code>MaxConcurrency</code>, <code>OutputLocation</code>, or <code>ScheduleExpression</code>. To use these parameters, you must use the <code>Targets</code> parameter.</p> </note>
            parameters: <p>The parameters for the runtime configuration of the document.</p>
            targets: <p>The targets for the association. You can target managed nodes by using tags, Amazon Web Services resource groups, all managed nodes in an Amazon Web Services account, or individual managed node IDs. You can target all managed nodes in an Amazon Web Services account by specifying the <code>InstanceIds</code> key with a value of <code>*</code>. For more information about choosing targets for an association, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state-manager-targets-and-rate-controls.html">Understanding targets and rate controls in State Manager associations</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            schedule_expression: <p>A cron expression when the association will be applied to the targets.</p>
            output_location: <p>An Amazon Simple Storage Service (Amazon S3) bucket where you want to store the output details of the request.</p>
            association_name: <p>Specify a descriptive name for the association.</p>
            automation_target_parameter_name: <p>Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a tool in Amazon Web Services Systems Manager.</p>
            max_errors: <p>The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set <code>MaxError</code> to 10%, then the system stops sending the request when the sixth error is received.</p> <p>Executions that are already running an association when <code>MaxErrors</code> is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set <code>MaxConcurrency</code> to 1 so that executions proceed one at a time.</p>
            max_concurrency: <p>The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.</p> <p>If a new managed node starts and attempts to run an association while Systems Manager is running <code>MaxConcurrency</code> associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for <code>MaxConcurrency</code>.</p>
            compliance_severity: <p>The severity level to assign to the association.</p>
            sync_compliance: <p>The mode for generating association compliance. You can specify <code>AUTO</code> or <code>MANUAL</code>. In <code>AUTO</code> mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is <code>COMPLIANT</code>. If the association execution doesn't run successfully, the association is <code>NON-COMPLIANT</code>.</p> <p>In <code>MANUAL</code> mode, you must specify the <code>AssociationId</code> as a parameter for the <a>PutComplianceItems</a> API operation. In this case, compliance data isn't managed by State Manager. It is managed by your direct call to the <a>PutComplianceItems</a> API operation.</p> <p>By default, all associations use <code>AUTO</code> mode.</p>
            apply_only_at_cron_interval: <p>By default, when you create a new association, the system runs it immediately after it is created and then according to the schedule you specified and when target changes are detected. Specify <code>true</code> for <code>ApplyOnlyAtCronInterval</code>if you want the association to run only according to the schedule you specified.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#state-manager-about-scheduling">Understanding when associations are applied to resources</a> and <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#runbook-target-updates">>About target updates with Automation runbooks</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>This parameter isn't supported for rate expressions.</p>
            calendar_names: <p>The names of Amazon Resource Names (ARNs) of the Change Calendar type documents you want to gate your associations under. The associations only run when that change calendar is open. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar">Amazon Web Services Systems Manager Change Calendar</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            target_locations: <p>A location is a combination of Amazon Web Services Regions and Amazon Web Services accounts where you want to run the association. Use this action to create an association in multiple Regions and multiple accounts.</p> <note> <p>The <code>TargetLocationAlarmConfiguration</code> parameter is not supported by State Manager.</p> </note>
            schedule_offset: <p>Number of days to wait after the scheduled day to run an association. For example, if you specified a cron schedule of <code>cron(0 0 ? * THU#2 *)</code>, you could specify an offset of 3 to run the association each Sunday after the second Thursday of the month. For more information about cron schedules for associations, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html">Reference: Cron and rate expressions for Systems Manager</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p> <note> <p>To use offsets, you must specify the <code>ApplyOnlyAtCronInterval</code> parameter. This option tells the system not to run an association immediately after you create it. </p> </note>
            duration: <p>The number of hours the association can run before it is canceled. Duration applies to associations that are currently running, and any pending and in progress commands on all targets. If a target was taken offline for the association to run, it is made available again immediately, without a reboot. </p> <p>The <code>Duration</code> parameter applies only when both these conditions are true:</p> <ul> <li> <p>The association for which you specify a duration is cancelable according to the parameters of the SSM command document or Automation runbook associated with this execution. </p> </li> <li> <p>The command specifies the <code> <a href="https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_CreateAssociation.html#systemsmanager-CreateAssociation-request-ApplyOnlyAtCronInterval">ApplyOnlyAtCronInterval</a> </code> parameter, which means that the association doesn't run immediately after it is created, but only according to the specified schedule.</p> </li> </ul>
            target_maps: <p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>
            tags: <p>Adds or overwrites one or more tags for a State Manager association. <i>Tags</i> are metadata that you can assign to your Amazon Web Services resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. Each tag consists of a key and an optional value, both of which you define. </p>
            association_dispatch_assume_role: <p>A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html"> service-linked role for Systems Manager</a> will be used by default. </p> <note> <p>It is recommended that you define a custom IAM role so that you have full control of the permissions that State Manager has when taking actions on your behalf.</p> <p>Service-linked role support in State Manager is being phased out. Associations relying on service-linked role may require updates in the future to continue functioning properly.</p> </note>

        Raises:
            capo_ssm.errors.association_already_exists.AssociationAlreadyExists: <p>The specified association already exists.</p>
            capo_ssm.errors.association_limit_exceeded.AssociationLimitExceeded: <p>You can have at most 2,000 active associations.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_output_location.InvalidOutputLocation: <p>The output location isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_parameters.InvalidParameters: <p>You must specify values for all required parameters in the Amazon Web Services Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.</p>
            capo_ssm.errors.invalid_schedule.InvalidSchedule: <p>The schedule is invalid. Verify your cron or rate expression and try again.</p>
            capo_ssm.errors.invalid_tag.InvalidTag: <p>The specified tag key or value isn't valid.</p>
            capo_ssm.errors.invalid_target.InvalidTarget: <p>The target isn't valid or doesn't exist. It might not be configured for Systems Manager or you might not have permission to perform the operation.</p>
            capo_ssm.errors.invalid_target_maps.InvalidTargetMaps: <p>TargetMap parameter isn't valid.</p>
            capo_ssm.errors.unsupported_platform_type.UnsupportedPlatformType: <p>The document doesn't support the platform type of the given managed node IDs. For example, you sent an document for a Windows managed node to a Linux node.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_association_request.CreateAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_association_result.CreateAssociationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_association

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_association.async_create_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_association_request.CreateAssociationRequest = {
            "name": name
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if parameters is not None:
            input_["parameters"] = parameters
        if targets is not None:
            input_["targets"] = targets
        if schedule_expression is not None:
            input_["schedule_expression"] = schedule_expression
        if output_location is not None:
            input_["output_location"] = output_location
        if association_name is not None:
            input_["association_name"] = association_name
        if automation_target_parameter_name is not None:
            input_["automation_target_parameter_name"] = (
                automation_target_parameter_name
            )
        if max_errors is not None:
            input_["max_errors"] = max_errors
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if compliance_severity is not None:
            input_["compliance_severity"] = compliance_severity
        if sync_compliance is not None:
            input_["sync_compliance"] = sync_compliance
        if apply_only_at_cron_interval is not None:
            input_["apply_only_at_cron_interval"] = apply_only_at_cron_interval
        if calendar_names is not None:
            input_["calendar_names"] = calendar_names
        if target_locations is not None:
            input_["target_locations"] = target_locations
        if schedule_offset is not None:
            input_["schedule_offset"] = schedule_offset
        if duration is not None:
            input_["duration"] = duration
        if target_maps is not None:
            input_["target_maps"] = target_maps
        if tags is not None:
            input_["tags"] = tags
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration
        if association_dispatch_assume_role is not None:
            input_["association_dispatch_assume_role"] = (
                association_dispatch_assume_role
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_association_batch(
        self,
        entries: "capo_ssm.types.create_association_batch_request_entries.CreateAssociationBatchRequestEntries",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        association_dispatch_assume_role: Optional[
            "capo_ssm.types.association_dispatch_assume_role_arn.AssociationDispatchAssumeRoleArn"
        ] = None,
    ) -> "capo_ssm.types.create_association_batch_result.CreateAssociationBatchResult":
        """<p>Associates the specified Amazon Web Services Systems Manager document (SSM document) with the specified managed nodes or targets.</p> <p>When you associate a document with one or more managed nodes using IDs or tags, Amazon Web Services Systems Manager Agent (SSM Agent) running on the managed node processes the document and configures the node as specified.</p> <p>If you associate a document with a managed node that already has an associated document, the system returns the AssociationAlreadyExists exception.</p>

        Args:
            entries: <p>One or more associations.</p>
            association_dispatch_assume_role: <p>A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html"> service-linked role for Systems Manager</a> will be used by default. </p> <note> <p>It is recommended that you define a custom IAM role so that you have full control of the permissions that State Manager has when taking actions on your behalf.</p> <p>Service-linked role support in State Manager is being phased out. Associations relying on service-linked role may require updates in the future to continue functioning properly.</p> </note>

        Raises:
            capo_ssm.errors.association_limit_exceeded.AssociationLimitExceeded: <p>You can have at most 2,000 active associations.</p>
            capo_ssm.errors.duplicate_instance_id.DuplicateInstanceId: <p>You can't specify a managed node ID in more than one association.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_output_location.InvalidOutputLocation: <p>The output location isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_parameters.InvalidParameters: <p>You must specify values for all required parameters in the Amazon Web Services Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.</p>
            capo_ssm.errors.invalid_schedule.InvalidSchedule: <p>The schedule is invalid. Verify your cron or rate expression and try again.</p>
            capo_ssm.errors.invalid_target.InvalidTarget: <p>The target isn't valid or doesn't exist. It might not be configured for Systems Manager or you might not have permission to perform the operation.</p>
            capo_ssm.errors.invalid_target_maps.InvalidTargetMaps: <p>TargetMap parameter isn't valid.</p>
            capo_ssm.errors.unsupported_platform_type.UnsupportedPlatformType: <p>The document doesn't support the platform type of the given managed node IDs. For example, you sent an document for a Windows managed node to a Linux node.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_association_batch_request.CreateAssociationBatchRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_association_batch_result.CreateAssociationBatchResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_association_batch

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_association_batch.async_create_association_batch(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_association_batch_request.CreateAssociationBatchRequest = {
            "entries": entries
        }
        if association_dispatch_assume_role is not None:
            input_["association_dispatch_assume_role"] = (
                association_dispatch_assume_role
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_cloud_connector(
        self,
        display_name: "capo_ssm.types.display_name.DisplayName",
        role_arn: "capo_ssm.types.cloud_connector_iam_role_arn.CloudConnectorIamRoleArn",
        configuration: "capo_ssm.types.cloud_connector_configuration.CloudConnectorConfiguration",
        config_connector_arn: "capo_ssm.types.config_connector_arn.ConfigConnectorArn",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        description: Optional[
            "capo_ssm.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
    ) -> "capo_ssm.types.create_cloud_connector_result.CreateCloudConnectorResult":
        """<p>Creates a cloud connector that establishes a connection between Systems Manager and a third-party cloud environment.</p>

        Args:
            display_name: <p>A friendly name for the cloud connector.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of the IAM role that the cloud connector uses to communicate with the third-party cloud environment.</p>
            description: <p>A description for the cloud connector.</p>
            configuration: <p>The configuration details for connecting to the third-party cloud environment.</p>
            config_connector_arn: <p>The ARN of the Amazon Web Services Config connector associated with this cloud connector.</p>
            tags: <p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment.</p>

        Raises:
            capo_ssm.errors.conflict_exception.ConflictException: <p>An error occurred because of a conflict with a concurrent request or the current state of the resource. Retry your request.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_cloud_connector_request.CreateCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_cloud_connector_result.CreateCloudConnectorResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_cloud_connector

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_cloud_connector.async_create_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_cloud_connector_request.CreateCloudConnectorRequest = {
            "display_name": display_name,
            "role_arn": role_arn,
            "configuration": configuration,
            "config_connector_arn": config_connector_arn,
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

    async def create_document(
        self,
        content: "capo_ssm.types.document_content.DocumentContent",
        name: "capo_ssm.types.document_name.DocumentName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        requires: Optional[
            "capo_ssm.types.document_requires_list.DocumentRequiresList"
        ] = None,
        attachments: Optional[
            "capo_ssm.types.attachments_source_list.AttachmentsSourceList"
        ] = None,
        display_name: Optional[
            "capo_ssm.types.document_display_name.DocumentDisplayName"
        ] = None,
        version_name: Optional[
            "capo_ssm.types.document_version_name.DocumentVersionName"
        ] = None,
        document_type: Optional["capo_ssm.types.document_type.DocumentType"] = None,
        document_format: Optional[
            "capo_ssm.types.document_format.DocumentFormat"
        ] = None,
        target_type: Optional["capo_ssm.types.target_type.TargetType"] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
    ) -> "capo_ssm.types.create_document_result.CreateDocumentResult":
        """<p>Creates a Amazon Web Services Systems Manager (SSM document). An SSM document defines the actions that Systems Manager performs on your managed nodes. For more information about SSM documents, including information about supported schemas, features, and syntax, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents.html">Amazon Web Services Systems Manager Documents</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>

        Args:
            content: <p>The content for the new SSM document in JSON or YAML format. The content of the document must not exceed 64KB. This quota also includes the content specified for input parameters at runtime. We recommend storing the contents for your new document in an external JSON or YAML file and referencing the file in a command.</p> <p>For examples, see the following topics in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-console">Create an SSM document (console)</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-document-cli">Create an SSM document (command line)</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-using.html#create-ssm-document-api">Create an SSM document (API)</a> </p> </li> </ul>
            requires: <p>A list of SSM documents required by a document. This parameter is used exclusively by AppConfig. When a user creates an AppConfig configuration in an SSM document, the user must also specify a required document for validation purposes. In this case, an <code>ApplicationConfiguration</code> document requires an <code>ApplicationConfigurationSchema</code> document for validation purposes. For more information, see <a href="https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html">What is AppConfig?</a> in the <i>AppConfig User Guide</i>.</p>
            attachments: <p>A list of key-value pairs that describe attachments to a version of a document.</p>
            name: <p>A name for the SSM document.</p> <important> <p>You can't use the following strings as document name prefixes. These are reserved by Amazon Web Services for use as document name prefixes:</p> <ul> <li> <p> <code>aws</code> </p> </li> <li> <p> <code>amazon</code> </p> </li> <li> <p> <code>amzn</code> </p> </li> <li> <p> <code>AWSEC2</code> </p> </li> <li> <p> <code>AWSConfigRemediation</code> </p> </li> <li> <p> <code>AWSSupport</code> </p> </li> </ul> </important>
            display_name: <p>An optional field where you can specify a friendly name for the SSM document. This value can differ for each version of the document. You can update this value at a later time using the <a>UpdateDocument</a> operation.</p>
            version_name: <p>An optional field specifying the version of the artifact you are creating with the document. For example, <code>Release12.1</code>. This value is unique across all versions of a document, and can't be changed.</p>
            document_type: <p>The type of document to create.</p> <note> <p>The <code>DeploymentStrategy</code> document type is an internal-use-only document type reserved for AppConfig.</p> </note>
            document_format: <p>Specify the document format for the request. The document format can be JSON, YAML, or TEXT. JSON is the default format.</p>
            target_type: <p>Specify a target type to define the kinds of resources the document can run on. For example, to run a document on EC2 instances, specify the following value: <code>/AWS::EC2::Instance</code>. If you specify a value of '/' the document can run on all types of resources. If you don't specify a value, the document can't run on any resources. For a list of valid resource types, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">Amazon Web Services resource and property types reference</a> in the <i>CloudFormation User Guide</i>. </p>
            tags: <p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an SSM document to identify the types of targets or the environment where it will run. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> </ul> <note> <p>To add tags to an existing SSM document, use the <a>AddTagsToResource</a> operation.</p> </note>

        Raises:
            capo_ssm.errors.document_already_exists.DocumentAlreadyExists: <p>The specified document already exists.</p>
            capo_ssm.errors.document_limit_exceeded.DocumentLimitExceeded: <p>You can have at most 500 active SSM documents.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document_content.InvalidDocumentContent: <p>The content for the document isn't valid.</p>
            capo_ssm.errors.invalid_document_schema_version.InvalidDocumentSchemaVersion: <p>The version of the document schema isn't supported.</p>
            capo_ssm.errors.max_document_size_exceeded.MaxDocumentSizeExceeded: <p>The size limit of a document is 64 KB.</p>
            capo_ssm.errors.no_longer_supported_exception.NoLongerSupportedException: <p>The requested operation is no longer supported by Systems Manager.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_document_request.CreateDocumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_document_result.CreateDocumentResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_document

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_document.async_create_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_document_request.CreateDocumentRequest = {
            "content": content,
            "name": name,
        }
        if requires is not None:
            input_["requires"] = requires
        if attachments is not None:
            input_["attachments"] = attachments
        if display_name is not None:
            input_["display_name"] = display_name
        if version_name is not None:
            input_["version_name"] = version_name
        if document_type is not None:
            input_["document_type"] = document_type
        if document_format is not None:
            input_["document_format"] = document_format
        if target_type is not None:
            input_["target_type"] = target_type
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_maintenance_window(
        self,
        name: "capo_ssm.types.maintenance_window_name.MaintenanceWindowName",
        schedule: "capo_ssm.types.maintenance_window_schedule.MaintenanceWindowSchedule",
        duration: "capo_ssm.types.maintenance_window_duration_hours.MaintenanceWindowDurationHours",
        cutoff: "capo_ssm.types.maintenance_window_cutoff.MaintenanceWindowCutoff",
        allow_unassociated_targets: "capo_ssm.types.maintenance_window_allow_unassociated_targets.MaintenanceWindowAllowUnassociatedTargets",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        description: Optional[
            "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
        ] = None,
        start_date: Optional[
            "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
        ] = None,
        end_date: Optional[
            "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
        ] = None,
        schedule_timezone: Optional[
            "capo_ssm.types.maintenance_window_timezone.MaintenanceWindowTimezone"
        ] = None,
        schedule_offset: Optional[
            "capo_ssm.types.maintenance_window_offset.MaintenanceWindowOffset"
        ] = None,
        client_token: Optional["capo_ssm.types.client_token.ClientToken"] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
    ) -> (
        "capo_ssm.types.create_maintenance_window_result.CreateMaintenanceWindowResult"
    ):
        """<p>Creates a new maintenance window.</p> <note> <p>The value you specify for <code>Duration</code> determines the specific end time for the maintenance window based on the time it begins. No maintenance window tasks are permitted to start after the resulting endtime minus the number of hours you specify for <code>Cutoff</code>. For example, if the maintenance window starts at 3 PM, the duration is three hours, and the value you specify for <code>Cutoff</code> is one hour, no maintenance window tasks can start after 5 PM.</p> </note>

        Args:
            name: <p>The name of the maintenance window.</p>
            description: <p>An optional description for the maintenance window. We recommend specifying a description to help you organize your maintenance windows. </p>
            start_date: <p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. <code>StartDate</code> allows you to delay activation of the maintenance window until the specified future date.</p> <note> <p>When using a rate schedule, if you provide a start date that occurs in the past, the current date and time are used as the start date. </p> </note>
            end_date: <p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. <code>EndDate</code> allows you to set a date and time in the future when the maintenance window will no longer run.</p>
            schedule: <p>The schedule of the maintenance window in the form of a cron or rate expression.</p>
            schedule_timezone: <p>The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the <a href="https://www.iana.org/time-zones">Time Zone Database</a> on the IANA website.</p>
            schedule_offset: <p>The number of days to wait after the date and time specified by a cron expression before running the maintenance window.</p> <p>For example, the following cron expression schedules a maintenance window to run on the third Tuesday of every month at 11:30 PM.</p> <p> <code>cron(30 23 ? * TUE#3 *)</code> </p> <p>If the schedule offset is <code>2</code>, the maintenance window won't run until two days later.</p>
            duration: <p>The duration of the maintenance window in hours.</p>
            cutoff: <p>The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.</p>
            allow_unassociated_targets: <p>Enables a maintenance window task to run on managed nodes, even if you haven't registered those nodes as targets. If enabled, then you must specify the unregistered managed nodes (by node ID) when you register a task with the maintenance window.</p> <p>If you don't enable this option, then you must specify previously-registered targets when you register a task with the maintenance window.</p>
            client_token: <p>User-provided idempotency token.</p>
            tags: <p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a maintenance window to identify the type of tasks it will run, the types of targets, and the environment it will run in. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=TaskType,Value=AgentUpdate</code> </p> </li> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> </ul> <note> <p>To add tags to an existing maintenance window, use the <a>AddTagsToResource</a> operation.</p> </note>

        Raises:
            capo_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch: <p>Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.</p> <p>For information about resource quotas in Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_maintenance_window_request.CreateMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_maintenance_window_result.CreateMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_maintenance_window.async_create_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_maintenance_window_request.CreateMaintenanceWindowRequest = {
            "name": name,
            "schedule": schedule,
            "duration": duration,
            "cutoff": cutoff,
            "allow_unassociated_targets": allow_unassociated_targets,
        }
        if description is not None:
            input_["description"] = description
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if schedule_timezone is not None:
            input_["schedule_timezone"] = schedule_timezone
        if schedule_offset is not None:
            input_["schedule_offset"] = schedule_offset
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

    async def create_ops_item(
        self,
        description: "capo_ssm.types.ops_item_description.OpsItemDescription",
        source: "capo_ssm.types.ops_item_source.OpsItemSource",
        title: "capo_ssm.types.ops_item_title.OpsItemTitle",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        ops_item_type: Optional["capo_ssm.types.ops_item_type.OpsItemType"] = None,
        operational_data: Optional[
            "capo_ssm.types.ops_item_operational_data.OpsItemOperationalData"
        ] = None,
        notifications: Optional[
            "capo_ssm.types.ops_item_notifications.OpsItemNotifications"
        ] = None,
        priority: Optional["capo_ssm.types.ops_item_priority.OpsItemPriority"] = None,
        related_ops_items: Optional[
            "capo_ssm.types.related_ops_items.RelatedOpsItems"
        ] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
        category: Optional["capo_ssm.types.ops_item_category.OpsItemCategory"] = None,
        severity: Optional["capo_ssm.types.ops_item_severity.OpsItemSeverity"] = None,
        actual_start_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        actual_end_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        planned_start_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        planned_end_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        account_id: Optional[
            "capo_ssm.types.ops_item_account_id.OpsItemAccountId"
        ] = None,
    ) -> "capo_ssm.types.create_ops_item_response.CreateOpsItemResponse":
        """<p>Creates a new OpsItem. You must have permission in Identity and Access Management (IAM) to create a new OpsItem. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html">Set up OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html">Amazon Web Services Systems Manager OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>

        Args:
            description: <p>User-defined text that contains information about the OpsItem, in Markdown format. </p> <note> <p>Provide enough information so that users viewing this OpsItem for the first time understand the issue. </p> </note>
            ops_item_type: <p>The type of OpsItem to create. Systems Manager supports the following types of OpsItems:</p> <ul> <li> <p> <code>/aws/issue</code> </p> <p>This type of OpsItem is used for default OpsItems created by OpsCenter. </p> </li> <li> <p> <code>/aws/insight</code> </p> <p>This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems. </p> </li> <li> <p> <code>/aws/changerequest</code> </p> <p>This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests. </p> <important> <p>Amazon Web Services Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html">Amazon Web Services Systems Manager Change Manager availability change</a>.</p> </important> </li> </ul>
            operational_data: <p>Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.</p> <important> <p>Operational data keys <i>can't</i> begin with the following: <code>amazon</code>, <code>aws</code>, <code>amzn</code>, <code>ssm</code>, <code>/amazon</code>, <code>/aws</code>, <code>/amzn</code>, <code>/ssm</code>.</p> </important> <p>You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the <a>DescribeOpsItems</a> API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the <a>GetOpsItem</a> API operation).</p> <p>Use the <code>/aws/resources</code> key in OperationalData to specify a related resource in the request. Use the <code>/aws/automations</code> key in OperationalData to associate an Automation runbook with the OpsItem. To view Amazon Web Services CLI example commands that use these keys, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html">Create OpsItems manually</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            notifications: <p>The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.</p>
            priority: <p>The importance of this OpsItem in relation to other OpsItems in the system.</p>
            related_ops_items: <p>One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.</p>
            source: <p>The origin of the OpsItem, such as Amazon EC2 or Systems Manager.</p> <note> <p>The source name can't contain the following strings: <code>aws</code>, <code>amazon</code>, and <code>amzn</code>. </p> </note>
            title: <p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>
            tags: <p>Optional metadata that you assign to a resource.</p> <p>Tags use a key-value pair. For example:</p> <p> <code>Key=Department,Value=Finance</code> </p> <important> <p>To add tags to a new OpsItem, a user must have IAM permissions for both the <code>ssm:CreateOpsItems</code> operation and the <code>ssm:AddTagsToResource</code> operation. To add tags to an existing OpsItem, use the <a>AddTagsToResource</a> operation.</p> </important>
            category: <p>Specify a category to assign to an OpsItem. </p>
            severity: <p>Specify a severity to assign to an OpsItem.</p>
            actual_start_time: <p>The time a runbook workflow started. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            actual_end_time: <p>The time a runbook workflow ended. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            planned_start_time: <p>The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            planned_end_time: <p>The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            account_id: <p>The target Amazon Web Services account where you want to create an OpsItem. To make this call, your account must be configured to work with OpsItems across accounts. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html">Set up OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_access_denied_exception.OpsItemAccessDeniedException: <p>You don't have permission to view OpsItems in the specified account. Verify that your account is configured either as a Systems Manager delegated administrator or that you are logged into the Organizations management account.</p>
            capo_ssm.errors.ops_item_already_exists_exception.OpsItemAlreadyExistsException: <p>The OpsItem already exists.</p>
            capo_ssm.errors.ops_item_invalid_parameter_exception.OpsItemInvalidParameterException: <p>A specified parameter argument isn't valid. Verify the available arguments and try again.</p>
            capo_ssm.errors.ops_item_limit_exceeded_exception.OpsItemLimitExceededException: <p>The request caused OpsItems to exceed one or more quotas.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_ops_item_request.CreateOpsItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_ops_item_response.CreateOpsItemResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.create_ops_item

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_ops_item.async_create_ops_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_ops_item_request.CreateOpsItemRequest = {
            "description": description,
            "source": source,
            "title": title,
        }
        if ops_item_type is not None:
            input_["ops_item_type"] = ops_item_type
        if operational_data is not None:
            input_["operational_data"] = operational_data
        if notifications is not None:
            input_["notifications"] = notifications
        if priority is not None:
            input_["priority"] = priority
        if related_ops_items is not None:
            input_["related_ops_items"] = related_ops_items
        if tags is not None:
            input_["tags"] = tags
        if category is not None:
            input_["category"] = category
        if severity is not None:
            input_["severity"] = severity
        if actual_start_time is not None:
            input_["actual_start_time"] = actual_start_time
        if actual_end_time is not None:
            input_["actual_end_time"] = actual_end_time
        if planned_start_time is not None:
            input_["planned_start_time"] = planned_start_time
        if planned_end_time is not None:
            input_["planned_end_time"] = planned_end_time
        if account_id is not None:
            input_["account_id"] = account_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_ops_metadata(
        self,
        resource_id: "capo_ssm.types.ops_metadata_resource_id.OpsMetadataResourceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        metadata: Optional["capo_ssm.types.metadata_map.MetadataMap"] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
    ) -> "capo_ssm.types.create_ops_metadata_result.CreateOpsMetadataResult":
        """<p>If you create a new application in Application Manager, Amazon Web Services Systems Manager calls this API operation to specify information about the new application, including the application type.</p>

        Args:
            resource_id: <p>A resource ID for a new Application Manager application.</p>
            metadata: <p>Metadata for a new Application Manager application. </p>
            tags: <p>Optional metadata that you assign to a resource. You can specify a maximum of five tags for an OpsMetadata object. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an OpsMetadata object to identify an environment or target Amazon Web Services Region. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> <li> <p> <code>Key=Region,Value=us-east-2</code> </p> </li> </ul>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_metadata_already_exists_exception.OpsMetadataAlreadyExistsException: <p>An OpsMetadata object already exists for the selected resource.</p>
            capo_ssm.errors.ops_metadata_invalid_argument_exception.OpsMetadataInvalidArgumentException: <p>One of the arguments passed is invalid. </p>
            capo_ssm.errors.ops_metadata_limit_exceeded_exception.OpsMetadataLimitExceededException: <p>Your account reached the maximum number of OpsMetadata objects allowed by Application Manager. The maximum is 200 OpsMetadata objects. Delete one or more OpsMetadata object and try again.</p>
            capo_ssm.errors.ops_metadata_too_many_updates_exception.OpsMetadataTooManyUpdatesException: <p>The system is processing too many concurrent updates. Wait a few moments and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_ops_metadata_request.CreateOpsMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_ops_metadata_result.CreateOpsMetadataResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_ops_metadata

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_ops_metadata.async_create_ops_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_ops_metadata_request.CreateOpsMetadataRequest = {
            "resource_id": resource_id
        }
        if metadata is not None:
            input_["metadata"] = metadata
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_patch_baseline(
        self,
        name: "capo_ssm.types.baseline_name.BaselineName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        operating_system: Optional[
            "capo_ssm.types.operating_system.OperatingSystem"
        ] = None,
        global_filters: Optional[
            "capo_ssm.types.patch_filter_group.PatchFilterGroup"
        ] = None,
        approval_rules: Optional[
            "capo_ssm.types.patch_rule_group.PatchRuleGroup"
        ] = None,
        approved_patches: Optional["capo_ssm.types.patch_id_list.PatchIdList"] = None,
        approved_patches_compliance_level: Optional[
            "capo_ssm.types.patch_compliance_level.PatchComplianceLevel"
        ] = None,
        approved_patches_enable_non_security: Optional[
            "capo_ssm.types.boolean.Boolean"
        ] = None,
        rejected_patches: Optional["capo_ssm.types.patch_id_list.PatchIdList"] = None,
        rejected_patches_action: Optional[
            "capo_ssm.types.patch_action.PatchAction"
        ] = None,
        description: Optional[
            "capo_ssm.types.baseline_description.BaselineDescription"
        ] = None,
        sources: Optional["capo_ssm.types.patch_source_list.PatchSourceList"] = None,
        available_security_updates_compliance_status: Optional[
            "capo_ssm.types.patch_compliance_status.PatchComplianceStatus"
        ] = None,
        client_token: Optional["capo_ssm.types.client_token.ClientToken"] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
    ) -> "capo_ssm.types.create_patch_baseline_result.CreatePatchBaselineResult":
        """<p>Creates a patch baseline.</p> <note> <p>For information about valid key-value pairs in <code>PatchFilters</code> for each supported operating system type, see <a>PatchFilter</a>.</p> </note>

        Args:
            operating_system: <p>Defines the operating system the patch baseline applies to. The default value is <code>WINDOWS</code>.</p>
            name: <p>The name of the patch baseline.</p>
            global_filters: <p>A set of global filters used to include patches in the baseline.</p> <important> <p>The <code>GlobalFilters</code> parameter can be configured only by using the CLI or an Amazon Web Services SDK. It can't be configured from the Patch Manager console, and its value isn't displayed in the console.</p> </important>
            approval_rules: <p>A set of rules used to include patches in the baseline.</p>
            approved_patches: <p>A list of explicitly approved patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            approved_patches_compliance_level: <p>Defines the compliance level for approved patches. When an approved patch is reported as missing, this value describes the severity of the compliance violation. The default value is <code>UNSPECIFIED</code>.</p>
            approved_patches_enable_non_security: <p>Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is <code>false</code>. Applies to Linux managed nodes only.</p>
            rejected_patches: <p>A list of explicitly rejected patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            rejected_patches_action: <p>The action for Patch Manager to take on patches included in the <code>RejectedPackages</code> list.</p> <dl> <dt>ALLOW_AS_DEPENDENCY</dt> <dd> <p> <b>Linux and macOS</b>: A package in the rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as <code>INSTALLED_OTHER</code>. This is the default action if no option is specified.</p> <p> <b>Windows Server</b>: Windows Server doesn't support the concept of package dependencies. If a package in the rejected patches list and already installed on the node, its status is reported as <code>INSTALLED_OTHER</code>. Any package not already installed on the node is skipped. This is the default action if no option is specified.</p> </dd> <dt>BLOCK</dt> <dd> <p> <b>All OSs</b>: Packages in the rejected patches list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances. </p> <p>State value assignment for patch compliance:</p> <ul> <li> <p>If a package was installed before it was added to the rejected patches list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as <code>INSTALLED_REJECTED</code>.</p> </li> <li> <p>If an update attempts to install a dependency package that is now rejected by the baseline, when previous versions of the package were not rejected, the package being updated is reported as <code>MISSING</code> for <code>SCAN</code> operations and as <code>FAILED</code> for <code>INSTALL</code> operations.</p> </li> </ul> </dd> </dl>
            description: <p>A description of the patch baseline.</p>
            sources: <p>Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.</p>
            available_security_updates_compliance_status: <p>Indicates the status you want to assign to security patches that are available but not approved because they don't meet the installation criteria specified in the patch baseline.</p> <p>Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.</p> <p>Supported for Windows Server managed nodes only.</p>
            client_token: <p>User-provided idempotency token.</p>
            tags: <p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a patch baseline to identify the severity level of patches it specifies and the operating system family it applies to. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=PatchSeverity,Value=Critical</code> </p> </li> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> </ul> <note> <p>To add tags to an existing patch baseline, use the <a>AddTagsToResource</a> operation.</p> </note>

        Raises:
            capo_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch: <p>Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.</p> <p>For information about resource quotas in Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_patch_baseline_request.CreatePatchBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_patch_baseline_result.CreatePatchBaselineResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_patch_baseline

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_patch_baseline.async_create_patch_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_patch_baseline_request.CreatePatchBaselineRequest = {
            "name": name
        }
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if global_filters is not None:
            input_["global_filters"] = global_filters
        if approval_rules is not None:
            input_["approval_rules"] = approval_rules
        if approved_patches is not None:
            input_["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None:
            input_["approved_patches_compliance_level"] = (
                approved_patches_compliance_level
            )
        if approved_patches_enable_non_security is not None:
            input_["approved_patches_enable_non_security"] = (
                approved_patches_enable_non_security
            )
        if rejected_patches is not None:
            input_["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None:
            input_["rejected_patches_action"] = rejected_patches_action
        if description is not None:
            input_["description"] = description
        if sources is not None:
            input_["sources"] = sources
        if available_security_updates_compliance_status is not None:
            input_["available_security_updates_compliance_status"] = (
                available_security_updates_compliance_status
            )
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

    async def create_resource_data_sync(
        self,
        sync_name: "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        s3_destination: Optional[
            "capo_ssm.types.resource_data_sync_s3_destination.ResourceDataSyncS3Destination"
        ] = None,
        sync_type: Optional[
            "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
        ] = None,
        sync_source: Optional[
            "capo_ssm.types.resource_data_sync_source.ResourceDataSyncSource"
        ] = None,
    ) -> "capo_ssm.types.create_resource_data_sync_result.CreateResourceDataSyncResult":
        """<p>A resource data sync helps you view data from multiple sources in a single location. Amazon Web Services Systems Manager offers two types of resource data sync: <code>SyncToDestination</code> and <code>SyncFromSource</code>.</p> <p>You can configure Systems Manager Inventory to use the <code>SyncToDestination</code> type to synchronize Inventory data from multiple Amazon Web Services Regions to a single Amazon Simple Storage Service (Amazon S3) bucket. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/inventory-create-resource-data-sync.html">Creating a resource data sync for Inventory</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>You can configure Systems Manager Explorer to use the <code>SyncFromSource</code> type to synchronize operational work items (OpsItems) and operational data (OpsData) from multiple Amazon Web Services Regions to a single Amazon S3 bucket. This type can synchronize OpsItems and OpsData from multiple Amazon Web Services accounts and Amazon Web Services Regions or <code>EntireOrganization</code> by using Organizations. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/Explorer-resource-data-sync.html">Setting up Systems Manager Explorer to display data from multiple accounts and Regions</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>A resource data sync is an asynchronous operation that returns immediately. After a successful initial sync is completed, the system continuously syncs data. To check the status of a sync, use the <a>ListResourceDataSync</a>.</p> <note> <p>By default, data isn't encrypted in Amazon S3. We strongly recommend that you enable encryption in Amazon S3 to ensure secure data storage. We also recommend that you secure access to the Amazon S3 bucket by creating a restrictive bucket policy. </p> </note>

        Args:
            sync_name: <p>A name for the configuration.</p>
            s3_destination: <p>Amazon S3 configuration details for the sync. This parameter is required if the <code>SyncType</code> value is SyncToDestination.</p>
            sync_type: <p>Specify <code>SyncToDestination</code> to create a resource data sync that synchronizes data to an S3 bucket for Inventory. If you specify <code>SyncToDestination</code>, you must provide a value for <code>S3Destination</code>. Specify <code>SyncFromSource</code> to synchronize data from a single account and multiple Regions, or multiple Amazon Web Services accounts and Amazon Web Services Regions, as listed in Organizations for Explorer. If you specify <code>SyncFromSource</code>, you must provide a value for <code>SyncSource</code>. The default value is <code>SyncToDestination</code>.</p>
            sync_source: <p>Specify information about the data sources to synchronize. This parameter is required if the <code>SyncType</code> value is SyncFromSource.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_data_sync_already_exists_exception.ResourceDataSyncAlreadyExistsException: <p>A sync configuration with the same name already exists.</p>
            capo_ssm.errors.resource_data_sync_count_exceeded_exception.ResourceDataSyncCountExceededException: <p>You have exceeded the allowed maximum sync configurations.</p>
            capo_ssm.errors.resource_data_sync_invalid_configuration_exception.ResourceDataSyncInvalidConfigurationException: <p>The specified sync configuration is invalid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.create_resource_data_sync_request.CreateResourceDataSyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.create_resource_data_sync_result.CreateResourceDataSyncResult"
        ]:
            import capo_ssm._operations.amazon_ssm.create_resource_data_sync

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.create_resource_data_sync.async_create_resource_data_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.create_resource_data_sync_request.CreateResourceDataSyncRequest = {
            "sync_name": sync_name
        }
        if s3_destination is not None:
            input_["s3_destination"] = s3_destination
        if sync_type is not None:
            input_["sync_type"] = sync_type
        if sync_source is not None:
            input_["sync_source"] = sync_source

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_activation(
        self,
        activation_id: "capo_ssm.types.activation_id.ActivationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.delete_activation_result.DeleteActivationResult":
        """<p>Deletes an activation. You aren't required to delete an activation. If you delete an activation, you can no longer use it to register additional managed nodes. Deleting an activation doesn't de-register managed nodes. You must manually de-register managed nodes.</p>

        Args:
            activation_id: <p>The ID of the activation that you want to delete.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_activation.InvalidActivation: <p>The activation isn't valid. The activation might have been deleted, or the ActivationId and the ActivationCode don't match.</p>
            capo_ssm.errors.invalid_activation_id.InvalidActivationId: <p>The activation ID isn't valid. Verify that you entered the correct ActivationId or ActivationCode and try again.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_activation_request.DeleteActivationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_activation_result.DeleteActivationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_activation

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_activation.async_delete_activation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_activation_request.DeleteActivationRequest = {
            "activation_id": activation_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_association(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        name: Optional["capo_ssm.types.document_arn.DocumentARN"] = None,
        instance_id: Optional["capo_ssm.types.instance_id.InstanceId"] = None,
        association_id: Optional["capo_ssm.types.association_id.AssociationId"] = None,
    ) -> "capo_ssm.types.delete_association_result.DeleteAssociationResult":
        """<p>Disassociates the specified Amazon Web Services Systems Manager document (SSM document) from the specified managed node. If you created the association by using the <code>Targets</code> parameter, then you must delete the association by using the association ID.</p> <p>When you disassociate a document from a managed node, it doesn't change the configuration of the node. To change the configuration state of a managed node after you disassociate a document, you must create a new document with the desired configuration and associate it with the node.</p>

        Args:
            name: <p>The name of the SSM document.</p>
            instance_id: <p>The managed node ID.</p> <note> <p> <code>InstanceId</code> has been deprecated. To specify a managed node ID for an association, use the <code>Targets</code> parameter. Requests that include the parameter <code>InstanceID</code> with Systems Manager documents (SSM documents) that use schema version 2.0 or later will fail. In addition, if you use the parameter <code>InstanceId</code>, you can't use the parameters <code>AssociationName</code>, <code>DocumentVersion</code>, <code>MaxErrors</code>, <code>MaxConcurrency</code>, <code>OutputLocation</code>, or <code>ScheduleExpression</code>. To use these parameters, you must use the <code>Targets</code> parameter.</p> </note>
            association_id: <p>The association ID that you want to delete.</p>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_association_request.DeleteAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_association_result.DeleteAssociationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_association

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_association.async_delete_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_association_request.DeleteAssociationRequest = {}
        if name is not None:
            input_["name"] = name
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if association_id is not None:
            input_["association_id"] = association_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_cloud_connector(
        self,
        cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.delete_cloud_connector_result.DeleteCloudConnectorResult":
        """<p>Deletes a cloud connector.</p>

        Args:
            cloud_connector_id: <p>The ID of the cloud connector to delete.</p>

        Raises:
            capo_ssm.errors.conflict_exception.ConflictException: <p>An error occurred because of a conflict with a concurrent request or the current state of the resource. Retry your request.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_cloud_connector_request.DeleteCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_cloud_connector_result.DeleteCloudConnectorResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_cloud_connector

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_cloud_connector.async_delete_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_cloud_connector_request.DeleteCloudConnectorRequest = {
            "cloud_connector_id": cloud_connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_document(
        self,
        name: "capo_ssm.types.document_name.DocumentName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        version_name: Optional[
            "capo_ssm.types.document_version_name.DocumentVersionName"
        ] = None,
        force: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.delete_document_result.DeleteDocumentResult":
        """<p>Deletes the Amazon Web Services Systems Manager document (SSM document) and all managed node associations to the document.</p> <p>Before you delete the document, we recommend that you use <a>DeleteAssociation</a> to disassociate all managed nodes that are associated with the document.</p>

        Args:
            name: <p>The name of the document.</p>
            document_version: <p>The version of the document that you want to delete. If not provided, all versions of the document are deleted.</p>
            version_name: <p>The version name of the document that you want to delete. If not provided, all versions of the document are deleted.</p>
            force: <p>Some SSM document types require that you specify a <code>Force</code> flag before you can delete the document. For example, you must specify a <code>Force</code> flag to delete a document of type <code>ApplicationConfigurationSchema</code>. You can restrict access to the <code>Force</code> flag in an Identity and Access Management (IAM) policy.</p>

        Raises:
            capo_ssm.errors.associated_instances.AssociatedInstances: <p>You must disassociate a document from all managed nodes before you can delete it.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_operation.InvalidDocumentOperation: <p>You attempted to delete a document while it is still shared. You must stop sharing the document before you can delete it.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_document_request.DeleteDocumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_document_result.DeleteDocumentResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_document

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_document.async_delete_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_document_request.DeleteDocumentRequest = {
            "name": name
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if version_name is not None:
            input_["version_name"] = version_name
        if force is not None:
            input_["force"] = force

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_inventory(
        self,
        type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        schema_delete_option: Optional[
            "capo_ssm.types.inventory_schema_delete_option.InventorySchemaDeleteOption"
        ] = None,
        dry_run: Optional["capo_ssm.types.dry_run.DryRun"] = None,
        client_token: Optional["capo_ssm.types.uuid.UUID"] = None,
    ) -> "capo_ssm.types.delete_inventory_result.DeleteInventoryResult":
        """<p>Delete a custom inventory type or the data associated with a custom Inventory type. Deleting a custom inventory type is also referred to as deleting a custom inventory schema.</p>

        Args:
            type_name: <p>The name of the custom inventory type for which you want to delete either all previously collected data or the inventory type itself. </p>
            schema_delete_option: <p>Use the <code>SchemaDeleteOption</code> to delete a custom inventory type (schema). If you don't choose this option, the system only deletes existing inventory data associated with the custom inventory type. Choose one of the following options:</p> <p>DisableSchema: If you choose this option, the system ignores all inventory data for the specified version, and any earlier versions. To enable this schema again, you must call the <code>PutInventory</code> operation for a version greater than the disabled version.</p> <p>DeleteSchema: This option deletes the specified custom type from the Inventory service. You can recreate the schema later, if you want.</p>
            dry_run: <p>Use this option to view a summary of the deletion request without deleting any data or the data type. This option is useful when you only want to understand what will be deleted. Once you validate that the data to be deleted is what you intend to delete, you can run the same command without specifying the <code>DryRun</code> option.</p>
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_delete_inventory_parameters_exception.InvalidDeleteInventoryParametersException: <p>One or more of the parameters specified for the delete operation isn't valid. Verify all parameters and try again.</p>
            capo_ssm.errors.invalid_inventory_request_exception.InvalidInventoryRequestException: <p>The request isn't valid.</p>
            capo_ssm.errors.invalid_option_exception.InvalidOptionException: <p>The delete inventory option specified isn't valid. Verify the option and try again.</p>
            capo_ssm.errors.invalid_type_name_exception.InvalidTypeNameException: <p>The parameter type name isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_inventory_request.DeleteInventoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_inventory_result.DeleteInventoryResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_inventory

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_inventory.async_delete_inventory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_inventory_request.DeleteInventoryRequest = {
            "type_name": type_name
        }
        if schema_delete_option is not None:
            input_["schema_delete_option"] = schema_delete_option
        if dry_run is not None:
            input_["dry_run"] = dry_run
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

    async def delete_maintenance_window(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> (
        "capo_ssm.types.delete_maintenance_window_result.DeleteMaintenanceWindowResult"
    ):
        """<p>Deletes a maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window to delete.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_maintenance_window_request.DeleteMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_maintenance_window_result.DeleteMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_maintenance_window.async_delete_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_maintenance_window_request.DeleteMaintenanceWindowRequest = {
            "window_id": window_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ops_item(
        self,
        ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.delete_ops_item_response.DeleteOpsItemResponse":
        """<p>Delete an OpsItem. You must have permission in Identity and Access Management (IAM) to delete an OpsItem. </p> <important> <p>Note the following important information about this operation.</p> <ul> <li> <p>Deleting an OpsItem is irreversible. You can't restore a deleted OpsItem.</p> </li> <li> <p>This operation uses an <i>eventual consistency model</i>, which means the system can take a few minutes to complete this operation. If you delete an OpsItem and immediately call, for example, <a>GetOpsItem</a>, the deleted OpsItem might still appear in the response. </p> </li> <li> <p>This operation is idempotent. The system doesn't throw an exception if you repeatedly call this operation for the same OpsItem. If the first call is successful, all additional calls return the same successful response as the first call.</p> </li> <li> <p>This operation doesn't support cross-account calls. A delegated administrator or management account can't delete OpsItems in other accounts, even if OpsCenter has been set up for cross-account administration. For more information about cross-account administration, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setting-up-cross-account.html">Setting up OpsCenter to centrally manage OpsItems across accounts</a> in the <i>Systems Manager User Guide</i>.</p> </li> </ul> </important>

        Args:
            ops_item_id: <p>The ID of the OpsItem that you want to delete.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_invalid_parameter_exception.OpsItemInvalidParameterException: <p>A specified parameter argument isn't valid. Verify the available arguments and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_ops_item_request.DeleteOpsItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_ops_item_response.DeleteOpsItemResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_ops_item

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_ops_item.async_delete_ops_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_ops_item_request.DeleteOpsItemRequest = {
            "ops_item_id": ops_item_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_ops_metadata(
        self,
        ops_metadata_arn: "capo_ssm.types.ops_metadata_arn.OpsMetadataArn",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.delete_ops_metadata_result.DeleteOpsMetadataResult":
        """<p>Delete OpsMetadata related to an application.</p>

        Args:
            ops_metadata_arn: <p>The Amazon Resource Name (ARN) of an OpsMetadata Object to delete.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_metadata_invalid_argument_exception.OpsMetadataInvalidArgumentException: <p>One of the arguments passed is invalid. </p>
            capo_ssm.errors.ops_metadata_not_found_exception.OpsMetadataNotFoundException: <p>The OpsMetadata object doesn't exist. </p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_ops_metadata_request.DeleteOpsMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_ops_metadata_result.DeleteOpsMetadataResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_ops_metadata

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_ops_metadata.async_delete_ops_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_ops_metadata_request.DeleteOpsMetadataRequest = {
            "ops_metadata_arn": ops_metadata_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_parameter(
        self,
        name: "capo_ssm.types.ps_parameter_name.PSParameterName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.delete_parameter_result.DeleteParameterResult":
        """<p>Delete a parameter from the system. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.</p>

        Args:
            name: <p>The name of the parameter to delete.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.parameter_not_found.ParameterNotFound: <p>The parameter couldn't be found. Verify the name and try again.</p> <note> <p>For the <code>DeleteParameter</code> and <code>GetParameter</code> actions, if the specified parameter doesn't exist, the <code>ParameterNotFound</code> exception is <i>not</i> recorded in CloudTrail event logs.</p> </note>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_parameter_request.DeleteParameterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_parameter_result.DeleteParameterResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_parameter

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_parameter.async_delete_parameter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_parameter_request.DeleteParameterRequest = {
            "name": name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_parameters(
        self,
        names: "capo_ssm.types.parameter_name_list.ParameterNameList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.delete_parameters_result.DeleteParametersResult":
        """<p>Delete a list of parameters. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.</p>

        Args:
            names: <p>The names of the parameters to delete. After deleting a parameter, wait for at least 30 seconds to create a parameter with the same name.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_parameters_request.DeleteParametersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_parameters_result.DeleteParametersResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_parameters

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_parameters.async_delete_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_parameters_request.DeleteParametersRequest = {
            "names": names
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_patch_baseline(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.delete_patch_baseline_result.DeletePatchBaselineResult":
        """<p>Deletes a patch baseline.</p>

        Args:
            baseline_id: <p>The ID of the patch baseline to delete.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_in_use_exception.ResourceInUseException: <p>Error returned if an attempt is made to delete a patch baseline that is registered for a patch group.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_patch_baseline_request.DeletePatchBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_patch_baseline_result.DeletePatchBaselineResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_patch_baseline

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_patch_baseline.async_delete_patch_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_patch_baseline_request.DeletePatchBaselineRequest = {
            "baseline_id": baseline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_data_sync(
        self,
        sync_name: "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_type: Optional[
            "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
        ] = None,
    ) -> "capo_ssm.types.delete_resource_data_sync_result.DeleteResourceDataSyncResult":
        """<p>Deletes a resource data sync configuration. After the configuration is deleted, changes to data on managed nodes are no longer synced to or from the target. Deleting a sync configuration doesn't delete data.</p>

        Args:
            sync_name: <p>The name of the configuration to delete.</p>
            sync_type: <p>Specify the type of resource data sync to delete.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_data_sync_invalid_configuration_exception.ResourceDataSyncInvalidConfigurationException: <p>The specified sync configuration is invalid.</p>
            capo_ssm.errors.resource_data_sync_not_found_exception.ResourceDataSyncNotFoundException: <p>The specified sync name wasn't found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_resource_data_sync_request.DeleteResourceDataSyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_resource_data_sync_result.DeleteResourceDataSyncResult"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_resource_data_sync

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_resource_data_sync.async_delete_resource_data_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_resource_data_sync_request.DeleteResourceDataSyncRequest = {
            "sync_name": sync_name
        }
        if sync_type is not None:
            input_["sync_type"] = sync_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_resource_policy(
        self,
        resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString",
        policy_id: "capo_ssm.types.policy_id.PolicyId",
        policy_hash: "capo_ssm.types.policy_hash.PolicyHash",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        deletion_mode: Optional["capo_ssm.types.deletion_mode.DeletionMode"] = None,
    ) -> "capo_ssm.types.delete_resource_policy_response.DeleteResourcePolicyResponse":
        """<p>Deletes a Systems Manager resource policy. A resource policy helps you to define the IAM entity (for example, an Amazon Web Services account) that can manage your Systems Manager resources. The following resources support Systems Manager resource policies.</p> <ul> <li> <p> <code>OpsItemGroup</code> - The resource policy for <code>OpsItemGroup</code> enables Amazon Web Services accounts to view and interact with OpsCenter operational work items (OpsItems).</p> </li> <li> <p> <code>Parameter</code> - The resource policy is used to share a parameter with other accounts using Resource Access Manager (RAM). For more information about cross-account sharing of parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html">Working with shared parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </li> <li> <p> <code>Document</code> – Shares the document using Resource Access Manager (RAM). For more information about sharing documents, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html">Sharing Systems Manager documents</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </li> </ul>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to which the policies are attached.</p>
            policy_id: <p>The policy ID.</p>
            policy_hash: <p>ID of the current policy version. The hash helps to prevent multiple calls from attempting to overwrite a policy.</p>
            deletion_mode: <p>Specifies the intended outcome of the operation. Applies only to the <code>Document</code> resource type. The operation ignores this parameter for other resource types. Optional. Defaults to <code>RemoveSharing</code>.</p> <ul> <li> <p> <code>RemoveSharing</code> – Deletes the resource policy and removes sharing of the document.</p> </li> <li> <p> <code>RollbackMigration</code> – Reverts the document to Custom sharing, preserving existing consumer access, instead of removing the policy.</p> </li> </ul>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.malformed_resource_policy_document_exception.MalformedResourcePolicyDocumentException: <p>The specified policy document is malformed or invalid, or excessive <code>PutResourcePolicy</code> or <code>DeleteResourcePolicy</code> calls have been made.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.resource_policy_conflict_exception.ResourcePolicyConflictException: <p>The hash provided in the call doesn't match the stored hash. This exception is thrown when trying to update an obsolete policy version or when multiple requests to update a policy are sent.</p>
            capo_ssm.errors.resource_policy_invalid_parameter_exception.ResourcePolicyInvalidParameterException: <p>One or more parameters specified for the call aren't valid. Verify the parameters and their values and try again.</p>
            capo_ssm.errors.resource_policy_not_found_exception.ResourcePolicyNotFoundException: <p>No policies with the specified policy ID and hash could be found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.delete_resource_policy_response.DeleteResourcePolicyResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.delete_resource_policy

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.delete_resource_policy.async_delete_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy_id": policy_id,
            "policy_hash": policy_hash,
        }
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_managed_instance(
        self,
        instance_id: "capo_ssm.types.managed_instance_id.ManagedInstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.deregister_managed_instance_result.DeregisterManagedInstanceResult":
        """<p>Removes the server or virtual machine from the list of registered servers.</p> <p>If you want to reregister an on-premises server, edge device, or VM, you must use a different Activation Code and Activation ID than used to register the machine previously. The Activation Code and Activation ID must not have already been used on the maximum number of activations specified when they were created. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-deregister-hybrid-nodes.html">Deregistering managed nodes in a hybrid and multicloud environment</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>

        Args:
            instance_id: <p>The ID assigned to the managed node when you registered it using the activation process. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.deregister_managed_instance_request.DeregisterManagedInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.deregister_managed_instance_result.DeregisterManagedInstanceResult"
        ]:
            import capo_ssm._operations.amazon_ssm.deregister_managed_instance

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.deregister_managed_instance.async_deregister_managed_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.deregister_managed_instance_request.DeregisterManagedInstanceRequest = {
            "instance_id": instance_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_patch_baseline_for_patch_group(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        patch_group: "capo_ssm.types.patch_group.PatchGroup",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.deregister_patch_baseline_for_patch_group_result.DeregisterPatchBaselineForPatchGroupResult":
        """<p>Removes a patch group from a patch baseline.</p>

        Args:
            baseline_id: <p>The ID of the patch baseline to deregister the patch group from.</p>
            patch_group: <p>The name of the patch group that should be deregistered from the patch baseline.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.deregister_patch_baseline_for_patch_group_request.DeregisterPatchBaselineForPatchGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.deregister_patch_baseline_for_patch_group_result.DeregisterPatchBaselineForPatchGroupResult"
        ]:
            import capo_ssm._operations.amazon_ssm.deregister_patch_baseline_for_patch_group

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.deregister_patch_baseline_for_patch_group.async_deregister_patch_baseline_for_patch_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.deregister_patch_baseline_for_patch_group_request.DeregisterPatchBaselineForPatchGroupRequest = {
            "baseline_id": baseline_id,
            "patch_group": patch_group,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_target_from_maintenance_window(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        window_target_id: "capo_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        safe: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.deregister_target_from_maintenance_window_result.DeregisterTargetFromMaintenanceWindowResult":
        """<p>Removes a target from a maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window the target should be removed from.</p>
            window_target_id: <p>The ID of the target definition to remove.</p>
            safe: <p>The system checks if the target is being referenced by a task. If the target is being referenced, the system returns an error and doesn't deregister the target from the maintenance window.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.target_in_use_exception.TargetInUseException: <p>You specified the <code>Safe</code> option for the DeregisterTargetFromMaintenanceWindow operation, but the target is still referenced in a task.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.deregister_target_from_maintenance_window_request.DeregisterTargetFromMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.deregister_target_from_maintenance_window_result.DeregisterTargetFromMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.deregister_target_from_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.deregister_target_from_maintenance_window.async_deregister_target_from_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.deregister_target_from_maintenance_window_request.DeregisterTargetFromMaintenanceWindowRequest = {
            "window_id": window_id,
            "window_target_id": window_target_id,
        }
        if safe is not None:
            input_["safe"] = safe

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def deregister_task_from_maintenance_window(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        window_task_id: "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.deregister_task_from_maintenance_window_result.DeregisterTaskFromMaintenanceWindowResult":
        """<p>Removes a task from a maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window the task should be removed from.</p>
            window_task_id: <p>The ID of the task to remove from the maintenance window.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.deregister_task_from_maintenance_window_request.DeregisterTaskFromMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.deregister_task_from_maintenance_window_result.DeregisterTaskFromMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.deregister_task_from_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.deregister_task_from_maintenance_window.async_deregister_task_from_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.deregister_task_from_maintenance_window_request.DeregisterTaskFromMaintenanceWindowRequest = {
            "window_id": window_id,
            "window_task_id": window_task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_activations(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.describe_activations_filter_list.DescribeActivationsFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_activations_result.DescribeActivationsResult":
        """<p>Describes details about the activation, such as the date and time the activation was created, its expiration date, the Identity and Access Management (IAM) role assigned to the managed nodes in the activation, and the number of nodes registered by using this activation.</p>

        Args:
            filters: <p>A filter to view information about your activations.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_activations_request.DescribeActivationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_activations_result.DescribeActivationsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_activations

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_activations.async_describe_activations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_activations_request.DescribeActivationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_activations(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.describe_activations_filter_list.DescribeActivationsFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.activation.Activation]":
        _token = next_token
        while True:
            _response = await self.describe_activations(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("activation_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_association(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        name: Optional["capo_ssm.types.document_arn.DocumentARN"] = None,
        instance_id: Optional["capo_ssm.types.instance_id.InstanceId"] = None,
        association_id: Optional["capo_ssm.types.association_id.AssociationId"] = None,
        association_version: Optional[
            "capo_ssm.types.association_version.AssociationVersion"
        ] = None,
    ) -> "capo_ssm.types.describe_association_result.DescribeAssociationResult":
        """<p>Describes the association for the specified target or managed node. If you created the association by using the <code>Targets</code> parameter, then you must retrieve the association by using the association ID.</p>

        Args:
            name: <p>The name of the SSM document.</p>
            instance_id: <p>The managed node ID.</p>
            association_id: <p>The association ID for which you want information.</p>
            association_version: <p>Specify the association version to retrieve. To view the latest version, either specify <code>$LATEST</code> for this parameter, or omit this parameter. To view a list of all associations for a managed node, use <a>ListAssociations</a>. To get a list of versions for a specific association, use <a>ListAssociationVersions</a>. </p>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_association_version.InvalidAssociationVersion: <p>The version you specified isn't valid. Use ListAssociationVersions to view all versions of an association according to the association ID. Or, use the <code>$LATEST</code> parameter to view the latest version of the association.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_association_request.DescribeAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_association_result.DescribeAssociationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_association

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_association.async_describe_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_association_request.DescribeAssociationRequest = {}
        if name is not None:
            input_["name"] = name
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if association_id is not None:
            input_["association_id"] = association_id
        if association_version is not None:
            input_["association_version"] = association_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_association_executions(
        self,
        association_id: "capo_ssm.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.association_execution_filter_list.AssociationExecutionFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_association_executions_result.DescribeAssociationExecutionsResult":
        """<p>Views all executions for a specific association ID. </p>

        Args:
            association_id: <p>The association ID for which you want to view execution history details.</p>
            filters: <p>Filters for the request. You can specify the following filters and values.</p> <p>ExecutionId (EQUAL)</p> <p>Status (EQUAL)</p> <p>CreatedTime (EQUAL, GREATER_THAN, LESS_THAN)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_association_executions_request.DescribeAssociationExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_association_executions_result.DescribeAssociationExecutionsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_association_executions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_association_executions.async_describe_association_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_association_executions_request.DescribeAssociationExecutionsRequest = {
            "association_id": association_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_association_executions(
        self,
        association_id: "capo_ssm.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.association_execution_filter_list.AssociationExecutionFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.association_execution.AssociationExecution]":
        _token = next_token
        while True:
            _response = await self.describe_association_executions(
                association_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("association_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_association_execution_targets(
        self,
        association_id: "capo_ssm.types.association_id.AssociationId",
        execution_id: "capo_ssm.types.association_execution_id.AssociationExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.association_execution_targets_filter_list.AssociationExecutionTargetsFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_association_execution_targets_result.DescribeAssociationExecutionTargetsResult":
        """<p>Views information about a specific execution of a specific association.</p>

        Args:
            association_id: <p>The association ID that includes the execution for which you want to view details.</p>
            execution_id: <p>The execution ID for which you want to view details.</p>
            filters: <p>Filters for the request. You can specify the following filters and values.</p> <p>Status (EQUAL)</p> <p>ResourceId (EQUAL)</p> <p>ResourceType (EQUAL)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.association_execution_does_not_exist.AssociationExecutionDoesNotExist: <p>The specified execution ID doesn't exist. Verify the ID number and try again.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_association_execution_targets_request.DescribeAssociationExecutionTargetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_association_execution_targets_result.DescribeAssociationExecutionTargetsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_association_execution_targets

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_association_execution_targets.async_describe_association_execution_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_association_execution_targets_request.DescribeAssociationExecutionTargetsRequest = {
            "association_id": association_id,
            "execution_id": execution_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_association_execution_targets(
        self,
        association_id: "capo_ssm.types.association_id.AssociationId",
        execution_id: "capo_ssm.types.association_execution_id.AssociationExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.association_execution_targets_filter_list.AssociationExecutionTargetsFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.association_execution_target.AssociationExecutionTarget]":
        _token = next_token
        while True:
            _response = await self.describe_association_execution_targets(
                association_id,
                execution_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("association_execution_targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_automation_executions(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.automation_execution_filter_list.AutomationExecutionFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_automation_executions_result.DescribeAutomationExecutionsResult":
        """<p>Provides details about all active and terminated Automation executions.</p>

        Args:
            filters: <p>Filters used to limit the scope of executions that are requested.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_filter_value.InvalidFilterValue: <p>The filter value isn't valid. Verify the value and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_automation_executions_request.DescribeAutomationExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_automation_executions_result.DescribeAutomationExecutionsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_automation_executions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_automation_executions.async_describe_automation_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_automation_executions_request.DescribeAutomationExecutionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_automation_executions(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.automation_execution_filter_list.AutomationExecutionFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.automation_execution_metadata.AutomationExecutionMetadata]":
        _token = next_token
        while True:
            _response = await self.describe_automation_executions(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("automation_execution_metadata_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_automation_step_executions(
        self,
        automation_execution_id: "capo_ssm.types.automation_execution_id.AutomationExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.step_execution_filter_list.StepExecutionFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        reverse_order: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.describe_automation_step_executions_result.DescribeAutomationStepExecutionsResult":
        """<p>Information about all active and terminated step executions in an Automation workflow.</p>

        Args:
            automation_execution_id: <p>The Automation execution ID for which you want step execution descriptions.</p>
            filters: <p>One or more filters to limit the number of step executions returned by the request.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            reverse_order: <p>Indicates whether to list step executions in reverse order by start time. The default value is 'false'.</p>

        Raises:
            capo_ssm.errors.automation_execution_not_found_exception.AutomationExecutionNotFoundException: <p>There is no automation execution information for the requested automation execution ID.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_filter_value.InvalidFilterValue: <p>The filter value isn't valid. Verify the value and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_automation_step_executions_request.DescribeAutomationStepExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_automation_step_executions_result.DescribeAutomationStepExecutionsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_automation_step_executions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_automation_step_executions.async_describe_automation_step_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_automation_step_executions_request.DescribeAutomationStepExecutionsRequest = {
            "automation_execution_id": automation_execution_id
        }
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if reverse_order is not None:
            input_["reverse_order"] = reverse_order

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_automation_step_executions(
        self,
        automation_execution_id: "capo_ssm.types.automation_execution_id.AutomationExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.step_execution_filter_list.StepExecutionFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        reverse_order: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[capo_ssm.types.step_execution.StepExecution]":
        _token = next_token
        while True:
            _response = await self.describe_automation_step_executions(
                automation_execution_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
                reverse_order=reverse_order,
            )
            _page = _resolve_path(_response, ("step_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_available_patches(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_available_patches_result.DescribeAvailablePatchesResult":
        """<p>Lists all patches eligible to be included in a patch baseline.</p> <note> <p>Currently, <code>DescribeAvailablePatches</code> supports only the Amazon Linux 1, Amazon Linux 2, and Windows Server operating systems.</p> </note>

        Args:
            filters: <p>Each element in the array is a structure containing a key-value pair.</p> <p> <b>Windows Server</b> </p> <p>Supported keys for Windows Server managed node patches include the following:</p> <ul> <li> <p> <b> <code>PATCH_SET</code> </b> </p> <p>Sample values: <code>OS</code> | <code>APPLICATION</code> </p> </li> <li> <p> <b> <code>PRODUCT</code> </b> </p> <p>Sample values: <code>WindowsServer2012</code> | <code>Office 2010</code> | <code>MicrosoftDefenderAntivirus</code> </p> </li> <li> <p> <b> <code>PRODUCT_FAMILY</code> </b> </p> <p>Sample values: <code>Windows</code> | <code>Office</code> </p> </li> <li> <p> <b> <code>MSRC_SEVERITY</code> </b> </p> <p>Sample values: <code>ServicePacks</code> | <code>Important</code> | <code>Moderate</code> </p> </li> <li> <p> <b> <code>CLASSIFICATION</code> </b> </p> <p>Sample values: <code>ServicePacks</code> | <code>SecurityUpdates</code> | <code>DefinitionUpdates</code> </p> </li> <li> <p> <b> <code>PATCH_ID</code> </b> </p> <p>Sample values: <code>KB123456</code> | <code>KB4516046</code> </p> </li> </ul> <p> <b>Linux</b> </p> <important> <p>When specifying filters for Linux patches, you must specify a key-pair for <code>PRODUCT</code>. For example, using the Command Line Interface (CLI), the following command fails:</p> <p> <code>aws ssm describe-available-patches --filters Key=CVE_ID,Values=CVE-2018-3615</code> </p> <p>However, the following command succeeds:</p> <p> <code>aws ssm describe-available-patches --filters Key=PRODUCT,Values=AmazonLinux2018.03 Key=CVE_ID,Values=CVE-2018-3615</code> </p> </important> <p>Supported keys for Linux managed node patches include the following:</p> <ul> <li> <p> <b> <code>PRODUCT</code> </b> </p> <p>Sample values: <code>AmazonLinux2018.03</code> | <code>AmazonLinux2.0</code> </p> </li> <li> <p> <b> <code>NAME</code> </b> </p> <p>Sample values: <code>kernel-headers</code> | <code>samba-python</code> | <code>php</code> </p> </li> <li> <p> <b> <code>SEVERITY</code> </b> </p> <p>Sample values: <code>Critical</code> | <code>Important</code> | <code>Medium</code> | <code>Low</code> </p> </li> <li> <p> <b> <code>EPOCH</code> </b> </p> <p>Sample values: <code>0</code> | <code>1</code> </p> </li> <li> <p> <b> <code>VERSION</code> </b> </p> <p>Sample values: <code>78.6.1</code> | <code>4.10.16</code> </p> </li> <li> <p> <b> <code>RELEASE</code> </b> </p> <p>Sample values: <code>9.56.amzn1</code> | <code>1.amzn2</code> </p> </li> <li> <p> <b> <code>ARCH</code> </b> </p> <p>Sample values: <code>i686</code> | <code>x86_64</code> </p> </li> <li> <p> <b> <code>REPOSITORY</code> </b> </p> <p>Sample values: <code>Core</code> | <code>Updates</code> </p> </li> <li> <p> <b> <code>ADVISORY_ID</code> </b> </p> <p>Sample values: <code>ALAS-2018-1058</code> | <code>ALAS2-2021-1594</code> </p> </li> <li> <p> <b> <code>CVE_ID</code> </b> </p> <p>Sample values: <code>CVE-2018-3615</code> | <code>CVE-2020-1472</code> </p> </li> <li> <p> <b> <code>BUGZILLA_ID</code> </b> </p> <p>Sample values: <code>1463241</code> </p> </li> </ul>
            max_results: <p>The maximum number of patches to return (per page).</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_available_patches_request.DescribeAvailablePatchesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_available_patches_result.DescribeAvailablePatchesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_available_patches

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_available_patches.async_describe_available_patches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_available_patches_request.DescribeAvailablePatchesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_available_patches(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.patch.Patch]":
        _token = next_token
        while True:
            _response = await self.describe_available_patches(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("patches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_document(
        self,
        name: "capo_ssm.types.document_arn.DocumentARN",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        version_name: Optional[
            "capo_ssm.types.document_version_name.DocumentVersionName"
        ] = None,
    ) -> "capo_ssm.types.describe_document_result.DescribeDocumentResult":
        """<p>Describes the specified Amazon Web Services Systems Manager document (SSM document).</p>

        Args:
            name: <p>The name of the SSM document.</p> <note> <p>If you're calling a shared SSM document from a different Amazon Web Services account, <code>Name</code> is the full Amazon Resource Name (ARN) of the document.</p> </note>
            document_version: <p>The document version for which you want information. Can be a specific version or the default version.</p>
            version_name: <p>An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_document_request.DescribeDocumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_document_result.DescribeDocumentResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_document

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_document.async_describe_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_document_request.DescribeDocumentRequest = {
            "name": name
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if version_name is not None:
            input_["version_name"] = version_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_document_permission(
        self,
        name: "capo_ssm.types.document_name.DocumentName",
        permission_type: "capo_ssm.types.document_permission_type.DocumentPermissionType",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.document_permission_max_results.DocumentPermissionMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_document_permission_response.DescribeDocumentPermissionResponse":
        """<p>Describes the permissions for a Amazon Web Services Systems Manager document (SSM document). If you created the document, you are the owner. If a document is shared, it can either be shared privately (by specifying a user's Amazon Web Services account ID) or publicly (<i>All</i>). </p>

        Args:
            name: <p>The name of the document for which you are the owner. </p>
            permission_type: <p>The permission type for the document. The permission type can be <i>Share</i>.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_operation.InvalidDocumentOperation: <p>You attempted to delete a document while it is still shared. You must stop sharing the document before you can delete it.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.invalid_permission_type.InvalidPermissionType: <p>The permission type isn't supported. <i>Share</i> is the only supported permission type.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_document_permission_request.DescribeDocumentPermissionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_document_permission_response.DescribeDocumentPermissionResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_document_permission

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_document_permission.async_describe_document_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_document_permission_request.DescribeDocumentPermissionRequest = {
            "name": name,
            "permission_type": permission_type,
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

    async def describe_effective_instance_associations(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.effective_instance_association_max_results.EffectiveInstanceAssociationMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_effective_instance_associations_result.DescribeEffectiveInstanceAssociationsResult":
        """<p>All associations for the managed nodes.</p>

        Args:
            instance_id: <p>The managed node ID for which you want to view all associations.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_effective_instance_associations_request.DescribeEffectiveInstanceAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_effective_instance_associations_result.DescribeEffectiveInstanceAssociationsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_effective_instance_associations

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_effective_instance_associations.async_describe_effective_instance_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_effective_instance_associations_request.DescribeEffectiveInstanceAssociationsRequest = {
            "instance_id": instance_id
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

    async def iter_describe_effective_instance_associations(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.effective_instance_association_max_results.EffectiveInstanceAssociationMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.instance_association.InstanceAssociation]":
        _token = next_token
        while True:
            _response = await self.describe_effective_instance_associations(
                instance_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_effective_patches_for_patch_baseline(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_effective_patches_for_patch_baseline_result.DescribeEffectivePatchesForPatchBaselineResult":
        """<p>Retrieves the current effective patches (the patch and the approval state) for the specified patch baseline. Applies to patch baselines for Windows only.</p>

        Args:
            baseline_id: <p>The ID of the patch baseline to retrieve the effective patches for.</p>
            max_results: <p>The maximum number of patches to return (per page).</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.unsupported_operating_system.UnsupportedOperatingSystem: <p>The operating systems you specified isn't supported, or the operation isn't supported for the operating system.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_effective_patches_for_patch_baseline_request.DescribeEffectivePatchesForPatchBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_effective_patches_for_patch_baseline_result.DescribeEffectivePatchesForPatchBaselineResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_effective_patches_for_patch_baseline

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_effective_patches_for_patch_baseline.async_describe_effective_patches_for_patch_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_effective_patches_for_patch_baseline_request.DescribeEffectivePatchesForPatchBaselineRequest = {
            "baseline_id": baseline_id
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

    async def iter_describe_effective_patches_for_patch_baseline(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.effective_patch.EffectivePatch]":
        _token = next_token
        while True:
            _response = await self.describe_effective_patches_for_patch_baseline(
                baseline_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("effective_patches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instance_associations_status(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_instance_associations_status_result.DescribeInstanceAssociationsStatusResult":
        """<p>The status of the associations for the managed nodes.</p>

        Args:
            instance_id: <p>The managed node IDs for which you want association status information.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_instance_associations_status_request.DescribeInstanceAssociationsStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_instance_associations_status_result.DescribeInstanceAssociationsStatusResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_instance_associations_status

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_instance_associations_status.async_describe_instance_associations_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_instance_associations_status_request.DescribeInstanceAssociationsStatusRequest = {
            "instance_id": instance_id
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

    async def iter_describe_instance_associations_status(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.instance_association_status_info.InstanceAssociationStatusInfo]":
        _token = next_token
        while True:
            _response = await self.describe_instance_associations_status(
                instance_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instance_association_status_infos",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instance_information(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        instance_information_filter_list: Optional[
            "capo_ssm.types.instance_information_filter_list.InstanceInformationFilterList"
        ] = None,
        filters: Optional[
            "capo_ssm.types.instance_information_string_filter_list.InstanceInformationStringFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.max_results_ec2_compatible.MaxResultsEC2Compatible"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_instance_information_result.DescribeInstanceInformationResult":
        """<p>Provides information about one or more of your managed nodes, including the operating system platform, SSM Agent version, association status, and IP address. This operation does not return information for nodes that are either Stopped or Terminated.</p> <p>If you specify one or more node IDs, the operation returns information for those managed nodes. If you don't specify node IDs, it returns information for all your managed nodes. If you specify a node ID that isn't valid or a node that you don't own, you receive an error.</p> <note> <p>The <code>IamRole</code> field returned for this API operation is the role assigned to an Amazon EC2 instance configured with a Systems Manager Quick Setup host management configuration or the role assigned to an on-premises managed node.</p> </note>

        Args:
            instance_information_filter_list: <p>This is a legacy method. We recommend that you don't use this method. Instead, use the <code>Filters</code> data type. <code>Filters</code> enables you to return node information by filtering based on tags applied to managed nodes.</p> <note> <p>Attempting to use <code>InstanceInformationFilterList</code> and <code>Filters</code> leads to an exception error. </p> </note>
            filters: <p>One or more filters. Use a filter to return a more specific list of managed nodes. You can filter based on tags applied to your managed nodes. Tag filters can't be combined with other filter types. Use this <code>Filters</code> data type instead of <code>InstanceInformationFilterList</code>, which is deprecated.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. The default value is 10 items. </p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_instance_information_filter_value.InvalidInstanceInformationFilterValue: <p>The specified filter value isn't valid.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_instance_information_request.DescribeInstanceInformationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_instance_information_result.DescribeInstanceInformationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_instance_information

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_instance_information.async_describe_instance_information(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_instance_information_request.DescribeInstanceInformationRequest = {}
        if instance_information_filter_list is not None:
            input_["instance_information_filter_list"] = (
                instance_information_filter_list
            )
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_instance_information(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        instance_information_filter_list: Optional[
            "capo_ssm.types.instance_information_filter_list.InstanceInformationFilterList"
        ] = None,
        filters: Optional[
            "capo_ssm.types.instance_information_string_filter_list.InstanceInformationStringFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.max_results_ec2_compatible.MaxResultsEC2Compatible"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.instance_information.InstanceInformation]":
        _token = next_token
        while True:
            _response = await self.describe_instance_information(
                config_overrides=config_overrides,
                instance_information_filter_list=instance_information_filter_list,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instance_information_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instance_patches(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
        ] = None,
    ) -> (
        "capo_ssm.types.describe_instance_patches_result.DescribeInstancePatchesResult"
    ):
        """<p>Retrieves information about the patches on the specified managed node and their state relative to the patch baseline being used for the node.</p>

        Args:
            instance_id: <p>The ID of the managed node whose patch state information should be retrieved.</p>
            filters: <p>Each element in the array is a structure containing a key-value pair.</p> <p>Supported keys for <code>DescribeInstancePatches</code>include the following:</p> <ul> <li> <p> <b> <code>Classification</code> </b> </p> <p>Sample values: <code>Security</code> | <code>SecurityUpdates</code> </p> </li> <li> <p> <b> <code>KBId</code> </b> </p> <p>Sample values: <code>KB4480056</code> | <code>java-1.7.0-openjdk.x86_64</code> </p> </li> <li> <p> <b> <code>Severity</code> </b> </p> <p>Sample values: <code>Important</code> | <code>Medium</code> | <code>Low</code> </p> </li> <li> <p> <b> <code>State</code> </b> </p> <p>Sample values: <code>Installed</code> | <code>InstalledOther</code> | <code>InstalledPendingReboot</code> </p> <p>For lists of all <code>State</code> values, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-states.html">Patch compliance state values</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of patches to return (per page).</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_instance_patches_request.DescribeInstancePatchesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_instance_patches_result.DescribeInstancePatchesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_instance_patches

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_instance_patches.async_describe_instance_patches(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_instance_patches_request.DescribeInstancePatchesRequest = {
            "instance_id": instance_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_instance_patches(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_ssm.types.patch_compliance_data.PatchComplianceData]":
        _token = next_token
        while True:
            _response = await self.describe_instance_patches(
                instance_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("patches",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instance_patch_states(
        self,
        instance_ids: "capo_ssm.types.instance_id_list.InstanceIdList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
        ] = None,
    ) -> "capo_ssm.types.describe_instance_patch_states_result.DescribeInstancePatchStatesResult":
        """<p>Retrieves the high-level patch state of one or more managed nodes.</p>

        Args:
            instance_ids: <p>The ID of the managed node for which patch state information should be retrieved.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of managed nodes to return (per page).</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_instance_patch_states_request.DescribeInstancePatchStatesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_instance_patch_states_result.DescribeInstancePatchStatesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_instance_patch_states

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_instance_patch_states.async_describe_instance_patch_states(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_instance_patch_states_request.DescribeInstancePatchStatesRequest = {
            "instance_ids": instance_ids
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

    async def iter_describe_instance_patch_states(
        self,
        instance_ids: "capo_ssm.types.instance_id_list.InstanceIdList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_ssm.types.instance_patch_state.InstancePatchState]":
        _token = next_token
        while True:
            _response = await self.describe_instance_patch_states(
                instance_ids,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("instance_patch_states",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instance_patch_states_for_patch_group(
        self,
        patch_group: "capo_ssm.types.patch_group.PatchGroup",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.instance_patch_state_filter_list.InstancePatchStateFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
        ] = None,
    ) -> "capo_ssm.types.describe_instance_patch_states_for_patch_group_result.DescribeInstancePatchStatesForPatchGroupResult":
        """<p>Retrieves the high-level patch state for the managed nodes in the specified patch group.</p>

        Args:
            patch_group: <p>The name of the patch group for which the patch state information should be retrieved.</p>
            filters: <p>Each entry in the array is a structure containing:</p> <ul> <li> <p>Key (string between 1 and 200 characters)</p> </li> <li> <p>Values (array containing a single string)</p> </li> <li> <p>Type (string "Equal", "NotEqual", "LessThan", "GreaterThan")</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of patches to return (per page).</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_instance_patch_states_for_patch_group_request.DescribeInstancePatchStatesForPatchGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_instance_patch_states_for_patch_group_result.DescribeInstancePatchStatesForPatchGroupResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_instance_patch_states_for_patch_group

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_instance_patch_states_for_patch_group.async_describe_instance_patch_states_for_patch_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_instance_patch_states_for_patch_group_request.DescribeInstancePatchStatesForPatchGroupRequest = {
            "patch_group": patch_group
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_instance_patch_states_for_patch_group(
        self,
        patch_group: "capo_ssm.types.patch_group.PatchGroup",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.instance_patch_state_filter_list.InstancePatchStateFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.patch_compliance_max_results.PatchComplianceMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_ssm.types.instance_patch_state.InstancePatchState]":
        _token = next_token
        while True:
            _response = await self.describe_instance_patch_states_for_patch_group(
                patch_group,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("instance_patch_states",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instance_properties(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        instance_property_filter_list: Optional[
            "capo_ssm.types.instance_property_filter_list.InstancePropertyFilterList"
        ] = None,
        filters_with_operator: Optional[
            "capo_ssm.types.instance_property_string_filter_list.InstancePropertyStringFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.describe_instance_properties_max_results.DescribeInstancePropertiesMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_instance_properties_result.DescribeInstancePropertiesResult":
        """<p>An API operation used by the Systems Manager console to display information about Systems Manager managed nodes.</p>

        Args:
            instance_property_filter_list: <p>An array of instance property filters.</p>
            filters_with_operator: <p>The request filters to use with the operator.</p>
            max_results: <p>The maximum number of items to return for the call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token provided by a previous request to use to return the next set of properties.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_activation_id.InvalidActivationId: <p>The activation ID isn't valid. Verify that you entered the correct ActivationId or ActivationCode and try again.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_instance_property_filter_value.InvalidInstancePropertyFilterValue: <p>The specified filter value isn't valid.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_instance_properties_request.DescribeInstancePropertiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_instance_properties_result.DescribeInstancePropertiesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_instance_properties

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_instance_properties.async_describe_instance_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_instance_properties_request.DescribeInstancePropertiesRequest = {}
        if instance_property_filter_list is not None:
            input_["instance_property_filter_list"] = instance_property_filter_list
        if filters_with_operator is not None:
            input_["filters_with_operator"] = filters_with_operator
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

    async def iter_describe_instance_properties(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        instance_property_filter_list: Optional[
            "capo_ssm.types.instance_property_filter_list.InstancePropertyFilterList"
        ] = None,
        filters_with_operator: Optional[
            "capo_ssm.types.instance_property_string_filter_list.InstancePropertyStringFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.describe_instance_properties_max_results.DescribeInstancePropertiesMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.instance_property.InstanceProperty]":
        _token = next_token
        while True:
            _response = await self.describe_instance_properties(
                config_overrides=config_overrides,
                instance_property_filter_list=instance_property_filter_list,
                filters_with_operator=filters_with_operator,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("instance_properties",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_inventory_deletions(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        deletion_id: Optional["capo_ssm.types.uuid.UUID"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.describe_inventory_deletions_result.DescribeInventoryDeletionsResult":
        """<p>Describes a specific delete inventory operation.</p>

        Args:
            deletion_id: <p>Specify the delete inventory ID for which you want information. This ID was returned by the <code>DeleteInventory</code> operation.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_deletion_id_exception.InvalidDeletionIdException: <p>The ID specified for the delete operation doesn't exist or isn't valid. Verify the ID and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_inventory_deletions_request.DescribeInventoryDeletionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_inventory_deletions_result.DescribeInventoryDeletionsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_inventory_deletions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_inventory_deletions.async_describe_inventory_deletions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_inventory_deletions_request.DescribeInventoryDeletionsRequest = {}
        if deletion_id is not None:
            input_["deletion_id"] = deletion_id
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

    async def iter_describe_inventory_deletions(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        deletion_id: Optional["capo_ssm.types.uuid.UUID"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.inventory_deletion_status_item.InventoryDeletionStatusItem]":
        _token = next_token
        while True:
            _response = await self.describe_inventory_deletions(
                config_overrides=config_overrides,
                deletion_id=deletion_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("inventory_deletions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_window_executions(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_window_executions_result.DescribeMaintenanceWindowExecutionsResult":
        """<p>Lists the executions of a maintenance window. This includes information about when the maintenance window was scheduled to be active, and information about tasks registered and run with the maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window whose executions should be retrieved.</p>
            filters: <p>Each entry in the array is a structure containing:</p> <ul> <li> <p>Key. A string between 1 and 128 characters. Supported keys include <code>ExecutedBefore</code> and <code>ExecutedAfter</code>.</p> </li> <li> <p>Values. An array of strings, each between 1 and 256 characters. Supported values are date/time strings in a valid ISO 8601 date/time format, such as <code>2024-11-04T05:00:00Z</code>.</p> </li> </ul>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_window_executions_request.DescribeMaintenanceWindowExecutionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_window_executions_result.DescribeMaintenanceWindowExecutionsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_window_executions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_window_executions.async_describe_maintenance_window_executions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_window_executions_request.DescribeMaintenanceWindowExecutionsRequest = {
            "window_id": window_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_maintenance_window_executions(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.maintenance_window_execution.MaintenanceWindowExecution]":
        _token = next_token
        while True:
            _response = await self.describe_maintenance_window_executions(
                window_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("window_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_window_execution_task_invocations(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_window_execution_task_invocations_result.DescribeMaintenanceWindowExecutionTaskInvocationsResult":
        """<p>Retrieves the individual task executions (one per target) for a particular task run as part of a maintenance window execution.</p>

        Args:
            window_execution_id: <p>The ID of the maintenance window execution the task is part of.</p>
            task_id: <p>The ID of the specific task in the maintenance window task that should be retrieved.</p>
            filters: <p>Optional filters used to scope down the returned task invocations. The supported filter key is <code>STATUS</code> with the corresponding values <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, <code>CANCELLING</code>, and <code>CANCELLED</code>.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_window_execution_task_invocations_request.DescribeMaintenanceWindowExecutionTaskInvocationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_window_execution_task_invocations_result.DescribeMaintenanceWindowExecutionTaskInvocationsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_window_execution_task_invocations

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_window_execution_task_invocations.async_describe_maintenance_window_execution_task_invocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_window_execution_task_invocations_request.DescribeMaintenanceWindowExecutionTaskInvocationsRequest = {
            "window_execution_id": window_execution_id,
            "task_id": task_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_maintenance_window_execution_task_invocations(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.maintenance_window_execution_task_invocation_identity.MaintenanceWindowExecutionTaskInvocationIdentity]":
        _token = next_token
        while True:
            _response = (
                await self.describe_maintenance_window_execution_task_invocations(
                    window_execution_id,
                    task_id,
                    config_overrides=config_overrides,
                    filters=filters,
                    max_results=max_results,
                    next_token=_token,
                )
            )
            _page = _resolve_path(
                _response, ("window_execution_task_invocation_identities",)
            )
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_window_execution_tasks(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_window_execution_tasks_result.DescribeMaintenanceWindowExecutionTasksResult":
        """<p>For a given maintenance window execution, lists the tasks that were run.</p>

        Args:
            window_execution_id: <p>The ID of the maintenance window execution whose task executions should be retrieved.</p>
            filters: <p>Optional filters used to scope down the returned tasks. The supported filter key is <code>STATUS</code> with the corresponding values <code>PENDING</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>, <code>TIMED_OUT</code>, <code>CANCELLING</code>, and <code>CANCELLED</code>.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_window_execution_tasks_request.DescribeMaintenanceWindowExecutionTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_window_execution_tasks_result.DescribeMaintenanceWindowExecutionTasksResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_window_execution_tasks

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_window_execution_tasks.async_describe_maintenance_window_execution_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_window_execution_tasks_request.DescribeMaintenanceWindowExecutionTasksRequest = {
            "window_execution_id": window_execution_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_maintenance_window_execution_tasks(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.maintenance_window_execution_task_identity.MaintenanceWindowExecutionTaskIdentity]":
        _token = next_token
        while True:
            _response = await self.describe_maintenance_window_execution_tasks(
                window_execution_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("window_execution_task_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_windows(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_windows_result.DescribeMaintenanceWindowsResult":
        """<p>Retrieves the maintenance windows in an Amazon Web Services account.</p>

        Args:
            filters: <p>Optional filters used to narrow down the scope of the returned maintenance windows. Supported filter keys are <code>Name</code> and <code>Enabled</code>. For example, <code>Name=MyMaintenanceWindow</code> and <code>Enabled=True</code>.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_windows_request.DescribeMaintenanceWindowsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_windows_result.DescribeMaintenanceWindowsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_windows

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_windows.async_describe_maintenance_windows(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_windows_request.DescribeMaintenanceWindowsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_maintenance_windows(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.maintenance_window_identity.MaintenanceWindowIdentity]":
        _token = next_token
        while True:
            _response = await self.describe_maintenance_windows(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("window_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_window_schedule(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        window_id: Optional[
            "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
        ] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        resource_type: Optional[
            "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
        ] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_search_max_results.MaintenanceWindowSearchMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_window_schedule_result.DescribeMaintenanceWindowScheduleResult":
        """<p>Retrieves information about upcoming executions of a maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window to retrieve information about.</p>
            targets: <p>The managed node ID or key-value pair to retrieve information about.</p>
            resource_type: <p>The type of resource you want to retrieve information about. For example, <code>INSTANCE</code>.</p>
            filters: <p>Filters used to limit the range of results. For example, you can limit maintenance window executions to only those scheduled before or after a certain date and time.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_window_schedule_request.DescribeMaintenanceWindowScheduleRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_window_schedule_result.DescribeMaintenanceWindowScheduleResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_window_schedule

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_window_schedule.async_describe_maintenance_window_schedule(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_window_schedule_request.DescribeMaintenanceWindowScheduleRequest = {}
        if window_id is not None:
            input_["window_id"] = window_id
        if targets is not None:
            input_["targets"] = targets
        if resource_type is not None:
            input_["resource_type"] = resource_type
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_maintenance_window_schedule(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        window_id: Optional[
            "capo_ssm.types.maintenance_window_id.MaintenanceWindowId"
        ] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        resource_type: Optional[
            "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType"
        ] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_search_max_results.MaintenanceWindowSearchMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.scheduled_window_execution.ScheduledWindowExecution]":
        _token = next_token
        while True:
            _response = await self.describe_maintenance_window_schedule(
                config_overrides=config_overrides,
                window_id=window_id,
                targets=targets,
                resource_type=resource_type,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("scheduled_window_executions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_windows_for_target(
        self,
        targets: "capo_ssm.types.targets.Targets",
        resource_type: "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_search_max_results.MaintenanceWindowSearchMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_windows_for_target_result.DescribeMaintenanceWindowsForTargetResult":
        """<p>Retrieves information about the maintenance window targets or tasks that a managed node is associated with.</p>

        Args:
            targets: <p>The managed node ID or key-value pair to retrieve information about.</p>
            resource_type: <p>The type of resource you want to retrieve information about. For example, <code>INSTANCE</code>.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_windows_for_target_request.DescribeMaintenanceWindowsForTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_windows_for_target_result.DescribeMaintenanceWindowsForTargetResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_windows_for_target

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_windows_for_target.async_describe_maintenance_windows_for_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_windows_for_target_request.DescribeMaintenanceWindowsForTargetRequest = {
            "targets": targets,
            "resource_type": resource_type,
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

    async def iter_describe_maintenance_windows_for_target(
        self,
        targets: "capo_ssm.types.targets.Targets",
        resource_type: "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_search_max_results.MaintenanceWindowSearchMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.maintenance_window_identity_for_target.MaintenanceWindowIdentityForTarget]":
        _token = next_token
        while True:
            _response = await self.describe_maintenance_windows_for_target(
                targets,
                resource_type,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("window_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_window_targets(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_window_targets_result.DescribeMaintenanceWindowTargetsResult":
        """<p>Lists the targets registered with the maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window whose targets should be retrieved.</p>
            filters: <p>Optional filters that can be used to narrow down the scope of the returned window targets. The supported filter keys are <code>Type</code>, <code>WindowTargetId</code>, and <code>OwnerInformation</code>.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_window_targets_request.DescribeMaintenanceWindowTargetsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_window_targets_result.DescribeMaintenanceWindowTargetsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_window_targets

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_window_targets.async_describe_maintenance_window_targets(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_window_targets_request.DescribeMaintenanceWindowTargetsRequest = {
            "window_id": window_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_maintenance_window_targets(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.maintenance_window_target.MaintenanceWindowTarget]":
        _token = next_token
        while True:
            _response = await self.describe_maintenance_window_targets(
                window_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("targets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_maintenance_window_tasks(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_maintenance_window_tasks_result.DescribeMaintenanceWindowTasksResult":
        """<p>Lists the tasks in a maintenance window.</p> <note> <p>For maintenance window tasks without a specified target, you can't supply values for <code>--max-errors</code> and <code>--max-concurrency</code>. Instead, the system inserts a placeholder value of <code>1</code>, which may be reported in the response to this command. These values don't affect the running of your task and can be ignored.</p> </note>

        Args:
            window_id: <p>The ID of the maintenance window whose tasks should be retrieved.</p>
            filters: <p>Optional filters used to narrow down the scope of the returned tasks. The supported filter keys are <code>WindowTaskId</code>, <code>TaskArn</code>, <code>Priority</code>, and <code>TaskType</code>.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_maintenance_window_tasks_request.DescribeMaintenanceWindowTasksRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_maintenance_window_tasks_result.DescribeMaintenanceWindowTasksResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_maintenance_window_tasks

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_maintenance_window_tasks.async_describe_maintenance_window_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_maintenance_window_tasks_request.DescribeMaintenanceWindowTasksRequest = {
            "window_id": window_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_maintenance_window_tasks(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.maintenance_window_filter_list.MaintenanceWindowFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.maintenance_window_max_results.MaintenanceWindowMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.maintenance_window_task.MaintenanceWindowTask]":
        _token = next_token
        while True:
            _response = await self.describe_maintenance_window_tasks(
                window_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_ops_items(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        ops_item_filters: Optional[
            "capo_ssm.types.ops_item_filters.OpsItemFilters"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.ops_item_max_results.OpsItemMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
    ) -> "capo_ssm.types.describe_ops_items_response.DescribeOpsItemsResponse":
        """<p>Query a set of OpsItems. You must have permission in Identity and Access Management (IAM) to query a list of OpsItems. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html">Set up OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html">Amazon Web Services Systems Manager OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>

        Args:
            ops_item_filters: <p>One or more filters to limit the response.</p> <ul> <li> <p>Key: CreatedTime</p> <p>Operations: GreaterThan, LessThan</p> </li> <li> <p>Key: LastModifiedBy</p> <p>Operations: Contains, Equals</p> </li> <li> <p>Key: LastModifiedTime</p> <p>Operations: GreaterThan, LessThan</p> </li> <li> <p>Key: Priority</p> <p>Operations: Equals</p> </li> <li> <p>Key: Source</p> <p>Operations: Contains, Equals</p> </li> <li> <p>Key: Status</p> <p>Operations: Equals</p> </li> <li> <p>Key: Title*</p> <p>Operations: Equals,Contains</p> </li> <li> <p>Key: OperationalData**</p> <p>Operations: Equals</p> </li> <li> <p>Key: OperationalDataKey</p> <p>Operations: Equals</p> </li> <li> <p>Key: OperationalDataValue</p> <p>Operations: Equals, Contains</p> </li> <li> <p>Key: OpsItemId</p> <p>Operations: Equals</p> </li> <li> <p>Key: ResourceId</p> <p>Operations: Contains</p> </li> <li> <p>Key: AutomationId</p> <p>Operations: Equals</p> </li> <li> <p>Key: AccountId</p> <p>Operations: Equals</p> </li> </ul> <p>*The Equals operator for Title matches the first 100 characters. If you specify more than 100 characters, they system returns an error that the filter value exceeds the length limit.</p> <p>**If you filter the response by using the OperationalData operator, specify a key-value pair by using the following JSON format: {"key":"key_name","value":"a_value"}</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_ops_items_request.DescribeOpsItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_ops_items_response.DescribeOpsItemsResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_ops_items

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_ops_items.async_describe_ops_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_ops_items_request.DescribeOpsItemsRequest = {}
        if ops_item_filters is not None:
            input_["ops_item_filters"] = ops_item_filters
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

    async def iter_describe_ops_items(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        ops_item_filters: Optional[
            "capo_ssm.types.ops_item_filters.OpsItemFilters"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.ops_item_max_results.OpsItemMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
    ) -> "AsyncIterator[capo_ssm.types.ops_item_summary.OpsItemSummary]":
        _token = next_token
        while True:
            _response = await self.describe_ops_items(
                config_overrides=config_overrides,
                ops_item_filters=ops_item_filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ops_item_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_parameters(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.parameters_filter_list.ParametersFilterList"
        ] = None,
        parameter_filters: Optional[
            "capo_ssm.types.parameter_string_filter_list.ParameterStringFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        shared: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.describe_parameters_result.DescribeParametersResult":
        """<p>Lists the parameters in your Amazon Web Services account or the parameters shared with you when you enable the <a href="https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html#systemsmanager-DescribeParameters-request-Shared">Shared</a> option.</p> <p>Request results are returned on a best-effort basis. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of <code>MaxResults</code>. If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a <code>NextToken</code>. You can specify the <code>NextToken</code> in a subsequent call to get the next set of results.</p> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p> <important> <p>If you change the KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, <code>DescribeParameters</code> retrieves whatever the original key alias was referencing.</p> </important>

        Args:
            filters: <p>This data type is deprecated. Instead, use <code>ParameterFilters</code>.</p>
            parameter_filters: <p>Filters to limit the request results.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            shared: <p>Lists parameters that are shared with you.</p> <note> <p>By default when using this option, the command returns parameters that have been shared using a standard Resource Access Manager Resource Share. In order for a parameter that was shared using the <a>PutResourcePolicy</a> command to be returned, the associated <code>RAM Resource Share Created From Policy</code> must have been promoted to a standard Resource Share using the RAM <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a> API operation.</p> <p>For more information about sharing parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html">Working with shared parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </note>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_filter_option.InvalidFilterOption: <p>The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.</p>
            capo_ssm.errors.invalid_filter_value.InvalidFilterValue: <p>The filter value isn't valid. Verify the value and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_parameters_request.DescribeParametersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_parameters_result.DescribeParametersResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_parameters

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_parameters.async_describe_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_parameters_request.DescribeParametersRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if parameter_filters is not None:
            input_["parameter_filters"] = parameter_filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if shared is not None:
            input_["shared"] = shared

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_parameters(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.parameters_filter_list.ParametersFilterList"
        ] = None,
        parameter_filters: Optional[
            "capo_ssm.types.parameter_string_filter_list.ParameterStringFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        shared: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[capo_ssm.types.describe_parameters_result.DescribeParametersResult]":
        _token = next_token
        while True:
            _response = await self.describe_parameters(
                config_overrides=config_overrides,
                filters=filters,
                parameter_filters=parameter_filters,
                max_results=max_results,
                next_token=_token,
                shared=shared,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_patch_baselines(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_patch_baselines_result.DescribePatchBaselinesResult":
        """<p>Lists the patch baselines in your Amazon Web Services account.</p>

        Args:
            filters: <p>Each element in the array is a structure containing a key-value pair.</p> <p>Supported keys for <code>DescribePatchBaselines</code> include the following:</p> <ul> <li> <p> <b> <code>NAME_PREFIX</code> </b> </p> <p>Sample values: <code>AWS-</code> | <code>My-</code> </p> </li> <li> <p> <b> <code>OWNER</code> </b> </p> <p>Sample values: <code>AWS</code> | <code>Self</code> </p> </li> <li> <p> <b> <code>OPERATING_SYSTEM</code> </b> </p> <p>Sample values: <code>AMAZON_LINUX</code> | <code>SUSE</code> | <code>WINDOWS</code> </p> </li> </ul>
            max_results: <p>The maximum number of patch baselines to return (per page).</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_patch_baselines_request.DescribePatchBaselinesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_patch_baselines_result.DescribePatchBaselinesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_patch_baselines

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_patch_baselines.async_describe_patch_baselines(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_patch_baselines_request.DescribePatchBaselinesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_describe_patch_baselines(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.patch_baseline_identity.PatchBaselineIdentity]":
        _token = next_token
        while True:
            _response = await self.describe_patch_baselines(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("baseline_identities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_patch_groups(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.describe_patch_groups_result.DescribePatchGroupsResult":
        """<p>Lists all patch groups that have been registered with patch baselines.</p>

        Args:
            max_results: <p>The maximum number of patch groups to return (per page).</p>
            filters: <p>Each element in the array is a structure containing a key-value pair.</p> <p>Supported keys for <code>DescribePatchGroups</code> include the following:</p> <ul> <li> <p> <b> <code>NAME_PREFIX</code> </b> </p> <p>Sample values: <code>AWS-</code> | <code>My-</code>.</p> </li> <li> <p> <b> <code>OPERATING_SYSTEM</code> </b> </p> <p>Sample values: <code>AMAZON_LINUX</code> | <code>SUSE</code> | <code>WINDOWS</code> </p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_patch_groups_request.DescribePatchGroupsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_patch_groups_result.DescribePatchGroupsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_patch_groups

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_patch_groups.async_describe_patch_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_patch_groups_request.DescribePatchGroupsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_patch_groups(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.patch_baseline_max_results.PatchBaselineMaxResults"
        ] = None,
        filters: Optional[
            "capo_ssm.types.patch_orchestrator_filter_list.PatchOrchestratorFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.patch_group_patch_baseline_mapping.PatchGroupPatchBaselineMapping]":
        _token = next_token
        while True:
            _response = await self.describe_patch_groups(
                config_overrides=config_overrides,
                max_results=max_results,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("mappings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_patch_group_state(
        self,
        patch_group: "capo_ssm.types.patch_group.PatchGroup",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> (
        "capo_ssm.types.describe_patch_group_state_result.DescribePatchGroupStateResult"
    ):
        """<p>Returns high-level aggregated patch compliance state information for a patch group.</p>

        Args:
            patch_group: <p>The name of the patch group whose patch snapshot should be retrieved.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_patch_group_state_request.DescribePatchGroupStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_patch_group_state_result.DescribePatchGroupStateResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_patch_group_state

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_patch_group_state.async_describe_patch_group_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_patch_group_state_request.DescribePatchGroupStateRequest = {
            "patch_group": patch_group
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_patch_properties(
        self,
        operating_system: "capo_ssm.types.operating_system.OperatingSystem",
        property: "capo_ssm.types.patch_property.PatchProperty",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        patch_set: Optional["capo_ssm.types.patch_set.PatchSet"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> (
        "capo_ssm.types.describe_patch_properties_result.DescribePatchPropertiesResult"
    ):
        """<p>Lists the properties of available patches organized by product, product family, classification, severity, and other properties of available patches. You can use the reported properties in the filters you specify in requests for operations such as <a>CreatePatchBaseline</a>, <a>UpdatePatchBaseline</a>, <a>DescribeAvailablePatches</a>, and <a>DescribePatchBaselines</a>.</p> <p>The following section lists the properties that can be used in filters for each major operating system type:</p> <dl> <dt>AMAZON_LINUX</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> | <code>SEVERITY</code> </p> </dd> <dt>AMAZON_LINUX_2</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> | <code>SEVERITY</code> </p> </dd> <dt>AMAZON_LINUX_2023</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> | <code>SEVERITY</code> </p> </dd> <dt>CENTOS</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> | <code>SEVERITY</code> </p> </dd> <dt>DEBIAN</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>PRIORITY</code> </p> </dd> <dt>MACOS</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> </p> </dd> <dt>ORACLE_LINUX</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> | <code>SEVERITY</code> </p> </dd> <dt>REDHAT_ENTERPRISE_LINUX</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> | <code>SEVERITY</code> </p> </dd> <dt>SUSE</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>CLASSIFICATION</code> | <code>SEVERITY</code> </p> </dd> <dt>UBUNTU</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>PRIORITY</code> </p> </dd> <dt>WINDOWS</dt> <dd> <p>Valid properties: <code>PRODUCT</code> | <code>PRODUCT_FAMILY</code> | <code>CLASSIFICATION</code> | <code>MSRC_SEVERITY</code> </p> </dd> </dl>

        Args:
            operating_system: <p>The operating system type for which to list patches.</p>
            property: <p>The patch property for which you want to view patch details. </p>
            patch_set: <p>Indicates whether to list patches for the Windows operating system or for applications released by Microsoft. Not applicable for the Linux or macOS operating systems.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_patch_properties_request.DescribePatchPropertiesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_patch_properties_result.DescribePatchPropertiesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_patch_properties

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_patch_properties.async_describe_patch_properties(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_patch_properties_request.DescribePatchPropertiesRequest = {
            "operating_system": operating_system,
            "property": property,
        }
        if patch_set is not None:
            input_["patch_set"] = patch_set
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

    async def iter_describe_patch_properties(
        self,
        operating_system: "capo_ssm.types.operating_system.OperatingSystem",
        property: "capo_ssm.types.patch_property.PatchProperty",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        patch_set: Optional["capo_ssm.types.patch_set.PatchSet"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.patch_property_entry.PatchPropertyEntry]":
        _token = next_token
        while True:
            _response = await self.describe_patch_properties(
                operating_system,
                property,
                config_overrides=config_overrides,
                patch_set=patch_set,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("properties",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_sessions(
        self,
        state: "capo_ssm.types.session_state.SessionState",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.session_max_results.SessionMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.session_filter_list.SessionFilterList"
        ] = None,
    ) -> "capo_ssm.types.describe_sessions_response.DescribeSessionsResponse":
        """<p>Retrieves a list of all active sessions (both connected and disconnected) or terminated sessions from the past 30 days.</p>

        Args:
            state: <p>The session status to retrieve a list of sessions for. For example, "Active".</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            filters: <p>One or more filters to limit the type of sessions returned by the request.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.describe_sessions_request.DescribeSessionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.describe_sessions_response.DescribeSessionsResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.describe_sessions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.describe_sessions.async_describe_sessions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.describe_sessions_request.DescribeSessionsRequest = {
            "state": state
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_sessions(
        self,
        state: "capo_ssm.types.session_state.SessionState",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.session_max_results.SessionMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.session_filter_list.SessionFilterList"
        ] = None,
    ) -> "AsyncIterator[capo_ssm.types.session.Session]":
        _token = next_token
        while True:
            _response = await self.describe_sessions(
                state,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def disassociate_ops_item_related_item(
        self,
        ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId",
        association_id: "capo_ssm.types.ops_item_related_item_association_id.OpsItemRelatedItemAssociationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.disassociate_ops_item_related_item_response.DisassociateOpsItemRelatedItemResponse":
        """<p>Deletes the association between an OpsItem and a related item. For example, this API operation can delete an Incident Manager incident from an OpsItem. Incident Manager is a tool in Amazon Web Services Systems Manager.</p>

        Args:
            ops_item_id: <p>The ID of the OpsItem for which you want to delete an association between the OpsItem and a related item.</p>
            association_id: <p>The ID of the association for which you want to delete an association between the OpsItem and a related item.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_conflict_exception.OpsItemConflictException: <p>The specified OpsItem is in the process of being deleted.</p>
            capo_ssm.errors.ops_item_invalid_parameter_exception.OpsItemInvalidParameterException: <p>A specified parameter argument isn't valid. Verify the available arguments and try again.</p>
            capo_ssm.errors.ops_item_not_found_exception.OpsItemNotFoundException: <p>The specified OpsItem ID doesn't exist. Verify the ID and try again.</p>
            capo_ssm.errors.ops_item_related_item_association_not_found_exception.OpsItemRelatedItemAssociationNotFoundException: <p>The association wasn't found using the parameters you specified in the call. Verify the information and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.disassociate_ops_item_related_item_request.DisassociateOpsItemRelatedItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.disassociate_ops_item_related_item_response.DisassociateOpsItemRelatedItemResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.disassociate_ops_item_related_item

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.disassociate_ops_item_related_item.async_disassociate_ops_item_related_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.disassociate_ops_item_related_item_request.DisassociateOpsItemRelatedItemRequest = {
            "ops_item_id": ops_item_id,
            "association_id": association_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_access_token(
        self,
        access_request_id: "capo_ssm.types.access_request_id.AccessRequestId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_access_token_response.GetAccessTokenResponse":
        """<p>Returns a credentials set to be used with just-in-time node access.</p>

        Args:
            access_request_id: <p>The ID of a just-in-time node access request.</p>

        Raises:
            capo_ssm.errors.access_denied_exception.AccessDeniedException: <p>The requester doesn't have permissions to perform the requested operation.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because the service is throttling requests.</p>
            capo_ssm.errors.validation_exception.ValidationException: <p>The request isn't valid. Verify that you entered valid contents for the command and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_access_token_request.GetAccessTokenRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_access_token_response.GetAccessTokenResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.get_access_token

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_access_token.async_get_access_token(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_access_token_request.GetAccessTokenRequest = {
            "access_request_id": access_request_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_automation_execution(
        self,
        automation_execution_id: "capo_ssm.types.automation_execution_id.AutomationExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_automation_execution_result.GetAutomationExecutionResult":
        """<p>Get detailed information about a particular Automation execution.</p>

        Args:
            automation_execution_id: <p>The unique identifier for an existing automation execution to examine. The execution ID is returned by StartAutomationExecution when the execution of an Automation runbook is initiated.</p>

        Raises:
            capo_ssm.errors.automation_execution_not_found_exception.AutomationExecutionNotFoundException: <p>There is no automation execution information for the requested automation execution ID.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_automation_execution_request.GetAutomationExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_automation_execution_result.GetAutomationExecutionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_automation_execution

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_automation_execution.async_get_automation_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_automation_execution_request.GetAutomationExecutionRequest = {
            "automation_execution_id": automation_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_calendar_state(
        self,
        calendar_names: "capo_ssm.types.calendar_name_or_arn_list.CalendarNameOrARNList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        at_time: Optional["capo_ssm.types.iso8601_string.ISO8601String"] = None,
    ) -> "capo_ssm.types.get_calendar_state_response.GetCalendarStateResponse":
        """<p>Gets the state of a Amazon Web Services Systems Manager change calendar at the current time or a specified time. If you specify a time, <code>GetCalendarState</code> returns the state of the calendar at that specific time, and returns the next time that the change calendar state will transition. If you don't specify a time, <code>GetCalendarState</code> uses the current time. Change Calendar entries have two possible states: <code>OPEN</code> or <code>CLOSED</code>.</p> <p>If you specify more than one calendar in a request, the command returns the status of <code>OPEN</code> only if all calendars in the request are open. If one or more calendars in the request are closed, the status returned is <code>CLOSED</code>.</p> <p>For more information about Change Calendar, a tool in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar.html">Amazon Web Services Systems Manager Change Calendar</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>

        Args:
            calendar_names: <p>The names of Amazon Resource Names (ARNs) of the Systems Manager documents (SSM documents) that represent the calendar entries for which you want to get the state.</p>
            at_time: <p>(Optional) The specific time for which you want to get calendar state information, in <a href="https://en.wikipedia.org/wiki/ISO_8601">ISO 8601</a> format. If you don't specify a value or <code>AtTime</code>, the current time is used.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_type.InvalidDocumentType: <p>The SSM document type isn't valid. Valid document types are described in the <code>DocumentType</code> property.</p>
            capo_ssm.errors.unsupported_calendar_exception.UnsupportedCalendarException: <p>The calendar entry contained in the specified SSM document isn't supported.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_calendar_state_request.GetCalendarStateRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_calendar_state_response.GetCalendarStateResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.get_calendar_state

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_calendar_state.async_get_calendar_state(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_calendar_state_request.GetCalendarStateRequest = {
            "calendar_names": calendar_names
        }
        if at_time is not None:
            input_["at_time"] = at_time

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_cloud_connector(
        self,
        cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_cloud_connector_result.GetCloudConnectorResult":
        """<p>Returns detailed information about a cloud connector.</p>

        Args:
            cloud_connector_id: <p>The ID of the cloud connector to retrieve information about.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_cloud_connector_request.GetCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_cloud_connector_result.GetCloudConnectorResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_cloud_connector

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_cloud_connector.async_get_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_cloud_connector_request.GetCloudConnectorRequest = {
            "cloud_connector_id": cloud_connector_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_command_invocation(
        self,
        command_id: "capo_ssm.types.command_id.CommandId",
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        plugin_name: Optional[
            "capo_ssm.types.command_plugin_name.CommandPluginName"
        ] = None,
    ) -> "capo_ssm.types.get_command_invocation_result.GetCommandInvocationResult":
        """<p>Returns detailed information about command execution for an invocation or plugin. The Run Command API follows an eventual consistency model, due to the distributed nature of the system supporting the API. This means that the result of an API command you run that affects your resources might not be immediately visible to all subsequent commands you run. You should keep this in mind when you carry out an API command that immediately follows a previous API command.</p> <p> <code>GetCommandInvocation</code> only gives the execution status of a plugin in a document. To get the command execution status on a specific managed node, use <a>ListCommandInvocations</a>. To get the command execution status across managed nodes, use <a>ListCommands</a>.</p>

        Args:
            command_id: <p>(Required) The parent command ID of the invocation plugin.</p>
            instance_id: <p>(Required) The ID of the managed node targeted by the command. A <i>managed node</i> can be an Amazon Elastic Compute Cloud (Amazon EC2) instance, edge device, and on-premises server or VM in your hybrid environment that is configured for Amazon Web Services Systems Manager.</p>
            plugin_name: <p>The name of the step for which you want detailed results. If the document contains only one step, you can omit the name and details for that step. If the document contains more than one step, you must specify the name of the step for which you want to view details. Be sure to specify the name of the step, not the name of a plugin like <code>aws:RunShellScript</code>.</p> <p>To find the <code>PluginName</code>, check the document content and find the name of the step you want details for. Alternatively, use <a>ListCommandInvocations</a> with the <code>CommandId</code> and <code>Details</code> parameters. The <code>PluginName</code> is the <code>Name</code> attribute of the <code>CommandPlugin</code> object in the <code>CommandPlugins</code> list.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_command_id.InvalidCommandId: <p>The specified command ID isn't valid. Verify the ID and try again.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_plugin_name.InvalidPluginName: <p>The plugin name isn't valid.</p>
            capo_ssm.errors.invocation_does_not_exist.InvocationDoesNotExist: <p>The command ID and managed node ID you specified didn't match any invocations. Verify the command ID and the managed node ID and try again. </p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_command_invocation_request.GetCommandInvocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_command_invocation_result.GetCommandInvocationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_command_invocation

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_command_invocation.async_get_command_invocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_command_invocation_request.GetCommandInvocationRequest = {
            "command_id": command_id,
            "instance_id": instance_id,
        }
        if plugin_name is not None:
            input_["plugin_name"] = plugin_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_connection_status(
        self,
        target: "capo_ssm.types.session_target.SessionTarget",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_connection_status_response.GetConnectionStatusResponse":
        """<p>Retrieves the Session Manager connection status for a managed node to determine whether it is running and ready to receive Session Manager connections.</p>

        Args:
            target: <p>The managed node ID.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_connection_status_request.GetConnectionStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_connection_status_response.GetConnectionStatusResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.get_connection_status

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_connection_status.async_get_connection_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_connection_status_request.GetConnectionStatusRequest = {
            "target": target
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_default_patch_baseline(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        operating_system: Optional[
            "capo_ssm.types.operating_system.OperatingSystem"
        ] = None,
    ) -> (
        "capo_ssm.types.get_default_patch_baseline_result.GetDefaultPatchBaselineResult"
    ):
        """<p>Retrieves the default patch baseline. Amazon Web Services Systems Manager supports creating multiple default patch baselines. For example, you can create a default patch baseline for each operating system.</p> <p>If you don't specify an operating system value, the default patch baseline for Windows is returned.</p>

        Args:
            operating_system: <p>Returns the default patch baseline for the specified operating system.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_default_patch_baseline_request.GetDefaultPatchBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_default_patch_baseline_result.GetDefaultPatchBaselineResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_default_patch_baseline

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_default_patch_baseline.async_get_default_patch_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_default_patch_baseline_request.GetDefaultPatchBaselineRequest = {}
        if operating_system is not None:
            input_["operating_system"] = operating_system

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_deployable_patch_snapshot_for_instance(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        snapshot_id: "capo_ssm.types.snapshot_id.SnapshotId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        baseline_override: Optional[
            "capo_ssm.types.baseline_override.BaselineOverride"
        ] = None,
        use_s3_dual_stack_endpoint: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.get_deployable_patch_snapshot_for_instance_result.GetDeployablePatchSnapshotForInstanceResult":
        """<p>Retrieves the current snapshot for the patch baseline the managed node uses. This API is primarily used by the <code>AWS-RunPatchBaseline</code> Systems Manager document (SSM document).</p> <note> <p>If you run the command locally, such as with the Command Line Interface (CLI), the system attempts to use your local Amazon Web Services credentials and the operation fails. To avoid this, you can run the command in the Amazon Web Services Systems Manager console. Use Run Command, a tool in Amazon Web Services Systems Manager, with an SSM document that enables you to target a managed node with a script or command. For example, run the command using the <code>AWS-RunShellScript</code> document or the <code>AWS-RunPowerShellScript</code> document.</p> </note>

        Args:
            instance_id: <p>The ID of the managed node for which the appropriate patch snapshot should be retrieved.</p>
            snapshot_id: <p>The snapshot ID provided by the user when running <code>AWS-RunPatchBaseline</code>.</p>
            baseline_override: <p>Defines the basic information about a patch baseline override.</p>
            use_s3_dual_stack_endpoint: <p>Specifies whether to use S3 dualstack endpoints for the patch snapshot download URL. Set to <code>true</code> to receive a presigned URL that supports both IPv4 and IPv6 connectivity. Set to <code>false</code> to use standard IPv4-only endpoints. Default is <code>false</code>. This parameter is required for managed nodes in IPv6-only environments. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.unsupported_feature_required_exception.UnsupportedFeatureRequiredException: <p>Patching for applications released by Microsoft is only available on EC2 instances and advanced instances. To patch applications released by Microsoft on on-premises servers and VMs, you must enable advanced instances. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-managedinstances-advanced.html">Turning on the advanced-instances tier</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            capo_ssm.errors.unsupported_operating_system.UnsupportedOperatingSystem: <p>The operating systems you specified isn't supported, or the operation isn't supported for the operating system.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_deployable_patch_snapshot_for_instance_request.GetDeployablePatchSnapshotForInstanceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_deployable_patch_snapshot_for_instance_result.GetDeployablePatchSnapshotForInstanceResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_deployable_patch_snapshot_for_instance

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_deployable_patch_snapshot_for_instance.async_get_deployable_patch_snapshot_for_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_deployable_patch_snapshot_for_instance_request.GetDeployablePatchSnapshotForInstanceRequest = {
            "instance_id": instance_id,
            "snapshot_id": snapshot_id,
        }
        if baseline_override is not None:
            input_["baseline_override"] = baseline_override
        if use_s3_dual_stack_endpoint is not None:
            input_["use_s3_dual_stack_endpoint"] = use_s3_dual_stack_endpoint

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_document(
        self,
        name: "capo_ssm.types.document_arn.DocumentARN",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        version_name: Optional[
            "capo_ssm.types.document_version_name.DocumentVersionName"
        ] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        document_format: Optional[
            "capo_ssm.types.document_format.DocumentFormat"
        ] = None,
    ) -> "capo_ssm.types.get_document_result.GetDocumentResult":
        """<p>Gets the contents of the specified Amazon Web Services Systems Manager document (SSM document).</p>

        Args:
            name: <p>The name of the SSM document.</p>
            version_name: <p>An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document and can't be changed.</p>
            document_version: <p>The document version for which you want information.</p>
            document_format: <p>Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_document_request.GetDocumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_document_result.GetDocumentResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_document

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_document.async_get_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_document_request.GetDocumentRequest = {"name": name}
        if version_name is not None:
            input_["version_name"] = version_name
        if document_version is not None:
            input_["document_version"] = document_version
        if document_format is not None:
            input_["document_format"] = document_format

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_execution_preview(
        self,
        execution_preview_id: "capo_ssm.types.execution_preview_id.ExecutionPreviewId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_execution_preview_response.GetExecutionPreviewResponse":
        """<p>Initiates the process of retrieving an existing preview that shows the effects that running a specified Automation runbook would have on the targeted resources.</p>

        Args:
            execution_preview_id: <p>The ID of the existing execution preview.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_execution_preview_request.GetExecutionPreviewRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_execution_preview_response.GetExecutionPreviewResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.get_execution_preview

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_execution_preview.async_get_execution_preview(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_execution_preview_request.GetExecutionPreviewRequest = {
            "execution_preview_id": execution_preview_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_inventory(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.inventory_filter_list.InventoryFilterList"
        ] = None,
        aggregators: Optional[
            "capo_ssm.types.inventory_aggregator_list.InventoryAggregatorList"
        ] = None,
        result_attributes: Optional[
            "capo_ssm.types.result_attribute_list.ResultAttributeList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.get_inventory_result.GetInventoryResult":
        """<p>Query inventory information. This includes managed node status, such as <code>Stopped</code> or <code>Terminated</code>.</p>

        Args:
            filters: <p>One or more filters. Use a filter to return a more specific list of results.</p>
            aggregators: <p>Returns counts of inventory types based on one or more expressions. For example, if you aggregate by using an expression that uses the <code>AWS:InstanceInformation.PlatformType</code> type, you can see a count of how many Windows and Linux managed nodes exist in your inventoried fleet.</p>
            result_attributes: <p>The list of inventory item types to return.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_aggregator_exception.InvalidAggregatorException: <p>The specified aggregator isn't valid for the group type. Verify that the aggregator you provided is supported.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_inventory_group_exception.InvalidInventoryGroupException: <p>The specified inventory group isn't valid.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.invalid_result_attribute_exception.InvalidResultAttributeException: <p>The specified inventory item result attribute isn't valid.</p>
            capo_ssm.errors.invalid_type_name_exception.InvalidTypeNameException: <p>The parameter type name isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_inventory_request.GetInventoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_inventory_result.GetInventoryResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_inventory

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_inventory.async_get_inventory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_inventory_request.GetInventoryRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if aggregators is not None:
            input_["aggregators"] = aggregators
        if result_attributes is not None:
            input_["result_attributes"] = result_attributes
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

    async def iter_get_inventory(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.inventory_filter_list.InventoryFilterList"
        ] = None,
        aggregators: Optional[
            "capo_ssm.types.inventory_aggregator_list.InventoryAggregatorList"
        ] = None,
        result_attributes: Optional[
            "capo_ssm.types.result_attribute_list.ResultAttributeList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.inventory_result_entity.InventoryResultEntity]":
        _token = next_token
        while True:
            _response = await self.get_inventory(
                config_overrides=config_overrides,
                filters=filters,
                aggregators=aggregators,
                result_attributes=result_attributes,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_inventory_schema(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        type_name: Optional[
            "capo_ssm.types.inventory_item_type_name_filter.InventoryItemTypeNameFilter"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.get_inventory_schema_max_results.GetInventorySchemaMaxResults"
        ] = None,
        aggregator: Optional[
            "capo_ssm.types.aggregator_schema_only.AggregatorSchemaOnly"
        ] = None,
        sub_type: Optional["capo_ssm.types.is_sub_type_schema.IsSubTypeSchema"] = None,
    ) -> "capo_ssm.types.get_inventory_schema_result.GetInventorySchemaResult":
        """<p>Return a list of inventory type names for the account, or return a list of attribute names for a specific Inventory item type.</p>

        Args:
            type_name: <p>The type of inventory item to return.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            aggregator: <p>Returns inventory schemas that support aggregation. For example, this call returns the <code>AWS:InstanceInformation</code> type, because it supports aggregation based on the <code>PlatformName</code>, <code>PlatformType</code>, and <code>PlatformVersion</code> attributes.</p>
            sub_type: <p>Returns the sub-type schema for a specified inventory type.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.invalid_type_name_exception.InvalidTypeNameException: <p>The parameter type name isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_inventory_schema_request.GetInventorySchemaRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_inventory_schema_result.GetInventorySchemaResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_inventory_schema

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_inventory_schema.async_get_inventory_schema(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_inventory_schema_request.GetInventorySchemaRequest = {}
        if type_name is not None:
            input_["type_name"] = type_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if aggregator is not None:
            input_["aggregator"] = aggregator
        if sub_type is not None:
            input_["sub_type"] = sub_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_get_inventory_schema(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        type_name: Optional[
            "capo_ssm.types.inventory_item_type_name_filter.InventoryItemTypeNameFilter"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_ssm.types.get_inventory_schema_max_results.GetInventorySchemaMaxResults"
        ] = None,
        aggregator: Optional[
            "capo_ssm.types.aggregator_schema_only.AggregatorSchemaOnly"
        ] = None,
        sub_type: Optional["capo_ssm.types.is_sub_type_schema.IsSubTypeSchema"] = None,
    ) -> "AsyncIterator[capo_ssm.types.inventory_item_schema.InventoryItemSchema]":
        _token = next_token
        while True:
            _response = await self.get_inventory_schema(
                config_overrides=config_overrides,
                type_name=type_name,
                next_token=_token,
                max_results=max_results,
                aggregator=aggregator,
                sub_type=sub_type,
            )
            _page = _resolve_path(_response, ("schemas",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_maintenance_window(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_maintenance_window_result.GetMaintenanceWindowResult":
        """<p>Retrieves a maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window for which you want to retrieve information.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_maintenance_window_request.GetMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_maintenance_window_result.GetMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_maintenance_window.async_get_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_maintenance_window_request.GetMaintenanceWindowRequest = {
            "window_id": window_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_maintenance_window_execution(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_maintenance_window_execution_result.GetMaintenanceWindowExecutionResult":
        """<p>Retrieves details about a specific a maintenance window execution.</p>

        Args:
            window_execution_id: <p>The ID of the maintenance window execution that includes the task.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_maintenance_window_execution_request.GetMaintenanceWindowExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_maintenance_window_execution_result.GetMaintenanceWindowExecutionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_maintenance_window_execution

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_maintenance_window_execution.async_get_maintenance_window_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_maintenance_window_execution_request.GetMaintenanceWindowExecutionRequest = {
            "window_execution_id": window_execution_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_maintenance_window_execution_task(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_maintenance_window_execution_task_result.GetMaintenanceWindowExecutionTaskResult":
        """<p>Retrieves the details about a specific task run as part of a maintenance window execution.</p>

        Args:
            window_execution_id: <p>The ID of the maintenance window execution that includes the task.</p>
            task_id: <p>The ID of the specific task execution in the maintenance window task that should be retrieved.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_maintenance_window_execution_task_request.GetMaintenanceWindowExecutionTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_maintenance_window_execution_task_result.GetMaintenanceWindowExecutionTaskResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_maintenance_window_execution_task

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_maintenance_window_execution_task.async_get_maintenance_window_execution_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_maintenance_window_execution_task_request.GetMaintenanceWindowExecutionTaskRequest = {
            "window_execution_id": window_execution_id,
            "task_id": task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_maintenance_window_execution_task_invocation(
        self,
        window_execution_id: "capo_ssm.types.maintenance_window_execution_id.MaintenanceWindowExecutionId",
        task_id: "capo_ssm.types.maintenance_window_execution_task_id.MaintenanceWindowExecutionTaskId",
        invocation_id: "capo_ssm.types.maintenance_window_execution_task_invocation_id.MaintenanceWindowExecutionTaskInvocationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_maintenance_window_execution_task_invocation_result.GetMaintenanceWindowExecutionTaskInvocationResult":
        """<p>Retrieves information about a specific task running on a specific target.</p>

        Args:
            window_execution_id: <p>The ID of the maintenance window execution for which the task is a part.</p>
            task_id: <p>The ID of the specific task in the maintenance window task that should be retrieved. </p>
            invocation_id: <p>The invocation ID to retrieve.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_maintenance_window_execution_task_invocation_request.GetMaintenanceWindowExecutionTaskInvocationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_maintenance_window_execution_task_invocation_result.GetMaintenanceWindowExecutionTaskInvocationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_maintenance_window_execution_task_invocation

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_maintenance_window_execution_task_invocation.async_get_maintenance_window_execution_task_invocation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_maintenance_window_execution_task_invocation_request.GetMaintenanceWindowExecutionTaskInvocationRequest = {
            "window_execution_id": window_execution_id,
            "task_id": task_id,
            "invocation_id": invocation_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_maintenance_window_task(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        window_task_id: "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_maintenance_window_task_result.GetMaintenanceWindowTaskResult":
        """<p>Retrieves the details of a maintenance window task.</p> <note> <p>For maintenance window tasks without a specified target, you can't supply values for <code>--max-errors</code> and <code>--max-concurrency</code>. Instead, the system inserts a placeholder value of <code>1</code>, which may be reported in the response to this command. These values don't affect the running of your task and can be ignored.</p> </note> <p>To retrieve a list of tasks in a maintenance window, instead use the <a>DescribeMaintenanceWindowTasks</a> command.</p>

        Args:
            window_id: <p>The maintenance window ID that includes the task to retrieve.</p>
            window_task_id: <p>The maintenance window task ID to retrieve.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_maintenance_window_task_request.GetMaintenanceWindowTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_maintenance_window_task_result.GetMaintenanceWindowTaskResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_maintenance_window_task

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_maintenance_window_task.async_get_maintenance_window_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_maintenance_window_task_request.GetMaintenanceWindowTaskRequest = {
            "window_id": window_id,
            "window_task_id": window_task_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ops_item(
        self,
        ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        ops_item_arn: Optional["capo_ssm.types.ops_item_arn.OpsItemArn"] = None,
    ) -> "capo_ssm.types.get_ops_item_response.GetOpsItemResponse":
        """<p>Get information about an OpsItem by using the ID. You must have permission in Identity and Access Management (IAM) to view information about an OpsItem. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html">Set up OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html">Amazon Web Services Systems Manager OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>

        Args:
            ops_item_id: <p>The ID of the OpsItem that you want to get.</p>
            ops_item_arn: <p>The OpsItem Amazon Resource Name (ARN).</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_access_denied_exception.OpsItemAccessDeniedException: <p>You don't have permission to view OpsItems in the specified account. Verify that your account is configured either as a Systems Manager delegated administrator or that you are logged into the Organizations management account.</p>
            capo_ssm.errors.ops_item_not_found_exception.OpsItemNotFoundException: <p>The specified OpsItem ID doesn't exist. Verify the ID and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_ops_item_request.GetOpsItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_ops_item_response.GetOpsItemResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.get_ops_item

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_ops_item.async_get_ops_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_ops_item_request.GetOpsItemRequest = {
            "ops_item_id": ops_item_id
        }
        if ops_item_arn is not None:
            input_["ops_item_arn"] = ops_item_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_ops_metadata(
        self,
        ops_metadata_arn: "capo_ssm.types.ops_metadata_arn.OpsMetadataArn",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.get_ops_metadata_max_results.GetOpsMetadataMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.get_ops_metadata_result.GetOpsMetadataResult":
        """<p>View operational metadata related to an application in Application Manager.</p>

        Args:
            ops_metadata_arn: <p>The Amazon Resource Name (ARN) of an OpsMetadata Object to view.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_metadata_invalid_argument_exception.OpsMetadataInvalidArgumentException: <p>One of the arguments passed is invalid. </p>
            capo_ssm.errors.ops_metadata_not_found_exception.OpsMetadataNotFoundException: <p>The OpsMetadata object doesn't exist. </p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_ops_metadata_request.GetOpsMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_ops_metadata_result.GetOpsMetadataResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_ops_metadata

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_ops_metadata.async_get_ops_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_ops_metadata_request.GetOpsMetadataRequest = {
            "ops_metadata_arn": ops_metadata_arn
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

    async def get_ops_summary(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_name: Optional[
            "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
        ] = None,
        filters: Optional["capo_ssm.types.ops_filter_list.OpsFilterList"] = None,
        aggregators: Optional[
            "capo_ssm.types.ops_aggregator_list.OpsAggregatorList"
        ] = None,
        result_attributes: Optional[
            "capo_ssm.types.ops_result_attribute_list.OpsResultAttributeList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.get_ops_summary_result.GetOpsSummaryResult":
        """<p>View a summary of operations metadata (OpsData) based on specified filters and aggregators. OpsData can include information about Amazon Web Services Systems Manager OpsCenter operational workitems (OpsItems) as well as information about any Amazon Web Services resource or service configured to report OpsData to Amazon Web Services Systems Manager Explorer. </p>

        Args:
            sync_name: <p>Specify the name of a resource data sync to get.</p>
            filters: <p>Optional filters used to scope down the returned OpsData. </p>
            aggregators: <p>Optional aggregators that return counts of OpsData based on one or more expressions.</p>
            result_attributes: <p>The OpsData data type to return.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_aggregator_exception.InvalidAggregatorException: <p>The specified aggregator isn't valid for the group type. Verify that the aggregator you provided is supported.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.invalid_type_name_exception.InvalidTypeNameException: <p>The parameter type name isn't valid.</p>
            capo_ssm.errors.resource_data_sync_not_found_exception.ResourceDataSyncNotFoundException: <p>The specified sync name wasn't found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_ops_summary_request.GetOpsSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_ops_summary_result.GetOpsSummaryResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_ops_summary

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_ops_summary.async_get_ops_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_ops_summary_request.GetOpsSummaryRequest = {}
        if sync_name is not None:
            input_["sync_name"] = sync_name
        if filters is not None:
            input_["filters"] = filters
        if aggregators is not None:
            input_["aggregators"] = aggregators
        if result_attributes is not None:
            input_["result_attributes"] = result_attributes
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

    async def iter_get_ops_summary(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_name: Optional[
            "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
        ] = None,
        filters: Optional["capo_ssm.types.ops_filter_list.OpsFilterList"] = None,
        aggregators: Optional[
            "capo_ssm.types.ops_aggregator_list.OpsAggregatorList"
        ] = None,
        result_attributes: Optional[
            "capo_ssm.types.ops_result_attribute_list.OpsResultAttributeList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.ops_entity.OpsEntity]":
        _token = next_token
        while True:
            _response = await self.get_ops_summary(
                config_overrides=config_overrides,
                sync_name=sync_name,
                filters=filters,
                aggregators=aggregators,
                result_attributes=result_attributes,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("entities",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_parameter(
        self,
        name: "capo_ssm.types.ps_parameter_name.PSParameterName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        with_decryption: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.get_parameter_result.GetParameterResult":
        """<p>Get information about a single parameter by specifying the parameter name.</p> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p> <note> <p>To get information about more than one parameter at a time, use the <a>GetParameters</a> operation.</p> </note> <note> <p>Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process. This applies to <code>GetParameter</code>, <code>GetParameters</code>, and <code>PutParameter</code> API calls for your Amazon Web Services account and Amazon Web Services Region. By default, Parameter Store is configured with a standard throughput quota suitable for low- to moderate-volume workloads. Applications that retrieve configuration data infrequently or operate at smaller scale can use this default setting without additional cost.</p> <p>For higher-volume workloads, you can enable higher throughput. This increases the maximum number of supported transactions per second for your account and Region. Increased throughput supports applications and workloads that need concurrent access to multiple parameters. If you experience <code>ThrottlingException: Rate exceeded</code> errors, enable higher throughput. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html">Changing Parameter Store throughput</a>.</p> </note>

        Args:
            name: <p>The name or Amazon Resource Name (ARN) of the parameter that you want to query. For parameters shared with you from another account, you must use the full ARN.</p> <p>To query by parameter label, use <code>"Name": "name:label"</code>. To query by parameter version, use <code>"Name": "name:version"</code>.</p> <p>For more information about shared parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html">Working with shared parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            with_decryption: <p>Return decrypted values for secure string parameters. This flag is ignored for <code>String</code> and <code>StringList</code> parameter types.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_key_id.InvalidKeyId: <p>The query key ID isn't valid.</p>
            capo_ssm.errors.parameter_not_found.ParameterNotFound: <p>The parameter couldn't be found. Verify the name and try again.</p> <note> <p>For the <code>DeleteParameter</code> and <code>GetParameter</code> actions, if the specified parameter doesn't exist, the <code>ParameterNotFound</code> exception is <i>not</i> recorded in CloudTrail event logs.</p> </note>
            capo_ssm.errors.parameter_version_not_found.ParameterVersionNotFound: <p>The specified parameter version wasn't found. Verify the parameter name and version, and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_parameter_request.GetParameterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_parameter_result.GetParameterResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_parameter

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_parameter.async_get_parameter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_parameter_request.GetParameterRequest = {
            "name": name
        }
        if with_decryption is not None:
            input_["with_decryption"] = with_decryption

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_parameter_history(
        self,
        name: "capo_ssm.types.ps_parameter_name.PSParameterName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        with_decryption: Optional["capo_ssm.types.boolean.Boolean"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.get_parameter_history_result.GetParameterHistoryResult":
        """<p>Retrieves the history of all changes to a parameter.</p> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p> <important> <p>If you change the KMS key alias for the KMS key used to encrypt a parameter, then you must also update the key alias the parameter uses to reference KMS. Otherwise, <code>GetParameterHistory</code> retrieves whatever the original key alias was referencing.</p> </important>

        Args:
            name: <p>The name or Amazon Resource Name (ARN) of the parameter for which you want to review history. For parameters shared with you from another account, you must use the full ARN.</p>
            with_decryption: <p>Return decrypted values for secure string parameters. This flag is ignored for <code>String</code> and <code>StringList</code> parameter types.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_key_id.InvalidKeyId: <p>The query key ID isn't valid.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.parameter_not_found.ParameterNotFound: <p>The parameter couldn't be found. Verify the name and try again.</p> <note> <p>For the <code>DeleteParameter</code> and <code>GetParameter</code> actions, if the specified parameter doesn't exist, the <code>ParameterNotFound</code> exception is <i>not</i> recorded in CloudTrail event logs.</p> </note>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_parameter_history_request.GetParameterHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_parameter_history_result.GetParameterHistoryResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_parameter_history

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_parameter_history.async_get_parameter_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_parameter_history_request.GetParameterHistoryRequest = {
            "name": name
        }
        if with_decryption is not None:
            input_["with_decryption"] = with_decryption
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

    async def iter_get_parameter_history(
        self,
        name: "capo_ssm.types.ps_parameter_name.PSParameterName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        with_decryption: Optional["capo_ssm.types.boolean.Boolean"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.get_parameter_history_result.GetParameterHistoryResult]":
        _token = next_token
        while True:
            _response = await self.get_parameter_history(
                name,
                config_overrides=config_overrides,
                with_decryption=with_decryption,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_parameters(
        self,
        names: "capo_ssm.types.parameter_name_list.ParameterNameList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        with_decryption: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.get_parameters_result.GetParametersResult":
        """<p>Get information about one or more parameters by specifying multiple parameter names.</p> <note> <p>To get information about a single parameter, you can use the <a>GetParameter</a> operation instead.</p> </note> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p> <note> <p>Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process. This applies to <code>GetParameter</code>, <code>GetParameters</code>, and <code>PutParameter</code> API calls for your Amazon Web Services account and Amazon Web Services Region. By default, Parameter Store is configured with a standard throughput quota suitable for low- to moderate-volume workloads. Applications that retrieve configuration data infrequently or operate at smaller scale can use this default setting without additional cost.</p> <p>For higher-volume workloads, you can enable higher throughput. This increases the maximum number of supported transactions per second for your account and Region. Increased throughput supports applications and workloads that need concurrent access to multiple parameters. If you experience <code>ThrottlingException: Rate exceeded</code> errors, enable higher throughput. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html">Changing Parameter Store throughput</a>.</p> </note>

        Args:
            names: <p>The names or Amazon Resource Names (ARNs) of the parameters that you want to query. For parameters shared with you from another account, you must use the full ARNs.</p> <p>To query by parameter label, use <code>"Name": "name:label"</code>. To query by parameter version, use <code>"Name": "name:version"</code>.</p> <note> <p>The results for <code>GetParameters</code> requests are listed in alphabetical order in query responses.</p> </note> <p>For information about shared parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html">Working with shared parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            with_decryption: <p>Return decrypted secure string value. Return decrypted values for secure string parameters. This flag is ignored for <code>String</code> and <code>StringList</code> parameter types.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_key_id.InvalidKeyId: <p>The query key ID isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_parameters_request.GetParametersRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_parameters_result.GetParametersResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_parameters

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_parameters.async_get_parameters(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_parameters_request.GetParametersRequest = {
            "names": names
        }
        if with_decryption is not None:
            input_["with_decryption"] = with_decryption

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_parameters_by_path(
        self,
        path: "capo_ssm.types.ps_parameter_name.PSParameterName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        recursive: Optional["capo_ssm.types.boolean.Boolean"] = None,
        parameter_filters: Optional[
            "capo_ssm.types.parameter_string_filter_list.ParameterStringFilterList"
        ] = None,
        with_decryption: Optional["capo_ssm.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_ssm.types.get_parameters_by_path_max_results.GetParametersByPathMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.get_parameters_by_path_result.GetParametersByPathResult":
        """<p>Retrieve information about one or more parameters under a specified level in a hierarchy. </p> <p>Request results are returned on a best-effort basis. If you specify <code>MaxResults</code> in the request, the response includes information up to the limit specified. The number of items returned, however, can be between zero and the value of <code>MaxResults</code>. If the service reaches an internal limit while processing the results, it stops the operation and returns the matching values up to that point and a <code>NextToken</code>. You can specify the <code>NextToken</code> in a subsequent call to get the next set of results.</p> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p>

        Args:
            path: <p>The hierarchy for the parameter. Hierarchies start with a forward slash (/). The hierarchy is the parameter name except the last part of the parameter. For the API call to succeed, the last part of the parameter name can't be in the path. A parameter name hierarchy can have a maximum of 15 levels. Here is an example of a hierarchy: <code>/Finance/Prod/IAD/WinServ2016/license33 </code> </p>
            recursive: <p>Retrieve all parameters within a hierarchy.</p> <important> <p>If a user has access to a path, then the user can access all levels of that path. For example, if a user has permission to access path <code>/a</code>, then the user can also access <code>/a/b</code>. Even if a user has explicitly been denied access in IAM for parameter <code>/a/b</code>, they can still call the GetParametersByPath API operation recursively for <code>/a</code> and view <code>/a/b</code>.</p> </important>
            parameter_filters: <p>Filters to limit the request results.</p> <note> <p>The following <code>Key</code> values are supported for <code>GetParametersByPath</code>: <code>Type</code>, <code>KeyId</code>, and <code>Label</code>.</p> <p>The following <code>Key</code> values aren't supported for <code>GetParametersByPath</code>: <code>tag</code>, <code>DataType</code>, <code>Name</code>, <code>Path</code>, and <code>Tier</code>.</p> </note>
            with_decryption: <p>Retrieve all parameters in a hierarchy with their value decrypted.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_filter_option.InvalidFilterOption: <p>The specified filter option isn't valid. Valid options are Equals and BeginsWith. For Path filter, valid options are Recursive and OneLevel.</p>
            capo_ssm.errors.invalid_filter_value.InvalidFilterValue: <p>The filter value isn't valid. Verify the value and try again.</p>
            capo_ssm.errors.invalid_key_id.InvalidKeyId: <p>The query key ID isn't valid.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_parameters_by_path_request.GetParametersByPathRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_parameters_by_path_result.GetParametersByPathResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_parameters_by_path

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_parameters_by_path.async_get_parameters_by_path(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_parameters_by_path_request.GetParametersByPathRequest = {
            "path": path
        }
        if recursive is not None:
            input_["recursive"] = recursive
        if parameter_filters is not None:
            input_["parameter_filters"] = parameter_filters
        if with_decryption is not None:
            input_["with_decryption"] = with_decryption
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

    async def iter_get_parameters_by_path(
        self,
        path: "capo_ssm.types.ps_parameter_name.PSParameterName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        recursive: Optional["capo_ssm.types.boolean.Boolean"] = None,
        parameter_filters: Optional[
            "capo_ssm.types.parameter_string_filter_list.ParameterStringFilterList"
        ] = None,
        with_decryption: Optional["capo_ssm.types.boolean.Boolean"] = None,
        max_results: Optional[
            "capo_ssm.types.get_parameters_by_path_max_results.GetParametersByPathMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.get_parameters_by_path_result.GetParametersByPathResult]":
        _token = next_token
        while True:
            _response = await self.get_parameters_by_path(
                path,
                config_overrides=config_overrides,
                recursive=recursive,
                parameter_filters=parameter_filters,
                with_decryption=with_decryption,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_patch_baseline(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_patch_baseline_result.GetPatchBaselineResult":
        """<p>Retrieves information about a patch baseline.</p>

        Args:
            baseline_id: <p>The ID of the patch baseline to retrieve.</p> <note> <p>To retrieve information about an Amazon Web Services managed patch baseline, specify the full Amazon Resource Name (ARN) of the baseline. For example, for the baseline <code>AWS-AmazonLinuxDefaultPatchBaseline</code>, specify <code>arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0e392de35e7c563b7</code> instead of <code>pb-0e392de35e7c563b7</code>.</p> </note>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_patch_baseline_request.GetPatchBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_patch_baseline_result.GetPatchBaselineResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_patch_baseline

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_patch_baseline.async_get_patch_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_patch_baseline_request.GetPatchBaselineRequest = {
            "baseline_id": baseline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_patch_baseline_for_patch_group(
        self,
        patch_group: "capo_ssm.types.patch_group.PatchGroup",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        operating_system: Optional[
            "capo_ssm.types.operating_system.OperatingSystem"
        ] = None,
    ) -> "capo_ssm.types.get_patch_baseline_for_patch_group_result.GetPatchBaselineForPatchGroupResult":
        """<p>Retrieves the patch baseline that should be used for the specified patch group.</p>

        Args:
            patch_group: <p>The name of the patch group whose patch baseline should be retrieved.</p>
            operating_system: <p>Returns the operating system rule specified for patch groups using the patch baseline. The default value is <code>WINDOWS</code>. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_patch_baseline_for_patch_group_request.GetPatchBaselineForPatchGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_patch_baseline_for_patch_group_result.GetPatchBaselineForPatchGroupResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_patch_baseline_for_patch_group

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_patch_baseline_for_patch_group.async_get_patch_baseline_for_patch_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_patch_baseline_for_patch_group_request.GetPatchBaselineForPatchGroupRequest = {
            "patch_group": patch_group
        }
        if operating_system is not None:
            input_["operating_system"] = operating_system

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_resource_policies(
        self,
        resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
        max_results: Optional[
            "capo_ssm.types.resource_policy_max_results.ResourcePolicyMaxResults"
        ] = None,
    ) -> "capo_ssm.types.get_resource_policies_response.GetResourcePoliciesResponse":
        """<p>Returns an array of the <code>Policy</code> object.</p>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to which the policies are attached.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.resource_policy_invalid_parameter_exception.ResourcePolicyInvalidParameterException: <p>One or more parameters specified for the call aren't valid. Verify the parameters and their values and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_resource_policies_request.GetResourcePoliciesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_resource_policies_response.GetResourcePoliciesResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.get_resource_policies

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_resource_policies.async_get_resource_policies(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_resource_policies_request.GetResourcePoliciesRequest = {
            "resource_arn": resource_arn
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

    async def iter_get_resource_policies(
        self,
        resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
        max_results: Optional[
            "capo_ssm.types.resource_policy_max_results.ResourcePolicyMaxResults"
        ] = None,
    ) -> "AsyncIterator[capo_ssm.types.get_resource_policies_response_entry.GetResourcePoliciesResponseEntry]":
        _token = next_token
        while True:
            _response = await self.get_resource_policies(
                resource_arn,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("policies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def get_service_setting(
        self,
        setting_id: "capo_ssm.types.service_setting_id.ServiceSettingId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.get_service_setting_result.GetServiceSettingResult":
        """<p> <code>ServiceSetting</code> is an account-level setting for an Amazon Web Services service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an Amazon Web Services service charges money to the account based on feature or service usage, then the Amazon Web Services service team might create a default setting of <code>false</code>. This means the user can't use this feature unless they change the setting to <code>true</code> and intentionally opt in for a paid feature.</p> <p>Services map a <code>SettingId</code> object to a setting value. Amazon Web Services services teams define the default value for a <code>SettingId</code>. You can't create a new <code>SettingId</code>, but you can overwrite the default value if you have the <code>ssm:UpdateServiceSetting</code> permission for the setting. Use the <a>UpdateServiceSetting</a> API operation to change the default setting. Or use the <a>ResetServiceSetting</a> to change the value back to the original value defined by the Amazon Web Services service team.</p> <p>Query the current service setting for the Amazon Web Services account. </p>

        Args:
            setting_id: <p>The ID of the service setting to get. The setting ID can be one of the following.</p> <ul> <li> <p> <code>/ssm/appmanager/appmanager-enabled</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-destination</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-group-name</code> </p> </li> <li> <p>/ssm/automation/enable-adaptive-concurrency</p> </li> <li> <p> <code>/ssm/documents/console/public-sharing-permission</code> </p> </li> <li> <p> <code>/ssm/managed-instance/activation-tier</code> </p> </li> <li> <p> <code>/ssm/managed-instance/default-ec2-instance-management-role</code> </p> </li> <li> <p> <code>/ssm/opsinsights/opscenter</code> </p> </li> <li> <p> <code>/ssm/parameter-store/default-parameter-tier</code> </p> </li> <li> <p> <code>/ssm/parameter-store/high-throughput-enabled</code> </p> </li> </ul>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.service_setting_not_found.ServiceSettingNotFound: <p>The specified service setting wasn't found. Either the service name or the setting hasn't been provisioned by the Amazon Web Services service team.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.get_service_setting_request.GetServiceSettingRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.get_service_setting_result.GetServiceSettingResult"
        ]:
            import capo_ssm._operations.amazon_ssm.get_service_setting

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.get_service_setting.async_get_service_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.get_service_setting_request.GetServiceSettingRequest = {
            "setting_id": setting_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def label_parameter_version(
        self,
        name: "capo_ssm.types.ps_parameter_name.PSParameterName",
        labels: "capo_ssm.types.parameter_label_list.ParameterLabelList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        parameter_version: Optional[
            "capo_ssm.types.ps_parameter_version.PSParameterVersion"
        ] = None,
    ) -> "capo_ssm.types.label_parameter_version_result.LabelParameterVersionResult":
        """<p>A parameter label is a user-defined alias to help you manage different versions of a parameter. When you modify a parameter, Amazon Web Services Systems Manager automatically saves a new version and increments the version number by one. A label can help you remember the purpose of a parameter when there are multiple versions. </p> <p>Parameter labels have the following requirements and restrictions.</p> <ul> <li> <p>A version of a parameter can have a maximum of 10 labels.</p> </li> <li> <p>You can't attach the same label to different versions of the same parameter. For example, if version 1 has the label Production, then you can't attach Production to version 2.</p> </li> <li> <p>You can move a label from one version of a parameter to another.</p> </li> <li> <p>You can't create a label when you create a new parameter. You must attach a label to a specific version of a parameter.</p> </li> <li> <p>If you no longer want to use a parameter label, then you can either delete it or move it to a different version of a parameter.</p> </li> <li> <p>A label can have a maximum of 100 characters.</p> </li> <li> <p>Labels can contain letters (case sensitive), numbers, periods (.), hyphens (-), or underscores (_).</p> </li> <li> <p>Labels can't begin with a number, "<code>aws</code>" or "<code>ssm</code>" (not case sensitive). If a label fails to meet these requirements, then the label isn't associated with a parameter and the system displays it in the list of InvalidLabels.</p> </li> <li> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p> </li> </ul>

        Args:
            name: <p>The parameter name on which you want to attach one or more labels.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>
            parameter_version: <p>The specific version of the parameter on which you want to attach one or more labels. If no version is specified, the system attaches the label to the latest version.</p>
            labels: <p>One or more labels to attach to the specified parameter version.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.parameter_not_found.ParameterNotFound: <p>The parameter couldn't be found. Verify the name and try again.</p> <note> <p>For the <code>DeleteParameter</code> and <code>GetParameter</code> actions, if the specified parameter doesn't exist, the <code>ParameterNotFound</code> exception is <i>not</i> recorded in CloudTrail event logs.</p> </note>
            capo_ssm.errors.parameter_version_label_limit_exceeded.ParameterVersionLabelLimitExceeded: <p>A parameter version can have a maximum of ten labels.</p>
            capo_ssm.errors.parameter_version_not_found.ParameterVersionNotFound: <p>The specified parameter version wasn't found. Verify the parameter name and version, and try again.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.label_parameter_version_request.LabelParameterVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.label_parameter_version_result.LabelParameterVersionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.label_parameter_version

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.label_parameter_version.async_label_parameter_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.label_parameter_version_request.LabelParameterVersionRequest = {
            "name": name,
            "labels": labels,
        }
        if parameter_version is not None:
            input_["parameter_version"] = parameter_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_associations(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        association_filter_list: Optional[
            "capo_ssm.types.association_filter_list.AssociationFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.list_associations_result.ListAssociationsResult":
        """<p>Returns all State Manager associations in the current Amazon Web Services account and Amazon Web Services Region. You can limit the results to a specific State Manager association document or managed node by specifying a filter. State Manager is a tool in Amazon Web Services Systems Manager.</p>

        Args:
            association_filter_list: <p>One or more filters. Use a filter to return a more specific list of results.</p> <note> <p>Filtering associations using the <code>InstanceID</code> attribute only returns legacy associations created using the <code>InstanceID</code> attribute. Associations targeting the managed node that are part of the Target Attributes <code>ResourceGroup</code> or <code>Tags</code> aren't returned.</p> </note>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_associations_request.ListAssociationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_associations_result.ListAssociationsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_associations

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_associations.async_list_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_associations_request.ListAssociationsRequest = {}
        if association_filter_list is not None:
            input_["association_filter_list"] = association_filter_list
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

    async def iter_list_associations(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        association_filter_list: Optional[
            "capo_ssm.types.association_filter_list.AssociationFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.association.Association]":
        _token = next_token
        while True:
            _response = await self.list_associations(
                config_overrides=config_overrides,
                association_filter_list=association_filter_list,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_association_versions(
        self,
        association_id: "capo_ssm.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> (
        "capo_ssm.types.list_association_versions_result.ListAssociationVersionsResult"
    ):
        """<p>Retrieves all versions of an association for a specific association ID.</p>

        Args:
            association_id: <p>The association ID for which you want to view all versions.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_association_versions_request.ListAssociationVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_association_versions_result.ListAssociationVersionsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_association_versions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_association_versions.async_list_association_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_association_versions_request.ListAssociationVersionsRequest = {
            "association_id": association_id
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

    async def iter_list_association_versions(
        self,
        association_id: "capo_ssm.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> (
        "AsyncIterator[capo_ssm.types.association_version_info.AssociationVersionInfo]"
    ):
        _token = next_token
        while True:
            _response = await self.list_association_versions(
                association_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("association_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_cloud_connectors(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.cloud_connector_max_results.CloudConnectorMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.cloud_connector_filter_list.CloudConnectorFilterList"
        ] = None,
    ) -> "capo_ssm.types.list_cloud_connectors_result.ListCloudConnectorsResult":
        """<p>Returns a list of cloud connectors in the current Amazon Web Services account and Amazon Web Services Region.</p>

        Args:
            max_results: <p>The maximum number of items to return for this call.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            filters: <p>One or more filters to limit the cloud connectors returned in the response.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_cloud_connectors_request.ListCloudConnectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_cloud_connectors_result.ListCloudConnectorsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_cloud_connectors

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_cloud_connectors.async_list_cloud_connectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_cloud_connectors_request.ListCloudConnectorsRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_cloud_connectors(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.cloud_connector_max_results.CloudConnectorMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.cloud_connector_filter_list.CloudConnectorFilterList"
        ] = None,
    ) -> "AsyncIterator[capo_ssm.types.cloud_connector_summary.CloudConnectorSummary]":
        _token = next_token
        while True:
            _response = await self.list_cloud_connectors(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("cloud_connectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_command_invocations(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        command_id: Optional["capo_ssm.types.command_id.CommandId"] = None,
        instance_id: Optional["capo_ssm.types.instance_id.InstanceId"] = None,
        max_results: Optional[
            "capo_ssm.types.command_max_results.CommandMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.command_filter_list.CommandFilterList"
        ] = None,
        details: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.list_command_invocations_result.ListCommandInvocationsResult":
        """<p>An invocation is copy of a command sent to a specific managed node. A command can apply to one or more managed nodes. A command invocation applies to one managed node. For example, if a user runs <code>SendCommand</code> against three managed nodes, then a command invocation is created for each requested managed node ID. <code>ListCommandInvocations</code> provide status about command execution.</p>

        Args:
            command_id: <p>(Optional) The invocations for a specific command ID.</p>
            instance_id: <p>(Optional) The command execution details for a specific managed node ID.</p>
            max_results: <p>(Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>
            filters: <p>(Optional) One or more filters. Use a filter to return a more specific list of results.</p>
            details: <p>(Optional) If set this returns the response of the command executions and any command output. The default value is <code>false</code>. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_command_id.InvalidCommandId: <p>The specified command ID isn't valid. Verify the ID and try again.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_command_invocations_request.ListCommandInvocationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_command_invocations_result.ListCommandInvocationsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_command_invocations

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_command_invocations.async_list_command_invocations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_command_invocations_request.ListCommandInvocationsRequest = {}
        if command_id is not None:
            input_["command_id"] = command_id
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters
        if details is not None:
            input_["details"] = details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_command_invocations(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        command_id: Optional["capo_ssm.types.command_id.CommandId"] = None,
        instance_id: Optional["capo_ssm.types.instance_id.InstanceId"] = None,
        max_results: Optional[
            "capo_ssm.types.command_max_results.CommandMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.command_filter_list.CommandFilterList"
        ] = None,
        details: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "AsyncIterator[capo_ssm.types.command_invocation.CommandInvocation]":
        _token = next_token
        while True:
            _response = await self.list_command_invocations(
                config_overrides=config_overrides,
                command_id=command_id,
                instance_id=instance_id,
                max_results=max_results,
                next_token=_token,
                filters=filters,
                details=details,
            )
            _page = _resolve_path(_response, ("command_invocations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_commands(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        command_id: Optional["capo_ssm.types.command_id.CommandId"] = None,
        instance_id: Optional["capo_ssm.types.instance_id.InstanceId"] = None,
        max_results: Optional[
            "capo_ssm.types.command_max_results.CommandMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.command_filter_list.CommandFilterList"
        ] = None,
    ) -> "capo_ssm.types.list_commands_result.ListCommandsResult":
        """<p>Lists the commands requested by users of the Amazon Web Services account.</p>

        Args:
            command_id: <p>(Optional) If provided, lists only the specified command.</p>
            instance_id: <p>(Optional) Lists commands issued against this managed node ID.</p> <note> <p>You can't specify a managed node ID in the same command that you specify <code>Status</code> = <code>Pending</code>. This is because the command hasn't reached the managed node yet.</p> </note>
            max_results: <p>(Optional) The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>(Optional) The token for the next set of items to return. (You received this token from a previous call.)</p>
            filters: <p>(Optional) One or more filters. Use a filter to return a more specific list of results. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_command_id.InvalidCommandId: <p>The specified command ID isn't valid. Verify the ID and try again.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_commands_request.ListCommandsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_commands_result.ListCommandsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_commands

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_commands.async_list_commands(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_commands_request.ListCommandsRequest = {}
        if command_id is not None:
            input_["command_id"] = command_id
        if instance_id is not None:
            input_["instance_id"] = instance_id
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_list_commands(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        command_id: Optional["capo_ssm.types.command_id.CommandId"] = None,
        instance_id: Optional["capo_ssm.types.instance_id.InstanceId"] = None,
        max_results: Optional[
            "capo_ssm.types.command_max_results.CommandMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        filters: Optional[
            "capo_ssm.types.command_filter_list.CommandFilterList"
        ] = None,
    ) -> "AsyncIterator[capo_ssm.types.command.Command]":
        _token = next_token
        while True:
            _response = await self.list_commands(
                config_overrides=config_overrides,
                command_id=command_id,
                instance_id=instance_id,
                max_results=max_results,
                next_token=_token,
                filters=filters,
            )
            _page = _resolve_path(_response, ("commands",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_compliance_items(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
        ] = None,
        resource_ids: Optional[
            "capo_ssm.types.compliance_resource_id_list.ComplianceResourceIdList"
        ] = None,
        resource_types: Optional[
            "capo_ssm.types.compliance_resource_type_list.ComplianceResourceTypeList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.list_compliance_items_result.ListComplianceItemsResult":
        """<p>For a specified resource ID, this API operation returns a list of compliance statuses for different resource types. Currently, you can only specify one resource ID per call. List results depend on the criteria specified in the filter.</p>

        Args:
            filters: <p>One or more compliance filters. Use a filter to return a more specific list of results.</p>
            resource_ids: <p>The ID for the resources from which to get compliance information. Currently, you can only specify one resource ID.</p>
            resource_types: <p>The type of resource from which to get compliance information. Currently, the only supported resource type is <code>ManagedInstance</code>.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.invalid_resource_type.InvalidResourceType: <p>The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_compliance_items_request.ListComplianceItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_compliance_items_result.ListComplianceItemsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_compliance_items

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_compliance_items.async_list_compliance_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_compliance_items_request.ListComplianceItemsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if resource_ids is not None:
            input_["resource_ids"] = resource_ids
        if resource_types is not None:
            input_["resource_types"] = resource_types
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

    async def iter_list_compliance_items(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
        ] = None,
        resource_ids: Optional[
            "capo_ssm.types.compliance_resource_id_list.ComplianceResourceIdList"
        ] = None,
        resource_types: Optional[
            "capo_ssm.types.compliance_resource_type_list.ComplianceResourceTypeList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.compliance_item.ComplianceItem]":
        _token = next_token
        while True:
            _response = await self.list_compliance_items(
                config_overrides=config_overrides,
                filters=filters,
                resource_ids=resource_ids,
                resource_types=resource_types,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("compliance_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_compliance_summaries(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_ssm.types.list_compliance_summaries_result.ListComplianceSummariesResult"
    ):
        """<p>Returns a summary count of compliant and non-compliant resources for a compliance type. For example, this call can return State Manager associations, patches, or custom compliance types according to the filter criteria that you specify.</p>

        Args:
            filters: <p>One or more compliance or inventory filters. Use a filter to return a more specific list of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            max_results: <p>The maximum number of items to return for this call. Currently, you can specify null or 50. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_compliance_summaries_request.ListComplianceSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_compliance_summaries_result.ListComplianceSummariesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_compliance_summaries

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_compliance_summaries.async_list_compliance_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_compliance_summaries_request.ListComplianceSummariesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_compliance_summaries(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.compliance_summary_item.ComplianceSummaryItem]":
        _token = next_token
        while True:
            _response = await self.list_compliance_summaries(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("compliance_summary_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_document_metadata_history(
        self,
        name: "capo_ssm.types.document_name.DocumentName",
        metadata: "capo_ssm.types.document_metadata_enum.DocumentMetadataEnum",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.list_document_metadata_history_response.ListDocumentMetadataHistoryResponse":
        """<important> <p>Amazon Web Services Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html">Amazon Web Services Systems Manager Change Manager availability change</a>.</p> </important> <p>Information about approval reviews for a version of a change template in Change Manager.</p>

        Args:
            name: <p>The name of the change template.</p>
            document_version: <p>The version of the change template.</p>
            metadata: <p>The type of data for which details are being requested. Currently, the only supported value is <code>DocumentReviews</code>.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_document_metadata_history_request.ListDocumentMetadataHistoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_document_metadata_history_response.ListDocumentMetadataHistoryResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.list_document_metadata_history

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_document_metadata_history.async_list_document_metadata_history(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_document_metadata_history_request.ListDocumentMetadataHistoryRequest = {
            "name": name,
            "metadata": metadata,
        }
        if document_version is not None:
            input_["document_version"] = document_version
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

    async def list_documents(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_filter_list: Optional[
            "capo_ssm.types.document_filter_list.DocumentFilterList"
        ] = None,
        filters: Optional[
            "capo_ssm.types.document_key_values_filter_list.DocumentKeyValuesFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.list_documents_result.ListDocumentsResult":
        """<p>Returns all Systems Manager (SSM) documents in the current Amazon Web Services account and Amazon Web Services Region. You can limit the results of this request by using a filter.</p>

        Args:
            document_filter_list: <p>This data type is deprecated. Instead, use <code>Filters</code>.</p>
            filters: <p>One or more <code>DocumentKeyValuesFilter</code> objects. Use a filter to return a more specific list of results. For keys, you can specify one or more key-value pair tags that have been applied to a document. Other valid keys include <code>Owner</code>, <code>Name</code>, <code>PlatformTypes</code>, <code>DocumentType</code>, and <code>TargetType</code>. For example, to return documents you own use <code>Key=Owner,Values=Self</code>. To specify a custom key-value pair, use the format <code>Key=tag:tagName,Values=valueName</code>.</p> <note> <p>This API operation only supports filtering documents by using a single tag key and one or more tag values. For example: <code>Key=tag:tagName,Values=valueName1,valueName2</code> </p> </note>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter_key.InvalidFilterKey: <p>The specified key isn't valid.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_documents_request.ListDocumentsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_documents_result.ListDocumentsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_documents

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_documents.async_list_documents(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_documents_request.ListDocumentsRequest = {}
        if document_filter_list is not None:
            input_["document_filter_list"] = document_filter_list
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_documents(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_filter_list: Optional[
            "capo_ssm.types.document_filter_list.DocumentFilterList"
        ] = None,
        filters: Optional[
            "capo_ssm.types.document_key_values_filter_list.DocumentKeyValuesFilterList"
        ] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.document_identifier.DocumentIdentifier]":
        _token = next_token
        while True:
            _response = await self.list_documents(
                config_overrides=config_overrides,
                document_filter_list=document_filter_list,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("document_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_document_versions(
        self,
        name: "capo_ssm.types.document_arn.DocumentARN",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.list_document_versions_result.ListDocumentVersionsResult":
        """<p>List all versions for a document.</p>

        Args:
            name: <p>The name of the document. You can specify an Amazon Resource Name (ARN).</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_document_versions_request.ListDocumentVersionsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_document_versions_result.ListDocumentVersionsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_document_versions

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_document_versions.async_list_document_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_document_versions_request.ListDocumentVersionsRequest = {
            "name": name
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

    async def iter_list_document_versions(
        self,
        name: "capo_ssm.types.document_arn.DocumentARN",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.document_version_info.DocumentVersionInfo]":
        _token = next_token
        while True:
            _response = await self.list_document_versions(
                name,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("document_versions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_inventory_entries(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        type_name: "capo_ssm.types.inventory_item_type_name.InventoryItemTypeName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.inventory_filter_list.InventoryFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.list_inventory_entries_result.ListInventoryEntriesResult":
        """<p>A list of inventory items returned by the request.</p>

        Args:
            instance_id: <p>The managed node ID for which you want inventory information.</p>
            type_name: <p>The type of inventory item for which you want information.</p>
            filters: <p>One or more filters. Use a filter to return a more specific list of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.invalid_type_name_exception.InvalidTypeNameException: <p>The parameter type name isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_inventory_entries_request.ListInventoryEntriesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_inventory_entries_result.ListInventoryEntriesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_inventory_entries

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_inventory_entries.async_list_inventory_entries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_inventory_entries_request.ListInventoryEntriesRequest = {
            "instance_id": instance_id,
            "type_name": type_name,
        }
        if filters is not None:
            input_["filters"] = filters
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

    async def list_nodes(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_name: Optional[
            "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
        ] = None,
        filters: Optional["capo_ssm.types.node_filter_list.NodeFilterList"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.list_nodes_result.ListNodesResult":
        """<p>Takes in filters and returns a list of managed nodes matching the filter criteria.</p>

        Args:
            sync_name: <p>The name of the Amazon Web Services managed resource data sync to retrieve information about.</p> <p>For cross-account/cross-Region configurations, this parameter is required, and the name of the supported resource data sync is <code>AWS-QuickSetup-ManagedNode</code>.</p> <p>For single account/single-Region configurations, the parameter is not required.</p>
            filters: <p>One or more filters. Use a filter to return a more specific list of managed nodes.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.resource_data_sync_not_found_exception.ResourceDataSyncNotFoundException: <p>The specified sync name wasn't found.</p>
            capo_ssm.errors.unsupported_operation_exception.UnsupportedOperationException: <p>This operation is not supported for the current account. You must first enable the Systems Manager integrated experience in your account.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_nodes_request.ListNodesRequest]",
        ) -> AsyncOperationResponse["capo_ssm.types.list_nodes_result.ListNodesResult"]:
            import capo_ssm._operations.amazon_ssm.list_nodes

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_nodes.async_list_nodes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_nodes_request.ListNodesRequest = {}
        if sync_name is not None:
            input_["sync_name"] = sync_name
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_nodes(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_name: Optional[
            "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
        ] = None,
        filters: Optional["capo_ssm.types.node_filter_list.NodeFilterList"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.node.Node]":
        _token = next_token
        while True:
            _response = await self.list_nodes(
                config_overrides=config_overrides,
                sync_name=sync_name,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("nodes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_nodes_summary(
        self,
        aggregators: "capo_ssm.types.node_aggregator_list.NodeAggregatorList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_name: Optional[
            "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
        ] = None,
        filters: Optional["capo_ssm.types.node_filter_list.NodeFilterList"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.list_nodes_summary_result.ListNodesSummaryResult":
        """<p>Generates a summary of managed instance/node metadata based on the filters and aggregators you specify. Results are grouped by the input aggregator you specify.</p>

        Args:
            sync_name: <p>The name of the Amazon Web Services managed resource data sync to retrieve information about.</p> <p>For cross-account/cross-Region configurations, this parameter is required, and the name of the supported resource data sync is <code>AWS-QuickSetup-ManagedNode</code>.</p> <p>For single account/single-Region configurations, the parameter is not required.</p>
            filters: <p>One or more filters. Use a filter to generate a summary that matches your specified filter criteria.</p>
            aggregators: <p>Specify one or more aggregators to return a count of managed nodes that match that expression. For example, a count of managed nodes by operating system.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.) The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_aggregator_exception.InvalidAggregatorException: <p>The specified aggregator isn't valid for the group type. Verify that the aggregator you provided is supported.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.resource_data_sync_not_found_exception.ResourceDataSyncNotFoundException: <p>The specified sync name wasn't found.</p>
            capo_ssm.errors.unsupported_operation_exception.UnsupportedOperationException: <p>This operation is not supported for the current account. You must first enable the Systems Manager integrated experience in your account.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            ListNodesSummary
            This example illustrates one usage of ListNodesSummary

            >>> await client.list_nodes_summary(sync_name='AWS-QuickSetup-ManagedNode', aggregators=[{'AggregatorType': 'Count', 'TypeName': 'Instance', 'AttributeName': 'Region'}], filters=[{'Key': 'InstanceStatus', 'Values': ['Active'], 'Type': 'Equal'}], max_results=2, next_token='A9lT8CAxj9aDFRi+MNAoFq08I---EXAMPLE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_nodes_summary_request.ListNodesSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_nodes_summary_result.ListNodesSummaryResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_nodes_summary

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_nodes_summary.async_list_nodes_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_nodes_summary_request.ListNodesSummaryRequest = {
            "aggregators": aggregators
        }
        if sync_name is not None:
            input_["sync_name"] = sync_name
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_nodes_summary(
        self,
        aggregators: "capo_ssm.types.node_aggregator_list.NodeAggregatorList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_name: Optional[
            "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName"
        ] = None,
        filters: Optional["capo_ssm.types.node_filter_list.NodeFilterList"] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.node_summary.NodeSummary]":
        _token = next_token
        while True:
            _response = await self.list_nodes_summary(
                aggregators,
                config_overrides=config_overrides,
                sync_name=sync_name,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ops_item_events(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.ops_item_event_filters.OpsItemEventFilters"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.ops_item_event_max_results.OpsItemEventMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
    ) -> "capo_ssm.types.list_ops_item_events_response.ListOpsItemEventsResponse":
        """<p>Returns a list of all OpsItem events in the current Amazon Web Services Region and Amazon Web Services account. You can limit the results to events associated with specific OpsItems by specifying a filter.</p>

        Args:
            filters: <p>One or more OpsItem filters. Use a filter to return a more specific list of results. </p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results. </p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_invalid_parameter_exception.OpsItemInvalidParameterException: <p>A specified parameter argument isn't valid. Verify the available arguments and try again.</p>
            capo_ssm.errors.ops_item_limit_exceeded_exception.OpsItemLimitExceededException: <p>The request caused OpsItems to exceed one or more quotas.</p>
            capo_ssm.errors.ops_item_not_found_exception.OpsItemNotFoundException: <p>The specified OpsItem ID doesn't exist. Verify the ID and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_ops_item_events_request.ListOpsItemEventsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_ops_item_events_response.ListOpsItemEventsResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.list_ops_item_events

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_ops_item_events.async_list_ops_item_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_ops_item_events_request.ListOpsItemEventsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_ops_item_events(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.ops_item_event_filters.OpsItemEventFilters"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.ops_item_event_max_results.OpsItemEventMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
    ) -> "AsyncIterator[capo_ssm.types.ops_item_event_summary.OpsItemEventSummary]":
        _token = next_token
        while True:
            _response = await self.list_ops_item_events(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ops_item_related_items(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        ops_item_id: Optional["capo_ssm.types.ops_item_id.OpsItemId"] = None,
        filters: Optional[
            "capo_ssm.types.ops_item_related_items_filters.OpsItemRelatedItemsFilters"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.ops_item_related_items_max_results.OpsItemRelatedItemsMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
    ) -> "capo_ssm.types.list_ops_item_related_items_response.ListOpsItemRelatedItemsResponse":
        """<p>Lists all related-item resources associated with a Systems Manager OpsCenter OpsItem. OpsCenter is a tool in Amazon Web Services Systems Manager.</p>

        Args:
            ops_item_id: <p>The ID of the OpsItem for which you want to list all related-item resources.</p>
            filters: <p>One or more OpsItem filters. Use a filter to return a more specific list of results. </p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_invalid_parameter_exception.OpsItemInvalidParameterException: <p>A specified parameter argument isn't valid. Verify the available arguments and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_ops_item_related_items_request.ListOpsItemRelatedItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_ops_item_related_items_response.ListOpsItemRelatedItemsResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.list_ops_item_related_items

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_ops_item_related_items.async_list_ops_item_related_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_ops_item_related_items_request.ListOpsItemRelatedItemsRequest = {}
        if ops_item_id is not None:
            input_["ops_item_id"] = ops_item_id
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_ops_item_related_items(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        ops_item_id: Optional["capo_ssm.types.ops_item_id.OpsItemId"] = None,
        filters: Optional[
            "capo_ssm.types.ops_item_related_items_filters.OpsItemRelatedItemsFilters"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.ops_item_related_items_max_results.OpsItemRelatedItemsMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.string.String"] = None,
    ) -> "AsyncIterator[capo_ssm.types.ops_item_related_item_summary.OpsItemRelatedItemSummary]":
        _token = next_token
        while True:
            _response = await self.list_ops_item_related_items(
                config_overrides=config_overrides,
                ops_item_id=ops_item_id,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_ops_metadata(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.ops_metadata_filter_list.OpsMetadataFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.list_ops_metadata_max_results.ListOpsMetadataMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.list_ops_metadata_result.ListOpsMetadataResult":
        """<p>Amazon Web Services Systems Manager calls this API operation when displaying all Application Manager OpsMetadata objects or blobs.</p>

        Args:
            filters: <p>One or more filters to limit the number of OpsMetadata objects returned by the call.</p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_metadata_invalid_argument_exception.OpsMetadataInvalidArgumentException: <p>One of the arguments passed is invalid. </p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_ops_metadata_request.ListOpsMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_ops_metadata_result.ListOpsMetadataResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_ops_metadata

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_ops_metadata.async_list_ops_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_ops_metadata_request.ListOpsMetadataRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_ops_metadata(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.ops_metadata_filter_list.OpsMetadataFilterList"
        ] = None,
        max_results: Optional[
            "capo_ssm.types.list_ops_metadata_max_results.ListOpsMetadataMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.ops_metadata.OpsMetadata]":
        _token = next_token
        while True:
            _response = await self.list_ops_metadata(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("ops_metadata_list",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_compliance_summaries(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.list_resource_compliance_summaries_result.ListResourceComplianceSummariesResult":
        """<p>Returns a resource-level summary count. The summary includes information about compliant and non-compliant statuses and detailed compliance-item severity counts, according to the filter criteria you specify.</p>

        Args:
            filters: <p>One or more filters. Use a filter to return a more specific list of results.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_filter.InvalidFilter: <p>The filter name isn't valid. Verify that you entered the correct name and try again.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_resource_compliance_summaries_request.ListResourceComplianceSummariesRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_resource_compliance_summaries_result.ListResourceComplianceSummariesResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_resource_compliance_summaries

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_resource_compliance_summaries.async_list_resource_compliance_summaries(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_resource_compliance_summaries_request.ListResourceComplianceSummariesRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    async def iter_list_resource_compliance_summaries(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        filters: Optional[
            "capo_ssm.types.compliance_string_filter_list.ComplianceStringFilterList"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.resource_compliance_summary_item.ResourceComplianceSummaryItem]":
        _token = next_token
        while True:
            _response = await self.list_resource_compliance_summaries(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resource_compliance_summary_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_resource_data_sync(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_type: Optional[
            "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "capo_ssm.types.list_resource_data_sync_result.ListResourceDataSyncResult":
        """<p>Lists your resource data sync configurations. Includes information about the last time a sync attempted to start, the last sync status, and the last time a sync successfully completed.</p> <p>The number of sync configurations might be too large to return using a single call to <code>ListResourceDataSync</code>. You can limit the number of sync configurations returned by using the <code>MaxResults</code> parameter. To determine whether there are more sync configurations to list, check the value of <code>NextToken</code> in the output. If there are more sync configurations to list, you can request them by specifying the <code>NextToken</code> returned in the call to the parameter of a subsequent call. </p>

        Args:
            sync_type: <p>View a list of resource data syncs according to the sync type. Specify <code>SyncToDestination</code> to view resource data syncs that synchronize data to an Amazon S3 bucket. Specify <code>SyncFromSource</code> to view resource data syncs from Organizations or from multiple Amazon Web Services Regions.</p>
            next_token: <p>A token to start the list. Use this token to get the next set of results. </p>
            max_results: <p>The maximum number of items to return for this call. The call also returns a token that you can specify in a subsequent call to get the next set of results.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_next_token.InvalidNextToken: <p>The specified token isn't valid.</p>
            capo_ssm.errors.resource_data_sync_invalid_configuration_exception.ResourceDataSyncInvalidConfigurationException: <p>The specified sync configuration is invalid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_resource_data_sync_request.ListResourceDataSyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_resource_data_sync_result.ListResourceDataSyncResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_resource_data_sync

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_resource_data_sync.async_list_resource_data_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_resource_data_sync_request.ListResourceDataSyncRequest = {}
        if sync_type is not None:
            input_["sync_type"] = sync_type
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

    async def iter_list_resource_data_sync(
        self,
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        sync_type: Optional[
            "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
        max_results: Optional["capo_ssm.types.max_results.MaxResults"] = None,
    ) -> "AsyncIterator[capo_ssm.types.resource_data_sync_item.ResourceDataSyncItem]":
        _token = next_token
        while True:
            _response = await self.list_resource_data_sync(
                config_overrides=config_overrides,
                sync_type=sync_type,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resource_data_sync_items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def list_tags_for_resource(
        self,
        resource_type: "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging",
        resource_id: "capo_ssm.types.resource_id.ResourceId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.list_tags_for_resource_result.ListTagsForResourceResult":
        """<p>Returns a list of the tags assigned to the specified resource.</p> <p>For information about the ID format for each supported resource type, see <a>AddTagsToResource</a>.</p>

        Args:
            resource_type: <p>Returns a list of tags for a specific resource type.</p>
            resource_id: <p>The resource ID for which you want to see a list of tags.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.invalid_resource_type.InvalidResourceType: <p>The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.list_tags_for_resource_result.ListTagsForResourceResult"
        ]:
            import capo_ssm._operations.amazon_ssm.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_type": resource_type,
            "resource_id": resource_id,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_document_permission(
        self,
        name: "capo_ssm.types.document_name.DocumentName",
        permission_type: "capo_ssm.types.document_permission_type.DocumentPermissionType",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        account_ids_to_add: Optional[
            "capo_ssm.types.account_id_list.AccountIdList"
        ] = None,
        account_ids_to_remove: Optional[
            "capo_ssm.types.account_id_list.AccountIdList"
        ] = None,
        shared_document_version: Optional[
            "capo_ssm.types.shared_document_version.SharedDocumentVersion"
        ] = None,
    ) -> "capo_ssm.types.modify_document_permission_response.ModifyDocumentPermissionResponse":
        """<p>Shares a Amazon Web Services Systems Manager document (SSM document)publicly or privately. If you share a document privately, you must specify the Amazon Web Services user IDs for those people who can use the document. If you share a document publicly, you must specify <i>All</i> as the account ID.</p>

        Args:
            name: <p>The name of the document that you want to share.</p>
            permission_type: <p>The permission type for the document. The permission type can be <i>Share</i>.</p>
            account_ids_to_add: <p>The Amazon Web Services users that should have access to the document. The account IDs can either be a group of account IDs or <i>All</i>. You must specify a value for this parameter or the <code>AccountIdsToRemove</code> parameter.</p>
            account_ids_to_remove: <p>The Amazon Web Services users that should no longer have access to the document. The Amazon Web Services user can either be a group of account IDs or <i>All</i>. This action has a higher priority than <code>AccountIdsToAdd</code>. If you specify an ID to add and the same ID to remove, the system removes access to the document. You must specify a value for this parameter or the <code>AccountIdsToAdd</code> parameter.</p>
            shared_document_version: <p>(Optional) The version of the document to share. If it isn't specified, the system choose the <code>Default</code> version to share.</p>

        Raises:
            capo_ssm.errors.document_limit_exceeded.DocumentLimitExceeded: <p>You can have at most 500 active SSM documents.</p>
            capo_ssm.errors.document_permission_limit.DocumentPermissionLimit: <p>The document can't be shared with more Amazon Web Services accounts. You can specify a maximum of 20 accounts per API operation to share a private document.</p> <p>By default, you can share a private document with a maximum of 1,000 accounts and publicly share up to five documents.</p> <p>If you need to increase the quota for privately or publicly shared Systems Manager documents, contact Amazon Web Services Support.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_permission_type.InvalidPermissionType: <p>The permission type isn't supported. <i>Share</i> is the only supported permission type.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.modify_document_permission_request.ModifyDocumentPermissionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.modify_document_permission_response.ModifyDocumentPermissionResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.modify_document_permission

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.modify_document_permission.async_modify_document_permission(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.modify_document_permission_request.ModifyDocumentPermissionRequest = {
            "name": name,
            "permission_type": permission_type,
        }
        if account_ids_to_add is not None:
            input_["account_ids_to_add"] = account_ids_to_add
        if account_ids_to_remove is not None:
            input_["account_ids_to_remove"] = account_ids_to_remove
        if shared_document_version is not None:
            input_["shared_document_version"] = shared_document_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_compliance_items(
        self,
        resource_id: "capo_ssm.types.compliance_resource_id.ComplianceResourceId",
        resource_type: "capo_ssm.types.compliance_resource_type.ComplianceResourceType",
        compliance_type: "capo_ssm.types.compliance_type_name.ComplianceTypeName",
        execution_summary: "capo_ssm.types.compliance_execution_summary.ComplianceExecutionSummary",
        items: "capo_ssm.types.compliance_item_entry_list.ComplianceItemEntryList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        item_content_hash: Optional[
            "capo_ssm.types.compliance_item_content_hash.ComplianceItemContentHash"
        ] = None,
        upload_type: Optional[
            "capo_ssm.types.compliance_upload_type.ComplianceUploadType"
        ] = None,
    ) -> "capo_ssm.types.put_compliance_items_result.PutComplianceItemsResult":
        """<p>Registers a compliance type and other compliance details on a designated resource. This operation lets you register custom compliance details with a resource. This call overwrites existing compliance information on the resource, so you must provide a full list of compliance items each time that you send the request.</p> <p>ComplianceType can be one of the following:</p> <ul> <li> <p>ExecutionId: The execution ID when the patch, association, or custom compliance item was applied.</p> </li> <li> <p>ExecutionType: Specify patch, association, or Custom:<code>string</code>.</p> </li> <li> <p>ExecutionTime. The time the patch, association, or custom compliance item was applied to the managed node.</p> <important> <p>For State Manager associations, this represents the time when compliance status was captured by the Systems Manager service during its internal compliance aggregation workflow, not necessarily when the association was executed on the managed node. State Manager updates compliance information for all associations on an instance whenever any association executes, which may result in multiple associations showing the same execution time.</p> </important> </li> <li> <p>Id: The patch, association, or custom compliance ID.</p> </li> <li> <p>Title: A title.</p> </li> <li> <p>Status: The status of the compliance item. For example, <code>approved</code> for patches, or <code>Failed</code> for associations.</p> </li> <li> <p>Severity: A patch severity. For example, <code>Critical</code>.</p> </li> <li> <p>DocumentName: An SSM document name. For example, <code>AWS-RunPatchBaseline</code>.</p> </li> <li> <p>DocumentVersion: An SSM document version number. For example, 4.</p> </li> <li> <p>Classification: A patch classification. For example, <code>security updates</code>.</p> </li> <li> <p>PatchBaselineId: A patch baseline ID.</p> </li> <li> <p>PatchSeverity: A patch severity. For example, <code>Critical</code>.</p> </li> <li> <p>PatchState: A patch state. For example, <code>InstancesWithFailedPatches</code>.</p> </li> <li> <p>PatchGroup: The name of a patch group.</p> </li> <li> <p>InstalledTime: The time the association, patch, or custom compliance item was applied to the resource. Specify the time by using the following format: <code>yyyy-MM-dd'T'HH:mm:ss'Z'</code> </p> </li> </ul>

        Args:
            resource_id: <p>Specify an ID for this resource. For a managed node, this is the node ID.</p>
            resource_type: <p>Specify the type of resource. <code>ManagedInstance</code> is currently the only supported resource type.</p>
            compliance_type: <p>Specify the compliance type. For example, specify Association (for a State Manager association), Patch, or Custom:<code>string</code>.</p>
            execution_summary: <p>A summary of the call execution that includes an execution ID, the type of execution (for example, <code>Command</code>), and the date/time of the execution using a datetime object that is saved in the following format: <code>yyyy-MM-dd'T'HH:mm:ss'Z'</code> </p>
            items: <p>Information about the compliance as defined by the resource type. For example, for a patch compliance type, <code>Items</code> includes information about the PatchSeverity, Classification, and so on.</p>
            item_content_hash: <p>MD5 or SHA-256 content hash. The content hash is used to determine if existing information should be overwritten or ignored. If the content hashes match, the request to put compliance information is ignored.</p>
            upload_type: <p>The mode for uploading compliance items. You can specify <code>COMPLETE</code> or <code>PARTIAL</code>. In <code>COMPLETE</code> mode, the system overwrites all existing compliance information for the resource. You must provide a full list of compliance items each time you send the request.</p> <p>In <code>PARTIAL</code> mode, the system overwrites compliance information for a specific association. The association must be configured with <code>SyncCompliance</code> set to <code>MANUAL</code>. By default, all requests use <code>COMPLETE</code> mode.</p> <note> <p>This attribute is only valid for association compliance.</p> </note>

        Raises:
            capo_ssm.errors.compliance_type_count_limit_exceeded_exception.ComplianceTypeCountLimitExceededException: <p>You specified too many custom compliance types. You can specify a maximum of 10 different types. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_item_content_exception.InvalidItemContentException: <p>One or more content items isn't valid.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.invalid_resource_type.InvalidResourceType: <p>The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.</p>
            capo_ssm.errors.item_size_limit_exceeded_exception.ItemSizeLimitExceededException: <p>The inventory item size has exceeded the size limit.</p>
            capo_ssm.errors.total_size_limit_exceeded_exception.TotalSizeLimitExceededException: <p>The size of inventory data has exceeded the total size limit for the resource.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.put_compliance_items_request.PutComplianceItemsRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.put_compliance_items_result.PutComplianceItemsResult"
        ]:
            import capo_ssm._operations.amazon_ssm.put_compliance_items

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.put_compliance_items.async_put_compliance_items(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.put_compliance_items_request.PutComplianceItemsRequest = {
            "resource_id": resource_id,
            "resource_type": resource_type,
            "compliance_type": compliance_type,
            "execution_summary": execution_summary,
            "items": items,
        }
        if item_content_hash is not None:
            input_["item_content_hash"] = item_content_hash
        if upload_type is not None:
            input_["upload_type"] = upload_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_inventory(
        self,
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        items: "capo_ssm.types.inventory_item_list.InventoryItemList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.put_inventory_result.PutInventoryResult":
        """<p>Bulk update custom inventory items on one or more managed nodes. The request adds an inventory item, if it doesn't already exist, or updates an inventory item, if it does exist.</p>

        Args:
            instance_id: <p>An managed node ID where you want to add or update inventory items.</p>
            items: <p>The inventory items that you want to add or update on managed nodes.</p>

        Raises:
            capo_ssm.errors.custom_schema_count_limit_exceeded_exception.CustomSchemaCountLimitExceededException: <p>You have exceeded the limit for custom schemas. Delete one or more custom schemas and try again.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_inventory_item_context_exception.InvalidInventoryItemContextException: <p>You specified invalid keys or values in the <code>Context</code> attribute for <code>InventoryItem</code>. Verify the keys and values, and try again.</p>
            capo_ssm.errors.invalid_item_content_exception.InvalidItemContentException: <p>One or more content items isn't valid.</p>
            capo_ssm.errors.invalid_type_name_exception.InvalidTypeNameException: <p>The parameter type name isn't valid.</p>
            capo_ssm.errors.item_content_mismatch_exception.ItemContentMismatchException: <p>The inventory item has invalid content. </p>
            capo_ssm.errors.item_size_limit_exceeded_exception.ItemSizeLimitExceededException: <p>The inventory item size has exceeded the size limit.</p>
            capo_ssm.errors.sub_type_count_limit_exceeded_exception.SubTypeCountLimitExceededException: <p>The sub-type count exceeded the limit for the inventory type.</p>
            capo_ssm.errors.total_size_limit_exceeded_exception.TotalSizeLimitExceededException: <p>The size of inventory data has exceeded the total size limit for the resource.</p>
            capo_ssm.errors.unsupported_inventory_item_context_exception.UnsupportedInventoryItemContextException: <p>The <code>Context</code> attribute that you specified for the <code>InventoryItem</code> isn't allowed for this inventory type. You can only use the <code>Context</code> attribute with inventory types like <code>AWS:ComplianceItem</code>.</p>
            capo_ssm.errors.unsupported_inventory_schema_version_exception.UnsupportedInventorySchemaVersionException: <p>Inventory item type schema version has to match supported versions in the service. Check output of GetInventorySchema to see the available schema version for each type.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.put_inventory_request.PutInventoryRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.put_inventory_result.PutInventoryResult"
        ]:
            import capo_ssm._operations.amazon_ssm.put_inventory

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.put_inventory.async_put_inventory(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.put_inventory_request.PutInventoryRequest = {
            "instance_id": instance_id,
            "items": items,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_parameter(
        self,
        name: "capo_ssm.types.ps_parameter_name.PSParameterName",
        value: "capo_ssm.types.ps_parameter_value.PSParameterValue",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        description: Optional[
            "capo_ssm.types.parameter_description.ParameterDescription"
        ] = None,
        type: Optional["capo_ssm.types.parameter_type.ParameterType"] = None,
        key_id: Optional["capo_ssm.types.parameter_key_id.ParameterKeyId"] = None,
        overwrite: Optional["capo_ssm.types.boolean.Boolean"] = None,
        allowed_pattern: Optional[
            "capo_ssm.types.allowed_pattern.AllowedPattern"
        ] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
        tier: Optional["capo_ssm.types.parameter_tier.ParameterTier"] = None,
        policies: Optional[
            "capo_ssm.types.parameter_policies.ParameterPolicies"
        ] = None,
        data_type: Optional[
            "capo_ssm.types.parameter_data_type.ParameterDataType"
        ] = None,
    ) -> "capo_ssm.types.put_parameter_result.PutParameterResult":
        r"""<p>Create or update a parameter in Parameter Store.</p> <note> <p>Parameter Store throughput defines the number of API transactions per second (TPS) that Systems Manager can process. This applies to <code>GetParameter</code>, <code>GetParameters</code>, and <code>PutParameter</code> API calls for your Amazon Web Services account and Amazon Web Services Region. By default, Parameter Store is configured with a standard throughput quota suitable for low- to moderate-volume workloads. Applications that retrieve configuration data infrequently or operate at smaller scale can use this default setting without additional cost.</p> <p>For higher-volume workloads, you can enable higher throughput. This increases the maximum number of supported transactions per second for your account and Region. Increased throughput supports applications and workloads that need concurrent access to multiple parameters. If you experience <code>ThrottlingException: Rate exceeded</code> errors, enable higher throughput. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-throughput.html">Changing Parameter Store throughput</a>.</p> </note>

        Args:
            name: <p>The fully qualified name of the parameter that you want to create or update.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note> <p>The fully qualified name includes the complete hierarchy of the parameter path and name. For parameters in a hierarchy, you must include a leading forward slash character (/) when you create or reference a parameter. For example: <code>/Dev/DBServer/MySQL/db-string13</code> </p> <p>Naming Constraints:</p> <ul> <li> <p>Parameter names are case sensitive.</p> </li> <li> <p>A parameter name must be unique within an Amazon Web Services Region</p> </li> <li> <p>A parameter name can't be prefixed with "<code>aws</code>" or "<code>ssm</code>" (case-insensitive).</p> </li> <li> <p>Parameter names can include only the following symbols and letters: <code>a-zA-Z0-9_.-</code> </p> <p>In addition, the slash character ( / ) is used to delineate hierarchies in parameter names. For example: <code>/Dev/Production/East/Project-ABC/MyParameter</code> </p> </li> <li> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p> </li> <li> <p>Parameter hierarchies are limited to a maximum depth of fifteen levels.</p> </li> </ul> <p>For additional information about valid values for parameter names, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html">Creating Systems Manager parameters</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <note> <p>The reported maximum length of 2048 characters for a parameter name includes 1037 characters that are reserved for internal use by Systems Manager. The maximum length for a parameter name that you specify is 1011 characters.</p> <p>This count of 1011 characters includes the characters in the ARN that precede the name you specify. This ARN length will vary depending on your partition and Region. For example, the following 45 characters count toward the 1011 character maximum for a parameter created in the US East (Ohio) Region: <code>arn:aws:ssm:us-east-2:111122223333:parameter/</code>.</p> </note>
            description: <p>Information about the parameter that you want to add to the system. Optional but recommended.</p> <important> <p>Don't enter personally identifiable information in this field.</p> </important>
            value: <p>The parameter value that you want to add to the system. Standard parameters have a value limit of 4 KB. Advanced parameters have a value limit of 8 KB.</p> <note> <p>Parameters can't be referenced or nested in the values of other parameters. You can't include values wrapped in double brackets <code>{{}}</code> or <code>{{ssm:<i>parameter-name</i>}}</code> in a parameter value.</p> </note>
            type: <p>The type of parameter that you want to create.</p> <note> <p> <code>SecureString</code> isn't currently supported for CloudFormation templates.</p> </note> <p>Items in a <code>StringList</code> must be separated by a comma (,). You can't use other punctuation or special character to escape items in the list. If you have a parameter value that requires a comma, then use the <code>String</code> data type.</p> <important> <p>Specifying a parameter type isn't required when updating a parameter. You must specify a parameter type when creating a parameter.</p> </important>
            key_id: <p>The Key Management Service (KMS) ID that you want to use to encrypt a parameter. Use a custom key for better security. Required for parameters that use the <code>SecureString</code> data type.</p> <p>If you don't specify a key ID, the system uses the default key associated with your Amazon Web Services account, which is not as secure as using a custom key.</p> <ul> <li> <p>To use a custom KMS key, choose the <code>SecureString</code> data type with the <code>Key ID</code> parameter.</p> </li> </ul>
            overwrite: <p>Overwrite an existing parameter. The default value is <code>false</code>.</p>
            allowed_pattern: <p>A regular expression used to validate the parameter value. For example, for String types with values restricted to numbers, you can specify the following: AllowedPattern=^\d+$ </p>
            tags: <p>Optional metadata that you assign to a resource. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a Systems Manager parameter to identify the type of resource to which it applies, the environment, or the type of configuration data referenced by the parameter. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=Resource,Value=S3bucket</code> </p> </li> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> <li> <p> <code>Key=ParameterType,Value=LicenseKey</code> </p> </li> </ul> <note> <p>To add tags to an existing Systems Manager parameter, use the <a>AddTagsToResource</a> operation.</p> </note>
            tier: <p>The parameter tier to assign to a parameter.</p> <p>Parameter Store offers a standard tier and an advanced tier for parameters. Standard parameters have a content size limit of 4 KB and can't be configured to use parameter policies. You can create a maximum of 10,000 standard parameters for each Region in an Amazon Web Services account. Standard parameters are offered at no additional cost. </p> <p>Advanced parameters have a content size limit of 8 KB and can be configured to use parameter policies. You can create a maximum of 100,000 advanced parameters for each Region in an Amazon Web Services account. Advanced parameters incur a charge. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html">Managing parameter tiers</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>You can change a standard parameter to an advanced parameter any time. But you can't revert an advanced parameter to a standard parameter. Reverting an advanced parameter to a standard parameter would result in data loss because the system would truncate the size of the parameter from 8 KB to 4 KB. Reverting would also remove any policies attached to the parameter. Lastly, advanced parameters use a different form of encryption than standard parameters. </p> <p>If you no longer need an advanced parameter, or if you no longer want to incur charges for an advanced parameter, you must delete it and recreate it as a new standard parameter. </p> <p> <b>Using the Default Tier Configuration</b> </p> <p>In <code>PutParameter</code> requests, you can specify the tier to create the parameter in. Whenever you specify a tier in the request, Parameter Store creates or updates the parameter according to that request. However, if you don't specify a tier in a request, Parameter Store assigns the tier based on the current Parameter Store default tier configuration.</p> <p>The default tier when you begin using Parameter Store is the standard-parameter tier. If you use the advanced-parameter tier, you can specify one of the following as the default:</p> <ul> <li> <p> <b>Advanced</b>: With this option, Parameter Store evaluates all requests as advanced parameters. </p> </li> <li> <p> <b>Intelligent-Tiering</b>: With this option, Parameter Store evaluates each request to determine if the parameter is standard or advanced. </p> <p>If the request doesn't include any options that require an advanced parameter, the parameter is created in the standard-parameter tier. If one or more options requiring an advanced parameter are included in the request, Parameter Store create a parameter in the advanced-parameter tier.</p> <p>This approach helps control your parameter-related costs by always creating standard parameters unless an advanced parameter is necessary. </p> </li> </ul> <p>Options that require an advanced parameter include the following:</p> <ul> <li> <p>The content size of the parameter is more than 4 KB.</p> </li> <li> <p>The parameter uses a parameter policy.</p> </li> <li> <p>More than 10,000 parameters already exist in your Amazon Web Services account in the current Amazon Web Services Region.</p> </li> </ul> <p>For more information about configuring the default tier option, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html#ps-default-tier">Specifying a default parameter tier</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            policies: <p>One or more policies to apply to a parameter. This operation takes a JSON array. Parameter Store, a tool in Amazon Web Services Systems Manager supports the following policy types:</p> <p>Expiration: This policy deletes the parameter after it expires. When you create the policy, you specify the expiration date. You can update the expiration date and time by updating the policy. Updating the <i>parameter</i> doesn't affect the expiration date and time. When the expiration time is reached, Parameter Store deletes the parameter.</p> <p>ExpirationNotification: This policy initiates an event in Amazon CloudWatch Events that notifies you about the expiration. By using this policy, you can receive notification before or after the expiration time is reached, in units of days or hours.</p> <p>NoChangeNotification: This policy initiates a CloudWatch Events event if a parameter hasn't been modified for a specified period of time. This policy type is useful when, for example, a secret needs to be changed within a period of time, but it hasn't been changed.</p> <p>All existing policies are preserved until you send new policies or an empty policy. For more information about parameter policies, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-policies.html">Assigning parameter policies</a>. </p>
            data_type: <p>The data type for a <code>String</code> parameter. Supported data types include plain text and Amazon Machine Image (AMI) IDs.</p> <p> <b>The following data type values are supported.</b> </p> <ul> <li> <p> <code>text</code> </p> </li> <li> <p> <code>aws:ec2:image</code> </p> </li> <li> <p> <code>aws:ssm:integration</code> </p> </li> </ul> <p>When you create a <code>String</code> parameter and specify <code>aws:ec2:image</code>, Amazon Web Services Systems Manager validates the parameter value is in the required format, such as <code>ami-12345abcdeEXAMPLE</code>, and that the specified AMI is available in your Amazon Web Services account.</p> <note> <p>If the action is successful, the service sends back an HTTP 200 response which indicates a successful <code>PutParameter</code> call for all cases except for data type <code>aws:ec2:image</code>. If you call <code>PutParameter</code> with <code>aws:ec2:image</code> data type, a successful HTTP 200 response does not guarantee that your parameter was successfully created or updated. The <code>aws:ec2:image</code> value is validated asynchronously, and the <code>PutParameter</code> call returns before the validation is complete. If you submit an invalid AMI value, the PutParameter operation will return success, but the asynchronous validation will fail and the parameter will not be created or updated. To monitor whether your <code>aws:ec2:image</code> parameters are created successfully, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-cwe.html">Setting up notifications or trigger actions based on Parameter Store events</a>. For more information about AMI format validation , see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-ec2-aliases.html">Native parameter support for Amazon Machine Image IDs</a>. </p> </note>

        Raises:
            capo_ssm.errors.hierarchy_level_limit_exceeded_exception.HierarchyLevelLimitExceededException: <p>A hierarchy can have a maximum of 15 levels. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-parameter-name-constraints.html">Requirements and constraints for parameter names</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>
            capo_ssm.errors.hierarchy_type_mismatch_exception.HierarchyTypeMismatchException: <p>Parameter Store doesn't support changing a parameter type in a hierarchy. For example, you can't change a parameter from a <code>String</code> type to a <code>SecureString</code> type. You must create a new, unique parameter.</p>
            capo_ssm.errors.incompatible_policy_exception.IncompatiblePolicyException: <p>There is a conflict in the policies specified for this parameter. You can't, for example, specify two Expiration policies for a parameter. Review your policies, and try again.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_allowed_pattern_exception.InvalidAllowedPatternException: <p>The request doesn't meet the regular expression requirement.</p>
            capo_ssm.errors.invalid_key_id.InvalidKeyId: <p>The query key ID isn't valid.</p>
            capo_ssm.errors.invalid_policy_attribute_exception.InvalidPolicyAttributeException: <p>A policy attribute or its value is invalid. </p>
            capo_ssm.errors.invalid_policy_type_exception.InvalidPolicyTypeException: <p>The policy type isn't supported. Parameter Store supports the following policy types: Expiration, ExpirationNotification, and NoChangeNotification.</p>
            capo_ssm.errors.parameter_already_exists.ParameterAlreadyExists: <p>The parameter already exists. You can't create duplicate parameters.</p>
            capo_ssm.errors.parameter_limit_exceeded.ParameterLimitExceeded: <p>You have exceeded the number of parameters for this Amazon Web Services account. Delete one or more parameters and try again.</p>
            capo_ssm.errors.parameter_max_version_limit_exceeded.ParameterMaxVersionLimitExceeded: <p>Parameter Store retains the 100 most recently created versions of a parameter. After this number of versions has been created, Parameter Store deletes the oldest version when a new one is created. However, if the oldest version has a <i>label</i> attached to it, Parameter Store won't delete the version and instead presents this error message:</p> <p> <code>An error occurred (ParameterMaxVersionLimitExceeded) when calling the PutParameter operation: You attempted to create a new version of <i>parameter-name</i> by calling the PutParameter API with the overwrite flag. Version <i>version-number</i>, the oldest version, can't be deleted because it has a label associated with it. Move the label to another version of the parameter, and try again.</code> </p> <p>This safeguard is to prevent parameter versions with mission critical labels assigned to them from being deleted. To continue creating new parameters, first move the label from the oldest version of the parameter to a newer one for use in your operations. For information about moving parameter labels, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html#sysman-paramstore-labels-console-move">Move a parameter label (console)</a> or <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-labels.html#sysman-paramstore-labels-cli-move">Move a parameter label (CLI)</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>
            capo_ssm.errors.parameter_pattern_mismatch_exception.ParameterPatternMismatchException: <p>The parameter name isn't valid.</p>
            capo_ssm.errors.policies_limit_exceeded_exception.PoliciesLimitExceededException: <p>You specified more than the maximum number of allowed policies for the parameter. The maximum is 10.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.unsupported_parameter_type.UnsupportedParameterType: <p>The parameter type isn't supported.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.put_parameter_request.PutParameterRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.put_parameter_result.PutParameterResult"
        ]:
            import capo_ssm._operations.amazon_ssm.put_parameter

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.put_parameter.async_put_parameter(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.put_parameter_request.PutParameterRequest = {
            "name": name,
            "value": value,
        }
        if description is not None:
            input_["description"] = description
        if type is not None:
            input_["type"] = type
        if key_id is not None:
            input_["key_id"] = key_id
        if overwrite is not None:
            input_["overwrite"] = overwrite
        if allowed_pattern is not None:
            input_["allowed_pattern"] = allowed_pattern
        if tags is not None:
            input_["tags"] = tags
        if tier is not None:
            input_["tier"] = tier
        if policies is not None:
            input_["policies"] = policies
        if data_type is not None:
            input_["data_type"] = data_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def put_resource_policy(
        self,
        resource_arn: "capo_ssm.types.resource_arn_string.ResourceArnString",
        policy: "capo_ssm.types.policy.Policy",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        policy_id: Optional["capo_ssm.types.policy_id.PolicyId"] = None,
        policy_hash: Optional["capo_ssm.types.policy_hash.PolicyHash"] = None,
    ) -> "capo_ssm.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates a Systems Manager resource policy. A resource policy helps you to define the IAM entity (for example, an Amazon Web Services account) that can manage your Systems Manager resources. The following resources support Systems Manager resource policies.</p> <ul> <li> <p> <code>OpsItemGroup</code> - The resource policy for <code>OpsItemGroup</code> enables Amazon Web Services accounts to view and interact with OpsCenter operational work items (OpsItems).</p> </li> <li> <p> <code>Parameter</code> - The resource policy is used to share a parameter with other accounts using Resource Access Manager (RAM). </p> <p>To share a parameter, it must be in the advanced parameter tier. For information about parameter tiers, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html">Managing parameter tiers</a>. For information about changing an existing standard parameter to an advanced parameter, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-advanced-parameters.html#parameter-store-advanced-parameters-enabling">Changing a standard parameter to an advanced parameter</a>.</p> <p>To share a <code>SecureString</code> parameter, it must be encrypted with a customer managed key, and you must share the key separately through Key Management Service. Amazon Web Services managed keys cannot be shared. Parameters encrypted with the default Amazon Web Services managed key can be updated to use a customer managed key instead. For KMS key definitions, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html">KMS concepts</a> in the <i>Key Management Service Developer Guide</i>.</p> <important> <p>While you can share a parameter using the Systems Manager <code>PutResourcePolicy</code> operation, we recommend using Resource Access Manager (RAM) instead. This is because using <code>PutResourcePolicy</code> requires the extra step of promoting the parameter to a standard RAM Resource Share using the RAM <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a> API operation. Otherwise, the parameter won't be returned by the Systems Manager <a href="https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeParameters.html">DescribeParameters</a> API operation using the <code>--shared</code> option.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-shared-parameters.html#share">Sharing a parameter</a> in the <i>Amazon Web Services Systems Manager User Guide</i> </p> </important> </li> <li> <p> <code>Document</code> – Shares the document using Resource Access Manager (RAM). For more information about sharing documents, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html">Sharing Systems Manager documents</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </li> </ul> <important> <p>While you can share a document using the Systems Manager <code>PutResourcePolicy</code> operation, we recommend using Resource Access Manager (RAM) instead. Using <code>PutResourcePolicy</code> requires an extra step. You must promote the document to a standard RAM Resource Share using the RAM <a href="https://docs.aws.amazon.com/ram/latest/APIReference/API_PromoteResourceShareCreatedFromPolicy.html">PromoteResourceShareCreatedFromPolicy</a> API operation. Otherwise, the Systems Manager <a href="https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocuments.html">ListDocuments</a> API operation won't return the document when filtering for shared documents. The Amazon Web Services Config <a href="https://docs.aws.amazon.com/config/latest/APIReference/API_PutRemediationConfigurations.html">PutRemediationConfigurations</a> API operation also can't use the document.</p> </important>

        Args:
            resource_arn: <p>Amazon Resource Name (ARN) of the resource to which you want to attach a policy.</p>
            policy: <p>A policy you want to associate with a resource.</p>
            policy_id: <p>The policy ID.</p>
            policy_hash: <p>ID of the current policy version. The hash helps to prevent a situation where multiple users attempt to overwrite a policy. You must provide this hash when updating or deleting a policy.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.malformed_resource_policy_document_exception.MalformedResourcePolicyDocumentException: <p>The specified policy document is malformed or invalid, or excessive <code>PutResourcePolicy</code> or <code>DeleteResourcePolicy</code> calls have been made.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.resource_policy_conflict_exception.ResourcePolicyConflictException: <p>The hash provided in the call doesn't match the stored hash. This exception is thrown when trying to update an obsolete policy version or when multiple requests to update a policy are sent.</p>
            capo_ssm.errors.resource_policy_invalid_parameter_exception.ResourcePolicyInvalidParameterException: <p>One or more parameters specified for the call aren't valid. Verify the parameters and their values and try again.</p>
            capo_ssm.errors.resource_policy_limit_exceeded_exception.ResourcePolicyLimitExceededException: <p>The <a>PutResourcePolicy</a> API action enforces two limits. A policy can't be greater than 1024 bytes in size. And only one policy can be attached to <code>OpsItemGroup</code>. Verify these limits and try again.</p>
            capo_ssm.errors.resource_policy_not_found_exception.ResourcePolicyNotFoundException: <p>No policies with the specified policy ID and hash could be found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.put_resource_policy

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.put_resource_policy.async_put_resource_policy(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.put_resource_policy_request.PutResourcePolicyRequest = {
            "resource_arn": resource_arn,
            "policy": policy,
        }
        if policy_id is not None:
            input_["policy_id"] = policy_id
        if policy_hash is not None:
            input_["policy_hash"] = policy_hash

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_default_patch_baseline(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.register_default_patch_baseline_result.RegisterDefaultPatchBaselineResult":
        """<p>Defines the default patch baseline for the relevant operating system.</p> <p>To reset the Amazon Web Services-predefined patch baseline as the default, specify the full patch baseline Amazon Resource Name (ARN) as the baseline ID value. For example, for CentOS, specify <code>arn:aws:ssm:us-east-2:733109147000:patchbaseline/pb-0574b43a65ea646ed</code> instead of <code>pb-0574b43a65ea646ed</code>.</p>

        Args:
            baseline_id: <p>The ID of the patch baseline that should be the default patch baseline.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.register_default_patch_baseline_request.RegisterDefaultPatchBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.register_default_patch_baseline_result.RegisterDefaultPatchBaselineResult"
        ]:
            import capo_ssm._operations.amazon_ssm.register_default_patch_baseline

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.register_default_patch_baseline.async_register_default_patch_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.register_default_patch_baseline_request.RegisterDefaultPatchBaselineRequest = {
            "baseline_id": baseline_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_patch_baseline_for_patch_group(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        patch_group: "capo_ssm.types.patch_group.PatchGroup",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.register_patch_baseline_for_patch_group_result.RegisterPatchBaselineForPatchGroupResult":
        """<p>Registers a patch baseline for a patch group.</p>

        Args:
            baseline_id: <p>The ID of the patch baseline to register with the patch group.</p>
            patch_group: <p>The name of the patch group to be registered with the patch baseline.</p>

        Raises:
            capo_ssm.errors.already_exists_exception.AlreadyExistsException: <p>Error returned if an attempt is made to register a patch group with a patch baseline that is already registered with a different patch baseline.</p>
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.</p> <p>For information about resource quotas in Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.register_patch_baseline_for_patch_group_request.RegisterPatchBaselineForPatchGroupRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.register_patch_baseline_for_patch_group_result.RegisterPatchBaselineForPatchGroupResult"
        ]:
            import capo_ssm._operations.amazon_ssm.register_patch_baseline_for_patch_group

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.register_patch_baseline_for_patch_group.async_register_patch_baseline_for_patch_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.register_patch_baseline_for_patch_group_request.RegisterPatchBaselineForPatchGroupRequest = {
            "baseline_id": baseline_id,
            "patch_group": patch_group,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def register_target_with_maintenance_window(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        resource_type: "capo_ssm.types.maintenance_window_resource_type.MaintenanceWindowResourceType",
        targets: "capo_ssm.types.targets.Targets",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        owner_information: Optional[
            "capo_ssm.types.owner_information.OwnerInformation"
        ] = None,
        name: Optional[
            "capo_ssm.types.maintenance_window_name.MaintenanceWindowName"
        ] = None,
        description: Optional[
            "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
        ] = None,
        client_token: Optional["capo_ssm.types.client_token.ClientToken"] = None,
    ) -> "capo_ssm.types.register_target_with_maintenance_window_result.RegisterTargetWithMaintenanceWindowResult":
        """<p>Registers a target with a maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window the target should be registered with.</p>
            resource_type: <p>The type of target being registered with the maintenance window.</p>
            targets: <p>The targets to register with the maintenance window. In other words, the managed nodes to run commands on when the maintenance window runs.</p> <note> <p>If a single maintenance window task is registered with multiple targets, its task invocations occur sequentially and not in parallel. If your task must run on multiple targets at the same time, register a task for each target individually and assign each task the same priority level.</p> </note> <p>You can specify targets using managed node IDs, resource group names, or tags that have been applied to managed nodes.</p> <p> <b>Example 1</b>: Specify managed node IDs</p> <p> <code>Key=InstanceIds,Values=<instance-id-1>,<instance-id-2>,<instance-id-3></code> </p> <p> <b>Example 2</b>: Use tag key-pairs applied to managed nodes</p> <p> <code>Key=tag:<my-tag-key>,Values=<my-tag-value-1>,<my-tag-value-2></code> </p> <p> <b>Example 3</b>: Use tag-keys applied to managed nodes</p> <p> <code>Key=tag-key,Values=<my-tag-key-1>,<my-tag-key-2></code> </p> <p> <b>Example 4</b>: Use resource group names</p> <p> <code>Key=resource-groups:Name,Values=<resource-group-name></code> </p> <p> <b>Example 5</b>: Use filters for resource group types</p> <p> <code>Key=resource-groups:ResourceTypeFilters,Values=<resource-type-1>,<resource-type-2></code> </p> <note> <p>For <code>Key=resource-groups:ResourceTypeFilters</code>, specify resource types in the following format</p> <p> <code>Key=resource-groups:ResourceTypeFilters,Values=AWS::EC2::INSTANCE,AWS::EC2::VPC</code> </p> </note> <p>For more information about these examples formats, including the best use case for each one, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/mw-cli-tutorial-targets-examples.html">Examples: Register targets with a maintenance window</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            owner_information: <p>User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.</p>
            name: <p>An optional name for the target.</p>
            description: <p>An optional description for the target.</p>
            client_token: <p>User-provided idempotency token.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch: <p>Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.</p> <p>For information about resource quotas in Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.register_target_with_maintenance_window_request.RegisterTargetWithMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.register_target_with_maintenance_window_result.RegisterTargetWithMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.register_target_with_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.register_target_with_maintenance_window.async_register_target_with_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.register_target_with_maintenance_window_request.RegisterTargetWithMaintenanceWindowRequest = {
            "window_id": window_id,
            "resource_type": resource_type,
            "targets": targets,
        }
        if owner_information is not None:
            input_["owner_information"] = owner_information
        if name is not None:
            input_["name"] = name
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

    async def register_task_with_maintenance_window(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        task_arn: "capo_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn",
        task_type: "capo_ssm.types.maintenance_window_task_type.MaintenanceWindowTaskType",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        service_role_arn: Optional["capo_ssm.types.service_role.ServiceRole"] = None,
        task_parameters: Optional[
            "capo_ssm.types.maintenance_window_task_parameters.MaintenanceWindowTaskParameters"
        ] = None,
        task_invocation_parameters: Optional[
            "capo_ssm.types.maintenance_window_task_invocation_parameters.MaintenanceWindowTaskInvocationParameters"
        ] = None,
        priority: Optional[
            "capo_ssm.types.maintenance_window_task_priority.MaintenanceWindowTaskPriority"
        ] = None,
        max_concurrency: Optional[
            "capo_ssm.types.max_concurrency.MaxConcurrency"
        ] = None,
        max_errors: Optional["capo_ssm.types.max_errors.MaxErrors"] = None,
        logging_info: Optional["capo_ssm.types.logging_info.LoggingInfo"] = None,
        name: Optional[
            "capo_ssm.types.maintenance_window_name.MaintenanceWindowName"
        ] = None,
        description: Optional[
            "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
        ] = None,
        client_token: Optional["capo_ssm.types.client_token.ClientToken"] = None,
        cutoff_behavior: Optional[
            "capo_ssm.types.maintenance_window_task_cutoff_behavior.MaintenanceWindowTaskCutoffBehavior"
        ] = None,
        alarm_configuration: Optional[
            "capo_ssm.types.alarm_configuration.AlarmConfiguration"
        ] = None,
    ) -> "capo_ssm.types.register_task_with_maintenance_window_result.RegisterTaskWithMaintenanceWindowResult":
        """<p>Adds a new task to a maintenance window.</p>

        Args:
            window_id: <p>The ID of the maintenance window the task should be added to.</p>
            targets: <p>The targets (either managed nodes or maintenance window targets).</p> <note> <p>One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that don't specify targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">Registering maintenance window tasks without targets</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </note> <p>Specify managed nodes using the following format: </p> <p> <code>Key=InstanceIds,Values=<instance-id-1>,<instance-id-2></code> </p> <p>Specify maintenance window targets using the following format:</p> <p> <code>Key=WindowTargetIds,Values=<window-target-id-1>,<window-target-id-2></code> </p>
            task_arn: <p>The ARN of the task to run.</p>
            service_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run <code>RegisterTaskWithMaintenanceWindow</code>.</p> <p>However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html">Setting up Maintenance Windows</a> in the in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            task_type: <p>The type of task being registered.</p>
            task_parameters: <p>The parameters that should be passed to the task when it is run.</p> <note> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>
            task_invocation_parameters: <p>The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty. </p>
            priority: <p>The priority of the task in the maintenance window, the lower the number the higher the priority. Tasks in a maintenance window are scheduled in priority order with tasks that have the same priority scheduled in parallel.</p>
            max_concurrency: <p>The maximum number of targets this task can be run for, in parallel.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>
            max_errors: <p>The maximum number of errors allowed before this task stops being scheduled.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>
            logging_info: <p>A structure containing information about an Amazon Simple Storage Service (Amazon S3) bucket to write managed node-level logs to. </p> <note> <p> <code>LoggingInfo</code> has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the <code>OutputS3BucketName</code> and <code>OutputS3KeyPrefix</code> options in the <code>TaskInvocationParameters</code> structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>
            name: <p>An optional name for the task.</p>
            description: <p>An optional description for the task.</p>
            client_token: <p>User-provided idempotency token.</p>
            cutoff_behavior: <p>Indicates whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached. </p> <ul> <li> <p> <code>CONTINUE_TASK</code>: When the cutoff time is reached, any tasks that are running continue. The default value.</p> </li> <li> <p> <code>CANCEL_TASK</code>:</p> <ul> <li> <p>For Automation, Lambda, Step Functions tasks: When the cutoff time is reached, any task invocations that are already running continue, but no new task invocations are started.</p> </li> <li> <p>For Run Command tasks: When the cutoff time is reached, the system sends a <a>CancelCommand</a> operation that attempts to cancel the command associated with the task. However, there is no guarantee that the command will be terminated and the underlying process stopped.</p> </li> </ul> <p>The status for tasks that are not completed is <code>TIMED_OUT</code>.</p> </li> </ul>
            alarm_configuration: <p>The CloudWatch alarm you want to apply to your maintenance window task.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.feature_not_available_exception.FeatureNotAvailableException: <p>You attempted to register a <code>LAMBDA</code> or <code>STEP_FUNCTIONS</code> task in a region where the corresponding service isn't available. </p>
            capo_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch: <p>Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_limit_exceeded_exception.ResourceLimitExceededException: <p>Error returned when the caller has exceeded the default resource quotas. For example, too many maintenance windows or patch baselines have been created.</p> <p>For information about resource quotas in Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.register_task_with_maintenance_window_request.RegisterTaskWithMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.register_task_with_maintenance_window_result.RegisterTaskWithMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.register_task_with_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.register_task_with_maintenance_window.async_register_task_with_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.register_task_with_maintenance_window_request.RegisterTaskWithMaintenanceWindowRequest = {
            "window_id": window_id,
            "task_arn": task_arn,
            "task_type": task_type,
        }
        if targets is not None:
            input_["targets"] = targets
        if service_role_arn is not None:
            input_["service_role_arn"] = service_role_arn
        if task_parameters is not None:
            input_["task_parameters"] = task_parameters
        if task_invocation_parameters is not None:
            input_["task_invocation_parameters"] = task_invocation_parameters
        if priority is not None:
            input_["priority"] = priority
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if max_errors is not None:
            input_["max_errors"] = max_errors
        if logging_info is not None:
            input_["logging_info"] = logging_info
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if cutoff_behavior is not None:
            input_["cutoff_behavior"] = cutoff_behavior
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags_from_resource(
        self,
        resource_type: "capo_ssm.types.resource_type_for_tagging.ResourceTypeForTagging",
        resource_id: "capo_ssm.types.resource_id.ResourceId",
        tag_keys: "capo_ssm.types.key_list.KeyList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.remove_tags_from_resource_result.RemoveTagsFromResourceResult":
        """<p>Removes tag keys from the specified resource.</p>

        Args:
            resource_type: <p>The type of resource from which you want to remove a tag.</p> <note> <p>The <code>ManagedInstance</code> type for this API operation is only for on-premises managed nodes. Specify the name of the managed node in the following format: <code>mi-<i>ID_number</i> </code>. For example, <code>mi-1a2b3c4d5e6f</code>.</p> </note>
            resource_id: <p>The ID of the resource from which you want to remove tags. For example:</p> <p>ManagedInstance: mi-012345abcde</p> <p>MaintenanceWindow: mw-012345abcde</p> <p> <code>Automation</code>: <code>example-c160-4567-8519-012345abcde</code> </p> <p>PatchBaseline: pb-012345abcde</p> <p>OpsMetadata object: <code>ResourceID</code> for tagging is created from the Amazon Resource Name (ARN) for the object. Specifically, <code>ResourceID</code> is created from the strings that come after the word <code>opsmetadata</code> in the ARN. For example, an OpsMetadata object with an ARN of <code>arn:aws:ssm:us-east-2:1234567890:opsmetadata/aws/ssm/MyGroup/appmanager</code> has a <code>ResourceID</code> of either <code>aws/ssm/MyGroup/appmanager</code> or <code>/aws/ssm/MyGroup/appmanager</code>.</p> <p>For the Document and Parameter values, use the name of the resource.</p> <note> <p>The <code>ManagedInstance</code> type for this API operation is only for on-premises managed nodes. Specify the name of the managed node in the following format: mi-ID_number. For example, mi-1a2b3c4d5e6f.</p> </note>
            tag_keys: <p>Tag keys that you want to remove from the specified resource.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_resource_id.InvalidResourceId: <p>The resource ID isn't valid. Verify that you entered the correct ID and try again.</p>
            capo_ssm.errors.invalid_resource_type.InvalidResourceType: <p>The resource type isn't valid. For example, if you are attempting to tag an EC2 instance, the instance must be a registered managed node.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.remove_tags_from_resource_request.RemoveTagsFromResourceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.remove_tags_from_resource_result.RemoveTagsFromResourceResult"
        ]:
            import capo_ssm._operations.amazon_ssm.remove_tags_from_resource

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.remove_tags_from_resource.async_remove_tags_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.remove_tags_from_resource_request.RemoveTagsFromResourceRequest = {
            "resource_type": resource_type,
            "resource_id": resource_id,
            "tag_keys": tag_keys,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reset_service_setting(
        self,
        setting_id: "capo_ssm.types.service_setting_id.ServiceSettingId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.reset_service_setting_result.ResetServiceSettingResult":
        """<p> <code>ServiceSetting</code> is an account-level setting for an Amazon Web Services service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an Amazon Web Services service charges money to the account based on feature or service usage, then the Amazon Web Services service team might create a default setting of "false". This means the user can't use this feature unless they change the setting to "true" and intentionally opt in for a paid feature.</p> <p>Services map a <code>SettingId</code> object to a setting value. Amazon Web Services services teams define the default value for a <code>SettingId</code>. You can't create a new <code>SettingId</code>, but you can overwrite the default value if you have the <code>ssm:UpdateServiceSetting</code> permission for the setting. Use the <a>GetServiceSetting</a> API operation to view the current value. Use the <a>UpdateServiceSetting</a> API operation to change the default setting. </p> <p>Reset the service setting for the account to the default value as provisioned by the Amazon Web Services service team. </p>

        Args:
            setting_id: <p>The Amazon Resource Name (ARN) of the service setting to reset. The setting ID can be one of the following.</p> <ul> <li> <p> <code>/ssm/appmanager/appmanager-enabled</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-destination</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-group-name</code> </p> </li> <li> <p>/ssm/automation/enable-adaptive-concurrency</p> </li> <li> <p> <code>/ssm/documents/console/public-sharing-permission</code> </p> </li> <li> <p> <code>/ssm/managed-instance/activation-tier</code> </p> </li> <li> <p> <code>/ssm/managed-instance/default-ec2-instance-management-role</code> </p> </li> <li> <p> <code>/ssm/opsinsights/opscenter</code> </p> </li> <li> <p> <code>/ssm/parameter-store/default-parameter-tier</code> </p> </li> <li> <p> <code>/ssm/parameter-store/high-throughput-enabled</code> </p> </li> </ul>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.service_setting_not_found.ServiceSettingNotFound: <p>The specified service setting wasn't found. Either the service name or the setting hasn't been provisioned by the Amazon Web Services service team.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.reset_service_setting_request.ResetServiceSettingRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.reset_service_setting_result.ResetServiceSettingResult"
        ]:
            import capo_ssm._operations.amazon_ssm.reset_service_setting

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.reset_service_setting.async_reset_service_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.reset_service_setting_request.ResetServiceSettingRequest = {
            "setting_id": setting_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def resume_session(
        self,
        session_id: "capo_ssm.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.resume_session_response.ResumeSessionResponse":
        """<p>Reconnects a session to a managed node after it has been disconnected. Connections can be resumed for disconnected sessions, but not terminated sessions.</p> <note> <p>This command is primarily for use by client machines to automatically reconnect during intermittent network issues. It isn't intended for any other use.</p> </note>

        Args:
            session_id: <p>The ID of the disconnected session to resume.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.resume_session_request.ResumeSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.resume_session_response.ResumeSessionResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.resume_session

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.resume_session.async_resume_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.resume_session_request.ResumeSessionRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_automation_signal(
        self,
        automation_execution_id: "capo_ssm.types.automation_execution_id.AutomationExecutionId",
        signal_type: "capo_ssm.types.signal_type.SignalType",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        payload: Optional[
            "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
        ] = None,
    ) -> "capo_ssm.types.send_automation_signal_result.SendAutomationSignalResult":
        """<p>Sends a signal to an Automation execution to change the current behavior or status of the execution. </p>

        Args:
            automation_execution_id: <p>The unique identifier for an existing Automation execution that you want to send the signal to.</p>
            signal_type: <p>The type of signal to send to an Automation execution. </p>
            payload: <p>The data sent with the signal. The data schema depends on the type of signal used in the request.</p> <p>For <code>Approve</code> and <code>Reject</code> signal types, the payload is an optional comment that you can send with the signal type. For example:</p> <p> <code>Comment="Looks good"</code> </p> <p>For <code>StartStep</code> and <code>Resume</code> signal types, you must send the name of the Automation step to start or resume as the payload. For example:</p> <p> <code>StepName="step1"</code> </p> <p>For the <code>StopStep</code> signal type, you must send the step execution ID as the payload. For example:</p> <p> <code>StepExecutionId="97fff367-fc5a-4299-aed8-0123456789ab"</code> </p>

        Raises:
            capo_ssm.errors.automation_execution_not_found_exception.AutomationExecutionNotFoundException: <p>There is no automation execution information for the requested automation execution ID.</p>
            capo_ssm.errors.automation_step_not_found_exception.AutomationStepNotFoundException: <p>The specified step name and execution ID don't exist. Verify the information and try again.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_automation_signal_exception.InvalidAutomationSignalException: <p>The signal isn't valid for the current Automation execution.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.send_automation_signal_request.SendAutomationSignalRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.send_automation_signal_result.SendAutomationSignalResult"
        ]:
            import capo_ssm._operations.amazon_ssm.send_automation_signal

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.send_automation_signal.async_send_automation_signal(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.send_automation_signal_request.SendAutomationSignalRequest = {
            "automation_execution_id": automation_execution_id,
            "signal_type": signal_type,
        }
        if payload is not None:
            input_["payload"] = payload

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def send_command(
        self,
        document_name: "capo_ssm.types.document_arn.DocumentARN",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        instance_ids: Optional["capo_ssm.types.instance_id_list.InstanceIdList"] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        document_hash: Optional["capo_ssm.types.document_hash.DocumentHash"] = None,
        document_hash_type: Optional[
            "capo_ssm.types.document_hash_type.DocumentHashType"
        ] = None,
        timeout_seconds: Optional[
            "capo_ssm.types.timeout_seconds.TimeoutSeconds"
        ] = None,
        comment: Optional["capo_ssm.types.comment.Comment"] = None,
        parameters: Optional["capo_ssm.types.parameters.Parameters"] = None,
        output_s3_region: Optional["capo_ssm.types.s3_region.S3Region"] = None,
        output_s3_bucket_name: Optional[
            "capo_ssm.types.s3_bucket_name.S3BucketName"
        ] = None,
        output_s3_key_prefix: Optional[
            "capo_ssm.types.s3_key_prefix.S3KeyPrefix"
        ] = None,
        max_concurrency: Optional[
            "capo_ssm.types.max_concurrency.MaxConcurrency"
        ] = None,
        max_errors: Optional["capo_ssm.types.max_errors.MaxErrors"] = None,
        service_role_arn: Optional["capo_ssm.types.service_role.ServiceRole"] = None,
        notification_config: Optional[
            "capo_ssm.types.notification_config.NotificationConfig"
        ] = None,
        cloud_watch_output_config: Optional[
            "capo_ssm.types.cloud_watch_output_config.CloudWatchOutputConfig"
        ] = None,
        alarm_configuration: Optional[
            "capo_ssm.types.alarm_configuration.AlarmConfiguration"
        ] = None,
    ) -> "capo_ssm.types.send_command_result.SendCommandResult":
        r"""<p>Runs commands on one or more managed nodes.</p>

        Args:
            instance_ids: <p>The IDs of the managed nodes where the command should run. Specifying managed node IDs is most useful when you are targeting a limited number of managed nodes, though you can specify up to 50 IDs.</p> <p>To target a larger number of managed nodes, or if you prefer not to list individual node IDs, we recommend using the <code>Targets</code> option instead. Using <code>Targets</code>, which accepts tag key-value pairs to identify the managed nodes to send commands to, you can a send command to tens, hundreds, or thousands of nodes at once.</p> <p>For more information about how to use targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html">Run commands at scale</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            targets: <p>An array of search criteria that targets managed nodes using a <code>Key,Value</code> combination that you specify. Specifying targets is most useful when you want to send a command to a large number of managed nodes at once. Using <code>Targets</code>, which accepts tag key-value pairs to identify managed nodes, you can send a command to tens, hundreds, or thousands of nodes at once.</p> <p>To send a command to a smaller number of managed nodes, you can use the <code>InstanceIds</code> option instead.</p> <p>For more information about how to use targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html">Run commands at scale</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            document_name: <p>The name of the Amazon Web Services Systems Manager document (SSM document) to run. This can be a public document or a custom document. To run a shared document belonging to another account, specify the document Amazon Resource Name (ARN). For more information about how to use shared documents, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-using-shared.html">Sharing SSM documents</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <note> <p>If you specify a document name or ARN that hasn't been shared with your account, you receive an <code>InvalidDocument</code> error. </p> </note>
            document_version: <p>The SSM document version to use in the request. You can specify $DEFAULT, $LATEST, or a specific version number. If you run commands by using the Command Line Interface (Amazon Web Services CLI), then you must escape the first two options by using a backslash. If you specify a version number, then you don't need to use the backslash. For example:</p> <p>--document-version "\$DEFAULT"</p> <p>--document-version "\$LATEST"</p> <p>--document-version "3"</p>
            document_hash: <p>The Sha256 or Sha1 hash created by the system when the document was created. </p> <note> <p>Sha1 hashes have been deprecated.</p> </note>
            document_hash_type: <p>Sha256 or Sha1.</p> <note> <p>Sha1 hashes have been deprecated.</p> </note>
            timeout_seconds: <p>If this time is reached and the command hasn't already started running, it won't run.</p>
            comment: <p>User-specified information about the command, such as a brief description of what the command should do.</p>
            parameters: <p>The required and optional parameters specified in the document being run.</p>
            output_s3_region: <p>(Deprecated) You can no longer specify this parameter. The system ignores it. Instead, Systems Manager automatically determines the Amazon Web Services Region of the S3 bucket.</p>
            output_s3_bucket_name: <p>The name of the S3 bucket where command execution responses should be stored.</p>
            output_s3_key_prefix: <p>The directory structure within the S3 bucket where the responses should be stored.</p>
            max_concurrency: <p>(Optional) The maximum number of managed nodes that are allowed to run the command at the same time. You can specify a number such as 10 or a percentage such as 10%. The default value is <code>50</code>. For more information about how to use <code>MaxConcurrency</code>, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-velocity">Using concurrency controls</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            max_errors: <p>The maximum number of errors allowed without the command failing. When the command fails one more time beyond the value of <code>MaxErrors</code>, the systems stops sending the command to additional targets. You can specify a number like 10 or a percentage like 10%. The default value is <code>0</code>. For more information about how to use <code>MaxErrors</code>, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/send-commands-multiple.html#send-commands-maxerrors">Using error controls</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            service_role_arn: <p>The ARN of the Identity and Access Management (IAM) service role to use to publish Amazon Simple Notification Service (Amazon SNS) notifications for Run Command commands.</p> <p>This role must provide the <code>sns:Publish</code> permission for your notification topic. For information about creating and using this service role, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html">Monitoring Systems Manager status changes using Amazon SNS notifications</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            notification_config: <p>Configurations for sending notifications.</p>
            cloud_watch_output_config: <p>Enables Amazon Web Services Systems Manager to send Run Command output to Amazon CloudWatch Logs. Run Command is a tool in Amazon Web Services Systems Manager.</p>
            alarm_configuration: <p>The CloudWatch alarm you want to apply to your command.</p>

        Raises:
            capo_ssm.errors.duplicate_instance_id.DuplicateInstanceId: <p>You can't specify a managed node ID in more than one association.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.invalid_notification_config.InvalidNotificationConfig: <p>One or more configuration items isn't valid. Verify that a valid Amazon Resource Name (ARN) was provided for an Amazon Simple Notification Service topic.</p>
            capo_ssm.errors.invalid_output_folder.InvalidOutputFolder: <p>The S3 bucket doesn't exist.</p>
            capo_ssm.errors.invalid_parameters.InvalidParameters: <p>You must specify values for all required parameters in the Amazon Web Services Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.</p>
            capo_ssm.errors.invalid_role.InvalidRole: <p>The role name can't contain invalid characters. Also verify that you specified an IAM role for notifications that includes the required trust policy. For information about configuring the IAM role for Run Command notifications, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/monitoring-sns-notifications.html">Monitoring Systems Manager status changes using Amazon SNS notifications</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            capo_ssm.errors.max_document_size_exceeded.MaxDocumentSizeExceeded: <p>The size limit of a document is 64 KB.</p>
            capo_ssm.errors.unsupported_platform_type.UnsupportedPlatformType: <p>The document doesn't support the platform type of the given managed node IDs. For example, you sent an document for a Windows managed node to a Linux node.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.send_command_request.SendCommandRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.send_command_result.SendCommandResult"
        ]:
            import capo_ssm._operations.amazon_ssm.send_command

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.send_command.async_send_command(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.send_command_request.SendCommandRequest = {
            "document_name": document_name
        }
        if instance_ids is not None:
            input_["instance_ids"] = instance_ids
        if targets is not None:
            input_["targets"] = targets
        if document_version is not None:
            input_["document_version"] = document_version
        if document_hash is not None:
            input_["document_hash"] = document_hash
        if document_hash_type is not None:
            input_["document_hash_type"] = document_hash_type
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if comment is not None:
            input_["comment"] = comment
        if parameters is not None:
            input_["parameters"] = parameters
        if output_s3_region is not None:
            input_["output_s3_region"] = output_s3_region
        if output_s3_bucket_name is not None:
            input_["output_s3_bucket_name"] = output_s3_bucket_name
        if output_s3_key_prefix is not None:
            input_["output_s3_key_prefix"] = output_s3_key_prefix
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if max_errors is not None:
            input_["max_errors"] = max_errors
        if service_role_arn is not None:
            input_["service_role_arn"] = service_role_arn
        if notification_config is not None:
            input_["notification_config"] = notification_config
        if cloud_watch_output_config is not None:
            input_["cloud_watch_output_config"] = cloud_watch_output_config
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_access_request(
        self,
        reason: "capo_ssm.types.string1to256.String1to256",
        targets: "capo_ssm.types.targets.Targets",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
    ) -> "capo_ssm.types.start_access_request_response.StartAccessRequestResponse":
        """<p>Starts the workflow for just-in-time node access sessions.</p>

        Args:
            reason: <p>A brief description explaining why you are requesting access to the node.</p>
            targets: <p>The node you are requesting access to.</p>
            tags: <p>Key-value pairs of metadata you want to assign to the access request.</p>

        Raises:
            capo_ssm.errors.access_denied_exception.AccessDeniedException: <p>The requester doesn't have permissions to perform the requested operation.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request exceeds the service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_ssm.errors.throttling_exception.ThrottlingException: <p>The request or operation couldn't be performed because the service is throttling requests.</p>
            capo_ssm.errors.validation_exception.ValidationException: <p>The request isn't valid. Verify that you entered valid contents for the command and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.start_access_request_request.StartAccessRequestRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.start_access_request_response.StartAccessRequestResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.start_access_request

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.start_access_request.async_start_access_request(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.start_access_request_request.StartAccessRequestRequest = {
            "reason": reason,
            "targets": targets,
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

    async def start_associations_once(
        self,
        association_ids: "capo_ssm.types.association_id_list.AssociationIdList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.start_associations_once_result.StartAssociationsOnceResult":
        """<p>Runs an association immediately and only one time. This operation can be helpful when troubleshooting associations.</p>

        Args:
            association_ids: <p>The association IDs that you want to run immediately and only one time.</p>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.invalid_association.InvalidAssociation: <p>The association isn't valid or doesn't exist. </p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.start_associations_once_request.StartAssociationsOnceRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.start_associations_once_result.StartAssociationsOnceResult"
        ]:
            import capo_ssm._operations.amazon_ssm.start_associations_once

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.start_associations_once.async_start_associations_once(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.start_associations_once_request.StartAssociationsOnceRequest = {
            "association_ids": association_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_automation_execution(
        self,
        document_name: "capo_ssm.types.document_arn.DocumentARN",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        parameters: Optional[
            "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
        ] = None,
        client_token: Optional[
            "capo_ssm.types.idempotency_token.IdempotencyToken"
        ] = None,
        mode: Optional["capo_ssm.types.execution_mode.ExecutionMode"] = None,
        target_parameter_name: Optional[
            "capo_ssm.types.automation_parameter_key.AutomationParameterKey"
        ] = None,
        targets: Optional["capo_ssm.types.automation_targets.AutomationTargets"] = None,
        target_maps: Optional["capo_ssm.types.target_maps.TargetMaps"] = None,
        max_concurrency: Optional[
            "capo_ssm.types.max_concurrency.MaxConcurrency"
        ] = None,
        max_errors: Optional["capo_ssm.types.max_errors.MaxErrors"] = None,
        target_locations: Optional[
            "capo_ssm.types.target_locations.TargetLocations"
        ] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
        alarm_configuration: Optional[
            "capo_ssm.types.alarm_configuration.AlarmConfiguration"
        ] = None,
        target_locations_url: Optional[
            "capo_ssm.types.target_locations_url.TargetLocationsURL"
        ] = None,
    ) -> "capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult":
        """<p>Initiates execution of an Automation runbook.</p>

        Args:
            document_name: <p>The name of the SSM document to run. This can be a public document or a custom document. To run a shared document belonging to another account, specify the document ARN. For more information about how to use shared documents, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/documents-ssm-sharing.html">Sharing SSM documents</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            document_version: <p>The version of the Automation runbook to use for this execution.</p>
            parameters: <p>A key-value map of execution parameters, which match the declared parameters in the Automation runbook.</p>
            client_token: <p>User-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.</p>
            mode: <p>The execution mode of the automation. Valid modes include the following: Auto and Interactive. The default mode is Auto.</p>
            target_parameter_name: <p>The name of the parameter used as the target resource for the rate-controlled execution. Required if you specify targets.</p>
            targets: <p>A key-value mapping to target resources. Required if you specify TargetParameterName.</p> <p>If both this parameter and the <code>TargetLocation:Targets</code> parameter are supplied, <code>TargetLocation:Targets</code> takes precedence.</p>
            target_maps: <p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>
            max_concurrency: <p>The maximum number of targets allowed to run this task in parallel. You can specify a number, such as 10, or a percentage, such as 10%. The default value is <code>10</code>.</p> <p>If both this parameter and the <code>TargetLocation:TargetsMaxConcurrency</code> are supplied, <code>TargetLocation:TargetsMaxConcurrency</code> takes precedence.</p>
            max_errors: <p>The number of errors that are allowed before the system stops running the automation on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops running the automation when the fourth error is received. If you specify 0, then the system stops running the automation on additional targets after the first error result is returned. If you run an automation on 50 resources and set max-errors to 10%, then the system stops running the automation on additional targets when the sixth error is received.</p> <p>Executions that are already running an automation when max-errors is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set max-concurrency to 1 so the executions proceed one at a time.</p> <p>If this parameter and the <code>TargetLocation:TargetsMaxErrors</code> parameter are both supplied, <code>TargetLocation:TargetsMaxErrors</code> takes precedence.</p>
            target_locations: <p>A location is a combination of Amazon Web Services Regions and/or Amazon Web Services accounts where you want to run the automation. Use this operation to start an automation in multiple Amazon Web Services Regions and multiple Amazon Web Services accounts. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation-multiple-accounts-and-regions.html">Running automations in multiple Amazon Web Services Regions and accounts</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>
            tags: <p>Optional metadata that you assign to a resource. You can specify a maximum of five tags for an automation. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag an automation to identify an environment or operating system. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=environment,Value=test</code> </p> </li> <li> <p> <code>Key=OS,Value=Windows</code> </p> </li> </ul> <note> <p>The <code>Array Members</code> maximum value is reported as 1000. This number includes capacity reserved for internal operations. When calling the <code>StartAutomationExecution</code> action, you can specify a maximum of 5 tags. You can, however, use the <a>AddTagsToResource</a> action to add up to a total of 50 tags to an existing automation configuration.</p> </note>
            alarm_configuration: <p>The CloudWatch alarm you want to apply to your automation.</p>
            target_locations_url: <p>Specify a publicly accessible URL for a file that contains the <code>TargetLocations</code> body. Currently, only files in presigned Amazon S3 buckets are supported. </p>

        Raises:
            capo_ssm.errors.automation_definition_not_found_exception.AutomationDefinitionNotFoundException: <p>An Automation runbook with the specified name couldn't be found.</p>
            capo_ssm.errors.automation_definition_version_not_found_exception.AutomationDefinitionVersionNotFoundException: <p>An Automation runbook with the specified name and version couldn't be found.</p>
            capo_ssm.errors.automation_execution_limit_exceeded_exception.AutomationExecutionLimitExceededException: <p>The number of simultaneously running Automation executions exceeded the allowable limit.</p>
            capo_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch: <p>Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_automation_execution_parameters_exception.InvalidAutomationExecutionParametersException: <p>The supplied parameters for invoking the specified Automation runbook are incorrect. For example, they may not match the set of parameters permitted for the specified Automation document.</p>
            capo_ssm.errors.invalid_target.InvalidTarget: <p>The target isn't valid or doesn't exist. It might not be configured for Systems Manager or you might not have permission to perform the operation.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.start_automation_execution_request.StartAutomationExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.start_automation_execution_result.StartAutomationExecutionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.start_automation_execution

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.start_automation_execution.async_start_automation_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.start_automation_execution_request.StartAutomationExecutionRequest = {
            "document_name": document_name
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if parameters is not None:
            input_["parameters"] = parameters
        if client_token is not None:
            input_["client_token"] = client_token
        if mode is not None:
            input_["mode"] = mode
        if target_parameter_name is not None:
            input_["target_parameter_name"] = target_parameter_name
        if targets is not None:
            input_["targets"] = targets
        if target_maps is not None:
            input_["target_maps"] = target_maps
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if max_errors is not None:
            input_["max_errors"] = max_errors
        if target_locations is not None:
            input_["target_locations"] = target_locations
        if tags is not None:
            input_["tags"] = tags
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration
        if target_locations_url is not None:
            input_["target_locations_url"] = target_locations_url

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_change_request_execution(
        self,
        document_name: "capo_ssm.types.document_arn.DocumentARN",
        runbooks: "capo_ssm.types.runbooks.Runbooks",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        scheduled_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        parameters: Optional[
            "capo_ssm.types.automation_parameter_map.AutomationParameterMap"
        ] = None,
        change_request_name: Optional[
            "capo_ssm.types.change_request_name.ChangeRequestName"
        ] = None,
        client_token: Optional[
            "capo_ssm.types.idempotency_token.IdempotencyToken"
        ] = None,
        auto_approve: Optional["capo_ssm.types.boolean.Boolean"] = None,
        tags: Optional["capo_ssm.types.tag_list.TagList"] = None,
        scheduled_end_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        change_details: Optional[
            "capo_ssm.types.change_details_value.ChangeDetailsValue"
        ] = None,
    ) -> "capo_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult":
        """<important> <p>Amazon Web Services Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html">Amazon Web Services Systems Manager Change Manager availability change</a>.</p> </important> <p>Creates a change request for Change Manager. The Automation runbooks specified in the change request run only after all required approvals for the change request have been received.</p>

        Args:
            scheduled_time: <p>The date and time specified in the change request to run the Automation runbooks.</p> <note> <p>The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.</p> </note>
            document_name: <p>The name of the change template document to run during the runbook workflow.</p>
            document_version: <p>The version of the change template document to run during the runbook workflow.</p>
            parameters: <p>A key-value map of parameters that match the declared parameters in the change template document.</p>
            change_request_name: <p>The name of the change request associated with the runbook workflow to be run.</p>
            client_token: <p>The user-provided idempotency token. The token must be unique, is case insensitive, enforces the UUID format, and can't be reused.</p>
            auto_approve: <p>Indicates whether the change request can be approved automatically without the need for manual approvals.</p> <p>If <code>AutoApprovable</code> is enabled in a change template, then setting <code>AutoApprove</code> to <code>true</code> in <code>StartChangeRequestExecution</code> creates a change request that bypasses approver review.</p> <note> <p>Change Calendar restrictions are not bypassed in this scenario. If the state of an associated calendar is <code>CLOSED</code>, change freeze approvers must still grant permission for this change request to run. If they don't, the change won't be processed until the calendar state is again <code>OPEN</code>. </p> </note>
            runbooks: <p>Information about the Automation runbooks that are run during the runbook workflow.</p> <note> <p>The Automation runbooks specified for the runbook workflow can't run until all required approvals for the change request have been received.</p> </note>
            tags: <p>Optional metadata that you assign to a resource. You can specify a maximum of five tags for a change request. Tags enable you to categorize a resource in different ways, such as by purpose, owner, or environment. For example, you might want to tag a change request to identify an environment or target Amazon Web Services Region. In this case, you could specify the following key-value pairs:</p> <ul> <li> <p> <code>Key=Environment,Value=Production</code> </p> </li> <li> <p> <code>Key=Region,Value=us-east-2</code> </p> </li> </ul> <note> <p>The <code>Array Members</code> maximum value is reported as 1000. This number includes capacity reserved for internal operations. When calling the <code>StartChangeRequestExecution</code> action, you can specify a maximum of 5 tags. You can, however, use the <a>AddTagsToResource</a> action to add up to a total of 50 tags to an existing change request configuration.</p> </note>
            scheduled_end_time: <p>The time that the requester expects the runbook workflow related to the change request to complete. The time is an estimate only that the requester provides for reviewers.</p>
            change_details: <p>User-provided details about the change. If no details are provided, content specified in the <b>Template information</b> section of the associated change template is added.</p>

        Raises:
            capo_ssm.errors.automation_definition_not_approved_exception.AutomationDefinitionNotApprovedException: <p>Indicates that the Change Manager change template used in the change request was rejected or is still in a pending state.</p>
            capo_ssm.errors.automation_definition_not_found_exception.AutomationDefinitionNotFoundException: <p>An Automation runbook with the specified name couldn't be found.</p>
            capo_ssm.errors.automation_definition_version_not_found_exception.AutomationDefinitionVersionNotFoundException: <p>An Automation runbook with the specified name and version couldn't be found.</p>
            capo_ssm.errors.automation_execution_limit_exceeded_exception.AutomationExecutionLimitExceededException: <p>The number of simultaneously running Automation executions exceeded the allowable limit.</p>
            capo_ssm.errors.idempotent_parameter_mismatch.IdempotentParameterMismatch: <p>Error returned when an idempotent operation is retried and the parameters don't match the original call to the API with the same idempotency token. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_automation_execution_parameters_exception.InvalidAutomationExecutionParametersException: <p>The supplied parameters for invoking the specified Automation runbook are incorrect. For example, they may not match the set of parameters permitted for the specified Automation document.</p>
            capo_ssm.errors.no_longer_supported_exception.NoLongerSupportedException: <p>The requested operation is no longer supported by Systems Manager.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.start_change_request_execution_request.StartChangeRequestExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.start_change_request_execution_result.StartChangeRequestExecutionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.start_change_request_execution

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.start_change_request_execution.async_start_change_request_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.start_change_request_execution_request.StartChangeRequestExecutionRequest = {
            "document_name": document_name,
            "runbooks": runbooks,
        }
        if scheduled_time is not None:
            input_["scheduled_time"] = scheduled_time
        if document_version is not None:
            input_["document_version"] = document_version
        if parameters is not None:
            input_["parameters"] = parameters
        if change_request_name is not None:
            input_["change_request_name"] = change_request_name
        if client_token is not None:
            input_["client_token"] = client_token
        if auto_approve is not None:
            input_["auto_approve"] = auto_approve
        if tags is not None:
            input_["tags"] = tags
        if scheduled_end_time is not None:
            input_["scheduled_end_time"] = scheduled_end_time
        if change_details is not None:
            input_["change_details"] = change_details

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_execution_preview(
        self,
        document_name: "capo_ssm.types.document_name.DocumentName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        execution_inputs: Optional[
            "capo_ssm.types.execution_inputs.ExecutionInputs"
        ] = None,
    ) -> (
        "capo_ssm.types.start_execution_preview_response.StartExecutionPreviewResponse"
    ):
        """<p>Initiates the process of creating a preview showing the effects that running a specified Automation runbook would have on the targeted resources.</p>

        Args:
            document_name: <p>The name of the Automation runbook to run. The result of the execution preview indicates what the impact would be of running this runbook.</p>
            document_version: <p>The version of the Automation runbook to run. The default value is <code>$DEFAULT</code>.</p>
            execution_inputs: <p>Information about the inputs that can be specified for the preview operation. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.validation_exception.ValidationException: <p>The request isn't valid. Verify that you entered valid contents for the command and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            StartExecutionPreview
            This example illustrates one usage of StartExecutionPreview

            >>> await client.start_execution_preview(document_name='AWS-StartEC2Instance')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.start_execution_preview_request.StartExecutionPreviewRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.start_execution_preview_response.StartExecutionPreviewResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.start_execution_preview

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.start_execution_preview.async_start_execution_preview(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.start_execution_preview_request.StartExecutionPreviewRequest = {
            "document_name": document_name
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if execution_inputs is not None:
            input_["execution_inputs"] = execution_inputs

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_session(
        self,
        target: "capo_ssm.types.session_target.SessionTarget",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_name: Optional["capo_ssm.types.document_arn.DocumentARN"] = None,
        reason: Optional["capo_ssm.types.session_reason.SessionReason"] = None,
        parameters: Optional[
            "capo_ssm.types.session_manager_parameters.SessionManagerParameters"
        ] = None,
    ) -> "capo_ssm.types.start_session_response.StartSessionResponse":
        """<p>Initiates a connection to a target (for example, a managed node) for a Session Manager session. Returns a URL and token that can be used to open a WebSocket connection for sending input and receiving outputs.</p> <note> <p>Amazon Web Services CLI usage: <code>start-session</code> is an interactive command that requires the Session Manager plugin to be installed on the client machine making the call. For information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-install-plugin.html">Install the Session Manager plugin for the Amazon Web Services CLI</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>Amazon Web Services Tools for PowerShell usage: Start-SSMSession isn't currently supported by Amazon Web Services Tools for PowerShell on Windows local machines.</p> </note>

        Args:
            target: <p>The managed node to connect to for the session.</p>
            document_name: <p>The name of the SSM document you want to use to define the type of session, input parameters, or preferences for the session. For example, <code>SSM-SessionManagerRunShell</code>. You can call the <a>GetDocument</a> API to verify the document exists before attempting to start a session. If no document name is provided, a shell to the managed node is launched by default. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html">Start a session</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            reason: <p>The reason for connecting to the instance. This value is included in the details for the Amazon CloudWatch Events event created when you start the session.</p>
            parameters: <p>The values you want to specify for the parameters defined in the Session document. For more information about these parameters, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-create-preferences-cli.html">Create a Session Manager preferences document</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.target_not_connected.TargetNotConnected: <p>The specified target managed node for the session isn't fully configured for use with Session Manager. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started.html">Setting up Session Manager</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. This error is also returned if you attempt to start a session on a managed node that is located in a different account or Region</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.start_session_request.StartSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.start_session_response.StartSessionResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.start_session

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.start_session.async_start_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.start_session_request.StartSessionRequest = {
            "target": target
        }
        if document_name is not None:
            input_["document_name"] = document_name
        if reason is not None:
            input_["reason"] = reason
        if parameters is not None:
            input_["parameters"] = parameters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_automation_execution(
        self,
        automation_execution_id: "capo_ssm.types.automation_execution_id.AutomationExecutionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        type: Optional["capo_ssm.types.stop_type.StopType"] = None,
    ) -> (
        "capo_ssm.types.stop_automation_execution_result.StopAutomationExecutionResult"
    ):
        """<p>Stop an Automation that is currently running.</p>

        Args:
            automation_execution_id: <p>The execution ID of the Automation to stop.</p>
            type: <p>The stop request type. Valid types include the following: Cancel and Complete. The default type is Cancel.</p>

        Raises:
            capo_ssm.errors.automation_execution_not_found_exception.AutomationExecutionNotFoundException: <p>There is no automation execution information for the requested automation execution ID.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_automation_status_update_exception.InvalidAutomationStatusUpdateException: <p>The specified update status operation isn't valid.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.stop_automation_execution_request.StopAutomationExecutionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.stop_automation_execution_result.StopAutomationExecutionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.stop_automation_execution

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.stop_automation_execution.async_stop_automation_execution(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.stop_automation_execution_request.StopAutomationExecutionRequest = {
            "automation_execution_id": automation_execution_id
        }
        if type is not None:
            input_["type"] = type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def terminate_session(
        self,
        session_id: "capo_ssm.types.session_id.SessionId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.terminate_session_response.TerminateSessionResponse":
        """<p>Permanently ends a session and closes the data connection between the Session Manager client and SSM Agent on the managed node. A terminated session can't be resumed.</p>

        Args:
            session_id: <p>The ID of the session to terminate.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.terminate_session_request.TerminateSessionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.terminate_session_response.TerminateSessionResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.terminate_session

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.terminate_session.async_terminate_session(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.terminate_session_request.TerminateSessionRequest = {
            "session_id": session_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def unlabel_parameter_version(
        self,
        name: "capo_ssm.types.ps_parameter_name.PSParameterName",
        parameter_version: "capo_ssm.types.ps_parameter_version.PSParameterVersion",
        labels: "capo_ssm.types.parameter_label_list.ParameterLabelList",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> (
        "capo_ssm.types.unlabel_parameter_version_result.UnlabelParameterVersionResult"
    ):
        """<p>Remove a label or labels from a parameter.</p> <p>Parameter names can't contain spaces. The service removes any spaces specified for the beginning or end of a parameter name. If the specified name for a parameter contains spaces between characters, the request fails with a <code>ValidationException</code> error.</p>

        Args:
            name: <p>The name of the parameter from which you want to delete one or more labels.</p> <note> <p>You can't enter the Amazon Resource Name (ARN) for a parameter, only the parameter name itself.</p> </note>
            parameter_version: <p>The specific version of the parameter which you want to delete one or more labels from. If it isn't present, the call will fail.</p>
            labels: <p>One or more labels to delete from the specified parameter version.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.parameter_not_found.ParameterNotFound: <p>The parameter couldn't be found. Verify the name and try again.</p> <note> <p>For the <code>DeleteParameter</code> and <code>GetParameter</code> actions, if the specified parameter doesn't exist, the <code>ParameterNotFound</code> exception is <i>not</i> recorded in CloudTrail event logs.</p> </note>
            capo_ssm.errors.parameter_version_not_found.ParameterVersionNotFound: <p>The specified parameter version wasn't found. Verify the parameter name and version, and try again.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.unlabel_parameter_version_request.UnlabelParameterVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.unlabel_parameter_version_result.UnlabelParameterVersionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.unlabel_parameter_version

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.unlabel_parameter_version.async_unlabel_parameter_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.unlabel_parameter_version_request.UnlabelParameterVersionRequest = {
            "name": name,
            "parameter_version": parameter_version,
            "labels": labels,
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
        association_id: "capo_ssm.types.association_id.AssociationId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        parameters: Optional["capo_ssm.types.parameters.Parameters"] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        schedule_expression: Optional[
            "capo_ssm.types.schedule_expression.ScheduleExpression"
        ] = None,
        output_location: Optional[
            "capo_ssm.types.instance_association_output_location.InstanceAssociationOutputLocation"
        ] = None,
        name: Optional["capo_ssm.types.document_arn.DocumentARN"] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        association_name: Optional[
            "capo_ssm.types.association_name.AssociationName"
        ] = None,
        association_version: Optional[
            "capo_ssm.types.association_version.AssociationVersion"
        ] = None,
        automation_target_parameter_name: Optional[
            "capo_ssm.types.automation_target_parameter_name.AutomationTargetParameterName"
        ] = None,
        max_errors: Optional["capo_ssm.types.max_errors.MaxErrors"] = None,
        max_concurrency: Optional[
            "capo_ssm.types.max_concurrency.MaxConcurrency"
        ] = None,
        compliance_severity: Optional[
            "capo_ssm.types.association_compliance_severity.AssociationComplianceSeverity"
        ] = None,
        sync_compliance: Optional[
            "capo_ssm.types.association_sync_compliance.AssociationSyncCompliance"
        ] = None,
        apply_only_at_cron_interval: Optional[
            "capo_ssm.types.apply_only_at_cron_interval.ApplyOnlyAtCronInterval"
        ] = None,
        calendar_names: Optional[
            "capo_ssm.types.calendar_name_or_arn_list.CalendarNameOrARNList"
        ] = None,
        target_locations: Optional[
            "capo_ssm.types.target_locations.TargetLocations"
        ] = None,
        schedule_offset: Optional[
            "capo_ssm.types.schedule_offset.ScheduleOffset"
        ] = None,
        duration: Optional["capo_ssm.types.duration.Duration"] = None,
        target_maps: Optional["capo_ssm.types.target_maps.TargetMaps"] = None,
        alarm_configuration: Optional[
            "capo_ssm.types.alarm_configuration.AlarmConfiguration"
        ] = None,
        association_dispatch_assume_role: Optional[
            "capo_ssm.types.association_dispatch_assume_role_arn.AssociationDispatchAssumeRoleArn"
        ] = None,
    ) -> "capo_ssm.types.update_association_result.UpdateAssociationResult":
        """<p>Updates an association. You can update the association name and version, the document version, schedule, parameters, and Amazon Simple Storage Service (Amazon S3) output. When you call <code>UpdateAssociation</code>, the system removes all optional parameters from the request and overwrites the association with null values for those parameters. This is by design. You must specify all optional parameters in the call, even if you are not changing the parameters. This includes the <code>Name</code> parameter. Before calling this API action, we recommend that you call the <a>DescribeAssociation</a> API operation and make a note of all optional parameters required for your <code>UpdateAssociation</code> call.</p> <p>In order to call this API operation, a user, group, or role must be granted permission to call the <a>DescribeAssociation</a> API operation. If you don't have permission to call <code>DescribeAssociation</code>, then you receive the following error: <code>An error occurred (AccessDeniedException) when calling the UpdateAssociation operation: User: <user_arn> isn't authorized to perform: ssm:DescribeAssociation on resource: <resource_arn></code> </p> <important> <p>When you update an association, the association immediately runs against the specified targets. You can add the <code>ApplyOnlyAtCronInterval</code> parameter to run the association during the next schedule run.</p> </important>

        Args:
            association_id: <p>The ID of the association you want to update. </p>
            parameters: <p>The parameters you want to update for the association. If you create a parameter using Parameter Store, a tool in Amazon Web Services Systems Manager, you can reference the parameter using <code>{{ssm:parameter-name}}</code>.</p>
            document_version: <p>The document version you want update for the association. </p> <important> <p>State Manager doesn't support running associations that use a new version of a document if that document is shared from another account. State Manager always runs the <code>default</code> version of a document if shared from another account, even though the Systems Manager console shows that a new version was processed. If you want to run an association using a new version of a document shared form another account, you must set the document version to <code>default</code>.</p> </important>
            schedule_expression: <p>The cron expression used to schedule the association that you want to update.</p>
            output_location: <p>An S3 bucket where you want to store the results of this request.</p>
            name: <p>The name of the SSM Command document or Automation runbook that contains the configuration information for the managed node.</p> <p>You can specify Amazon Web Services-predefined documents, documents you created, or a document that is shared with you from another account.</p> <p>For Systems Manager document (SSM document) that are shared with you from other Amazon Web Services accounts, you must specify the complete SSM document ARN, in the following format:</p> <p> <code>arn:aws:ssm:<i>region</i>:<i>account-id</i>:document/<i>document-name</i> </code> </p> <p>For example:</p> <p> <code>arn:aws:ssm:us-east-2:12345678912:document/My-Shared-Document</code> </p> <p>For Amazon Web Services-predefined documents and SSM documents you created in your account, you only need to specify the document name. For example, <code>AWS-ApplyPatchBaseline</code> or <code>My-Document</code>.</p>
            targets: <p>The targets of the association.</p>
            association_name: <p>The name of the association that you want to update.</p>
            association_version: <p>This parameter is provided for concurrency control purposes. You must specify the latest association version in the service. If you want to ensure that this request succeeds, either specify <code>$LATEST</code>, or omit this parameter.</p>
            automation_target_parameter_name: <p>Choose the parameter that will define how your automation will branch out. This target is required for associations that use an Automation runbook and target resources by using rate controls. Automation is a tool in Amazon Web Services Systems Manager.</p>
            max_errors: <p>The number of errors that are allowed before the system stops sending requests to run the association on additional targets. You can specify either an absolute number of errors, for example 10, or a percentage of the target set, for example 10%. If you specify 3, for example, the system stops sending requests when the fourth error is received. If you specify 0, then the system stops sending requests after the first error is returned. If you run an association on 50 managed nodes and set <code>MaxError</code> to 10%, then the system stops sending the request when the sixth error is received.</p> <p>Executions that are already running an association when <code>MaxErrors</code> is reached are allowed to complete, but some of these executions may fail as well. If you need to ensure that there won't be more than max-errors failed executions, set <code>MaxConcurrency</code> to 1 so that executions proceed one at a time.</p>
            max_concurrency: <p>The maximum number of targets allowed to run the association at the same time. You can specify a number, for example 10, or a percentage of the target set, for example 10%. The default value is 100%, which means all targets run the association at the same time.</p> <p>If a new managed node starts and attempts to run an association while Systems Manager is running <code>MaxConcurrency</code> associations, the association is allowed to run. During the next association interval, the new managed node will process its association within the limit specified for <code>MaxConcurrency</code>.</p>
            compliance_severity: <p>The severity level to assign to the association.</p>
            sync_compliance: <p>The mode for generating association compliance. You can specify <code>AUTO</code> or <code>MANUAL</code>. In <code>AUTO</code> mode, the system uses the status of the association execution to determine the compliance status. If the association execution runs successfully, then the association is <code>COMPLIANT</code>. If the association execution doesn't run successfully, the association is <code>NON-COMPLIANT</code>.</p> <p>In <code>MANUAL</code> mode, you must specify the <code>AssociationId</code> as a parameter for the <a>PutComplianceItems</a> API operation. In this case, compliance data isn't managed by State Manager, a tool in Amazon Web Services Systems Manager. It is managed by your direct call to the <a>PutComplianceItems</a> API operation.</p> <p>By default, all associations use <code>AUTO</code> mode.</p>
            apply_only_at_cron_interval: <p>By default, when you update an association, the system runs it immediately after it is updated and then according to the schedule you specified. Specify <code>true</code> for <code>ApplyOnlyAtCronInterval</code> if you want the association to run only according to the schedule you specified.</p> <p>If you chose this option when you created an association and later you edit that association or you make changes to the Automation runbook or SSM document on which that association is based, State Manager applies the association at the next specified cron interval. For example, if you chose the <code>Latest</code> version of an SSM document when you created an association and you edit the association by choosing a different document version on the Documents page, State Manager applies the association at the next specified cron interval if you previously set <code>ApplyOnlyAtCronInterval</code> to <code>true</code>. If this option wasn't selected, State Manager immediately runs the association.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#state-manager-about-scheduling">Understanding when associations are applied to resources</a> and <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/state-manager-about.html#runbook-target-updates">About target updates with Automation runbooks</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>This parameter isn't supported for rate expressions.</p> <p>You can reset this parameter. To do so, specify the <code>no-apply-only-at-cron-interval</code> parameter when you update the association from the command line. This parameter forces the association to run immediately after updating it and according to the interval specified.</p>
            calendar_names: <p>The names or Amazon Resource Names (ARNs) of the Change Calendar type documents you want to gate your associations under. The associations only run when that change calendar is open. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-change-calendar">Amazon Web Services Systems Manager Change Calendar</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            target_locations: <p>A location is a combination of Amazon Web Services Regions and Amazon Web Services accounts where you want to run the association. Use this action to update an association in multiple Regions and multiple accounts.</p> <note> <p>The <code>TargetLocationAlarmConfiguration</code> parameter is not supported by State Manager.</p> </note>
            schedule_offset: <p>Number of days to wait after the scheduled day to run an association. For example, if you specified a cron schedule of <code>cron(0 0 ? * THU#2 *)</code>, you could specify an offset of 3 to run the association each Sunday after the second Thursday of the month. For more information about cron schedules for associations, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/reference-cron-and-rate-expressions.html">Reference: Cron and rate expressions for Systems Manager</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p> <note> <p>To use offsets, you must specify the <code>ApplyOnlyAtCronInterval</code> parameter. This option tells the system not to run an association immediately after you create it. </p> </note>
            duration: <p>The number of hours the association can run before it is canceled. Duration applies to associations that are currently running, and any pending and in progress commands on all targets. If a target was taken offline for the association to run, it is made available again immediately, without a reboot. </p> <p>The <code>Duration</code> parameter applies only when both these conditions are true:</p> <ul> <li> <p>The association for which you specify a duration is cancelable according to the parameters of the SSM command document or Automation runbook associated with this execution. </p> </li> <li> <p>The command specifies the <code> <a href="https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_UpdateAssociation.html#systemsmanager-UpdateAssociation-request-ApplyOnlyAtCronInterval">ApplyOnlyAtCronInterval</a> </code> parameter, which means that the association doesn't run immediately after it is updated, but only according to the specified schedule.</p> </li> </ul>
            target_maps: <p>A key-value mapping of document parameters to target resources. Both Targets and TargetMaps can't be specified together.</p>
            association_dispatch_assume_role: <p>A role used by association to take actions on your behalf. State Manager will assume this role and call required APIs when dispatching configurations to nodes. If not specified, <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/using-service-linked-roles.html"> service-linked role for Systems Manager</a> will be used by default. </p> <note> <p>It is recommended that you define a custom IAM role so that you have full control of the permissions that State Manager has when taking actions on your behalf.</p> <p>Service-linked role support in State Manager is being phased out. Associations relying on service-linked role may require updates in the future to continue functioning properly.</p> </note>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.association_version_limit_exceeded.AssociationVersionLimitExceeded: <p>You have reached the maximum number versions allowed for an association. Each association has a limit of 1,000 versions. </p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_association_version.InvalidAssociationVersion: <p>The version you specified isn't valid. Use ListAssociationVersions to view all versions of an association according to the association ID. Or, use the <code>$LATEST</code> parameter to view the latest version of the association.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_output_location.InvalidOutputLocation: <p>The output location isn't valid or doesn't exist.</p>
            capo_ssm.errors.invalid_parameters.InvalidParameters: <p>You must specify values for all required parameters in the Amazon Web Services Systems Manager document (SSM document). You can only supply values to parameters defined in the SSM document.</p>
            capo_ssm.errors.invalid_schedule.InvalidSchedule: <p>The schedule is invalid. Verify your cron or rate expression and try again.</p>
            capo_ssm.errors.invalid_target.InvalidTarget: <p>The target isn't valid or doesn't exist. It might not be configured for Systems Manager or you might not have permission to perform the operation.</p>
            capo_ssm.errors.invalid_target_maps.InvalidTargetMaps: <p>TargetMap parameter isn't valid.</p>
            capo_ssm.errors.invalid_update.InvalidUpdate: <p>The update isn't valid.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_association_request.UpdateAssociationRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_association_result.UpdateAssociationResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_association

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_association.async_update_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_association_request.UpdateAssociationRequest = {
            "association_id": association_id
        }
        if parameters is not None:
            input_["parameters"] = parameters
        if document_version is not None:
            input_["document_version"] = document_version
        if schedule_expression is not None:
            input_["schedule_expression"] = schedule_expression
        if output_location is not None:
            input_["output_location"] = output_location
        if name is not None:
            input_["name"] = name
        if targets is not None:
            input_["targets"] = targets
        if association_name is not None:
            input_["association_name"] = association_name
        if association_version is not None:
            input_["association_version"] = association_version
        if automation_target_parameter_name is not None:
            input_["automation_target_parameter_name"] = (
                automation_target_parameter_name
            )
        if max_errors is not None:
            input_["max_errors"] = max_errors
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if compliance_severity is not None:
            input_["compliance_severity"] = compliance_severity
        if sync_compliance is not None:
            input_["sync_compliance"] = sync_compliance
        if apply_only_at_cron_interval is not None:
            input_["apply_only_at_cron_interval"] = apply_only_at_cron_interval
        if calendar_names is not None:
            input_["calendar_names"] = calendar_names
        if target_locations is not None:
            input_["target_locations"] = target_locations
        if schedule_offset is not None:
            input_["schedule_offset"] = schedule_offset
        if duration is not None:
            input_["duration"] = duration
        if target_maps is not None:
            input_["target_maps"] = target_maps
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration
        if association_dispatch_assume_role is not None:
            input_["association_dispatch_assume_role"] = (
                association_dispatch_assume_role
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_association_status(
        self,
        name: "capo_ssm.types.document_arn.DocumentARN",
        instance_id: "capo_ssm.types.instance_id.InstanceId",
        association_status: "capo_ssm.types.association_status.AssociationStatus",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> (
        "capo_ssm.types.update_association_status_result.UpdateAssociationStatusResult"
    ):
        """<p>Updates the status of the Amazon Web Services Systems Manager document (SSM document) associated with the specified managed node.</p> <p> <code>UpdateAssociationStatus</code> is primarily used by the Amazon Web Services Systems Manager Agent (SSM Agent) to report status updates about your associations and is only used for associations created with the <code>InstanceId</code> legacy parameter.</p>

        Args:
            name: <p>The name of the SSM document.</p>
            instance_id: <p>The managed node ID.</p>
            association_status: <p>The association status.</p>

        Raises:
            capo_ssm.errors.association_does_not_exist.AssociationDoesNotExist: <p>The specified association doesn't exist.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.status_unchanged.StatusUnchanged: <p>The updated status is the same as the current status.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_association_status_request.UpdateAssociationStatusRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_association_status_result.UpdateAssociationStatusResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_association_status

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_association_status.async_update_association_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_association_status_request.UpdateAssociationStatusRequest = {
            "name": name,
            "instance_id": instance_id,
            "association_status": association_status,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_cloud_connector(
        self,
        cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        display_name: Optional["capo_ssm.types.display_name.DisplayName"] = None,
        configuration: Optional[
            "capo_ssm.types.cloud_connector_configuration.CloudConnectorConfiguration"
        ] = None,
        description: Optional[
            "capo_ssm.types.cloud_connector_description.CloudConnectorDescription"
        ] = None,
    ) -> "capo_ssm.types.update_cloud_connector_result.UpdateCloudConnectorResult":
        """<p>Updates an existing cloud connector with new configuration details.</p>

        Args:
            cloud_connector_id: <p>The ID of the cloud connector to update.</p>
            display_name: <p>A new friendly name for the cloud connector.</p>
            configuration: <p>The updated configuration details for connecting to the third-party cloud environment.</p>
            description: <p>A new description for the cloud connector.</p>

        Raises:
            capo_ssm.errors.conflict_exception.ConflictException: <p>An error occurred because of a conflict with a concurrent request or the current state of the resource. Retry your request.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_cloud_connector_request.UpdateCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_cloud_connector_result.UpdateCloudConnectorResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_cloud_connector

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_cloud_connector.async_update_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_cloud_connector_request.UpdateCloudConnectorRequest = {
            "cloud_connector_id": cloud_connector_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
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

    async def update_document(
        self,
        content: "capo_ssm.types.document_content.DocumentContent",
        name: "capo_ssm.types.document_name.DocumentName",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        attachments: Optional[
            "capo_ssm.types.attachments_source_list.AttachmentsSourceList"
        ] = None,
        display_name: Optional[
            "capo_ssm.types.document_display_name.DocumentDisplayName"
        ] = None,
        version_name: Optional[
            "capo_ssm.types.document_version_name.DocumentVersionName"
        ] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
        document_format: Optional[
            "capo_ssm.types.document_format.DocumentFormat"
        ] = None,
        target_type: Optional["capo_ssm.types.target_type.TargetType"] = None,
    ) -> "capo_ssm.types.update_document_result.UpdateDocumentResult":
        """<p>Updates one or more values for an SSM document.</p>

        Args:
            content: <p>A valid JSON or YAML string.</p>
            attachments: <p>A list of key-value pairs that describe attachments to a version of a document.</p>
            name: <p>The name of the SSM document that you want to update.</p>
            display_name: <p>The friendly name of the SSM document that you want to update. This value can differ for each version of the document. If you don't specify a value for this parameter in your request, the existing value is applied to the new document version.</p>
            version_name: <p>An optional field specifying the version of the artifact you are updating with the document. For example, 12.6. This value is unique across all versions of a document, and can't be changed.</p>
            document_version: <p>The version of the document that you want to update. Currently, Systems Manager supports updating only the latest version of the document. You can specify the version number of the latest version or use the <code>$LATEST</code> variable.</p> <note> <p>If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the <code>apply-only-at-cron-interval</code> parameter.</p> </note>
            document_format: <p>Specify the document format for the new document version. The document format can be JSON, YAML, or TEXT. JSON is the default format.</p>
            target_type: <p>Specify a new target type for the document.</p>

        Raises:
            capo_ssm.errors.document_version_limit_exceeded.DocumentVersionLimitExceeded: <p>The document has too many versions. Delete one or more document versions and try again.</p>
            capo_ssm.errors.duplicate_document_content.DuplicateDocumentContent: <p>The content of the association document matches another document. Change the content of the document and try again.</p>
            capo_ssm.errors.duplicate_document_version_name.DuplicateDocumentVersionName: <p>The version name has already been used in this document. Specify a different version name, and then try again.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_content.InvalidDocumentContent: <p>The content for the document isn't valid.</p>
            capo_ssm.errors.invalid_document_operation.InvalidDocumentOperation: <p>You attempted to delete a document while it is still shared. You must stop sharing the document before you can delete it.</p>
            capo_ssm.errors.invalid_document_schema_version.InvalidDocumentSchemaVersion: <p>The version of the document schema isn't supported.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.max_document_size_exceeded.MaxDocumentSizeExceeded: <p>The size limit of a document is 64 KB.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_document_request.UpdateDocumentRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_document_result.UpdateDocumentResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_document

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_document.async_update_document(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_document_request.UpdateDocumentRequest = {
            "content": content,
            "name": name,
        }
        if attachments is not None:
            input_["attachments"] = attachments
        if display_name is not None:
            input_["display_name"] = display_name
        if version_name is not None:
            input_["version_name"] = version_name
        if document_version is not None:
            input_["document_version"] = document_version
        if document_format is not None:
            input_["document_format"] = document_format
        if target_type is not None:
            input_["target_type"] = target_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_document_default_version(
        self,
        name: "capo_ssm.types.document_name.DocumentName",
        document_version: "capo_ssm.types.document_version_number.DocumentVersionNumber",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.update_document_default_version_result.UpdateDocumentDefaultVersionResult":
        """<p>Set the default version of a document. </p> <note> <p>If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the <code>apply-only-at-cron-interval</code> parameter.</p> </note>

        Args:
            name: <p>The name of a custom document that you want to set as the default version.</p>
            document_version: <p>The version of a custom document that you want to set as the default version.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_schema_version.InvalidDocumentSchemaVersion: <p>The version of the document schema isn't supported.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_document_default_version_request.UpdateDocumentDefaultVersionRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_document_default_version_result.UpdateDocumentDefaultVersionResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_document_default_version

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_document_default_version.async_update_document_default_version(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_document_default_version_request.UpdateDocumentDefaultVersionRequest = {
            "name": name,
            "document_version": document_version,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_document_metadata(
        self,
        name: "capo_ssm.types.document_name.DocumentName",
        document_reviews: "capo_ssm.types.document_reviews.DocumentReviews",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        document_version: Optional[
            "capo_ssm.types.document_version.DocumentVersion"
        ] = None,
    ) -> "capo_ssm.types.update_document_metadata_response.UpdateDocumentMetadataResponse":
        """<important> <p>Amazon Web Services Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html">Amazon Web Services Systems Manager Change Manager availability change</a>.</p> </important> <p>Updates information related to approval reviews for a specific version of a change template in Change Manager.</p>

        Args:
            name: <p>The name of the change template for which a version's metadata is to be updated.</p>
            document_version: <p>The version of a change template in which to update approval metadata.</p>
            document_reviews: <p>The change template review details to update.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_document.InvalidDocument: <p>The specified SSM document doesn't exist.</p>
            capo_ssm.errors.invalid_document_operation.InvalidDocumentOperation: <p>You attempted to delete a document while it is still shared. You must stop sharing the document before you can delete it.</p>
            capo_ssm.errors.invalid_document_version.InvalidDocumentVersion: <p>The document version isn't valid or doesn't exist.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_document_metadata_request.UpdateDocumentMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_document_metadata_response.UpdateDocumentMetadataResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.update_document_metadata

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_document_metadata.async_update_document_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_document_metadata_request.UpdateDocumentMetadataRequest = {
            "name": name,
            "document_reviews": document_reviews,
        }
        if document_version is not None:
            input_["document_version"] = document_version

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_maintenance_window(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        name: Optional[
            "capo_ssm.types.maintenance_window_name.MaintenanceWindowName"
        ] = None,
        description: Optional[
            "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
        ] = None,
        start_date: Optional[
            "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
        ] = None,
        end_date: Optional[
            "capo_ssm.types.maintenance_window_string_date_time.MaintenanceWindowStringDateTime"
        ] = None,
        schedule: Optional[
            "capo_ssm.types.maintenance_window_schedule.MaintenanceWindowSchedule"
        ] = None,
        schedule_timezone: Optional[
            "capo_ssm.types.maintenance_window_timezone.MaintenanceWindowTimezone"
        ] = None,
        schedule_offset: Optional[
            "capo_ssm.types.maintenance_window_offset.MaintenanceWindowOffset"
        ] = None,
        duration: Optional[
            "capo_ssm.types.maintenance_window_duration_hours.MaintenanceWindowDurationHours"
        ] = None,
        cutoff: Optional[
            "capo_ssm.types.maintenance_window_cutoff.MaintenanceWindowCutoff"
        ] = None,
        allow_unassociated_targets: Optional[
            "capo_ssm.types.maintenance_window_allow_unassociated_targets.MaintenanceWindowAllowUnassociatedTargets"
        ] = None,
        enabled: Optional[
            "capo_ssm.types.maintenance_window_enabled.MaintenanceWindowEnabled"
        ] = None,
        replace: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> (
        "capo_ssm.types.update_maintenance_window_result.UpdateMaintenanceWindowResult"
    ):
        """<p>Updates an existing maintenance window. Only specified parameters are modified.</p> <note> <p>The value you specify for <code>Duration</code> determines the specific end time for the maintenance window based on the time it begins. No maintenance window tasks are permitted to start after the resulting endtime minus the number of hours you specify for <code>Cutoff</code>. For example, if the maintenance window starts at 3 PM, the duration is three hours, and the value you specify for <code>Cutoff</code> is one hour, no maintenance window tasks can start after 5 PM.</p> </note>

        Args:
            window_id: <p>The ID of the maintenance window to update.</p>
            name: <p>The name of the maintenance window.</p>
            description: <p>An optional description for the update request.</p>
            start_date: <p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become active. <code>StartDate</code> allows you to delay activation of the maintenance window until the specified future date.</p> <note> <p>When using a rate schedule, if you provide a start date that occurs in the past, the current date and time are used as the start date. </p> </note>
            end_date: <p>The date and time, in ISO-8601 Extended format, for when you want the maintenance window to become inactive. <code>EndDate</code> allows you to set a date and time in the future when the maintenance window will no longer run.</p>
            schedule: <p>The schedule of the maintenance window in the form of a cron or rate expression.</p>
            schedule_timezone: <p>The time zone that the scheduled maintenance window executions are based on, in Internet Assigned Numbers Authority (IANA) format. For example: "America/Los_Angeles", "UTC", or "Asia/Seoul". For more information, see the <a href="https://www.iana.org/time-zones">Time Zone Database</a> on the IANA website.</p>
            schedule_offset: <p>The number of days to wait after the date and time specified by a cron expression before running the maintenance window.</p> <p>For example, the following cron expression schedules a maintenance window to run the third Tuesday of every month at 11:30 PM.</p> <p> <code>cron(30 23 ? * TUE#3 *)</code> </p> <p>If the schedule offset is <code>2</code>, the maintenance window won't run until two days later.</p>
            duration: <p>The duration of the maintenance window in hours.</p>
            cutoff: <p>The number of hours before the end of the maintenance window that Amazon Web Services Systems Manager stops scheduling new tasks for execution.</p>
            allow_unassociated_targets: <p>Whether targets must be registered with the maintenance window before tasks can be defined for those targets.</p>
            enabled: <p>Whether the maintenance window is enabled.</p>
            replace: <p>If <code>True</code>, then all fields that are required by the <a>CreateMaintenanceWindow</a> operation are also required for this API request. Optional fields that aren't specified are set to null. </p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_maintenance_window_request.UpdateMaintenanceWindowRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_maintenance_window_result.UpdateMaintenanceWindowResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_maintenance_window

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_maintenance_window.async_update_maintenance_window(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_maintenance_window_request.UpdateMaintenanceWindowRequest = {
            "window_id": window_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if start_date is not None:
            input_["start_date"] = start_date
        if end_date is not None:
            input_["end_date"] = end_date
        if schedule is not None:
            input_["schedule"] = schedule
        if schedule_timezone is not None:
            input_["schedule_timezone"] = schedule_timezone
        if schedule_offset is not None:
            input_["schedule_offset"] = schedule_offset
        if duration is not None:
            input_["duration"] = duration
        if cutoff is not None:
            input_["cutoff"] = cutoff
        if allow_unassociated_targets is not None:
            input_["allow_unassociated_targets"] = allow_unassociated_targets
        if enabled is not None:
            input_["enabled"] = enabled
        if replace is not None:
            input_["replace"] = replace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_maintenance_window_target(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        window_target_id: "capo_ssm.types.maintenance_window_target_id.MaintenanceWindowTargetId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        owner_information: Optional[
            "capo_ssm.types.owner_information.OwnerInformation"
        ] = None,
        name: Optional[
            "capo_ssm.types.maintenance_window_name.MaintenanceWindowName"
        ] = None,
        description: Optional[
            "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
        ] = None,
        replace: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.update_maintenance_window_target_result.UpdateMaintenanceWindowTargetResult":
        """<p>Modifies the target of an existing maintenance window. You can change the following:</p> <ul> <li> <p>Name</p> </li> <li> <p>Description</p> </li> <li> <p>Owner</p> </li> <li> <p>IDs for an ID target</p> </li> <li> <p>Tags for a Tag target</p> </li> <li> <p>From any supported tag type to another. The three supported tag types are ID target, Tag target, and resource group. For more information, see <a>Target</a>.</p> </li> </ul> <note> <p>If a parameter is null, then the corresponding field isn't modified.</p> </note>

        Args:
            window_id: <p>The maintenance window ID with which to modify the target.</p>
            window_target_id: <p>The target ID to modify.</p>
            targets: <p>The targets to add or replace.</p>
            owner_information: <p>User-provided value that will be included in any Amazon CloudWatch Events events raised while running tasks for these targets in this maintenance window.</p>
            name: <p>A name for the update.</p>
            description: <p>An optional description for the update.</p>
            replace: <p>If <code>True</code>, then all fields that are required by the <a>RegisterTargetWithMaintenanceWindow</a> operation are also required for this API request. Optional fields that aren't specified are set to null.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_maintenance_window_target_request.UpdateMaintenanceWindowTargetRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_maintenance_window_target_result.UpdateMaintenanceWindowTargetResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_maintenance_window_target

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_maintenance_window_target.async_update_maintenance_window_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_maintenance_window_target_request.UpdateMaintenanceWindowTargetRequest = {
            "window_id": window_id,
            "window_target_id": window_target_id,
        }
        if targets is not None:
            input_["targets"] = targets
        if owner_information is not None:
            input_["owner_information"] = owner_information
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if replace is not None:
            input_["replace"] = replace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_maintenance_window_task(
        self,
        window_id: "capo_ssm.types.maintenance_window_id.MaintenanceWindowId",
        window_task_id: "capo_ssm.types.maintenance_window_task_id.MaintenanceWindowTaskId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        targets: Optional["capo_ssm.types.targets.Targets"] = None,
        task_arn: Optional[
            "capo_ssm.types.maintenance_window_task_arn.MaintenanceWindowTaskArn"
        ] = None,
        service_role_arn: Optional["capo_ssm.types.service_role.ServiceRole"] = None,
        task_parameters: Optional[
            "capo_ssm.types.maintenance_window_task_parameters.MaintenanceWindowTaskParameters"
        ] = None,
        task_invocation_parameters: Optional[
            "capo_ssm.types.maintenance_window_task_invocation_parameters.MaintenanceWindowTaskInvocationParameters"
        ] = None,
        priority: Optional[
            "capo_ssm.types.maintenance_window_task_priority.MaintenanceWindowTaskPriority"
        ] = None,
        max_concurrency: Optional[
            "capo_ssm.types.max_concurrency.MaxConcurrency"
        ] = None,
        max_errors: Optional["capo_ssm.types.max_errors.MaxErrors"] = None,
        logging_info: Optional["capo_ssm.types.logging_info.LoggingInfo"] = None,
        name: Optional[
            "capo_ssm.types.maintenance_window_name.MaintenanceWindowName"
        ] = None,
        description: Optional[
            "capo_ssm.types.maintenance_window_description.MaintenanceWindowDescription"
        ] = None,
        replace: Optional["capo_ssm.types.boolean.Boolean"] = None,
        cutoff_behavior: Optional[
            "capo_ssm.types.maintenance_window_task_cutoff_behavior.MaintenanceWindowTaskCutoffBehavior"
        ] = None,
        alarm_configuration: Optional[
            "capo_ssm.types.alarm_configuration.AlarmConfiguration"
        ] = None,
    ) -> "capo_ssm.types.update_maintenance_window_task_result.UpdateMaintenanceWindowTaskResult":
        """<p>Modifies a task assigned to a maintenance window. You can't change the task type, but you can change the following values:</p> <ul> <li> <p> <code>TaskARN</code>. For example, you can change a <code>RUN_COMMAND</code> task from <code>AWS-RunPowerShellScript</code> to <code>AWS-RunShellScript</code>.</p> </li> <li> <p> <code>ServiceRoleArn</code> </p> </li> <li> <p> <code>TaskInvocationParameters</code> </p> </li> <li> <p> <code>Priority</code> </p> </li> <li> <p> <code>MaxConcurrency</code> </p> </li> <li> <p> <code>MaxErrors</code> </p> </li> </ul> <note> <p>One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that don't specify targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">Registering maintenance window tasks without targets</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </note> <p>If the value for a parameter in <code>UpdateMaintenanceWindowTask</code> is null, then the corresponding field isn't modified. If you set <code>Replace</code> to true, then all fields required by the <a>RegisterTaskWithMaintenanceWindow</a> operation are required for this request. Optional fields that aren't specified are set to null.</p> <important> <p>When you update a maintenance window task that has options specified in <code>TaskInvocationParameters</code>, you must provide again all the <code>TaskInvocationParameters</code> values that you want to retain. The values you don't specify again are removed. For example, suppose that when you registered a Run Command task, you specified <code>TaskInvocationParameters</code> values for <code>Comment</code>, <code>NotificationConfig</code>, and <code>OutputS3BucketName</code>. If you update the maintenance window task and specify only a different <code>OutputS3BucketName</code> value, the values for <code>Comment</code> and <code>NotificationConfig</code> are removed.</p> </important>

        Args:
            window_id: <p>The maintenance window ID that contains the task to modify.</p>
            window_task_id: <p>The task ID to modify.</p>
            targets: <p>The targets (either managed nodes or tags) to modify. Managed nodes are specified using the format <code>Key=instanceids,Values=instanceID_1,instanceID_2</code>. Tags are specified using the format <code> Key=tag_name,Values=tag_value</code>. </p> <note> <p>One or more targets must be specified for maintenance window Run Command-type tasks. Depending on the task, targets are optional for other maintenance window task types (Automation, Lambda, and Step Functions). For more information about running tasks that don't specify targets, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">Registering maintenance window tasks without targets</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> </note>
            task_arn: <p>The task ARN to modify.</p>
            service_role_arn: <p>The Amazon Resource Name (ARN) of the IAM service role for Amazon Web Services Systems Manager to assume when running a maintenance window task. If you do not specify a service role ARN, Systems Manager uses a service-linked role in your account. If no appropriate service-linked role for Systems Manager exists in your account, it is created when you run <code>RegisterTaskWithMaintenanceWindow</code>.</p> <p>However, for an improved security posture, we strongly recommend creating a custom policy and custom service role for running your maintenance window tasks. The policy can be crafted to provide only the permissions needed for your particular maintenance window tasks. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-maintenance-permissions.html">Setting up Maintenance Windows</a> in the in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            task_parameters: <p>The parameters to modify.</p> <note> <p> <code>TaskParameters</code> has been deprecated. To specify parameters to pass to a task when it runs, instead use the <code>Parameters</code> option in the <code>TaskInvocationParameters</code> structure. For information about how Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note> <p>The map has the following format:</p> <p>Key: string, between 1 and 255 characters</p> <p>Value: an array of strings, each string is between 1 and 255 characters</p>
            task_invocation_parameters: <p>The parameters that the task should use during execution. Populate only the fields that match the task type. All other fields should be empty.</p> <important> <p>When you update a maintenance window task that has options specified in <code>TaskInvocationParameters</code>, you must provide again all the <code>TaskInvocationParameters</code> values that you want to retain. The values you don't specify again are removed. For example, suppose that when you registered a Run Command task, you specified <code>TaskInvocationParameters</code> values for <code>Comment</code>, <code>NotificationConfig</code>, and <code>OutputS3BucketName</code>. If you update the maintenance window task and specify only a different <code>OutputS3BucketName</code> value, the values for <code>Comment</code> and <code>NotificationConfig</code> are removed.</p> </important>
            priority: <p>The new task priority to specify. The lower the number, the higher the priority. Tasks that have the same priority are scheduled in parallel.</p>
            max_concurrency: <p>The new <code>MaxConcurrency</code> value you want to specify. <code>MaxConcurrency</code> is the number of targets that are allowed to run this task, in parallel.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>
            max_errors: <p>The new <code>MaxErrors</code> value to specify. <code>MaxErrors</code> is the maximum number of errors that are allowed before the task stops being scheduled.</p> <note> <p>Although this element is listed as "Required: No", a value can be omitted only when you are registering or updating a <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows-targetless-tasks.html">targetless task</a> You must provide a value in all other cases.</p> <p>For maintenance window tasks without a target specified, you can't supply a value for this option. Instead, the system inserts a placeholder value of <code>1</code>. This value doesn't affect the running of your task.</p> </note>
            logging_info: <p>The new logging location in Amazon S3 to specify.</p> <note> <p> <code>LoggingInfo</code> has been deprecated. To specify an Amazon Simple Storage Service (Amazon S3) bucket to contain logs, instead use the <code>OutputS3BucketName</code> and <code>OutputS3KeyPrefix</code> options in the <code>TaskInvocationParameters</code> structure. For information about how Amazon Web Services Systems Manager handles these options for the supported maintenance window task types, see <a>MaintenanceWindowTaskInvocationParameters</a>.</p> </note>
            name: <p>The new task name to specify.</p>
            description: <p>The new task description to specify.</p>
            replace: <p>If True, then all fields that are required by the <a>RegisterTaskWithMaintenanceWindow</a> operation are also required for this API request. Optional fields that aren't specified are set to null.</p>
            cutoff_behavior: <p>Indicates whether tasks should continue to run after the cutoff time specified in the maintenance windows is reached. </p> <ul> <li> <p> <code>CONTINUE_TASK</code>: When the cutoff time is reached, any tasks that are running continue. The default value.</p> </li> <li> <p> <code>CANCEL_TASK</code>:</p> <ul> <li> <p>For Automation, Lambda, Step Functions tasks: When the cutoff time is reached, any task invocations that are already running continue, but no new task invocations are started.</p> </li> <li> <p>For Run Command tasks: When the cutoff time is reached, the system sends a <a>CancelCommand</a> operation that attempts to cancel the command associated with the task. However, there is no guarantee that the command will be terminated and the underlying process stopped.</p> </li> </ul> <p>The status for tasks that are not completed is <code>TIMED_OUT</code>.</p> </li> </ul>
            alarm_configuration: <p>The CloudWatch alarm you want to apply to your maintenance window task.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_maintenance_window_task_request.UpdateMaintenanceWindowTaskRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_maintenance_window_task_result.UpdateMaintenanceWindowTaskResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_maintenance_window_task

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_maintenance_window_task.async_update_maintenance_window_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_maintenance_window_task_request.UpdateMaintenanceWindowTaskRequest = {
            "window_id": window_id,
            "window_task_id": window_task_id,
        }
        if targets is not None:
            input_["targets"] = targets
        if task_arn is not None:
            input_["task_arn"] = task_arn
        if service_role_arn is not None:
            input_["service_role_arn"] = service_role_arn
        if task_parameters is not None:
            input_["task_parameters"] = task_parameters
        if task_invocation_parameters is not None:
            input_["task_invocation_parameters"] = task_invocation_parameters
        if priority is not None:
            input_["priority"] = priority
        if max_concurrency is not None:
            input_["max_concurrency"] = max_concurrency
        if max_errors is not None:
            input_["max_errors"] = max_errors
        if logging_info is not None:
            input_["logging_info"] = logging_info
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if replace is not None:
            input_["replace"] = replace
        if cutoff_behavior is not None:
            input_["cutoff_behavior"] = cutoff_behavior
        if alarm_configuration is not None:
            input_["alarm_configuration"] = alarm_configuration

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_managed_instance_role(
        self,
        instance_id: "capo_ssm.types.managed_instance_id.ManagedInstanceId",
        iam_role: "capo_ssm.types.iam_role.IamRole",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.update_managed_instance_role_result.UpdateManagedInstanceRoleResult":
        """<p>Changes the Identity and Access Management (IAM) role that is assigned to the on-premises server, edge device, or virtual machines (VM). IAM roles are first assigned to these hybrid nodes during the activation process. For more information, see <a>CreateActivation</a>.</p>

        Args:
            instance_id: <p>The ID of the managed node where you want to update the role.</p>
            iam_role: <p>The name of the Identity and Access Management (IAM) role that you want to assign to the managed node. This IAM role must provide AssumeRole permissions for the Amazon Web Services Systems Manager service principal <code>ssm.amazonaws.com</code>. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-service-role.html">Create the IAM service role required for Systems Manager in hybrid and multicloud environments</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <note> <p>You can't specify an IAM service-linked role for this parameter. You must create a unique role.</p> </note>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.invalid_instance_id.InvalidInstanceId: <p>The following problems can cause this exception:</p> <ul> <li> <p>You don't have permission to access the managed node.</p> </li> <li> <p>Amazon Web Services Systems Manager Agent (SSM Agent) isn't running. Verify that SSM Agent is running.</p> </li> <li> <p>SSM Agent isn't registered with the SSM endpoint. Try reinstalling SSM Agent.</p> </li> <li> <p>The managed node isn't in a valid state. Valid states are: <code>Running</code>, <code>Pending</code>, <code>Stopped</code>, and <code>Stopping</code>. Invalid states are: <code>Shutting-down</code> and <code>Terminated</code>.</p> </li> </ul>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_managed_instance_role_request.UpdateManagedInstanceRoleRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_managed_instance_role_result.UpdateManagedInstanceRoleResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_managed_instance_role

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_managed_instance_role.async_update_managed_instance_role(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_managed_instance_role_request.UpdateManagedInstanceRoleRequest = {
            "instance_id": instance_id,
            "iam_role": iam_role,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ops_item(
        self,
        ops_item_id: "capo_ssm.types.ops_item_id.OpsItemId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        description: Optional[
            "capo_ssm.types.ops_item_description.OpsItemDescription"
        ] = None,
        operational_data: Optional[
            "capo_ssm.types.ops_item_operational_data.OpsItemOperationalData"
        ] = None,
        operational_data_to_delete: Optional[
            "capo_ssm.types.ops_item_ops_data_keys_list.OpsItemOpsDataKeysList"
        ] = None,
        notifications: Optional[
            "capo_ssm.types.ops_item_notifications.OpsItemNotifications"
        ] = None,
        priority: Optional["capo_ssm.types.ops_item_priority.OpsItemPriority"] = None,
        related_ops_items: Optional[
            "capo_ssm.types.related_ops_items.RelatedOpsItems"
        ] = None,
        status: Optional["capo_ssm.types.ops_item_status.OpsItemStatus"] = None,
        title: Optional["capo_ssm.types.ops_item_title.OpsItemTitle"] = None,
        category: Optional["capo_ssm.types.ops_item_category.OpsItemCategory"] = None,
        severity: Optional["capo_ssm.types.ops_item_severity.OpsItemSeverity"] = None,
        actual_start_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        actual_end_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        planned_start_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        planned_end_time: Optional["capo_ssm.types.date_time.DateTime"] = None,
        ops_item_arn: Optional["capo_ssm.types.ops_item_arn.OpsItemArn"] = None,
    ) -> "capo_ssm.types.update_ops_item_response.UpdateOpsItemResponse":
        """<p>Edit or change an OpsItem. You must have permission in Identity and Access Management (IAM) to update an OpsItem. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html">Set up OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p> <p>Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html">Amazon Web Services Systems Manager OpsCenter</a> in the <i>Amazon Web Services Systems Manager User Guide</i>. </p>

        Args:
            description: <p>User-defined text that contains information about the OpsItem, in Markdown format. </p>
            operational_data: <p>Add new keys or edit existing key-value pairs of the OperationalData map in the OpsItem object.</p> <p>Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.</p> <important> <p>Operational data keys <i>can't</i> begin with the following: <code>amazon</code>, <code>aws</code>, <code>amzn</code>, <code>ssm</code>, <code>/amazon</code>, <code>/aws</code>, <code>/amzn</code>, <code>/ssm</code>.</p> </important> <p>You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the <a>DescribeOpsItems</a> API operation) can view and search on the specified data. Operational data that isn't searchable is only viewable by users who have access to the OpsItem (as provided by the <a>GetOpsItem</a> API operation).</p> <p>Use the <code>/aws/resources</code> key in OperationalData to specify a related resource in the request. Use the <code>/aws/automations</code> key in OperationalData to associate an Automation runbook with the OpsItem. To view Amazon Web Services CLI example commands that use these keys, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html">Creating OpsItems manually</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            operational_data_to_delete: <p>Keys that you want to remove from the OperationalData map.</p>
            notifications: <p>The Amazon Resource Name (ARN) of an SNS topic where notifications are sent when this OpsItem is edited or changed.</p>
            priority: <p>The importance of this OpsItem in relation to other OpsItems in the system.</p>
            related_ops_items: <p>One or more OpsItems that share something in common with the current OpsItems. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.</p>
            status: <p>The OpsItem status. For more information, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html">Editing OpsItem details</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            ops_item_id: <p>The ID of the OpsItem.</p>
            title: <p>A short heading that describes the nature of the OpsItem and the impacted resource.</p>
            category: <p>Specify a new category for an OpsItem.</p>
            severity: <p>Specify a new severity for an OpsItem.</p>
            actual_start_time: <p>The time a runbook workflow started. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            actual_end_time: <p>The time a runbook workflow ended. Currently reported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            planned_start_time: <p>The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            planned_end_time: <p>The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type <code>/aws/changerequest</code>.</p>
            ops_item_arn: <p>The OpsItem Amazon Resource Name (ARN).</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_item_access_denied_exception.OpsItemAccessDeniedException: <p>You don't have permission to view OpsItems in the specified account. Verify that your account is configured either as a Systems Manager delegated administrator or that you are logged into the Organizations management account.</p>
            capo_ssm.errors.ops_item_already_exists_exception.OpsItemAlreadyExistsException: <p>The OpsItem already exists.</p>
            capo_ssm.errors.ops_item_conflict_exception.OpsItemConflictException: <p>The specified OpsItem is in the process of being deleted.</p>
            capo_ssm.errors.ops_item_invalid_parameter_exception.OpsItemInvalidParameterException: <p>A specified parameter argument isn't valid. Verify the available arguments and try again.</p>
            capo_ssm.errors.ops_item_limit_exceeded_exception.OpsItemLimitExceededException: <p>The request caused OpsItems to exceed one or more quotas.</p>
            capo_ssm.errors.ops_item_not_found_exception.OpsItemNotFoundException: <p>The specified OpsItem ID doesn't exist. Verify the ID and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_ops_item_request.UpdateOpsItemRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_ops_item_response.UpdateOpsItemResponse"
        ]:
            import capo_ssm._operations.amazon_ssm.update_ops_item

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_ops_item.async_update_ops_item(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_ops_item_request.UpdateOpsItemRequest = {
            "ops_item_id": ops_item_id
        }
        if description is not None:
            input_["description"] = description
        if operational_data is not None:
            input_["operational_data"] = operational_data
        if operational_data_to_delete is not None:
            input_["operational_data_to_delete"] = operational_data_to_delete
        if notifications is not None:
            input_["notifications"] = notifications
        if priority is not None:
            input_["priority"] = priority
        if related_ops_items is not None:
            input_["related_ops_items"] = related_ops_items
        if status is not None:
            input_["status"] = status
        if title is not None:
            input_["title"] = title
        if category is not None:
            input_["category"] = category
        if severity is not None:
            input_["severity"] = severity
        if actual_start_time is not None:
            input_["actual_start_time"] = actual_start_time
        if actual_end_time is not None:
            input_["actual_end_time"] = actual_end_time
        if planned_start_time is not None:
            input_["planned_start_time"] = planned_start_time
        if planned_end_time is not None:
            input_["planned_end_time"] = planned_end_time
        if ops_item_arn is not None:
            input_["ops_item_arn"] = ops_item_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_ops_metadata(
        self,
        ops_metadata_arn: "capo_ssm.types.ops_metadata_arn.OpsMetadataArn",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        metadata_to_update: Optional["capo_ssm.types.metadata_map.MetadataMap"] = None,
        keys_to_delete: Optional[
            "capo_ssm.types.metadata_keys_to_delete_list.MetadataKeysToDeleteList"
        ] = None,
    ) -> "capo_ssm.types.update_ops_metadata_result.UpdateOpsMetadataResult":
        """<p>Amazon Web Services Systems Manager calls this API operation when you edit OpsMetadata in Application Manager.</p>

        Args:
            ops_metadata_arn: <p>The Amazon Resource Name (ARN) of the OpsMetadata Object to update.</p>
            metadata_to_update: <p>Metadata to add to an OpsMetadata object.</p>
            keys_to_delete: <p>The metadata keys to delete from the OpsMetadata object. </p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.ops_metadata_invalid_argument_exception.OpsMetadataInvalidArgumentException: <p>One of the arguments passed is invalid. </p>
            capo_ssm.errors.ops_metadata_key_limit_exceeded_exception.OpsMetadataKeyLimitExceededException: <p>The OpsMetadata object exceeds the maximum number of OpsMetadata keys that you can assign to an application in Application Manager.</p>
            capo_ssm.errors.ops_metadata_not_found_exception.OpsMetadataNotFoundException: <p>The OpsMetadata object doesn't exist. </p>
            capo_ssm.errors.ops_metadata_too_many_updates_exception.OpsMetadataTooManyUpdatesException: <p>The system is processing too many concurrent updates. Wait a few moments and try again.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_ops_metadata_request.UpdateOpsMetadataRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_ops_metadata_result.UpdateOpsMetadataResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_ops_metadata

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_ops_metadata.async_update_ops_metadata(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_ops_metadata_request.UpdateOpsMetadataRequest = {
            "ops_metadata_arn": ops_metadata_arn
        }
        if metadata_to_update is not None:
            input_["metadata_to_update"] = metadata_to_update
        if keys_to_delete is not None:
            input_["keys_to_delete"] = keys_to_delete

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_patch_baseline(
        self,
        baseline_id: "capo_ssm.types.baseline_id.BaselineId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        name: Optional["capo_ssm.types.baseline_name.BaselineName"] = None,
        global_filters: Optional[
            "capo_ssm.types.patch_filter_group.PatchFilterGroup"
        ] = None,
        approval_rules: Optional[
            "capo_ssm.types.patch_rule_group.PatchRuleGroup"
        ] = None,
        approved_patches: Optional["capo_ssm.types.patch_id_list.PatchIdList"] = None,
        approved_patches_compliance_level: Optional[
            "capo_ssm.types.patch_compliance_level.PatchComplianceLevel"
        ] = None,
        approved_patches_enable_non_security: Optional[
            "capo_ssm.types.boolean.Boolean"
        ] = None,
        rejected_patches: Optional["capo_ssm.types.patch_id_list.PatchIdList"] = None,
        rejected_patches_action: Optional[
            "capo_ssm.types.patch_action.PatchAction"
        ] = None,
        description: Optional[
            "capo_ssm.types.baseline_description.BaselineDescription"
        ] = None,
        sources: Optional["capo_ssm.types.patch_source_list.PatchSourceList"] = None,
        available_security_updates_compliance_status: Optional[
            "capo_ssm.types.patch_compliance_status.PatchComplianceStatus"
        ] = None,
        replace: Optional["capo_ssm.types.boolean.Boolean"] = None,
    ) -> "capo_ssm.types.update_patch_baseline_result.UpdatePatchBaselineResult":
        """<p>Modifies an existing patch baseline. Fields not specified in the request are left unchanged.</p> <note> <p>For information about valid key-value pairs in <code>PatchFilters</code> for each supported operating system type, see <a>PatchFilter</a>.</p> </note>

        Args:
            baseline_id: <p>The ID of the patch baseline to update.</p>
            name: <p>The name of the patch baseline.</p>
            global_filters: <p>A set of global filters used to include patches in the baseline.</p> <important> <p>The <code>GlobalFilters</code> parameter can be configured only by using the CLI or an Amazon Web Services SDK. It can't be configured from the Patch Manager console, and its value isn't displayed in the console.</p> </important>
            approval_rules: <p>A set of rules used to include patches in the baseline.</p>
            approved_patches: <p>A list of explicitly approved patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            approved_patches_compliance_level: <p>Assigns a new compliance severity level to an existing patch baseline.</p>
            approved_patches_enable_non_security: <p>Indicates whether the list of approved patches includes non-security updates that should be applied to the managed nodes. The default value is <code>false</code>. Applies to Linux managed nodes only.</p>
            rejected_patches: <p>A list of explicitly rejected patches for the baseline.</p> <p>For information about accepted formats for lists of approved patches and rejected patches, see <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-approved-rejected-package-name-formats.html">Package name formats for approved and rejected patch lists</a> in the <i>Amazon Web Services Systems Manager User Guide</i>.</p>
            rejected_patches_action: <p>The action for Patch Manager to take on patches included in the <code>RejectedPackages</code> list.</p> <dl> <dt>ALLOW_AS_DEPENDENCY</dt> <dd> <p> <b>Linux and macOS</b>: A package in the rejected patches list is installed only if it is a dependency of another package. It is considered compliant with the patch baseline, and its status is reported as <code>INSTALLED_OTHER</code>. This is the default action if no option is specified.</p> <p> <b>Windows Server</b>: Windows Server doesn't support the concept of package dependencies. If a package in the rejected patches list and already installed on the node, its status is reported as <code>INSTALLED_OTHER</code>. Any package not already installed on the node is skipped. This is the default action if no option is specified.</p> </dd> <dt>BLOCK</dt> <dd> <p> <b>All OSs</b>: Packages in the rejected patches list, and packages that include them as dependencies, aren't installed by Patch Manager under any circumstances. </p> <p>State value assignment for patch compliance:</p> <ul> <li> <p>If a package was installed before it was added to the rejected patches list, or is installed outside of Patch Manager afterward, it's considered noncompliant with the patch baseline and its status is reported as <code>INSTALLED_REJECTED</code>.</p> </li> <li> <p>If an update attempts to install a dependency package that is now rejected by the baseline, when previous versions of the package were not rejected, the package being updated is reported as <code>MISSING</code> for <code>SCAN</code> operations and as <code>FAILED</code> for <code>INSTALL</code> operations.</p> </li> </ul> </dd> </dl>
            description: <p>A description of the patch baseline.</p>
            sources: <p>Information about the patches to use to update the managed nodes, including target operating systems and source repositories. Applies to Linux managed nodes only.</p>
            available_security_updates_compliance_status: <p>Indicates the status to be assigned to security patches that are available but not approved because they don't meet the installation criteria specified in the patch baseline.</p> <p>Example scenario: Security patches that you might want installed can be skipped if you have specified a long period to wait after a patch is released before installation. If an update to the patch is released during your specified waiting period, the waiting period for installing the patch starts over. If the waiting period is too long, multiple versions of the patch could be released but never installed.</p> <p>Supported for Windows Server managed nodes only.</p>
            replace: <p>If True, then all fields that are required by the <a>CreatePatchBaseline</a> operation are also required for this API request. Optional fields that aren't specified are set to null.</p>

        Raises:
            capo_ssm.errors.does_not_exist_exception.DoesNotExistException: <p>Error returned when the ID specified for a resource, such as a maintenance window or patch baseline, doesn't exist.</p> <p>For information about resource quotas in Amazon Web Services Systems Manager, see <a href="https://docs.aws.amazon.com/general/latest/gr/ssm.html#limits_ssm">Systems Manager service quotas</a> in the <i>Amazon Web Services General Reference</i>.</p>
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_patch_baseline_request.UpdatePatchBaselineRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_patch_baseline_result.UpdatePatchBaselineResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_patch_baseline

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_patch_baseline.async_update_patch_baseline(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_patch_baseline_request.UpdatePatchBaselineRequest = {
            "baseline_id": baseline_id
        }
        if name is not None:
            input_["name"] = name
        if global_filters is not None:
            input_["global_filters"] = global_filters
        if approval_rules is not None:
            input_["approval_rules"] = approval_rules
        if approved_patches is not None:
            input_["approved_patches"] = approved_patches
        if approved_patches_compliance_level is not None:
            input_["approved_patches_compliance_level"] = (
                approved_patches_compliance_level
            )
        if approved_patches_enable_non_security is not None:
            input_["approved_patches_enable_non_security"] = (
                approved_patches_enable_non_security
            )
        if rejected_patches is not None:
            input_["rejected_patches"] = rejected_patches
        if rejected_patches_action is not None:
            input_["rejected_patches_action"] = rejected_patches_action
        if description is not None:
            input_["description"] = description
        if sources is not None:
            input_["sources"] = sources
        if available_security_updates_compliance_status is not None:
            input_["available_security_updates_compliance_status"] = (
                available_security_updates_compliance_status
            )
        if replace is not None:
            input_["replace"] = replace

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_resource_data_sync(
        self,
        sync_name: "capo_ssm.types.resource_data_sync_name.ResourceDataSyncName",
        sync_type: "capo_ssm.types.resource_data_sync_type.ResourceDataSyncType",
        sync_source: "capo_ssm.types.resource_data_sync_source.ResourceDataSyncSource",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.update_resource_data_sync_result.UpdateResourceDataSyncResult":
        """<p>Update a resource data sync. After you create a resource data sync for a Region, you can't change the account options for that sync. For example, if you create a sync in the us-east-2 (Ohio) Region and you choose the <code>Include only the current account</code> option, you can't edit that sync later and choose the <code>Include all accounts from my Organizations configuration</code> option. Instead, you must delete the first resource data sync, and create a new one.</p> <note> <p>This API operation only supports a resource data sync that was created with a SyncFromSource <code>SyncType</code>.</p> </note>

        Args:
            sync_name: <p>The name of the resource data sync you want to update.</p>
            sync_type: <p>The type of resource data sync. The supported <code>SyncType</code> is SyncFromSource.</p>
            sync_source: <p>Specify information about the data sources to synchronize.</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_data_sync_conflict_exception.ResourceDataSyncConflictException: <p>Another <code>UpdateResourceDataSync</code> request is being processed. Wait a few minutes and try again.</p>
            capo_ssm.errors.resource_data_sync_invalid_configuration_exception.ResourceDataSyncInvalidConfigurationException: <p>The specified sync configuration is invalid.</p>
            capo_ssm.errors.resource_data_sync_not_found_exception.ResourceDataSyncNotFoundException: <p>The specified sync name wasn't found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_resource_data_sync_request.UpdateResourceDataSyncRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_resource_data_sync_result.UpdateResourceDataSyncResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_resource_data_sync

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_resource_data_sync.async_update_resource_data_sync(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_resource_data_sync_request.UpdateResourceDataSyncRequest = {
            "sync_name": sync_name,
            "sync_type": sync_type,
            "sync_source": sync_source,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_service_setting(
        self,
        setting_id: "capo_ssm.types.service_setting_id.ServiceSettingId",
        setting_value: "capo_ssm.types.service_setting_value.ServiceSettingValue",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
    ) -> "capo_ssm.types.update_service_setting_result.UpdateServiceSettingResult":
        """<p> <code>ServiceSetting</code> is an account-level setting for an Amazon Web Services service. This setting defines how a user interacts with or uses a service or a feature of a service. For example, if an Amazon Web Services service charges money to the account based on feature or service usage, then the Amazon Web Services service team might create a default setting of "false". This means the user can't use this feature unless they change the setting to "true" and intentionally opt in for a paid feature.</p> <p>Services map a <code>SettingId</code> object to a setting value. Amazon Web Services services teams define the default value for a <code>SettingId</code>. You can't create a new <code>SettingId</code>, but you can overwrite the default value if you have the <code>ssm:UpdateServiceSetting</code> permission for the setting. Use the <a>GetServiceSetting</a> API operation to view the current value. Or, use the <a>ResetServiceSetting</a> to change the value back to the original value defined by the Amazon Web Services service team.</p> <p>Update the service setting for the account. </p>

        Args:
            setting_id: <p>The Amazon Resource Name (ARN) of the service setting to update. For example, <code>arn:aws:ssm:us-east-1:111122223333:servicesetting/ssm/parameter-store/high-throughput-enabled</code>. The setting ID can be one of the following.</p> <ul> <li> <p> <code>/ssm/appmanager/appmanager-enabled</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-destination</code> </p> </li> <li> <p> <code>/ssm/automation/customer-script-log-group-name</code> </p> </li> <li> <p>/ssm/automation/enable-adaptive-concurrency</p> </li> <li> <p> <code>/ssm/documents/console/public-sharing-permission</code> </p> </li> <li> <p> <code>/ssm/managed-instance/activation-tier</code> </p> </li> <li> <p> <code>/ssm/managed-instance/default-ec2-instance-management-role</code> </p> </li> <li> <p> <code>/ssm/opsinsights/opscenter</code> </p> </li> <li> <p> <code>/ssm/parameter-store/default-parameter-tier</code> </p> </li> <li> <p> <code>/ssm/parameter-store/high-throughput-enabled</code> </p> </li> </ul> <note> <p>Permissions to update the <code>/ssm/managed-instance/default-ec2-instance-management-role</code> setting should only be provided to administrators. Implement least privilege access when allowing individuals to configure or modify the Default Host Management Configuration.</p> </note>
            setting_value: <p>The new value to specify for the service setting. The following list specifies the available values for each setting.</p> <ul> <li> <p>For <code>/ssm/appmanager/appmanager-enabled</code>, enter <code>True</code> or <code>False</code>.</p> </li> <li> <p>For <code>/ssm/automation/customer-script-log-destination</code>, enter <code>CloudWatch</code>.</p> </li> <li> <p>For <code>/ssm/automation/customer-script-log-group-name</code>, enter the name of an Amazon CloudWatch Logs log group.</p> </li> <li> <p>For <code>/ssm/documents/console/public-sharing-permission</code>, enter <code>Enable</code> or <code>Disable</code>.</p> </li> <li> <p>For <code>/ssm/managed-instance/activation-tier</code>, enter <code>standard</code> or <code>advanced</code>.</p> </li> <li> <p>For <code>/ssm/managed-instance/default-ec2-instance-management-role</code>, enter the name of an IAM role. </p> </li> <li> <p> For <code>/ssm/opsinsights/opscenter</code>, enter <code>Enabled</code> or <code>Disabled</code>. </p> </li> <li> <p>For <code>/ssm/parameter-store/default-parameter-tier</code>, enter <code>Standard</code>, <code>Advanced</code>, or <code>Intelligent-Tiering</code> </p> </li> <li> <p>For <code>/ssm/parameter-store/high-throughput-enabled</code>, enter <code>true</code> or <code>false</code>.</p> </li> </ul>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.service_setting_not_found.ServiceSettingNotFound: <p>The specified service setting wasn't found. Either the service name or the setting hasn't been provisioned by the Amazon Web Services service team.</p>
            capo_ssm.errors.too_many_updates.TooManyUpdates: <p>There are concurrent updates for a resource that supports one update at a time.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.update_service_setting_request.UpdateServiceSettingRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.update_service_setting_result.UpdateServiceSettingResult"
        ]:
            import capo_ssm._operations.amazon_ssm.update_service_setting

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.update_service_setting.async_update_service_setting(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.update_service_setting_request.UpdateServiceSettingRequest = {
            "setting_id": setting_id,
            "setting_value": setting_value,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def validate_cloud_connector(
        self,
        cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.validate_cloud_connector_max_results.ValidateCloudConnectorMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "capo_ssm.types.validate_cloud_connector_result.ValidateCloudConnectorResult":
        """<p>Validates the configuration and connectivity of a cloud connector.</p>

        Args:
            cloud_connector_id: <p>The ID of the cloud connector to validate.</p>
            max_results: <p>The maximum number of validation findings to return.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_ssm.errors.internal_server_error.InternalServerError: <p>An error occurred on the server side.</p>
            capo_ssm.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified parameter to be shared could not be found.</p>
            capo_ssm.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_ssm.types.validate_cloud_connector_request.ValidateCloudConnectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_ssm.types.validate_cloud_connector_result.ValidateCloudConnectorResult"
        ]:
            import capo_ssm._operations.amazon_ssm.validate_cloud_connector

            (
                output,
                http_response,
            ) = await capo_ssm._operations.amazon_ssm.validate_cloud_connector.async_validate_cloud_connector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_ssm.types.validate_cloud_connector_request.ValidateCloudConnectorRequest = {
            "cloud_connector_id": cloud_connector_id
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

    async def iter_validate_cloud_connector(
        self,
        cloud_connector_id: "capo_ssm.types.cloud_connector_id.CloudConnectorId",
        *,
        config_overrides: Optional[AsyncSSMClientConfig] = None,
        max_results: Optional[
            "capo_ssm.types.validate_cloud_connector_max_results.ValidateCloudConnectorMaxResults"
        ] = None,
        next_token: Optional["capo_ssm.types.next_token.NextToken"] = None,
    ) -> "AsyncIterator[capo_ssm.types.validation_finding.ValidationFinding]":
        _token = next_token
        while True:
            _response = await self.validate_cloud_connector(
                cloud_connector_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("validation_findings",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, exc_type: Any, exc: Any, tb: Any):
        await self._client.aclose()
