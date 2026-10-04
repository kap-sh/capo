"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#Logs_20140328``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloudwatch_logs._auth._signers
import capo_cloudwatch_logs._auth._sigv4
from capo_cloudwatch_logs._auth._identity import Credentials
from capo_cloudwatch_logs._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudwatch_logs._auth._zapros_handler import AuthMiddleware
from capo_cloudwatch_logs._pagination import resolve_path as _resolve_path
from capo_cloudwatch_logs._services._aws_config import aws_config
from capo_cloudwatch_logs._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.access_policy
    import capo_cloudwatch_logs.types.account_ids
    import capo_cloudwatch_logs.types.account_policy_document
    import capo_cloudwatch_logs.types.aggregate_log_group_summary
    import capo_cloudwatch_logs.types.amazon_resource_name
    import capo_cloudwatch_logs.types.anomaly
    import capo_cloudwatch_logs.types.anomaly_detector
    import capo_cloudwatch_logs.types.anomaly_detector_arn
    import capo_cloudwatch_logs.types.anomaly_id
    import capo_cloudwatch_logs.types.anomaly_visibility_time
    import capo_cloudwatch_logs.types.apply_on_transformed_logs
    import capo_cloudwatch_logs.types.arn
    import capo_cloudwatch_logs.types.associate_kms_key_request
    import capo_cloudwatch_logs.types.associate_source_to_s3_table_integration_request
    import capo_cloudwatch_logs.types.associate_source_to_s3_table_integration_response
    import capo_cloudwatch_logs.types.baseline
    import capo_cloudwatch_logs.types.bearer_token_authentication_enabled
    import capo_cloudwatch_logs.types.boolean
    import capo_cloudwatch_logs.types.cancel_export_task_request
    import capo_cloudwatch_logs.types.cancel_import_task_request
    import capo_cloudwatch_logs.types.cancel_import_task_response
    import capo_cloudwatch_logs.types.client_token
    import capo_cloudwatch_logs.types.configuration_template
    import capo_cloudwatch_logs.types.create_delivery_request
    import capo_cloudwatch_logs.types.create_delivery_response
    import capo_cloudwatch_logs.types.create_export_task_request
    import capo_cloudwatch_logs.types.create_export_task_response
    import capo_cloudwatch_logs.types.create_import_task_request
    import capo_cloudwatch_logs.types.create_import_task_response
    import capo_cloudwatch_logs.types.create_log_anomaly_detector_request
    import capo_cloudwatch_logs.types.create_log_anomaly_detector_response
    import capo_cloudwatch_logs.types.create_log_group_request
    import capo_cloudwatch_logs.types.create_log_stream_request
    import capo_cloudwatch_logs.types.create_lookup_table_request
    import capo_cloudwatch_logs.types.create_lookup_table_response
    import capo_cloudwatch_logs.types.create_scheduled_query_request
    import capo_cloudwatch_logs.types.create_scheduled_query_response
    import capo_cloudwatch_logs.types.data_protection_policy_document
    import capo_cloudwatch_logs.types.data_source
    import capo_cloudwatch_logs.types.data_source_filters
    import capo_cloudwatch_logs.types.data_source_name
    import capo_cloudwatch_logs.types.data_source_type
    import capo_cloudwatch_logs.types.days
    import capo_cloudwatch_logs.types.delete_account_policy_request
    import capo_cloudwatch_logs.types.delete_data_protection_policy_request
    import capo_cloudwatch_logs.types.delete_delivery_destination_policy_request
    import capo_cloudwatch_logs.types.delete_delivery_destination_request
    import capo_cloudwatch_logs.types.delete_delivery_request
    import capo_cloudwatch_logs.types.delete_delivery_source_request
    import capo_cloudwatch_logs.types.delete_destination_request
    import capo_cloudwatch_logs.types.delete_index_policy_request
    import capo_cloudwatch_logs.types.delete_index_policy_response
    import capo_cloudwatch_logs.types.delete_integration_request
    import capo_cloudwatch_logs.types.delete_integration_response
    import capo_cloudwatch_logs.types.delete_log_anomaly_detector_request
    import capo_cloudwatch_logs.types.delete_log_group_request
    import capo_cloudwatch_logs.types.delete_log_stream_request
    import capo_cloudwatch_logs.types.delete_lookup_table_request
    import capo_cloudwatch_logs.types.delete_metric_filter_request
    import capo_cloudwatch_logs.types.delete_query_definition_request
    import capo_cloudwatch_logs.types.delete_query_definition_response
    import capo_cloudwatch_logs.types.delete_resource_policy_request
    import capo_cloudwatch_logs.types.delete_retention_policy_request
    import capo_cloudwatch_logs.types.delete_scheduled_query_request
    import capo_cloudwatch_logs.types.delete_scheduled_query_response
    import capo_cloudwatch_logs.types.delete_subscription_filter_request
    import capo_cloudwatch_logs.types.delete_syslog_configuration_request
    import capo_cloudwatch_logs.types.delete_transformer_request
    import capo_cloudwatch_logs.types.deletion_protection_enabled
    import capo_cloudwatch_logs.types.delivery
    import capo_cloudwatch_logs.types.delivery_destination
    import capo_cloudwatch_logs.types.delivery_destination_configuration
    import capo_cloudwatch_logs.types.delivery_destination_name
    import capo_cloudwatch_logs.types.delivery_destination_policy
    import capo_cloudwatch_logs.types.delivery_destination_type
    import capo_cloudwatch_logs.types.delivery_destination_types
    import capo_cloudwatch_logs.types.delivery_id
    import capo_cloudwatch_logs.types.delivery_source
    import capo_cloudwatch_logs.types.delivery_source_configuration
    import capo_cloudwatch_logs.types.delivery_source_name
    import capo_cloudwatch_logs.types.descending
    import capo_cloudwatch_logs.types.describe_account_policies_request
    import capo_cloudwatch_logs.types.describe_account_policies_response
    import capo_cloudwatch_logs.types.describe_configuration_templates_request
    import capo_cloudwatch_logs.types.describe_configuration_templates_response
    import capo_cloudwatch_logs.types.describe_deliveries_request
    import capo_cloudwatch_logs.types.describe_deliveries_response
    import capo_cloudwatch_logs.types.describe_delivery_destinations_request
    import capo_cloudwatch_logs.types.describe_delivery_destinations_response
    import capo_cloudwatch_logs.types.describe_delivery_sources_request
    import capo_cloudwatch_logs.types.describe_delivery_sources_response
    import capo_cloudwatch_logs.types.describe_destinations_request
    import capo_cloudwatch_logs.types.describe_destinations_response
    import capo_cloudwatch_logs.types.describe_export_tasks_request
    import capo_cloudwatch_logs.types.describe_export_tasks_response
    import capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers
    import capo_cloudwatch_logs.types.describe_field_indexes_request
    import capo_cloudwatch_logs.types.describe_field_indexes_response
    import capo_cloudwatch_logs.types.describe_import_task_batches_request
    import capo_cloudwatch_logs.types.describe_import_task_batches_response
    import capo_cloudwatch_logs.types.describe_import_tasks_request
    import capo_cloudwatch_logs.types.describe_import_tasks_response
    import capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers
    import capo_cloudwatch_logs.types.describe_index_policies_request
    import capo_cloudwatch_logs.types.describe_index_policies_response
    import capo_cloudwatch_logs.types.describe_limit
    import capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers
    import capo_cloudwatch_logs.types.describe_log_groups_request
    import capo_cloudwatch_logs.types.describe_log_groups_response
    import capo_cloudwatch_logs.types.describe_log_streams_request
    import capo_cloudwatch_logs.types.describe_log_streams_response
    import capo_cloudwatch_logs.types.describe_lookup_tables_max_results
    import capo_cloudwatch_logs.types.describe_lookup_tables_request
    import capo_cloudwatch_logs.types.describe_lookup_tables_response
    import capo_cloudwatch_logs.types.describe_metric_filters_request
    import capo_cloudwatch_logs.types.describe_metric_filters_response
    import capo_cloudwatch_logs.types.describe_queries_max_results
    import capo_cloudwatch_logs.types.describe_queries_request
    import capo_cloudwatch_logs.types.describe_queries_response
    import capo_cloudwatch_logs.types.describe_query_definitions_request
    import capo_cloudwatch_logs.types.describe_query_definitions_response
    import capo_cloudwatch_logs.types.describe_resource_policies_request
    import capo_cloudwatch_logs.types.describe_resource_policies_response
    import capo_cloudwatch_logs.types.describe_subscription_filters_request
    import capo_cloudwatch_logs.types.describe_subscription_filters_response
    import capo_cloudwatch_logs.types.destination
    import capo_cloudwatch_logs.types.destination_arn
    import capo_cloudwatch_logs.types.destination_configuration
    import capo_cloudwatch_logs.types.destination_name
    import capo_cloudwatch_logs.types.detector_kms_key_arn
    import capo_cloudwatch_logs.types.detector_name
    import capo_cloudwatch_logs.types.disassociate_kms_key_request
    import capo_cloudwatch_logs.types.disassociate_source_from_s3_table_integration_request
    import capo_cloudwatch_logs.types.disassociate_source_from_s3_table_integration_response
    import capo_cloudwatch_logs.types.distribution
    import capo_cloudwatch_logs.types.emit_system_fields
    import capo_cloudwatch_logs.types.end_time_offset
    import capo_cloudwatch_logs.types.entity
    import capo_cloudwatch_logs.types.evaluation_frequency
    import capo_cloudwatch_logs.types.events_limit
    import capo_cloudwatch_logs.types.events_limit_start_query
    import capo_cloudwatch_logs.types.execution_status_list
    import capo_cloudwatch_logs.types.expected_revision_id
    import capo_cloudwatch_logs.types.export_destination_bucket
    import capo_cloudwatch_logs.types.export_destination_prefix
    import capo_cloudwatch_logs.types.export_task_id
    import capo_cloudwatch_logs.types.export_task_name
    import capo_cloudwatch_logs.types.export_task_status_code
    import capo_cloudwatch_logs.types.field_delimiter
    import capo_cloudwatch_logs.types.field_index_names
    import capo_cloudwatch_logs.types.field_selection_criteria
    import capo_cloudwatch_logs.types.filter_log_events_request
    import capo_cloudwatch_logs.types.filter_log_events_response
    import capo_cloudwatch_logs.types.filter_name
    import capo_cloudwatch_logs.types.filter_pattern
    import capo_cloudwatch_logs.types.force
    import capo_cloudwatch_logs.types.force_update
    import capo_cloudwatch_logs.types.get_data_protection_policy_request
    import capo_cloudwatch_logs.types.get_data_protection_policy_response
    import capo_cloudwatch_logs.types.get_delivery_destination_policy_request
    import capo_cloudwatch_logs.types.get_delivery_destination_policy_response
    import capo_cloudwatch_logs.types.get_delivery_destination_request
    import capo_cloudwatch_logs.types.get_delivery_destination_response
    import capo_cloudwatch_logs.types.get_delivery_request
    import capo_cloudwatch_logs.types.get_delivery_response
    import capo_cloudwatch_logs.types.get_delivery_source_request
    import capo_cloudwatch_logs.types.get_delivery_source_response
    import capo_cloudwatch_logs.types.get_integration_request
    import capo_cloudwatch_logs.types.get_integration_response
    import capo_cloudwatch_logs.types.get_log_anomaly_detector_request
    import capo_cloudwatch_logs.types.get_log_anomaly_detector_response
    import capo_cloudwatch_logs.types.get_log_events_request
    import capo_cloudwatch_logs.types.get_log_events_response
    import capo_cloudwatch_logs.types.get_log_fields_request
    import capo_cloudwatch_logs.types.get_log_fields_response
    import capo_cloudwatch_logs.types.get_log_group_fields_request
    import capo_cloudwatch_logs.types.get_log_group_fields_response
    import capo_cloudwatch_logs.types.get_log_object_request
    import capo_cloudwatch_logs.types.get_log_object_response
    import capo_cloudwatch_logs.types.get_log_record_request
    import capo_cloudwatch_logs.types.get_log_record_response
    import capo_cloudwatch_logs.types.get_lookup_table_request
    import capo_cloudwatch_logs.types.get_lookup_table_response
    import capo_cloudwatch_logs.types.get_query_results_max_items
    import capo_cloudwatch_logs.types.get_query_results_next_token
    import capo_cloudwatch_logs.types.get_query_results_request
    import capo_cloudwatch_logs.types.get_query_results_response
    import capo_cloudwatch_logs.types.get_scheduled_query_history_max_results
    import capo_cloudwatch_logs.types.get_scheduled_query_history_request
    import capo_cloudwatch_logs.types.get_scheduled_query_history_response
    import capo_cloudwatch_logs.types.get_scheduled_query_request
    import capo_cloudwatch_logs.types.get_scheduled_query_response
    import capo_cloudwatch_logs.types.get_storage_tier_policy_request
    import capo_cloudwatch_logs.types.get_storage_tier_policy_response
    import capo_cloudwatch_logs.types.get_transformer_request
    import capo_cloudwatch_logs.types.get_transformer_response
    import capo_cloudwatch_logs.types.import_filter
    import capo_cloudwatch_logs.types.import_id
    import capo_cloudwatch_logs.types.import_status
    import capo_cloudwatch_logs.types.import_status_list
    import capo_cloudwatch_logs.types.include_linked_accounts
    import capo_cloudwatch_logs.types.index_categories
    import capo_cloudwatch_logs.types.input_log_events
    import capo_cloudwatch_logs.types.input_log_stream_names
    import capo_cloudwatch_logs.types.integration_name
    import capo_cloudwatch_logs.types.integration_name_prefix
    import capo_cloudwatch_logs.types.integration_status
    import capo_cloudwatch_logs.types.integration_type
    import capo_cloudwatch_logs.types.interleaved
    import capo_cloudwatch_logs.types.kms_key_id
    import capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by
    import capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_request
    import capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_response
    import capo_cloudwatch_logs.types.list_anomalies_limit
    import capo_cloudwatch_logs.types.list_anomalies_request
    import capo_cloudwatch_logs.types.list_anomalies_response
    import capo_cloudwatch_logs.types.list_integrations_request
    import capo_cloudwatch_logs.types.list_integrations_response
    import capo_cloudwatch_logs.types.list_limit
    import capo_cloudwatch_logs.types.list_log_anomaly_detectors_limit
    import capo_cloudwatch_logs.types.list_log_anomaly_detectors_request
    import capo_cloudwatch_logs.types.list_log_anomaly_detectors_response
    import capo_cloudwatch_logs.types.list_log_groups_for_query_max_results
    import capo_cloudwatch_logs.types.list_log_groups_for_query_request
    import capo_cloudwatch_logs.types.list_log_groups_for_query_response
    import capo_cloudwatch_logs.types.list_log_groups_request
    import capo_cloudwatch_logs.types.list_log_groups_request_limit
    import capo_cloudwatch_logs.types.list_log_groups_response
    import capo_cloudwatch_logs.types.list_scheduled_queries_max_results
    import capo_cloudwatch_logs.types.list_scheduled_queries_request
    import capo_cloudwatch_logs.types.list_scheduled_queries_response
    import capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_max_results
    import capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_request
    import capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_response
    import capo_cloudwatch_logs.types.list_syslog_configurations_max_results
    import capo_cloudwatch_logs.types.list_syslog_configurations_request
    import capo_cloudwatch_logs.types.list_syslog_configurations_response
    import capo_cloudwatch_logs.types.list_tags_for_resource_request
    import capo_cloudwatch_logs.types.list_tags_for_resource_response
    import capo_cloudwatch_logs.types.list_tags_log_group_request
    import capo_cloudwatch_logs.types.list_tags_log_group_response
    import capo_cloudwatch_logs.types.log_group
    import capo_cloudwatch_logs.types.log_group_arn
    import capo_cloudwatch_logs.types.log_group_arn_list
    import capo_cloudwatch_logs.types.log_group_class
    import capo_cloudwatch_logs.types.log_group_identifier
    import capo_cloudwatch_logs.types.log_group_identifiers
    import capo_cloudwatch_logs.types.log_group_name
    import capo_cloudwatch_logs.types.log_group_name_pattern
    import capo_cloudwatch_logs.types.log_group_name_regex_pattern
    import capo_cloudwatch_logs.types.log_group_names
    import capo_cloudwatch_logs.types.log_object_pointer
    import capo_cloudwatch_logs.types.log_record_pointer
    import capo_cloudwatch_logs.types.log_stream
    import capo_cloudwatch_logs.types.log_stream_name
    import capo_cloudwatch_logs.types.log_type
    import capo_cloudwatch_logs.types.log_types
    import capo_cloudwatch_logs.types.lookup_table_description
    import capo_cloudwatch_logs.types.lookup_table_name
    import capo_cloudwatch_logs.types.metric_filter
    import capo_cloudwatch_logs.types.metric_name
    import capo_cloudwatch_logs.types.metric_namespace
    import capo_cloudwatch_logs.types.metric_transformations
    import capo_cloudwatch_logs.types.next_token
    import capo_cloudwatch_logs.types.order_by
    import capo_cloudwatch_logs.types.output_format
    import capo_cloudwatch_logs.types.output_log_event
    import capo_cloudwatch_logs.types.pattern_id
    import capo_cloudwatch_logs.types.policy_document
    import capo_cloudwatch_logs.types.policy_name
    import capo_cloudwatch_logs.types.policy_scope
    import capo_cloudwatch_logs.types.policy_type
    import capo_cloudwatch_logs.types.processors
    import capo_cloudwatch_logs.types.put_account_policy_request
    import capo_cloudwatch_logs.types.put_account_policy_response
    import capo_cloudwatch_logs.types.put_bearer_token_authentication_request
    import capo_cloudwatch_logs.types.put_data_protection_policy_request
    import capo_cloudwatch_logs.types.put_data_protection_policy_response
    import capo_cloudwatch_logs.types.put_delivery_destination_policy_request
    import capo_cloudwatch_logs.types.put_delivery_destination_policy_response
    import capo_cloudwatch_logs.types.put_delivery_destination_request
    import capo_cloudwatch_logs.types.put_delivery_destination_response
    import capo_cloudwatch_logs.types.put_delivery_source_request
    import capo_cloudwatch_logs.types.put_delivery_source_response
    import capo_cloudwatch_logs.types.put_destination_policy_request
    import capo_cloudwatch_logs.types.put_destination_request
    import capo_cloudwatch_logs.types.put_destination_response
    import capo_cloudwatch_logs.types.put_index_policy_request
    import capo_cloudwatch_logs.types.put_index_policy_response
    import capo_cloudwatch_logs.types.put_integration_request
    import capo_cloudwatch_logs.types.put_integration_response
    import capo_cloudwatch_logs.types.put_log_events_request
    import capo_cloudwatch_logs.types.put_log_events_response
    import capo_cloudwatch_logs.types.put_log_group_deletion_protection_request
    import capo_cloudwatch_logs.types.put_metric_filter_request
    import capo_cloudwatch_logs.types.put_query_definition_request
    import capo_cloudwatch_logs.types.put_query_definition_response
    import capo_cloudwatch_logs.types.put_resource_policy_request
    import capo_cloudwatch_logs.types.put_resource_policy_response
    import capo_cloudwatch_logs.types.put_retention_policy_request
    import capo_cloudwatch_logs.types.put_storage_tier_policy_request
    import capo_cloudwatch_logs.types.put_storage_tier_policy_response
    import capo_cloudwatch_logs.types.put_subscription_filter_request
    import capo_cloudwatch_logs.types.put_syslog_configuration_request
    import capo_cloudwatch_logs.types.put_transformer_request
    import capo_cloudwatch_logs.types.query_definition_name
    import capo_cloudwatch_logs.types.query_definition_string
    import capo_cloudwatch_logs.types.query_id
    import capo_cloudwatch_logs.types.query_language
    import capo_cloudwatch_logs.types.query_list_max_results
    import capo_cloudwatch_logs.types.query_parameter_list
    import capo_cloudwatch_logs.types.query_status
    import capo_cloudwatch_logs.types.query_string
    import capo_cloudwatch_logs.types.record_fields
    import capo_cloudwatch_logs.types.resource_config
    import capo_cloudwatch_logs.types.resource_identifier
    import capo_cloudwatch_logs.types.resource_types
    import capo_cloudwatch_logs.types.role_arn
    import capo_cloudwatch_logs.types.s3_delivery_configuration
    import capo_cloudwatch_logs.types.s3_table_integration_source
    import capo_cloudwatch_logs.types.s3_table_integration_source_identifier
    import capo_cloudwatch_logs.types.schedule_expression
    import capo_cloudwatch_logs.types.schedule_timezone
    import capo_cloudwatch_logs.types.schedule_type
    import capo_cloudwatch_logs.types.scheduled_query_description
    import capo_cloudwatch_logs.types.scheduled_query_identifier
    import capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers
    import capo_cloudwatch_logs.types.scheduled_query_name
    import capo_cloudwatch_logs.types.scheduled_query_state
    import capo_cloudwatch_logs.types.scheduled_query_summary
    import capo_cloudwatch_logs.types.scope
    import capo_cloudwatch_logs.types.selection_criteria
    import capo_cloudwatch_logs.types.sequence_token
    import capo_cloudwatch_logs.types.service
    import capo_cloudwatch_logs.types.start_from_head
    import capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers
    import capo_cloudwatch_logs.types.start_live_tail_request
    import capo_cloudwatch_logs.types.start_live_tail_response
    import capo_cloudwatch_logs.types.start_query_request
    import capo_cloudwatch_logs.types.start_query_response
    import capo_cloudwatch_logs.types.start_time_offset
    import capo_cloudwatch_logs.types.stop_query_request
    import capo_cloudwatch_logs.types.stop_query_response
    import capo_cloudwatch_logs.types.storage_tier
    import capo_cloudwatch_logs.types.subscription_filter
    import capo_cloudwatch_logs.types.suppression_period
    import capo_cloudwatch_logs.types.suppression_state
    import capo_cloudwatch_logs.types.suppression_type
    import capo_cloudwatch_logs.types.table_body
    import capo_cloudwatch_logs.types.tag_filters
    import capo_cloudwatch_logs.types.tag_key_list
    import capo_cloudwatch_logs.types.tag_list
    import capo_cloudwatch_logs.types.tag_log_group_request
    import capo_cloudwatch_logs.types.tag_resource_request
    import capo_cloudwatch_logs.types.tags
    import capo_cloudwatch_logs.types.target_arn
    import capo_cloudwatch_logs.types.test_event_messages
    import capo_cloudwatch_logs.types.test_metric_filter_request
    import capo_cloudwatch_logs.types.test_metric_filter_response
    import capo_cloudwatch_logs.types.test_transformer_request
    import capo_cloudwatch_logs.types.test_transformer_response
    import capo_cloudwatch_logs.types.timestamp
    import capo_cloudwatch_logs.types.trigger_history_record
    import capo_cloudwatch_logs.types.unmask
    import capo_cloudwatch_logs.types.untag_log_group_request
    import capo_cloudwatch_logs.types.untag_resource_request
    import capo_cloudwatch_logs.types.update_anomaly_request
    import capo_cloudwatch_logs.types.update_delivery_configuration_request
    import capo_cloudwatch_logs.types.update_delivery_configuration_response
    import capo_cloudwatch_logs.types.update_log_anomaly_detector_request
    import capo_cloudwatch_logs.types.update_lookup_table_request
    import capo_cloudwatch_logs.types.update_lookup_table_response
    import capo_cloudwatch_logs.types.update_scheduled_query_request
    import capo_cloudwatch_logs.types.update_scheduled_query_response
    import capo_cloudwatch_logs.types.vpc_endpoint_id


class CloudWatchLogsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class CloudWatchLogsClient:
    """A client for the ``CloudWatchLogs`` service.

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
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        region: str | None = None,
        use_dual_stack: bool | None = None,
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
        self._config = CloudWatchLogsClientConfig(
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

    def operation_options(
        self, config_overrides: Optional[CloudWatchLogsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudWatchLogsClientConfig = config_overrides or {}
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
        )
        return interceptors_, options_

    def associate_kms_key(
        self,
        kms_key_id: "capo_cloudwatch_logs.types.kms_key_id.KmsKeyId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        resource_identifier: Optional[
            "capo_cloudwatch_logs.types.resource_identifier.ResourceIdentifier"
        ] = None,
    ) -> None:
        """<p>Associates the specified KMS key with either one log group in the account, or with all stored CloudWatch Logs query insights results in the account.</p> <p>When you use <code>AssociateKmsKey</code>, you specify either the <code>logGroupName</code> parameter or the <code>resourceIdentifier</code> parameter. You can't specify both of those parameters in the same operation.</p> <ul> <li> <p>Specify the <code>logGroupName</code> parameter to cause log events ingested into that log group to be encrypted with that key. Only the log events ingested after the key is associated are encrypted with that key.</p> <p>Associating a KMS key with a log group overrides any existing associations between the log group and a KMS key. After a KMS key is associated with a log group, all newly ingested data for the log group is encrypted using the KMS key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs. This enables CloudWatch Logs to decrypt this data whenever it is requested.</p> <p>Associating a key with a log group does not cause the results of queries of that log group to be encrypted with that key. To have query results encrypted with a KMS key, you must use an <code>AssociateKmsKey</code> operation with the <code>resourceIdentifier</code> parameter that specifies a <code>query-result</code> resource. </p> </li> <li> <p>Specify the <code>resourceIdentifier</code> parameter with a <code>query-result</code> resource, to use that key to encrypt the stored results of all future <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a> operations in the account. The response from a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html">GetQueryResults</a> operation will still return the query results in plain text.</p> <p>Even if you have not associated a key with your query results, the query results are encrypted when stored, using the default CloudWatch Logs method.</p> <p>If you run a query from a monitoring account that queries logs in a source account, the query results key from the monitoring account, if any, is used.</p> </li> </ul> <important> <p>If you delete the key that is used to encrypt log events or log group query results, then all the associated stored log events or query results that were encrypted with that key will be unencryptable and unusable.</p> </important> <note> <p>CloudWatch Logs supports only symmetric KMS keys. Do not associate an asymmetric KMS key with your log group or query results. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Using Symmetric and Asymmetric Keys</a>.</p> </note> <p>It can take up to 5 minutes for this operation to take effect.</p> <p>If you attempt to associate a KMS key with a log group but the KMS key does not exist or the KMS key is disabled, you receive an <code>InvalidParameterException</code> error. </p>

        Args:
            log_group_name: <p>The name of the log group.</p> <p>In your <code>AssociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data. This must be a symmetric KMS key. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms">Amazon Resource Names</a> and <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Using Symmetric and Asymmetric Keys</a>.</p>
            resource_identifier: <p>Specifies the target for this operation. You must specify one of the following:</p> <ul> <li> <p>Specify the following ARN to have future <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html">GetQueryResults</a> operations in this account encrypt the results with the specified KMS key. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:query-result:*</code> </p> </li> <li> <p>Specify the ARN of a log group to have CloudWatch Logs use the KMS key to encrypt log events that are ingested and stored by that log group. The log group ARN must be in the following format. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:log-group:<i>LOG_GROUP_NAME</i> </code> </p> </li> </ul> <p>In your <code>AssociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.associate_kms_key_request.AssociateKmsKeyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.associate_kms_key

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.associate_kms_key.associate_kms_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.associate_kms_key_request.AssociateKmsKeyRequest = {
            "kms_key_id": kms_key_id
        }
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_source_to_s3_table_integration(
        self,
        integration_arn: "capo_cloudwatch_logs.types.arn.Arn",
        data_source: "capo_cloudwatch_logs.types.data_source.DataSource",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.associate_source_to_s3_table_integration_response.AssociateSourceToS3TableIntegrationResponse":
        """<p>Associates a data source with an S3 Table Integration for query access in the 'logs' namespace. This enables querying log data using analytics engines that support Iceberg such as Amazon Athena, Amazon Redshift, and Apache Spark.</p>

        Args:
            integration_arn: <p>The Amazon Resource Name (ARN) of the S3 Table Integration to associate the data source with.</p>
            data_source: <p>The data source to associate with the S3 Table Integration. Contains the name and type of the data source.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.associate_source_to_s3_table_integration_request.AssociateSourceToS3TableIntegrationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.associate_source_to_s3_table_integration_response.AssociateSourceToS3TableIntegrationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.associate_source_to_s3_table_integration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.associate_source_to_s3_table_integration.associate_source_to_s3_table_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.associate_source_to_s3_table_integration_request.AssociateSourceToS3TableIntegrationRequest = {
            "integration_arn": integration_arn,
            "data_source": data_source,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_export_task(
        self,
        task_id: "capo_cloudwatch_logs.types.export_task_id.ExportTaskId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Cancels the specified export task.</p> <p>The task must be in the <code>PENDING</code> or <code>RUNNING</code> state.</p>

        Args:
            task_id: <p>The ID of the export task.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.cancel_export_task_request.CancelExportTaskRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.cancel_export_task

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.cancel_export_task.cancel_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.cancel_export_task_request.CancelExportTaskRequest = {
            "task_id": task_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_import_task(
        self,
        import_id: "capo_cloudwatch_logs.types.import_id.ImportId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.cancel_import_task_response.CancelImportTaskResponse":
        """<p>Cancels an active import task and stops importing data from the CloudTrail Lake Event Data Store.</p>

        Args:
            import_id: <p>The ID of the import task to cancel.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.cancel_import_task_request.CancelImportTaskRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.cancel_import_task_response.CancelImportTaskResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.cancel_import_task

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.cancel_import_task.cancel_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.cancel_import_task_request.CancelImportTaskRequest = {
            "import_id": import_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_delivery(
        self,
        delivery_source_name: "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName",
        delivery_destination_arn: "capo_cloudwatch_logs.types.arn.Arn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        record_fields: Optional[
            "capo_cloudwatch_logs.types.record_fields.RecordFields"
        ] = None,
        field_delimiter: Optional[
            "capo_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
        ] = None,
        s3_delivery_configuration: Optional[
            "capo_cloudwatch_logs.types.s3_delivery_configuration.S3DeliveryConfiguration"
        ] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
    ) -> "capo_cloudwatch_logs.types.create_delivery_response.CreateDeliveryResponse":
        """<p>Creates a <i>delivery</i>. A delivery is a connection between a logical <i>delivery source</i> and a logical <i>delivery destination</i> that you have already created.</p> <p>Only some Amazon Web Services services support being configured as a delivery source using this operation. These services are listed as <b>Supported [V2 Permissions]</b> in the table at <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html">Enabling logging from Amazon Web Services services.</a> </p> <p>A delivery destination can represent a log group in CloudWatch Logs, an Amazon S3 bucket, a delivery stream in Firehose, or X-Ray.</p> <p>To configure logs delivery between a supported Amazon Web Services service and a destination, you must do the following:</p> <ul> <li> <p>Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html">PutDeliverySource</a>.</p> </li> <li> <p>Create a <i>delivery destination</i>, which is a logical object that represents the actual delivery destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html">PutDeliveryDestination</a>.</p> </li> <li> <p>If you are delivering logs cross-account, you must use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html">PutDeliveryDestinationPolicy</a> in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination. </p> </li> <li> <p>Use <code>CreateDelivery</code> to create a <i>delivery</i> by pairing exactly one delivery source and one delivery destination. </p> </li> </ul> <p>You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.</p> <p>To update an existing delivery configuration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html">UpdateDeliveryConfiguration</a>.</p>

        Args:
            delivery_source_name: <p>The name of the delivery source to use for this delivery.</p>
            delivery_destination_arn: <p>The ARN of the delivery destination to use for this delivery.</p>
            record_fields: <p>The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.</p>
            field_delimiter: <p>The field delimiter to use between record fields when the final output format of a delivery is in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>
            s3_delivery_configuration: <p>This structure contains parameters that are valid only when the delivery's delivery destination is an S3 bucket.</p>
            tags: <p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_delivery_request.CreateDeliveryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.create_delivery_response.CreateDeliveryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_delivery

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_delivery.create_delivery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_delivery_request.CreateDeliveryRequest = {
            "delivery_source_name": delivery_source_name,
            "delivery_destination_arn": delivery_destination_arn,
        }
        if record_fields is not None:
            input_["record_fields"] = record_fields
        if field_delimiter is not None:
            input_["field_delimiter"] = field_delimiter
        if s3_delivery_configuration is not None:
            input_["s3_delivery_configuration"] = s3_delivery_configuration
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_export_task(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        from_: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        to: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        destination: "capo_cloudwatch_logs.types.export_destination_bucket.ExportDestinationBucket",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        task_name: Optional[
            "capo_cloudwatch_logs.types.export_task_name.ExportTaskName"
        ] = None,
        log_stream_name_prefix: Optional[
            "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
        ] = None,
        destination_prefix: Optional[
            "capo_cloudwatch_logs.types.export_destination_prefix.ExportDestinationPrefix"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.create_export_task_response.CreateExportTaskResponse":
        """<p>Creates an export task so that you can efficiently export data from a log group to an Amazon S3 bucket. When you perform a <code>CreateExportTask</code> operation, you must use credentials that have permission to write to the S3 bucket that you specify as the destination.</p> <p>Exporting log data to S3 buckets that are encrypted by KMS is supported. Exporting log data to Amazon S3 buckets that have S3 Object Lock enabled with a retention period is also supported.</p> <p>Exporting to S3 buckets that are encrypted with AES-256 is supported. </p> <p>This is an asynchronous call. If all the required information is provided, this operation initiates an export task and responds with the ID of the task. After the task has started, you can use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeExportTasks.html">DescribeExportTasks</a> to get the status of the export task. Each account can only have one active (<code>RUNNING</code> or <code>PENDING</code>) export task at a time. To cancel an export task, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CancelExportTask.html">CancelExportTask</a>.</p> <p>You can export logs from multiple log groups or multiple time ranges to the same S3 bucket. To separate log data for each export task, specify a prefix to be used as the Amazon S3 key prefix for all exported objects.</p> <note> <p>We recommend that you don't regularly export to Amazon S3 as a way to continuously archive your logs. For that use case, we instead recommend that you use subscriptions. For more information about subscriptions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions.html">Real-time processing of log data with subscriptions</a>.</p> </note> <note> <p>Time-based sorting on chunks of log data inside an exported file is not guaranteed. You can sort the exported log field data by using Linux utilities.</p> </note>

        Args:
            task_name: <p>The name of the export task.</p>
            log_group_name: <p>The name of the log group.</p>
            log_stream_name_prefix: <p>Export only log streams that match the provided prefix. If you don't specify a value, no prefix filter is applied.</p>
            from_: <p>The start time of the range for the request, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp earlier than this time are not exported.</p>
            to: <p>The end time of the range for the request, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp later than this time are not exported.</p> <p>You must specify a time that is not earlier than when this log group was created.</p>
            destination: <p>The name of S3 bucket for the exported log data. The bucket must be in the same Amazon Web Services Region.</p>
            destination_prefix: <p>The prefix used as the start of the key for every object exported. If you don't specify a value, the default is <code>exportedlogs</code>.</p> <p>The length of this parameter must comply with the S3 object key name length limits. The object key name is a sequence of Unicode characters with UTF-8 encoding, and can be up to 1,024 bytes.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_export_task_request.CreateExportTaskRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.create_export_task_response.CreateExportTaskResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_export_task

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_export_task.create_export_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_export_task_request.CreateExportTaskRequest = {
            "log_group_name": log_group_name,
            "from": from_,
            "to": to,
            "destination": destination,
        }
        if task_name is not None:
            input_["task_name"] = task_name
        if log_stream_name_prefix is not None:
            input_["log_stream_name_prefix"] = log_stream_name_prefix
        if destination_prefix is not None:
            input_["destination_prefix"] = destination_prefix

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_import_task(
        self,
        import_source_arn: "capo_cloudwatch_logs.types.arn.Arn",
        import_role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        import_filter: Optional[
            "capo_cloudwatch_logs.types.import_filter.ImportFilter"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.create_import_task_response.CreateImportTaskResponse":
        """<p>Starts an import from a data source to CloudWatch Log and creates a managed log group as the destination for the imported data. Currently, <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store.html">CloudTrail Event Data Store</a> is the only supported data source. </p> <p>The import task must satisfy the following constraints:</p> <ul> <li> <p>The specified source must be in an ACTIVE state.</p> </li> <li> <p>The API caller must have permissions to access the data in the provided source and to perform iam:PassRole on the provided import role which has the same permissions, as described below.</p> </li> <li> <p>The provided IAM role must trust the "cloudtrail.amazonaws.com" principal and have the following permissions:</p> <ul> <li> <p>cloudtrail:GetEventDataStoreData</p> </li> <li> <p>logs:CreateLogGroup</p> </li> <li> <p>logs:CreateLogStream</p> </li> <li> <p>logs:PutResourcePolicy</p> </li> <li> <p>(If source has an associated Amazon Web Services KMS Key) kms:Decrypt</p> </li> <li> <p>(If source has an associated Amazon Web Services KMS Key) kms:GenerateDataKey</p> </li> </ul> <p>Example IAM policy for provided import role:</p> <p> <code>[ { "Effect": "Allow", "Action": "iam:PassRole", "Resource": "arn:aws:iam::123456789012:role/apiCallerCredentials", "Condition": { "StringLike": { "iam:AssociatedResourceARN": "arn:aws:logs:us-east-1:123456789012:log-group:aws/cloudtrail/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb:*" } } }, { "Effect": "Allow", "Action": [ "cloudtrail:GetEventDataStoreData" ], "Resource": [ "arn:aws:cloudtrail:us-east-1:123456789012:eventdatastore/f1d45bff-d0e3-4868-b5d9-2eb678aa32fb" ] }, { "Effect": "Allow", "Action": [ "logs:CreateImportTask", "logs:CreateLogGroup", "logs:CreateLogStream", "logs:PutResourcePolicy" ], "Resource": [ "arn:aws:logs:us-east-1:123456789012:log-group:/aws/cloudtrail/*" ] }, { "Effect": "Allow", "Action": [ "kms:Decrypt", "kms:GenerateDataKey" ], "Resource": [ "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012" ] } ]</code> </p> </li> <li> <p>If the import source has a customer managed key, the "cloudtrail.amazonaws.com" principal needs permissions to perform kms:Decrypt and kms:GenerateDataKey.</p> </li> <li> <p>There can be no more than 3 active imports per account at a given time.</p> </li> <li> <p>The startEventTime must be less than or equal to endEventTime.</p> </li> <li> <p>The data being imported must be within the specified source's retention period.</p> </li> </ul>

        Args:
            import_source_arn: <p>The ARN of the source to import from.</p>
            import_role_arn: <p>The ARN of the IAM role that grants CloudWatch Logs permission to import from the CloudTrail Lake Event Data Store.</p>
            import_filter: <p>Optional filters to constrain the import by CloudTrail event time. Times are specified in Unix timestamp milliseconds. The range of data being imported must be within the specified source's retention period.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_import_task_request.CreateImportTaskRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.create_import_task_response.CreateImportTaskResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_import_task

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_import_task.create_import_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_import_task_request.CreateImportTaskRequest = {
            "import_source_arn": import_source_arn,
            "import_role_arn": import_role_arn,
        }
        if import_filter is not None:
            input_["import_filter"] = import_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_log_anomaly_detector(
        self,
        log_group_arn_list: "capo_cloudwatch_logs.types.log_group_arn_list.LogGroupArnList",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        detector_name: Optional[
            "capo_cloudwatch_logs.types.detector_name.DetectorName"
        ] = None,
        evaluation_frequency: Optional[
            "capo_cloudwatch_logs.types.evaluation_frequency.EvaluationFrequency"
        ] = None,
        filter_pattern: Optional[
            "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
        ] = None,
        kms_key_id: Optional[
            "capo_cloudwatch_logs.types.detector_kms_key_arn.DetectorKmsKeyArn"
        ] = None,
        anomaly_visibility_time: Optional[
            "capo_cloudwatch_logs.types.anomaly_visibility_time.AnomalyVisibilityTime"
        ] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
    ) -> "capo_cloudwatch_logs.types.create_log_anomaly_detector_response.CreateLogAnomalyDetectorResponse":
        """<p>Creates an <i>anomaly detector</i> that regularly scans one or more log groups and look for patterns and anomalies in the logs.</p> <p>An anomaly detector can help surface issues by automatically discovering anomalies in your log event traffic. An anomaly detector uses machine learning algorithms to scan log events and find <i>patterns</i>. A pattern is a shared text structure that recurs among your log fields. Patterns provide a useful tool for analyzing large sets of logs because a large number of log events can often be compressed into a few patterns.</p> <p>The anomaly detector uses pattern recognition to find <code>anomalies</code>, which are unusual log events. It uses the <code>evaluationFrequency</code> to compare current log events and patterns with trained baselines. </p> <p>Fields within a pattern are called <i>tokens</i>. Fields that vary within a pattern, such as a request ID or timestamp, are referred to as <i>dynamic tokens</i> and represented by <code><*></code>. </p> <p>The following is an example of a pattern:</p> <p> <code>[INFO] Request time: <*> ms</code> </p> <p>This pattern represents log events like <code>[INFO] Request time: 327 ms</code> and other similar log events that differ only by the number, in this csse 327. When the pattern is displayed, the different numbers are replaced by <code><*></code> </p> <note> <p>Any parts of log events that are masked as sensitive data are not scanned for anomalies. For more information about masking sensitive data, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html">Help protect sensitive log data with masking</a>. </p> </note>

        Args:
            log_group_arn_list: <p>An array containing the ARN of the log group that this anomaly detector will watch. You can specify only one log group ARN.</p>
            detector_name: <p>A name for this anomaly detector.</p>
            evaluation_frequency: <p>Specifies how often the anomaly detector is to run and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then 15 minutes might be a good setting for <code>evaluationFrequency</code> .</p>
            filter_pattern: <p>You can use this parameter to limit the anomaly detection model to examine only log events that match the pattern you specify here. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html">Filter and Pattern Syntax</a>.</p>
            kms_key_id: <p>Optionally assigns a KMS key to secure this anomaly detector and its findings. If a key is assigned, the anomalies found and the model used by this detector are encrypted at rest with the key. If a key is assigned to an anomaly detector, a user must have permissions for both this key and for the anomaly detector to retrieve information about the anomalies that it finds.</p> <p> Make sure the value provided is a valid KMS key ARN. For more information about using a KMS key and to see the required IAM policy, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/LogsAnomalyDetection-KMS.html">Use a KMS key with an anomaly detector</a>.</p>
            anomaly_visibility_time: <p>The number of days to have visibility on an anomaly. After this time period has elapsed for an anomaly, it will be automatically baselined and the anomaly detector will treat new occurrences of a similar anomaly as normal. Therefore, if you do not correct the cause of an anomaly during the time period specified in <code>anomalyVisibilityTime</code>, it will be considered normal going forward and will not be detected as an anomaly.</p>
            tags: <p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_log_anomaly_detector_request.CreateLogAnomalyDetectorRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.create_log_anomaly_detector_response.CreateLogAnomalyDetectorResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_log_anomaly_detector

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_log_anomaly_detector.create_log_anomaly_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_log_anomaly_detector_request.CreateLogAnomalyDetectorRequest = {
            "log_group_arn_list": log_group_arn_list
        }
        if detector_name is not None:
            input_["detector_name"] = detector_name
        if evaluation_frequency is not None:
            input_["evaluation_frequency"] = evaluation_frequency
        if filter_pattern is not None:
            input_["filter_pattern"] = filter_pattern
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if anomaly_visibility_time is not None:
            input_["anomaly_visibility_time"] = anomaly_visibility_time
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_log_group(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        kms_key_id: Optional["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
        log_group_class: Optional[
            "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
        ] = None,
        deletion_protection_enabled: Optional[
            "capo_cloudwatch_logs.types.deletion_protection_enabled.DeletionProtectionEnabled"
        ] = None,
    ) -> None:
        """<p>Creates a log group with the specified name. You can create up to 1,000,000 log groups per Region per account.</p> <p>You must use the following guidelines when naming a log group:</p> <ul> <li> <p>Log group names must be unique within a Region for an Amazon Web Services account.</p> </li> <li> <p>Log group names can be between 1 and 512 characters long.</p> </li> <li> <p>Log group names consist of the following characters: a-z, A-Z, 0-9, '_' (underscore), '-' (hyphen), '/' (forward slash), '.' (period), and '#' (number sign)</p> </li> <li> <p>Log group names can't start with the string <code>aws/</code> </p> </li> </ul> <p>When you create a log group, by default the log events in the log group do not expire. To set a retention policy so that events expire and are deleted after a specified time, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutRetentionPolicy.html">PutRetentionPolicy</a>.</p> <p>If you associate an KMS key with the log group, ingested data is encrypted using the KMS key. This association is stored as long as the data encrypted with the KMS key is still within CloudWatch Logs. This enables CloudWatch Logs to decrypt this data whenever it is requested.</p> <p>If you attempt to associate a KMS key with the log group but the KMS key does not exist or the KMS key is disabled, you receive an <code>InvalidParameterException</code> error. </p> <important> <p>CloudWatch Logs supports only symmetric KMS keys. Do not associate an asymmetric KMS key with your log group. For more information, see <a href="https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html">Using Symmetric and Asymmetric Keys</a>.</p> </important>

        Args:
            log_group_name: <p>A name for the log group.</p>
            kms_key_id: <p>The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data. For more information, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms">Amazon Resource Names</a>.</p>
            tags: <p>The key-value pairs to use for the tags.</p> <p>You can grant users access to certain log groups while preventing them from accessing other log groups. To do so, tag your groups and use IAM policies that refer to those tags. To assign tags when you create a log group, you must have either the <code>logs:TagResource</code> or <code>logs:TagLogGroup</code> permission. For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a>. For more information about using tags to control access, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html">Controlling access to Amazon Web Services resources using tags</a>.</p>
            log_group_class: <p>Use this parameter to specify the log group class for this log group. There are three classes:</p> <ul> <li> <p>The <code>Standard</code> log class supports all CloudWatch Logs features.</p> </li> <li> <p>The <code>Infrequent Access</code> log class supports a subset of CloudWatch Logs features and incurs lower costs.</p> </li> <li> <p>Use the <code>Delivery</code> log class only for delivering Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.</p> </li> </ul> <p>If you omit this parameter, the default of <code>STANDARD</code> is used.</p> <important> <p>The value of <code>logGroupClass</code> can't be changed after a log group is created.</p> </important> <p>For details about the features supported by each class, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html">Log classes</a> </p>
            deletion_protection_enabled: <p>Use this parameter to enable deletion protection for the new log group. When enabled on a log group, deletion protection blocks all deletion operations until it is explicitly disabled. By default log groups are created without deletion protection enabled.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_log_group_request.CreateLogGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_log_group

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_log_group.create_log_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_log_group_request.CreateLogGroupRequest = {
            "log_group_name": log_group_name
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if log_group_class is not None:
            input_["log_group_class"] = log_group_class
        if deletion_protection_enabled is not None:
            input_["deletion_protection_enabled"] = deletion_protection_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_log_stream(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        log_stream_name: "capo_cloudwatch_logs.types.log_stream_name.LogStreamName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Creates a log stream for the specified log group. A log stream is a sequence of log events that originate from a single source, such as an application instance or a resource that is being monitored.</p> <p>There is no limit on the number of log streams that you can create for a log group. There is a limit of 50 TPS on <code>CreateLogStream</code> operations, after which transactions are throttled.</p> <p>You must use the following guidelines when naming a log stream:</p> <ul> <li> <p>Log stream names must be unique within the log group.</p> </li> <li> <p>Log stream names can be between 1 and 512 characters long.</p> </li> <li> <p>Don't use ':' (colon) or '*' (asterisk) characters.</p> </li> </ul>

        Args:
            log_group_name: <p>The name of the log group.</p>
            log_stream_name: <p>The name of the log stream.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_log_stream_request.CreateLogStreamRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_log_stream

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_log_stream.create_log_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_log_stream_request.CreateLogStreamRequest = {
            "log_group_name": log_group_name,
            "log_stream_name": log_stream_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_lookup_table(
        self,
        lookup_table_name: "capo_cloudwatch_logs.types.lookup_table_name.LookupTableName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        description: Optional[
            "capo_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
        ] = None,
        table_body: Optional["capo_cloudwatch_logs.types.table_body.TableBody"] = None,
        query_id: Optional["capo_cloudwatch_logs.types.query_id.QueryId"] = None,
        kms_key_id: Optional["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
    ) -> "capo_cloudwatch_logs.types.create_lookup_table_response.CreateLookupTableResponse":
        """<p>Creates a lookup table by uploading CSV data or from CloudWatch Logs query results. You can use lookup tables to enrich log data in CloudWatch Logs queries with reference data such as user details, application names, or error descriptions.</p> <p>The table name must be unique within your account and Region. You must specify either <code>tableBody</code> or <code>queryId</code>, but not both. If you use <code>tableBody</code>, the CSV content must include a header row with column names, use UTF-8 encoding, and not exceed 10 MB.</p>

        Args:
            lookup_table_name: <p>The name of the lookup table. The name must be unique within your account and Region. The name can contain only alphanumeric characters and underscores, and can be up to 256 characters long.</p>
            description: <p>A description of the lookup table. The description can be up to 1024 characters long.</p>
            table_body: <p>The CSV content of the lookup table. The first row must be a header row with column names. The content must use UTF-8 encoding and not exceed 10 MB.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>
            query_id: <p>The ID of a completed or cancelled CloudWatch Logs query whose results populate the lookup table. A cancelled query populates the table with the partial results that were available when the query was stopped.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>
            kms_key_id: <p>The ARN of the KMS key to use to encrypt the lookup table data. If you don't specify a key, the data is encrypted with an Amazon Web Services-owned key.</p>
            tags: <p>A list of key-value pairs to associate with the lookup table. You can associate as many as 50 tags with a lookup table. Tags can help you organize and categorize your resources.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.resource_already_exists_exception.ResourceAlreadyExistsException: <p>The specified resource already exists.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_lookup_table_request.CreateLookupTableRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.create_lookup_table_response.CreateLookupTableResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_lookup_table

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_lookup_table.create_lookup_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_lookup_table_request.CreateLookupTableRequest = {
            "lookup_table_name": lookup_table_name
        }
        if description is not None:
            input_["description"] = description
        if table_body is not None:
            input_["table_body"] = table_body
        if query_id is not None:
            input_["query_id"] = query_id
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_scheduled_query(
        self,
        name: "capo_cloudwatch_logs.types.scheduled_query_name.ScheduledQueryName",
        query_language: "capo_cloudwatch_logs.types.query_language.QueryLanguage",
        query_string: "capo_cloudwatch_logs.types.query_string.QueryString",
        schedule_expression: "capo_cloudwatch_logs.types.schedule_expression.ScheduleExpression",
        execution_role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        description: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
        ] = None,
        log_group_identifiers: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
        ] = None,
        timezone: Optional[
            "capo_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
        ] = None,
        start_time_offset: Optional[
            "capo_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
        ] = None,
        end_time_offset: Optional[
            "capo_cloudwatch_logs.types.end_time_offset.EndTimeOffset"
        ] = None,
        destination_configuration: Optional[
            "capo_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
        ] = None,
        schedule_start_time: Optional[
            "capo_cloudwatch_logs.types.timestamp.Timestamp"
        ] = None,
        schedule_end_time: Optional[
            "capo_cloudwatch_logs.types.timestamp.Timestamp"
        ] = None,
        state: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
        ] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
    ) -> "capo_cloudwatch_logs.types.create_scheduled_query_response.CreateScheduledQueryResponse":
        """<p>Creates a scheduled query that runs CloudWatch Logs Insights queries at regular intervals. Scheduled queries enable proactive monitoring by automatically executing queries to detect patterns and anomalies in your log data. Query results can be delivered to Amazon S3 for analysis or further processing.</p>

        Args:
            name: <p>The name of the scheduled query. The name must be unique within your account and region. Length must be between 1 and 300 characters.</p>
            description: <p>An optional description for the scheduled query to help identify its purpose and functionality.</p>
            query_language: <p>The query language to use for the scheduled query. Valid values are <code>CWLI</code>, <code>PPL</code>, and <code>SQL</code>.</p>
            query_string: <p>The query string to execute. This is the same query syntax used in CloudWatch Logs Insights. Maximum length is 10,000 characters.</p>
            log_group_identifiers: <p>An array of log group names or ARNs to query. You can specify between 1 and 50 log groups. Log groups can be identified by name or full ARN.</p>
            schedule_expression: <p>A cron expression that defines when the scheduled query runs. The expression uses standard cron syntax and supports minute-level precision. Maximum length is 256 characters.</p>
            timezone: <p>The timezone for evaluating the schedule expression. This determines when the scheduled query executes relative to the specified timezone.</p>
            start_time_offset: <p>The time offset in seconds that defines the lookback period for the query. This determines how far back in time the query searches from the execution time.</p>
            end_time_offset: <p>The time offset in seconds that defines the end of the lookback period for the query. Together with <code>startTimeOffset</code>, this determines the time window relative to the execution time over which the query runs.</p>
            destination_configuration: <p>Configuration for where to deliver query results. Supports Amazon S3 destinations for storing query output and lookup table destinations for automatically refreshing lookup tables with query results. You can configure one or both destination types.</p>
            schedule_start_time: <p>The start time for the scheduled query in Unix epoch format. The query will not execute before this time.</p>
            schedule_end_time: <p>The end time for the scheduled query in Unix epoch format. The query will stop executing after this time.</p>
            execution_role_arn: <p>The ARN of the IAM role that grants permissions to execute the query and deliver results to the specified destination. The role must have permissions to read from the specified log groups and write to the destination.</p>
            state: <p>The initial state of the scheduled query. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. Default is <code>ENABLED</code>.</p>
            tags: <p>Key-value pairs to associate with the scheduled query for resource management and cost allocation.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.create_scheduled_query_request.CreateScheduledQueryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.create_scheduled_query_response.CreateScheduledQueryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.create_scheduled_query

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.create_scheduled_query.create_scheduled_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.create_scheduled_query_request.CreateScheduledQueryRequest = {
            "name": name,
            "query_language": query_language,
            "query_string": query_string,
            "schedule_expression": schedule_expression,
            "execution_role_arn": execution_role_arn,
        }
        if description is not None:
            input_["description"] = description
        if log_group_identifiers is not None:
            input_["log_group_identifiers"] = log_group_identifiers
        if timezone is not None:
            input_["timezone"] = timezone
        if start_time_offset is not None:
            input_["start_time_offset"] = start_time_offset
        if end_time_offset is not None:
            input_["end_time_offset"] = end_time_offset
        if destination_configuration is not None:
            input_["destination_configuration"] = destination_configuration
        if schedule_start_time is not None:
            input_["schedule_start_time"] = schedule_start_time
        if schedule_end_time is not None:
            input_["schedule_end_time"] = schedule_end_time
        if state is not None:
            input_["state"] = state
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_account_policy(
        self,
        policy_name: "capo_cloudwatch_logs.types.policy_name.PolicyName",
        policy_type: "capo_cloudwatch_logs.types.policy_type.PolicyType",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes a CloudWatch Logs account policy. This stops the account-wide policy from applying to log groups or data sources in the account. If you delete a data protection policy or subscription filter policy, any log-group level policies of those types remain in effect. This operation supports deletion of data source-based field index policies, including facet configurations, in addition to log group-based policies.</p> <p>To use this operation, you must be signed on with the correct permissions depending on the type of policy that you are deleting.</p> <ul> <li> <p>To delete a data protection policy, you must have the <code>logs:DeleteDataProtectionPolicy</code> and <code>logs:DeleteAccountPolicy</code> permissions.</p> </li> <li> <p>To delete a subscription filter policy, you must have the <code>logs:DeleteSubscriptionFilter</code> and <code>logs:DeleteAccountPolicy</code> permissions.</p> </li> <li> <p>To delete a transformer policy, you must have the <code>logs:DeleteTransformer</code> and <code>logs:DeleteAccountPolicy</code> permissions.</p> </li> <li> <p>To delete a field index policy, you must have the <code>logs:DeleteIndexPolicy</code> and <code>logs:DeleteAccountPolicy</code> permissions.</p> <p>If you delete a field index policy that included facet configurations, those facets will no longer be available for interactive exploration in the CloudWatch Logs Insights console. However, facet data is retained for up to 30 days.</p> </li> </ul> <p>If you delete a field index policy, the indexing of the log events that happened before you deleted the policy will still be used for up to 30 days to improve CloudWatch Logs Insights queries.</p>

        Args:
            policy_name: <p>The name of the policy to delete.</p>
            policy_type: <p>The type of policy to delete.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_account_policy_request.DeleteAccountPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_account_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_account_policy.delete_account_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_account_policy_request.DeleteAccountPolicyRequest = {
            "policy_name": policy_name,
            "policy_type": policy_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_data_protection_policy(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the data protection policy from the specified log group. </p> <p>For more information about data protection policies, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html">PutDataProtectionPolicy</a>.</p>

        Args:
            log_group_identifier: <p>The name or ARN of the log group that you want to delete the data protection policy for.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_data_protection_policy_request.DeleteDataProtectionPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_data_protection_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_data_protection_policy.delete_data_protection_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_data_protection_policy_request.DeleteDataProtectionPolicyRequest = {
            "log_group_identifier": log_group_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_delivery(
        self,
        id: "capo_cloudwatch_logs.types.delivery_id.DeliveryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes a <i>delivery</i>. A delivery is a connection between a logical <i>delivery source</i> and a logical <i>delivery destination</i>. Deleting a delivery only deletes the connection between the delivery source and delivery destination. It does not delete the delivery destination or the delivery source.</p>

        Args:
            id: <p>The unique ID of the delivery to delete. You can find the ID of a delivery with the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.html">DescribeDeliveries</a> operation.</p>

        Raises:
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_delivery_request.DeleteDeliveryRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_delivery

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_delivery.delete_delivery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_delivery_request.DeleteDeliveryRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_delivery_destination(
        self,
        name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes a <i>delivery destination</i>. A delivery is a connection between a logical <i>delivery source</i> and a logical <i>delivery destination</i>.</p> <p>You can't delete a delivery destination if any current deliveries are associated with it. To find whether any deliveries are associated with this delivery destination, use the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.html">DescribeDeliveries</a> operation and check the <code>deliveryDestinationArn</code> field in the results.</p>

        Args:
            name: <p>The name of the delivery destination that you want to delete. You can find a list of delivery destination names by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveryDestinations.html">DescribeDeliveryDestinations</a> operation.</p>

        Raises:
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_delivery_destination_request.DeleteDeliveryDestinationRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_delivery_destination

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_delivery_destination.delete_delivery_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_delivery_destination_request.DeleteDeliveryDestinationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_delivery_destination_policy(
        self,
        delivery_destination_name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes a delivery destination policy. For more information about these policies, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html">PutDeliveryDestinationPolicy</a>.</p>

        Args:
            delivery_destination_name: <p>The name of the delivery destination that you want to delete the policy for.</p>

        Raises:
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_delivery_destination_policy_request.DeleteDeliveryDestinationPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_delivery_destination_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_delivery_destination_policy.delete_delivery_destination_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_delivery_destination_policy_request.DeleteDeliveryDestinationPolicyRequest = {
            "delivery_destination_name": delivery_destination_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_delivery_source(
        self,
        name: "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes a <i>delivery source</i>. A delivery is a connection between a logical <i>delivery source</i> and a logical <i>delivery destination</i>.</p> <p>You can't delete a delivery source if any current deliveries are associated with it. To find whether any deliveries are associated with this delivery source, use the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.html">DescribeDeliveries</a> operation and check the <code>deliverySourceName</code> field in the results.</p>

        Args:
            name: <p>The name of the delivery source that you want to delete.</p>

        Raises:
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_delivery_source_request.DeleteDeliverySourceRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_delivery_source

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_delivery_source.delete_delivery_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_delivery_source_request.DeleteDeliverySourceRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_destination(
        self,
        destination_name: "capo_cloudwatch_logs.types.destination_name.DestinationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified destination, and eventually disables all the subscription filters that publish to it. This operation does not delete the physical resource encapsulated by the destination.</p>

        Args:
            destination_name: <p>The name of the destination.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_destination_request.DeleteDestinationRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_destination

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_destination.delete_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_destination_request.DeleteDestinationRequest = {
            "destination_name": destination_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_index_policy(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.delete_index_policy_response.DeleteIndexPolicyResponse":
        """<p>Deletes a log-group level field index policy that was applied to a single log group. The indexing of the log events that happened before you delete the policy will still be used for as many as 30 days to improve CloudWatch Logs Insights queries.</p> <p>If the deleted policy included facet configurations, those facets will no longer be available for interactive exploration in the CloudWatch Logs Insights console for this log group. However, facet data is retained for up to 30 days.</p> <p>You can't use this operation to delete an account-level index policy. Instead, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteAccountPolicy.html">DeleteAccountPolicy</a>.</p> <p>If you delete a log-group level field index policy and there is an account-level field index policy, in a few minutes the log group begins using that account-wide policy to index new incoming log events. This operation only affects log group-level policies, including any facet configurations, and preserves any data source-based account policies that may apply to the log group.</p>

        Args:
            log_group_identifier: <p>The log group to delete the index policy for. You can specify either the name or the ARN of the log group.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_index_policy_request.DeleteIndexPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.delete_index_policy_response.DeleteIndexPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_index_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_index_policy.delete_index_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_index_policy_request.DeleteIndexPolicyRequest = {
            "log_group_identifier": log_group_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_integration(
        self,
        integration_name: "capo_cloudwatch_logs.types.integration_name.IntegrationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        force: Optional["capo_cloudwatch_logs.types.force.Force"] = None,
    ) -> "capo_cloudwatch_logs.types.delete_integration_response.DeleteIntegrationResponse":
        """<p>Deletes the integration between CloudWatch Logs and OpenSearch Service. If your integration has active vended logs dashboards, you must specify <code>true</code> for the <code>force</code> parameter, otherwise the operation will fail. If you delete the integration by setting <code>force</code> to <code>true</code>, all your vended logs dashboards powered by OpenSearch Service will be deleted and the data that was on them will no longer be accessible.</p>

        Args:
            integration_name: <p>The name of the integration to delete. To find the name of your integration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html">ListIntegrations</a>.</p>
            force: <p>Specify <code>true</code> to force the deletion of the integration even if vended logs dashboards currently exist.</p> <p>The default is <code>false</code>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_integration_request.DeleteIntegrationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.delete_integration_response.DeleteIntegrationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_integration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_integration.delete_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_integration_request.DeleteIntegrationRequest = {
            "integration_name": integration_name
        }
        if force is not None:
            input_["force"] = force

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_log_anomaly_detector(
        self,
        anomaly_detector_arn: "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified CloudWatch Logs anomaly detector.</p>

        Args:
            anomaly_detector_arn: <p>The ARN of the anomaly detector to delete. You can find the ARNs of log anomaly detectors in your account by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogAnomalyDetectors.html">ListLogAnomalyDetectors</a> operation.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_log_anomaly_detector_request.DeleteLogAnomalyDetectorRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_log_anomaly_detector

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_log_anomaly_detector.delete_log_anomaly_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_log_anomaly_detector_request.DeleteLogAnomalyDetectorRequest = {
            "anomaly_detector_arn": anomaly_detector_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_log_group(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified log group and permanently deletes all the archived log events associated with the log group.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_log_group_request.DeleteLogGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_log_group

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_log_group.delete_log_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_log_group_request.DeleteLogGroupRequest = {
            "log_group_name": log_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_log_stream(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        log_stream_name: "capo_cloudwatch_logs.types.log_stream_name.LogStreamName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified log stream and permanently deletes all the archived log events associated with the log stream.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            log_stream_name: <p>The name of the log stream.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_log_stream_request.DeleteLogStreamRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_log_stream

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_log_stream.delete_log_stream(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_log_stream_request.DeleteLogStreamRequest = {
            "log_group_name": log_group_name,
            "log_stream_name": log_stream_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_lookup_table(
        self,
        lookup_table_arn: "capo_cloudwatch_logs.types.arn.Arn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes a lookup table permanently. This operation cannot be undone.</p> <p>Queries that reference a deleted table will return an error. Before deleting a lookup table, review any saved queries or dashboards that may reference it.</p>

        Args:
            lookup_table_arn: <p>The ARN of the lookup table to delete.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_lookup_table_request.DeleteLookupTableRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_lookup_table

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_lookup_table.delete_lookup_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_lookup_table_request.DeleteLookupTableRequest = {
            "lookup_table_arn": lookup_table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_metric_filter(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        filter_name: "capo_cloudwatch_logs.types.filter_name.FilterName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified metric filter.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            filter_name: <p>The name of the metric filter.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_metric_filter_request.DeleteMetricFilterRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_metric_filter

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_metric_filter.delete_metric_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_metric_filter_request.DeleteMetricFilterRequest = {
            "log_group_name": log_group_name,
            "filter_name": filter_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_query_definition(
        self,
        query_definition_id: "capo_cloudwatch_logs.types.query_id.QueryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.delete_query_definition_response.DeleteQueryDefinitionResponse":
        """<p>Deletes a saved CloudWatch Logs Insights query definition. A query definition contains details about a saved CloudWatch Logs Insights query.</p> <p>Each <code>DeleteQueryDefinition</code> operation can delete one query definition.</p> <p>You must have the <code>logs:DeleteQueryDefinition</code> permission to be able to perform this operation.</p>

        Args:
            query_definition_id: <p>The ID of the query definition that you want to delete. You can use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html">DescribeQueryDefinitions</a> to retrieve the IDs of your saved query definitions.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_query_definition_request.DeleteQueryDefinitionRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.delete_query_definition_response.DeleteQueryDefinitionResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_query_definition

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_query_definition.delete_query_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_query_definition_request.DeleteQueryDefinitionRequest = {
            "query_definition_id": query_definition_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_resource_policy(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        policy_name: Optional[
            "capo_cloudwatch_logs.types.policy_name.PolicyName"
        ] = None,
        resource_arn: Optional["capo_cloudwatch_logs.types.arn.Arn"] = None,
        expected_revision_id: Optional[
            "capo_cloudwatch_logs.types.expected_revision_id.ExpectedRevisionId"
        ] = None,
    ) -> None:
        """<p>Deletes a resource policy from this account. This revokes the access of the identities in that policy to put log events to this account.</p>

        Args:
            policy_name: <p>The name of the policy to be revoked. This parameter is required.</p>
            resource_arn: <p>The ARN of the CloudWatch Logs resource for which the resource policy needs to be deleted</p>
            expected_revision_id: <p>The expected revision ID of the resource policy. Required when deleting a resource-scoped policy to prevent concurrent modifications.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_resource_policy_request.DeleteResourcePolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_resource_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_resource_policy.delete_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_resource_policy_request.DeleteResourcePolicyRequest = {}
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_retention_policy(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified retention policy.</p> <p>Log events do not expire if they belong to log groups without a retention policy.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_retention_policy_request.DeleteRetentionPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_retention_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_retention_policy.delete_retention_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_retention_policy_request.DeleteRetentionPolicyRequest = {
            "log_group_name": log_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_scheduled_query(
        self,
        identifier: "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.delete_scheduled_query_response.DeleteScheduledQueryResponse":
        """<p>Deletes a scheduled query and stops all future executions. This operation also removes any configured actions and associated resources.</p>

        Args:
            identifier: <p>The ARN or name of the scheduled query to delete.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_scheduled_query_request.DeleteScheduledQueryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.delete_scheduled_query_response.DeleteScheduledQueryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_scheduled_query

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_scheduled_query.delete_scheduled_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_scheduled_query_request.DeleteScheduledQueryRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_subscription_filter(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        filter_name: "capo_cloudwatch_logs.types.filter_name.FilterName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified subscription filter.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            filter_name: <p>The name of the subscription filter.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_subscription_filter_request.DeleteSubscriptionFilterRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_subscription_filter

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_subscription_filter.delete_subscription_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_subscription_filter_request.DeleteSubscriptionFilterRequest = {
            "log_group_name": log_group_name,
            "filter_name": filter_name,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_syslog_configuration(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        vpc_endpoint_id: Optional[
            "capo_cloudwatch_logs.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
    ) -> None:
        """<p>Deletes a syslog configuration for a log group. After deletion, syslog data is no longer ingested through the specified VPC endpoint.</p>

        Args:
            log_group_identifier: <p>The name or ARN of the log group to remove the syslog configuration from.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint associated with the syslog configuration to delete.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_syslog_configuration_request.DeleteSyslogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_syslog_configuration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_syslog_configuration.delete_syslog_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_syslog_configuration_request.DeleteSyslogConfigurationRequest = {
            "log_group_identifier": log_group_identifier
        }
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_transformer(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Deletes the log transformer for the specified log group. As soon as you do this, the transformation of incoming log events according to that transformer stops. If this account has an account-level transformer that applies to this log group, the log group begins using that account-level transformer when this log-group level transformer is deleted.</p> <p>After you delete a transformer, be sure to edit any metric filters or subscription filters that relied on the transformed versions of the log events.</p>

        Args:
            log_group_identifier: <p>Specify either the name or ARN of the log group to delete the transformer for. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.delete_transformer_request.DeleteTransformerRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.delete_transformer

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.delete_transformer.delete_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.delete_transformer_request.DeleteTransformerRequest = {
            "log_group_identifier": log_group_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account_policies(
        self,
        policy_type: "capo_cloudwatch_logs.types.policy_type.PolicyType",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        policy_name: Optional[
            "capo_cloudwatch_logs.types.policy_name.PolicyName"
        ] = None,
        account_identifiers: Optional[
            "capo_cloudwatch_logs.types.account_ids.AccountIds"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.describe_account_policies_response.DescribeAccountPoliciesResponse":
        """<p>Returns a list of all CloudWatch Logs account policies in the account.</p> <p>To use this operation, you must be signed on with the correct permissions depending on the type of policy that you are retrieving information for.</p> <ul> <li> <p>To see data protection policies, you must have the <code>logs:GetDataProtectionPolicy</code> and <code>logs:DescribeAccountPolicies</code> permissions.</p> </li> <li> <p>To see subscription filter policies, you must have the <code>logs:DescribeSubscriptionFilters</code> and <code>logs:DescribeAccountPolicies</code> permissions.</p> </li> <li> <p>To see transformer policies, you must have the <code>logs:GetTransformer</code> and <code>logs:DescribeAccountPolicies</code> permissions.</p> </li> <li> <p>To see field index policies, you must have the <code>logs:DescribeIndexPolicies</code> and <code>logs:DescribeAccountPolicies</code> permissions.</p> </li> </ul>

        Args:
            policy_type: <p>Use this parameter to limit the returned policies to only the policies that match the policy type that you specify.</p>
            policy_name: <p>Use this parameter to limit the returned policies to only the policy with the name that you specify.</p>
            account_identifiers: <p>If you are using an account that is set up as a monitoring account for CloudWatch unified cross-account observability, you can use this to specify the account ID of a source account. If you do, the operation returns the account policy for the specified account. Currently, you can specify only one account ID in this parameter.</p> <p>If you omit this parameter, only the policy in the current account is returned.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_account_policies_request.DescribeAccountPoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_account_policies_response.DescribeAccountPoliciesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_account_policies

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_account_policies.describe_account_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_account_policies_request.DescribeAccountPoliciesRequest = {
            "policy_type": policy_type
        }
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if account_identifiers is not None:
            input_["account_identifiers"] = account_identifiers
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_configuration_templates(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        service: Optional["capo_cloudwatch_logs.types.service.Service"] = None,
        log_types: Optional["capo_cloudwatch_logs.types.log_types.LogTypes"] = None,
        resource_types: Optional[
            "capo_cloudwatch_logs.types.resource_types.ResourceTypes"
        ] = None,
        delivery_destination_types: Optional[
            "capo_cloudwatch_logs.types.delivery_destination_types.DeliveryDestinationTypes"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_configuration_templates_response.DescribeConfigurationTemplatesResponse":
        """<p>Use this operation to return the valid and default values that are used when creating delivery sources, delivery destinations, and deliveries. For more information about deliveries, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a>.</p>

        Args:
            service: <p>Use this parameter to filter the response to include only the configuration templates that apply to the Amazon Web Services service that you specify here.</p>
            log_types: <p>Use this parameter to filter the response to include only the configuration templates that apply to the log types that you specify here.</p>
            resource_types: <p>Use this parameter to filter the response to include only the configuration templates that apply to the resource types that you specify here.</p>
            delivery_destination_types: <p>Use this parameter to filter the response to include only the configuration templates that apply to the delivery destination types that you specify here.</p>
            limit: <p>Use this parameter to limit the number of configuration templates that are returned in the response.</p>

        Raises:
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_configuration_templates_request.DescribeConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_configuration_templates_response.DescribeConfigurationTemplatesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_configuration_templates

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_configuration_templates.describe_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_configuration_templates_request.DescribeConfigurationTemplatesRequest = {}
        if service is not None:
            input_["service"] = service
        if log_types is not None:
            input_["log_types"] = log_types
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if delivery_destination_types is not None:
            input_["delivery_destination_types"] = delivery_destination_types
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_configuration_templates(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        service: Optional["capo_cloudwatch_logs.types.service.Service"] = None,
        log_types: Optional["capo_cloudwatch_logs.types.log_types.LogTypes"] = None,
        resource_types: Optional[
            "capo_cloudwatch_logs.types.resource_types.ResourceTypes"
        ] = None,
        delivery_destination_types: Optional[
            "capo_cloudwatch_logs.types.delivery_destination_types.DeliveryDestinationTypes"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.configuration_template.ConfigurationTemplate]":
        _token = next_token
        while True:
            _response = self.describe_configuration_templates(
                config_overrides=config_overrides,
                service=service,
                log_types=log_types,
                resource_types=resource_types,
                delivery_destination_types=delivery_destination_types,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("configuration_templates",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_deliveries(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_deliveries_response.DescribeDeliveriesResponse":
        """<p>Retrieves a list of the deliveries that have been created in the account.</p> <p>A <i>delivery</i> is a connection between a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html"> <i>delivery source</i> </a> and a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html"> <i>delivery destination</i> </a>.</p> <p>A delivery source represents an Amazon Web Services resource that sends logs to an logs delivery destination. The destination can be CloudWatch Logs, Amazon S3, Firehose or X-Ray. Only some Amazon Web Services services support being configured as a delivery source. These services are listed in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html">Enable logging from Amazon Web Services services.</a> </p>

        Args:
            limit: <p>Optionally specify the maximum number of deliveries to return in the response.</p>

        Raises:
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_deliveries_request.DescribeDeliveriesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_deliveries_response.DescribeDeliveriesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_deliveries

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_deliveries.describe_deliveries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_deliveries_request.DescribeDeliveriesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_deliveries(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.delivery.Delivery]":
        _token = next_token
        while True:
            _response = self.describe_deliveries(
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("deliveries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_delivery_destinations(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_delivery_destinations_response.DescribeDeliveryDestinationsResponse":
        """<p>Retrieves a list of the delivery destinations that have been created in the account.</p>

        Args:
            limit: <p>Optionally specify the maximum number of delivery destinations to return in the response.</p>

        Raises:
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_delivery_destinations_request.DescribeDeliveryDestinationsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_delivery_destinations_response.DescribeDeliveryDestinationsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_delivery_destinations

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_delivery_destinations.describe_delivery_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_delivery_destinations_request.DescribeDeliveryDestinationsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_delivery_destinations(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> (
        "Iterator[capo_cloudwatch_logs.types.delivery_destination.DeliveryDestination]"
    ):
        _token = next_token
        while True:
            _response = self.describe_delivery_destinations(
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("delivery_destinations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_delivery_sources(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_delivery_sources_response.DescribeDeliverySourcesResponse":
        """<p>Retrieves a list of the delivery sources that have been created in the account.</p>

        Args:
            limit: <p>Optionally specify the maximum number of delivery sources to return in the response.</p>

        Raises:
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_delivery_sources_request.DescribeDeliverySourcesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_delivery_sources_response.DescribeDeliverySourcesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_delivery_sources

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_delivery_sources.describe_delivery_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_delivery_sources_request.DescribeDeliverySourcesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_delivery_sources(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.delivery_source.DeliverySource]":
        _token = next_token
        while True:
            _response = self.describe_delivery_sources(
                config_overrides=config_overrides,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("delivery_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_destinations(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        destination_name_prefix: Optional[
            "capo_cloudwatch_logs.types.destination_name.DestinationName"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_destinations_response.DescribeDestinationsResponse":
        """<p>Lists all your destinations. The results are ASCII-sorted by destination name.</p>

        Args:
            destination_name_prefix: <p>The prefix to match. If you don't specify a value, no prefix filter is applied.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of items returned. If you don't specify a value, the default maximum value of 50 items is used.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_destinations_request.DescribeDestinationsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_destinations_response.DescribeDestinationsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_destinations

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_destinations.describe_destinations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_destinations_request.DescribeDestinationsRequest = {}
        if destination_name_prefix is not None:
            input_["destination_name_prefix"] = destination_name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_destinations(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        destination_name_prefix: Optional[
            "capo_cloudwatch_logs.types.destination_name.DestinationName"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.destination.Destination]":
        _token = next_token
        while True:
            _response = self.describe_destinations(
                config_overrides=config_overrides,
                destination_name_prefix=destination_name_prefix,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("destinations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_export_tasks(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        task_id: Optional[
            "capo_cloudwatch_logs.types.export_task_id.ExportTaskId"
        ] = None,
        status_code: Optional[
            "capo_cloudwatch_logs.types.export_task_status_code.ExportTaskStatusCode"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_export_tasks_response.DescribeExportTasksResponse":
        """<p>Lists the specified export tasks. You can list all your export tasks or filter the results based on task ID or task status.</p>

        Args:
            task_id: <p>The ID of the export task. Specifying a task ID filters the results to one or zero export tasks.</p>
            status_code: <p>The status code of the export task. Specifying a status code filters the results to zero or more export tasks.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_export_tasks_request.DescribeExportTasksRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_export_tasks_response.DescribeExportTasksResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_export_tasks

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_export_tasks.describe_export_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_export_tasks_request.DescribeExportTasksRequest = {}
        if task_id is not None:
            input_["task_id"] = task_id
        if status_code is not None:
            input_["status_code"] = status_code
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_field_indexes(
        self,
        log_group_identifiers: "capo_cloudwatch_logs.types.describe_field_indexes_log_group_identifiers.DescribeFieldIndexesLogGroupIdentifiers",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        index_categories: Optional[
            "capo_cloudwatch_logs.types.index_categories.IndexCategories"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.describe_field_indexes_response.DescribeFieldIndexesResponse":
        """<p>Returns a list of field indexes discovered in log data. By default, the response includes the <code>DEFAULT</code>, <code>CUSTOM</code>, and <code>INACTIVE</code> index categories. To return indexes from other categories, use the <code>indexCategories</code> parameter.</p> <p>For more information about field index policies, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html">PutIndexPolicy</a>.</p>

        Args:
            log_group_identifiers: <p>An array containing the names or ARNs of the log groups that you want to retrieve field indexes for.</p>
            index_categories: <p>The index categories to return. The following values are supported:</p> <ul> <li> <p> <code>DEFAULT</code>: Fields that CloudWatch Logs indexes by default. Examples include <code>@logStream</code> and <code>@data_format</code>.</p> </li> <li> <p> <code>CUSTOM</code>: Fields that you added manually to the field index policy. CloudWatch Logs always indexes these fields. These fields count toward the quota of 20 fields for each log group.</p> </li> <li> <p> <code>AUTO</code>: Fields that CloudWatch Logs indexes automatically based on your query patterns and usage. These fields do not count toward the field index quota. CloudWatch Logs might update these fields based on changes in your query patterns. To keep a field indexed permanently, add it to an account-level or log-group level field index policy.</p> </li> <li> <p> <code>INACTIVE</code>: Fields that CloudWatch Logs indexed before but does not index now. This happens if you remove a field from the field index policy or if CloudWatch Logs automatically selects a different field based on your queries.</p> </li> </ul> <p>If you omit this parameter, the response includes the <code>DEFAULT</code>, <code>CUSTOM</code>, and <code>INACTIVE</code> categories.</p> <p>For more information about automatically indexed fields and using the <code>AUTO</code> category, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Automatic.html">Automatically indexed fields</a>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_field_indexes_request.DescribeFieldIndexesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_field_indexes_response.DescribeFieldIndexesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_field_indexes

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_field_indexes.describe_field_indexes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_field_indexes_request.DescribeFieldIndexesRequest = {
            "log_group_identifiers": log_group_identifiers
        }
        if index_categories is not None:
            input_["index_categories"] = index_categories
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_import_task_batches(
        self,
        import_id: "capo_cloudwatch_logs.types.import_id.ImportId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        batch_import_status: Optional[
            "capo_cloudwatch_logs.types.import_status_list.ImportStatusList"
        ] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.describe_import_task_batches_response.DescribeImportTaskBatchesResponse":
        """<p>Gets detailed information about the individual batches within an import task, including their status and any error messages. For CloudTrail Event Data Store sources, a batch refers to a subset of stored events grouped by their eventTime. </p>

        Args:
            import_id: <p>The ID of the import task to get batch information for.</p>
            batch_import_status: <p>Optional filter to list import batches by their status. Accepts multiple status values: IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>
            limit: <p>The maximum number of import batches to return in the response. Default: 10</p>
            next_token: <p>The pagination token for the next set of results.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_import_task_batches_request.DescribeImportTaskBatchesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_import_task_batches_response.DescribeImportTaskBatchesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_import_task_batches

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_import_task_batches.describe_import_task_batches(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_import_task_batches_request.DescribeImportTaskBatchesRequest = {
            "import_id": import_id
        }
        if batch_import_status is not None:
            input_["batch_import_status"] = batch_import_status
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_import_tasks(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        import_id: Optional["capo_cloudwatch_logs.types.import_id.ImportId"] = None,
        import_status: Optional[
            "capo_cloudwatch_logs.types.import_status.ImportStatus"
        ] = None,
        import_source_arn: Optional["capo_cloudwatch_logs.types.arn.Arn"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.describe_import_tasks_response.DescribeImportTasksResponse":
        """<p>Lists and describes import tasks, with optional filtering by import status and source ARN.</p>

        Args:
            import_id: <p>Optional filter to describe a specific import task by its ID.</p>
            import_status: <p>Optional filter to list imports by their status. Valid values are IN_PROGRESS, CANCELLED, COMPLETED and FAILED.</p>
            import_source_arn: <p>Optional filter to list imports from a specific source</p>
            limit: <p>The maximum number of import tasks to return in the response. Default: 50</p>
            next_token: <p>The pagination token for the next set of results.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_import_tasks_request.DescribeImportTasksRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_import_tasks_response.DescribeImportTasksResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_import_tasks

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_import_tasks.describe_import_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_import_tasks_request.DescribeImportTasksRequest = {}
        if import_id is not None:
            input_["import_id"] = import_id
        if import_status is not None:
            input_["import_status"] = import_status
        if import_source_arn is not None:
            input_["import_source_arn"] = import_source_arn
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_index_policies(
        self,
        log_group_identifiers: "capo_cloudwatch_logs.types.describe_index_policies_log_group_identifiers.DescribeIndexPoliciesLogGroupIdentifiers",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.describe_index_policies_response.DescribeIndexPoliciesResponse":
        """<p>Returns the field index policies of the specified log group. For more information about field index policies, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html">PutIndexPolicy</a>.</p> <p>If a specified log group has a log-group level index policy, that policy is returned by this operation.</p> <p>If a specified log group doesn't have a log-group level index policy, but an account-wide index policy applies to it, that account-wide policy is returned by this operation.</p> <p>To find information about only account-level policies, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeAccountPolicies.html">DescribeAccountPolicies</a> instead.</p>

        Args:
            log_group_identifiers: <p>An array containing the name or ARN of the log group that you want to retrieve field index policies for.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_index_policies_request.DescribeIndexPoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_index_policies_response.DescribeIndexPoliciesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_index_policies

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_index_policies.describe_index_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_index_policies_request.DescribeIndexPoliciesRequest = {
            "log_group_identifiers": log_group_identifiers
        }
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_log_groups(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        account_identifiers: Optional[
            "capo_cloudwatch_logs.types.account_ids.AccountIds"
        ] = None,
        log_group_name_prefix: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_name_pattern: Optional[
            "capo_cloudwatch_logs.types.log_group_name_pattern.LogGroupNamePattern"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
        include_linked_accounts: Optional[
            "capo_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
        ] = None,
        log_group_class: Optional[
            "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
        ] = None,
        log_group_identifiers: Optional[
            "capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers.DescribeLogGroupsLogGroupIdentifiers"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_log_groups_response.DescribeLogGroupsResponse":
        """<p>Returns information about log groups, including data sources that ingest into each log group. You can return all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.</p> <p>CloudWatch Logs doesn't support IAM policies that control access to the <code>DescribeLogGroups</code> action by using the <code>aws:ResourceTag/<i>key-name</i> </code> condition key. Other CloudWatch Logs actions do support the use of the <code>aws:ResourceTag/<i>key-name</i> </code> condition key to control access. For more information about using tags to control access, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html">Controlling access to Amazon Web Services resources using tags</a>.</p> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p>

        Args:
            account_identifiers: <p>When <code>includeLinkedAccounts</code> is set to <code>true</code>, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array. </p>
            log_group_name_prefix: <p>The prefix to match.</p> <note> <p> <code>logGroupNamePrefix</code> and <code>logGroupNamePattern</code> are mutually exclusive. Only one of these parameters can be passed. </p> </note>
            log_group_name_pattern: <p>If you specify a string for this parameter, the operation returns only log groups that have names that match the string based on a case-sensitive substring search. For example, if you specify <code>DataLogs</code>, log groups named <code>DataLogs</code>, <code>aws/DataLogs</code>, and <code>GroupDataLogs</code> would match, but <code>datalogs</code>, <code>Data/log/s</code> and <code>Groupdata</code> would not match.</p> <p>If you specify <code>logGroupNamePattern</code> in your request, then only <code>arn</code>, <code>creationTime</code>, and <code>logGroupName</code> are included in the response. </p> <note> <p> <code>logGroupNamePattern</code> and <code>logGroupNamePrefix</code> are mutually exclusive. Only one of these parameters can be passed. </p> </note>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>
            include_linked_accounts: <p>If you are using a monitoring account, set this to <code>true</code> to have the operation return log groups in the accounts listed in <code>accountIdentifiers</code>.</p> <p>If this parameter is set to <code>true</code> and <code>accountIdentifiers</code> contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account. </p> <p>The default for this parameter is <code>false</code>.</p>
            log_group_class: <p>Use this parameter to limit the results to only those log groups in the specified log group class. If you omit this parameter, log groups of all classes can be returned.</p> <p>Specifies the log group class for this log group. There are three classes:</p> <ul> <li> <p>The <code>Standard</code> log class supports all CloudWatch Logs features.</p> </li> <li> <p>The <code>Infrequent Access</code> log class supports a subset of CloudWatch Logs features and incurs lower costs.</p> </li> <li> <p>Use the <code>Delivery</code> log class only for delivering Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesn't offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.</p> </li> </ul> <p>For details about the features supported by each class, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html">Log classes</a> </p>
            log_group_identifiers: <p>Use this array to filter the list of log groups returned. If you specify this parameter, the only other filter that you can choose to specify is <code>includeLinkedAccounts</code>.</p> <p>If you are using this operation in a monitoring account, you can specify the ARNs of log groups in source accounts and in the monitoring account itself. If you are using this operation in an account that is not a cross-account monitoring account, you can specify only log group names in the same account as the operation.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_log_groups_request.DescribeLogGroupsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_log_groups_response.DescribeLogGroupsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_log_groups

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_log_groups.describe_log_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_log_groups_request.DescribeLogGroupsRequest = {}
        if account_identifiers is not None:
            input_["account_identifiers"] = account_identifiers
        if log_group_name_prefix is not None:
            input_["log_group_name_prefix"] = log_group_name_prefix
        if log_group_name_pattern is not None:
            input_["log_group_name_pattern"] = log_group_name_pattern
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if log_group_class is not None:
            input_["log_group_class"] = log_group_class
        if log_group_identifiers is not None:
            input_["log_group_identifiers"] = log_group_identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_log_groups(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        account_identifiers: Optional[
            "capo_cloudwatch_logs.types.account_ids.AccountIds"
        ] = None,
        log_group_name_prefix: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_name_pattern: Optional[
            "capo_cloudwatch_logs.types.log_group_name_pattern.LogGroupNamePattern"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
        include_linked_accounts: Optional[
            "capo_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
        ] = None,
        log_group_class: Optional[
            "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
        ] = None,
        log_group_identifiers: Optional[
            "capo_cloudwatch_logs.types.describe_log_groups_log_group_identifiers.DescribeLogGroupsLogGroupIdentifiers"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.log_group.LogGroup]":
        _token = next_token
        while True:
            _response = self.describe_log_groups(
                config_overrides=config_overrides,
                account_identifiers=account_identifiers,
                log_group_name_prefix=log_group_name_prefix,
                log_group_name_pattern=log_group_name_pattern,
                next_token=_token,
                limit=limit,
                include_linked_accounts=include_linked_accounts,
                log_group_class=log_group_class,
                log_group_identifiers=log_group_identifiers,
            )
            _page = _resolve_path(_response, ("log_groups",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_log_streams(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
        log_stream_name_prefix: Optional[
            "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
        ] = None,
        order_by: Optional["capo_cloudwatch_logs.types.order_by.OrderBy"] = None,
        descending: Optional["capo_cloudwatch_logs.types.descending.Descending"] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_log_streams_response.DescribeLogStreamsResponse":
        """<p>Lists the log streams for the specified log group. You can list all the log streams or filter the results by prefix. You can also control how the results are ordered.</p> <p>You can specify the log group to search by using either <code>logGroupIdentifier</code> or <code>logGroupName</code>. You must include one of these two parameters, but you can't include both. </p> <p>This operation has a limit of 25 transactions per second, after which transactions are throttled.</p> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p>

        Args:
            log_group_name: <p>The name of the log group.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>
            log_group_identifier: <p>Specify either the name or ARN of the log group to view. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>
            log_stream_name_prefix: <p>The prefix to match.</p> <p>If <code>orderBy</code> is <code>LastEventTime</code>, you cannot specify this parameter.</p>
            order_by: <p>If the value is <code>LogStreamName</code>, the results are ordered by log stream name. If the value is <code>LastEventTime</code>, the results are ordered by the event time. The default value is <code>LogStreamName</code>.</p> <p>If you order the results by event time, you cannot specify the <code>logStreamNamePrefix</code> parameter.</p> <p> <code>lastEventTimestamp</code> represents the time of the most recent log event in the log stream in CloudWatch Logs. This number is expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. <code>lastEventTimestamp</code> updates on an eventual consistency basis. It typically updates in less than an hour from ingestion, but in rare situations might take longer.</p>
            descending: <p>If the value is true, results are returned in descending order. If the value is to false, results are returned in ascending order. The default value is false.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_log_streams_request.DescribeLogStreamsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_log_streams_response.DescribeLogStreamsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_log_streams

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_log_streams.describe_log_streams(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_log_streams_request.DescribeLogStreamsRequest = {}
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if log_group_identifier is not None:
            input_["log_group_identifier"] = log_group_identifier
        if log_stream_name_prefix is not None:
            input_["log_stream_name_prefix"] = log_stream_name_prefix
        if order_by is not None:
            input_["order_by"] = order_by
        if descending is not None:
            input_["descending"] = descending
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_log_streams(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
        log_stream_name_prefix: Optional[
            "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
        ] = None,
        order_by: Optional["capo_cloudwatch_logs.types.order_by.OrderBy"] = None,
        descending: Optional["capo_cloudwatch_logs.types.descending.Descending"] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.log_stream.LogStream]":
        _token = next_token
        while True:
            _response = self.describe_log_streams(
                config_overrides=config_overrides,
                log_group_name=log_group_name,
                log_group_identifier=log_group_identifier,
                log_stream_name_prefix=log_stream_name_prefix,
                order_by=order_by,
                descending=descending,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("log_streams",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_lookup_tables(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        lookup_table_name_prefix: Optional[
            "capo_cloudwatch_logs.types.lookup_table_name.LookupTableName"
        ] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.describe_lookup_tables_max_results.DescribeLookupTablesMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.describe_lookup_tables_response.DescribeLookupTablesResponse":
        """<p>Retrieves metadata about lookup tables in your account. You can optionally filter the results by table name prefix. Results are sorted by table name in ascending order.</p>

        Args:
            lookup_table_name_prefix: <p>A prefix to filter lookup tables by name. Only tables whose names start with this prefix are returned. If you don't specify a prefix, all tables in the account and Region are returned.</p>
            max_results: <p>The maximum number of lookup tables to return in the response. The default value is 50 and the maximum value is 100.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_lookup_tables_request.DescribeLookupTablesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_lookup_tables_response.DescribeLookupTablesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_lookup_tables

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_lookup_tables.describe_lookup_tables(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_lookup_tables_request.DescribeLookupTablesRequest = {}
        if lookup_table_name_prefix is not None:
            input_["lookup_table_name_prefix"] = lookup_table_name_prefix
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

    def describe_metric_filters(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        filter_name_prefix: Optional[
            "capo_cloudwatch_logs.types.filter_name.FilterName"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
        metric_name: Optional[
            "capo_cloudwatch_logs.types.metric_name.MetricName"
        ] = None,
        metric_namespace: Optional[
            "capo_cloudwatch_logs.types.metric_namespace.MetricNamespace"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_metric_filters_response.DescribeMetricFiltersResponse":
        """<p>Lists the specified metric filters. You can list all of the metric filters or filter the results by log name, prefix, metric name, or metric namespace. The results are ASCII-sorted by filter name.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            filter_name_prefix: <p>The prefix to match. CloudWatch Logs uses the value that you set here only if you also include the <code>logGroupName</code> parameter in your request.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>
            metric_name: <p>Filters results to include only those with the specified metric name. If you include this parameter in your request, you must also include the <code>metricNamespace</code> parameter.</p>
            metric_namespace: <p>Filters results to include only those in the specified namespace. If you include this parameter in your request, you must also include the <code>metricName</code> parameter.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_metric_filters_request.DescribeMetricFiltersRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_metric_filters_response.DescribeMetricFiltersResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_metric_filters

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_metric_filters.describe_metric_filters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_metric_filters_request.DescribeMetricFiltersRequest = {}
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if filter_name_prefix is not None:
            input_["filter_name_prefix"] = filter_name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if metric_name is not None:
            input_["metric_name"] = metric_name
        if metric_namespace is not None:
            input_["metric_namespace"] = metric_namespace

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_metric_filters(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        filter_name_prefix: Optional[
            "capo_cloudwatch_logs.types.filter_name.FilterName"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
        metric_name: Optional[
            "capo_cloudwatch_logs.types.metric_name.MetricName"
        ] = None,
        metric_namespace: Optional[
            "capo_cloudwatch_logs.types.metric_namespace.MetricNamespace"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.metric_filter.MetricFilter]":
        _token = next_token
        while True:
            _response = self.describe_metric_filters(
                config_overrides=config_overrides,
                log_group_name=log_group_name,
                filter_name_prefix=filter_name_prefix,
                next_token=_token,
                limit=limit,
                metric_name=metric_name,
                metric_namespace=metric_namespace,
            )
            _page = _resolve_path(_response, ("metric_filters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_queries(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        status: Optional["capo_cloudwatch_logs.types.query_status.QueryStatus"] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.describe_queries_max_results.DescribeQueriesMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        query_language: Optional[
            "capo_cloudwatch_logs.types.query_language.QueryLanguage"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_queries_response.DescribeQueriesResponse":
        """<p>Returns a list of CloudWatch Logs Insights queries that are scheduled, running, or have been run recently in this account. You can request all queries or limit it to queries of a specific log group or queries with a certain status.</p> <p>This operation includes both interactive queries started directly by users and automated queries executed by scheduled query configurations. Scheduled query executions appear in the results alongside manually initiated queries, providing visibility into all query activity in your account.</p>

        Args:
            log_group_name: <p>Limits the returned queries to only those for the specified log group.</p>
            status: <p>Limits the returned queries to only those that have the specified status. Valid values are <code>Cancelled</code>, <code>Complete</code>, <code>Failed</code>, <code>Running</code>, and <code>Scheduled</code>.</p>
            max_results: <p>Limits the number of returned queries to the specified number.</p>
            query_language: <p>Limits the returned queries to only the queries that use the specified query language.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_queries_request.DescribeQueriesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_queries_response.DescribeQueriesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_queries

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_queries.describe_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_queries_request.DescribeQueriesRequest = {}
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if status is not None:
            input_["status"] = status
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if query_language is not None:
            input_["query_language"] = query_language

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_query_definitions(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        query_language: Optional[
            "capo_cloudwatch_logs.types.query_language.QueryLanguage"
        ] = None,
        query_definition_name_prefix: Optional[
            "capo_cloudwatch_logs.types.query_definition_name.QueryDefinitionName"
        ] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.query_list_max_results.QueryListMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.describe_query_definitions_response.DescribeQueryDefinitionsResponse":
        """<p>This operation returns a paginated list of your saved CloudWatch Logs Insights query definitions. You can retrieve query definitions from the current account or from a source account that is linked to the current account.</p> <p>You can use the <code>queryDefinitionNamePrefix</code> parameter to limit the results to only the query definitions that have names that start with a certain string.</p>

        Args:
            query_language: <p>The query language used for this query. For more information about the query languages that CloudWatch Logs supports, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html">Supported query languages</a>.</p>
            query_definition_name_prefix: <p>Use this parameter to filter your results to only the query definitions that have names that start with the prefix you specify.</p>
            max_results: <p>Limits the number of returned query definitions to the specified number.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_query_definitions_request.DescribeQueryDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_query_definitions_response.DescribeQueryDefinitionsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_query_definitions

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_query_definitions.describe_query_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_query_definitions_request.DescribeQueryDefinitionsRequest = {}
        if query_language is not None:
            input_["query_language"] = query_language
        if query_definition_name_prefix is not None:
            input_["query_definition_name_prefix"] = query_definition_name_prefix
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

    def describe_resource_policies(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
        resource_arn: Optional["capo_cloudwatch_logs.types.arn.Arn"] = None,
        policy_scope: Optional[
            "capo_cloudwatch_logs.types.policy_scope.PolicyScope"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_resource_policies_response.DescribeResourcePoliciesResponse":
        """<p>Lists the resource policies in this account.</p>

        Args:
            limit: <p>The maximum number of resource policies to be displayed with one call of this API.</p>
            resource_arn: <p>The ARN of the CloudWatch Logs resource for which to query the resource policy.</p>
            policy_scope: <p>Specifies the scope of the resource policy. Valid values are <code>ACCOUNT</code> or <code>RESOURCE</code>. When not specified, defaults to <code>ACCOUNT</code>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_resource_policies_request.DescribeResourcePoliciesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_resource_policies_response.DescribeResourcePoliciesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_resource_policies

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_resource_policies.describe_resource_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_resource_policies_request.DescribeResourcePoliciesRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if policy_scope is not None:
            input_["policy_scope"] = policy_scope

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_subscription_filters(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        filter_name_prefix: Optional[
            "capo_cloudwatch_logs.types.filter_name.FilterName"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.describe_subscription_filters_response.DescribeSubscriptionFiltersResponse":
        """<p>Lists the subscription filters for the specified log group. You can list all the subscription filters or filter the results by prefix. The results are ASCII-sorted by filter name.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            filter_name_prefix: <p>The prefix to match. If you don't specify a value, no prefix filter is applied.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of items returned. If you don't specify a value, the default is up to 50 items.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.describe_subscription_filters_request.DescribeSubscriptionFiltersRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.describe_subscription_filters_response.DescribeSubscriptionFiltersResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.describe_subscription_filters

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.describe_subscription_filters.describe_subscription_filters(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.describe_subscription_filters_request.DescribeSubscriptionFiltersRequest = {
            "log_group_name": log_group_name
        }
        if filter_name_prefix is not None:
            input_["filter_name_prefix"] = filter_name_prefix
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_subscription_filters(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        filter_name_prefix: Optional[
            "capo_cloudwatch_logs.types.filter_name.FilterName"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.describe_limit.DescribeLimit"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.subscription_filter.SubscriptionFilter]":
        _token = next_token
        while True:
            _response = self.describe_subscription_filters(
                log_group_name,
                config_overrides=config_overrides,
                filter_name_prefix=filter_name_prefix,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("subscription_filters",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def disassociate_kms_key(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        resource_identifier: Optional[
            "capo_cloudwatch_logs.types.resource_identifier.ResourceIdentifier"
        ] = None,
    ) -> None:
        """<p>Disassociates the specified KMS key from the specified log group or from all CloudWatch Logs Insights query results in the account.</p> <p>When you use <code>DisassociateKmsKey</code>, you specify either the <code>logGroupName</code> parameter or the <code>resourceIdentifier</code> parameter. You can't specify both of those parameters in the same operation.</p> <ul> <li> <p>Specify the <code>logGroupName</code> parameter to stop using the KMS key to encrypt future log events ingested and stored in the log group. Instead, they will be encrypted with the default CloudWatch Logs method. The log events that were ingested while the key was associated with the log group are still encrypted with that key. Therefore, CloudWatch Logs will need permissions for the key whenever that data is accessed.</p> </li> <li> <p>Specify the <code>resourceIdentifier</code> parameter with the <code>query-result</code> resource to stop using the KMS key to encrypt the results of all future <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a> operations in the account. They will instead be encrypted with the default CloudWatch Logs method. The results from queries that ran while the key was associated with the account are still encrypted with that key. Therefore, CloudWatch Logs will need permissions for the key whenever that data is accessed.</p> </li> </ul> <p>It can take up to 5 minutes for this operation to take effect.</p>

        Args:
            log_group_name: <p>The name of the log group.</p> <p>In your <code>DisassociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>
            resource_identifier: <p>Specifies the target for this operation. You must specify one of the following:</p> <ul> <li> <p>Specify the ARN of a log group to stop having CloudWatch Logs use the KMS key to encrypt log events that are ingested and stored by that log group. After you run this operation, CloudWatch Logs encrypts ingested log events with the default CloudWatch Logs method. The log group ARN must be in the following format. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:log-group:<i>LOG_GROUP_NAME</i> </code> </p> </li> <li> <p>Specify the following ARN to stop using this key to encrypt the results of future <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a> operations in this account. Replace <i>REGION</i> and <i>ACCOUNT_ID</i> with your Region and account ID.</p> <p> <code>arn:aws:logs:<i>REGION</i>:<i>ACCOUNT_ID</i>:query-result:*</code> </p> </li> </ul> <p>In your <code>DisssociateKmsKey</code> operation, you must specify either the <code>resourceIdentifier</code> parameter or the <code>logGroup</code> parameter, but you can't specify both.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.disassociate_kms_key_request.DisassociateKmsKeyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.disassociate_kms_key

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.disassociate_kms_key.disassociate_kms_key(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.disassociate_kms_key_request.DisassociateKmsKeyRequest = {}
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_source_from_s3_table_integration(
        self,
        identifier: "capo_cloudwatch_logs.types.s3_table_integration_source_identifier.S3TableIntegrationSourceIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.disassociate_source_from_s3_table_integration_response.DisassociateSourceFromS3TableIntegrationResponse":
        """<p>Disassociates a data source from an S3 Table Integration, removing query access and deleting all associated data from the integration.</p>

        Args:
            identifier: <p>The unique identifier of the association to remove between the data source and S3 Table Integration.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.disassociate_source_from_s3_table_integration_request.DisassociateSourceFromS3TableIntegrationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.disassociate_source_from_s3_table_integration_response.DisassociateSourceFromS3TableIntegrationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.disassociate_source_from_s3_table_integration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.disassociate_source_from_s3_table_integration.disassociate_source_from_s3_table_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.disassociate_source_from_s3_table_integration_request.DisassociateSourceFromS3TableIntegrationRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def filter_log_events(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
        log_stream_names: Optional[
            "capo_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
        ] = None,
        log_stream_name_prefix: Optional[
            "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
        ] = None,
        start_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        filter_pattern: Optional[
            "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional["capo_cloudwatch_logs.types.events_limit.EventsLimit"] = None,
        start_from_head: Optional[
            "capo_cloudwatch_logs.types.start_from_head.StartFromHead"
        ] = None,
        interleaved: Optional[
            "capo_cloudwatch_logs.types.interleaved.Interleaved"
        ] = None,
        unmask: Optional["capo_cloudwatch_logs.types.unmask.Unmask"] = None,
    ) -> (
        "capo_cloudwatch_logs.types.filter_log_events_response.FilterLogEventsResponse"
    ):
        """<p>Lists log events from the specified log group. You can list all the log events or filter the results using one or more of the following:</p> <ul> <li> <p>A filter pattern</p> </li> <li> <p>A time range</p> </li> <li> <p>The log stream name, or a log stream name prefix that matches multiple log streams</p> </li> </ul> <p>You must have the <code>logs:FilterLogEvents</code> permission to perform this operation.</p> <p>You can specify the log group to search by using either <code>logGroupIdentifier</code> or <code>logGroupName</code>. You must include one of these two parameters, but you can't include both. </p> <p> <code>FilterLogEvents</code> is a paginated operation. Each page returned can contain up to 1 MB of log events or up to 10,000 log events. A returned page might only be partially full, or even empty. For example, if the result of a query would return 15,000 log events, the first page isn't guaranteed to have 10,000 log events even if they all fit into 1 MB.</p> <p>Partially full or empty pages don't necessarily mean that pagination is finished. If the results include a <code>nextToken</code>, there might be more log events available. You can return these additional log events by providing the nextToken in a subsequent <code>FilterLogEvents</code> operation. If the results don't include a <code>nextToken</code>, then pagination is finished. </p> <p>Specifying the <code>limit</code> parameter only guarantees that a single page doesn't return more log events than the specified limit, but it might return fewer events than the limit. This is the expected API behavior.</p> <p>The returned log events are sorted by event timestamp, the timestamp when the event was ingested by CloudWatch Logs, and the ID of the <code>PutLogEvents</code> request. By default, the events are returned in ascending timestamp order (oldest first). To return events in descending timestamp order (newest first), set the <code>startFromHead</code> parameter to <code>false</code>.</p> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p> <note> <p>If you are using <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html">log transformation</a>, the <code>FilterLogEvents</code> operation returns only the original versions of log events, before they were transformed. To view the transformed versions, you must use a <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html">CloudWatch Logs query.</a> </p> </note>

        Args:
            log_group_name: <p>The name of the log group to search.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>
            log_group_identifier: <p>Specify either the name or ARN of the log group to view log events from. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>
            log_stream_names: <p>Filters the results to only logs from the log streams in this list.</p> <p>If you specify a value for both <code>logStreamNames</code> and <code>logStreamNamePrefix</code>, the action returns an <code>InvalidParameterException</code> error.</p>
            log_stream_name_prefix: <p>Filters the results to include only events from log streams that have names starting with this prefix.</p> <p>If you specify a value for both <code>logStreamNamePrefix</code> and <code>logStreamNames</code>, the action returns an <code>InvalidParameterException</code> error.</p>
            start_time: <p>The start of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp before this time are not returned.</p> <note> <p>Set <code>startTime</code> explicitly to reduce the chances of empty pages in the response.</p> </note>
            end_time: <p>The end of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp later than this time are not returned.</p>
            filter_pattern: <p>The filter pattern to use. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html">Filter and Pattern Syntax</a>.</p> <p>If not provided, all the events are matched.</p>
            next_token: <p>The token for the next set of events to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of events to return. The default is 10,000 events.</p>
            start_from_head: <p>If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is true.</p> <p>The <code>startFromHead</code> parameter sets the sort direction on the first request. On subsequent requests, the <code>nextToken</code> determines the sort direction. To continue paginating in the same direction, provide the returned <code>nextToken</code>. If you provide both <code>nextToken</code> and <code>startFromHead</code>, the direction of the <code>nextToken</code> is used.</p> <note> <p>Setting <code>startFromHead</code> to <code>false</code> is supported only when <code>startTime</code> is on or after <code>Jan 1, 2024 00:00:00 UTC</code>. A request with <code>startFromHead</code> set to <code>false</code> and a <code>startTime</code> before this date returns an <code>InvalidParameterException</code>.</p> </note>
            interleaved: <p>If the value is true, the operation attempts to provide responses that contain events from multiple log streams within the log group, interleaved in a single response. If the value is false, all the matched log events in the first log stream are searched first, then those in the next log stream, and so on.</p> <p> <b>Important</b> As of June 17, 2019, this parameter is ignored and the value is assumed to be true. The response from this operation always interleaves events from multiple log streams within a log group.</p>
            unmask: <p>Specify <code>true</code> to display the log event fields with all sensitive data unmasked and visible. The default is <code>false</code>.</p> <p>To use this operation with this parameter, you must be signed into an account with the <code>logs:Unmask</code> permission.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.filter_log_events_request.FilterLogEventsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.filter_log_events_response.FilterLogEventsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.filter_log_events

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.filter_log_events.filter_log_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.filter_log_events_request.FilterLogEventsRequest = {}
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if log_group_identifier is not None:
            input_["log_group_identifier"] = log_group_identifier
        if log_stream_names is not None:
            input_["log_stream_names"] = log_stream_names
        if log_stream_name_prefix is not None:
            input_["log_stream_name_prefix"] = log_stream_name_prefix
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if filter_pattern is not None:
            input_["filter_pattern"] = filter_pattern
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if start_from_head is not None:
            input_["start_from_head"] = start_from_head
        if interleaved is not None:
            input_["interleaved"] = interleaved
        if unmask is not None:
            input_["unmask"] = unmask

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_filter_log_events(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
        log_stream_names: Optional[
            "capo_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
        ] = None,
        log_stream_name_prefix: Optional[
            "capo_cloudwatch_logs.types.log_stream_name.LogStreamName"
        ] = None,
        start_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        filter_pattern: Optional[
            "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional["capo_cloudwatch_logs.types.events_limit.EventsLimit"] = None,
        start_from_head: Optional[
            "capo_cloudwatch_logs.types.start_from_head.StartFromHead"
        ] = None,
        interleaved: Optional[
            "capo_cloudwatch_logs.types.interleaved.Interleaved"
        ] = None,
        unmask: Optional["capo_cloudwatch_logs.types.unmask.Unmask"] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.filter_log_events_response.FilterLogEventsResponse]":
        _token = next_token
        while True:
            _response = self.filter_log_events(
                config_overrides=config_overrides,
                log_group_name=log_group_name,
                log_group_identifier=log_group_identifier,
                log_stream_names=log_stream_names,
                log_stream_name_prefix=log_stream_name_prefix,
                start_time=start_time,
                end_time=end_time,
                filter_pattern=filter_pattern,
                next_token=_token,
                limit=limit,
                start_from_head=start_from_head,
                interleaved=interleaved,
                unmask=unmask,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_data_protection_policy(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_data_protection_policy_response.GetDataProtectionPolicyResponse":
        """<p>Returns information about a log group data protection policy.</p>

        Args:
            log_group_identifier: <p>The name or ARN of the log group that contains the data protection policy that you want to see.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_data_protection_policy_request.GetDataProtectionPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_data_protection_policy_response.GetDataProtectionPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_data_protection_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_data_protection_policy.get_data_protection_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_data_protection_policy_request.GetDataProtectionPolicyRequest = {
            "log_group_identifier": log_group_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_delivery(
        self,
        id: "capo_cloudwatch_logs.types.delivery_id.DeliveryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_delivery_response.GetDeliveryResponse":
        """<p>Returns complete information about one logical <i>delivery</i>. A delivery is a connection between a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html"> <i>delivery source</i> </a> and a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html"> <i>delivery destination</i> </a>.</p> <p>A delivery source represents an Amazon Web Services resource that sends logs to an logs delivery destination. The destination can be CloudWatch Logs, Amazon S3, or Firehose. Only some Amazon Web Services services support being configured as a delivery source. These services are listed in <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html">Enable logging from Amazon Web Services services.</a> </p> <p>You need to specify the delivery <code>id</code> in this operation. You can find the IDs of the deliveries in your account with the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeDeliveries.html">DescribeDeliveries</a> operation.</p>

        Args:
            id: <p>The ID of the delivery that you want to retrieve.</p>

        Raises:
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_delivery_request.GetDeliveryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_delivery_response.GetDeliveryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_delivery

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_delivery.get_delivery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_delivery_request.GetDeliveryRequest = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_delivery_destination(
        self,
        name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_delivery_destination_response.GetDeliveryDestinationResponse":
        """<p>Retrieves complete information about one delivery destination.</p>

        Args:
            name: <p>The name of the delivery destination that you want to retrieve.</p>

        Raises:
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_delivery_destination_request.GetDeliveryDestinationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_delivery_destination_response.GetDeliveryDestinationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_delivery_destination

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_delivery_destination.get_delivery_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_delivery_destination_request.GetDeliveryDestinationRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_delivery_destination_policy(
        self,
        delivery_destination_name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_delivery_destination_policy_response.GetDeliveryDestinationPolicyResponse":
        """<p>Retrieves the delivery destination policy assigned to the delivery destination that you specify. For more information about delivery destinations and their policies, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html">PutDeliveryDestinationPolicy</a>.</p>

        Args:
            delivery_destination_name: <p>The name of the delivery destination that you want to retrieve the policy of.</p>

        Raises:
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_delivery_destination_policy_request.GetDeliveryDestinationPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_delivery_destination_policy_response.GetDeliveryDestinationPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_delivery_destination_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_delivery_destination_policy.get_delivery_destination_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_delivery_destination_policy_request.GetDeliveryDestinationPolicyRequest = {
            "delivery_destination_name": delivery_destination_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_delivery_source(
        self,
        name: "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_delivery_source_response.GetDeliverySourceResponse":
        """<p>Retrieves complete information about one delivery source.</p>

        Args:
            name: <p>The name of the delivery source that you want to retrieve.</p>

        Raises:
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_delivery_source_request.GetDeliverySourceRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_delivery_source_response.GetDeliverySourceResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_delivery_source

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_delivery_source.get_delivery_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_delivery_source_request.GetDeliverySourceRequest = {
            "name": name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_integration(
        self,
        integration_name: "capo_cloudwatch_logs.types.integration_name.IntegrationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_integration_response.GetIntegrationResponse":
        """<p>Returns information about one integration between CloudWatch Logs and OpenSearch Service. </p>

        Args:
            integration_name: <p>The name of the integration that you want to find information about. To find the name of your integration, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html">ListIntegrations</a> </p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_integration_request.GetIntegrationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_integration_response.GetIntegrationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_integration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_integration.get_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_integration_request.GetIntegrationRequest = {
            "integration_name": integration_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_log_anomaly_detector(
        self,
        anomaly_detector_arn: "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_log_anomaly_detector_response.GetLogAnomalyDetectorResponse":
        """<p>Retrieves information about the log anomaly detector that you specify. The KMS key ARN detected is valid.</p>

        Args:
            anomaly_detector_arn: <p>The ARN of the anomaly detector to retrieve information about. You can find the ARNs of log anomaly detectors in your account by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListLogAnomalyDetectors.html">ListLogAnomalyDetectors</a> operation.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_log_anomaly_detector_request.GetLogAnomalyDetectorRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_log_anomaly_detector_response.GetLogAnomalyDetectorResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_log_anomaly_detector

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_log_anomaly_detector.get_log_anomaly_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_log_anomaly_detector_request.GetLogAnomalyDetectorRequest = {
            "anomaly_detector_arn": anomaly_detector_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_log_events(
        self,
        log_stream_name: "capo_cloudwatch_logs.types.log_stream_name.LogStreamName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
        start_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional["capo_cloudwatch_logs.types.events_limit.EventsLimit"] = None,
        start_from_head: Optional[
            "capo_cloudwatch_logs.types.start_from_head.StartFromHead"
        ] = None,
        unmask: Optional["capo_cloudwatch_logs.types.unmask.Unmask"] = None,
    ) -> "capo_cloudwatch_logs.types.get_log_events_response.GetLogEventsResponse":
        """<p>Lists log events from the specified log stream. You can list all of the log events or filter using a time range.</p> <p> <code>GetLogEvents</code> is a paginated operation. Each page returned can contain up to 1 MB of log events or up to 10,000 log events. A returned page might only be partially full, or even empty. For example, if the result of a query would return 15,000 log events, the first page isn't guaranteed to have 10,000 log events even if they all fit into 1 MB.</p> <p>Partially full or empty pages don't necessarily mean that pagination is finished. As long as the <code>nextBackwardToken</code> or <code>nextForwardToken</code> returned is NOT equal to the <code>nextToken</code> that you passed into the API call, there might be more log events available. The token that you use depends on the direction you want to move in along the log stream. The returned tokens are never null.</p> <note> <p>If you set <code>startFromHead</code> to <code>true</code> and you don’t include <code>endTime</code> in your request, you can end up in a situation where the pagination doesn't terminate. This can happen when the new log events are being added to the target log streams faster than they are being read. This situation is a good use case for the CloudWatch Logs <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html">Live Tail</a> feature.</p> </note> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p> <p>You can specify the log group to search by using either <code>logGroupIdentifier</code> or <code>logGroupName</code>. You must include one of these two parameters, but you can't include both. </p> <note> <p>If you are using <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html">log transformation</a>, the <code>GetLogEvents</code> operation returns only the original versions of log events, before they were transformed. To view the transformed versions, you must use a <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html">CloudWatch Logs query.</a> </p> </note>

        Args:
            log_group_name: <p>The name of the log group.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>
            log_group_identifier: <p>Specify either the name or ARN of the log group to view events from. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>
            log_stream_name: <p>The name of the log stream.</p>
            start_time: <p>The start of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp equal to this time or later than this time are included. Events with a timestamp earlier than this time are not included.</p> <note> <p>Set <code>startTime</code> explicitly to reduce the chances of empty pages in the response.</p> </note>
            end_time: <p>The end of the time range, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. Events with a timestamp equal to or later than this time are not included.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            limit: <p>The maximum number of log events returned. If you don't specify a limit, the default is as many log events as can fit in a response size of 1 MB (up to 10,000 log events).</p>
            start_from_head: <p>If the value is true, the earliest log events are returned first. If the value is false, the latest log events are returned first. The default value is false.</p> <p>If you are using a previous <code>nextForwardToken</code> value as the <code>nextToken</code> in this operation, you must specify <code>true</code> for <code>startFromHead</code>.</p>
            unmask: <p>Specify <code>true</code> to display the log event fields with all sensitive data unmasked and visible. The default is <code>false</code>.</p> <p>To use this operation with this parameter, you must be signed into an account with the <code>logs:Unmask</code> permission.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_log_events_request.GetLogEventsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_log_events_response.GetLogEventsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_log_events

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_log_events.get_log_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_log_events_request.GetLogEventsRequest = {
            "log_stream_name": log_stream_name
        }
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if log_group_identifier is not None:
            input_["log_group_identifier"] = log_group_identifier
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if start_from_head is not None:
            input_["start_from_head"] = start_from_head
        if unmask is not None:
            input_["unmask"] = unmask

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_get_log_events(
        self,
        log_stream_name: "capo_cloudwatch_logs.types.log_stream_name.LogStreamName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
        start_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        end_time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional["capo_cloudwatch_logs.types.events_limit.EventsLimit"] = None,
        start_from_head: Optional[
            "capo_cloudwatch_logs.types.start_from_head.StartFromHead"
        ] = None,
        unmask: Optional["capo_cloudwatch_logs.types.unmask.Unmask"] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.output_log_event.OutputLogEvent]":
        _token = next_token
        while True:
            _response = self.get_log_events(
                log_stream_name,
                config_overrides=config_overrides,
                log_group_name=log_group_name,
                log_group_identifier=log_group_identifier,
                start_time=start_time,
                end_time=end_time,
                next_token=_token,
                limit=limit,
                start_from_head=start_from_head,
                unmask=unmask,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_forward_token",))
            if not _token:
                break

    def get_log_fields(
        self,
        data_source_name: "capo_cloudwatch_logs.types.data_source_name.DataSourceName",
        data_source_type: "capo_cloudwatch_logs.types.data_source_type.DataSourceType",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_log_fields_response.GetLogFieldsResponse":
        """<p>Discovers available fields for a specific data source and type. The response includes any field modifications introduced through pipelines, such as new fields or changed field types. </p>

        Args:
            data_source_name: <p>The name of the data source to retrieve log fields for.</p>
            data_source_type: <p>The type of the data source to retrieve log fields for.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_log_fields_request.GetLogFieldsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_log_fields_response.GetLogFieldsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_log_fields

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_log_fields.get_log_fields(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_log_fields_request.GetLogFieldsRequest = {
            "data_source_name": data_source_name,
            "data_source_type": data_source_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_log_group_fields(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        time: Optional["capo_cloudwatch_logs.types.timestamp.Timestamp"] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.get_log_group_fields_response.GetLogGroupFieldsResponse":
        """<p>Returns a list of the fields that are included in log events in the specified log group. Includes the percentage of log events that contain each field. The search is limited to a time period that you specify.</p> <p>This operation is used for discovering fields within log group events. For discovering fields across data sources, use the GetLogFields operation.</p> <p>You can specify the log group to search by using either <code>logGroupIdentifier</code> or <code>logGroupName</code>. You must specify one of these parameters, but you can't specify both. </p> <p>In the results, fields that start with <code>@</code> are fields generated by CloudWatch Logs. For example, <code>@timestamp</code> is the timestamp of each log event. For more information about the fields that are generated by CloudWatch logs, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData-discoverable-fields.html">Supported Logs and Discovered Fields</a>.</p> <p>The response results are sorted by the frequency percentage, starting with the highest percentage.</p> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p>

        Args:
            log_group_name: <p>The name of the log group to search.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>
            time: <p>The time to set as the center of the query. If you specify <code>time</code>, the 8 minutes before and 8 minutes after this time are searched. If you omit <code>time</code>, the most recent 15 minutes up to the current time are searched.</p> <p>The <code>time</code> value is specified as epoch time, which is the number of seconds since <code>January 1, 1970, 00:00:00 UTC</code>.</p>
            log_group_identifier: <p>Specify either the name or ARN of the log group to view. If the log group is in a source account and you are using a monitoring account, you must specify the ARN.</p> <note> <p> You must include either <code>logGroupIdentifier</code> or <code>logGroupName</code>, but not both. </p> </note>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_log_group_fields_request.GetLogGroupFieldsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_log_group_fields_response.GetLogGroupFieldsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_log_group_fields

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_log_group_fields.get_log_group_fields(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_log_group_fields_request.GetLogGroupFieldsRequest = {}
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if time is not None:
            input_["time"] = time
        if log_group_identifier is not None:
            input_["log_group_identifier"] = log_group_identifier

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_log_object(
        self,
        log_object_pointer: "capo_cloudwatch_logs.types.log_object_pointer.LogObjectPointer",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        unmask: Optional["capo_cloudwatch_logs.types.unmask.Unmask"] = None,
    ) -> "capo_cloudwatch_logs.types.get_log_object_response.GetLogObjectResponse":
        """<p>Retrieves a large logging object (LLO) and streams it back. This API is used to fetch the content of large portions of log events that have been ingested through the PutOpenTelemetryLogs API. When log events contain fields that would cause the total event size to exceed 1MB, CloudWatch Logs automatically processes up to 10 fields, starting with the largest fields. Each field is truncated as needed to keep the total event size as close to 1MB as possible. The excess portions are stored as Large Log Objects (LLOs) and these fields are processed separately and LLO reference system fields (in the format <code>@ptr.$[path.to.field]</code>) are added. The path in the reference field reflects the original JSON structure where the large field was located. For example, this could be <code>@ptr.$['input']['message']</code>, <code>@ptr.$['AAA']['BBB']['CCC']['DDD']</code>, <code>@ptr.$['AAA']</code>, or any other path matching your log structure.</p> <note> <p>The <code>GetLogObject</code> API routes requests using SDK host prefix injection. SDK versions released before April 1, 2026 route to <code>streaming-logs.<i>Region</i>.amazonaws.com</code>, which does not support VPC endpoints. SDK versions released on or after April 1, 2026 route to <code>stream-logs.<i>Region</i>.amazonaws.com</code>, which supports VPC endpoints. To set up a VPC endpoint for this API, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html#create-VPC-endpoint-for-CloudWatchLogs">Creating a VPC endpoint for CloudWatch Logs </a>.</p> </note>

        Args:
            unmask: <p>A boolean flag that indicates whether to unmask sensitive log data. When set to true, any masked or redacted data in the log object will be displayed in its original form. Default is false.</p>
            log_object_pointer: <p>A pointer to the specific log object to retrieve. This is a required parameter that uniquely identifies the log object within CloudWatch Logs. The pointer is typically obtained from a previous query or filter operation.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_log_object_request.GetLogObjectRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_log_object_response.GetLogObjectResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_log_object

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_log_object.get_log_object(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_log_object_request.GetLogObjectRequest = {
            "log_object_pointer": log_object_pointer
        }
        if unmask is not None:
            input_["unmask"] = unmask

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def get_log_record(
        self,
        log_record_pointer: "capo_cloudwatch_logs.types.log_record_pointer.LogRecordPointer",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        unmask: Optional["capo_cloudwatch_logs.types.unmask.Unmask"] = None,
    ) -> "capo_cloudwatch_logs.types.get_log_record_response.GetLogRecordResponse":
        """<p>Retrieves all of the fields and values of a single log event. All fields are retrieved, even if the original query that produced the <code>logRecordPointer</code> retrieved only a subset of fields. Fields are returned as field name/field value pairs.</p> <p>The full unparsed log event is returned within <code>@message</code>.</p>

        Args:
            log_record_pointer: <p>The pointer corresponding to the log event record you want to retrieve. You get this from the response of a <code>GetQueryResults</code> operation. In that response, the value of the <code>@ptr</code> field for a log event is the value to use as <code>logRecordPointer</code> to retrieve that complete log event record.</p>
            unmask: <p>Specify <code>true</code> to display the log event fields with all sensitive data unmasked and visible. The default is <code>false</code>.</p> <p>To use this operation with this parameter, you must be signed into an account with the <code>logs:Unmask</code> permission.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_log_record_request.GetLogRecordRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_log_record_response.GetLogRecordResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_log_record

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_log_record.get_log_record(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_log_record_request.GetLogRecordRequest = {
            "log_record_pointer": log_record_pointer
        }
        if unmask is not None:
            input_["unmask"] = unmask

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_lookup_table(
        self,
        lookup_table_arn: "capo_cloudwatch_logs.types.arn.Arn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse":
        """<p>Retrieves the full content of a lookup table, including the CSV data.</p>

        Args:
            lookup_table_arn: <p>The ARN of the lookup table to retrieve.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_lookup_table_request.GetLookupTableRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_lookup_table_response.GetLookupTableResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_lookup_table

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_lookup_table.get_lookup_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_lookup_table_request.GetLookupTableRequest = {
            "lookup_table_arn": lookup_table_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_query_results(
        self,
        query_id: "capo_cloudwatch_logs.types.query_id.QueryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional[
            "capo_cloudwatch_logs.types.get_query_results_next_token.GetQueryResultsNextToken"
        ] = None,
        max_items: Optional[
            "capo_cloudwatch_logs.types.get_query_results_max_items.GetQueryResultsMaxItems"
        ] = None,
    ) -> (
        "capo_cloudwatch_logs.types.get_query_results_response.GetQueryResultsResponse"
    ):
        """<p>Returns the results from the specified query.</p> <p>Only the fields requested in the query are returned, along with a <code>@ptr</code> field, which is the identifier for the log record. You can use the value of <code>@ptr</code> in a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogRecord.html">GetLogRecord</a> operation to get the full log record.</p> <p> <code>GetQueryResults</code> does not start running a query. To run a query, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a>. For more information about how long results of previous queries are available, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.html">CloudWatch Logs quotas</a>.</p> <p>If the value of the <code>Status</code> field in the output is <code>Running</code>, this operation returns only partial results. If you see a value of <code>Scheduled</code> or <code>Running</code> for the status, you can retry the operation later to see the final results. </p> <p>This operation is used both for retrieving results from interactive queries and from automated scheduled query executions. Scheduled queries use <code>GetQueryResults</code> internally to retrieve query results for processing and delivery to configured destinations.</p> <p>You can retrieve up to 100,000 log event results from a query, if available, by using pagination. Use the <code>nextToken</code> returned in the response to request additional pages of results, with each page returning up to 10,000 log events. This is only supported for Logs Insights QL and is currently not supported for PPL and SQL query languages.</p> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account to start queries in linked source accounts. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p>

        Args:
            query_id: <p>The ID number of the query.</p>
            next_token: <p>The token for the next set of items to return. The token expires after 1 hour.</p>
            max_items: <p>The maximum number of log events to return in the response. The maximum is 10,000 log events per request. You can retrieve up to 100,000 log event results from a query by paginating with the <code>nextToken</code>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_query_results_request.GetQueryResultsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_query_results_response.GetQueryResultsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_query_results

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_query_results.get_query_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_query_results_request.GetQueryResultsRequest = {
            "query_id": query_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_items is not None:
            input_["max_items"] = max_items

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_scheduled_query(
        self,
        identifier: "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_scheduled_query_response.GetScheduledQueryResponse":
        """<p>Retrieves details about a specific scheduled query, including its configuration, execution status, and metadata.</p>

        Args:
            identifier: <p>The ARN or name of the scheduled query to retrieve.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_scheduled_query_request.GetScheduledQueryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_scheduled_query_response.GetScheduledQueryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_scheduled_query

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_scheduled_query.get_scheduled_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_scheduled_query_request.GetScheduledQueryRequest = {
            "identifier": identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_scheduled_query_history(
        self,
        identifier: "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier",
        start_time: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        end_time: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        execution_statuses: Optional[
            "capo_cloudwatch_logs.types.execution_status_list.ExecutionStatusList"
        ] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.get_scheduled_query_history_max_results.GetScheduledQueryHistoryMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.get_scheduled_query_history_response.GetScheduledQueryHistoryResponse":
        """<p>Retrieves the execution history of a scheduled query within a specified time range, including query results and destination processing status.</p>

        Args:
            identifier: <p>The ARN or name of the scheduled query to retrieve history for.</p>
            start_time: <p>The start time for the history query in Unix epoch format.</p>
            end_time: <p>The end time for the history query in Unix epoch format.</p>
            execution_statuses: <p>An array of execution statuses to filter the history results. Only executions with the specified statuses are returned.</p>
            max_results: <p>The maximum number of history records to return. Valid range is 1 to 1000.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_scheduled_query_history_request.GetScheduledQueryHistoryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_scheduled_query_history_response.GetScheduledQueryHistoryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_scheduled_query_history

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_scheduled_query_history.get_scheduled_query_history(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_scheduled_query_history_request.GetScheduledQueryHistoryRequest = {
            "identifier": identifier,
            "start_time": start_time,
            "end_time": end_time,
        }
        if execution_statuses is not None:
            input_["execution_statuses"] = execution_statuses
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

    def iter_get_scheduled_query_history(
        self,
        identifier: "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier",
        start_time: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        end_time: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        execution_statuses: Optional[
            "capo_cloudwatch_logs.types.execution_status_list.ExecutionStatusList"
        ] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.get_scheduled_query_history_max_results.GetScheduledQueryHistoryMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.trigger_history_record.TriggerHistoryRecord]":
        _token = next_token
        while True:
            _response = self.get_scheduled_query_history(
                identifier,
                start_time,
                end_time,
                config_overrides=config_overrides,
                execution_statuses=execution_statuses,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("trigger_history",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_storage_tier_policy(
        self, *, config_overrides: Optional[CloudWatchLogsClientConfig] = None
    ) -> "capo_cloudwatch_logs.types.get_storage_tier_policy_response.GetStorageTierPolicyResponse":
        """<p>Returns the storage tier policy for the account.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_storage_tier_policy_request.GetStorageTierPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_storage_tier_policy_response.GetStorageTierPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_storage_tier_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_storage_tier_policy.get_storage_tier_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_storage_tier_policy_request.GetStorageTierPolicyRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_transformer(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.get_transformer_response.GetTransformerResponse":
        """<p>Returns the information about the log transformer associated with this log group.</p> <p>This operation returns data only for transformers created at the log group level. To get information for an account-level transformer, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeAccountPolicies.html">DescribeAccountPolicies</a>.</p>

        Args:
            log_group_identifier: <p>Specify either the name or ARN of the log group to return transformer information for. If the log group is in a source account and you are using a monitoring account, you must use the log group ARN.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.get_transformer_request.GetTransformerRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.get_transformer_response.GetTransformerResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.get_transformer

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.get_transformer.get_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.get_transformer_request.GetTransformerRequest = {
            "log_group_identifier": log_group_identifier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_aggregate_log_group_summaries(
        self,
        group_by: "capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by.ListAggregateLogGroupSummariesGroupBy",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        account_identifiers: Optional[
            "capo_cloudwatch_logs.types.account_ids.AccountIds"
        ] = None,
        include_linked_accounts: Optional[
            "capo_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
        ] = None,
        log_group_class: Optional[
            "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
        ] = None,
        log_group_name_pattern: Optional[
            "capo_cloudwatch_logs.types.log_group_name_regex_pattern.LogGroupNameRegexPattern"
        ] = None,
        data_sources: Optional[
            "capo_cloudwatch_logs.types.data_source_filters.DataSourceFilters"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.list_log_groups_request_limit.ListLogGroupsRequestLimit"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_response.ListAggregateLogGroupSummariesResponse":
        """<p>Returns an aggregate summary of all log groups in the Region grouped by specified data source characteristics. Supports optional filtering by log group class, name patterns, and data sources. If you perform this action in a monitoring account, you can also return aggregated summaries of log groups from source accounts that are linked to the monitoring account. For more information about using cross-account observability to set up monitoring accounts and source accounts, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>.</p> <p>The operation aggregates log groups by data source name and type and optionally format, providing counts of log groups that share these characteristics. The operation paginates results. By default, it returns up to 50 results and includes a token to retrieve more results.</p>

        Args:
            account_identifiers: <p>When <code>includeLinkedAccounts</code> is set to <code>true</code>, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.</p>
            include_linked_accounts: <p>If you are using a monitoring account, set this to <code>true</code> to have the operation return log groups in the accounts listed in <code>accountIdentifiers</code>.</p> <p>If this parameter is set to <code>true</code> and <code>accountIdentifiers</code> contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account. </p> <p>The default for this parameter is <code>false</code>.</p>
            log_group_class: <p>Filters the results by log group class to include only log groups of the specified class.</p>
            log_group_name_pattern: <p>Use this parameter to limit the returned log groups to only those with names that match the pattern that you specify. This parameter is a regular expression that can match prefixes and substrings, and supports wildcard matching and matching multiple patterns, as in the following examples. </p> <ul> <li> <p>Use <code>^</code> to match log group names by prefix.</p> </li> <li> <p>For a substring match, specify the string to match. All matches are case sensitive</p> </li> <li> <p>To match multiple patterns, separate them with a <code>|</code> as in the example <code>^/aws/lambda|discovery</code> </p> </li> </ul> <p>You can specify as many as five different regular expression patterns in this field, each of which must be between 3 and 24 characters. You can include the <code>^</code> symbol as many as five times, and include the <code>|</code> symbol as many as four times.</p>
            data_sources: <p>Filters the results by data source characteristics to include only log groups associated with the specified data sources.</p>
            group_by: <p>Specifies how to group the log groups in the summary.</p>
            limit: <p>The maximum number of aggregated summaries to return. If you omit this parameter, the default is up to 50 aggregated summaries.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_request.ListAggregateLogGroupSummariesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_response.ListAggregateLogGroupSummariesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_aggregate_log_group_summaries

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_aggregate_log_group_summaries.list_aggregate_log_group_summaries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_request.ListAggregateLogGroupSummariesRequest = {
            "group_by": group_by
        }
        if account_identifiers is not None:
            input_["account_identifiers"] = account_identifiers
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if log_group_class is not None:
            input_["log_group_class"] = log_group_class
        if log_group_name_pattern is not None:
            input_["log_group_name_pattern"] = log_group_name_pattern
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_aggregate_log_group_summaries(
        self,
        group_by: "capo_cloudwatch_logs.types.list_aggregate_log_group_summaries_group_by.ListAggregateLogGroupSummariesGroupBy",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        account_identifiers: Optional[
            "capo_cloudwatch_logs.types.account_ids.AccountIds"
        ] = None,
        include_linked_accounts: Optional[
            "capo_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
        ] = None,
        log_group_class: Optional[
            "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
        ] = None,
        log_group_name_pattern: Optional[
            "capo_cloudwatch_logs.types.log_group_name_regex_pattern.LogGroupNameRegexPattern"
        ] = None,
        data_sources: Optional[
            "capo_cloudwatch_logs.types.data_source_filters.DataSourceFilters"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.list_log_groups_request_limit.ListLogGroupsRequestLimit"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.aggregate_log_group_summary.AggregateLogGroupSummary]":
        _token = next_token
        while True:
            _response = self.list_aggregate_log_group_summaries(
                group_by,
                config_overrides=config_overrides,
                account_identifiers=account_identifiers,
                include_linked_accounts=include_linked_accounts,
                log_group_class=log_group_class,
                log_group_name_pattern=log_group_name_pattern,
                data_sources=data_sources,
                next_token=_token,
                limit=limit,
            )
            _page = _resolve_path(_response, ("aggregate_log_group_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_anomalies(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        anomaly_detector_arn: Optional[
            "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
        ] = None,
        suppression_state: Optional[
            "capo_cloudwatch_logs.types.suppression_state.SuppressionState"
        ] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.list_anomalies_limit.ListAnomaliesLimit"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.list_anomalies_response.ListAnomaliesResponse":
        """<p>Returns a list of anomalies that log anomaly detectors have found. For details about the structure format of each anomaly object that is returned, see the example in this section.</p>

        Args:
            anomaly_detector_arn: <p>Use this to optionally limit the results to only the anomalies found by a certain anomaly detector.</p>
            suppression_state: <p>You can specify this parameter if you want to the operation to return only anomalies that are currently either suppressed or unsuppressed.</p>
            limit: <p>The maximum number of items to return. If you don't specify a value, the default maximum value of 50 items is used.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_anomalies_request.ListAnomaliesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_anomalies_response.ListAnomaliesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_anomalies

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_anomalies.list_anomalies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_anomalies_request.ListAnomaliesRequest = {}
        if anomaly_detector_arn is not None:
            input_["anomaly_detector_arn"] = anomaly_detector_arn
        if suppression_state is not None:
            input_["suppression_state"] = suppression_state
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_anomalies(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        anomaly_detector_arn: Optional[
            "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn"
        ] = None,
        suppression_state: Optional[
            "capo_cloudwatch_logs.types.suppression_state.SuppressionState"
        ] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.list_anomalies_limit.ListAnomaliesLimit"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.anomaly.Anomaly]":
        _token = next_token
        while True:
            _response = self.list_anomalies(
                config_overrides=config_overrides,
                anomaly_detector_arn=anomaly_detector_arn,
                suppression_state=suppression_state,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("anomalies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_integrations(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        integration_name_prefix: Optional[
            "capo_cloudwatch_logs.types.integration_name_prefix.IntegrationNamePrefix"
        ] = None,
        integration_type: Optional[
            "capo_cloudwatch_logs.types.integration_type.IntegrationType"
        ] = None,
        integration_status: Optional[
            "capo_cloudwatch_logs.types.integration_status.IntegrationStatus"
        ] = None,
    ) -> (
        "capo_cloudwatch_logs.types.list_integrations_response.ListIntegrationsResponse"
    ):
        """<p>Returns a list of integrations between CloudWatch Logs and other services in this account. Currently, only one integration can be created in an account, and this integration must be with OpenSearch Service.</p>

        Args:
            integration_name_prefix: <p>To limit the results to integrations that start with a certain name prefix, specify that name prefix here.</p>
            integration_type: <p>To limit the results to integrations of a certain type, specify that type here.</p>
            integration_status: <p>To limit the results to integrations with a certain status, specify that status here.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_integrations_request.ListIntegrationsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_integrations_response.ListIntegrationsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_integrations

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_integrations.list_integrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_integrations_request.ListIntegrationsRequest = {}
        if integration_name_prefix is not None:
            input_["integration_name_prefix"] = integration_name_prefix
        if integration_type is not None:
            input_["integration_type"] = integration_type
        if integration_status is not None:
            input_["integration_status"] = integration_status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_log_anomaly_detectors(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        filter_log_group_arn: Optional[
            "capo_cloudwatch_logs.types.log_group_arn.LogGroupArn"
        ] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.list_log_anomaly_detectors_limit.ListLogAnomalyDetectorsLimit"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.list_log_anomaly_detectors_response.ListLogAnomalyDetectorsResponse":
        """<p>Retrieves a list of the log anomaly detectors in the account.</p>

        Args:
            filter_log_group_arn: <p>Use this to optionally filter the results to only include anomaly detectors that are associated with the specified log group.</p>
            limit: <p>The maximum number of items to return. If you don't specify a value, the default maximum value of 50 items is used.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_log_anomaly_detectors_request.ListLogAnomalyDetectorsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_log_anomaly_detectors_response.ListLogAnomalyDetectorsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_log_anomaly_detectors

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_log_anomaly_detectors.list_log_anomaly_detectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_log_anomaly_detectors_request.ListLogAnomalyDetectorsRequest = {}
        if filter_log_group_arn is not None:
            input_["filter_log_group_arn"] = filter_log_group_arn
        if limit is not None:
            input_["limit"] = limit
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_log_anomaly_detectors(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        filter_log_group_arn: Optional[
            "capo_cloudwatch_logs.types.log_group_arn.LogGroupArn"
        ] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.list_log_anomaly_detectors_limit.ListLogAnomalyDetectorsLimit"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.anomaly_detector.AnomalyDetector]":
        _token = next_token
        while True:
            _response = self.list_log_anomaly_detectors(
                config_overrides=config_overrides,
                filter_log_group_arn=filter_log_group_arn,
                limit=limit,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("anomaly_detectors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_log_groups(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_name_pattern: Optional[
            "capo_cloudwatch_logs.types.log_group_name_regex_pattern.LogGroupNameRegexPattern"
        ] = None,
        log_group_class: Optional[
            "capo_cloudwatch_logs.types.log_group_class.LogGroupClass"
        ] = None,
        include_linked_accounts: Optional[
            "capo_cloudwatch_logs.types.include_linked_accounts.IncludeLinkedAccounts"
        ] = None,
        account_identifiers: Optional[
            "capo_cloudwatch_logs.types.account_ids.AccountIds"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        limit: Optional["capo_cloudwatch_logs.types.list_limit.ListLimit"] = None,
        data_sources: Optional[
            "capo_cloudwatch_logs.types.data_source_filters.DataSourceFilters"
        ] = None,
        field_index_names: Optional[
            "capo_cloudwatch_logs.types.field_index_names.FieldIndexNames"
        ] = None,
        log_group_tags: Optional[
            "capo_cloudwatch_logs.types.tag_filters.TagFilters"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.list_log_groups_response.ListLogGroupsResponse":
        """<p>Returns a list of log groups in the Region in your account. If you are performing this action in a monitoring account, you can choose to also return log groups from source accounts that are linked to the monitoring account. For more information about using cross-account observability to set up monitoring accounts and source accounts, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html"> CloudWatch cross-account observability</a>.</p> <p>You can optionally filter the results by log group class, log group name pattern, field indexes, data sources, field index names, or log group tags. If you specify more than one filter type, the results include log groups that satisfy all filters.</p> <p>This operation is paginated. By default, your first use of this operation returns 50 results, and includes a token to use in a subsequent operation to return more results.</p>

        Args:
            log_group_name_pattern: <p>Use this parameter to limit the returned log groups to only those with names that match the pattern that you specify. This parameter is a regular expression that can match prefixes and substrings, and supports wildcard matching and matching multiple patterns, as in the following examples. </p> <ul> <li> <p>Use <code>^</code> to match log group names by prefix.</p> </li> <li> <p>For a substring match, specify the string to match. All matches are case sensitive</p> </li> <li> <p>To match multiple patterns, separate them with a <code>|</code> as in the example <code>^/aws/lambda|discovery</code> </p> </li> </ul> <p>You can specify as many as five different regular expression patterns in this field, each of which must be between 3 and 24 characters. You can include the <code>^</code> symbol as many as five times, and include the <code>|</code> symbol as many as four times.</p>
            log_group_class: <p>Use this parameter to limit the results to only those log groups in the specified log group class. If you omit this parameter, log groups of all classes can be returned.</p>
            include_linked_accounts: <p>If you are using a monitoring account, set this to <code>true</code> to have the operation return log groups in the accounts listed in <code>accountIdentifiers</code>.</p> <p>If this parameter is set to <code>true</code> and <code>accountIdentifiers</code> contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account. </p> <p>The default for this parameter is <code>false</code>.</p>
            account_identifiers: <p>When <code>includeLinkedAccounts</code> is set to <code>true</code>, use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.</p>
            limit: <p>The maximum number of log groups to return. If you omit this parameter, the default is up to 50 log groups.</p>
            data_sources: <p>An array of data source filters to filter log groups by their associated data sources. You can filter by data source name, type, or both. Multiple filters within the same dimension are combined with OR logic, while filters across different dimensions are combined with AND logic.</p>
            field_index_names: <p>An array of field index names to filter log groups that have specific field indexes. Only log groups containing all specified field indexes are returned. You can specify 1 to 20 field index names, each with 1 to 512 characters.</p>
            log_group_tags: <p>An array of tag filters to return only log groups that have specific tags. Multiple filters are combined with AND logic.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_log_groups_request.ListLogGroupsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_log_groups_response.ListLogGroupsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_log_groups

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_log_groups.list_log_groups(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_log_groups_request.ListLogGroupsRequest = {}
        if log_group_name_pattern is not None:
            input_["log_group_name_pattern"] = log_group_name_pattern
        if log_group_class is not None:
            input_["log_group_class"] = log_group_class
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if account_identifiers is not None:
            input_["account_identifiers"] = account_identifiers
        if next_token is not None:
            input_["next_token"] = next_token
        if limit is not None:
            input_["limit"] = limit
        if data_sources is not None:
            input_["data_sources"] = data_sources
        if field_index_names is not None:
            input_["field_index_names"] = field_index_names
        if log_group_tags is not None:
            input_["log_group_tags"] = log_group_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_log_groups_for_query(
        self,
        query_id: "capo_cloudwatch_logs.types.query_id.QueryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.list_log_groups_for_query_max_results.ListLogGroupsForQueryMaxResults"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.list_log_groups_for_query_response.ListLogGroupsForQueryResponse":
        """<p>Returns a list of the log groups that were analyzed during a single CloudWatch Logs Insights query. This can be useful for queries that use log group name prefixes or the <code>filterIndex</code> command, because the log groups are dynamically selected in these cases.</p> <p>For more information about field indexes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html">Create field indexes to improve query performance and reduce costs</a>.</p>

        Args:
            query_id: <p>The ID of the query to use. This query ID is from the response to your <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a> operation.</p>
            max_results: <p>Limits the number of returned log groups to the specified number.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_log_groups_for_query_request.ListLogGroupsForQueryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_log_groups_for_query_response.ListLogGroupsForQueryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_log_groups_for_query

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_log_groups_for_query.list_log_groups_for_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_log_groups_for_query_request.ListLogGroupsForQueryRequest = {
            "query_id": query_id
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

    def iter_list_log_groups_for_query(
        self,
        query_id: "capo_cloudwatch_logs.types.query_id.QueryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.list_log_groups_for_query_max_results.ListLogGroupsForQueryMaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier]":
        _token = next_token
        while True:
            _response = self.list_log_groups_for_query(
                query_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("log_group_identifiers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_scheduled_queries(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.list_scheduled_queries_max_results.ListScheduledQueriesMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
        ] = None,
        schedule_type: Optional[
            "capo_cloudwatch_logs.types.schedule_type.ScheduleType"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.list_scheduled_queries_response.ListScheduledQueriesResponse":
        """<p>Lists all scheduled queries in your account and region. You can filter results by state to show only enabled or disabled queries.</p>

        Args:
            max_results: <p>The maximum number of scheduled queries to return. Valid range is 1 to 1000.</p>
            state: <p>Filter scheduled queries by state. Valid values are <code>ENABLED</code> and <code>DISABLED</code>. If not specified, all scheduled queries are returned.</p>
            schedule_type: <p>Filter scheduled queries by schedule type. Valid values are <code>CUSTOMER_MANAGED</code> and <code>AWS_MANAGED</code>. If not specified, scheduled queries of all schedule types are returned.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_scheduled_queries_request.ListScheduledQueriesRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_scheduled_queries_response.ListScheduledQueriesResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_scheduled_queries

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_scheduled_queries.list_scheduled_queries(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_scheduled_queries_request.ListScheduledQueriesRequest = {}
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if state is not None:
            input_["state"] = state
        if schedule_type is not None:
            input_["schedule_type"] = schedule_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_scheduled_queries(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.list_scheduled_queries_max_results.ListScheduledQueriesMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        state: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
        ] = None,
        schedule_type: Optional[
            "capo_cloudwatch_logs.types.schedule_type.ScheduleType"
        ] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.scheduled_query_summary.ScheduledQuerySummary]":
        _token = next_token
        while True:
            _response = self.list_scheduled_queries(
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                state=state,
                schedule_type=schedule_type,
            )
            _page = _resolve_path(_response, ("scheduled_queries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sources_for_s3_table_integration(
        self,
        integration_arn: "capo_cloudwatch_logs.types.arn.Arn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_max_results.ListSourcesForS3TableIntegrationMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_response.ListSourcesForS3TableIntegrationResponse":
        """<p>Returns a list of data source associations for a specified S3 Table Integration, showing which data sources are currently associated for query access.</p>

        Args:
            integration_arn: <p>The Amazon Resource Name (ARN) of the S3 Table Integration to list associations for.</p>
            max_results: <p>The maximum number of associations to return in a single call. Valid range is 1 to 100.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_request.ListSourcesForS3TableIntegrationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_response.ListSourcesForS3TableIntegrationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_sources_for_s3_table_integration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_sources_for_s3_table_integration.list_sources_for_s3_table_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_request.ListSourcesForS3TableIntegrationRequest = {
            "integration_arn": integration_arn
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

    def iter_list_sources_for_s3_table_integration(
        self,
        integration_arn: "capo_cloudwatch_logs.types.arn.Arn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.list_sources_for_s3_table_integration_max_results.ListSourcesForS3TableIntegrationMaxResults"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudwatch_logs.types.s3_table_integration_source.S3TableIntegrationSource]":
        _token = next_token
        while True:
            _response = self.list_sources_for_s3_table_integration(
                integration_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_syslog_configurations(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_group_identifier: Optional[
            "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier"
        ] = None,
        vpc_endpoint_id: Optional[
            "capo_cloudwatch_logs.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
        next_token: Optional["capo_cloudwatch_logs.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudwatch_logs.types.list_syslog_configurations_max_results.ListSyslogConfigurationsMaxResults"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.list_syslog_configurations_response.ListSyslogConfigurationsResponse":
        """<p>Returns a list of syslog configurations. You can optionally filter the results by log group or VPC endpoint.</p>

        Args:
            log_group_identifier: <p>The name or ARN of the log group to filter syslog configurations for.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint to filter syslog configurations for.</p>
            next_token: <p>The token for the next set of items to return. You received this token from a previous call.</p>
            max_results: <p>The maximum number of syslog configurations to return in the response.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_syslog_configurations_request.ListSyslogConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_syslog_configurations_response.ListSyslogConfigurationsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_syslog_configurations

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_syslog_configurations.list_syslog_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_syslog_configurations_request.ListSyslogConfigurationsRequest = {}
        if log_group_identifier is not None:
            input_["log_group_identifier"] = log_group_identifier
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_cloudwatch_logs.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with a CloudWatch Logs resource. Currently, log groups and destinations support tagging.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you want to view tags for.</p> <p>The ARN format of a log group is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:log-group:<i>log-group-name</i> </code> </p> <p>The ARN format of a destination is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:destination:<i>destination-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_tags_for_resource

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_tags_log_group(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.list_tags_log_group_response.ListTagsLogGroupResponse":
        """<important> <p>The ListTagsLogGroup operation is on the path to deprecation. We recommend that you use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html">ListTagsForResource</a> instead.</p> </important> <p>Lists the tags for the specified log group.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>

        Raises:
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.list_tags_log_group_request.ListTagsLogGroupRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.list_tags_log_group_response.ListTagsLogGroupResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.list_tags_log_group

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.list_tags_log_group.list_tags_log_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.list_tags_log_group_request.ListTagsLogGroupRequest = {
            "log_group_name": log_group_name
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_account_policy(
        self,
        policy_name: "capo_cloudwatch_logs.types.policy_name.PolicyName",
        policy_document: "capo_cloudwatch_logs.types.account_policy_document.AccountPolicyDocument",
        policy_type: "capo_cloudwatch_logs.types.policy_type.PolicyType",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        scope: Optional["capo_cloudwatch_logs.types.scope.Scope"] = None,
        selection_criteria: Optional[
            "capo_cloudwatch_logs.types.selection_criteria.SelectionCriteria"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.put_account_policy_response.PutAccountPolicyResponse":
        r"""<p>Creates an account-level data protection policy, subscription filter policy, field index policy, transformer policy, or metric extraction policy that applies to all log groups, a subset of log groups, or a data source name and type combination in the account. Account-level policies are Region-specific: a policy applies only to log groups in the Region where you create it. To apply a policy across multiple Regions, create the policy separately in each Region.</p> <important> <p> <code>PutAccountPolicy</code> is an account-wide administrative operation intended for CloudWatch Logs administrators. Because it affects all log groups (or a broad subset) in the account, you should grant <code>logs:PutAccountPolicy</code> permissions only to administrators who manage logging configuration across the account, not to application teams or individual log group owners.</p> </important> <p> <b>Conflict resolution between account-level and log-group-level policies</b> </p> <p>When both an account-level policy and a log-group-level policy of the same type apply to a log group, the resolution depends on the policy type:</p> <ul> <li> <p> <i>Data protection</i> — The two policies are cumulative. Any sensitive term specified in either the account-level or the log-group-level policy is masked.</p> </li> <li> <p> <i>Subscription filters</i> — Account-level and log-group-level subscription filters are additive. A log group can have up to 1 account-level and up to 2 log-group-level subscription filters.</p> </li> <li> <p> <i>Transformers</i> — A log-group-level transformer overrides the account-level transformer. If a log group has its own transformer, it ignores the account-level transformer policy.</p> </li> <li> <p> <i>Field index policies</i> — If a log group has its own field index policy (created with <code>PutIndexPolicy</code>), any account-level policy that uses <code>LogGroupNamePrefix</code> selection criteria or has no selection criteria is ignored for that log group. However, account-level policies that use <code>DataSourceName</code> and <code>DataSourceType</code> selection criteria still apply alongside the log-group-level policy.</p> </li> <li> <p> <i>Metric extraction policies</i> — Metric extraction policies are account-level only and have no log-group-level equivalent, so no conflict resolution applies.</p> </li> </ul> <p>For field index policies, you can configure indexed fields as <i>facets</i> to enable interactive exploration of your logs. Facets provide value distributions and counts for indexed fields in the CloudWatch Logs Insights console without requiring query execution. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Facets.html">Use facets to group and explore logs</a>.</p> <p>To use this operation, you must be signed on with the correct permissions depending on the type of policy that you are creating.</p> <ul> <li> <p>To create a data protection policy, you must have the <code>logs:PutDataProtectionPolicy</code> and <code>logs:PutAccountPolicy</code> permissions.</p> </li> <li> <p>To create a subscription filter policy, you must have the <code>logs:PutSubscriptionFilter</code> and <code>logs:PutAccountPolicy</code> permissions.</p> </li> <li> <p>To create a transformer policy, you must have the <code>logs:PutTransformer</code> and <code>logs:PutAccountPolicy</code> permissions.</p> </li> <li> <p>To create a field index policy, you must have the <code>logs:PutIndexPolicy</code> and <code>logs:PutAccountPolicy</code> permissions.</p> </li> <li> <p>To configure facets for field index policies, you must have the <code>logs:PutIndexPolicy</code> and <code>logs:PutAccountPolicy</code> permissions.</p> </li> <li> <p>To create a metric extraction policy, you must have the <code>logs:PutMetricExtractionPolicy</code> and <code>logs:PutAccountPolicy</code> permissions.</p> </li> </ul> <p> <b>Data protection policy</b> </p> <p>A data protection policy can help safeguard sensitive data that's ingested by your log groups by auditing and masking the sensitive log data. Each account can have only one account-level data protection policy.</p> <important> <p>Sensitive data is detected and masked when it is ingested into a log group. When you set a data protection policy, log events ingested into the log groups before that time are not masked.</p> </important> <p>If you use <code>PutAccountPolicy</code> to create a data protection policy for your whole account, it applies to both existing log groups and all log groups that are created later in this account. The account-level policy is applied to existing log groups with eventual consistency. It might take up to 5 minutes before sensitive data in existing log groups begins to be masked.</p> <p>By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the <code>logs:Unmask</code> permission can use a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html">GetLogEvents</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html">FilterLogEvents</a> operation with the <code>unmask</code> parameter set to <code>true</code> to view the unmasked log events. Users with the <code>logs:Unmask</code> can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the <code>unmask</code> query command.</p> <p>For more information, including a list of types of data that can be audited and masked, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html">Protect sensitive log data with masking</a>.</p> <p>To use the <code>PutAccountPolicy</code> operation for a data protection policy, you must be signed on with the <code>logs:PutDataProtectionPolicy</code> and <code>logs:PutAccountPolicy</code> permissions.</p> <p>The <code>PutAccountPolicy</code> operation applies to all log groups in the account. You can use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html">PutDataProtectionPolicy</a> to create a data protection policy that applies to just one log group. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.</p> <p> <b>Subscription filter policy</b> </p> <p>A subscription filter policy sets up a real-time feed of log events from CloudWatch Logs to other Amazon Web Services services. Account-level subscription filter policies apply to both existing log groups and log groups that are created later in this account. Supported destinations are Kinesis Data Streams, Firehose, and Lambda. When log events are sent to the receiving service, they are Base64 encoded and compressed with the GZIP format.</p> <p>The following destinations are supported for subscription filters:</p> <ul> <li> <p>An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.</p> </li> <li> <p>An Firehose data stream in the same account as the subscription policy, for same-account delivery.</p> </li> <li> <p>A Lambda function in the same account as the subscription policy, for same-account delivery.</p> </li> <li> <p>A logical destination in a different account created with <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html">PutDestination</a>, for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.</p> </li> </ul> <p>Each account can have one account-level subscription filter policy per Region. If you are updating an existing filter, you must specify the correct name in <code>PolicyName</code>. To perform a <code>PutAccountPolicy</code> subscription filter operation for any destination except a Lambda function, you must also have the <code>iam:PassRole</code> permission.</p> <p> <b>Transformer policy</b> </p> <p>Creates or updates a <i>log transformer policy</i> for your account. You use log transformers to transform log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contain relevant, source-specific information. After you have created a transformer, CloudWatch Logs performs this transformation at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filters.</p> <p>You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.</p> <p>A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. For more information about the available processors to use in a transformer, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors"> Processors that you can use</a>.</p> <p>Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major Amazon Web Services log sources such as VPC flow logs, Lambda, and Amazon RDS. You can use pre-built transformation templates or create custom transformation policies.</p> <p>You can create transformers only for the log groups in the Standard log class.</p> <p>You can have one account-level transformer policy that applies to all log groups in the account. Or you can create as many as 20 account-level transformer policies that are each scoped to a subset of log groups with the <code>selectionCriteria</code> parameter. If you have multiple account-level transformer policies with selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with <code>my-log</code>, you can't have another transformer policy filtered to <code>my-logpprod</code> or <code>my-logging</code>.</p> <p>You can also set up a transformer at the log-group level. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html">PutTransformer</a>. If there is both a log-group level transformer created with <code>PutTransformer</code> and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.</p> <p> <b>Field index policy</b> </p> <p>You can use field index policies to create indexes on fields found in log events for a log group or data source name and type combination. Creating field indexes can help lower the scan volume for CloudWatch Logs Insights queries that reference those fields, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields or values that match only a small fraction of the total log events. Common examples of indexes include request ID, session ID, user IDs, or instance IDs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html">Create field indexes to improve query performance and reduce costs</a> </p> <p>To find the fields that are in your log group events, use the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.html">GetLogGroupFields</a> operation. To find the fields for a data source use the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogFields.html">GetLogFields</a> operation.</p> <p>For example, suppose you have created a field index for <code>requestId</code>. Then, any CloudWatch Logs Insights query on that log group that includes <code>requestId = <i>value</i> </code> or <code>requestId in [<i>value</i>, <i>value</i>, ...]</code> will attempt to process only the log events where the indexed field matches the specified value.</p> <p>Matches of log events to the names of indexed fields are case-sensitive. For example, an indexed field of <code>RequestId</code> won't match a log event containing <code>requestId</code>.</p> <p>You can have one account-level field index policy that applies to all log groups in the account. Or you can create as many as 20 account-level field index policies that are each scoped to a subset of log groups using <code>LogGroupNamePrefix</code> with the <code>selectionCriteria</code> parameter. You can have another 20 account-level field index policies using <code>DataSourceName</code> and <code>DataSourceType</code> for the <code>selectionCriteria</code> parameter. If you have multiple account-level index policies with <code>LogGroupNamePrefix</code> selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with <i>my-log</i>, you can't have another field index policy filtered to <i>my-logpprod</i> or <i>my-logging</i>. Similarly, if you have multiple account-level index policies with <code>DataSourceName</code> and <code>DataSourceType</code> selection criteria, no two of them can use the same data source name and type combination. For example, if you have one policy filtered to the data source name <code>amazon_vpc</code> and data source type <code>flow</code> you cannot create another policy with this combination.</p> <p>If you create an account-level field index policy in a monitoring account in cross-account observability, the policy is applied only to the monitoring account and not to any source accounts.</p> <p>CloudWatch Logs provides default field indexes for all log groups in the Standard log class. Default field indexes are automatically available for the following fields: </p> <ul> <li> <p> <code>@logStream</code> </p> </li> <li> <p> <code>@aws.region</code> </p> </li> <li> <p> <code>@aws.account</code> </p> </li> <li> <p> <code>@source.log</code> </p> </li> <li> <p> <code>@data_source_name</code> </p> </li> <li> <p> <code>@data_source_type</code> </p> </li> <li> <p> <code>@data_format</code> </p> </li> <li> <p> <code>traceId</code> </p> </li> <li> <p> <code>severityText</code> </p> </li> <li> <p> <code>attributes.session.id</code> </p> </li> </ul> <p>CloudWatch Logs provides default field indexes for certain data source name and type combinations as well. Default field indexes are automatically available for the following data source name and type combinations as identified in the following list:</p> <p> <code>amazon_vpc.flow</code> </p> <ul> <li> <p> <code>action</code> </p> </li> <li> <p> <code>logStatus</code> </p> </li> <li> <p> <code>region</code> </p> </li> <li> <p> <code>flowDirection</code> </p> </li> <li> <p> <code>type</code> </p> </li> </ul> <p> <code>amazon_route53.resolver_query</code> </p> <ul> <li> <p> <code>transport</code> </p> </li> <li> <p> <code>rcode</code> </p> </li> </ul> <p> <code>aws_waf.access</code> </p> <ul> <li> <p> <code>action</code> </p> </li> <li> <p> <code>httpRequest.country</code> </p> </li> </ul> <p> <code>aws_cloudtrail.data</code>, <code>aws_cloudtrail.management</code> </p> <ul> <li> <p> <code>eventSource</code> </p> </li> <li> <p> <code>eventName</code> </p> </li> <li> <p> <code>awsRegion</code> </p> </li> <li> <p> <code>userAgent</code> </p> </li> <li> <p> <code>errorCode</code> </p> </li> <li> <p> <code>eventType</code> </p> </li> <li> <p> <code>managementEvent</code> </p> </li> <li> <p> <code>readOnly</code> </p> </li> <li> <p> <code>eventCategory</code> </p> </li> <li> <p> <code>requestId</code> </p> </li> </ul> <p>Default field indexes are in addition to any custom field indexes you define within your policy. Default field indexes are not counted towards your <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Syntax">field index quota</a>. </p> <p>If you want to create a field index policy for a single log group, you can use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html">PutIndexPolicy</a> instead of <code>PutAccountPolicy</code>. If you do so, that log group will use that log-group level policy and any account-level policies that match at the data source level; any account-level policy that matches at the log group level (for example, no selection criteria or log group name prefix selection criteria) will be ignored.</p> <p> <b>Metric extraction policy</b> </p> <p>A metric extraction policy controls whether CloudWatch Metrics can be created through the Embedded Metrics Format (EMF) for log groups in your account. By default, EMF metric creation is enabled for all log groups. You can use metric extraction policies to disable EMF metric creation for your entire account or specific log groups.</p> <p>When a policy disables EMF metric creation for a log group, log events in the EMF format are still ingested, but no CloudWatch Metrics are created from them.</p> <important> <p>Creating a policy disables metrics for Amazon Web Services features that use EMF to create metrics, such as CloudWatch Container Insights and CloudWatch Application Signals. To prevent turning off those features by accident, we recommend that you exclude the underlying log-groups through a selection-criteria such as <code>LogGroupNamePrefix NOT IN ["/aws/containerinsights", "/aws/ecs/containerinsights", "/aws/application-signals/data"]</code>.</p> </important> <p>Each account can have either one account-level metric extraction policy that applies to all log groups, or up to 5 policies that are each scoped to a subset of log groups with the <code>selectionCriteria</code> parameter. The selection criteria supports filtering by <code>LogGroupName</code> and <code>LogGroupNamePrefix</code> using the operators <code>IN</code> and <code>NOT IN</code>. You can specify up to 50 values in each <code>IN</code> or <code>NOT IN</code> list.</p> <p>The selection criteria can be specified in these formats:</p> <p> <code>LogGroupName IN ["log-group-1", "log-group-2"]</code> </p> <p> <code>LogGroupNamePrefix NOT IN ["/aws/prefix1", "/aws/prefix2"]</code> </p> <p>If you have multiple account-level metric extraction policies with selection criteria, no two of them can have overlapping criteria. For example, if you have one policy with selection criteria <code>LogGroupNamePrefix IN ["my-log"]</code>, you can't have another metric extraction policy with selection criteria <code>LogGroupNamePrefix IN ["/my-log-prod"]</code> or <code>LogGroupNamePrefix IN ["/my-logging"]</code>, as the set of log groups matching these prefixes would be a subset of the log groups matching the first policy's prefix, creating an overlap.</p> <p>When using <code>NOT IN</code>, only one policy with this operator is allowed per account.</p> <p>When combining policies with <code>IN</code> and <code>NOT IN</code> operators, the overlap check ensures that policies don't have conflicting effects. Two policies with <code>IN</code> and <code>NOT IN</code> operators do not overlap if and only if every value in the <code>IN </code>policy is completely contained within some value in the <code>NOT IN</code> policy. For example:</p> <ul> <li> <p>If you have a <code>NOT IN</code> policy for prefix <code>"/aws/lambda"</code>, you can create an <code>IN</code> policy for the exact log group name <code>"/aws/lambda/function1"</code> because the set of log groups matching <code>"/aws/lambda/function1"</code> is a subset of the log groups matching <code>"/aws/lambda"</code>.</p> </li> <li> <p>If you have a <code>NOT IN</code> policy for prefix <code>"/aws/lambda"</code>, you cannot create an <code>IN</code> policy for prefix <code>"/aws"</code> because the set of log groups matching <code>"/aws"</code> is not a subset of the log groups matching <code>"/aws/lambda"</code>.</p> </li> </ul>

        Args:
            policy_name: <p>A name for the policy. This must be unique within the account and cannot start with <code>aws/</code>.</p>
            policy_document: <p>Specify the policy, in JSON.</p> <p> <b>Data protection policy</b> </p> <p>A data protection policy must include two JSON blocks:</p> <ul> <li> <p>The first block must include both a <code>DataIdentifer</code> array and an <code>Operation</code> property with an <code>Audit</code> action. The <code>DataIdentifer</code> array lists the types of sensitive data that you want to mask. For more information about the available options, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html">Types of data that you can mask</a>.</p> <p>The <code>Operation</code> property with an <code>Audit</code> action is required to find the sensitive data terms. This <code>Audit</code> action must contain a <code>FindingsDestination</code> object. You can optionally use that <code>FindingsDestination</code> object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Firehose streams, and S3 buckets, they must already exist.</p> </li> <li> <p>The second block must include both a <code>DataIdentifer</code> array and an <code>Operation</code> property with an <code>Deidentify</code> action. The <code>DataIdentifer</code> array must exactly match the <code>DataIdentifer</code> array in the first block of the policy.</p> <p>The <code>Operation</code> property with the <code>Deidentify</code> action is what actually masks the data, and it must contain the <code> "MaskConfig": {}</code> object. The <code> "MaskConfig": {}</code> object must be empty.</p> </li> </ul> <p>For an example data protection policy, see the <b>Examples</b> section on this page.</p> <important> <p>The contents of the two <code>DataIdentifer</code> arrays must match exactly.</p> </important> <p>In addition to the two JSON blocks, the <code>policyDocument</code> can also include <code>Name</code>, <code>Description</code>, and <code>Version</code> fields. The <code>Name</code> is different than the operation's <code>policyName</code> parameter, and is used as a dimension when CloudWatch Logs reports audit findings metrics to CloudWatch.</p> <p>The JSON specified in <code>policyDocument</code> can be up to 30,720 characters long.</p> <p> <b>Subscription filter policy</b> </p> <p>A subscription filter policy can include the following attributes in a JSON block:</p> <ul> <li> <p> <b>DestinationArn</b> The ARN of the destination to deliver log events to. Supported destinations are:</p> <ul> <li> <p>An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.</p> </li> <li> <p>An Firehose data stream in the same account as the subscription policy, for same-account delivery.</p> </li> <li> <p>A Lambda function in the same account as the subscription policy, for same-account delivery.</p> </li> <li> <p>A logical destination in a different account created with <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html">PutDestination</a>, for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.</p> </li> </ul> </li> <li> <p> <b>RoleArn</b> The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.</p> </li> <li> <p> <b>FilterPattern</b> A filter pattern for subscribing to a filtered stream of log events.</p> </li> <li> <p> <b>Distribution</b> The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to <code>Random</code> for a more even distribution. This property is only applicable when the destination is an Kinesis Data Streams data stream.</p> </li> </ul> <p> <b>Transformer policy</b> </p> <p>A transformer policy must include one JSON block with the array of processors and their configurations. For more information about available processors, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors"> Processors that you can use</a>. </p> <p> <b>Field index policy</b> </p> <p>A field index filter policy can include the following attribute in a JSON block:</p> <ul> <li> <p> <b>Fields</b> The array of field indexes to create.</p> </li> <li> <p> <b>FieldsV2</b> The object of field indexes to create along with it's type.</p> </li> </ul> <p>It must contain at least one field index.</p> <p>The following is an example of an index policy document that creates indexes with different types.</p> <p> <code>"policyDocument": "{ \"Fields\": [ \"TransactionId\" ], \"FieldsV2\": {\"RequestId\": {\"type\": \"FIELD_INDEX\"}, \"APIName\": {\"type\": \"FACET\"}, \"StatusCode\": {\"type\": \"FACET\"}}}"</code> </p> <p>You can use <code>FieldsV2</code> to specify the type for each field. Supported types are <code>FIELD_INDEX</code> and <code>FACET</code>. Field names within <code>Fields</code> and <code>FieldsV2</code> must be mutually exclusive.</p>
            policy_type: <p>The type of policy that you're creating or updating.</p>
            scope: <p>Currently the only valid value for this parameter is <code>ALL</code>, which specifies that the data protection policy applies to all log groups in the account. If you omit this parameter, the default of <code>ALL</code> is used.</p>
            selection_criteria: <p>Use this parameter to apply the new policy to a subset of log groups in the account or a data source name and type combination. </p> <p>Specifying <code>selectionCriteria</code> is valid only when you specify <code>SUBSCRIPTION_FILTER_POLICY</code>, <code>FIELD_INDEX_POLICY</code> or <code>TRANSFORMER_POLICY</code>for <code>policyType</code>.</p> <ul> <li> <p>If <code>policyType</code> is <code>SUBSCRIPTION_FILTER_POLICY</code>, the only supported <code>selectionCriteria</code> filter is <code>LogGroupName NOT IN []</code> </p> </li> <li> <p>If <code>policyType</code> is <code>TRANSFORMER_POLICY</code>, the only supported <code>selectionCriteria</code> filter is <code>LogGroupNamePrefix</code> </p> </li> <li> <p>If <code>policyType</code> is <code>FIELD_INDEX_POLICY</code>, the supported <code>selectionCriteria</code> filters are:</p> <ul> <li> <p> <code>LogGroupNamePrefix</code> </p> </li> <li> <p> <code>DataSourceName</code> AND <code>DataSourceType</code> </p> </li> </ul> <p>When you specify <code>selectionCriteria</code> for a field index policy you can use either <code>LogGroupNamePrefix</code> by itself or <code>DataSourceName</code> and <code>DataSourceType</code> together.</p> </li> </ul> <p>The <code>selectionCriteria</code> string can be up to 25KB in length. The length is determined by using its UTF-8 bytes.</p> <p>Using the <code>selectionCriteria</code> parameter with <code>SUBSCRIPTION_FILTER_POLICY</code> is useful to help prevent infinite loops. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-recursion-prevention.html">Log recursion prevention</a>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_account_policy_request.PutAccountPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_account_policy_response.PutAccountPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_account_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_account_policy.put_account_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_account_policy_request.PutAccountPolicyRequest = {
            "policy_name": policy_name,
            "policy_document": policy_document,
            "policy_type": policy_type,
        }
        if scope is not None:
            input_["scope"] = scope
        if selection_criteria is not None:
            input_["selection_criteria"] = selection_criteria

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_bearer_token_authentication(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        bearer_token_authentication_enabled: "capo_cloudwatch_logs.types.bearer_token_authentication_enabled.BearerTokenAuthenticationEnabled",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        r"""<p>Enables or disables bearer token authentication for the specified log group. When enabled on a log group, bearer token authentication is enabled on operations until it is explicitly disabled.</p> <p>For information about the parameters that are common to all actions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/CommonParameters.html">Common Parameters</a>.</p>

        Args:
            log_group_identifier: <p>The name or ARN of the log group.</p> <p>Type: String</p> <p>Length Constraints: Minimum length of 1. Maximum length of 512.</p> <p>Pattern: <code>[\.\-_/#A-Za-z0-9]+</code> </p> <p>Required: Yes</p>
            bearer_token_authentication_enabled: <p>Whether to enable bearer token authentication.</p> <p>Type: Boolean</p> <p>Required: Yes</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_bearer_token_authentication_request.PutBearerTokenAuthenticationRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_bearer_token_authentication

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_bearer_token_authentication.put_bearer_token_authentication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_bearer_token_authentication_request.PutBearerTokenAuthenticationRequest = {
            "log_group_identifier": log_group_identifier,
            "bearer_token_authentication_enabled": bearer_token_authentication_enabled,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_data_protection_policy(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        policy_document: "capo_cloudwatch_logs.types.data_protection_policy_document.DataProtectionPolicyDocument",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.put_data_protection_policy_response.PutDataProtectionPolicyResponse":
        """<p>Creates a data protection policy for the specified log group. A data protection policy can help safeguard sensitive data that's ingested by the log group by auditing and masking the sensitive log data.</p> <important> <p>Sensitive data is detected and masked when it is ingested into the log group. When you set a data protection policy, log events ingested into the log group before that time are not masked.</p> </important> <p>By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the <code>logs:Unmask</code> permission can use a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html">GetLogEvents</a> or <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html">FilterLogEvents</a> operation with the <code>unmask</code> parameter set to <code>true</code> to view the unmasked log events. Users with the <code>logs:Unmask</code> can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the <code>unmask</code> query command.</p> <p>For more information, including a list of types of data that can be audited and masked, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html">Protect sensitive log data with masking</a>.</p> <p>The <code>PutDataProtectionPolicy</code> operation applies to only the specified log group. You can also use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html">PutAccountPolicy</a> to create an account-level data protection policy that applies to all log groups in the account, including both existing log groups and log groups that are created level. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.</p>

        Args:
            log_group_identifier: <p>Specify either the log group name or log group ARN.</p>
            policy_document: <p>Specify the data protection policy, in JSON.</p> <p>This policy must include two JSON blocks:</p> <ul> <li> <p>The first block must include both a <code>DataIdentifer</code> array and an <code>Operation</code> property with an <code>Audit</code> action. The <code>DataIdentifer</code> array lists the types of sensitive data that you want to mask. For more information about the available options, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html">Types of data that you can mask</a>.</p> <p>The <code>Operation</code> property with an <code>Audit</code> action is required to find the sensitive data terms. This <code>Audit</code> action must contain a <code>FindingsDestination</code> object. You can optionally use that <code>FindingsDestination</code> object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Firehose streams, and S3 buckets, they must already exist.</p> </li> <li> <p>The second block must include both a <code>DataIdentifer</code> array and an <code>Operation</code> property with an <code>Deidentify</code> action. The <code>DataIdentifer</code> array must exactly match the <code>DataIdentifer</code> array in the first block of the policy.</p> <p>The <code>Operation</code> property with the <code>Deidentify</code> action is what actually masks the data, and it must contain the <code> "MaskConfig": {}</code> object. The <code> "MaskConfig": {}</code> object must be empty.</p> </li> </ul> <p>For an example data protection policy, see the <b>Examples</b> section on this page.</p> <important> <p>The contents of the two <code>DataIdentifer</code> arrays must match exactly.</p> </important> <p>In addition to the two JSON blocks, the <code>policyDocument</code> can also include <code>Name</code>, <code>Description</code>, and <code>Version</code> fields. The <code>Name</code> is used as a dimension when CloudWatch Logs reports audit findings metrics to CloudWatch.</p> <p>The JSON specified in <code>policyDocument</code> can be up to 30,720 characters.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_data_protection_policy_request.PutDataProtectionPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_data_protection_policy_response.PutDataProtectionPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_data_protection_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_data_protection_policy.put_data_protection_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_data_protection_policy_request.PutDataProtectionPolicyRequest = {
            "log_group_identifier": log_group_identifier,
            "policy_document": policy_document,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_delivery_destination(
        self,
        name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        output_format: Optional[
            "capo_cloudwatch_logs.types.output_format.OutputFormat"
        ] = None,
        delivery_destination_configuration: Optional[
            "capo_cloudwatch_logs.types.delivery_destination_configuration.DeliveryDestinationConfiguration"
        ] = None,
        delivery_destination_type: Optional[
            "capo_cloudwatch_logs.types.delivery_destination_type.DeliveryDestinationType"
        ] = None,
        role_arn: Optional["capo_cloudwatch_logs.types.arn.Arn"] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
    ) -> "capo_cloudwatch_logs.types.put_delivery_destination_response.PutDeliveryDestinationResponse":
        """<p>Creates or updates a logical <i>delivery destination</i>. A delivery destination is an Amazon Web Services resource that represents an Amazon Web Services service that logs can be sent to. CloudWatch Logs, Amazon S3, and Firehose are supported as logs delivery destinations and X-Ray as the trace delivery destination.</p> <p>To configure logs delivery between a supported Amazon Web Services service and a destination, you must do the following:</p> <ul> <li> <p>Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html">PutDeliverySource</a>.</p> </li> <li> <p>Use <code>PutDeliveryDestination</code> to create a <i>delivery destination</i> in the same account of the actual delivery destination. The delivery destination that you create is a logical object that represents the actual delivery destination. </p> </li> <li> <p>If you are delivering logs cross-account, you must use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html">PutDeliveryDestinationPolicy</a> in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination. </p> </li> <li> <p>Use <code>CreateDelivery</code> to create a <i>delivery</i> by pairing exactly one delivery source and one delivery destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a>. </p> </li> </ul> <p>You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.</p> <p>Only some Amazon Web Services services support being configured as a delivery source. These services are listed as <b>Supported [V2 Permissions]</b> in the table at <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html">Enabling logging from Amazon Web Services services.</a> </p> <p>If you use this operation to update an existing delivery destination, all the current delivery destination parameters are overwritten with the new parameter values that you specify.</p>

        Args:
            name: <p>A name for this delivery destination. This name must be unique for all delivery destinations in your account.</p>
            output_format: <p>The format for the logs that this delivery destination will receive.</p>
            delivery_destination_configuration: <p>A structure that contains the ARN of the Amazon Web Services resource that will receive the logs.</p> <note> <p> <code>deliveryDestinationConfiguration</code> is required for CloudWatch Logs, Amazon S3, Firehose log delivery destinations and not required for X-Ray trace delivery destinations. <code>deliveryDestinationType</code> is needed for X-Ray trace delivery destinations but not required for other logs delivery destinations.</p> </note>
            delivery_destination_type: <p>The type of delivery destination. This parameter specifies the target service where log data will be delivered. Valid values include:</p> <ul> <li> <p> <code>S3</code> - Amazon S3 for long-term storage and analytics</p> </li> <li> <p> <code>CWL</code> - CloudWatch Logs for centralized log management</p> </li> <li> <p> <code>FH</code> - Amazon Kinesis Data Firehose for real-time data streaming</p> </li> <li> <p> <code>XRAY</code> - Amazon Web Services X-Ray for distributed tracing and application monitoring</p> </li> </ul> <p>The delivery destination type determines the format and configuration options available for log delivery.</p>
            role_arn: <p>The ARN of an IAM role in your account that CloudWatch Logs assumes to deliver to this delivery destination. The trust policy of the role must allow CloudWatch Logs to assume it. This parameter is supported only for X-Ray trace delivery destinations.</p>
            tags: <p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>

        Raises:
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_delivery_destination_request.PutDeliveryDestinationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_delivery_destination_response.PutDeliveryDestinationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_delivery_destination

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_delivery_destination.put_delivery_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_delivery_destination_request.PutDeliveryDestinationRequest = {
            "name": name
        }
        if output_format is not None:
            input_["output_format"] = output_format
        if delivery_destination_configuration is not None:
            input_["delivery_destination_configuration"] = (
                delivery_destination_configuration
            )
        if delivery_destination_type is not None:
            input_["delivery_destination_type"] = delivery_destination_type
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_delivery_destination_policy(
        self,
        delivery_destination_name: "capo_cloudwatch_logs.types.delivery_destination_name.DeliveryDestinationName",
        delivery_destination_policy: "capo_cloudwatch_logs.types.delivery_destination_policy.DeliveryDestinationPolicy",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.put_delivery_destination_policy_response.PutDeliveryDestinationPolicyResponse":
        """<p>Creates and assigns an IAM policy that grants permissions to CloudWatch Logs to deliver logs cross-account to a specified destination in this account. To configure the delivery of logs from an Amazon Web Services service in another account to a logs delivery destination in the current account, you must do the following:</p> <ul> <li> <p>Create a delivery source, which is a logical object that represents the resource that is actually sending the logs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html">PutDeliverySource</a>.</p> </li> <li> <p>Create a <i>delivery destination</i>, which is a logical object that represents the actual delivery destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html">PutDeliveryDestination</a>.</p> </li> <li> <p>Use this operation in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination. </p> </li> <li> <p>Create a <i>delivery</i> by pairing exactly one delivery source and one delivery destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a>.</p> </li> </ul> <p>Only some Amazon Web Services services support being configured as a delivery source. These services are listed as <b>Supported [V2 Permissions]</b> in the table at <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html">Enabling logging from Amazon Web Services services.</a> </p> <p>The contents of the policy must include two statements. One statement enables general logs delivery, and the other allows delivery to the chosen destination. See the examples for the needed policies.</p>

        Args:
            delivery_destination_name: <p>The name of the delivery destination to assign this policy to.</p>
            delivery_destination_policy: <p>The contents of the policy.</p>

        Raises:
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_delivery_destination_policy_request.PutDeliveryDestinationPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_delivery_destination_policy_response.PutDeliveryDestinationPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_delivery_destination_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_delivery_destination_policy.put_delivery_destination_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_delivery_destination_policy_request.PutDeliveryDestinationPolicyRequest = {
            "delivery_destination_name": delivery_destination_name,
            "delivery_destination_policy": delivery_destination_policy,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_delivery_source(
        self,
        name: "capo_cloudwatch_logs.types.delivery_source_name.DeliverySourceName",
        resource_arn: "capo_cloudwatch_logs.types.arn.Arn",
        log_type: "capo_cloudwatch_logs.types.log_type.LogType",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
        delivery_source_configuration: Optional[
            "capo_cloudwatch_logs.types.delivery_source_configuration.DeliverySourceConfiguration"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.put_delivery_source_response.PutDeliverySourceResponse":
        """<p>Creates or updates a logical <i>delivery source</i>. A delivery source represents an Amazon Web Services resource that sends logs to an logs delivery destination. The destination can be CloudWatch Logs, Amazon S3, Firehose or X-Ray for sending traces.</p> <p>To configure logs delivery between a delivery destination and an Amazon Web Services service that is supported as a delivery source, you must do the following:</p> <ul> <li> <p>Use <code>PutDeliverySource</code> to create a delivery source, which is a logical object that represents the resource that is actually sending the logs. </p> </li> <li> <p>Use <code>PutDeliveryDestination</code> to create a <i>delivery destination</i>, which is a logical object that represents the actual delivery destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.html">PutDeliveryDestination</a>.</p> </li> <li> <p>If you are delivering logs cross-account, you must use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.html">PutDeliveryDestinationPolicy</a> in the destination account to assign an IAM policy to the destination. This policy allows delivery to that destination. </p> </li> <li> <p>Use <code>CreateDelivery</code> to create a <i>delivery</i> by pairing exactly one delivery source and one delivery destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html">CreateDelivery</a>. </p> </li> </ul> <p>You can configure a single delivery source to send logs to multiple destinations by creating multiple deliveries. You can also create multiple deliveries to configure multiple delivery sources to send logs to the same delivery destination.</p> <p>Only some Amazon Web Services services support being configured as a delivery source. These services are listed as <b>Supported [V2 Permissions]</b> in the table at <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html">Enabling logging from Amazon Web Services services.</a> </p> <p>If you use this operation to update an existing delivery source, all the current delivery source parameters are overwritten with the new parameter values that you specify.</p>

        Args:
            name: <p>A name for this delivery source. This name must be unique for all delivery sources in your account.</p>
            resource_arn: <p>The ARN of the Amazon Web Services resource that is generating and sending logs. For example, <code>arn:aws:workmail:us-east-1:123456789012:organization/m-1234EXAMPLEabcd1234abcd1234abcd1234</code> </p> <p>For the <code>SECURITY_FINDING_LOGS</code> logType, use a wildcard ARN for the hub resource. For Amazon Web Services Security Hub CSPM, use <code>arn:aws:securityhub:us-east-1:111122223333:hub/*</code> and for Amazon Web Services Security Hub, use <code>arn:aws:securityhub:us-east-1:111122223333:hubv2/*</code> </p> <p>For the <code>INSIGHTS_QUERY_LOGS</code> log type, use a wildcard log group ARN, such as <code>arn:aws:logs:us-east-1:111122223333:log-group:*</code>. Amazon Web Services does not support a specific log group ARN for this log type.</p>
            log_type: <p>Defines the type of log that the source is sending.</p> <ul> <li> <p>For Amazon Web Services Amplify, the valid values are <code>ACCESS_LOGS</code> and <code>WAF_LOGS</code>.</p> </li> <li> <p>For Application Load Balancer, the valid values are <code>ALB_ACCESS_LOGS</code>, <code>ALB_CONNECTION_LOGS</code>, and <code>ALB_HEALTH_CHECK_LOGS</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Gateway, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Identity, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Memory, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Payments, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Runtime, the valid values are <code>APPLICATION_LOGS</code>, <code>USAGE_LOGS</code>, and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock AgentCore Tools, the valid values are <code>APPLICATION_LOGS</code>, <code>USAGE_LOGS</code>, and <code>TRACES</code>.</p> </li> <li> <p>For Amazon Bedrock Agents, the valid values are <code>APPLICATION_LOGS</code> and <code>EVENT_LOGS</code>.</p> </li> <li> <p>For Amazon Bedrock Knowledge Bases, the valid values are <code>APPLICATION_LOGS</code> and <code>TRACES</code>.</p> </li> <li> <p>For CloudFront, the valid value is <code>ACCESS_LOGS</code>.</p> </li> <li> <p>For query execution logs from CloudWatch Logs Insights, the valid value is <code>INSIGHTS_QUERY_LOGS</code>.</p> </li> <li> <p>For Amazon CodeWhisperer, the valid value is <code>EVENT_LOGS</code>.</p> </li> <li> <p>For DevOps Agent, the valid value is <code>APPLICATION_LOGS</code>.</p> </li> <li> <p>For Amazon EKS Auto Mode, the valid values are <code>AUTO_MODE_BLOCK_STORAGE_LOGS</code>, <code>AUTO_MODE_COMPUTE_LOGS</code>, <code>AUTO_MODE_IPAM_LOGS</code>, and <code>AUTO_MODE_LOAD_BALANCING_LOGS</code>.</p> </li> <li> <p>For Amazon EKS Capability Logs, the valid values are <code>EKS_CAPABILITY_ACK_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_APPLICATION_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_APPLICATIONSET_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_COMMITSERVER_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_REPOSERVER_LOGS</code>, <code>EKS_CAPABILITY_ARGOCD_SERVER_LOGS</code>, and <code>EKS_CAPABILITY_KRO_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services Elemental Inference, the valid value is <code>APPLICATION_LOGS</code>.</p> </li> <li> <p>For Elemental MediaPackage, the valid values are <code>EGRESS_ACCESS_LOGS</code> and <code>INGRESS_ACCESS_LOGS</code>.</p> </li> <li> <p>For Elemental MediaTailor, the valid values are <code>AD_DECISION_SERVER_LOGS</code>, <code>MANIFEST_SERVICE_LOGS</code>, and <code>TRANSCODE_LOGS</code>.</p> </li> <li> <p>For Entity Resolution, the valid value is <code>WORKFLOW_LOGS</code>.</p> </li> <li> <p>For IAM Identity Center, the valid value is <code>ERROR_LOGS</code>.</p> </li> <li> <p>For Network Firewall Proxy, the valid values are <code>ALERT_LOGS</code>, <code>ALLOW_LOGS</code>, and <code>DENY_LOGS</code>.</p> </li> <li> <p>For Network Load Balancer, the valid value is <code>NLB_ACCESS_LOGS</code>.</p> </li> <li> <p>For PCS, the valid values are <code>PCS_SCHEDULER_LOGS</code>, <code>PCS_JOBCOMP_LOGS</code>, and <code>PCS_SCHEDULER_AUDIT_LOGS</code>.</p> </li> <li> <p>For Amazon Q, the valid values are <code>EVENT_LOGS</code> and <code>SYNC_JOB_LOGS</code>.</p> </li> <li> <p>For Amazon Q in Connect AI agents, the valid value is <code>EVENT_LOGS</code>.</p> </li> <li> <p>For Quick, the valid values are <code>AGENT_HOURS_LOGS</code>, <code>AGENT_METADATA_LOGS</code>, <code>CHAT_LOGS</code>, <code>DLP_LOGS</code>, <code>FEEDBACK_LOGS</code>, <code>INDEX_USAGE_LOGS</code>, and <code>KB_FILE_SYNC_LOGS</code>.</p> </li> <li> <p>For Route 53 Global Resolver, the valid value is <code>GLOBAL_RESOLVER_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services RTB Fabric, the valid value is <code>APPLICATION_LOGS</code>.</p> </li> <li> <p>For Amazon S3, the valid value is <code>S3_SERVER_ACCESS_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services Security Hub, the valid value is <code>SECURITY_FINDING_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services Security Hub CSPM, the valid value is <code>SECURITY_FINDING_LOGS</code>.</p> </li> <li> <p>For Amazon SES mail manager, the valid values are <code>APPLICATION_LOGS</code> and <code>TRAFFIC_POLICY_DEBUG_LOGS</code>.</p> </li> <li> <p>For Amazon Web Services Shield Advanced, the valid value is <code>FLOW_LOGS</code>.</p> </li> <li> <p>For Amazon VPC Route Server, the valid value is <code>EVENT_LOGS</code>.</p> </li> <li> <p>For Amazon WorkMail, the valid values are <code>ACCESS_CONTROL_LOGS</code>, <code>AUTHENTICATION_LOGS</code>, <code>WORKMAIL_AVAILABILITY_PROVIDER_LOGS</code>, <code>WORKMAIL_MAILBOX_ACCESS_LOGS</code>, and <code>WORKMAIL_PERSONAL_ACCESS_TOKEN_LOGS</code>.</p> </li> </ul>
            tags: <p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>
            delivery_source_configuration: <p>A map of key-value pairs to configure the delivery source. Both keys and values must be between 1 and 255 characters in length. For example, <code>{"samplingRate": "50"}</code>.</p>

        Raises:
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_delivery_source_request.PutDeliverySourceRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_delivery_source_response.PutDeliverySourceResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_delivery_source

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_delivery_source.put_delivery_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_delivery_source_request.PutDeliverySourceRequest = {
            "name": name,
            "resource_arn": resource_arn,
            "log_type": log_type,
        }
        if tags is not None:
            input_["tags"] = tags
        if delivery_source_configuration is not None:
            input_["delivery_source_configuration"] = delivery_source_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_destination(
        self,
        destination_name: "capo_cloudwatch_logs.types.destination_name.DestinationName",
        target_arn: "capo_cloudwatch_logs.types.target_arn.TargetArn",
        role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        tags: Optional["capo_cloudwatch_logs.types.tags.Tags"] = None,
    ) -> "capo_cloudwatch_logs.types.put_destination_response.PutDestinationResponse":
        """<p>Creates or updates a destination. This operation is used only to create destinations for cross-account subscriptions.</p> <p>A destination encapsulates a physical resource (such as an Amazon Kinesis stream). With a destination, you can subscribe to a real-time stream of log events for a different account, ingested using <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html">PutLogEvents</a>.</p> <p>Through an access policy, a destination controls what is written to it. By default, <code>PutDestination</code> does not set any access policy with the destination, which means a cross-account user cannot call <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutSubscriptionFilter.html">PutSubscriptionFilter</a> against this destination. To enable this, the destination owner must call <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.html">PutDestinationPolicy</a> after <code>PutDestination</code>.</p> <p>To perform a <code>PutDestination</code> operation, you must also have the <code>iam:PassRole</code> permission.</p>

        Args:
            destination_name: <p>A name for the destination.</p>
            target_arn: <p>The ARN of an Amazon Kinesis stream to which to deliver matching log events.</p>
            role_arn: <p>The ARN of an IAM role that grants CloudWatch Logs permissions to call the Amazon Kinesis <code>PutRecord</code> operation on the destination stream.</p>
            tags: <p>An optional list of key-value pairs to associate with the resource.</p> <p>For more information about tagging, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html">Tagging Amazon Web Services resources</a> </p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_destination_request.PutDestinationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_destination_response.PutDestinationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_destination

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_destination.put_destination(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_destination_request.PutDestinationRequest = {
            "destination_name": destination_name,
            "target_arn": target_arn,
            "role_arn": role_arn,
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

    def put_destination_policy(
        self,
        destination_name: "capo_cloudwatch_logs.types.destination_name.DestinationName",
        access_policy: "capo_cloudwatch_logs.types.access_policy.AccessPolicy",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        force_update: Optional[
            "capo_cloudwatch_logs.types.force_update.ForceUpdate"
        ] = None,
    ) -> None:
        """<p>Creates or updates an access policy associated with an existing destination. An access policy is an <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/policies_overview.html">IAM policy document</a> that is used to authorize claims to register a subscription filter against a given destination.</p>

        Args:
            destination_name: <p>A name for an existing destination.</p>
            access_policy: <p>An IAM policy document that authorizes cross-account users to deliver their log events to the associated destination. This can be up to 5120 bytes.</p>
            force_update: <p>Specify true if you are updating an existing destination policy to grant permission to an organization ID instead of granting permission to individual Amazon Web Services accounts. Before you update a destination policy this way, you must first update the subscription filters in the accounts that send logs to this destination. If you do not, the subscription filters might stop working. By specifying <code>true</code> for <code>forceUpdate</code>, you are affirming that you have already updated the subscription filters. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Cross-Account-Log_Subscription-Update.html"> Updating an existing cross-account subscription</a> </p> <p>If you omit this parameter, the default of <code>false</code> is used.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_destination_policy_request.PutDestinationPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_destination_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_destination_policy.put_destination_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_destination_policy_request.PutDestinationPolicyRequest = {
            "destination_name": destination_name,
            "access_policy": access_policy,
        }
        if force_update is not None:
            input_["force_update"] = force_update

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_index_policy(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        policy_document: "capo_cloudwatch_logs.types.policy_document.PolicyDocument",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.put_index_policy_response.PutIndexPolicyResponse":
        """<p>Creates or updates a <i>field index policy</i> for the specified log group. Only log groups in the Standard log class support field index policies. For more information about log classes, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html">Log classes</a>.</p> <p>You can use field index policies to create <i>field indexes</i> on fields found in log events in the log group. Creating field indexes speeds up and lowers the costs for CloudWatch Logs Insights queries that reference those field indexes, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields or values that match only a small fraction of the total log events. Common examples of indexes include request ID, session ID, userID, and instance IDs. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html">Create field indexes to improve query performance and reduce costs</a>.</p> <p>You can configure indexed fields as <i>facets</i> to enable interactive exploration and filtering of your logs in the CloudWatch Logs Insights console. Facets allow you to view value distributions and counts for indexed fields without running queries. When you create a field index, you can optionally set it as a facet to enable this interactive analysis capability. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Facets.html">Use facets to group and explore logs</a>.</p> <p>To find the fields that are in your log group events, use the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.html">GetLogGroupFields</a> operation.</p> <p>For example, suppose you have created a field index for <code>requestId</code>. Then, any CloudWatch Logs Insights query on that log group that includes <code>requestId = <i>value</i> </code> or <code>requestId IN [<i>value</i>, <i>value</i>, ...]</code> will process fewer log events to reduce costs, and have improved performance.</p> <p>CloudWatch Logs provides default field indexes for all log groups in the Standard log class. Default field indexes are automatically available for the following fields: </p> <ul> <li> <p> <code>@logStream</code> </p> </li> <li> <p> <code>@aws.region</code> </p> </li> <li> <p> <code>@aws.account</code> </p> </li> <li> <p> <code>@source.log</code> </p> </li> <li> <p> <code>traceId</code> </p> </li> </ul> <p>Default field indexes are in addition to any custom field indexes you define within your policy. Default field indexes are not counted towards your field index quota. </p> <p>Each index policy has the following quotas and restrictions:</p> <ul> <li> <p>As many as 20 fields can be included in the policy.</p> </li> <li> <p>Each field name can include as many as 100 characters.</p> </li> </ul> <p>Matches of log events to the names of indexed fields are case-sensitive. For example, a field index of <code>RequestId</code> won't match a log event containing <code>requestId</code>.</p> <p>Log group-level field index policies created with <code>PutIndexPolicy</code> override account-level field index policies created with <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html">PutAccountPolicy</a> that apply to log groups. If you use <code>PutIndexPolicy</code> to create a field index policy for a log group, that log group uses only that policy for log group-level indexing, including any facet configurations. The log group ignores any account-wide field index policy that applies to log groups, but data source-based account policies may still apply.</p>

        Args:
            log_group_identifier: <p>Specify either the log group name or log group ARN to apply this field index policy to. If you specify an ARN, use the format arn:aws:logs:<i>region</i>:<i>account-id</i>:log-group:<i>log_group_name</i> Don't include an * at the end.</p>
            policy_document: <p>The index policy document, in JSON format. The following is an example of an index policy document that creates indexes with different types.</p> <p> <code>"policyDocument": "{"Fields": [ "TransactionId" ], "FieldsV2": {"RequestId": {"type": "FIELD_INDEX"}, "APIName": {"type": "FACET"}, "StatusCode": {"type": "FACET"}}}"</code> </p> <p>You can use <code>FieldsV2</code> to specify the type for each field. Supported types are <code>FIELD_INDEX</code> and <code>FACET</code>. Field names within <code>Fields</code> and <code>FieldsV2</code> must be mutually exclusive.</p> <p>The policy document must include at least one field index. For more information about the fields that can be included and other restrictions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing-Syntax.html">Field index syntax and quotas</a>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_index_policy_request.PutIndexPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_index_policy_response.PutIndexPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_index_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_index_policy.put_index_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_index_policy_request.PutIndexPolicyRequest = {
            "log_group_identifier": log_group_identifier,
            "policy_document": policy_document,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_integration(
        self,
        integration_name: "capo_cloudwatch_logs.types.integration_name.IntegrationName",
        resource_config: "capo_cloudwatch_logs.types.resource_config.ResourceConfig",
        integration_type: "capo_cloudwatch_logs.types.integration_type.IntegrationType",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.put_integration_response.PutIntegrationResponse":
        """<p>Creates an integration between CloudWatch Logs and another service in this account. Currently, only integrations with OpenSearch Service are supported, and currently you can have only one integration in your account.</p> <p>Integrating with OpenSearch Service makes it possible for you to create curated vended logs dashboards, powered by OpenSearch Service analytics. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-OpenSearch-Dashboards.html">Vended log dashboards powered by Amazon OpenSearch Service</a>.</p> <p>You can use this operation only to create a new integration. You can't modify an existing integration.</p>

        Args:
            integration_name: <p>A name for the integration.</p>
            resource_config: <p>A structure that contains configuration information for the integration that you are creating.</p>
            integration_type: <p>The type of integration. Currently, the only supported type is <code>OPENSEARCH</code>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_integration_request.PutIntegrationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_integration_response.PutIntegrationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_integration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_integration.put_integration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_integration_request.PutIntegrationRequest = {
            "integration_name": integration_name,
            "resource_config": resource_config,
            "integration_type": integration_type,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_log_events(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        log_stream_name: "capo_cloudwatch_logs.types.log_stream_name.LogStreamName",
        log_events: "capo_cloudwatch_logs.types.input_log_events.InputLogEvents",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        sequence_token: Optional[
            "capo_cloudwatch_logs.types.sequence_token.SequenceToken"
        ] = None,
        entity: Optional["capo_cloudwatch_logs.types.entity.Entity"] = None,
    ) -> "capo_cloudwatch_logs.types.put_log_events_response.PutLogEventsResponse":
        """<p>Uploads a batch of log events to the specified log stream.</p> <important> <p>The sequence token is now ignored in <code>PutLogEvents</code> actions. <code>PutLogEvents</code> actions are always accepted and never return <code>InvalidSequenceTokenException</code> or <code>DataAlreadyAcceptedException</code> even if the sequence token is not valid. You can use parallel <code>PutLogEvents</code> actions on the same log stream. </p> </important> <p>The batch of events must satisfy the following constraints:</p> <ul> <li> <p>The maximum batch size is 1,048,576 bytes. This size is calculated as the sum of all event messages in UTF-8, plus 26 bytes for each log event.</p> </li> <li> <p>Events more than 2 hours in the future are rejected while processing remaining valid events.</p> </li> <li> <p>Events older than 14 days or preceding the log group's retention period are rejected while processing remaining valid events.</p> </li> <li> <p>The log events in the batch must be in chronological order by their timestamp. The timestamp is the time that the event occurred, expressed as the number of milliseconds after <code>Jan 1, 1970 00:00:00 UTC</code>. (In Amazon Web Services Tools for PowerShell and the Amazon Web Services SDK for .NET, the timestamp is specified in .NET format: <code>yyyy-mm-ddThh:mm:ss</code>. For example, <code>2017-09-15T13:45:30</code>.) </p> </li> <li> <p> A batch of log events in a single request must be in a chronological order. Otherwise, the operation fails.</p> </li> <li> <p>Each log event can be no larger than 1 MB.</p> </li> <li> <p>The maximum number of log events in a batch is 10,000.</p> </li> <li> <p>For valid events (within 14 days in the past to 2 hours in future), the time span in a single batch cannot exceed 24 hours. Otherwise, the operation fails.</p> </li> </ul> <important> <p>The quota of five requests per second per log stream has been removed. Instead, <code>PutLogEvents</code> actions are throttled based on a per-second per-account quota. You can request an increase to the per-second throttling quota by using the Service Quotas service.</p> </important> <p>If a call to <code>PutLogEvents</code> returns "UnrecognizedClientException" the most likely cause is a non-valid Amazon Web Services access key ID or secret key. </p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            log_stream_name: <p>The name of the log stream.</p>
            log_events: <p>The log events.</p>
            sequence_token: <p>The sequence token obtained from the response of the previous <code>PutLogEvents</code> call.</p> <important> <p>The <code>sequenceToken</code> parameter is now ignored in <code>PutLogEvents</code> actions. <code>PutLogEvents</code> actions are now accepted and never return <code>InvalidSequenceTokenException</code> or <code>DataAlreadyAcceptedException</code> even if the sequence token is not valid.</p> </important>
            entity: <p>The entity associated with the log events.</p>

        Raises:
            capo_cloudwatch_logs.errors.data_already_accepted_exception.DataAlreadyAcceptedException: <p>The event was already logged.</p> <important> <p> <code>PutLogEvents</code> actions are now always accepted and never return <code>DataAlreadyAcceptedException</code> regardless of whether a given batch of log events has already been accepted. </p> </important>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.invalid_sequence_token_exception.InvalidSequenceTokenException: <p>The sequence token is not valid. You can get the correct sequence token in the <code>expectedSequenceToken</code> field in the <code>InvalidSequenceTokenException</code> message. </p> <important> <p> <code>PutLogEvents</code> actions are now always accepted and never return <code>InvalidSequenceTokenException</code> regardless of receiving an invalid sequence token. </p> </important>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.unrecognized_client_exception.UnrecognizedClientException: <p>The most likely cause is an Amazon Web Services access key ID or secret key that's not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_log_events_request.PutLogEventsRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_log_events_response.PutLogEventsResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_log_events

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_log_events.put_log_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_log_events_request.PutLogEventsRequest = {
            "log_group_name": log_group_name,
            "log_stream_name": log_stream_name,
            "log_events": log_events,
        }
        if sequence_token is not None:
            input_["sequence_token"] = sequence_token
        if entity is not None:
            input_["entity"] = entity

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_log_group_deletion_protection(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        deletion_protection_enabled: "capo_cloudwatch_logs.types.deletion_protection_enabled.DeletionProtectionEnabled",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        r"""<p>Enables or disables deletion protection for the specified log group. When enabled on a log group, deletion protection blocks all deletion operations until it is explicitly disabled.</p> <p>For information about the parameters that are common to all actions, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/CommonParameters.html">Common Parameters</a>.</p>

        Args:
            log_group_identifier: <p>The name or ARN of the log group.</p> <p>Type: String</p> <p>Length Constraints: Minimum length of 1. Maximum length of 512.</p> <p>Pattern: <code>[\.\-_/#A-Za-z0-9]+</code> </p> <p>Required: Yes</p>
            deletion_protection_enabled: <p>Whether to enable deletion protection.</p> <p>Type: Boolean</p> <p>Required: Yes</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_log_group_deletion_protection_request.PutLogGroupDeletionProtectionRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_log_group_deletion_protection

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_log_group_deletion_protection.put_log_group_deletion_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_log_group_deletion_protection_request.PutLogGroupDeletionProtectionRequest = {
            "log_group_identifier": log_group_identifier,
            "deletion_protection_enabled": deletion_protection_enabled,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_metric_filter(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        filter_name: "capo_cloudwatch_logs.types.filter_name.FilterName",
        filter_pattern: "capo_cloudwatch_logs.types.filter_pattern.FilterPattern",
        metric_transformations: "capo_cloudwatch_logs.types.metric_transformations.MetricTransformations",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        apply_on_transformed_logs: Optional[
            "capo_cloudwatch_logs.types.apply_on_transformed_logs.ApplyOnTransformedLogs"
        ] = None,
        field_selection_criteria: Optional[
            "capo_cloudwatch_logs.types.field_selection_criteria.FieldSelectionCriteria"
        ] = None,
        emit_system_field_dimensions: Optional[
            "capo_cloudwatch_logs.types.emit_system_fields.EmitSystemFields"
        ] = None,
    ) -> None:
        """<p>Creates or updates a metric filter and associates it with the specified log group. With metric filters, you can configure rules to extract metric data from log events ingested through <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html">PutLogEvents</a>.</p> <p>The maximum number of metric filters that can be associated with a log group is 100.</p> <p>Using regular expressions in filter patterns is supported. For these filters, there is a quota of two regular expression patterns within a single filter pattern. There is also a quota of five regular expression patterns per log group. For more information about using regular expressions in filter patterns, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html"> Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail</a>.</p> <p>When you create a metric filter, you can also optionally assign a unit and dimensions to the metric that is created.</p> <important> <p>Metrics extracted from log events are charged as custom metrics. To prevent unexpected high charges, do not specify high-cardinality fields such as <code>IPAddress</code> or <code>requestID</code> as dimensions. Each different value found for a dimension is treated as a separate metric and accrues charges as a separate custom metric. </p> <p>CloudWatch Logs might disable a metric filter if it generates 1,000 different name/value pairs for your specified dimensions within one hour.</p> <p>You can also set up a billing alarm to alert you if your charges are higher than expected. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/monitor_estimated_charges_with_cloudwatch.html"> Creating a Billing Alarm to Monitor Your Estimated Amazon Web Services Charges</a>. </p> </important>

        Args:
            log_group_name: <p>The name of the log group.</p>
            filter_name: <p>A name for the metric filter.</p>
            filter_pattern: <p>A filter pattern for extracting metric data out of ingested log events.</p>
            metric_transformations: <p>A collection of information that defines how metric data gets emitted.</p>
            apply_on_transformed_logs: <p>This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html">PutTransformer</a>.</p> <p>If the log group uses either a log-group level or account-level transformer, and you specify <code>true</code>, the metric filter will be applied on the transformed version of the log events instead of the original ingested log events.</p>
            field_selection_criteria: <p>A filter expression that specifies which log events should be processed by this metric filter based on system fields such as source account and source region. Uses selection criteria syntax with operators like <code>=</code>, <code>!=</code>, <code>AND</code>, <code>OR</code>, <code>IN</code>, <code>NOT IN</code>. Example: <code>@aws.region = "us-east-1"</code> or <code>@aws.account IN ["123456789012", "987654321098"]</code>. Maximum length: 2000 characters.</p>
            emit_system_field_dimensions: <p>A list of system fields to emit as additional dimensions in the generated metrics. Valid values are <code>@aws.account</code> and <code>@aws.region</code>. These dimensions help identify the source of centralized log data and count toward the total dimension limit for metric filters.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_metric_filter_request.PutMetricFilterRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_metric_filter

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_metric_filter.put_metric_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_metric_filter_request.PutMetricFilterRequest = {
            "log_group_name": log_group_name,
            "filter_name": filter_name,
            "filter_pattern": filter_pattern,
            "metric_transformations": metric_transformations,
        }
        if apply_on_transformed_logs is not None:
            input_["apply_on_transformed_logs"] = apply_on_transformed_logs
        if field_selection_criteria is not None:
            input_["field_selection_criteria"] = field_selection_criteria
        if emit_system_field_dimensions is not None:
            input_["emit_system_field_dimensions"] = emit_system_field_dimensions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_query_definition(
        self,
        name: "capo_cloudwatch_logs.types.query_definition_name.QueryDefinitionName",
        query_string: "capo_cloudwatch_logs.types.query_definition_string.QueryDefinitionString",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        query_language: Optional[
            "capo_cloudwatch_logs.types.query_language.QueryLanguage"
        ] = None,
        query_definition_id: Optional[
            "capo_cloudwatch_logs.types.query_id.QueryId"
        ] = None,
        log_group_names: Optional[
            "capo_cloudwatch_logs.types.log_group_names.LogGroupNames"
        ] = None,
        client_token: Optional[
            "capo_cloudwatch_logs.types.client_token.ClientToken"
        ] = None,
        parameters: Optional[
            "capo_cloudwatch_logs.types.query_parameter_list.QueryParameterList"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.put_query_definition_response.PutQueryDefinitionResponse":
        """<p>Creates or updates a query definition for CloudWatch Logs Insights. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html">Analyzing Log Data with CloudWatch Logs Insights</a>.</p> <p>To update a query definition, specify its <code>queryDefinitionId</code> in your request. The values of <code>name</code>, <code>queryString</code>, and <code>logGroupNames</code> are changed to the values that you specify in your update operation. No current values are retained from the current query definition. For example, imagine updating a current query definition that includes log groups. If you don't specify the <code>logGroupNames</code> parameter in your update operation, the query definition changes to contain no log groups.</p> <p>You must have the <code>logs:PutQueryDefinition</code> permission to be able to perform this operation.</p>

        Args:
            query_language: <p>Specify the query language to use for this query. The options are Logs Insights QL, OpenSearch PPL, and OpenSearch SQL. For more information about the query languages that CloudWatch Logs supports, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html">Supported query languages</a>.</p>
            name: <p>A name for the query definition. If you are saving numerous query definitions, we recommend that you name them. This way, you can find the ones you want by using the first part of the name as a filter in the <code>queryDefinitionNamePrefix</code> parameter of <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html">DescribeQueryDefinitions</a>.</p>
            query_definition_id: <p>If you are updating a query definition, use this parameter to specify the ID of the query definition that you want to update. You can use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeQueryDefinitions.html">DescribeQueryDefinitions</a> to retrieve the IDs of your saved query definitions.</p> <p>If you are creating a query definition, do not specify this parameter. CloudWatch generates a unique ID for the new query definition and include it in the response to this operation.</p>
            log_group_names: <p>Use this parameter to include specific log groups as part of your query definition. If your query uses the OpenSearch Service query language, you specify the log group names inside the <code>querystring</code> instead of here.</p> <p>If you are updating an existing query definition for the Logs Insights QL or OpenSearch Service PPL and you omit this parameter, then the updated definition will contain no log groups.</p>
            query_string: <p>The query string to use for this definition. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html">CloudWatch Logs Insights Query Syntax</a>.</p>
            client_token: <p>Used as an idempotency token, to avoid returning an exception if the service receives the same request twice because of a network error.</p>
            parameters: <p>Use this parameter to include specific query parameters as part of your query definition. Query parameters are supported only for Logs Insights QL queries. Query parameters allow you to use placeholder variables in your query string that are substituted with values at execution time. Use the <code>{{parameterName}}</code> syntax in your query string to reference a parameter.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_query_definition_request.PutQueryDefinitionRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_query_definition_response.PutQueryDefinitionResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_query_definition

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_query_definition.put_query_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_query_definition_request.PutQueryDefinitionRequest = {
            "name": name,
            "query_string": query_string,
        }
        if query_language is not None:
            input_["query_language"] = query_language
        if query_definition_id is not None:
            input_["query_definition_id"] = query_definition_id
        if log_group_names is not None:
            input_["log_group_names"] = log_group_names
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_resource_policy(
        self,
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        policy_name: Optional[
            "capo_cloudwatch_logs.types.policy_name.PolicyName"
        ] = None,
        policy_document: Optional[
            "capo_cloudwatch_logs.types.policy_document.PolicyDocument"
        ] = None,
        resource_arn: Optional["capo_cloudwatch_logs.types.arn.Arn"] = None,
        expected_revision_id: Optional[
            "capo_cloudwatch_logs.types.expected_revision_id.ExpectedRevisionId"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.put_resource_policy_response.PutResourcePolicyResponse":
        """<p>Creates or updates a resource policy allowing other Amazon Web Services services to put log events to this account, such as Amazon Route 53. This API has the following restrictions:</p> <ul> <li> <p> <b>Supported actions</b> - Policy only supports <code>logs:PutLogEvents</code> and <code>logs:CreateLogStream </code> actions</p> </li> <li> <p> <b>Supported principals</b> - Policy only applies when operations are invoked by Amazon Web Services service principals (not IAM users, roles, or cross-account principals</p> </li> <li> <p> <b>Policy limits</b> - An account can have a maximum of 10 policies without resourceARN and one per LogGroup resourceARN</p> </li> </ul> <important> <p>Resource policies with actions invoked by non-Amazon Web Services service principals (such as IAM users, roles, or other Amazon Web Services accounts) will not be enforced. For access control involving these principals, use the IAM policies.</p> </important>

        Args:
            policy_name: <p>Name of the new policy. This parameter is required.</p>
            policy_document: <p>Details of the new policy, including the identity of the principal that is enabled to put logs to this account. This is formatted as a JSON string. This parameter is required.</p> <p>The following example creates a resource policy enabling the Route 53 service to put DNS query logs in to the specified log group. Replace <code>"logArn"</code> with the ARN of your CloudWatch Logs resource, such as a log group or log stream.</p> <p>CloudWatch Logs also supports <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourcearn">aws:SourceArn</a> and <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-sourceaccount">aws:SourceAccount</a> condition context keys.</p> <p>In the example resource policy, you would replace the value of <code>SourceArn</code> with the resource making the call from Route 53 to CloudWatch Logs. You would also replace the value of <code>SourceAccount</code> with the Amazon Web Services account ID making that call.</p> <p></p> <p> <code>{ "Version": "2012-10-17", "Statement": [ { "Sid": "Route53LogsToCloudWatchLogs", "Effect": "Allow", "Principal": { "Service": [ "route53.amazonaws.com" ] }, "Action": "logs:PutLogEvents", "Resource": "logArn", "Condition": { "ArnLike": { "aws:SourceArn": "myRoute53ResourceArn" }, "StringEquals": { "aws:SourceAccount": "myAwsAccountId" } } } ] }</code> </p>
            resource_arn: <p>The ARN of the CloudWatch Logs resource to which the resource policy needs to be added or attached. Currently only supports LogGroup ARN.</p>
            expected_revision_id: <p>The expected revision ID of the resource policy. Required when <code>resourceArn</code> is provided to prevent concurrent modifications. Use <code>null</code> when creating a resource policy for the first time.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_resource_policy_request.PutResourcePolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_resource_policy_response.PutResourcePolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_resource_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_resource_policy.put_resource_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_resource_policy_request.PutResourcePolicyRequest = {}
        if policy_name is not None:
            input_["policy_name"] = policy_name
        if policy_document is not None:
            input_["policy_document"] = policy_document
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if expected_revision_id is not None:
            input_["expected_revision_id"] = expected_revision_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_retention_policy(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        retention_in_days: "capo_cloudwatch_logs.types.days.Days",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Sets the retention of the specified log group. With a retention policy, you can configure the number of days for which to retain log events in the specified log group.</p> <note> <p>CloudWatch Logs doesn't immediately delete log events when they reach their retention setting. It typically takes up to 72 hours after that before log events are deleted, but in rare situations might take longer.</p> <p>To illustrate, imagine that you change a log group to have a longer retention setting when it contains log events that are past the expiration date, but haven't been deleted. Those log events will take up to 72 hours to be deleted after the new retention date is reached. To make sure that log data is deleted permanently, keep a log group at its lower retention setting until 72 hours after the previous retention period ends. Alternatively, wait to change the retention setting until you confirm that the earlier log events are deleted. </p> <p>When log events reach their retention setting they are marked for deletion. After they are marked for deletion, they do not add to your archival storage costs anymore, even if they are not actually deleted until later. These log events marked for deletion are also not included when you use an API to retrieve the <code>storedBytes</code> value to see how many bytes a log group is storing.</p> </note>

        Args:
            log_group_name: <p>The name of the log group.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_retention_policy_request.PutRetentionPolicyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_retention_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_retention_policy.put_retention_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_retention_policy_request.PutRetentionPolicyRequest = {
            "log_group_name": log_group_name,
            "retention_in_days": retention_in_days,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_storage_tier_policy(
        self,
        storage_tier: "capo_cloudwatch_logs.types.storage_tier.StorageTier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.put_storage_tier_policy_response.PutStorageTierPolicyResponse":
        """<p>Sets the storage tier policy for the account. When you set the storage tier to <code>INTELLIGENT_TIERING</code>, the service automatically moves log data to the most cost-effective storage tier based on access frequency.</p>

        Args:
            storage_tier: <p>The storage tier to set for the account. Use <code>INTELLIGENT_TIERING</code> to automatically optimize storage costs by moving log data to the appropriate tier based on access frequency.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_storage_tier_policy_request.PutStorageTierPolicyRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.put_storage_tier_policy_response.PutStorageTierPolicyResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_storage_tier_policy

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_storage_tier_policy.put_storage_tier_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_storage_tier_policy_request.PutStorageTierPolicyRequest = {
            "storage_tier": storage_tier
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_subscription_filter(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        filter_name: "capo_cloudwatch_logs.types.filter_name.FilterName",
        filter_pattern: "capo_cloudwatch_logs.types.filter_pattern.FilterPattern",
        destination_arn: "capo_cloudwatch_logs.types.destination_arn.DestinationArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        role_arn: Optional["capo_cloudwatch_logs.types.role_arn.RoleArn"] = None,
        distribution: Optional[
            "capo_cloudwatch_logs.types.distribution.Distribution"
        ] = None,
        apply_on_transformed_logs: Optional[
            "capo_cloudwatch_logs.types.apply_on_transformed_logs.ApplyOnTransformedLogs"
        ] = None,
        field_selection_criteria: Optional[
            "capo_cloudwatch_logs.types.field_selection_criteria.FieldSelectionCriteria"
        ] = None,
        emit_system_fields: Optional[
            "capo_cloudwatch_logs.types.emit_system_fields.EmitSystemFields"
        ] = None,
    ) -> None:
        """<p>Creates or updates a subscription filter and associates it with the specified log group. With subscription filters, you can subscribe to a real-time stream of log events ingested through <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.html">PutLogEvents</a> and have them delivered to a specific destination. When log events are sent to the receiving service, they are Base64 encoded and compressed with the GZIP format.</p> <p>The following destinations are supported for subscription filters:</p> <ul> <li> <p>An Amazon Kinesis data stream belonging to the same account as the subscription filter, for same-account delivery.</p> </li> <li> <p>A logical destination created with <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html">PutDestination</a> that belongs to a different account, for cross-account delivery. We currently support Kinesis Data Streams and Firehose as logical destinations.</p> </li> <li> <p>An Amazon Kinesis Data Firehose delivery stream that belongs to the same account as the subscription filter, for same-account delivery.</p> </li> <li> <p>An Lambda function that belongs to the same account as the subscription filter, for same-account delivery.</p> </li> </ul> <p>Each log group can have up to two subscription filters associated with it. If you are updating an existing filter, you must specify the correct name in <code>filterName</code>. </p> <p>Using regular expressions in filter patterns is supported. For these filters, there is a quotas of quota of two regular expression patterns within a single filter pattern. There is also a quota of five regular expression patterns per log group. For more information about using regular expressions in filter patterns, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html"> Filter pattern syntax for metric filters, subscription filters, filter log events, and Live Tail</a>.</p> <p>To perform a <code>PutSubscriptionFilter</code> operation for any destination except a Lambda function, you must also have the <code>iam:PassRole</code> permission.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            filter_name: <p>A name for the subscription filter. If you are updating an existing filter, you must specify the correct name in <code>filterName</code>. To find the name of the filter currently associated with a log group, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeSubscriptionFilters.html">DescribeSubscriptionFilters</a>.</p>
            filter_pattern: <p>A filter pattern for subscribing to a filtered stream of log events.</p>
            destination_arn: <p>The ARN of the destination to deliver matching log events to. Currently, the supported destinations are:</p> <ul> <li> <p>An Amazon Kinesis stream belonging to the same account as the subscription filter, for same-account delivery.</p> </li> <li> <p>A logical destination (specified using an ARN) belonging to a different account, for cross-account delivery.</p> <p>If you're setting up a cross-account subscription, the destination must have an IAM policy associated with it. The IAM policy must allow the sender to send logs to the destination. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.html">PutDestinationPolicy</a>.</p> </li> <li> <p>A Kinesis Data Firehose delivery stream belonging to the same account as the subscription filter, for same-account delivery.</p> </li> <li> <p>A Lambda function belonging to the same account as the subscription filter, for same-account delivery.</p> </li> </ul>
            role_arn: <p>The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You don't need to provide the ARN when you are working with a logical destination for cross-account delivery.</p>
            distribution: <p>The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to random for a more even distribution. This property is only applicable when the destination is an Amazon Kinesis data stream. </p>
            apply_on_transformed_logs: <p>This parameter is valid only for log groups that have an active log transformer. For more information about log transformers, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html">PutTransformer</a>.</p> <p>If the log group uses either a log-group level or account-level transformer, and you specify <code>true</code>, the subscription filter will be applied on the transformed version of the log events instead of the original ingested log events.</p>
            field_selection_criteria: <p>A filter expression that specifies which log events should be processed by this subscription filter based on system fields such as source account and source region. Uses selection criteria syntax with operators like <code>=</code>, <code>!=</code>, <code>AND</code>, <code>OR</code>, <code>IN</code>, <code>NOT IN</code>. Example: <code>@aws.region NOT IN ["cn-north-1"]</code> or <code>@aws.account = "123456789012" AND @aws.region = "us-east-1"</code>. Maximum length: 2000 characters.</p>
            emit_system_fields: <p>A list of system fields to include in the log events sent to the subscription destination. Valid values are <code>@aws.account</code>, <code>@aws.region</code>, and <code>@source.log</code>. These fields provide source information for centralized log data in the forwarded payload.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_subscription_filter_request.PutSubscriptionFilterRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_subscription_filter

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_subscription_filter.put_subscription_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_subscription_filter_request.PutSubscriptionFilterRequest = {
            "log_group_name": log_group_name,
            "filter_name": filter_name,
            "filter_pattern": filter_pattern,
            "destination_arn": destination_arn,
        }
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if distribution is not None:
            input_["distribution"] = distribution
        if apply_on_transformed_logs is not None:
            input_["apply_on_transformed_logs"] = apply_on_transformed_logs
        if field_selection_criteria is not None:
            input_["field_selection_criteria"] = field_selection_criteria
        if emit_system_fields is not None:
            input_["emit_system_fields"] = emit_system_fields

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_syslog_configuration(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        vpc_endpoint_id: Optional[
            "capo_cloudwatch_logs.types.vpc_endpoint_id.VpcEndpointId"
        ] = None,
    ) -> None:
        """<p>Creates or updates a syslog configuration for a log group. This enables ingestion of syslog data through the specified VPC endpoint into the log group.</p>

        Args:
            log_group_identifier: <p>The name or ARN of the log group to associate with the syslog configuration.</p>
            vpc_endpoint_id: <p>The ID of the VPC endpoint to use for syslog ingestion.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_syslog_configuration_request.PutSyslogConfigurationRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_syslog_configuration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_syslog_configuration.put_syslog_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_syslog_configuration_request.PutSyslogConfigurationRequest = {
            "log_group_identifier": log_group_identifier
        }
        if vpc_endpoint_id is not None:
            input_["vpc_endpoint_id"] = vpc_endpoint_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_transformer(
        self,
        log_group_identifier: "capo_cloudwatch_logs.types.log_group_identifier.LogGroupIdentifier",
        transformer_config: "capo_cloudwatch_logs.types.processors.Processors",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Creates or updates a <i>log transformer</i> for a single log group. You use log transformers to transform log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contains relevant, source-specific information.</p> <p>After you have created a transformer, CloudWatch Logs performs the transformations at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filers.</p> <p>You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.</p> <p>A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. The processors work one after another, in the order that you list them, like a pipeline. For more information about the available processors to use in a transformer, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors"> Processors that you can use</a>.</p> <p>Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major Amazon Web Services log sources such as VPC flow logs, Lambda, and Amazon RDS. You can use pre-built transformation templates or create custom transformation policies.</p> <p>You can create transformers only for the log groups in the Standard log class.</p> <p>You can also set up a transformer at the account level. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html">PutAccountPolicy</a>. If there is both a log-group level transformer created with <code>PutTransformer</code> and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.</p>

        Args:
            log_group_identifier: <p>Specify either the name or ARN of the log group to create the transformer for. </p>
            transformer_config: <p>This structure contains the configuration of this log transformer. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.put_transformer_request.PutTransformerRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.put_transformer

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.put_transformer.put_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.put_transformer_request.PutTransformerRequest = {
            "log_group_identifier": log_group_identifier,
            "transformer_config": transformer_config,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_live_tail(
        self,
        log_group_identifiers: "capo_cloudwatch_logs.types.start_live_tail_log_group_identifiers.StartLiveTailLogGroupIdentifiers",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        log_stream_names: Optional[
            "capo_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
        ] = None,
        log_stream_name_prefixes: Optional[
            "capo_cloudwatch_logs.types.input_log_stream_names.InputLogStreamNames"
        ] = None,
        log_event_filter_pattern: Optional[
            "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse":
        """<p>Starts a Live Tail streaming session for one or more log groups. A Live Tail session returns a stream of log events that have been recently ingested in the log groups. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html">Use Live Tail to view logs in near real time</a>. </p> <p>The response to this operation is a response stream, over which the server sends live log events and the client receives them.</p> <p>The following objects are sent over the stream:</p> <ul> <li> <p>A single <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LiveTailSessionStart.html">LiveTailSessionStart</a> object is sent at the start of the session.</p> </li> <li> <p>Every second, a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LiveTailSessionUpdate.html">LiveTailSessionUpdate</a> object is sent. Each of these objects contains an array of the actual log events.</p> <p>If no new log events were ingested in the past second, the <code>LiveTailSessionUpdate</code> object will contain an empty array.</p> <p>The array of log events contained in a <code>LiveTailSessionUpdate</code> can include as many as 500 log events. If the number of log events matching the request exceeds 500 per second, the log events are sampled down to 500 log events to be included in each <code>LiveTailSessionUpdate</code> object.</p> <p>If your client consumes the log events slower than the server produces them, CloudWatch Logs buffers up to 10 <code>LiveTailSessionUpdate</code> events or 5000 log events, after which it starts dropping the oldest events.</p> </li> <li> <p>A <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartLiveTailResponseStream.html#CWL-Type-StartLiveTailResponseStream-SessionStreamingException">SessionStreamingException</a> object is returned if an unknown error occurs on the server side.</p> </li> <li> <p>A <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartLiveTailResponseStream.html#CWL-Type-StartLiveTailResponseStream-SessionTimeoutException">SessionTimeoutException</a> object is returned when the session times out, after it has been kept open for three hours.</p> </li> </ul> <note> <p>The <code>StartLiveTail</code> API routes requests using SDK host prefix injection. SDK versions released before April 1, 2026 route to <code>streaming-logs.<i>Region</i>.amazonaws.com</code>, which does not support VPC endpoints. SDK versions released on or after April 1, 2026 route to <code>stream-logs.<i>Region</i>.amazonaws.com</code>, which supports VPC endpoints. To set up a VPC endpoint for this API, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/cloudwatch-logs-and-interface-VPC.html#create-VPC-endpoint-for-CloudWatchLogs">Creating a VPC endpoint for CloudWatch Logs </a>.</p> </note> <important> <p>You can end a session before it times out by closing the session stream or by closing the client that is receiving the stream. The session also ends if the established connection between the client and the server breaks.</p> </important> <p>For examples of using an SDK to start a Live Tail session, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/example_cloudwatch-logs_StartLiveTail_section.html"> Start a Live Tail session using an Amazon Web Services SDK</a>.</p>

        Args:
            log_group_identifiers: <p>An array where each item in the array is a log group to include in the Live Tail session.</p> <p>Specify each log group by its ARN. </p> <p>If you specify an ARN, the ARN can't end with an asterisk (*).</p> <note> <p> You can include up to 10 log groups.</p> </note>
            log_stream_names: <p>If you specify this parameter, then only log events in the log streams that you specify here are included in the Live Tail session.</p> <p>If you specify this field, you can't also specify the <code>logStreamNamePrefixes</code> field.</p> <note> <p>You can specify this parameter only if you specify only one log group in <code>logGroupIdentifiers</code>.</p> </note>
            log_stream_name_prefixes: <p>If you specify this parameter, then only log events in the log streams that have names that start with the prefixes that you specify here are included in the Live Tail session.</p> <p>If you specify this field, you can't also specify the <code>logStreamNames</code> field.</p> <note> <p>You can specify this parameter only if you specify only one log group in <code>logGroupIdentifiers</code>.</p> </note>
            log_event_filter_pattern: <p>An optional pattern to use to filter the results to include only log events that match the pattern. For example, a filter pattern of <code>error 404</code> causes only log events that include both <code>error</code> and <code>404</code> to be included in the Live Tail stream.</p> <p>Regular expression filter patterns are supported.</p> <p>For more information about filter pattern syntax, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html">Filter and Pattern Syntax</a>.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.start_live_tail_request.StartLiveTailRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.start_live_tail_response.StartLiveTailResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.start_live_tail

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.start_live_tail.start_live_tail(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.start_live_tail_request.StartLiveTailRequest = {
            "log_group_identifiers": log_group_identifiers
        }
        if log_stream_names is not None:
            input_["log_stream_names"] = log_stream_names
        if log_stream_name_prefixes is not None:
            input_["log_stream_name_prefixes"] = log_stream_name_prefixes
        if log_event_filter_pattern is not None:
            input_["log_event_filter_pattern"] = log_event_filter_pattern

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def start_query(
        self,
        start_time: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        end_time: "capo_cloudwatch_logs.types.timestamp.Timestamp",
        query_string: "capo_cloudwatch_logs.types.query_string.QueryString",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        query_language: Optional[
            "capo_cloudwatch_logs.types.query_language.QueryLanguage"
        ] = None,
        log_group_name: Optional[
            "capo_cloudwatch_logs.types.log_group_name.LogGroupName"
        ] = None,
        log_group_names: Optional[
            "capo_cloudwatch_logs.types.log_group_names.LogGroupNames"
        ] = None,
        log_group_identifiers: Optional[
            "capo_cloudwatch_logs.types.log_group_identifiers.LogGroupIdentifiers"
        ] = None,
        limit: Optional[
            "capo_cloudwatch_logs.types.events_limit_start_query.EventsLimitStartQuery"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.start_query_response.StartQueryResponse":
        """<p>Starts a query of one or more log groups or data sources using CloudWatch Logs Insights. You specify the log groups or data sources and time range to query and the query string to use. You can query up to 10 data sources in a single query.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html">CloudWatch Logs Insights Query Syntax</a>.</p> <p>After you run a query using <code>StartQuery</code>, the query results are stored by CloudWatch Logs. You can use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetQueryResults.html">GetQueryResults</a> to retrieve the results of a query, using the <code>queryId</code> that <code>StartQuery</code> returns. </p> <p>Interactive queries started with <code>StartQuery</code> share concurrency limits with automated scheduled query executions. Both types of queries count toward the same regional concurrent query quota, so high scheduled query activity may affect the availability of concurrent slots for interactive queries.</p> <note> <p>To specify the log groups to query, a <code>StartQuery</code> operation must include one of the following:</p> <ul> <li> <p>Either exactly one of the following parameters: <code>logGroupName</code>, <code>logGroupNames</code>, or <code>logGroupIdentifiers</code> </p> </li> <li> <p>Or the <code>queryString</code> must include a <code>SOURCE</code> command to select log groups for the query. The <code>SOURCE</code> command can select log groups based on log group name prefix, account ID, and log class, or select data sources using dataSource syntax in LogsQL, PPL, and SQL. In LogsQL, the <code>SOURCE</code> command also supports filtering by log group tags. </p> <p>For more information about the <code>SOURCE</code> command, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax-Source.html">SOURCE</a>.</p> </li> </ul> </note> <p>If you have associated a KMS key with the query results in this account, then <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_StartQuery.html">StartQuery</a> uses that key to encrypt the results when it stores them. If no key is associated with query results, the query results are encrypted with the default CloudWatch Logs encryption method.</p> <p>Queries time out after 60 minutes of runtime. If your queries are timing out, reduce the time range being searched or partition your query into a number of queries.</p> <p>If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account to start a query in a linked source account. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html">CloudWatch cross-account observability</a>. For a cross-account <code>StartQuery</code> operation, the query definition must be defined in the monitoring account.</p> <p>You can have up to 100 concurrent CloudWatch Logs insights queries, including queries that have been added to dashboards. </p>

        Args:
            query_language: <p>Specify the query language to use for this query. The options are Logs Insights QL, OpenSearch PPL, and OpenSearch SQL. For more information about the query languages that CloudWatch Logs supports, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_AnalyzeLogData_Languages.html">Supported query languages</a>.</p>
            log_group_name: <p>The log group on which to perform the query.</p> <note> <p>A <code>StartQuery</code> operation must include exactly one of the following parameters: <code>logGroupName</code>, <code>logGroupNames</code>, or <code>logGroupIdentifiers</code>. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the <code>querystring</code> instead of here.</p> </note>
            log_group_names: <p>The list of log groups to be queried. You can include up to 50 log groups.</p> <note> <p>A <code>StartQuery</code> operation must include exactly one of the following parameters: <code>logGroupName</code>, <code>logGroupNames</code>, or <code>logGroupIdentifiers</code>. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the <code>querystring</code> instead of here.</p> </note>
            log_group_identifiers: <p>The list of log groups to query. You can include up to 50 log groups.</p> <p>You can specify them by the log group name or ARN. If a log group that you're querying is in a source account and you're using a monitoring account, you must specify the ARN of the log group here. The query definition must also be defined in the monitoring account.</p> <p>If you specify an ARN, use the format arn:aws:logs:<i>region</i>:<i>account-id</i>:log-group:<i>log_group_name</i> Don't include an * at the end.</p> <p>A <code>StartQuery</code> operation must include exactly one of the following parameters: <code>logGroupName</code>, <code>logGroupNames</code>, or <code>logGroupIdentifiers</code>. The exception is queries using the OpenSearch Service SQL query language, where you specify the log group names inside the <code>querystring</code> instead of here. </p>
            start_time: <p>The beginning of the time range to query. The range is inclusive, so the specified start time is included in the query. Specified as epoch time, the number of seconds since <code>January 1, 1970, 00:00:00 UTC</code>.</p>
            end_time: <p>The end of the time range to query. The range is inclusive, so the specified end time is included in the query. Specified as epoch time, the number of seconds since <code>January 1, 1970, 00:00:00 UTC</code>.</p>
            query_string: <p>The query string to use. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html">CloudWatch Logs Insights Query Syntax</a>.</p>
            limit: <p>The maximum number of log events to return from the query. The maximum limit is 100,000. The maximum events returned in a single GetQueryResults API call is 10,000 log events per request. You can retrieve up to 100,000 log event results from a query by paginating with the <code>nextToken</code>. 100,000 limit is only supported for Logs Insights QL and is currently not supported for PPL and SQL query languages.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.limit_exceeded_exception.LimitExceededException: <p>You have reached the maximum number of resources that can be created.</p>
            capo_cloudwatch_logs.errors.malformed_query_exception.MalformedQueryException: <p>The query string is not valid. Details about this error are displayed in a <code>QueryCompileError</code> object. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_QueryCompileError.html">QueryCompileError</a>.</p> <p>For more information about valid query syntax, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html">CloudWatch Logs Insights Query Syntax</a>.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.start_query_request.StartQueryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.start_query_response.StartQueryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.start_query

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.start_query.start_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.start_query_request.StartQueryRequest = {
            "start_time": start_time,
            "end_time": end_time,
            "query_string": query_string,
        }
        if query_language is not None:
            input_["query_language"] = query_language
        if log_group_name is not None:
            input_["log_group_name"] = log_group_name
        if log_group_names is not None:
            input_["log_group_names"] = log_group_names
        if log_group_identifiers is not None:
            input_["log_group_identifiers"] = log_group_identifiers
        if limit is not None:
            input_["limit"] = limit

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_query(
        self,
        query_id: "capo_cloudwatch_logs.types.query_id.QueryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.stop_query_response.StopQueryResponse":
        """<p>Stops a CloudWatch Logs Insights query that is in progress. If the query has already ended, the operation returns an error indicating that the specified query is not running.</p> <p>This operation can be used to cancel both interactive queries and individual scheduled query executions. When used with scheduled queries, <code>StopQuery</code> cancels only the specific execution identified by the query ID, not the scheduled query configuration itself.</p>

        Args:
            query_id: <p>The ID number of the query to stop. To find this ID number, use <code>DescribeQueries</code>.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.stop_query_request.StopQueryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.stop_query_response.StopQueryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.stop_query

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.stop_query.stop_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.stop_query_request.StopQueryRequest = {
            "query_id": query_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_log_group(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        tags: "capo_cloudwatch_logs.types.tags.Tags",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<important> <p>The TagLogGroup operation is on the path to deprecation. We recommend that you use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html">TagResource</a> instead.</p> </important> <p>Adds or updates the specified tags for the specified log group.</p> <p>To list the tags for a log group, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html">ListTagsForResource</a>. To remove tags, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html">UntagResource</a>.</p> <p>For more information about tags, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#log-group-tagging">Tag Log Groups in Amazon CloudWatch Logs</a> in the <i>Amazon CloudWatch Logs User Guide</i>.</p> <p>CloudWatch Logs doesn't support IAM policies that prevent users from assigning specified tags to log groups using the <code>aws:Resource/<i>key-name</i> </code> or <code>aws:TagKeys</code> condition keys. For more information about using tags to control access, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html">Controlling access to Amazon Web Services resources using tags</a>.</p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            tags: <p>The key-value pairs to use for the tags.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.tag_log_group_request.TagLogGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.tag_log_group

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.tag_log_group.tag_log_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.tag_log_group_request.TagLogGroupRequest = {
            "log_group_name": log_group_name,
            "tags": tags,
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
        resource_arn: "capo_cloudwatch_logs.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_cloudwatch_logs.types.tags.Tags",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Assigns one or more tags (key-value pairs) to the specified CloudWatch Logs resource. Currently, the only CloudWatch Logs resources that can be tagged are log groups and destinations. </p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with a resource that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a CloudWatch Logs resource.</p>

        Args:
            resource_arn: <p>The ARN of the resource that you're adding tags to.</p> <p>The ARN format of a log group is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:log-group:<i>log-group-name</i> </code> </p> <p>The ARN format of a destination is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:destination:<i>destination-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p>
            tags: <p>The list of key-value pairs to associate with the resource.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.too_many_tags_exception.TooManyTagsException: <p>A resource can have no more than 50 tags.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.tag_resource

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.tag_resource_request.TagResourceRequest = {
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

    def test_metric_filter(
        self,
        filter_pattern: "capo_cloudwatch_logs.types.filter_pattern.FilterPattern",
        log_event_messages: "capo_cloudwatch_logs.types.test_event_messages.TestEventMessages",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.test_metric_filter_response.TestMetricFilterResponse":
        """<p>Tests the filter pattern of a metric filter against a sample of log event messages. You can use this operation to validate the correctness of a metric filter pattern.</p>

        Args:
            log_event_messages: <p>The log event messages to test.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.test_metric_filter_request.TestMetricFilterRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.test_metric_filter_response.TestMetricFilterResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.test_metric_filter

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.test_metric_filter.test_metric_filter(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.test_metric_filter_request.TestMetricFilterRequest = {
            "filter_pattern": filter_pattern,
            "log_event_messages": log_event_messages,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_transformer(
        self,
        transformer_config: "capo_cloudwatch_logs.types.processors.Processors",
        log_event_messages: "capo_cloudwatch_logs.types.test_event_messages.TestEventMessages",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> "capo_cloudwatch_logs.types.test_transformer_response.TestTransformerResponse":
        """<p>Use this operation to test a log transformer. You enter the transformer configuration and a set of log events to test with. The operation responds with an array that includes the original log events and the transformed versions.</p>

        Args:
            transformer_config: <p>This structure contains the configuration of this log transformer that you want to test. A log transformer is an array of processors, where each processor applies one type of transformation to the log events that are ingested.</p>
            log_event_messages: <p>An array of the raw log events that you want to use to test this transformer.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_operation_exception.InvalidOperationException: <p>The operation is not valid on the specified resource.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.test_transformer_request.TestTransformerRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.test_transformer_response.TestTransformerResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.test_transformer

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.test_transformer.test_transformer(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.test_transformer_request.TestTransformerRequest = {
            "transformer_config": transformer_config,
            "log_event_messages": log_event_messages,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def untag_log_group(
        self,
        log_group_name: "capo_cloudwatch_logs.types.log_group_name.LogGroupName",
        tags: "capo_cloudwatch_logs.types.tag_list.TagList",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<important> <p>The UntagLogGroup operation is on the path to deprecation. We recommend that you use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html">UntagResource</a> instead.</p> </important> <p>Removes the specified tags from the specified log group.</p> <p>To list the tags for a log group, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html">ListTagsForResource</a>. To add tags, use <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html">TagResource</a>.</p> <p>When using IAM policies to control tag management for CloudWatch Logs log groups, the condition keys <code>aws:Resource/key-name</code> and <code>aws:TagKeys</code> cannot be used to restrict which tags users can assign. </p>

        Args:
            log_group_name: <p>The name of the log group.</p>
            tags: <p>The tag keys. The corresponding tags are removed from the log group.</p>

        Raises:
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.untag_log_group_request.UntagLogGroupRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.untag_log_group

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.untag_log_group.untag_log_group(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.untag_log_group_request.UntagLogGroupRequest = {
            "log_group_name": log_group_name,
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
        resource_arn: "capo_cloudwatch_logs.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_cloudwatch_logs.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
    ) -> None:
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The ARN of the CloudWatch Logs resource that you're removing tags from.</p> <p>The ARN format of a log group is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:log-group:<i>log-group-name</i> </code> </p> <p>The ARN format of a destination is <code>arn:aws:logs:<i>Region</i>:<i>account-id</i>:destination:<i>destination-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html">CloudWatch Logs resources and operations</a>.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.untag_resource

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.untag_resource_request.UntagResourceRequest = {
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

    def update_anomaly(
        self,
        anomaly_detector_arn: "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        anomaly_id: Optional["capo_cloudwatch_logs.types.anomaly_id.AnomalyId"] = None,
        pattern_id: Optional["capo_cloudwatch_logs.types.pattern_id.PatternId"] = None,
        suppression_type: Optional[
            "capo_cloudwatch_logs.types.suppression_type.SuppressionType"
        ] = None,
        suppression_period: Optional[
            "capo_cloudwatch_logs.types.suppression_period.SuppressionPeriod"
        ] = None,
        baseline: Optional["capo_cloudwatch_logs.types.baseline.Baseline"] = None,
    ) -> None:
        """<p>Use this operation to <i>suppress</i> anomaly detection for a specified anomaly or pattern. If you suppress an anomaly, CloudWatch Logs won't report new occurrences of that anomaly and won't update that anomaly with new data. If you suppress a pattern, CloudWatch Logs won't report any anomalies related to that pattern.</p> <p>You must specify either <code>anomalyId</code> or <code>patternId</code>, but you can't specify both parameters in the same operation.</p> <p>If you have previously used this operation to suppress detection of a pattern or anomaly, you can use it again to cause CloudWatch Logs to end the suppression. To do this, use this operation and specify the anomaly or pattern to stop suppressing, and omit the <code>suppressionType</code> and <code>suppressionPeriod</code> parameters.</p>

        Args:
            anomaly_id: <p>If you are suppressing or unsuppressing an anomaly, specify its unique ID here. You can find anomaly IDs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html">ListAnomalies</a> operation.</p>
            pattern_id: <p>If you are suppressing or unsuppressing an pattern, specify its unique ID here. You can find pattern IDs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html">ListAnomalies</a> operation.</p>
            anomaly_detector_arn: <p>The ARN of the anomaly detector that this operation is to act on.</p>
            suppression_type: <p>Use this to specify whether the suppression to be temporary or infinite. If you specify <code>LIMITED</code>, you must also specify a <code>suppressionPeriod</code>. If you specify <code>INFINITE</code>, any value for <code>suppressionPeriod</code> is ignored. </p>
            suppression_period: <p>If you are temporarily suppressing an anomaly or pattern, use this structure to specify how long the suppression is to last.</p>
            baseline: <p>Set this to <code>true</code> to prevent CloudWatch Logs from displaying this behavior as an anomaly in the future. The behavior is then treated as baseline behavior. However, if similar but more severe occurrences of this behavior occur in the future, those will still be reported as anomalies. </p> <p>The default is <code>false</code> </p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.update_anomaly_request.UpdateAnomalyRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.update_anomaly

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.update_anomaly.update_anomaly(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.update_anomaly_request.UpdateAnomalyRequest = {
            "anomaly_detector_arn": anomaly_detector_arn
        }
        if anomaly_id is not None:
            input_["anomaly_id"] = anomaly_id
        if pattern_id is not None:
            input_["pattern_id"] = pattern_id
        if suppression_type is not None:
            input_["suppression_type"] = suppression_type
        if suppression_period is not None:
            input_["suppression_period"] = suppression_period
        if baseline is not None:
            input_["baseline"] = baseline

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_delivery_configuration(
        self,
        id: "capo_cloudwatch_logs.types.delivery_id.DeliveryId",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        record_fields: Optional[
            "capo_cloudwatch_logs.types.record_fields.RecordFields"
        ] = None,
        field_delimiter: Optional[
            "capo_cloudwatch_logs.types.field_delimiter.FieldDelimiter"
        ] = None,
        s3_delivery_configuration: Optional[
            "capo_cloudwatch_logs.types.s3_delivery_configuration.S3DeliveryConfiguration"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.update_delivery_configuration_response.UpdateDeliveryConfigurationResponse":
        """<p>Use this operation to update the configuration of a <a href="https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html">delivery</a> to change either the S3 path pattern or the format of the delivered logs. You can't use this operation to change the source or destination of the delivery.</p>

        Args:
            id: <p>The ID of the delivery to be updated by this request.</p>
            record_fields: <p>The list of record fields to be delivered to the destination, in order. If the delivery's log source has mandatory fields, they must be included in this list.</p>
            field_delimiter: <p>The field delimiter to use between record fields when the final output format of a delivery is in <code>Plain</code>, <code>W3C</code>, or <code>Raw</code> format.</p>
            s3_delivery_configuration: <p>This structure contains parameters that are valid only when the delivery's delivery destination is an S3 bucket.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.update_delivery_configuration_request.UpdateDeliveryConfigurationRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.update_delivery_configuration_response.UpdateDeliveryConfigurationResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.update_delivery_configuration

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.update_delivery_configuration.update_delivery_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.update_delivery_configuration_request.UpdateDeliveryConfigurationRequest = {
            "id": id
        }
        if record_fields is not None:
            input_["record_fields"] = record_fields
        if field_delimiter is not None:
            input_["field_delimiter"] = field_delimiter
        if s3_delivery_configuration is not None:
            input_["s3_delivery_configuration"] = s3_delivery_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_log_anomaly_detector(
        self,
        anomaly_detector_arn: "capo_cloudwatch_logs.types.anomaly_detector_arn.AnomalyDetectorArn",
        enabled: "capo_cloudwatch_logs.types.boolean.Boolean",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        evaluation_frequency: Optional[
            "capo_cloudwatch_logs.types.evaluation_frequency.EvaluationFrequency"
        ] = None,
        filter_pattern: Optional[
            "capo_cloudwatch_logs.types.filter_pattern.FilterPattern"
        ] = None,
        anomaly_visibility_time: Optional[
            "capo_cloudwatch_logs.types.anomaly_visibility_time.AnomalyVisibilityTime"
        ] = None,
    ) -> None:
        """<p>Updates an existing log anomaly detector.</p>

        Args:
            anomaly_detector_arn: <p>The ARN of the anomaly detector that you want to update.</p>
            evaluation_frequency: <p>Specifies how often the anomaly detector runs and look for anomalies. Set this value according to the frequency that the log group receives new logs. For example, if the log group receives new log events every 10 minutes, then setting <code>evaluationFrequency</code> to <code>FIFTEEN_MIN</code> might be appropriate.</p>
            anomaly_visibility_time: <p>The number of days to use as the life cycle of anomalies. After this time, anomalies are automatically baselined and the anomaly detector model will treat new occurrences of similar event as normal. Therefore, if you do not correct the cause of an anomaly during this time, it will be considered normal going forward and will not be detected.</p>
            enabled: <p>Use this parameter to pause or restart the anomaly detector. </p>

        Raises:
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.operation_aborted_exception.OperationAbortedException: <p>Multiple concurrent requests to update the same resource were in conflict.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.update_log_anomaly_detector_request.UpdateLogAnomalyDetectorRequest]",
        ) -> OperationResponse[None]:
            import capo_cloudwatch_logs._operations.logs_20140328.update_log_anomaly_detector

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.update_log_anomaly_detector.update_log_anomaly_detector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.update_log_anomaly_detector_request.UpdateLogAnomalyDetectorRequest = {
            "anomaly_detector_arn": anomaly_detector_arn,
            "enabled": enabled,
        }
        if evaluation_frequency is not None:
            input_["evaluation_frequency"] = evaluation_frequency
        if filter_pattern is not None:
            input_["filter_pattern"] = filter_pattern
        if anomaly_visibility_time is not None:
            input_["anomaly_visibility_time"] = anomaly_visibility_time

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_lookup_table(
        self,
        lookup_table_arn: "capo_cloudwatch_logs.types.arn.Arn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        description: Optional[
            "capo_cloudwatch_logs.types.lookup_table_description.LookupTableDescription"
        ] = None,
        table_body: Optional["capo_cloudwatch_logs.types.table_body.TableBody"] = None,
        query_id: Optional["capo_cloudwatch_logs.types.query_id.QueryId"] = None,
        kms_key_id: Optional["capo_cloudwatch_logs.types.kms_key_id.KmsKeyId"] = None,
    ) -> "capo_cloudwatch_logs.types.update_lookup_table_response.UpdateLookupTableResponse":
        """<p>Updates an existing lookup table by replacing all of its content with new CSV data or CloudWatch Logs query results. After the update completes, queries that use this table use the new data.</p> <p>This is a full replacement operation. All existing content is replaced. You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>

        Args:
            lookup_table_arn: <p>The ARN of the lookup table to update.</p>
            description: <p>An updated description of the lookup table.</p>
            table_body: <p>The new CSV content to replace the existing data. The first row must be a header row with column names. The content must use UTF-8 encoding and not exceed 10 MB.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>
            query_id: <p>The ID of a completed or cancelled CloudWatch Logs query whose results replace the lookup table content. A cancelled query replaces the content with the partial results that were available when the query was stopped.</p> <p>You must specify either <code>tableBody</code> or <code>queryId</code>, but not both.</p>
            kms_key_id: <p>The ARN of the KMS key to use to encrypt the lookup table data. You can use this parameter to add, update, or remove the KMS key. To remove the KMS key and use an Amazon Web Services-owned key instead, specify an empty string.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.invalid_parameter_exception.InvalidParameterException: <p>A parameter is specified incorrectly.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.service_unavailable_exception.ServiceUnavailableException: <p>The service cannot complete the request.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.update_lookup_table_request.UpdateLookupTableRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.update_lookup_table_response.UpdateLookupTableResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.update_lookup_table

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.update_lookup_table.update_lookup_table(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.update_lookup_table_request.UpdateLookupTableRequest = {
            "lookup_table_arn": lookup_table_arn
        }
        if description is not None:
            input_["description"] = description
        if table_body is not None:
            input_["table_body"] = table_body
        if query_id is not None:
            input_["query_id"] = query_id
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_scheduled_query(
        self,
        identifier: "capo_cloudwatch_logs.types.scheduled_query_identifier.ScheduledQueryIdentifier",
        query_language: "capo_cloudwatch_logs.types.query_language.QueryLanguage",
        query_string: "capo_cloudwatch_logs.types.query_string.QueryString",
        schedule_expression: "capo_cloudwatch_logs.types.schedule_expression.ScheduleExpression",
        execution_role_arn: "capo_cloudwatch_logs.types.role_arn.RoleArn",
        *,
        config_overrides: Optional[CloudWatchLogsClientConfig] = None,
        description: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_description.ScheduledQueryDescription"
        ] = None,
        log_group_identifiers: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_log_group_identifiers.ScheduledQueryLogGroupIdentifiers"
        ] = None,
        timezone: Optional[
            "capo_cloudwatch_logs.types.schedule_timezone.ScheduleTimezone"
        ] = None,
        start_time_offset: Optional[
            "capo_cloudwatch_logs.types.start_time_offset.StartTimeOffset"
        ] = None,
        end_time_offset: Optional[
            "capo_cloudwatch_logs.types.end_time_offset.EndTimeOffset"
        ] = None,
        destination_configuration: Optional[
            "capo_cloudwatch_logs.types.destination_configuration.DestinationConfiguration"
        ] = None,
        schedule_start_time: Optional[
            "capo_cloudwatch_logs.types.timestamp.Timestamp"
        ] = None,
        schedule_end_time: Optional[
            "capo_cloudwatch_logs.types.timestamp.Timestamp"
        ] = None,
        state: Optional[
            "capo_cloudwatch_logs.types.scheduled_query_state.ScheduledQueryState"
        ] = None,
    ) -> "capo_cloudwatch_logs.types.update_scheduled_query_response.UpdateScheduledQueryResponse":
        """<p>Updates an existing scheduled query with new configuration. This operation uses PUT semantics, allowing modification of query parameters, schedule, and destinations.</p>

        Args:
            identifier: <p>The ARN or name of the scheduled query to update.</p>
            description: <p>An updated description for the scheduled query.</p>
            query_language: <p>The updated query language for the scheduled query.</p>
            query_string: <p>The updated query string to execute.</p>
            log_group_identifiers: <p>The updated array of log group names or ARNs to query.</p>
            schedule_expression: <p>The updated cron expression that defines when the scheduled query runs.</p>
            timezone: <p>The updated timezone for evaluating the schedule expression.</p>
            start_time_offset: <p>The updated time offset in seconds that defines the lookback period for the query.</p>
            end_time_offset: <p>The updated time offset in seconds that defines the end of the lookback period for the query.</p>
            destination_configuration: <p>The updated configuration for where to deliver query results.</p>
            schedule_start_time: <p>The updated start time for the scheduled query in Unix epoch format.</p>
            schedule_end_time: <p>The updated end time for the scheduled query in Unix epoch format.</p>
            execution_role_arn: <p>The updated ARN of the IAM role that grants permissions to execute the query and deliver results.</p>
            state: <p>The updated state of the scheduled query.</p>

        Raises:
            capo_cloudwatch_logs.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_cloudwatch_logs.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_cloudwatch_logs.errors.internal_server_exception.InternalServerException: <p>An internal server error occurred while processing the request. This exception is returned when the service encounters an unexpected condition that prevents it from fulfilling the request.</p>
            capo_cloudwatch_logs.errors.resource_not_found_exception.ResourceNotFoundException: <p>The specified resource does not exist.</p>
            capo_cloudwatch_logs.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_cloudwatch_logs.errors.validation_exception.ValidationException: <p>One of the parameters for the request is not valid.</p>
            capo_cloudwatch_logs.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudwatch_logs.types.update_scheduled_query_request.UpdateScheduledQueryRequest]",
        ) -> OperationResponse[
            "capo_cloudwatch_logs.types.update_scheduled_query_response.UpdateScheduledQueryResponse"
        ]:
            import capo_cloudwatch_logs._operations.logs_20140328.update_scheduled_query

            output, http_response = (
                capo_cloudwatch_logs._operations.logs_20140328.update_scheduled_query.update_scheduled_query(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudwatch_logs.types.update_scheduled_query_request.UpdateScheduledQueryRequest = {
            "identifier": identifier,
            "query_language": query_language,
            "query_string": query_string,
            "schedule_expression": schedule_expression,
            "execution_role_arn": execution_role_arn,
        }
        if description is not None:
            input_["description"] = description
        if log_group_identifiers is not None:
            input_["log_group_identifiers"] = log_group_identifiers
        if timezone is not None:
            input_["timezone"] = timezone
        if start_time_offset is not None:
            input_["start_time_offset"] = start_time_offset
        if end_time_offset is not None:
            input_["end_time_offset"] = end_time_offset
        if destination_configuration is not None:
            input_["destination_configuration"] = destination_configuration
        if schedule_start_time is not None:
            input_["schedule_start_time"] = schedule_start_time
        if schedule_end_time is not None:
            input_["schedule_end_time"] = schedule_end_time
        if state is not None:
            input_["state"] = state

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
