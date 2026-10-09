"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#AmazonDMSv20160101``."""

import warnings
from collections.abc import AsyncIterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import AsyncBaseHandler, AsyncClient

import capo_database_migration_service._auth._signers
import capo_database_migration_service._auth._sigv4
from capo_database_migration_service._auth._identity import Credentials
from capo_database_migration_service._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_database_migration_service._auth._zapros_handler import AuthMiddleware
from capo_database_migration_service._pagination import resolve_path as _resolve_path
from capo_database_migration_service._services._aws_config import aaws_config
from capo_database_migration_service._services._pipeline import (
    AsyncInterceptor,
    AsyncOperationOptions,
    AsyncOperationRequest,
    AsyncOperationResponse,
    aexecute_pipeline,
    aretry,
)

if TYPE_CHECKING:
    import capo_database_migration_service.types.add_tags_to_resource_message
    import capo_database_migration_service.types.add_tags_to_resource_response
    import capo_database_migration_service.types.apply_pending_maintenance_action_message
    import capo_database_migration_service.types.apply_pending_maintenance_action_response
    import capo_database_migration_service.types.arn_list
    import capo_database_migration_service.types.assessment_report_types_list
    import capo_database_migration_service.types.batch_start_recommendations_request
    import capo_database_migration_service.types.batch_start_recommendations_response
    import capo_database_migration_service.types.boolean
    import capo_database_migration_service.types.boolean_optional
    import capo_database_migration_service.types.cancel_metadata_model_conversion_message
    import capo_database_migration_service.types.cancel_metadata_model_conversion_response
    import capo_database_migration_service.types.cancel_metadata_model_creation_message
    import capo_database_migration_service.types.cancel_metadata_model_creation_response
    import capo_database_migration_service.types.cancel_replication_task_assessment_run_message
    import capo_database_migration_service.types.cancel_replication_task_assessment_run_response
    import capo_database_migration_service.types.certificate_wallet
    import capo_database_migration_service.types.compute_config
    import capo_database_migration_service.types.create_data_migration_message
    import capo_database_migration_service.types.create_data_migration_response
    import capo_database_migration_service.types.create_data_provider_message
    import capo_database_migration_service.types.create_data_provider_response
    import capo_database_migration_service.types.create_endpoint_message
    import capo_database_migration_service.types.create_endpoint_response
    import capo_database_migration_service.types.create_event_subscription_message
    import capo_database_migration_service.types.create_event_subscription_response
    import capo_database_migration_service.types.create_fleet_advisor_collector_request
    import capo_database_migration_service.types.create_fleet_advisor_collector_response
    import capo_database_migration_service.types.create_instance_profile_message
    import capo_database_migration_service.types.create_instance_profile_response
    import capo_database_migration_service.types.create_migration_project_message
    import capo_database_migration_service.types.create_migration_project_response
    import capo_database_migration_service.types.create_replication_config_message
    import capo_database_migration_service.types.create_replication_config_response
    import capo_database_migration_service.types.create_replication_instance_message
    import capo_database_migration_service.types.create_replication_instance_response
    import capo_database_migration_service.types.create_replication_subnet_group_message
    import capo_database_migration_service.types.create_replication_subnet_group_response
    import capo_database_migration_service.types.create_replication_task_message
    import capo_database_migration_service.types.create_replication_task_response
    import capo_database_migration_service.types.data_migration
    import capo_database_migration_service.types.data_provider_descriptor_definition_list
    import capo_database_migration_service.types.data_provider_settings
    import capo_database_migration_service.types.delete_certificate_message
    import capo_database_migration_service.types.delete_certificate_response
    import capo_database_migration_service.types.delete_collector_request
    import capo_database_migration_service.types.delete_connection_message
    import capo_database_migration_service.types.delete_connection_response
    import capo_database_migration_service.types.delete_data_migration_message
    import capo_database_migration_service.types.delete_data_migration_response
    import capo_database_migration_service.types.delete_data_provider_message
    import capo_database_migration_service.types.delete_data_provider_response
    import capo_database_migration_service.types.delete_endpoint_message
    import capo_database_migration_service.types.delete_endpoint_response
    import capo_database_migration_service.types.delete_event_subscription_message
    import capo_database_migration_service.types.delete_event_subscription_response
    import capo_database_migration_service.types.delete_fleet_advisor_databases_request
    import capo_database_migration_service.types.delete_fleet_advisor_databases_response
    import capo_database_migration_service.types.delete_instance_profile_message
    import capo_database_migration_service.types.delete_instance_profile_response
    import capo_database_migration_service.types.delete_migration_project_message
    import capo_database_migration_service.types.delete_migration_project_response
    import capo_database_migration_service.types.delete_replication_config_message
    import capo_database_migration_service.types.delete_replication_config_response
    import capo_database_migration_service.types.delete_replication_instance_message
    import capo_database_migration_service.types.delete_replication_instance_response
    import capo_database_migration_service.types.delete_replication_subnet_group_message
    import capo_database_migration_service.types.delete_replication_subnet_group_response
    import capo_database_migration_service.types.delete_replication_task_assessment_run_message
    import capo_database_migration_service.types.delete_replication_task_assessment_run_response
    import capo_database_migration_service.types.delete_replication_task_message
    import capo_database_migration_service.types.delete_replication_task_response
    import capo_database_migration_service.types.describe_account_attributes_message
    import capo_database_migration_service.types.describe_account_attributes_response
    import capo_database_migration_service.types.describe_applicable_individual_assessments_message
    import capo_database_migration_service.types.describe_applicable_individual_assessments_response
    import capo_database_migration_service.types.describe_certificates_message
    import capo_database_migration_service.types.describe_certificates_response
    import capo_database_migration_service.types.describe_connections_message
    import capo_database_migration_service.types.describe_connections_response
    import capo_database_migration_service.types.describe_conversion_configuration_message
    import capo_database_migration_service.types.describe_conversion_configuration_response
    import capo_database_migration_service.types.describe_data_migrations_message
    import capo_database_migration_service.types.describe_data_migrations_response
    import capo_database_migration_service.types.describe_data_providers_message
    import capo_database_migration_service.types.describe_data_providers_response
    import capo_database_migration_service.types.describe_endpoint_settings_message
    import capo_database_migration_service.types.describe_endpoint_settings_response
    import capo_database_migration_service.types.describe_endpoint_types_message
    import capo_database_migration_service.types.describe_endpoint_types_response
    import capo_database_migration_service.types.describe_endpoints_message
    import capo_database_migration_service.types.describe_endpoints_response
    import capo_database_migration_service.types.describe_engine_versions_message
    import capo_database_migration_service.types.describe_engine_versions_response
    import capo_database_migration_service.types.describe_event_categories_message
    import capo_database_migration_service.types.describe_event_categories_response
    import capo_database_migration_service.types.describe_event_subscriptions_message
    import capo_database_migration_service.types.describe_event_subscriptions_response
    import capo_database_migration_service.types.describe_events_message
    import capo_database_migration_service.types.describe_events_response
    import capo_database_migration_service.types.describe_extension_pack_associations_message
    import capo_database_migration_service.types.describe_extension_pack_associations_response
    import capo_database_migration_service.types.describe_fleet_advisor_collectors_request
    import capo_database_migration_service.types.describe_fleet_advisor_collectors_response
    import capo_database_migration_service.types.describe_fleet_advisor_databases_request
    import capo_database_migration_service.types.describe_fleet_advisor_databases_response
    import capo_database_migration_service.types.describe_fleet_advisor_lsa_analysis_request
    import capo_database_migration_service.types.describe_fleet_advisor_lsa_analysis_response
    import capo_database_migration_service.types.describe_fleet_advisor_schema_object_summary_request
    import capo_database_migration_service.types.describe_fleet_advisor_schema_object_summary_response
    import capo_database_migration_service.types.describe_fleet_advisor_schemas_request
    import capo_database_migration_service.types.describe_fleet_advisor_schemas_response
    import capo_database_migration_service.types.describe_instance_profiles_message
    import capo_database_migration_service.types.describe_instance_profiles_response
    import capo_database_migration_service.types.describe_metadata_model_assessments_message
    import capo_database_migration_service.types.describe_metadata_model_assessments_response
    import capo_database_migration_service.types.describe_metadata_model_children_message
    import capo_database_migration_service.types.describe_metadata_model_children_response
    import capo_database_migration_service.types.describe_metadata_model_conversions_message
    import capo_database_migration_service.types.describe_metadata_model_conversions_response
    import capo_database_migration_service.types.describe_metadata_model_creations_message
    import capo_database_migration_service.types.describe_metadata_model_creations_response
    import capo_database_migration_service.types.describe_metadata_model_exports_as_script_message
    import capo_database_migration_service.types.describe_metadata_model_exports_as_script_response
    import capo_database_migration_service.types.describe_metadata_model_exports_to_target_message
    import capo_database_migration_service.types.describe_metadata_model_exports_to_target_response
    import capo_database_migration_service.types.describe_metadata_model_imports_message
    import capo_database_migration_service.types.describe_metadata_model_imports_response
    import capo_database_migration_service.types.describe_metadata_model_message
    import capo_database_migration_service.types.describe_metadata_model_response
    import capo_database_migration_service.types.describe_migration_projects_message
    import capo_database_migration_service.types.describe_migration_projects_response
    import capo_database_migration_service.types.describe_orderable_replication_instances_message
    import capo_database_migration_service.types.describe_orderable_replication_instances_response
    import capo_database_migration_service.types.describe_pending_maintenance_actions_message
    import capo_database_migration_service.types.describe_pending_maintenance_actions_response
    import capo_database_migration_service.types.describe_recommendation_limitations_request
    import capo_database_migration_service.types.describe_recommendation_limitations_response
    import capo_database_migration_service.types.describe_recommendations_request
    import capo_database_migration_service.types.describe_recommendations_response
    import capo_database_migration_service.types.describe_refresh_schemas_status_message
    import capo_database_migration_service.types.describe_refresh_schemas_status_response
    import capo_database_migration_service.types.describe_replication_configs_message
    import capo_database_migration_service.types.describe_replication_configs_response
    import capo_database_migration_service.types.describe_replication_instance_task_logs_message
    import capo_database_migration_service.types.describe_replication_instance_task_logs_response
    import capo_database_migration_service.types.describe_replication_instances_message
    import capo_database_migration_service.types.describe_replication_instances_response
    import capo_database_migration_service.types.describe_replication_subnet_groups_message
    import capo_database_migration_service.types.describe_replication_subnet_groups_response
    import capo_database_migration_service.types.describe_replication_table_statistics_message
    import capo_database_migration_service.types.describe_replication_table_statistics_response
    import capo_database_migration_service.types.describe_replication_task_assessment_results_message
    import capo_database_migration_service.types.describe_replication_task_assessment_results_response
    import capo_database_migration_service.types.describe_replication_task_assessment_runs_message
    import capo_database_migration_service.types.describe_replication_task_assessment_runs_response
    import capo_database_migration_service.types.describe_replication_task_individual_assessments_message
    import capo_database_migration_service.types.describe_replication_task_individual_assessments_response
    import capo_database_migration_service.types.describe_replication_tasks_message
    import capo_database_migration_service.types.describe_replication_tasks_response
    import capo_database_migration_service.types.describe_replications_message
    import capo_database_migration_service.types.describe_replications_response
    import capo_database_migration_service.types.describe_schemas_message
    import capo_database_migration_service.types.describe_schemas_response
    import capo_database_migration_service.types.describe_table_statistics_message
    import capo_database_migration_service.types.describe_table_statistics_response
    import capo_database_migration_service.types.dms_ssl_mode_value
    import capo_database_migration_service.types.dms_transfer_settings
    import capo_database_migration_service.types.doc_db_settings
    import capo_database_migration_service.types.dynamo_db_settings
    import capo_database_migration_service.types.elasticsearch_settings
    import capo_database_migration_service.types.event_categories_list
    import capo_database_migration_service.types.exclude_test_list
    import capo_database_migration_service.types.export_metadata_model_assessment_message
    import capo_database_migration_service.types.export_metadata_model_assessment_response
    import capo_database_migration_service.types.filter_list
    import capo_database_migration_service.types.gcp_my_sql_settings
    import capo_database_migration_service.types.get_target_selection_rules_message
    import capo_database_migration_service.types.get_target_selection_rules_response
    import capo_database_migration_service.types.ibm_db2_settings
    import capo_database_migration_service.types.import_certificate_message
    import capo_database_migration_service.types.import_certificate_response
    import capo_database_migration_service.types.include_test_list
    import capo_database_migration_service.types.integer_optional
    import capo_database_migration_service.types.kafka_settings
    import capo_database_migration_service.types.kerberos_authentication_settings
    import capo_database_migration_service.types.key_list
    import capo_database_migration_service.types.kinesis_settings
    import capo_database_migration_service.types.list_tags_for_resource_message
    import capo_database_migration_service.types.list_tags_for_resource_response
    import capo_database_migration_service.types.marker
    import capo_database_migration_service.types.metadata_model_properties
    import capo_database_migration_service.types.metadata_model_reference
    import capo_database_migration_service.types.microsoft_sql_server_settings
    import capo_database_migration_service.types.migration_project_identifier
    import capo_database_migration_service.types.migration_type_value
    import capo_database_migration_service.types.modify_conversion_configuration_message
    import capo_database_migration_service.types.modify_conversion_configuration_response
    import capo_database_migration_service.types.modify_data_migration_message
    import capo_database_migration_service.types.modify_data_migration_response
    import capo_database_migration_service.types.modify_data_provider_message
    import capo_database_migration_service.types.modify_data_provider_response
    import capo_database_migration_service.types.modify_endpoint_message
    import capo_database_migration_service.types.modify_endpoint_response
    import capo_database_migration_service.types.modify_event_subscription_message
    import capo_database_migration_service.types.modify_event_subscription_response
    import capo_database_migration_service.types.modify_instance_profile_message
    import capo_database_migration_service.types.modify_instance_profile_response
    import capo_database_migration_service.types.modify_migration_project_message
    import capo_database_migration_service.types.modify_migration_project_response
    import capo_database_migration_service.types.modify_replication_config_message
    import capo_database_migration_service.types.modify_replication_config_response
    import capo_database_migration_service.types.modify_replication_instance_message
    import capo_database_migration_service.types.modify_replication_instance_response
    import capo_database_migration_service.types.modify_replication_subnet_group_message
    import capo_database_migration_service.types.modify_replication_subnet_group_response
    import capo_database_migration_service.types.modify_replication_task_message
    import capo_database_migration_service.types.modify_replication_task_response
    import capo_database_migration_service.types.mongo_db_settings
    import capo_database_migration_service.types.move_replication_task_message
    import capo_database_migration_service.types.move_replication_task_response
    import capo_database_migration_service.types.my_sql_settings
    import capo_database_migration_service.types.neptune_settings
    import capo_database_migration_service.types.oracle_settings
    import capo_database_migration_service.types.origin_type_value
    import capo_database_migration_service.types.postgre_sql_settings
    import capo_database_migration_service.types.reboot_replication_instance_message
    import capo_database_migration_service.types.reboot_replication_instance_response
    import capo_database_migration_service.types.recommendation_settings
    import capo_database_migration_service.types.redis_settings
    import capo_database_migration_service.types.redshift_settings
    import capo_database_migration_service.types.refresh_schemas_message
    import capo_database_migration_service.types.refresh_schemas_response
    import capo_database_migration_service.types.reload_option_value
    import capo_database_migration_service.types.reload_replication_tables_message
    import capo_database_migration_service.types.reload_replication_tables_response
    import capo_database_migration_service.types.reload_tables_message
    import capo_database_migration_service.types.reload_tables_response
    import capo_database_migration_service.types.remove_tags_from_resource_message
    import capo_database_migration_service.types.remove_tags_from_resource_response
    import capo_database_migration_service.types.replication_endpoint_type_value
    import capo_database_migration_service.types.replication_instance_class
    import capo_database_migration_service.types.run_fleet_advisor_lsa_analysis_response
    import capo_database_migration_service.types.s3_settings
    import capo_database_migration_service.types.sc_application_attributes
    import capo_database_migration_service.types.schema_conversion_request
    import capo_database_migration_service.types.secret_string
    import capo_database_migration_service.types.source_data_settings
    import capo_database_migration_service.types.source_ids_list
    import capo_database_migration_service.types.source_type
    import capo_database_migration_service.types.start_data_migration_message
    import capo_database_migration_service.types.start_data_migration_response
    import capo_database_migration_service.types.start_extension_pack_association_message
    import capo_database_migration_service.types.start_extension_pack_association_response
    import capo_database_migration_service.types.start_metadata_model_assessment_message
    import capo_database_migration_service.types.start_metadata_model_assessment_response
    import capo_database_migration_service.types.start_metadata_model_conversion_message
    import capo_database_migration_service.types.start_metadata_model_conversion_response
    import capo_database_migration_service.types.start_metadata_model_creation_message
    import capo_database_migration_service.types.start_metadata_model_creation_response
    import capo_database_migration_service.types.start_metadata_model_export_as_script_message
    import capo_database_migration_service.types.start_metadata_model_export_as_script_response
    import capo_database_migration_service.types.start_metadata_model_export_to_target_message
    import capo_database_migration_service.types.start_metadata_model_export_to_target_response
    import capo_database_migration_service.types.start_metadata_model_import_message
    import capo_database_migration_service.types.start_metadata_model_import_response
    import capo_database_migration_service.types.start_recommendations_request
    import capo_database_migration_service.types.start_recommendations_request_entry_list
    import capo_database_migration_service.types.start_replication_message
    import capo_database_migration_service.types.start_replication_migration_type_value
    import capo_database_migration_service.types.start_replication_response
    import capo_database_migration_service.types.start_replication_task_assessment_message
    import capo_database_migration_service.types.start_replication_task_assessment_response
    import capo_database_migration_service.types.start_replication_task_assessment_run_message
    import capo_database_migration_service.types.start_replication_task_assessment_run_response
    import capo_database_migration_service.types.start_replication_task_message
    import capo_database_migration_service.types.start_replication_task_response
    import capo_database_migration_service.types.start_replication_task_type_value
    import capo_database_migration_service.types.stop_data_migration_message
    import capo_database_migration_service.types.stop_data_migration_response
    import capo_database_migration_service.types.stop_replication_message
    import capo_database_migration_service.types.stop_replication_response
    import capo_database_migration_service.types.stop_replication_task_message
    import capo_database_migration_service.types.stop_replication_task_response
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.string_list
    import capo_database_migration_service.types.subnet_identifier_list
    import capo_database_migration_service.types.sybase_settings
    import capo_database_migration_service.types.t_stamp
    import capo_database_migration_service.types.table_list_to_reload
    import capo_database_migration_service.types.tag_list
    import capo_database_migration_service.types.target_data_settings
    import capo_database_migration_service.types.test_connection_message
    import capo_database_migration_service.types.test_connection_response
    import capo_database_migration_service.types.timestream_settings
    import capo_database_migration_service.types.update_subscriptions_to_event_bridge_message
    import capo_database_migration_service.types.update_subscriptions_to_event_bridge_response
    import capo_database_migration_service.types.vpc_security_group_id_list


class AsyncDatabaseMigrationServiceClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[AsyncInterceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class AsyncDatabaseMigrationServiceClient:
    """A client for the ``DatabaseMigrationService`` service.

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
        self._config = AsyncDatabaseMigrationServiceClientConfig(
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
        self,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> tuple[Iterable[AsyncInterceptor[Any, Any]], AsyncOperationOptions]:
        overrides: AsyncDatabaseMigrationServiceClientConfig = config_overrides or {}
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
        resource_arn: "capo_database_migration_service.types.string.String",
        tags: "capo_database_migration_service.types.tag_list.TagList",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.add_tags_to_resource_response.AddTagsToResourceResponse":
        """<p>Adds metadata tags to an DMS resource, including replication instance, endpoint, subnet group, and migration task. These tags can also be used with cost allocation reporting to track cost associated with DMS resources, or used in a Condition statement in an IAM policy for DMS. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html"> <code>Tag</code> </a> data type description.</p>

        Args:
            resource_arn: <p>Identifies the DMS resource to which tags should be added. The value for this parameter is an Amazon Resource Name (ARN).</p> <p>For DMS, you can tag a replication instance, an endpoint, or a replication task.</p>
            tags: <p>One or more tags to be assigned to the resource.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Add tags to resource
            Adds metadata tags to an AWS DMS resource, including replication instance, endpoint, security group, and migration task. These tags can also be used with cost allocation reporting to track cost associated with AWS DMS resources, or used in a Condition statement in an IAM policy for AWS DMS.

            >>> await client.add_tags_to_resource(resource_arn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E', tags=[{'Key': 'Acount', 'Value': '1633456'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.add_tags_to_resource_message.AddTagsToResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.add_tags_to_resource_response.AddTagsToResourceResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.add_tags_to_resource

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.add_tags_to_resource.async_add_tags_to_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.add_tags_to_resource_message.AddTagsToResourceMessage = {
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

    async def apply_pending_maintenance_action(
        self,
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        apply_action: "capo_database_migration_service.types.string.String",
        opt_in_type: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.apply_pending_maintenance_action_response.ApplyPendingMaintenanceActionResponse":
        """<p>Applies a pending maintenance action to a resource (for example, to a replication instance).</p>

        Args:
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action applies to.</p>
            apply_action: <p>The pending maintenance action to apply to this resource.</p> <p>Valid values: <code>os-upgrade</code>, <code>system-update</code>, <code>db-upgrade</code>, <code>os-patch</code> </p>
            opt_in_type: <p>A value that specifies the type of opt-in request, or undoes an opt-in request. You can't undo an opt-in request of type <code>immediate</code>.</p> <p>Valid values:</p> <ul> <li> <p> <code>immediate</code> - Apply the maintenance action immediately.</p> </li> <li> <p> <code>next-maintenance</code> - Apply the maintenance action during the next maintenance window for the resource.</p> </li> <li> <p> <code>undo-opt-in</code> - Cancel any existing <code>next-maintenance</code> opt-in requests.</p> </li> </ul>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.apply_pending_maintenance_action_message.ApplyPendingMaintenanceActionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.apply_pending_maintenance_action_response.ApplyPendingMaintenanceActionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.apply_pending_maintenance_action

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.apply_pending_maintenance_action.async_apply_pending_maintenance_action(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.apply_pending_maintenance_action_message.ApplyPendingMaintenanceActionMessage = {
            "replication_instance_arn": replication_instance_arn,
            "apply_action": apply_action,
            "opt_in_type": opt_in_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def batch_start_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        data: Optional[
            "capo_database_migration_service.types.start_recommendations_request_entry_list.StartRecommendationsRequestEntryList"
        ] = None,
    ) -> "capo_database_migration_service.types.batch_start_recommendations_response.BatchStartRecommendationsResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Starts the analysis of up to 20 source databases to recommend target engines for each source database. This is a batch version of <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartRecommendations.html">StartRecommendations</a>.</p> <p>The result of analysis of each source database is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of <code>200</code>.</p>

        Args:
            data: <p>Provides information about source databases to analyze. After this analysis, Fleet Advisor recommends target engines for each source database.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.batch_start_recommendations_request.BatchStartRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.batch_start_recommendations_response.BatchStartRecommendationsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.batch_start_recommendations

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.batch_start_recommendations.async_batch_start_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.batch_start_recommendations_request.BatchStartRecommendationsRequest = {}
        if data is not None:
            input_["data"] = data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_metadata_model_conversion(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        request_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.cancel_metadata_model_conversion_response.CancelMetadataModelConversionResponse":
        """<p>Cancels a single metadata model conversion operation that was started with <code>StartMetadataModelConversion</code>.</p> <p> <b>Required permissions:</b> <code>dms:CancelMetadataModelConversion</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            request_identifier: <p>The identifier for the metadata model conversion operation to cancel. This operation was initiated by StartMetadataModelConversion.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a metadata model conversion
            The following example cancels a metadata model conversion operation.

            >>> await client.cancel_metadata_model_conversion(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', request_identifier='a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.cancel_metadata_model_conversion_message.CancelMetadataModelConversionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.cancel_metadata_model_conversion_response.CancelMetadataModelConversionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.cancel_metadata_model_conversion

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.cancel_metadata_model_conversion.async_cancel_metadata_model_conversion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.cancel_metadata_model_conversion_message.CancelMetadataModelConversionMessage = {
            "migration_project_identifier": migration_project_identifier,
            "request_identifier": request_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_metadata_model_creation(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        request_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.cancel_metadata_model_creation_response.CancelMetadataModelCreationResponse":
        """<p>Cancels a single metadata model creation operation that was started with <code>StartMetadataModelCreation</code>.</p> <p> <b>Required permissions:</b> <code>dms:CancelMetadataModelCreation</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            request_identifier: <p>The identifier for the metadata model creation operation to cancel. This operation was initiated by <code>StartMetadataModelCreation</code>.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Cancel a metadata model creation
            The following example cancels a metadata model creation operation.

            >>> await client.cancel_metadata_model_creation(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', request_identifier='a1b2c3d4-5678-90ab-cdef-EXAMPLE11111')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.cancel_metadata_model_creation_message.CancelMetadataModelCreationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.cancel_metadata_model_creation_response.CancelMetadataModelCreationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.cancel_metadata_model_creation

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.cancel_metadata_model_creation.async_cancel_metadata_model_creation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.cancel_metadata_model_creation_message.CancelMetadataModelCreationMessage = {
            "migration_project_identifier": migration_project_identifier,
            "request_identifier": request_identifier,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def cancel_replication_task_assessment_run(
        self,
        replication_task_assessment_run_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.cancel_replication_task_assessment_run_response.CancelReplicationTaskAssessmentRunResponse":
        """<p>Cancels a single premigration assessment run.</p> <p>This operation prevents any individual assessments from running if they haven't started running. It also attempts to cancel any individual assessments that are currently running.</p>

        Args:
            replication_task_assessment_run_arn: <p>Amazon Resource Name (ARN) of the premigration assessment run to be canceled.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.cancel_replication_task_assessment_run_message.CancelReplicationTaskAssessmentRunMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.cancel_replication_task_assessment_run_response.CancelReplicationTaskAssessmentRunResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.cancel_replication_task_assessment_run

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.cancel_replication_task_assessment_run.async_cancel_replication_task_assessment_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.cancel_replication_task_assessment_run_message.CancelReplicationTaskAssessmentRunMessage = {
            "replication_task_assessment_run_arn": replication_task_assessment_run_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_migration(
        self,
        migration_project_identifier: "capo_database_migration_service.types.string.String",
        data_migration_type: "capo_database_migration_service.types.migration_type_value.MigrationTypeValue",
        service_access_role_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        data_migration_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        enable_cloudwatch_logs: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        source_data_settings: Optional[
            "capo_database_migration_service.types.source_data_settings.SourceDataSettings"
        ] = None,
        target_data_settings: Optional[
            "capo_database_migration_service.types.target_data_settings.TargetDataSettings"
        ] = None,
        number_of_jobs: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
        selection_rules: Optional[
            "capo_database_migration_service.types.secret_string.SecretString"
        ] = None,
    ) -> "capo_database_migration_service.types.create_data_migration_response.CreateDataMigrationResponse":
        """<p>Creates a data migration using the provided settings.</p>

        Args:
            data_migration_name: <p>A user-friendly name for the data migration. Data migration names have the following constraints:</p> <ul> <li> <p>Must begin with a letter, and can only contain ASCII letters, digits, and hyphens. </p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> <li> <p>Length must be from 1 to 255 characters.</p> </li> </ul>
            migration_project_identifier: <p>An identifier for the migration project.</p>
            data_migration_type: <p>Specifies if the data migration is full-load only, change data capture (CDC) only, or full-load and CDC.</p>
            service_access_role_arn: <p>The Amazon Resource Name (ARN) for the service access role that you want to use to create the data migration.</p>
            enable_cloudwatch_logs: <p>Specifies whether to enable CloudWatch logs for the data migration.</p>
            source_data_settings: <p>Specifies information about the source data provider.</p>
            target_data_settings: <p>Specifies information about the target data provider.</p>
            number_of_jobs: <p>The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.</p>
            tags: <p>One or more tags to be assigned to the data migration.</p>
            selection_rules: <p>An optional JSON string specifying what tables, views, and schemas to include or exclude from the migration.</p>

        Raises:
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_operation_fault.InvalidOperationFault: <p>The action or operation requested isn't valid.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_data_migration_message.CreateDataMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_data_migration_response.CreateDataMigrationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_data_migration

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_data_migration.async_create_data_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_data_migration_message.CreateDataMigrationMessage = {
            "migration_project_identifier": migration_project_identifier,
            "data_migration_type": data_migration_type,
            "service_access_role_arn": service_access_role_arn,
        }
        if data_migration_name is not None:
            input_["data_migration_name"] = data_migration_name
        if enable_cloudwatch_logs is not None:
            input_["enable_cloudwatch_logs"] = enable_cloudwatch_logs
        if source_data_settings is not None:
            input_["source_data_settings"] = source_data_settings
        if target_data_settings is not None:
            input_["target_data_settings"] = target_data_settings
        if number_of_jobs is not None:
            input_["number_of_jobs"] = number_of_jobs
        if tags is not None:
            input_["tags"] = tags
        if selection_rules is not None:
            input_["selection_rules"] = selection_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_data_provider(
        self,
        engine: "capo_database_migration_service.types.string.String",
        settings: "capo_database_migration_service.types.data_provider_settings.DataProviderSettings",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        data_provider_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        virtual: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
    ) -> "capo_database_migration_service.types.create_data_provider_response.CreateDataProviderResponse":
        """<p>Creates a data provider using the provided settings. A data provider stores a data store type and location information about your database. </p> <p> <b>Required permissions:</b> <code>dms:CreateDataProvider</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            data_provider_name: <p>A user-friendly name for the data provider.</p>
            description: <p>A user-friendly description of the data provider.</p>
            engine: <p>The type of database engine for the data provider.</p> <p>Valid values: <code>aurora</code>, <code>aurora-postgresql</code>, <code>db2</code>, <code>db2-zos</code>, <code>docdb</code>, <code>mariadb</code>, <code>mongodb</code>, <code>mysql</code>, <code>oracle</code>, <code>postgres</code>, <code>redshift</code>, <code>sqlserver</code>, and <code>sybase</code>. A value of <code>aurora</code> represents Amazon Aurora MySQL-Compatible Edition.</p>
            virtual: <p>Indicates whether the data provider is virtual.</p>
            settings: <p>The settings in JSON format for a data provider.</p>
            tags: <p>One or more tags to be assigned to the data provider.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a Microsoft SQL Server data provider
            The following example creates a Microsoft SQL Server data provider.

            >>> await client.create_data_provider(data_provider_name='example-data-provider', engine='sqlserver', description='Example data provider for documentation', settings={'MicrosoftSqlServerSettings': {'ServerName': 'example-source-server.us-east-1.rds.amazonaws.com', 'Port': 1433, 'DatabaseName': 'ExampleDatabase', 'SslMode': 'verify-full', 'CertificateArn': 'arn:aws:dms:us-east-1:111122223333:cert:EXAMPLEABCDEFGHIJKLMNOPQRS'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_data_provider_message.CreateDataProviderMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_data_provider_response.CreateDataProviderResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_data_provider

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_data_provider.async_create_data_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_data_provider_message.CreateDataProviderMessage = {
            "engine": engine,
            "settings": settings,
        }
        if data_provider_name is not None:
            input_["data_provider_name"] = data_provider_name
        if description is not None:
            input_["description"] = description
        if virtual is not None:
            input_["virtual"] = virtual
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_endpoint(
        self,
        endpoint_identifier: "capo_database_migration_service.types.string.String",
        endpoint_type: "capo_database_migration_service.types.replication_endpoint_type_value.ReplicationEndpointTypeValue",
        engine_name: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        username: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        password: Optional[
            "capo_database_migration_service.types.secret_string.SecretString"
        ] = None,
        server_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        port: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        database_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        extra_connection_attributes: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        kms_key_id: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
        certificate_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        ssl_mode: Optional[
            "capo_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
        ] = None,
        service_access_role_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        external_table_definition: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        dynamo_db_settings: Optional[
            "capo_database_migration_service.types.dynamo_db_settings.DynamoDbSettings"
        ] = None,
        s3_settings: Optional[
            "capo_database_migration_service.types.s3_settings.S3Settings"
        ] = None,
        dms_transfer_settings: Optional[
            "capo_database_migration_service.types.dms_transfer_settings.DmsTransferSettings"
        ] = None,
        mongo_db_settings: Optional[
            "capo_database_migration_service.types.mongo_db_settings.MongoDbSettings"
        ] = None,
        kinesis_settings: Optional[
            "capo_database_migration_service.types.kinesis_settings.KinesisSettings"
        ] = None,
        kafka_settings: Optional[
            "capo_database_migration_service.types.kafka_settings.KafkaSettings"
        ] = None,
        elasticsearch_settings: Optional[
            "capo_database_migration_service.types.elasticsearch_settings.ElasticsearchSettings"
        ] = None,
        neptune_settings: Optional[
            "capo_database_migration_service.types.neptune_settings.NeptuneSettings"
        ] = None,
        redshift_settings: Optional[
            "capo_database_migration_service.types.redshift_settings.RedshiftSettings"
        ] = None,
        postgre_sql_settings: Optional[
            "capo_database_migration_service.types.postgre_sql_settings.PostgreSQLSettings"
        ] = None,
        my_sql_settings: Optional[
            "capo_database_migration_service.types.my_sql_settings.MySQLSettings"
        ] = None,
        oracle_settings: Optional[
            "capo_database_migration_service.types.oracle_settings.OracleSettings"
        ] = None,
        sybase_settings: Optional[
            "capo_database_migration_service.types.sybase_settings.SybaseSettings"
        ] = None,
        microsoft_sql_server_settings: Optional[
            "capo_database_migration_service.types.microsoft_sql_server_settings.MicrosoftSQLServerSettings"
        ] = None,
        ibm_db2_settings: Optional[
            "capo_database_migration_service.types.ibm_db2_settings.IBMDb2Settings"
        ] = None,
        resource_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        doc_db_settings: Optional[
            "capo_database_migration_service.types.doc_db_settings.DocDbSettings"
        ] = None,
        redis_settings: Optional[
            "capo_database_migration_service.types.redis_settings.RedisSettings"
        ] = None,
        gcp_my_sql_settings: Optional[
            "capo_database_migration_service.types.gcp_my_sql_settings.GcpMySQLSettings"
        ] = None,
        timestream_settings: Optional[
            "capo_database_migration_service.types.timestream_settings.TimestreamSettings"
        ] = None,
    ) -> "capo_database_migration_service.types.create_endpoint_response.CreateEndpointResponse":
        """<p>Creates an endpoint using the provided settings.</p> <note> <p>For a MySQL source or target endpoint, don't explicitly specify the database using the <code>DatabaseName</code> request parameter on the <code>CreateEndpoint</code> API call. Specifying <code>DatabaseName</code> when you create a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task.</p> </note>

        Args:
            endpoint_identifier: <p>The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>
            endpoint_type: <p>The type of endpoint. Valid values are <code>source</code> and <code>target</code>.</p>
            engine_name: <p>The type of engine for the endpoint. Valid values, depending on the <code>EndpointType</code> value, include <code>"mysql"</code>, <code>"oracle"</code>, <code>"postgres"</code>, <code>"mariadb"</code>, <code>"aurora"</code>, <code>"aurora-postgresql"</code>, <code>"opensearch"</code>, <code>"redshift"</code>, <code>"s3"</code>, <code>"db2"</code>, <code>"db2-zos"</code>, <code>"azuredb"</code>, <code>"sybase"</code>, <code>"dynamodb"</code>, <code>"mongodb"</code>, <code>"kinesis"</code>, <code>"kafka"</code>, <code>"elasticsearch"</code>, <code>"docdb"</code>, <code>"sqlserver"</code>, <code>"neptune"</code>, <code>"babelfish"</code>, <code>redshift-serverless</code>, <code>aurora-serverless</code>, <code>aurora-postgresql-serverless</code>, <code>gcp-mysql</code>, <code>azure-sql-managed-instance</code>, <code>redis</code>, <code>dms-transfer</code>.</p>
            username: <p>The user name to be used to log in to the endpoint database.</p>
            password: <p>The password to be used to log in to the endpoint database.</p>
            server_name: <p>The name of the server where the endpoint database resides.</p>
            port: <p>The port used by the endpoint database.</p>
            database_name: <p>The name of the endpoint database. For a MySQL source or target endpoint, do not specify DatabaseName. To migrate to a specific database, use this setting and <code>targetDbType</code>.</p>
            extra_connection_attributes: <p>Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html">Working with DMS Endpoints</a> in the <i>Database Migration Service User Guide.</i> </p>
            kms_key_id: <p>An KMS key identifier that is used to encrypt the connection parameters for the endpoint.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>
            tags: <p>One or more tags to be assigned to the endpoint.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) for the certificate.</p>
            ssl_mode: <p>The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is <code>none</code> </p>
            service_access_role_arn: <p> The Amazon Resource Name (ARN) for the service access role that you want to use to create the endpoint. The role must allow the <code>iam:PassRole</code> action.</p>
            external_table_definition: <p>The external table definition. </p>
            dynamo_db_settings: <p>Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping">Using Object Mapping to Migrate Data to DynamoDB</a> in the <i>Database Migration Service User Guide.</i> </p>
            s3_settings: <p>Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring">Extra Connection Attributes When Using Amazon S3 as a Target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            dms_transfer_settings: <p>The settings in JSON format for the DMS transfer type of source endpoint. </p> <p>Possible settings include the following:</p> <ul> <li> <p> <code>ServiceAccessRoleArn</code> - The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the <code>iam:PassRole</code> action.</p> </li> <li> <p> <code>BucketName</code> - The name of the S3 bucket to use.</p> </li> </ul> <p>Shorthand syntax for these settings is as follows: <code>ServiceAccessRoleArn=string,BucketName=string</code> </p> <p>JSON syntax for these settings is as follows: <code>{ "ServiceAccessRoleArn": "string", "BucketName": "string", } </code> </p>
            mongo_db_settings: <p>Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration">Endpoint configuration settings when using MongoDB as a source for Database Migration Service</a> in the <i>Database Migration Service User Guide.</i> </p>
            kinesis_settings: <p>Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping">Using object mapping to migrate data to a Kinesis data stream</a> in the <i>Database Migration Service User Guide.</i> </p>
            kafka_settings: <p>Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping">Using object mapping to migrate data to a Kafka topic</a> in the <i>Database Migration Service User Guide.</i> </p>
            elasticsearch_settings: <p>Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration">Extra Connection Attributes When Using OpenSearch as a Target for DMS</a> in the <i>Database Migration Service User Guide</i>.</p>
            neptune_settings: <p>Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings">Specifying graph-mapping rules using Gremlin and R2RML for Amazon Neptune as a target</a> in the <i>Database Migration Service User Guide.</i> </p>
            postgre_sql_settings: <p>Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib">Extra connection attributes when using PostgreSQL as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib"> Extra connection attributes when using PostgreSQL as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            my_sql_settings: <p>Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib">Extra connection attributes when using MySQL as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib">Extra connection attributes when using a MySQL-compatible database as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            oracle_settings: <p>Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib">Extra connection attributes when using Oracle as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib"> Extra connection attributes when using Oracle as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            sybase_settings: <p>Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib">Extra connection attributes when using SAP ASE as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib">Extra connection attributes when using SAP ASE as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            microsoft_sql_server_settings: <p>Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib">Extra connection attributes when using SQL Server as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib"> Extra connection attributes when using SQL Server as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            ibm_db2_settings: <p>Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib">Extra connection attributes when using Db2 LUW as a source for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            resource_identifier: <p>A friendly name for the resource identifier at the end of the <code>EndpointArn</code> response parameter that is returned in the created <code>Endpoint</code> object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as <code>Example-App-ARN1</code>. For example, this value might result in the <code>EndpointArn</code> value <code>arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1</code>. If you don't specify a <code>ResourceIdentifier</code> value, DMS generates a default identifier value for the end of <code>EndpointArn</code>.</p>
            redis_settings: <p>Settings in JSON format for the target Redis endpoint.</p>
            gcp_my_sql_settings: <p>Settings in JSON format for the source GCP MySQL endpoint.</p>
            timestream_settings: <p>Settings in JSON format for the target Amazon Timestream endpoint.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create endpoint
            Creates an endpoint using the provided settings.

            >>> await client.create_endpoint(endpoint_identifier='test-endpoint-1', endpoint_type='source', engine_name='mysql', username='username', password='pasword', server_name='mydb.cx1llnox7iyx.us-west-2.rds.amazonaws.com', port=3306, database_name='testdb', extra_connection_attributes='', kms_key_id='arn:aws:kms:us-east-1:123456789012:key/4c1731d6-5435-ed4d-be13-d53411a7cfbd', tags=[{'Key': 'Acount', 'Value': '143327655'}], certificate_arn='', ssl_mode='require')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_endpoint_message.CreateEndpointMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_endpoint_response.CreateEndpointResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_endpoint

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_endpoint.async_create_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_endpoint_message.CreateEndpointMessage = {
            "endpoint_identifier": endpoint_identifier,
            "endpoint_type": endpoint_type,
            "engine_name": engine_name,
        }
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if server_name is not None:
            input_["server_name"] = server_name
        if port is not None:
            input_["port"] = port
        if database_name is not None:
            input_["database_name"] = database_name
        if extra_connection_attributes is not None:
            input_["extra_connection_attributes"] = extra_connection_attributes
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if ssl_mode is not None:
            input_["ssl_mode"] = ssl_mode
        if service_access_role_arn is not None:
            input_["service_access_role_arn"] = service_access_role_arn
        if external_table_definition is not None:
            input_["external_table_definition"] = external_table_definition
        if dynamo_db_settings is not None:
            input_["dynamo_db_settings"] = dynamo_db_settings
        if s3_settings is not None:
            input_["s3_settings"] = s3_settings
        if dms_transfer_settings is not None:
            input_["dms_transfer_settings"] = dms_transfer_settings
        if mongo_db_settings is not None:
            input_["mongo_db_settings"] = mongo_db_settings
        if kinesis_settings is not None:
            input_["kinesis_settings"] = kinesis_settings
        if kafka_settings is not None:
            input_["kafka_settings"] = kafka_settings
        if elasticsearch_settings is not None:
            input_["elasticsearch_settings"] = elasticsearch_settings
        if neptune_settings is not None:
            input_["neptune_settings"] = neptune_settings
        if redshift_settings is not None:
            input_["redshift_settings"] = redshift_settings
        if postgre_sql_settings is not None:
            input_["postgre_sql_settings"] = postgre_sql_settings
        if my_sql_settings is not None:
            input_["my_sql_settings"] = my_sql_settings
        if oracle_settings is not None:
            input_["oracle_settings"] = oracle_settings
        if sybase_settings is not None:
            input_["sybase_settings"] = sybase_settings
        if microsoft_sql_server_settings is not None:
            input_["microsoft_sql_server_settings"] = microsoft_sql_server_settings
        if ibm_db2_settings is not None:
            input_["ibm_db2_settings"] = ibm_db2_settings
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if doc_db_settings is not None:
            input_["doc_db_settings"] = doc_db_settings
        if redis_settings is not None:
            input_["redis_settings"] = redis_settings
        if gcp_my_sql_settings is not None:
            input_["gcp_my_sql_settings"] = gcp_my_sql_settings
        if timestream_settings is not None:
            input_["timestream_settings"] = timestream_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_event_subscription(
        self,
        subscription_name: "capo_database_migration_service.types.string.String",
        sns_topic_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        source_type: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        event_categories: Optional[
            "capo_database_migration_service.types.event_categories_list.EventCategoriesList"
        ] = None,
        source_ids: Optional[
            "capo_database_migration_service.types.source_ids_list.SourceIdsList"
        ] = None,
        enabled: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
    ) -> "capo_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse":
        """<p> Creates an DMS event notification subscription. </p> <p>You can specify the type of source (<code>SourceType</code>) you want to be notified of, provide a list of DMS source IDs (<code>SourceIds</code>) that triggers the events, and provide a list of event categories (<code>EventCategories</code>) for events you want to be notified of. If you specify both the <code>SourceType</code> and <code>SourceIds</code>, such as <code>SourceType = replication-instance</code> and <code>SourceIdentifier = my-replinstance</code>, you will be notified of all the replication instance events for the specified source. If you specify a <code>SourceType</code> but don't specify a <code>SourceIdentifier</code>, you receive notice of the events for that source type for all your DMS sources. If you don't specify either <code>SourceType</code> nor <code>SourceIdentifier</code>, you will be notified of events generated from all DMS sources belonging to your customer account.</p> <p>For more information about DMS events, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html">Working with Events and Notifications</a> in the <i>Database Migration Service User Guide.</i> </p>

        Args:
            subscription_name: <p>The name of the DMS event notification subscription. This name must be less than 255 characters.</p>
            sns_topic_arn: <p> The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it. </p>
            source_type: <p> The type of DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to <code>replication-instance</code>. If this value isn't specified, all events are returned. </p> <p>Valid values: <code>replication-instance</code> | <code>replication-task</code> </p>
            event_categories: <p>A list of event categories for a source type that you want to subscribe to. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html">Working with Events and Notifications</a> in the <i>Database Migration Service User Guide.</i> </p>
            source_ids: <p>A list of identifiers for which DMS provides notification events.</p> <p>If you don't specify a value, notifications are provided for all sources.</p> <p>If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.</p>
            enabled: <p> A Boolean value; set to <code>true</code> to activate the subscription, or set to <code>false</code> to create the subscription but not activate it. </p>
            tags: <p>One or more tags to be assigned to the event subscription.</p>

        Raises:
            capo_database_migration_service.errors.kms_access_denied_fault.KMSAccessDeniedFault: <p>The ciphertext references a key that doesn't exist or that the DMS account doesn't have access to.</p>
            capo_database_migration_service.errors.kms_disabled_fault.KMSDisabledFault: <p>The specified KMS key isn't enabled.</p>
            capo_database_migration_service.errors.kms_invalid_state_fault.KMSInvalidStateFault: <p>The state of the specified KMS resource isn't valid for this request.</p>
            capo_database_migration_service.errors.kms_not_found_fault.KMSNotFoundFault: <p>The specified KMS entity or resource can't be found.</p>
            capo_database_migration_service.errors.kms_throttling_fault.KMSThrottlingFault: <p>This request triggered KMS request throttling.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>The SNS topic is invalid.</p>
            capo_database_migration_service.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>You are not authorized for the SNS subscription.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_event_subscription_message.CreateEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_event_subscription_response.CreateEventSubscriptionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_event_subscription

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_event_subscription.async_create_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_event_subscription_message.CreateEventSubscriptionMessage = {
            "subscription_name": subscription_name,
            "sns_topic_arn": sns_topic_arn,
        }
        if source_type is not None:
            input_["source_type"] = source_type
        if event_categories is not None:
            input_["event_categories"] = event_categories
        if source_ids is not None:
            input_["source_ids"] = source_ids
        if enabled is not None:
            input_["enabled"] = enabled
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_fleet_advisor_collector(
        self,
        collector_name: "capo_database_migration_service.types.string.String",
        service_access_role_arn: "capo_database_migration_service.types.string.String",
        s3_bucket_name: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.create_fleet_advisor_collector_response.CreateFleetAdvisorCollectorResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Creates a Fleet Advisor collector using the specified parameters.</p>

        Args:
            collector_name: <p>The name of your Fleet Advisor collector (for example, <code>sample-collector</code>).</p>
            description: <p>A summary description of your Fleet Advisor collector.</p>
            service_access_role_arn: <p>The IAM role that grants permissions to access the specified Amazon S3 bucket.</p>
            s3_bucket_name: <p>The Amazon S3 bucket that the Fleet Advisor collector uses to store inventory metadata.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_fleet_advisor_collector_request.CreateFleetAdvisorCollectorRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_fleet_advisor_collector_response.CreateFleetAdvisorCollectorResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_fleet_advisor_collector

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_fleet_advisor_collector.async_create_fleet_advisor_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_fleet_advisor_collector_request.CreateFleetAdvisorCollectorRequest = {
            "collector_name": collector_name,
            "service_access_role_arn": service_access_role_arn,
            "s3_bucket_name": s3_bucket_name,
        }
        if description is not None:
            input_["description"] = description

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_instance_profile(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        availability_zone: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        kms_key_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        publicly_accessible: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
        network_type: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        instance_profile_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        subnet_group_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        vpc_security_groups: Optional[
            "capo_database_migration_service.types.string_list.StringList"
        ] = None,
    ) -> "capo_database_migration_service.types.create_instance_profile_response.CreateInstanceProfileResponse":
        """<p>Creates the instance profile using the specified parameters.</p> <p> <b>Required permissions:</b> <code>dms:CreateInstanceProfile</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            availability_zone: <p>The Availability Zone where the instance profile will be created. The default value is a random, system-chosen Availability Zone in the Amazon Web Services Region where your data provider is created, for examplem <code>us-east-1d</code>.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key that is used to encrypt the connection parameters for the instance profile.</p> <p>If you don't specify a value for the <code>KmsKeyArn</code> parameter, then DMS uses an Amazon Web Services owned encryption key to encrypt your resources.</p>
            publicly_accessible: <p>Specifies the accessibility options for the instance profile. A value of <code>true</code> represents an instance profile with a public IP address. A value of <code>false</code> represents an instance profile with a private IP address. The default value is <code>true</code>.</p>
            tags: <p>One or more tags to be assigned to the instance profile.</p>
            network_type: <p>Specifies the network type for the instance profile. A value of <code>IPV4</code> represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of <code>IPV6</code> represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of <code>DUAL</code> represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.</p>
            instance_profile_name: <p>A user-friendly name for the instance profile.</p>
            description: <p>A user-friendly description of the instance profile.</p>
            subnet_group_identifier: <p>A subnet group to associate with the instance profile.</p>
            vpc_security_groups: <p>Specifies the VPC security group names to be used with the instance profile. The VPC security group must work with the VPC containing the instance profile.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create an instance profile
            The following example creates an instance profile.

            >>> await client.create_instance_profile(instance_profile_name='example-instance-profile', description='Example instance profile for documentation', subnet_group_identifier='example-replication-subnet-group', vpc_security_groups=['sg-0123456789abcdef0'], kms_key_arn='arn:aws:kms:us-east-1:111122223333:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', network_type='IPV4', publicly_accessible=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_instance_profile_message.CreateInstanceProfileMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_instance_profile_response.CreateInstanceProfileResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_instance_profile

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_instance_profile.async_create_instance_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_instance_profile_message.CreateInstanceProfileMessage = {}
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if tags is not None:
            input_["tags"] = tags
        if network_type is not None:
            input_["network_type"] = network_type
        if instance_profile_name is not None:
            input_["instance_profile_name"] = instance_profile_name
        if description is not None:
            input_["description"] = description
        if subnet_group_identifier is not None:
            input_["subnet_group_identifier"] = subnet_group_identifier
        if vpc_security_groups is not None:
            input_["vpc_security_groups"] = vpc_security_groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_migration_project(
        self,
        source_data_provider_descriptors: "capo_database_migration_service.types.data_provider_descriptor_definition_list.DataProviderDescriptorDefinitionList",
        target_data_provider_descriptors: "capo_database_migration_service.types.data_provider_descriptor_definition_list.DataProviderDescriptorDefinitionList",
        instance_profile_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        migration_project_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        transformation_rules: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
        schema_conversion_application_attributes: Optional[
            "capo_database_migration_service.types.sc_application_attributes.SCApplicationAttributes"
        ] = None,
    ) -> "capo_database_migration_service.types.create_migration_project_response.CreateMigrationProjectResponse":
        """<p>Creates the migration project using the specified parameters.</p> <p>You can run this action only after you create an instance profile and data providers using <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateInstanceProfile.html">CreateInstanceProfile</a> and <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateDataProvider.html">CreateDataProvider</a>.</p> <p> <b>Required permissions:</b> <code>dms:CreateMigrationProject</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_name: <p>A user-friendly name for the migration project.</p>
            source_data_provider_descriptors: <p>Information about the source data provider, including the name, ARN, and Secrets Manager parameters.</p>
            target_data_provider_descriptors: <p>Information about the target data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters.</p>
            instance_profile_identifier: <p>The identifier of the associated instance profile. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>
            transformation_rules: <p>A JSON string that specifies the transformation rules for the migration project. Transformation rules let you customize how DMS Schema Conversion converts your source database objects, including renaming, adding prefixes or suffixes, and changing data types. For the transformation rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-transformation-rules.html">Transformation rules in DMS Schema Conversion</a>.</p> <note> <p>Homogeneous data migrations do not support transformation rules.</p> </note>
            description: <p>A user-friendly description of the migration project.</p>
            tags: <p>One or more tags to be assigned to the migration project.</p>
            schema_conversion_application_attributes: <p>The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a migration project
            The following example creates a migration project.

            >>> await client.create_migration_project(migration_project_name='example-migration-project', description='Example migration project for documentation', source_data_provider_descriptors=[{'DataProviderIdentifier': 'arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS', 'SecretsManagerSecretId': 'arn:aws:secretsmanager:us-east-1:111122223333:secret:example-source-secret-A1B2C3', 'SecretsManagerAccessRoleArn': 'arn:aws:iam::111122223333:role/example-secrets-manager-role'}], target_data_provider_descriptors=[{'DataProviderIdentifier': 'arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS', 'SecretsManagerSecretId': 'arn:aws:secretsmanager:us-east-1:111122223333:secret:example-target-secret-A1B2C3', 'SecretsManagerAccessRoleArn': 'arn:aws:iam::111122223333:role/example-secrets-manager-role'}], instance_profile_identifier='arn:aws:dms:us-east-1:111122223333:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS', transformation_rules='{"rules":[{"rule-type":"transformation","rule-id":"1","rule-name":"1","rule-target":"schema","rule-action":"rename","object-locator":{"schema-name":"ExampleSchema"},"value":"TargetSchema"}]}', schema_conversion_application_attributes={'S3BucketPath': 's3://amzn-s3-demo-bucket', 'S3BucketRoleArn': 'arn:aws:iam::111122223333:role/example-s3-access-role'})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_migration_project_message.CreateMigrationProjectMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_migration_project_response.CreateMigrationProjectResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_migration_project

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_migration_project.async_create_migration_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_migration_project_message.CreateMigrationProjectMessage = {
            "source_data_provider_descriptors": source_data_provider_descriptors,
            "target_data_provider_descriptors": target_data_provider_descriptors,
            "instance_profile_identifier": instance_profile_identifier,
        }
        if migration_project_name is not None:
            input_["migration_project_name"] = migration_project_name
        if transformation_rules is not None:
            input_["transformation_rules"] = transformation_rules
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if schema_conversion_application_attributes is not None:
            input_["schema_conversion_application_attributes"] = (
                schema_conversion_application_attributes
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_replication_config(
        self,
        replication_config_identifier: "capo_database_migration_service.types.string.String",
        source_endpoint_arn: "capo_database_migration_service.types.string.String",
        target_endpoint_arn: "capo_database_migration_service.types.string.String",
        compute_config: "capo_database_migration_service.types.compute_config.ComputeConfig",
        replication_type: "capo_database_migration_service.types.migration_type_value.MigrationTypeValue",
        table_mappings: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_settings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        supplemental_settings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        resource_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
    ) -> "capo_database_migration_service.types.create_replication_config_response.CreateReplicationConfigResponse":
        """<p>Creates a configuration that you can later provide to configure and start an DMS Serverless replication. You can also provide options to validate the configuration inputs before you start the replication.</p>

        Args:
            replication_config_identifier: <p>A unique identifier that you want to use to create a <code>ReplicationConfigArn</code> that is returned as part of the output from this action. You can then pass this output <code>ReplicationConfigArn</code> as the value of the <code>ReplicationConfigArn</code> option for other actions to identify both DMS Serverless replications and replication configurations that you want those actions to operate on. For some actions, you can also use either this unique identifier or a corresponding ARN in action filters to identify the specific replication and replication configuration to operate on.</p>
            source_endpoint_arn: <p>The Amazon Resource Name (ARN) of the source endpoint for this DMS Serverless replication configuration.</p>
            target_endpoint_arn: <p>The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.</p>
            compute_config: <p>Configuration parameters for provisioning an DMS Serverless replication.</p>
            replication_type: <p>The type of DMS Serverless replication to provision using this replication configuration.</p> <p>Possible values:</p> <ul> <li> <p> <code>"full-load"</code> </p> </li> <li> <p> <code>"cdc"</code> </p> </li> <li> <p> <code>"full-load-and-cdc"</code> </p> </li> </ul>
            table_mappings: <p>JSON table mappings for DMS Serverless replications that are provisioned using this replication configuration. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html"> Specifying table selection and transformations rules using JSON</a>.</p>
            replication_settings: <p>Optional JSON settings for DMS Serverless replications that are provisioned using this replication configuration. For example, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html"> Change processing tuning settings</a>.</p>
            supplemental_settings: <p>Optional JSON settings for specifying supplemental data. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html"> Specifying supplemental data for task settings</a>.</p>
            resource_identifier: <p>Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.FineGrainedAccess"> Fine-grained access control using resource names and tags</a>.</p>
            tags: <p>One or more optional tags associated with resources used by the DMS Serverless replication. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html"> Tagging resources in Database Migration Service</a>.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.invalid_subnet.InvalidSubnet: <p>The subnet provided isn't valid.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.replication_subnet_group_does_not_cover_enough_a_zs.ReplicationSubnetGroupDoesNotCoverEnoughAZs: <p>The replication subnet group does not cover enough Availability Zones (AZs). Edit the replication subnet group and add more AZs.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_replication_config_message.CreateReplicationConfigMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_replication_config_response.CreateReplicationConfigResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_config

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_config.async_create_replication_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_replication_config_message.CreateReplicationConfigMessage = {
            "replication_config_identifier": replication_config_identifier,
            "source_endpoint_arn": source_endpoint_arn,
            "target_endpoint_arn": target_endpoint_arn,
            "compute_config": compute_config,
            "replication_type": replication_type,
            "table_mappings": table_mappings,
        }
        if replication_settings is not None:
            input_["replication_settings"] = replication_settings
        if supplemental_settings is not None:
            input_["supplemental_settings"] = supplemental_settings
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_replication_instance(
        self,
        replication_instance_identifier: "capo_database_migration_service.types.string.String",
        replication_instance_class: "capo_database_migration_service.types.replication_instance_class.ReplicationInstanceClass",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        allocated_storage: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_database_migration_service.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        availability_zone: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_subnet_group_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        preferred_maintenance_window: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        multi_az: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        engine_version: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        auto_minor_version_upgrade: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
        kms_key_id: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        publicly_accessible: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        dns_name_servers: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        resource_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        network_type: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        kerberos_authentication_settings: Optional[
            "capo_database_migration_service.types.kerberos_authentication_settings.KerberosAuthenticationSettings"
        ] = None,
    ) -> "capo_database_migration_service.types.create_replication_instance_response.CreateReplicationInstanceResponse":
        """<p>Creates the replication instance using the specified parameters.</p> <p>DMS requires that your account have certain roles with appropriate permissions before you can create a replication instance. For information on the required roles, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.APIRole">Creating the IAM Roles to Use With the CLI and DMS API</a>. For information on the required permissions, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.IAMPermissions">IAM Permissions Needed to Use DMS</a>.</p> <note> <p>If you don't specify a version when creating a replication instance, DMS will create the instance using the default engine version. For information about the default engine version, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReleaseNotes.html">Release Notes</a>.</p> </note>

        Args:
            replication_instance_identifier: <p>The replication instance identifier. This parameter is stored as a lowercase string.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-63 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Can't end with a hyphen or contain two consecutive hyphens.</p> </li> </ul> <p>Example: <code>myrepinstance</code> </p>
            allocated_storage: <p>The amount of storage (in gigabytes) to be initially allocated for the replication instance.</p>
            replication_instance_class: <p>The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to <code>"dms.c4.large"</code>.</p> <p>For more information on the settings and capacities for the available replication instance classes, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Types.html "> Choosing the right DMS replication instance</a>; and, <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_BestPractices.SizingReplicationInstance.html">Selecting the best size for a replication instance</a>. </p>
            vpc_security_group_ids: <p> Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance. </p>
            availability_zone: <p>The Availability Zone where the replication instance will be created. The default value is a random, system-chosen Availability Zone in the endpoint's Amazon Web Services Region, for example: <code>us-east-1d</code>.</p>
            replication_subnet_group_identifier: <p>A subnet group to associate with the replication instance.</p>
            preferred_maintenance_window: <p>The weekly time range during which system maintenance can occur, in Universal Coordinated Time (UTC).</p> <p> Format: <code>ddd:hh24:mi-ddd:hh24:mi</code> </p> <p>Default: A 30-minute window selected at random from an 8-hour block of time per Amazon Web Services Region, occurring on a random day of the week.</p> <p>Valid Days: Mon, Tue, Wed, Thu, Fri, Sat, Sun</p> <p>Constraints: Minimum 30-minute window.</p>
            multi_az: <p> Specifies whether the replication instance is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the Multi-AZ parameter is set to <code>true</code>. </p>
            engine_version: <p>The engine version number of the replication instance.</p> <p>If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.</p>
            auto_minor_version_upgrade: <p>A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to <code>true</code>.</p> <p>Default: <code>true</code> </p>
            tags: <p>One or more tags to be assigned to the replication instance.</p>
            kms_key_id: <p>An KMS key identifier that is used to encrypt the data on the replication instance.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>
            publicly_accessible: <p> Specifies the accessibility options for the replication instance. A value of <code>true</code> represents an instance with a public IP address. A value of <code>false</code> represents an instance with a private IP address. The default value is <code>true</code>. </p>
            dns_name_servers: <p>A list of custom DNS name servers supported for the replication instance to access your on-premise source or target database. This list overrides the default name servers supported by the replication instance. You can specify a comma-separated list of internet addresses for up to four on-premise DNS name servers. For example: <code>"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"</code> </p>
            resource_identifier: <p>A friendly name for the resource identifier at the end of the <code>EndpointArn</code> response parameter that is returned in the created <code>Endpoint</code> object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as <code>Example-App-ARN1</code>. For example, this value might result in the <code>EndpointArn</code> value <code>arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1</code>. If you don't specify a <code>ResourceIdentifier</code> value, DMS generates a default identifier value for the end of <code>EndpointArn</code>.</p>
            network_type: <p>The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.</p>
            kerberos_authentication_settings: <p>Specifies the settings required for kerberos authentication when creating the replication instance.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.insufficient_resource_capacity_fault.InsufficientResourceCapacityFault: <p>There are not enough resources allocated to the database migration.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.invalid_subnet.InvalidSubnet: <p>The subnet provided isn't valid.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.replication_subnet_group_does_not_cover_enough_a_zs.ReplicationSubnetGroupDoesNotCoverEnoughAZs: <p>The replication subnet group does not cover enough Availability Zones (AZs). Edit the replication subnet group and add more AZs.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The storage quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create replication instance
            Creates the replication instance using the specified parameters.

            >>> await client.create_replication_instance(replication_instance_identifier='', allocated_storage=123, replication_instance_class='', vpc_security_group_ids=[], availability_zone='', replication_subnet_group_identifier='', preferred_maintenance_window='', multi_az=True, engine_version='', auto_minor_version_upgrade=True, tags=[{'Key': 'string', 'Value': 'string'}], kms_key_id='', publicly_accessible=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_replication_instance_message.CreateReplicationInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_replication_instance_response.CreateReplicationInstanceResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_instance

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_instance.async_create_replication_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_replication_instance_message.CreateReplicationInstanceMessage = {
            "replication_instance_identifier": replication_instance_identifier,
            "replication_instance_class": replication_instance_class,
        }
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if replication_subnet_group_identifier is not None:
            input_["replication_subnet_group_identifier"] = (
                replication_subnet_group_identifier
            )
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if dns_name_servers is not None:
            input_["dns_name_servers"] = dns_name_servers
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if network_type is not None:
            input_["network_type"] = network_type
        if kerberos_authentication_settings is not None:
            input_["kerberos_authentication_settings"] = (
                kerberos_authentication_settings
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def create_replication_subnet_group(
        self,
        replication_subnet_group_identifier: "capo_database_migration_service.types.string.String",
        replication_subnet_group_description: "capo_database_migration_service.types.string.String",
        subnet_ids: "capo_database_migration_service.types.subnet_identifier_list.SubnetIdentifierList",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
    ) -> "capo_database_migration_service.types.create_replication_subnet_group_response.CreateReplicationSubnetGroupResponse":
        """<p>Creates a replication subnet group given a list of the subnet IDs in a VPC.</p> <p>The VPC needs to have at least one subnet in at least two availability zones in the Amazon Web Services Region, otherwise the service will throw a <code>ReplicationSubnetGroupDoesNotCoverEnoughAZs</code> exception.</p> <p>If a replication subnet group exists in your Amazon Web Services account, the CreateReplicationSubnetGroup action returns the following error message: The Replication Subnet Group already exists. In this case, delete the existing replication subnet group. To do so, use the <a href="https://docs.aws.amazon.com/en_us/dms/latest/APIReference/API_DeleteReplicationSubnetGroup.html">DeleteReplicationSubnetGroup</a> action. Optionally, choose Subnet groups in the DMS console, then choose your subnet group. Next, choose Delete from Actions.</p>

        Args:
            replication_subnet_group_identifier: <p>The name for the replication subnet group. This value is stored as a lowercase string.</p> <p>Constraints: Must contain no more than 255 alphanumeric characters, periods, underscores, or hyphens. Must not be "default".</p> <p>Example: <code>mySubnetgroup</code> </p>
            replication_subnet_group_description: <p>The description for the subnet group. </p> <p>Constraints: This parameter Must not contain non-printable control characters.</p>
            subnet_ids: <p>Two or more subnet IDs to be assigned to the subnet group.</p>
            tags: <p>One or more tags to be assigned to the subnet group.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_subnet.InvalidSubnet: <p>The subnet provided isn't valid.</p>
            capo_database_migration_service.errors.replication_subnet_group_does_not_cover_enough_a_zs.ReplicationSubnetGroupDoesNotCoverEnoughAZs: <p>The replication subnet group does not cover enough Availability Zones (AZs). Edit the replication subnet group and add more AZs.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create replication subnet group
            Creates a replication subnet group given a list of the subnet IDs in a VPC.

            >>> await client.create_replication_subnet_group(replication_subnet_group_identifier='us-west-2ab-vpc-215ds366', replication_subnet_group_description='US West subnet group', subnet_ids=['subnet-e145356n', 'subnet-58f79200'], tags=[{'Key': 'Acount', 'Value': '145235'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_replication_subnet_group_message.CreateReplicationSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_replication_subnet_group_response.CreateReplicationSubnetGroupResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_subnet_group

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_subnet_group.async_create_replication_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_replication_subnet_group_message.CreateReplicationSubnetGroupMessage = {
            "replication_subnet_group_identifier": replication_subnet_group_identifier,
            "replication_subnet_group_description": replication_subnet_group_description,
            "subnet_ids": subnet_ids,
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

    async def create_replication_task(
        self,
        replication_task_identifier: "capo_database_migration_service.types.string.String",
        source_endpoint_arn: "capo_database_migration_service.types.string.String",
        target_endpoint_arn: "capo_database_migration_service.types.string.String",
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        migration_type: "capo_database_migration_service.types.migration_type_value.MigrationTypeValue",
        table_mappings: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_task_settings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        cdc_start_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        cdc_start_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        cdc_stop_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
        task_data: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        resource_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.create_replication_task_response.CreateReplicationTaskResponse":
        """<p>Creates a replication task using the specified parameters.</p>

        Args:
            replication_task_identifier: <p>An identifier for the replication task.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            source_endpoint_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.</p>
            target_endpoint_arn: <p>An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.</p>
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of a replication instance.</p>
            migration_type: <p>The migration type. Valid values: <code>full-load</code> | <code>cdc</code> | <code>full-load-and-cdc</code> </p>
            table_mappings: <p>The table mappings for the task, in JSON format. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html">Using Table Mapping to Specify Task Settings</a> in the <i>Database Migration Service User Guide.</i> </p>
            replication_task_settings: <p>Overall settings for the task, in JSON format. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html">Specifying Task Settings for Database Migration Service Tasks</a> in the <i>Database Migration Service User Guide.</i> </p>
            cdc_start_time: <p>Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p>Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”</p>
            cdc_start_position: <p>Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p> The value can be in date, checkpoint, or LSN/SCN format.</p> <p>Date Example: --cdc-start-position “2018-03-08T12:12:12”</p> <p>Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"</p> <p>LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”</p> <note> <p>When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the <code>slotName</code> extra connection attribute to the name of this logical replication slot. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib">Extra Connection Attributes When Using PostgreSQL as a Source for DMS</a>.</p> </note>
            cdc_stop_position: <p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p> <p>Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”</p> <p>Commit time example: --cdc-stop-position “commit_time:2018-02-09T12:12:12“</p>
            tags: <p>One or more tags to be assigned to the replication task.</p>
            task_data: <p>Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html">Specifying Supplemental Data for Task Settings</a> in the <i>Database Migration Service User Guide.</i> </p>
            resource_identifier: <p>A friendly name for the resource identifier at the end of the <code>EndpointArn</code> response parameter that is returned in the created <code>Endpoint</code> object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as <code>Example-App-ARN1</code>. For example, this value might result in the <code>EndpointArn</code> value <code>arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1</code>. If you don't specify a <code>ResourceIdentifier</code> value, DMS generates a default identifier value for the end of <code>EndpointArn</code>.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create replication task
            Creates a replication task using the specified parameters.

            >>> await client.create_replication_task(replication_task_identifier='task1', source_endpoint_arn='arn:aws:dms:us-east-1:123456789012:endpoint:ZW5UAN6P4E77EC7YWHK4RZZ3BE', target_endpoint_arn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E', replication_instance_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ', migration_type='full-load', table_mappings='file://mappingfile.json', replication_task_settings='', cdc_start_time='2016-12-14T18:25:43Z', tags=[{'Key': 'Acount', 'Value': '24352226'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.create_replication_task_message.CreateReplicationTaskMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.create_replication_task_response.CreateReplicationTaskResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_task

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.create_replication_task.async_create_replication_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.create_replication_task_message.CreateReplicationTaskMessage = {
            "replication_task_identifier": replication_task_identifier,
            "source_endpoint_arn": source_endpoint_arn,
            "target_endpoint_arn": target_endpoint_arn,
            "replication_instance_arn": replication_instance_arn,
            "migration_type": migration_type,
            "table_mappings": table_mappings,
        }
        if replication_task_settings is not None:
            input_["replication_task_settings"] = replication_task_settings
        if cdc_start_time is not None:
            input_["cdc_start_time"] = cdc_start_time
        if cdc_start_position is not None:
            input_["cdc_start_position"] = cdc_start_position
        if cdc_stop_position is not None:
            input_["cdc_stop_position"] = cdc_stop_position
        if tags is not None:
            input_["tags"] = tags
        if task_data is not None:
            input_["task_data"] = task_data
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_certificate(
        self,
        certificate_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_certificate_response.DeleteCertificateResponse":
        """<p>Deletes the specified certificate. </p>

        Args:
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Certificate
            Deletes the specified certificate.

            >>> await client.delete_certificate(certificate_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUSM457DE6XFJCJQ')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_certificate_message.DeleteCertificateMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_certificate_response.DeleteCertificateResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_certificate

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_certificate.async_delete_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_certificate_message.DeleteCertificateMessage = {
            "certificate_arn": certificate_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_connection(
        self,
        endpoint_arn: "capo_database_migration_service.types.string.String",
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_connection_response.DeleteConnectionResponse":
        """<p>Deletes the connection between a replication instance and an endpoint.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Connection
            Deletes the connection between the replication instance and the endpoint.

            >>> await client.delete_connection(replication_instance_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ', endpoint_arn='arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_connection_message.DeleteConnectionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_connection_response.DeleteConnectionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_connection

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_connection.async_delete_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_connection_message.DeleteConnectionMessage = {
            "endpoint_arn": endpoint_arn,
            "replication_instance_arn": replication_instance_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_migration(
        self,
        data_migration_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_data_migration_response.DeleteDataMigrationResponse":
        """<p>Deletes the specified data migration.</p>

        Args:
            data_migration_identifier: <p>The identifier (name or ARN) of the data migration to delete.</p>

        Raises:
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_data_migration_message.DeleteDataMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_data_migration_response.DeleteDataMigrationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_data_migration

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_data_migration.async_delete_data_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_data_migration_message.DeleteDataMigrationMessage = {
            "data_migration_identifier": data_migration_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_data_provider(
        self,
        data_provider_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_data_provider_response.DeleteDataProviderResponse":
        """<p>Deletes the specified data provider.</p> <p> <b>Required permissions:</b> <code>dms:DeleteDataProvider</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p> <note> <p>All migration projects associated with the data provider must be deleted or modified before you can delete the data provider.</p> </note>

        Args:
            data_provider_identifier: <p>The identifier of the data provider to delete.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a data provider
            The following example deletes a data provider identified by its ARN.

            >>> await client.delete_data_provider(data_provider_identifier='arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_data_provider_message.DeleteDataProviderMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_data_provider_response.DeleteDataProviderResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_data_provider

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_data_provider.async_delete_data_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_data_provider_message.DeleteDataProviderMessage = {
            "data_provider_identifier": data_provider_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_endpoint(
        self,
        endpoint_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_endpoint_response.DeleteEndpointResponse":
        """<p>Deletes the specified endpoint.</p> <note> <p>All tasks associated with the endpoint must be deleted before you can delete the endpoint.</p> </note> <p></p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Endpoint
            Deletes the specified endpoint. All tasks associated with the endpoint must be deleted before you can delete the endpoint.


            >>> await client.delete_endpoint(endpoint_arn='arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_endpoint_message.DeleteEndpointMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_endpoint_response.DeleteEndpointResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_endpoint

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_endpoint.async_delete_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_endpoint_message.DeleteEndpointMessage = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_event_subscription(
        self,
        subscription_name: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_event_subscription_response.DeleteEventSubscriptionResponse":
        """<p> Deletes an DMS event subscription. </p>

        Args:
            subscription_name: <p>The name of the DMS event notification subscription to be deleted.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_event_subscription_message.DeleteEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_event_subscription_response.DeleteEventSubscriptionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_event_subscription

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_event_subscription.async_delete_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_event_subscription_message.DeleteEventSubscriptionMessage = {
            "subscription_name": subscription_name
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_fleet_advisor_collector(
        self,
        collector_referenced_id: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> None:
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Deletes the specified Fleet Advisor collector.</p>

        Args:
            collector_referenced_id: <p>The reference ID of the Fleet Advisor collector to delete.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.collector_not_found_fault.CollectorNotFoundFault: <p>The specified collector doesn't exist.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_collector_request.DeleteCollectorRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_fleet_advisor_collector

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_fleet_advisor_collector.async_delete_fleet_advisor_collector(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_collector_request.DeleteCollectorRequest = {
            "collector_referenced_id": collector_referenced_id
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_fleet_advisor_databases(
        self,
        database_ids: "capo_database_migration_service.types.string_list.StringList",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_fleet_advisor_databases_response.DeleteFleetAdvisorDatabasesResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Deletes the specified Fleet Advisor collector databases.</p>

        Args:
            database_ids: <p>The IDs of the Fleet Advisor collector databases to delete.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_operation_fault.InvalidOperationFault: <p>The action or operation requested isn't valid.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_fleet_advisor_databases_request.DeleteFleetAdvisorDatabasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_fleet_advisor_databases_response.DeleteFleetAdvisorDatabasesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_fleet_advisor_databases

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_fleet_advisor_databases.async_delete_fleet_advisor_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_fleet_advisor_databases_request.DeleteFleetAdvisorDatabasesRequest = {
            "database_ids": database_ids
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_instance_profile(
        self,
        instance_profile_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_instance_profile_response.DeleteInstanceProfileResponse":
        """<p>Deletes the specified instance profile.</p> <p> <b>Required permissions:</b> <code>dms:DeleteInstanceProfile</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p> <note> <p>All migration projects associated with the instance profile must be deleted or modified before you can delete the instance profile.</p> </note>

        Args:
            instance_profile_identifier: <p>The identifier of the instance profile to delete.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete an instance profile
            The following example deletes an instance profile identified by its ARN.

            >>> await client.delete_instance_profile(instance_profile_identifier='arn:aws:dms:us-east-1:111122223333:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_instance_profile_message.DeleteInstanceProfileMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_instance_profile_response.DeleteInstanceProfileResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_instance_profile

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_instance_profile.async_delete_instance_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_instance_profile_message.DeleteInstanceProfileMessage = {
            "instance_profile_identifier": instance_profile_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_migration_project(
        self,
        migration_project_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_migration_project_response.DeleteMigrationProjectResponse":
        """<p>Deletes the specified migration project.</p> <p> <b>Required permissions:</b> <code>dms:DeleteMigrationProject</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p> <note> <p>The migration project must be closed before you can delete it.</p> </note>

        Args:
            migration_project_identifier: <p>The name or Amazon Resource Name (ARN) of the migration project to delete.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a migration project
            The following example deletes a migration project identified by its ARN.

            >>> await client.delete_migration_project(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_migration_project_message.DeleteMigrationProjectMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_migration_project_response.DeleteMigrationProjectResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_migration_project

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_migration_project.async_delete_migration_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_migration_project_message.DeleteMigrationProjectMessage = {
            "migration_project_identifier": migration_project_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_config(
        self,
        replication_config_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_replication_config_response.DeleteReplicationConfigResponse":
        """<p>Deletes an DMS Serverless replication configuration. This effectively deprovisions any and all replications that use this configuration. You can't delete the configuration for an DMS Serverless replication that is ongoing. You can delete the configuration when the replication is in a non-RUNNING and non-STARTING state.</p>

        Args:
            replication_config_arn: <p>The replication config to delete.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_replication_config_message.DeleteReplicationConfigMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_replication_config_response.DeleteReplicationConfigResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_config

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_config.async_delete_replication_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_replication_config_message.DeleteReplicationConfigMessage = {
            "replication_config_arn": replication_config_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_instance(
        self,
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_replication_instance_response.DeleteReplicationInstanceResponse":
        """<p>Deletes the specified replication instance.</p> <note> <p>You must delete any migration tasks that are associated with the replication instance before you can delete it.</p> </note> <p></p>

        Args:
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance to be deleted.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Replication Instance
            Deletes the specified replication instance. You must delete any migration tasks that are associated with the replication instance before you can delete it.



            >>> await client.delete_replication_instance(replication_instance_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_replication_instance_message.DeleteReplicationInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_replication_instance_response.DeleteReplicationInstanceResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_instance

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_instance.async_delete_replication_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_replication_instance_message.DeleteReplicationInstanceMessage = {
            "replication_instance_arn": replication_instance_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_subnet_group(
        self,
        replication_subnet_group_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_replication_subnet_group_response.DeleteReplicationSubnetGroupResponse":
        """<p>Deletes a subnet group.</p>

        Args:
            replication_subnet_group_identifier: <p>The subnet group name of the replication instance.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Replication Subnet Group
            Deletes a replication subnet group.

            >>> await client.delete_replication_subnet_group(replication_subnet_group_identifier='us-west-2ab-vpc-215ds366')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_replication_subnet_group_message.DeleteReplicationSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_replication_subnet_group_response.DeleteReplicationSubnetGroupResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_subnet_group

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_subnet_group.async_delete_replication_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_replication_subnet_group_message.DeleteReplicationSubnetGroupMessage = {
            "replication_subnet_group_identifier": replication_subnet_group_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_task(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_replication_task_response.DeleteReplicationTaskResponse":
        """<p>Deletes the specified replication task.</p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name (ARN) of the replication task to be deleted.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete Replication Task
            Deletes the specified replication task.

            >>> await client.delete_replication_task(replication_task_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_replication_task_message.DeleteReplicationTaskMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_replication_task_response.DeleteReplicationTaskResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_task

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_task.async_delete_replication_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_replication_task_message.DeleteReplicationTaskMessage = {
            "replication_task_arn": replication_task_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def delete_replication_task_assessment_run(
        self,
        replication_task_assessment_run_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.delete_replication_task_assessment_run_response.DeleteReplicationTaskAssessmentRunResponse":
        """<p>Deletes the record of a single premigration assessment run.</p> <p>This operation removes all metadata that DMS maintains about this assessment run. However, the operation leaves untouched all information about this assessment run that is stored in your Amazon S3 bucket.</p>

        Args:
            replication_task_assessment_run_arn: <p>Amazon Resource Name (ARN) of the premigration assessment run to be deleted.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.delete_replication_task_assessment_run_message.DeleteReplicationTaskAssessmentRunMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.delete_replication_task_assessment_run_response.DeleteReplicationTaskAssessmentRunResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_task_assessment_run

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.delete_replication_task_assessment_run.async_delete_replication_task_assessment_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.delete_replication_task_assessment_run_message.DeleteReplicationTaskAssessmentRunMessage = {
            "replication_task_assessment_run_arn": replication_task_assessment_run_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_account_attributes(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.describe_account_attributes_response.DescribeAccountAttributesResponse":
        """<p>Lists all of the DMS attributes for a customer account. These attributes include DMS quotas for the account and a unique account identifier in a particular DMS region. DMS quotas include a list of resource quotas supported by the account, such as the number of replication instances allowed. The description for each resource quota, includes the quota name, current usage toward that quota, and the quota's maximum value. DMS uses the unique account identifier to name each artifact used by DMS in the given region.</p> <p>This command does not take any parameters.</p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe acount attributes
            Lists all of the AWS DMS attributes for a customer account. The attributes include AWS DMS quotas for the account, such as the number of replication instances allowed. The description for a quota includes the quota name, current usage toward that quota, and the quota's maximum value. This operation does not take any parameters.

            >>> await client.describe_account_attributes()
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_account_attributes_message.DescribeAccountAttributesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_account_attributes_response.DescribeAccountAttributesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_account_attributes

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_account_attributes.async_describe_account_attributes(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_account_attributes_message.DescribeAccountAttributesMessage = {}

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_applicable_individual_assessments(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_task_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_instance_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_config_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        source_engine_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        target_engine_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        migration_type: Optional[
            "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_applicable_individual_assessments_response.DescribeApplicableIndividualAssessmentsResponse":
        """<p>Provides a list of individual assessments that you can specify for a new premigration assessment run, given one or more parameters.</p> <p>If you specify an existing migration task, this operation provides the default individual assessments you can specify for that task. Otherwise, the specified parameters model elements of a possible migration task on which to base a premigration assessment run.</p> <p>To use these migration task modeling parameters, you must specify an existing replication instance, a source database engine, a target database engine, and a migration type. This combination of parameters potentially limits the default individual assessments available for an assessment run created for a corresponding migration task.</p> <p>If you specify no parameters, this operation provides a list of all possible individual assessments that you can specify for an assessment run. If you specify any one of the task modeling parameters, you must specify all of them or the operation cannot provide a list of individual assessments. The only parameter that you can specify alone is for an existing migration task. The specified task definition then determines the default list of individual assessments that you can specify in an assessment run for the task.</p>

        Args:
            replication_task_arn: <p>Amazon Resource Name (ARN) of a migration task on which you want to base the default list of individual assessments.</p>
            replication_instance_arn: <p>ARN of a replication instance on which you want to base the default list of individual assessments.</p>
            replication_config_arn: <p>Amazon Resource Name (ARN) of a serverless replication on which you want to base the default list of individual assessments.</p>
            source_engine_name: <p>Name of a database engine that the specified replication instance supports as a source.</p>
            target_engine_name: <p>Name of a database engine that the specified replication instance supports as a target.</p>
            migration_type: <p>Name of the migration type that each provided individual assessment must support.</p>
            max_records: <p>Maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p>
            marker: <p>Optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_applicable_individual_assessments_message.DescribeApplicableIndividualAssessmentsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_applicable_individual_assessments_response.DescribeApplicableIndividualAssessmentsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_applicable_individual_assessments

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_applicable_individual_assessments.async_describe_applicable_individual_assessments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_applicable_individual_assessments_message.DescribeApplicableIndividualAssessmentsMessage = {}
        if replication_task_arn is not None:
            input_["replication_task_arn"] = replication_task_arn
        if replication_instance_arn is not None:
            input_["replication_instance_arn"] = replication_instance_arn
        if replication_config_arn is not None:
            input_["replication_config_arn"] = replication_config_arn
        if source_engine_name is not None:
            input_["source_engine_name"] = source_engine_name
        if target_engine_name is not None:
            input_["target_engine_name"] = target_engine_name
        if migration_type is not None:
            input_["migration_type"] = migration_type
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_applicable_individual_assessments(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_task_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_instance_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_config_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        source_engine_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        target_engine_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        migration_type: Optional[
            "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_applicable_individual_assessments_response.DescribeApplicableIndividualAssessmentsResponse]":
        _token = marker
        while True:
            _response = await self.describe_applicable_individual_assessments(
                config_overrides=config_overrides,
                replication_task_arn=replication_task_arn,
                replication_instance_arn=replication_instance_arn,
                replication_config_arn=replication_config_arn,
                source_engine_name=source_engine_name,
                target_engine_name=target_engine_name,
                migration_type=migration_type,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_certificates(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_certificates_response.DescribeCertificatesResponse":
        """<p>Provides a description of the certificate.</p>

        Args:
            filters: <p>Filters applied to the certificates described in the form of key-value pairs. Valid values are <code>certificate-arn</code> and <code>certificate-id</code>.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 10</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe certificates
            Provides a description of the certificate.

            >>> await client.describe_certificates(filters=[{'Name': 'string', 'Values': ['string', 'string']}], max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_certificates_message.DescribeCertificatesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_certificates_response.DescribeCertificatesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_certificates

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_certificates.async_describe_certificates(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_certificates_message.DescribeCertificatesMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_certificates(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_certificates_response.DescribeCertificatesResponse]":
        _token = marker
        while True:
            _response = await self.describe_certificates(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_connections(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_connections_response.DescribeConnectionsResponse":
        """<p>Describes the status of the connections that have been made between the replication instance and an endpoint. Connections are created when you test an endpoint.</p>

        Args:
            filters: <p>The filters applied to the connection.</p> <p>Valid filter names: endpoint-arn | replication-instance-arn</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe connections
            Describes the status of the connections that have been made between the replication instance and an endpoint. Connections are created when you test an endpoint.

            >>> await client.describe_connections(filters=[{'Name': 'string', 'Values': ['string', 'string']}], max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_connections_message.DescribeConnectionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_connections_response.DescribeConnectionsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_connections

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_connections.async_describe_connections(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_connections_message.DescribeConnectionsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_connections(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_connections_response.DescribeConnectionsResponse]":
        _token = marker
        while True:
            _response = await self.describe_connections(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_conversion_configuration(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.describe_conversion_configuration_response.DescribeConversionConfigurationResponse":
        """<p>Returns configuration parameters for a schema conversion project.</p> <p> <b>Required permissions:</b> <code>dms:DescribeConversionConfiguration</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The name or Amazon Resource Name (ARN) for the schema conversion project to describe.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieving conversion configuration for a migration project
            The following example retrieves the conversion configuration for a migration project.

            >>> await client.describe_conversion_configuration(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_conversion_configuration_message.DescribeConversionConfigurationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_conversion_configuration_response.DescribeConversionConfigurationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_conversion_configuration

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_conversion_configuration.async_describe_conversion_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_conversion_configuration_message.DescribeConversionConfigurationMessage = {
            "migration_project_identifier": migration_project_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_data_migrations(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.marker.Marker"] = None,
        without_settings: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        without_statistics: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_data_migrations_response.DescribeDataMigrationsResponse":
        """<p>Returns information about data migrations.</p>

        Args:
            filters: <p>Filters applied to the data migrations.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>
            without_settings: <p>An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose <code>true</code>; otherwise, choose <code>false</code> (the default).</p>
            without_statistics: <p>An option to set to avoid returning information about statistics. Use this to reduce overhead when statistics information is too large. To use this option, choose <code>true</code>; otherwise, choose <code>false</code> (the default).</p>

        Raises:
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_data_migrations_message.DescribeDataMigrationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_data_migrations_response.DescribeDataMigrationsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_data_migrations

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_data_migrations.async_describe_data_migrations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_data_migrations_message.DescribeDataMigrationsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if without_settings is not None:
            input_["without_settings"] = without_settings
        if without_statistics is not None:
            input_["without_statistics"] = without_statistics

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_data_migrations(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.marker.Marker"] = None,
        without_settings: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        without_statistics: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.data_migration.DataMigration]":
        _token = marker
        while True:
            _response = await self.describe_data_migrations(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
                without_settings=without_settings,
                without_statistics=without_statistics,
            )
            _page = _resolve_path(_response, ("data_migrations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_data_providers(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_data_providers_response.DescribeDataProvidersResponse":
        """<p>Returns a paginated list of data providers for your account in the current region.</p> <p> <b>Required permissions:</b> <code>dms:ListDataProviders</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            filters: <p>The filters to apply to the data providers.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>data-provider-identifier</code> – The data provider name or ARN.</p> </li> </ul>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe data providers with a filter
            The following example retrieves the details of a data provider identified by its ARN.

            >>> await client.describe_data_providers(filters=[{'Name': 'data-provider-identifier', 'Values': ['arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_data_providers_message.DescribeDataProvidersMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_data_providers_response.DescribeDataProvidersResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_data_providers

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_data_providers.async_describe_data_providers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_data_providers_message.DescribeDataProvidersMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_data_providers(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_data_providers_response.DescribeDataProvidersResponse]":
        _token = marker
        while True:
            _response = await self.describe_data_providers(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_endpoints_response.DescribeEndpointsResponse":
        """<p>Returns information about the endpoints for your account in the current region.</p>

        Args:
            filters: <p>Filters applied to the endpoints.</p> <p>Valid filter names: endpoint-arn | endpoint-type | endpoint-id | engine-name</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe endpoints
            Returns information about the endpoints for your account in the current region.

            >>> await client.describe_endpoints(filters=[{'Name': 'string', 'Values': ['string', 'string']}], max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_endpoints_message.DescribeEndpointsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_endpoints_response.DescribeEndpointsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_endpoints

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_endpoints.async_describe_endpoints(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_endpoints_message.DescribeEndpointsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_endpoints(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_endpoints_response.DescribeEndpointsResponse]":
        _token = marker
        while True:
            _response = await self.describe_endpoints(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_endpoint_settings(
        self,
        engine_name: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_endpoint_settings_response.DescribeEndpointSettingsResponse":
        """<p>Returns information about the possible endpoint settings available when you create an endpoint for a specific database engine.</p>

        Args:
            engine_name: <p>The database engine used for your source or target endpoint.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_endpoint_settings_message.DescribeEndpointSettingsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_endpoint_settings_response.DescribeEndpointSettingsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_endpoint_settings

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_endpoint_settings.async_describe_endpoint_settings(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_endpoint_settings_message.DescribeEndpointSettingsMessage = {
            "engine_name": engine_name
        }
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_endpoint_settings(
        self,
        engine_name: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_endpoint_settings_response.DescribeEndpointSettingsResponse]":
        _token = marker
        while True:
            _response = await self.describe_endpoint_settings(
                engine_name,
                config_overrides=config_overrides,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_endpoint_types(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_endpoint_types_response.DescribeEndpointTypesResponse":
        """<p>Returns information about the type of endpoints available.</p>

        Args:
            filters: <p>Filters applied to the endpoint types.</p> <p>Valid filter names: engine-name | endpoint-type</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe endpoint types
            Returns information about the type of endpoints available.

            >>> await client.describe_endpoint_types(filters=[{'Name': 'string', 'Values': ['string', 'string']}], max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_endpoint_types_message.DescribeEndpointTypesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_endpoint_types_response.DescribeEndpointTypesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_endpoint_types

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_endpoint_types.async_describe_endpoint_types(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_endpoint_types_message.DescribeEndpointTypesMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_endpoint_types(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_endpoint_types_response.DescribeEndpointTypesResponse]":
        _token = marker
        while True:
            _response = await self.describe_endpoint_types(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_engine_versions_response.DescribeEngineVersionsResponse":
        """<p>Returns information about the replication instance versions used in the project.</p>

        Args:
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_engine_versions_message.DescribeEngineVersionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_engine_versions_response.DescribeEngineVersionsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_engine_versions

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_engine_versions.async_describe_engine_versions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_engine_versions_message.DescribeEngineVersionsMessage = {}
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_engine_versions(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_engine_versions_response.DescribeEngineVersionsResponse]":
        _token = marker
        while True:
            _response = await self.describe_engine_versions(
                config_overrides=config_overrides,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_event_categories(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        source_type: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_event_categories_response.DescribeEventCategoriesResponse":
        """<p>Lists categories for all event source types, or, if specified, for a specified source type. You can see a list of the event categories and source types in <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html">Working with Events and Notifications</a> in the <i>Database Migration Service User Guide.</i> </p>

        Args:
            source_type: <p> The type of DMS resource that generates events. </p> <p>Valid values: replication-instance | replication-task</p>
            filters: <p>Filters applied to the event categories.</p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_event_categories_message.DescribeEventCategoriesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_event_categories_response.DescribeEventCategoriesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_event_categories

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_event_categories.async_describe_event_categories(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_event_categories_message.DescribeEventCategoriesMessage = {}
        if source_type is not None:
            input_["source_type"] = source_type
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_events(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        source_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        source_type: Optional[
            "capo_database_migration_service.types.source_type.SourceType"
        ] = None,
        start_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        end_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        duration: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        event_categories: Optional[
            "capo_database_migration_service.types.event_categories_list.EventCategoriesList"
        ] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_events_response.DescribeEventsResponse":
        """<p> Lists events for a given source identifier and source type. You can also specify a start and end time. For more information on DMS events, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html">Working with Events and Notifications</a> in the <i>Database Migration Service User Guide.</i> </p>

        Args:
            source_identifier: <p> The identifier of an event source.</p>
            source_type: <p>The type of DMS resource that generates events.</p> <p>Valid values: replication-instance | replication-task</p>
            start_time: <p>The start time for the events to be listed.</p>
            end_time: <p>The end time for the events to be listed.</p>
            duration: <p>The duration of the events to be listed.</p>
            event_categories: <p>A list of event categories for the source type that you've chosen.</p>
            filters: <p>Filters applied to events. The only valid filter is <code>replication-instance-id</code>.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_events_message.DescribeEventsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_events_response.DescribeEventsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_events

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_events.async_describe_events(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_events_message.DescribeEventsMessage = {}
        if source_identifier is not None:
            input_["source_identifier"] = source_identifier
        if source_type is not None:
            input_["source_type"] = source_type
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
        if duration is not None:
            input_["duration"] = duration
        if event_categories is not None:
            input_["event_categories"] = event_categories
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_events(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        source_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        source_type: Optional[
            "capo_database_migration_service.types.source_type.SourceType"
        ] = None,
        start_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        end_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        duration: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        event_categories: Optional[
            "capo_database_migration_service.types.event_categories_list.EventCategoriesList"
        ] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_events_response.DescribeEventsResponse]":
        _token = marker
        while True:
            _response = await self.describe_events(
                config_overrides=config_overrides,
                source_identifier=source_identifier,
                source_type=source_type,
                start_time=start_time,
                end_time=end_time,
                duration=duration,
                event_categories=event_categories,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_event_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        subscription_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_event_subscriptions_response.DescribeEventSubscriptionsResponse":
        """<p>Lists all the event subscriptions for a customer account. The description of a subscription includes <code>SubscriptionName</code>, <code>SNSTopicARN</code>, <code>CustomerID</code>, <code>SourceType</code>, <code>SourceID</code>, <code>CreationTime</code>, and <code>Status</code>. </p> <p>If you specify <code>SubscriptionName</code>, this action lists the description for that subscription.</p>

        Args:
            subscription_name: <p>The name of the DMS event subscription to be described.</p>
            filters: <p>Filters applied to event subscriptions.</p> <p>Valid filter names: <code>event-subscription-arn</code> | <code>event-subscription-id</code> </p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_event_subscriptions_response.DescribeEventSubscriptionsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_event_subscriptions

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_event_subscriptions.async_describe_event_subscriptions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_event_subscriptions_message.DescribeEventSubscriptionsMessage = {}
        if subscription_name is not None:
            input_["subscription_name"] = subscription_name
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_event_subscriptions(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        subscription_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_event_subscriptions_response.DescribeEventSubscriptionsResponse]":
        _token = marker
        while True:
            _response = await self.describe_event_subscriptions(
                config_overrides=config_overrides,
                subscription_name=subscription_name,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_extension_pack_associations(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_extension_pack_associations_response.DescribeExtensionPackAssociationsResponse":
        """<p>Returns a paginated list of extension pack installation requests for a migration project, initiated by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartExtensionPackAssociation.html">StartExtensionPackAssociation</a>.</p> <p> <b>Required permissions:</b> <code>dms:ListExtensionPacks</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            filters: <p>The filters to apply to the extension pack installation requests.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>request-id</code> – The request identifier.</p> </li> <li> <p> <code>status</code> – The request status. Valid values: <code>RECEIVED</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>.</p> </li> </ul>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the status of extension pack associations
            The following example retrieves the status of operations that apply an extension pack to the target database, identified by their request IDs.

            >>> await client.describe_extension_pack_associations(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', filters=[{'Name': 'request-id', 'Values': ['a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_extension_pack_associations_message.DescribeExtensionPackAssociationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_extension_pack_associations_response.DescribeExtensionPackAssociationsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_extension_pack_associations

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_extension_pack_associations.async_describe_extension_pack_associations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_extension_pack_associations_message.DescribeExtensionPackAssociationsMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_extension_pack_associations(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_extension_pack_associations_response.DescribeExtensionPackAssociationsResponse]":
        _token = marker
        while True:
            _response = await self.describe_extension_pack_associations(
                migration_project_identifier,
                config_overrides=config_overrides,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_fleet_advisor_collectors(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_fleet_advisor_collectors_response.DescribeFleetAdvisorCollectorsResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Returns a list of the Fleet Advisor collectors in your account.</p>

        Args:
            filters: <p> If you specify any of the following filters, the output includes information for only those collectors that meet the filter criteria:</p> <ul> <li> <p> <code>collector-referenced-id</code> – The ID of the collector agent, for example <code>d4610ac5-e323-4ad9-bc50-eaf7249dfe9d</code>.</p> </li> <li> <p> <code>collector-name</code> – The name of the collector agent.</p> </li> </ul> <p>An example is: <code>describe-fleet-advisor-collectors --filter Name="collector-referenced-id",Values="d4610ac5-e323-4ad9-bc50-eaf7249dfe9d"</code> </p>
            max_records: <p>Sets the maximum number of records returned in the response.</p>
            next_token: <p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_fleet_advisor_collectors_request.DescribeFleetAdvisorCollectorsRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_fleet_advisor_collectors_response.DescribeFleetAdvisorCollectorsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_collectors

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_collectors.async_describe_fleet_advisor_collectors(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_fleet_advisor_collectors_request.DescribeFleetAdvisorCollectorsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_fleet_advisor_collectors(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_fleet_advisor_collectors_response.DescribeFleetAdvisorCollectorsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_fleet_advisor_collectors(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_fleet_advisor_databases(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_fleet_advisor_databases_response.DescribeFleetAdvisorDatabasesResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Returns a list of Fleet Advisor databases in your account.</p>

        Args:
            filters: <p> If you specify any of the following filters, the output includes information for only those databases that meet the filter criteria: </p> <ul> <li> <p> <code>database-id</code> – The ID of the database.</p> </li> <li> <p> <code>database-name</code> – The name of the database.</p> </li> <li> <p> <code>database-engine</code> – The name of the database engine.</p> </li> <li> <p> <code>server-ip-address</code> – The IP address of the database server.</p> </li> <li> <p> <code>database-ip-address</code> – The IP address of the database.</p> </li> <li> <p> <code>collector-name</code> – The name of the associated Fleet Advisor collector.</p> </li> </ul> <p>An example is: <code>describe-fleet-advisor-databases --filter Name="database-id",Values="45"</code> </p>
            max_records: <p>Sets the maximum number of records returned in the response.</p>
            next_token: <p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_fleet_advisor_databases_request.DescribeFleetAdvisorDatabasesRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_fleet_advisor_databases_response.DescribeFleetAdvisorDatabasesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_databases

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_databases.async_describe_fleet_advisor_databases(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_fleet_advisor_databases_request.DescribeFleetAdvisorDatabasesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_fleet_advisor_databases(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_fleet_advisor_databases_response.DescribeFleetAdvisorDatabasesResponse]":
        _token = next_token
        while True:
            _response = await self.describe_fleet_advisor_databases(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_fleet_advisor_lsa_analysis(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_fleet_advisor_lsa_analysis_response.DescribeFleetAdvisorLsaAnalysisResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Provides descriptions of large-scale assessment (LSA) analyses produced by your Fleet Advisor collectors. </p>

        Args:
            max_records: <p>Sets the maximum number of records returned in the response.</p>
            next_token: <p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_fleet_advisor_lsa_analysis_request.DescribeFleetAdvisorLsaAnalysisRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_fleet_advisor_lsa_analysis_response.DescribeFleetAdvisorLsaAnalysisResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_lsa_analysis

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_lsa_analysis.async_describe_fleet_advisor_lsa_analysis(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_fleet_advisor_lsa_analysis_request.DescribeFleetAdvisorLsaAnalysisRequest = {}
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_fleet_advisor_lsa_analysis(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_fleet_advisor_lsa_analysis_response.DescribeFleetAdvisorLsaAnalysisResponse]":
        _token = next_token
        while True:
            _response = await self.describe_fleet_advisor_lsa_analysis(
                config_overrides=config_overrides,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_fleet_advisor_schema_object_summary(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_fleet_advisor_schema_object_summary_response.DescribeFleetAdvisorSchemaObjectSummaryResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Provides descriptions of the schemas discovered by your Fleet Advisor collectors.</p>

        Args:
            filters: <p> If you specify any of the following filters, the output includes information for only those schema objects that meet the filter criteria:</p> <ul> <li> <p> <code>schema-id</code> – The ID of the schema, for example <code>d4610ac5-e323-4ad9-bc50-eaf7249dfe9d</code>.</p> </li> </ul> <p>Example: <code>describe-fleet-advisor-schema-object-summary --filter Name="schema-id",Values="50"</code> </p>
            max_records: <important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Sets the maximum number of records returned in the response.</p>
            next_token: <p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_fleet_advisor_schema_object_summary_request.DescribeFleetAdvisorSchemaObjectSummaryRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_fleet_advisor_schema_object_summary_response.DescribeFleetAdvisorSchemaObjectSummaryResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_schema_object_summary

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_schema_object_summary.async_describe_fleet_advisor_schema_object_summary(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_fleet_advisor_schema_object_summary_request.DescribeFleetAdvisorSchemaObjectSummaryRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_fleet_advisor_schema_object_summary(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_fleet_advisor_schema_object_summary_response.DescribeFleetAdvisorSchemaObjectSummaryResponse]":
        _token = next_token
        while True:
            _response = await self.describe_fleet_advisor_schema_object_summary(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_fleet_advisor_schemas(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_fleet_advisor_schemas_response.DescribeFleetAdvisorSchemasResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Returns a list of schemas detected by Fleet Advisor Collectors in your account.</p>

        Args:
            filters: <p> If you specify any of the following filters, the output includes information for only those schemas that meet the filter criteria:</p> <ul> <li> <p> <code>complexity</code> – The schema's complexity, for example <code>Simple</code>.</p> </li> <li> <p> <code>database-id</code> – The ID of the schema's database.</p> </li> <li> <p> <code>database-ip-address</code> – The IP address of the schema's database.</p> </li> <li> <p> <code>database-name</code> – The name of the schema's database.</p> </li> <li> <p> <code>database-engine</code> – The name of the schema database's engine.</p> </li> <li> <p> <code>original-schema-name</code> – The name of the schema's database's main schema.</p> </li> <li> <p> <code>schema-id</code> – The ID of the schema, for example <code>15</code>.</p> </li> <li> <p> <code>schema-name</code> – The name of the schema.</p> </li> <li> <p> <code>server-ip-address</code> – The IP address of the schema database's server.</p> </li> </ul> <p>An example is: <code>describe-fleet-advisor-schemas --filter Name="schema-id",Values="50"</code> </p>
            max_records: <p>Sets the maximum number of records returned in the response.</p>
            next_token: <p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_fleet_advisor_schemas_request.DescribeFleetAdvisorSchemasRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_fleet_advisor_schemas_response.DescribeFleetAdvisorSchemasResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_schemas

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_fleet_advisor_schemas.async_describe_fleet_advisor_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_fleet_advisor_schemas_request.DescribeFleetAdvisorSchemasRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_fleet_advisor_schemas(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_fleet_advisor_schemas_response.DescribeFleetAdvisorSchemasResponse]":
        _token = next_token
        while True:
            _response = await self.describe_fleet_advisor_schemas(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_instance_profiles(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_instance_profiles_response.DescribeInstanceProfilesResponse":
        """<p>Returns a paginated list of instance profiles for your account in the current region.</p> <p> <b>Required permissions:</b> <code>dms:ListInstanceProfiles</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            filters: <p>The filters to apply to the instance profiles.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>instance-profile-identifier</code> – The instance profile name or ARN.</p> </li> </ul>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe instance profiles with a filter
            The following example retrieves the details of an instance profile identified by its ARN.

            >>> await client.describe_instance_profiles(filters=[{'Name': 'instance-profile-identifier', 'Values': ['arn:aws:dms:us-east-1:111122223333:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_instance_profiles_message.DescribeInstanceProfilesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_instance_profiles_response.DescribeInstanceProfilesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_instance_profiles

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_instance_profiles.async_describe_instance_profiles(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_instance_profiles_message.DescribeInstanceProfilesMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_instance_profiles(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_instance_profiles_response.DescribeInstanceProfilesResponse]":
        _token = marker
        while True:
            _response = await self.describe_instance_profiles(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_metadata_model(
        self,
        selection_rules: "capo_database_migration_service.types.string.String",
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_response.DescribeMetadataModelResponse":
        """<p>Gets detailed information about the specified metadata model, including its definition and corresponding converted objects in the target database if applicable.</p> <p> <b>Required permissions:</b> <code>dms:DescribeMetadataModel</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            selection_rules: <p>A JSON string that identifies the metadata model to retrieve. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts source or target selection rules depending on the <code>Origin</code> parameter. The <code>server-name</code> in the object locator must match the corresponding data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> <li> <p>Exactly one rule is allowed.</p> </li> </ul>
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            origin: <p>Specifies whether to retrieve metadata from the source or target tree. Valid values: SOURCE | TARGET</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve a source table metadata model
            The following example retrieves detailed information about the ExampleTable table in the ExampleSchema schema from the source metadata tree, including its SQL definition and references to the corresponding converted metadata models in the target database.

            >>> await client.describe_metadata_model(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema", "table-name": "ExampleTable"}, "rule-action": "explicit"}]}', origin='SOURCE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_message.DescribeMetadataModelMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_response.DescribeMetadataModelResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model.async_describe_metadata_model(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_message.DescribeMetadataModelMessage = {
            "selection_rules": selection_rules,
            "migration_project_identifier": migration_project_identifier,
            "origin": origin,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_metadata_model_assessments(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_assessments_response.DescribeMetadataModelAssessmentsResponse":
        """<p>Returns a paginated list of metadata model assessment requests for a migration project, initiated by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelAssessment.html">StartMetadataModelAssessment</a>.</p> <p> <b>Required permissions:</b> <code>dms:ListMetadataModelAssessments</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            filters: <p>The filters to apply to the metadata model assessment requests.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>request-id</code> – The request identifier.</p> </li> <li> <p> <code>status</code> – The request status. Valid values: <code>RECEIVED</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>.</p> </li> </ul>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the status of metadata model assessments
            The following example retrieves the status of metadata model assessment operations identified by their request IDs.

            >>> await client.describe_metadata_model_assessments(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', filters=[{'Name': 'request-id', 'Values': ['a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_assessments_message.DescribeMetadataModelAssessmentsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_assessments_response.DescribeMetadataModelAssessmentsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_assessments

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_assessments.async_describe_metadata_model_assessments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_assessments_message.DescribeMetadataModelAssessmentsMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_metadata_model_assessments(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_metadata_model_assessments_response.DescribeMetadataModelAssessmentsResponse]":
        _token = marker
        while True:
            _response = await self.describe_metadata_model_assessments(
                migration_project_identifier,
                config_overrides=config_overrides,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_metadata_model_children(
        self,
        selection_rules: "capo_database_migration_service.types.string.String",
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_children_response.DescribeMetadataModelChildrenResponse":
        """<p>Gets a list of child metadata models for the specified metadata model in the database hierarchy.</p> <p> <b>Required permissions:</b> <code>dms:DescribeMetadataModelChildren</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            selection_rules: <p>A JSON string that identifies the metadata model whose children to retrieve. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts source or target selection rules depending on the <code>Origin</code> parameter. The <code>server-name</code> in the object locator must match the corresponding data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> <li> <p>Exactly one rule is allowed.</p> </li> </ul>
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            origin: <p>Specifies whether to retrieve metadata from the source or target tree. Valid values: SOURCE | TARGET</p>
            marker: <p>Specifies the unique pagination token that indicates where the next page should start. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by MaxRecords.</p>
            max_records: <p>The maximum number of metadata model children to include in the response. If more items exist than the specified MaxRecords value, a marker is included in the response so that the remaining results can be retrieved.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve children of a schema
            The following example retrieves the child metadata models of the ExampleSchema schema from the source metadata tree.

            >>> await client.describe_metadata_model_children(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"}, "rule-action": "explicit"}]}', origin='SOURCE')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_children_message.DescribeMetadataModelChildrenMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_children_response.DescribeMetadataModelChildrenResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_children

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_children.async_describe_metadata_model_children(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_children_message.DescribeMetadataModelChildrenMessage = {
            "selection_rules": selection_rules,
            "migration_project_identifier": migration_project_identifier,
            "origin": origin,
        }
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_metadata_model_children(
        self,
        selection_rules: "capo_database_migration_service.types.string.String",
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.metadata_model_reference.MetadataModelReference]":
        _token = marker
        while True:
            _response = await self.describe_metadata_model_children(
                selection_rules,
                migration_project_identifier,
                origin,
                config_overrides=config_overrides,
                marker=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("metadata_model_children",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_metadata_model_conversions(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_conversions_response.DescribeMetadataModelConversionsResponse":
        """<p>Returns a paginated list of metadata model conversion requests for a migration project, initiated by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelConversion.html">StartMetadataModelConversion</a>.</p> <p>To cancel a queued or in-progress request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelConversion.html">CancelMetadataModelConversion</a>.</p> <p> <b>Required permissions:</b> <code>dms:ListMetadataModelConversions</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            filters: <p>The filters to apply to the metadata model conversion requests.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>request-id</code> – The request identifier.</p> </li> <li> <p> <code>status</code> – The request status. Valid values: <code>RECEIVED</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>, <code>CANCELING</code>, <code>CANCELED</code>.</p> </li> </ul>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the status of metadata model conversions
            The following example retrieves the status of metadata model conversion operations identified by their request IDs.

            >>> await client.describe_metadata_model_conversions(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', filters=[{'Name': 'request-id', 'Values': ['a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_conversions_message.DescribeMetadataModelConversionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_conversions_response.DescribeMetadataModelConversionsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_conversions

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_conversions.async_describe_metadata_model_conversions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_conversions_message.DescribeMetadataModelConversionsMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_metadata_model_conversions(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_metadata_model_conversions_response.DescribeMetadataModelConversionsResponse]":
        _token = marker
        while True:
            _response = await self.describe_metadata_model_conversions(
                migration_project_identifier,
                config_overrides=config_overrides,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_metadata_model_creations(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_creations_response.DescribeMetadataModelCreationsResponse":
        """<p>Returns a paginated list of metadata model creation requests for a migration project, initiated by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelCreation.html">StartMetadataModelCreation</a>.</p> <p>To cancel a queued or in-progress request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelCreation.html">CancelMetadataModelCreation</a>.</p> <p> <b>Required permissions:</b> <code>dms:DescribeMetadataModelCreations</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            filters: <p>The filters to apply to the metadata model creation requests.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>request-id</code> – The request identifier.</p> </li> <li> <p> <code>status</code> – The request status. Valid values: <code>RECEIVED</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>, <code>CANCELING</code>, <code>CANCELED</code>.</p> </li> </ul>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the status of metadata model creations
            The following example retrieves the status of metadata model creation operations identified by their request IDs.

            >>> await client.describe_metadata_model_creations(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', filters=[{'Name': 'request-id', 'Values': ['a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_creations_message.DescribeMetadataModelCreationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_creations_response.DescribeMetadataModelCreationsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_creations

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_creations.async_describe_metadata_model_creations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_creations_message.DescribeMetadataModelCreationsMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_metadata_model_creations(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.schema_conversion_request.SchemaConversionRequest]":
        _token = marker
        while True:
            _response = await self.describe_metadata_model_creations(
                migration_project_identifier,
                config_overrides=config_overrides,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            _page = _resolve_path(_response, ("requests",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_metadata_model_exports_as_script(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_exports_as_script_response.DescribeMetadataModelExportsAsScriptResponse":
        """<p>Returns a paginated list of metadata model export requests for a migration project, initiated by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportAsScript.html">StartMetadataModelExportAsScript</a>.</p> <p> <b>Required permissions:</b> <code>dms:ListMetadataModelExports</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            filters: <p>The filters to apply to the metadata model export requests.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>request-id</code> – The request identifier.</p> </li> <li> <p> <code>status</code> – The request status. Valid values: <code>RECEIVED</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>.</p> </li> </ul>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the status of metadata model exports as script
            The following example retrieves the status of operations that export metadata models as data definition language (DDL) scripts, identified by their request IDs.

            >>> await client.describe_metadata_model_exports_as_script(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', filters=[{'Name': 'request-id', 'Values': ['a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_exports_as_script_message.DescribeMetadataModelExportsAsScriptMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_exports_as_script_response.DescribeMetadataModelExportsAsScriptResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_exports_as_script

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_exports_as_script.async_describe_metadata_model_exports_as_script(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_exports_as_script_message.DescribeMetadataModelExportsAsScriptMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_metadata_model_exports_as_script(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_metadata_model_exports_as_script_response.DescribeMetadataModelExportsAsScriptResponse]":
        _token = marker
        while True:
            _response = await self.describe_metadata_model_exports_as_script(
                migration_project_identifier,
                config_overrides=config_overrides,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_metadata_model_exports_to_target(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_exports_to_target_response.DescribeMetadataModelExportsToTargetResponse":
        """<p>Returns a paginated list of metadata model export requests for a migration project, initiated by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportToTarget.html">StartMetadataModelExportToTarget</a>.</p> <p> <b>Required permissions:</b> <code>dms:ListMetadataModelExports</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            filters: <p>The filters to apply to the metadata model export requests.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>request-id</code> – The request identifier.</p> </li> <li> <p> <code>status</code> – The request status. Valid values: <code>RECEIVED</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>.</p> </li> </ul>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the status of metadata model exports to target
            The following example retrieves the status of operations that export converted metadata models to the target database, identified by their request IDs.

            >>> await client.describe_metadata_model_exports_to_target(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', filters=[{'Name': 'request-id', 'Values': ['a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_exports_to_target_message.DescribeMetadataModelExportsToTargetMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_exports_to_target_response.DescribeMetadataModelExportsToTargetResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_exports_to_target

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_exports_to_target.async_describe_metadata_model_exports_to_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_exports_to_target_message.DescribeMetadataModelExportsToTargetMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_metadata_model_exports_to_target(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_metadata_model_exports_to_target_response.DescribeMetadataModelExportsToTargetResponse]":
        _token = marker
        while True:
            _response = await self.describe_metadata_model_exports_to_target(
                migration_project_identifier,
                config_overrides=config_overrides,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_metadata_model_imports(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_metadata_model_imports_response.DescribeMetadataModelImportsResponse":
        """<p>Returns a paginated list of metadata model import requests for a migration project, initiated by <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html">StartMetadataModelImport</a>.</p> <p> <b>Required permissions:</b> <code>dms:DescribeMetadataModelImports</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            filters: <p>The filters to apply to the metadata model import requests.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>request-id</code> – The request identifier.</p> </li> <li> <p> <code>status</code> – The request status. Valid values: <code>RECEIVED</code>, <code>IN_PROGRESS</code>, <code>SUCCESS</code>, <code>FAILED</code>.</p> </li> </ul>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Retrieve the status of metadata model imports
            The following example retrieves the status of metadata import operations identified by their request IDs.

            >>> await client.describe_metadata_model_imports(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', filters=[{'Name': 'request-id', 'Values': ['a1b2c3d4-5678-90ab-cdef-EXAMPLE11111', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE22222', 'a1b2c3d4-5678-90ab-cdef-EXAMPLE33333']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_metadata_model_imports_message.DescribeMetadataModelImportsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_metadata_model_imports_response.DescribeMetadataModelImportsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_imports

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_metadata_model_imports.async_describe_metadata_model_imports(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_metadata_model_imports_message.DescribeMetadataModelImportsMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_metadata_model_imports(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_metadata_model_imports_response.DescribeMetadataModelImportsResponse]":
        _token = marker
        while True:
            _response = await self.describe_metadata_model_imports(
                migration_project_identifier,
                config_overrides=config_overrides,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_migration_projects(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_migration_projects_response.DescribeMigrationProjectsResponse":
        """<p>Returns a paginated list of migration projects for your account in the current region.</p> <p> <b>Required permissions:</b> <code>dms:ListMigrationProjects</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            filters: <p>The filters to apply to the migration projects.</p> <p>The following filter names are supported:</p> <ul> <li> <p> <code>migration-project-identifier</code> – The migration project name or ARN.</p> </li> <li> <p> <code>instance-profile-identifier</code> – The instance profile name or ARN.</p> </li> <li> <p> <code>data-provider-identifier</code> – The source or target data provider name or ARN.</p> </li> <li> <p> <code>source-data-provider-identifier</code> – The source data provider name or ARN.</p> </li> <li> <p> <code>target-data-provider-identifier</code> – The target data provider name or ARN.</p> </li> </ul>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, DMS includes a pagination token in the response so that you can retrieve the remaining results.</p>
            marker: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>Marker</code> is returned by a previous response, there are more results available. The value of <code>Marker</code> is a unique pagination token for each page. To retrieve the next page, make the call again using the returned token and keeping all other arguments unchanged.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe migration projects with a filter
            The following example retrieves the details of a migration project identified by its ARN.

            >>> await client.describe_migration_projects(filters=[{'Name': 'migration-project-identifier', 'Values': ['arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS']}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_migration_projects_message.DescribeMigrationProjectsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_migration_projects_response.DescribeMigrationProjectsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_migration_projects

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_migration_projects.async_describe_migration_projects(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_migration_projects_message.DescribeMigrationProjectsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_migration_projects(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_migration_projects_response.DescribeMigrationProjectsResponse]":
        _token = marker
        while True:
            _response = await self.describe_migration_projects(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_orderable_replication_instances(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_orderable_replication_instances_response.DescribeOrderableReplicationInstancesResponse":
        """<p>Returns information about the replication instance types that can be created in the specified region.</p>

        Args:
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe orderable replication instances
            Returns information about the replication instance types that can be created in the specified region.

            >>> await client.describe_orderable_replication_instances(max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_orderable_replication_instances_message.DescribeOrderableReplicationInstancesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_orderable_replication_instances_response.DescribeOrderableReplicationInstancesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_orderable_replication_instances

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_orderable_replication_instances.async_describe_orderable_replication_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_orderable_replication_instances_message.DescribeOrderableReplicationInstancesMessage = {}
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_orderable_replication_instances(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_orderable_replication_instances_response.DescribeOrderableReplicationInstancesResponse]":
        _token = marker
        while True:
            _response = await self.describe_orderable_replication_instances(
                config_overrides=config_overrides,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_instance_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_pending_maintenance_actions_response.DescribePendingMaintenanceActionsResponse":
        """<p>Returns a list of upcoming maintenance events for replication instances in your account in the current Region.</p>

        Args:
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance.</p>
            filters: <p></p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_pending_maintenance_actions_message.DescribePendingMaintenanceActionsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_pending_maintenance_actions_response.DescribePendingMaintenanceActionsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_pending_maintenance_actions

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_pending_maintenance_actions.async_describe_pending_maintenance_actions(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_pending_maintenance_actions_message.DescribePendingMaintenanceActionsMessage = {}
        if replication_instance_arn is not None:
            input_["replication_instance_arn"] = replication_instance_arn
        if filters is not None:
            input_["filters"] = filters
        if marker is not None:
            input_["marker"] = marker
        if max_records is not None:
            input_["max_records"] = max_records

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_pending_maintenance_actions(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_instance_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_pending_maintenance_actions_response.DescribePendingMaintenanceActionsResponse]":
        _token = marker
        while True:
            _response = await self.describe_pending_maintenance_actions(
                config_overrides=config_overrides,
                replication_instance_arn=replication_instance_arn,
                filters=filters,
                marker=_token,
                max_records=max_records,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_recommendation_limitations(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_recommendation_limitations_response.DescribeRecommendationLimitationsResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Returns a paginated list of limitations for recommendations of target Amazon Web Services engines.</p>

        Args:
            filters: <p>Filters applied to the limitations described in the form of key-value pairs.</p> <p>Valid filter names: <code>database-id</code> | <code>engine-name</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, Fleet Advisor includes a pagination token in the response so that you can retrieve the remaining results.</p>
            next_token: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_recommendation_limitations_request.DescribeRecommendationLimitationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_recommendation_limitations_response.DescribeRecommendationLimitationsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_recommendation_limitations

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_recommendation_limitations.async_describe_recommendation_limitations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_recommendation_limitations_request.DescribeRecommendationLimitationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_recommendation_limitations(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_recommendation_limitations_response.DescribeRecommendationLimitationsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_recommendation_limitations(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_recommendations_response.DescribeRecommendationsResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Returns a paginated list of target engine recommendations for your source databases.</p>

        Args:
            filters: <p>Filters applied to the target engine recommendations described in the form of key-value pairs.</p> <p>Valid filter names: <code>database-id</code> | <code>engine-name</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, Fleet Advisor includes a pagination token in the response so that you can retrieve the remaining results.</p>
            next_token: <p>Specifies the unique pagination token that makes it possible to display the next page of results. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p> <p>If <code>NextToken</code> is returned by a previous response, there are more results available. The value of <code>NextToken</code> is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_recommendations_request.DescribeRecommendationsRequest]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_recommendations_response.DescribeRecommendationsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_recommendations

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_recommendations.async_describe_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_recommendations_request.DescribeRecommendationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_recommendations(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        next_token: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_recommendations_response.DescribeRecommendationsResponse]":
        _token = next_token
        while True:
            _response = await self.describe_recommendations(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    async def describe_refresh_schemas_status(
        self,
        endpoint_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.describe_refresh_schemas_status_response.DescribeRefreshSchemasStatusResponse":
        """<p>Returns the status of the RefreshSchemas operation.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe refresh schema status
            Returns the status of the refresh-schemas operation.

            >>> await client.describe_refresh_schemas_status(endpoint_arn='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_refresh_schemas_status_message.DescribeRefreshSchemasStatusMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_refresh_schemas_status_response.DescribeRefreshSchemasStatusResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_refresh_schemas_status

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_refresh_schemas_status.async_describe_refresh_schemas_status(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_refresh_schemas_status_message.DescribeRefreshSchemasStatusMessage = {
            "endpoint_arn": endpoint_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def describe_replication_configs(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replication_configs_response.DescribeReplicationConfigsResponse":
        """<p>Returns one or more existing DMS Serverless replication configurations as a list of structures.</p>

        Args:
            filters: <p>Filters applied to the replication configs.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_configs_message.DescribeReplicationConfigsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_configs_response.DescribeReplicationConfigsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_configs

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_configs.async_describe_replication_configs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_configs_message.DescribeReplicationConfigsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_configs(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_configs_response.DescribeReplicationConfigsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_configs(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_instances(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replication_instances_response.DescribeReplicationInstancesResponse":
        """<p>Returns information about replication instances for your account in the current region.</p>

        Args:
            filters: <p>Filters applied to replication instances.</p> <p>Valid filter names: replication-instance-arn | replication-instance-id | replication-instance-class | engine-version</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe replication instances
            Returns the status of the refresh-schemas operation.

            >>> await client.describe_replication_instances(filters=[{'Name': 'string', 'Values': ['string', 'string']}], max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_instances_message.DescribeReplicationInstancesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_instances_response.DescribeReplicationInstancesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_instances

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_instances.async_describe_replication_instances(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_instances_message.DescribeReplicationInstancesMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_instances(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_instances_response.DescribeReplicationInstancesResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_instances(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_instance_task_logs(
        self,
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replication_instance_task_logs_response.DescribeReplicationInstanceTaskLogsResponse":
        """<p>Returns information about the task logs for the specified task.</p>

        Args:
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_instance_task_logs_message.DescribeReplicationInstanceTaskLogsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_instance_task_logs_response.DescribeReplicationInstanceTaskLogsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_instance_task_logs

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_instance_task_logs.async_describe_replication_instance_task_logs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_instance_task_logs_message.DescribeReplicationInstanceTaskLogsMessage = {
            "replication_instance_arn": replication_instance_arn
        }
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_instance_task_logs(
        self,
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_instance_task_logs_response.DescribeReplicationInstanceTaskLogsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_instance_task_logs(
                replication_instance_arn,
                config_overrides=config_overrides,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replications(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replications_response.DescribeReplicationsResponse":
        """<p>Provides details on replication progress by returning status information for one or more provisioned DMS Serverless replications.</p>

        Args:
            filters: <p>Filters applied to the replications.</p> <p> Valid filter names: <code>replication-config-arn</code> | <code>replication-config-id</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replications_message.DescribeReplicationsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replications_response.DescribeReplicationsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replications

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replications.async_describe_replications(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replications_message.DescribeReplicationsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replications(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replications_response.DescribeReplicationsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replications(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replication_subnet_groups_response.DescribeReplicationSubnetGroupsResponse":
        """<p>Returns information about the replication subnet groups.</p>

        Args:
            filters: <p>Filters applied to replication subnet groups.</p> <p>Valid filter names: replication-subnet-group-id</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe replication subnet groups
            Returns information about the replication subnet groups.

            >>> await client.describe_replication_subnet_groups(filters=[{'Name': 'string', 'Values': ['string', 'string']}], max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_subnet_groups_message.DescribeReplicationSubnetGroupsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_subnet_groups_response.DescribeReplicationSubnetGroupsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_subnet_groups

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_subnet_groups.async_describe_replication_subnet_groups(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_subnet_groups_message.DescribeReplicationSubnetGroupsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_subnet_groups(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_subnet_groups_response.DescribeReplicationSubnetGroupsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_subnet_groups(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_table_statistics(
        self,
        replication_config_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_replication_table_statistics_response.DescribeReplicationTableStatisticsResponse":
        """<p>Returns table and schema statistics for one or more provisioned replications that use a given DMS Serverless replication configuration.</p>

        Args:
            replication_config_arn: <p>The replication config to describe.</p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>
            filters: <p>Filters applied to the replication table statistics.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_table_statistics_message.DescribeReplicationTableStatisticsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_table_statistics_response.DescribeReplicationTableStatisticsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_table_statistics

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_table_statistics.async_describe_replication_table_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_table_statistics_message.DescribeReplicationTableStatisticsMessage = {
            "replication_config_arn": replication_config_arn
        }
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_table_statistics(
        self,
        replication_config_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_table_statistics_response.DescribeReplicationTableStatisticsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_table_statistics(
                replication_config_arn,
                config_overrides=config_overrides,
                max_records=max_records,
                marker=_token,
                filters=filters,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_task_assessment_results(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_task_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replication_task_assessment_results_response.DescribeReplicationTaskAssessmentResultsResponse":
        """<p>Returns the task assessment results from the Amazon S3 bucket that DMS creates in your Amazon Web Services account. This action always returns the latest results.</p> <p>For more information about DMS task assessments, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html">Creating a task assessment report</a> in the <i>Database Migration Service User Guide</i>.</p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the task. When this input parameter is specified, the API returns only one result and ignore the values of the <code>MaxRecords</code> and <code>Marker</code> parameters. </p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_task_assessment_results_message.DescribeReplicationTaskAssessmentResultsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_task_assessment_results_response.DescribeReplicationTaskAssessmentResultsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_task_assessment_results

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_task_assessment_results.async_describe_replication_task_assessment_results(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_task_assessment_results_message.DescribeReplicationTaskAssessmentResultsMessage = {}
        if replication_task_arn is not None:
            input_["replication_task_arn"] = replication_task_arn
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_task_assessment_results(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_task_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_task_assessment_results_response.DescribeReplicationTaskAssessmentResultsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_task_assessment_results(
                config_overrides=config_overrides,
                replication_task_arn=replication_task_arn,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_task_assessment_runs(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replication_task_assessment_runs_response.DescribeReplicationTaskAssessmentRunsResponse":
        """<p>Returns a paginated list of premigration assessment runs based on filter settings.</p> <p>These filter settings can specify a combination of premigration assessment runs, migration tasks, replication instances, and assessment run status values.</p> <note> <p>This operation doesn't return information about individual assessments. For this information, see the <code>DescribeReplicationTaskIndividualAssessments</code> operation. </p> </note>

        Args:
            filters: <p>Filters applied to the premigration assessment runs described in the form of key-value pairs.</p> <p>Valid filter names: <code>replication-task-assessment-run-arn</code>, <code>replication-task-arn</code>, <code>replication-instance-arn</code>, <code>status</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_task_assessment_runs_message.DescribeReplicationTaskAssessmentRunsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_task_assessment_runs_response.DescribeReplicationTaskAssessmentRunsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_task_assessment_runs

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_task_assessment_runs.async_describe_replication_task_assessment_runs(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_task_assessment_runs_message.DescribeReplicationTaskAssessmentRunsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_task_assessment_runs(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_task_assessment_runs_response.DescribeReplicationTaskAssessmentRunsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_task_assessment_runs(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_task_individual_assessments(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_replication_task_individual_assessments_response.DescribeReplicationTaskIndividualAssessmentsResponse":
        """<p>Returns a paginated list of individual assessments based on filter settings.</p> <p>These filter settings can specify a combination of premigration assessment runs, migration tasks, and assessment status values.</p>

        Args:
            filters: <p>Filters applied to the individual assessments described in the form of key-value pairs.</p> <p>Valid filter names: <code>replication-task-assessment-run-arn</code>, <code>replication-task-arn</code>, <code>status</code> </p>
            max_records: <p>The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved.</p>
            marker: <p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_task_individual_assessments_message.DescribeReplicationTaskIndividualAssessmentsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_task_individual_assessments_response.DescribeReplicationTaskIndividualAssessmentsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_task_individual_assessments

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_task_individual_assessments.async_describe_replication_task_individual_assessments(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_task_individual_assessments_message.DescribeReplicationTaskIndividualAssessmentsMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_task_individual_assessments(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_task_individual_assessments_response.DescribeReplicationTaskIndividualAssessmentsResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_task_individual_assessments(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_replication_tasks(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        without_settings: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_replication_tasks_response.DescribeReplicationTasksResponse":
        """<p>Returns information about replication tasks for your account in the current region.</p>

        Args:
            filters: <p>Filters applied to replication tasks.</p> <p>Valid filter names: replication-task-arn | replication-task-id | migration-type | endpoint-arn | replication-instance-arn</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>
            without_settings: <p>An option to set to avoid returning information about settings. Use this to reduce overhead when setting information is too large. To use this option, choose <code>true</code>; otherwise, choose <code>false</code> (the default).</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe replication tasks
            Returns information about replication tasks for your account in the current region.

            >>> await client.describe_replication_tasks(filters=[{'Name': 'string', 'Values': ['string', 'string']}], max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_replication_tasks_message.DescribeReplicationTasksMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_replication_tasks_response.DescribeReplicationTasksResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_tasks

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_replication_tasks.async_describe_replication_tasks(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_replication_tasks_message.DescribeReplicationTasksMessage = {}
        if filters is not None:
            input_["filters"] = filters
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if without_settings is not None:
            input_["without_settings"] = without_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_replication_tasks(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        without_settings: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_replication_tasks_response.DescribeReplicationTasksResponse]":
        _token = marker
        while True:
            _response = await self.describe_replication_tasks(
                config_overrides=config_overrides,
                filters=filters,
                max_records=max_records,
                marker=_token,
                without_settings=without_settings,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_schemas(
        self,
        endpoint_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "capo_database_migration_service.types.describe_schemas_response.DescribeSchemasResponse":
        """<p>Returns information about the schema for the specified endpoint.</p> <p></p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 100.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe schemas
            Returns information about the schema for the specified endpoint.

            >>> await client.describe_schemas(endpoint_arn='', max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_schemas_message.DescribeSchemasMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_schemas_response.DescribeSchemasResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_schemas

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_schemas.async_describe_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_schemas_message.DescribeSchemasMessage = {
            "endpoint_arn": endpoint_arn
        }
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_schemas(
        self,
        endpoint_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_schemas_response.DescribeSchemasResponse]":
        _token = marker
        while True:
            _response = await self.describe_schemas(
                endpoint_arn,
                config_overrides=config_overrides,
                max_records=max_records,
                marker=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def describe_table_statistics(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
    ) -> "capo_database_migration_service.types.describe_table_statistics_response.DescribeTableStatisticsResponse":
        """<p>Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.</p> <p>Note that the "last updated" column the DMS console only indicates the time that DMS last updated the table statistics record for a table. It does not indicate the time of the last update to the table.</p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name (ARN) of the replication task.</p>
            max_records: <p> The maximum number of records to include in the response. If more records exist than the specified <code>MaxRecords</code> value, a pagination token called a marker is included in the response so that the remaining results can be retrieved. </p> <p>Default: 100</p> <p>Constraints: Minimum 20, maximum 500.</p>
            marker: <p> An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>. </p>
            filters: <p>Filters applied to table statistics.</p> <p>Valid filter names: schema-name | table-name | table-state</p> <p>A combination of filters creates an AND condition where each record matches all specified filters.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Describe table statistics
            Returns table statistics on the database migration task, including table name, rows inserted, rows updated, and rows deleted.

            >>> await client.describe_table_statistics(replication_task_arn='', max_records=123, marker='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.describe_table_statistics_message.DescribeTableStatisticsMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.describe_table_statistics_response.DescribeTableStatisticsResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.describe_table_statistics

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.describe_table_statistics.async_describe_table_statistics(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.describe_table_statistics_message.DescribeTableStatisticsMessage = {
            "replication_task_arn": replication_task_arn
        }
        if max_records is not None:
            input_["max_records"] = max_records
        if marker is not None:
            input_["marker"] = marker
        if filters is not None:
            input_["filters"] = filters

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def iter_describe_table_statistics(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        max_records: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        marker: Optional["capo_database_migration_service.types.string.String"] = None,
        filters: Optional[
            "capo_database_migration_service.types.filter_list.FilterList"
        ] = None,
    ) -> "AsyncIterator[capo_database_migration_service.types.describe_table_statistics_response.DescribeTableStatisticsResponse]":
        _token = marker
        while True:
            _response = await self.describe_table_statistics(
                replication_task_arn,
                config_overrides=config_overrides,
                max_records=max_records,
                marker=_token,
                filters=filters,
            )
            yield _response
            _token = _resolve_path(_response, ("marker",))
            if not _token:
                break

    async def export_metadata_model_assessment(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        file_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        assessment_report_types: Optional[
            "capo_database_migration_service.types.assessment_report_types_list.AssessmentReportTypesList"
        ] = None,
    ) -> "capo_database_migration_service.types.export_metadata_model_assessment_response.ExportMetadataModelAssessmentResponse":
        """<p>Saves a copy of a database migration assessment report to your Amazon S3 bucket. DMS can save your assessment report as a comma-separated value (CSV) or a PDF file. </p> <p> <b>Required permissions:</b> <code>dms:ExportMetadataModelAssessment</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that identifies the metadata models to export a conversion assessment report for. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> </ul>
            file_name: <p>The name of the assessment file to create in your Amazon S3 bucket.</p>
            assessment_report_types: <p>The file format of the assessment file.</p>

        Raises:
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Export a conversion assessment report
            The following example exports a conversion assessment report for all objects in the ExampleSchema schema.

            >>> await client.export_metadata_model_assessment(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"}, "rule-action": "explicit"}]}', file_name='example-assessment-report', assessment_report_types=['pdf', 'csv'])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.export_metadata_model_assessment_message.ExportMetadataModelAssessmentMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.export_metadata_model_assessment_response.ExportMetadataModelAssessmentResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.export_metadata_model_assessment

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.export_metadata_model_assessment.async_export_metadata_model_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.export_metadata_model_assessment_message.ExportMetadataModelAssessmentMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
        }
        if file_name is not None:
            input_["file_name"] = file_name
        if assessment_report_types is not None:
            input_["assessment_report_types"] = assessment_report_types

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def get_target_selection_rules(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.get_target_selection_rules_response.GetTargetSelectionRulesResponse":
        """<p>Converts source selection rules into their target counterparts for schema conversion operations.</p> <p> <b>Required permissions:</b> <code>dms:GetTargetSelectionRules</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that contains the source selection rules to convert into their target counterparts. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> <li> <p>Does not support <code>category-name</code> in the object locator.</p> </li> <li> <p>Up to 10 rules are allowed.</p> </li> </ul>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Convert source selection rules to target selection rules
            The following example converts source selection rules that select the ExampleTable table in the ExampleSchema schema into target selection rules that reference its converted counterpart.

            >>> await client.get_target_selection_rules(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "database-name": "ExampleDatabase", "schema-name": "ExampleSchema", "table-name": "ExampleTable"}, "rule-action": "explicit"}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.get_target_selection_rules_message.GetTargetSelectionRulesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.get_target_selection_rules_response.GetTargetSelectionRulesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.get_target_selection_rules

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.get_target_selection_rules.async_get_target_selection_rules(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.get_target_selection_rules_message.GetTargetSelectionRulesMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def import_certificate(
        self,
        certificate_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        certificate_pem: Optional[
            "capo_database_migration_service.types.secret_string.SecretString"
        ] = None,
        certificate_wallet: Optional[
            "capo_database_migration_service.types.certificate_wallet.CertificateWallet"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
        kms_key_id: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.import_certificate_response.ImportCertificateResponse":
        """<p>Uploads the specified certificate.</p>

        Args:
            certificate_identifier: <p>A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.</p>
            certificate_pem: <p>The contents of a <code>.pem</code> file, which contains an X.509 certificate.</p>
            certificate_wallet: <p>The location of an imported Oracle Wallet certificate for use with SSL. Provide the name of a <code>.sso</code> file using the <code>fileb://</code> prefix. You can't provide the certificate inline.</p> <p>Example: <code>filebase64("${path.root}/rds-ca-2019-root.sso")</code> </p>
            tags: <p>The tags associated with the certificate.</p>
            kms_key_id: <p>An KMS key identifier that is used to encrypt the certificate.</p> <p>If you don't specify a value for the <code>KmsKeyId</code> parameter, then DMS uses your default encryption key.</p> <p>KMS creates the default encryption key for your Amazon Web Services account. Your Amazon Web Services account has a different default encryption key for each Amazon Web Services Region.</p>

        Raises:
            capo_database_migration_service.errors.invalid_certificate_fault.InvalidCertificateFault: <p>The certificate was not valid.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Import certificate
            Uploads the specified certificate.

            >>> await client.import_certificate(certificate_identifier='', certificate_pem='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.import_certificate_message.ImportCertificateMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.import_certificate_response.ImportCertificateResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.import_certificate

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.import_certificate.async_import_certificate(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.import_certificate_message.ImportCertificateMessage = {
            "certificate_identifier": certificate_identifier
        }
        if certificate_pem is not None:
            input_["certificate_pem"] = certificate_pem
        if certificate_wallet is not None:
            input_["certificate_wallet"] = certificate_wallet
        if tags is not None:
            input_["tags"] = tags
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def list_tags_for_resource(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        resource_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        resource_arn_list: Optional[
            "capo_database_migration_service.types.arn_list.ArnList"
        ] = None,
    ) -> "capo_database_migration_service.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists all metadata tags attached to an DMS resource, including replication instance, endpoint, subnet group, and migration task. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html"> <code>Tag</code> </a> data type description.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the DMS resource to list tags for. This returns a list of keys (names of tags) created for the resource and their associated tag values.</p>
            resource_arn_list: <p>List of ARNs that identify multiple DMS resources that you want to list tags for. This returns a list of keys (tag names) and their associated tag values. It also returns each tag's associated <code>ResourceArn</code> value, which is the ARN of the resource for which each listed tag is created. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List tags for resource
            Lists all tags for an AWS DMS resource.

            >>> await client.list_tags_for_resource(resource_arn='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.list_tags_for_resource_message.ListTagsForResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.list_tags_for_resource

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.list_tags_for_resource.async_list_tags_for_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.list_tags_for_resource_message.ListTagsForResourceMessage = {}
        if resource_arn is not None:
            input_["resource_arn"] = resource_arn
        if resource_arn_list is not None:
            input_["resource_arn_list"] = resource_arn_list

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_conversion_configuration(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        conversion_configuration: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.modify_conversion_configuration_response.ModifyConversionConfigurationResponse":
        """<p>Modifies the specified schema conversion configuration using the provided parameters. </p> <p> <b>Required permissions:</b> <code>dms:UpdateConversionConfiguration</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            conversion_configuration: <p>A JSON string that contains the schema conversion settings to update. For the format and available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/schema-conversion-settings.html">Specifying schema conversion settings for migration projects</a>.</p> <p>Usage:</p> <ul> <li> <p>Include only the sections and keys to change. The operation merges supplied values with the existing configuration.</p> </li> </ul>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Modifying conversion configuration for a migration project
            The following example enables generative AI assisted conversion and updates a conversion pair setting for a migration project.

            >>> await client.modify_conversion_configuration(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', conversion_configuration='{"Common project settings":{"EnableGenAiConversion":true},"MSSQL_TO_AURORA_POSTGRESQL":{"ConvertProceduresToFunction":false}}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_conversion_configuration_message.ModifyConversionConfigurationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_conversion_configuration_response.ModifyConversionConfigurationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_conversion_configuration

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_conversion_configuration.async_modify_conversion_configuration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_conversion_configuration_message.ModifyConversionConfigurationMessage = {
            "migration_project_identifier": migration_project_identifier,
            "conversion_configuration": conversion_configuration,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_data_migration(
        self,
        data_migration_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        data_migration_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        enable_cloudwatch_logs: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        service_access_role_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        data_migration_type: Optional[
            "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
        ] = None,
        source_data_settings: Optional[
            "capo_database_migration_service.types.source_data_settings.SourceDataSettings"
        ] = None,
        target_data_settings: Optional[
            "capo_database_migration_service.types.target_data_settings.TargetDataSettings"
        ] = None,
        number_of_jobs: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        selection_rules: Optional[
            "capo_database_migration_service.types.secret_string.SecretString"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_data_migration_response.ModifyDataMigrationResponse":
        """<p>Modifies an existing DMS data migration.</p>

        Args:
            data_migration_identifier: <p>The identifier (name or ARN) of the data migration to modify.</p>
            data_migration_name: <p>The new name for the data migration.</p>
            enable_cloudwatch_logs: <p>Whether to enable Cloudwatch logs for the data migration.</p>
            service_access_role_arn: <p>The new service access role ARN for the data migration.</p>
            data_migration_type: <p>The new migration type for the data migration.</p>
            source_data_settings: <p>The new information about the source data provider for the data migration.</p>
            target_data_settings: <p>The new information about the target data provider for the data migration.</p>
            number_of_jobs: <p>The number of parallel jobs that trigger parallel threads to unload the tables from the source, and then load them to the target.</p>
            selection_rules: <p>A JSON-formatted string that defines what objects to include and exclude from the migration.</p>

        Raises:
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_data_migration_message.ModifyDataMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_data_migration_response.ModifyDataMigrationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_data_migration

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_data_migration.async_modify_data_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_data_migration_message.ModifyDataMigrationMessage = {
            "data_migration_identifier": data_migration_identifier
        }
        if data_migration_name is not None:
            input_["data_migration_name"] = data_migration_name
        if enable_cloudwatch_logs is not None:
            input_["enable_cloudwatch_logs"] = enable_cloudwatch_logs
        if service_access_role_arn is not None:
            input_["service_access_role_arn"] = service_access_role_arn
        if data_migration_type is not None:
            input_["data_migration_type"] = data_migration_type
        if source_data_settings is not None:
            input_["source_data_settings"] = source_data_settings
        if target_data_settings is not None:
            input_["target_data_settings"] = target_data_settings
        if number_of_jobs is not None:
            input_["number_of_jobs"] = number_of_jobs
        if selection_rules is not None:
            input_["selection_rules"] = selection_rules

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_data_provider(
        self,
        data_provider_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        data_provider_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        engine: Optional["capo_database_migration_service.types.string.String"] = None,
        virtual: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        exact_settings: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        settings: Optional[
            "capo_database_migration_service.types.data_provider_settings.DataProviderSettings"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_data_provider_response.ModifyDataProviderResponse":
        """<p>Modifies the specified data provider using the provided settings.</p> <p> <b>Required permissions:</b> <code>dms:UpdateDataProvider</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p> <note> <p>You must remove the data provider from all migration projects before you can modify it.</p> </note>

        Args:
            data_provider_identifier: <p>The identifier of the data provider. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>
            data_provider_name: <p>The name of the data provider.</p>
            description: <p>A user-friendly description of the data provider.</p>
            engine: <p>The type of database engine for the data provider.</p> <p>Valid values: <code>aurora</code>, <code>aurora-postgresql</code>, <code>db2</code>, <code>db2-zos</code>, <code>docdb</code>, <code>mariadb</code>, <code>mongodb</code>, <code>mysql</code>, <code>oracle</code>, <code>postgres</code>, <code>redshift</code>, <code>sqlserver</code>, and <code>sybase</code>. A value of <code>aurora</code> represents Amazon Aurora MySQL-Compatible Edition.</p>
            virtual: <p>Indicates whether the data provider is virtual.</p>
            exact_settings: <p>If this attribute is Y, the current call to <code>ModifyDataProvider</code> replaces all existing data provider settings with the exact settings that you specify in this call. If this attribute is N, the current call to <code>ModifyDataProvider</code> does two things: </p> <ul> <li> <p>It replaces any data provider settings that already exist with new values, for settings with the same names.</p> </li> <li> <p>It creates new data provider settings that you specify in the call, for settings with different names. </p> </li> </ul>
            settings: <p>The settings in JSON format for a data provider.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Modify a data provider
            The following example updates the description and server name of a data provider.

            >>> await client.modify_data_provider(data_provider_identifier='arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS', description='Updated data provider description', engine='sqlserver', settings={'MicrosoftSqlServerSettings': {'ServerName': 'new-source-server.us-east-1.rds.amazonaws.com'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_data_provider_message.ModifyDataProviderMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_data_provider_response.ModifyDataProviderResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_data_provider

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_data_provider.async_modify_data_provider(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_data_provider_message.ModifyDataProviderMessage = {
            "data_provider_identifier": data_provider_identifier
        }
        if data_provider_name is not None:
            input_["data_provider_name"] = data_provider_name
        if description is not None:
            input_["description"] = description
        if engine is not None:
            input_["engine"] = engine
        if virtual is not None:
            input_["virtual"] = virtual
        if exact_settings is not None:
            input_["exact_settings"] = exact_settings
        if settings is not None:
            input_["settings"] = settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_endpoint(
        self,
        endpoint_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        endpoint_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        endpoint_type: Optional[
            "capo_database_migration_service.types.replication_endpoint_type_value.ReplicationEndpointTypeValue"
        ] = None,
        engine_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        username: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        password: Optional[
            "capo_database_migration_service.types.secret_string.SecretString"
        ] = None,
        server_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        port: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        database_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        extra_connection_attributes: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        certificate_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        ssl_mode: Optional[
            "capo_database_migration_service.types.dms_ssl_mode_value.DmsSslModeValue"
        ] = None,
        service_access_role_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        external_table_definition: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        dynamo_db_settings: Optional[
            "capo_database_migration_service.types.dynamo_db_settings.DynamoDbSettings"
        ] = None,
        s3_settings: Optional[
            "capo_database_migration_service.types.s3_settings.S3Settings"
        ] = None,
        dms_transfer_settings: Optional[
            "capo_database_migration_service.types.dms_transfer_settings.DmsTransferSettings"
        ] = None,
        mongo_db_settings: Optional[
            "capo_database_migration_service.types.mongo_db_settings.MongoDbSettings"
        ] = None,
        kinesis_settings: Optional[
            "capo_database_migration_service.types.kinesis_settings.KinesisSettings"
        ] = None,
        kafka_settings: Optional[
            "capo_database_migration_service.types.kafka_settings.KafkaSettings"
        ] = None,
        elasticsearch_settings: Optional[
            "capo_database_migration_service.types.elasticsearch_settings.ElasticsearchSettings"
        ] = None,
        neptune_settings: Optional[
            "capo_database_migration_service.types.neptune_settings.NeptuneSettings"
        ] = None,
        redshift_settings: Optional[
            "capo_database_migration_service.types.redshift_settings.RedshiftSettings"
        ] = None,
        postgre_sql_settings: Optional[
            "capo_database_migration_service.types.postgre_sql_settings.PostgreSQLSettings"
        ] = None,
        my_sql_settings: Optional[
            "capo_database_migration_service.types.my_sql_settings.MySQLSettings"
        ] = None,
        oracle_settings: Optional[
            "capo_database_migration_service.types.oracle_settings.OracleSettings"
        ] = None,
        sybase_settings: Optional[
            "capo_database_migration_service.types.sybase_settings.SybaseSettings"
        ] = None,
        microsoft_sql_server_settings: Optional[
            "capo_database_migration_service.types.microsoft_sql_server_settings.MicrosoftSQLServerSettings"
        ] = None,
        ibm_db2_settings: Optional[
            "capo_database_migration_service.types.ibm_db2_settings.IBMDb2Settings"
        ] = None,
        doc_db_settings: Optional[
            "capo_database_migration_service.types.doc_db_settings.DocDbSettings"
        ] = None,
        redis_settings: Optional[
            "capo_database_migration_service.types.redis_settings.RedisSettings"
        ] = None,
        exact_settings: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        gcp_my_sql_settings: Optional[
            "capo_database_migration_service.types.gcp_my_sql_settings.GcpMySQLSettings"
        ] = None,
        timestream_settings: Optional[
            "capo_database_migration_service.types.timestream_settings.TimestreamSettings"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_endpoint_response.ModifyEndpointResponse":
        """<p>Modifies the specified endpoint.</p> <note> <p>For a MySQL source or target endpoint, don't explicitly specify the database using the <code>DatabaseName</code> request parameter on the <code>ModifyEndpoint</code> API call. Specifying <code>DatabaseName</code> when you modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the DMS task.</p> </note>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>
            endpoint_identifier: <p>The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.</p>
            endpoint_type: <p>The type of endpoint. Valid values are <code>source</code> and <code>target</code>.</p>
            engine_name: <p>The database engine name. Valid values, depending on the EndpointType, include <code>"mysql"</code>, <code>"oracle"</code>, <code>"postgres"</code>, <code>"mariadb"</code>, <code>"aurora"</code>, <code>"aurora-postgresql"</code>, <code>"redshift"</code>, <code>"s3"</code>, <code>"db2"</code>, <code>"db2-zos"</code>, <code>"azuredb"</code>, <code>"sybase"</code>, <code>"dynamodb"</code>, <code>"mongodb"</code>, <code>"kinesis"</code>, <code>"kafka"</code>, <code>"elasticsearch"</code>, <code>"documentdb"</code>, <code>"sqlserver"</code>, <code>"neptune"</code>, and <code>"babelfish"</code>.</p>
            username: <p>The user name to be used to login to the endpoint database.</p>
            password: <p>The password to be used to login to the endpoint database.</p>
            server_name: <p>The name of the server where the endpoint database resides.</p>
            port: <p>The port used by the endpoint database.</p>
            database_name: <p>The name of the endpoint database. For a MySQL source or target endpoint, do not specify DatabaseName.</p>
            extra_connection_attributes: <p>Additional attributes associated with the connection. To reset this parameter, pass the empty string ("") as an argument.</p>
            certificate_arn: <p>The Amazon Resource Name (ARN) of the certificate used for SSL connection.</p>
            ssl_mode: <p>The SSL mode used to connect to the endpoint. The default value is <code>none</code>.</p>
            service_access_role_arn: <p> The Amazon Resource Name (ARN) for the IAM role you want to use to modify the endpoint. The role must allow the <code>iam:PassRole</code> action.</p>
            external_table_definition: <p>The external table definition.</p>
            dynamo_db_settings: <p>Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping">Using Object Mapping to Migrate Data to DynamoDB</a> in the <i>Database Migration Service User Guide.</i> </p>
            s3_settings: <p>Settings in JSON format for the target Amazon S3 endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring">Extra Connection Attributes When Using Amazon S3 as a Target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            dms_transfer_settings: <p>The settings in JSON format for the DMS transfer type of source endpoint. </p> <p>Attributes include the following:</p> <ul> <li> <p>serviceAccessRoleArn - The Amazon Resource Name (ARN) used by the service access IAM role. The role must allow the <code>iam:PassRole</code> action.</p> </li> <li> <p>BucketName - The name of the S3 bucket to use.</p> </li> </ul> <p>Shorthand syntax for these settings is as follows: <code>ServiceAccessRoleArn=string ,BucketName=string</code> </p> <p>JSON syntax for these settings is as follows: <code>{ "ServiceAccessRoleArn": "string", "BucketName": "string"} </code> </p>
            mongo_db_settings: <p>Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see the configuration properties section in <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration">Endpoint configuration settings when using MongoDB as a source for Database Migration Service</a> in the <i>Database Migration Service User Guide.</i> </p>
            kinesis_settings: <p>Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping">Using object mapping to migrate data to a Kinesis data stream</a> in the <i>Database Migration Service User Guide.</i> </p>
            kafka_settings: <p>Settings in JSON format for the target Apache Kafka endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping">Using object mapping to migrate data to a Kafka topic</a> in the <i>Database Migration Service User Guide.</i> </p>
            elasticsearch_settings: <p>Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration">Extra Connection Attributes When Using OpenSearch as a Target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            neptune_settings: <p>Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings">Specifying graph-mapping rules using Gremlin and R2RML for Amazon Neptune as a target</a> in the <i>Database Migration Service User Guide.</i> </p>
            postgre_sql_settings: <p>Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib">Extra connection attributes when using PostgreSQL as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib"> Extra connection attributes when using PostgreSQL as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            my_sql_settings: <p>Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib">Extra connection attributes when using MySQL as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib">Extra connection attributes when using a MySQL-compatible database as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            oracle_settings: <p>Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib">Extra connection attributes when using Oracle as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib"> Extra connection attributes when using Oracle as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            sybase_settings: <p>Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib">Extra connection attributes when using SAP ASE as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib">Extra connection attributes when using SAP ASE as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            microsoft_sql_server_settings: <p>Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib">Extra connection attributes when using SQL Server as a source for DMS</a> and <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib"> Extra connection attributes when using SQL Server as a target for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            ibm_db2_settings: <p>Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib">Extra connection attributes when using Db2 LUW as a source for DMS</a> in the <i>Database Migration Service User Guide.</i> </p>
            doc_db_settings: <p>Settings in JSON format for the source DocumentDB endpoint. For more information about the available settings, see the configuration properties section in <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html"> Using DocumentDB as a Target for Database Migration Service </a> in the <i>Database Migration Service User Guide.</i> </p>
            redis_settings: <p>Settings in JSON format for the Redis target endpoint.</p>
            exact_settings: <p>If this attribute is Y, the current call to <code>ModifyEndpoint</code> replaces all existing endpoint settings with the exact settings that you specify in this call. If this attribute is N, the current call to <code>ModifyEndpoint</code> does two things: </p> <ul> <li> <p>It replaces any endpoint settings that already exist with new values, for settings with the same names.</p> </li> <li> <p>It creates new endpoint settings that you specify in the call, for settings with different names. </p> </li> </ul> <p>For example, if you call <code>create-endpoint ... --endpoint-settings '{"a":1}' ...</code>, the endpoint has the following endpoint settings: <code>'{"a":1}'</code>. If you then call <code>modify-endpoint ... --endpoint-settings '{"b":2}' ...</code> for the same endpoint, the endpoint has the following settings: <code>'{"a":1,"b":2}'</code>. </p> <p>However, suppose that you follow this with a call to <code>modify-endpoint ... --endpoint-settings '{"b":2}' --exact-settings ...</code> for that same endpoint again. Then the endpoint has the following settings: <code>'{"b":2}'</code>. All existing settings are replaced with the exact settings that you specify. </p>
            gcp_my_sql_settings: <p>Settings in JSON format for the source GCP MySQL endpoint.</p>
            timestream_settings: <p>Settings in JSON format for the target Amazon Timestream endpoint.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Modify endpoint
            Modifies the specified endpoint.

            >>> await client.modify_endpoint(endpoint_arn='', endpoint_identifier='', endpoint_type='source', engine_name='', username='', password='', server_name='', port=123, database_name='', extra_connection_attributes='', certificate_arn='', ssl_mode='require')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_endpoint_message.ModifyEndpointMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_endpoint_response.ModifyEndpointResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_endpoint

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_endpoint.async_modify_endpoint(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_endpoint_message.ModifyEndpointMessage = {
            "endpoint_arn": endpoint_arn
        }
        if endpoint_identifier is not None:
            input_["endpoint_identifier"] = endpoint_identifier
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if engine_name is not None:
            input_["engine_name"] = engine_name
        if username is not None:
            input_["username"] = username
        if password is not None:
            input_["password"] = password
        if server_name is not None:
            input_["server_name"] = server_name
        if port is not None:
            input_["port"] = port
        if database_name is not None:
            input_["database_name"] = database_name
        if extra_connection_attributes is not None:
            input_["extra_connection_attributes"] = extra_connection_attributes
        if certificate_arn is not None:
            input_["certificate_arn"] = certificate_arn
        if ssl_mode is not None:
            input_["ssl_mode"] = ssl_mode
        if service_access_role_arn is not None:
            input_["service_access_role_arn"] = service_access_role_arn
        if external_table_definition is not None:
            input_["external_table_definition"] = external_table_definition
        if dynamo_db_settings is not None:
            input_["dynamo_db_settings"] = dynamo_db_settings
        if s3_settings is not None:
            input_["s3_settings"] = s3_settings
        if dms_transfer_settings is not None:
            input_["dms_transfer_settings"] = dms_transfer_settings
        if mongo_db_settings is not None:
            input_["mongo_db_settings"] = mongo_db_settings
        if kinesis_settings is not None:
            input_["kinesis_settings"] = kinesis_settings
        if kafka_settings is not None:
            input_["kafka_settings"] = kafka_settings
        if elasticsearch_settings is not None:
            input_["elasticsearch_settings"] = elasticsearch_settings
        if neptune_settings is not None:
            input_["neptune_settings"] = neptune_settings
        if redshift_settings is not None:
            input_["redshift_settings"] = redshift_settings
        if postgre_sql_settings is not None:
            input_["postgre_sql_settings"] = postgre_sql_settings
        if my_sql_settings is not None:
            input_["my_sql_settings"] = my_sql_settings
        if oracle_settings is not None:
            input_["oracle_settings"] = oracle_settings
        if sybase_settings is not None:
            input_["sybase_settings"] = sybase_settings
        if microsoft_sql_server_settings is not None:
            input_["microsoft_sql_server_settings"] = microsoft_sql_server_settings
        if ibm_db2_settings is not None:
            input_["ibm_db2_settings"] = ibm_db2_settings
        if doc_db_settings is not None:
            input_["doc_db_settings"] = doc_db_settings
        if redis_settings is not None:
            input_["redis_settings"] = redis_settings
        if exact_settings is not None:
            input_["exact_settings"] = exact_settings
        if gcp_my_sql_settings is not None:
            input_["gcp_my_sql_settings"] = gcp_my_sql_settings
        if timestream_settings is not None:
            input_["timestream_settings"] = timestream_settings

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_event_subscription(
        self,
        subscription_name: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        sns_topic_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        source_type: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        event_categories: Optional[
            "capo_database_migration_service.types.event_categories_list.EventCategoriesList"
        ] = None,
        enabled: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_event_subscription_response.ModifyEventSubscriptionResponse":
        """<p>Modifies an existing DMS event notification subscription. </p>

        Args:
            subscription_name: <p>The name of the DMS event notification subscription to be modified.</p>
            sns_topic_arn: <p> The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.</p>
            source_type: <p> The type of DMS resource that generates the events you want to subscribe to. </p> <p>Valid values: replication-instance | replication-task</p>
            event_categories: <p> A list of event categories for a source type that you want to subscribe to. Use the <code>DescribeEventCategories</code> action to see a list of event categories. </p>
            enabled: <p> A Boolean value; set to <b>true</b> to activate the subscription. </p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.kms_access_denied_fault.KMSAccessDeniedFault: <p>The ciphertext references a key that doesn't exist or that the DMS account doesn't have access to.</p>
            capo_database_migration_service.errors.kms_disabled_fault.KMSDisabledFault: <p>The specified KMS key isn't enabled.</p>
            capo_database_migration_service.errors.kms_invalid_state_fault.KMSInvalidStateFault: <p>The state of the specified KMS resource isn't valid for this request.</p>
            capo_database_migration_service.errors.kms_not_found_fault.KMSNotFoundFault: <p>The specified KMS entity or resource can't be found.</p>
            capo_database_migration_service.errors.kms_throttling_fault.KMSThrottlingFault: <p>This request triggered KMS request throttling.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.sns_invalid_topic_fault.SNSInvalidTopicFault: <p>The SNS topic is invalid.</p>
            capo_database_migration_service.errors.sns_no_authorization_fault.SNSNoAuthorizationFault: <p>You are not authorized for the SNS subscription.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_event_subscription_message.ModifyEventSubscriptionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_event_subscription_response.ModifyEventSubscriptionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_event_subscription

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_event_subscription.async_modify_event_subscription(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_event_subscription_message.ModifyEventSubscriptionMessage = {
            "subscription_name": subscription_name
        }
        if sns_topic_arn is not None:
            input_["sns_topic_arn"] = sns_topic_arn
        if source_type is not None:
            input_["source_type"] = source_type
        if event_categories is not None:
            input_["event_categories"] = event_categories
        if enabled is not None:
            input_["enabled"] = enabled

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_instance_profile(
        self,
        instance_profile_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        availability_zone: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        kms_key_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        publicly_accessible: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        network_type: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        instance_profile_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        subnet_group_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        vpc_security_groups: Optional[
            "capo_database_migration_service.types.string_list.StringList"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_instance_profile_response.ModifyInstanceProfileResponse":
        """<p>Modifies the specified instance profile using the provided parameters.</p> <p> <b>Required permissions:</b> <code>dms:UpdateInstanceProfile</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p> <note> <p>All migration projects associated with the instance profile must be deleted or modified before you can modify the instance profile.</p> </note>

        Args:
            instance_profile_identifier: <p>The identifier of the instance profile. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>
            availability_zone: <p>The Availability Zone where the instance profile runs.</p>
            kms_key_arn: <p>The Amazon Resource Name (ARN) of the KMS key that is used to encrypt the connection parameters for the instance profile.</p> <p>If you don't specify a value for the <code>KmsKeyArn</code> parameter, then DMS uses an Amazon Web Services owned encryption key to encrypt your resources.</p>
            publicly_accessible: <p>Specifies the accessibility options for the instance profile. A value of <code>true</code> represents an instance profile with a public IP address. A value of <code>false</code> represents an instance profile with a private IP address. The default value is <code>true</code>.</p>
            network_type: <p>Specifies the network type for the instance profile. A value of <code>IPV4</code> represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of <code>IPV6</code> represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of <code>DUAL</code> represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.</p>
            instance_profile_name: <p>A user-friendly name for the instance profile.</p>
            description: <p>A user-friendly description for the instance profile.</p>
            subnet_group_identifier: <p>A subnet group to associate with the instance profile.</p>
            vpc_security_groups: <p>Specifies the VPC security groups to be used with the instance profile. The VPC security group must work with the VPC containing the instance profile.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Modify an instance profile
            The following example updates the description and network type of an instance profile.

            >>> await client.modify_instance_profile(instance_profile_identifier='arn:aws:dms:us-east-1:111122223333:instance-profile:EXAMPLEABCDEFGHIJKLMNOPQRS', description='Updated instance profile description', network_type='DUAL')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_instance_profile_message.ModifyInstanceProfileMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_instance_profile_response.ModifyInstanceProfileResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_instance_profile

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_instance_profile.async_modify_instance_profile(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_instance_profile_message.ModifyInstanceProfileMessage = {
            "instance_profile_identifier": instance_profile_identifier
        }
        if availability_zone is not None:
            input_["availability_zone"] = availability_zone
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if publicly_accessible is not None:
            input_["publicly_accessible"] = publicly_accessible
        if network_type is not None:
            input_["network_type"] = network_type
        if instance_profile_name is not None:
            input_["instance_profile_name"] = instance_profile_name
        if description is not None:
            input_["description"] = description
        if subnet_group_identifier is not None:
            input_["subnet_group_identifier"] = subnet_group_identifier
        if vpc_security_groups is not None:
            input_["vpc_security_groups"] = vpc_security_groups

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_migration_project(
        self,
        migration_project_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        migration_project_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        source_data_provider_descriptors: Optional[
            "capo_database_migration_service.types.data_provider_descriptor_definition_list.DataProviderDescriptorDefinitionList"
        ] = None,
        target_data_provider_descriptors: Optional[
            "capo_database_migration_service.types.data_provider_descriptor_definition_list.DataProviderDescriptorDefinitionList"
        ] = None,
        instance_profile_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        transformation_rules: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        schema_conversion_application_attributes: Optional[
            "capo_database_migration_service.types.sc_application_attributes.SCApplicationAttributes"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_migration_project_response.ModifyMigrationProjectResponse":
        """<p>Modifies the specified migration project using the provided parameters.</p> <p> <b>Required permissions:</b> <code>dms:UpdateMigrationProject</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p> <note> <p>The migration project must be closed before you can modify it.</p> </note>

        Args:
            migration_project_identifier: <p>The identifier of the migration project. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.</p>
            migration_project_name: <p>A user-friendly name for the migration project.</p>
            source_data_provider_descriptors: <p>Information about the source data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters.</p>
            target_data_provider_descriptors: <p>Information about the target data provider, including the name, ARN, and Amazon Web Services Secrets Manager parameters.</p>
            instance_profile_identifier: <p>The name or Amazon Resource Name (ARN) for the instance profile.</p>
            transformation_rules: <p>A JSON string that specifies the transformation rules for the migration project. Transformation rules let you customize how DMS Schema Conversion converts your source database objects, including renaming, adding prefixes or suffixes, and changing data types. For the transformation rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-transformation-rules.html">Transformation rules in DMS Schema Conversion</a>.</p> <note> <p>Homogeneous data migrations do not support transformation rules.</p> </note>
            description: <p>A user-friendly description of the migration project.</p>
            schema_conversion_application_attributes: <p>The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Modify a migration project
            The following example updates the source data provider and description of a migration project.

            >>> await client.modify_migration_project(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', description='Updated migration project description', source_data_provider_descriptors=[{'DataProviderIdentifier': 'arn:aws:dms:us-east-1:111122223333:data-provider:EXAMPLEABCDEFGHIJKLMNOPQRS'}])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_migration_project_message.ModifyMigrationProjectMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_migration_project_response.ModifyMigrationProjectResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_migration_project

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_migration_project.async_modify_migration_project(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_migration_project_message.ModifyMigrationProjectMessage = {
            "migration_project_identifier": migration_project_identifier
        }
        if migration_project_name is not None:
            input_["migration_project_name"] = migration_project_name
        if source_data_provider_descriptors is not None:
            input_["source_data_provider_descriptors"] = (
                source_data_provider_descriptors
            )
        if target_data_provider_descriptors is not None:
            input_["target_data_provider_descriptors"] = (
                target_data_provider_descriptors
            )
        if instance_profile_identifier is not None:
            input_["instance_profile_identifier"] = instance_profile_identifier
        if transformation_rules is not None:
            input_["transformation_rules"] = transformation_rules
        if description is not None:
            input_["description"] = description
        if schema_conversion_application_attributes is not None:
            input_["schema_conversion_application_attributes"] = (
                schema_conversion_application_attributes
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_replication_config(
        self,
        replication_config_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_config_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_type: Optional[
            "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
        ] = None,
        table_mappings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_settings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        supplemental_settings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        compute_config: Optional[
            "capo_database_migration_service.types.compute_config.ComputeConfig"
        ] = None,
        source_endpoint_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        target_endpoint_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_replication_config_response.ModifyReplicationConfigResponse":
        """<p>Modifies an existing DMS Serverless replication configuration that you can use to start a replication. This command includes input validation and logic to check the state of any replication that uses this configuration. You can only modify a replication configuration before any replication that uses it has started. As soon as you have initially started a replication with a given configuiration, you can't modify that configuration, even if you stop it.</p> <p>Other run statuses that allow you to run this command include FAILED and CREATED. A provisioning state that allows you to run this command is FAILED_PROVISION.</p>

        Args:
            replication_config_arn: <p>The Amazon Resource Name of the replication to modify.</p>
            replication_config_identifier: <p>The new replication config to apply to the replication.</p>
            replication_type: <p>The type of replication.</p>
            table_mappings: <p>Table mappings specified in the replication.</p>
            replication_settings: <p>The settings for the replication.</p>
            supplemental_settings: <p>Additional settings for the replication.</p>
            compute_config: <p>Configuration parameters for provisioning an DMS Serverless replication.</p>
            source_endpoint_arn: <p>The Amazon Resource Name (ARN) of the source endpoint for this DMS serverless replication configuration.</p>
            target_endpoint_arn: <p>The Amazon Resource Name (ARN) of the target endpoint for this DMS serverless replication configuration.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.invalid_subnet.InvalidSubnet: <p>The subnet provided isn't valid.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.replication_subnet_group_does_not_cover_enough_a_zs.ReplicationSubnetGroupDoesNotCoverEnoughAZs: <p>The replication subnet group does not cover enough Availability Zones (AZs). Edit the replication subnet group and add more AZs.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_replication_config_message.ModifyReplicationConfigMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_replication_config_response.ModifyReplicationConfigResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_config

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_config.async_modify_replication_config(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_replication_config_message.ModifyReplicationConfigMessage = {
            "replication_config_arn": replication_config_arn
        }
        if replication_config_identifier is not None:
            input_["replication_config_identifier"] = replication_config_identifier
        if replication_type is not None:
            input_["replication_type"] = replication_type
        if table_mappings is not None:
            input_["table_mappings"] = table_mappings
        if replication_settings is not None:
            input_["replication_settings"] = replication_settings
        if supplemental_settings is not None:
            input_["supplemental_settings"] = supplemental_settings
        if compute_config is not None:
            input_["compute_config"] = compute_config
        if source_endpoint_arn is not None:
            input_["source_endpoint_arn"] = source_endpoint_arn
        if target_endpoint_arn is not None:
            input_["target_endpoint_arn"] = target_endpoint_arn

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_replication_instance(
        self,
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        allocated_storage: Optional[
            "capo_database_migration_service.types.integer_optional.IntegerOptional"
        ] = None,
        apply_immediately: Optional[
            "capo_database_migration_service.types.boolean.Boolean"
        ] = None,
        replication_instance_class: Optional[
            "capo_database_migration_service.types.replication_instance_class.ReplicationInstanceClass"
        ] = None,
        vpc_security_group_ids: Optional[
            "capo_database_migration_service.types.vpc_security_group_id_list.VpcSecurityGroupIdList"
        ] = None,
        preferred_maintenance_window: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        multi_az: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        engine_version: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        allow_major_version_upgrade: Optional[
            "capo_database_migration_service.types.boolean.Boolean"
        ] = None,
        auto_minor_version_upgrade: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        replication_instance_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        network_type: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        kerberos_authentication_settings: Optional[
            "capo_database_migration_service.types.kerberos_authentication_settings.KerberosAuthenticationSettings"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_replication_instance_response.ModifyReplicationInstanceResponse":
        """<p>Modifies the replication instance to apply new settings. You can change one or more parameters by specifying these parameters and the new values in the request.</p> <p>Some settings are applied during the maintenance window.</p> <p></p>

        Args:
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance.</p>
            allocated_storage: <p>The amount of storage (in gigabytes) to be allocated for the replication instance.</p>
            apply_immediately: <p>Indicates whether the changes should be applied immediately or during the next maintenance window.</p>
            replication_instance_class: <p>The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example to specify the instance class dms.c4.large, set this parameter to <code>"dms.c4.large"</code>.</p> <p>For more information on the settings and capacities for the available replication instance classes, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth"> Selecting the right DMS replication instance for your migration</a>. </p>
            vpc_security_group_ids: <p> Specifies the VPC security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance. </p>
            preferred_maintenance_window: <p>The weekly time range (in UTC) during which system maintenance can occur, which might result in an outage. Changing this parameter does not result in an outage, except in the following situation, and the change is asynchronously applied as soon as possible. If moving this window to the current time, there must be at least 30 minutes between the current time and end of the window to ensure pending changes are applied.</p> <p>Default: Uses existing setting</p> <p>Format: ddd:hh24:mi-ddd:hh24:mi</p> <p>Valid Days: Mon | Tue | Wed | Thu | Fri | Sat | Sun</p> <p>Constraints: Must be at least 30 minutes</p>
            multi_az: <p> Specifies whether the replication instance is a Multi-AZ deployment. You can't set the <code>AvailabilityZone</code> parameter if the Multi-AZ parameter is set to <code>true</code>. </p>
            engine_version: <p>The engine version number of the replication instance.</p> <p>When modifying a major engine version of an instance, also set <code>AllowMajorVersionUpgrade</code> to <code>true</code>.</p>
            allow_major_version_upgrade: <p>Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.</p> <p>This parameter must be set to <code>true</code> when specifying a value for the <code>EngineVersion</code> parameter that is a different major version than the replication instance's current version.</p>
            auto_minor_version_upgrade: <p>A value that indicates that minor version upgrades are applied automatically to the replication instance during the maintenance window. Changing this parameter doesn't result in an outage, except in the case described following. The change is asynchronously applied as soon as possible. </p> <p>An outage does result if these factors apply: </p> <ul> <li> <p>This parameter is set to <code>true</code> during the maintenance window.</p> </li> <li> <p>A newer minor version is available. </p> </li> <li> <p>DMS has enabled automatic patching for the given engine version. </p> </li> </ul>
            replication_instance_identifier: <p>The replication instance identifier. This parameter is stored as a lowercase string.</p>
            network_type: <p>The type of IP address protocol used by a replication instance, such as IPv4 only or Dual-stack that supports both IPv4 and IPv6 addressing. IPv6 only is not yet supported.</p>
            kerberos_authentication_settings: <p>Specifies the settings required for kerberos authentication when modifying a replication instance.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.insufficient_resource_capacity_fault.InsufficientResourceCapacityFault: <p>There are not enough resources allocated to the database migration.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.storage_quota_exceeded_fault.StorageQuotaExceededFault: <p>The storage quota has been exceeded.</p>
            capo_database_migration_service.errors.upgrade_dependency_failure_fault.UpgradeDependencyFailureFault: <p>An upgrade dependency is preventing the database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Modify replication instance
            Modifies the replication instance to apply new settings. You can change one or more parameters by specifying these parameters and the new values in the request. Some settings are applied during the maintenance window.

            >>> await client.modify_replication_instance(replication_instance_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ', allocated_storage=123, apply_immediately=True, replication_instance_class='dms.t2.micro', vpc_security_group_ids=[], preferred_maintenance_window='sun:06:00-sun:14:00', multi_az=True, engine_version='1.5.0', allow_major_version_upgrade=True, auto_minor_version_upgrade=True, replication_instance_identifier='test-rep-1')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_replication_instance_message.ModifyReplicationInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_replication_instance_response.ModifyReplicationInstanceResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_instance

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_instance.async_modify_replication_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_replication_instance_message.ModifyReplicationInstanceMessage = {
            "replication_instance_arn": replication_instance_arn
        }
        if allocated_storage is not None:
            input_["allocated_storage"] = allocated_storage
        if apply_immediately is not None:
            input_["apply_immediately"] = apply_immediately
        if replication_instance_class is not None:
            input_["replication_instance_class"] = replication_instance_class
        if vpc_security_group_ids is not None:
            input_["vpc_security_group_ids"] = vpc_security_group_ids
        if preferred_maintenance_window is not None:
            input_["preferred_maintenance_window"] = preferred_maintenance_window
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if engine_version is not None:
            input_["engine_version"] = engine_version
        if allow_major_version_upgrade is not None:
            input_["allow_major_version_upgrade"] = allow_major_version_upgrade
        if auto_minor_version_upgrade is not None:
            input_["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if replication_instance_identifier is not None:
            input_["replication_instance_identifier"] = replication_instance_identifier
        if network_type is not None:
            input_["network_type"] = network_type
        if kerberos_authentication_settings is not None:
            input_["kerberos_authentication_settings"] = (
                kerberos_authentication_settings
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_replication_subnet_group(
        self,
        replication_subnet_group_identifier: "capo_database_migration_service.types.string.String",
        subnet_ids: "capo_database_migration_service.types.subnet_identifier_list.SubnetIdentifierList",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_subnet_group_description: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_replication_subnet_group_response.ModifyReplicationSubnetGroupResponse":
        """<p>Modifies the settings for the specified replication subnet group.</p>

        Args:
            replication_subnet_group_identifier: <p>The name of the replication instance subnet group.</p>
            replication_subnet_group_description: <p>A description for the replication instance subnet group.</p>
            subnet_ids: <p>A list of subnet IDs.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_subnet.InvalidSubnet: <p>The subnet provided isn't valid.</p>
            capo_database_migration_service.errors.replication_subnet_group_does_not_cover_enough_a_zs.ReplicationSubnetGroupDoesNotCoverEnoughAZs: <p>The replication subnet group does not cover enough Availability Zones (AZs). Edit the replication subnet group and add more AZs.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.subnet_already_in_use.SubnetAlreadyInUse: <p>The specified subnet is already in use.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Modify replication subnet group
            Modifies the settings for the specified replication subnet group.

            >>> await client.modify_replication_subnet_group(replication_subnet_group_identifier='', replication_subnet_group_description='', subnet_ids=[])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_replication_subnet_group_message.ModifyReplicationSubnetGroupMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_replication_subnet_group_response.ModifyReplicationSubnetGroupResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_subnet_group

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_subnet_group.async_modify_replication_subnet_group(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_replication_subnet_group_message.ModifyReplicationSubnetGroupMessage = {
            "replication_subnet_group_identifier": replication_subnet_group_identifier,
            "subnet_ids": subnet_ids,
        }
        if replication_subnet_group_description is not None:
            input_["replication_subnet_group_description"] = (
                replication_subnet_group_description
            )

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def modify_replication_task(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        replication_task_identifier: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        migration_type: Optional[
            "capo_database_migration_service.types.migration_type_value.MigrationTypeValue"
        ] = None,
        table_mappings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        replication_task_settings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        cdc_start_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        cdc_start_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        cdc_stop_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        task_data: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.modify_replication_task_response.ModifyReplicationTaskResponse":
        """<p>Modifies the specified replication task.</p> <p>You can't modify the task endpoints. The task must be stopped before you can modify it. </p> <p>For more information about DMS tasks, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html">Working with Migration Tasks</a> in the <i>Database Migration Service User Guide</i>.</p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name (ARN) of the replication task.</p>
            replication_task_identifier: <p>The replication task identifier.</p> <p>Constraints:</p> <ul> <li> <p>Must contain 1-255 alphanumeric characters or hyphens.</p> </li> <li> <p>First character must be a letter.</p> </li> <li> <p>Cannot end with a hyphen or contain two consecutive hyphens.</p> </li> </ul>
            migration_type: <p>The migration type. Valid values: <code>full-load</code> | <code>cdc</code> | <code>full-load-and-cdc</code> </p>
            table_mappings: <p>When using the CLI or boto3, provide the path of the JSON file that contains the table mappings. Precede the path with <code>file://</code>. For example, <code>--table-mappings file://mappingfile.json</code>. When working with the DMS API, provide the JSON as the parameter value. </p>
            replication_task_settings: <p>JSON file that contains settings for the task, such as task metadata settings.</p>
            cdc_start_time: <p>Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p>Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”</p>
            cdc_start_position: <p>Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p> The value can be in date, checkpoint, or LSN/SCN format.</p> <p>Date Example: --cdc-start-position “2018-03-08T12:12:12”</p> <p>Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"</p> <p>LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”</p> <note> <p>When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the <code>slotName</code> extra connection attribute to the name of this logical replication slot. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib">Extra Connection Attributes When Using PostgreSQL as a Source for DMS</a>.</p> </note>
            cdc_stop_position: <p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p> <p>Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”</p> <p>Commit time example: --cdc-stop-position “commit_time:2018-02-09T12:12:12“</p>
            task_data: <p>Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html">Specifying Supplemental Data for Task Settings</a> in the <i>Database Migration Service User Guide.</i> </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.modify_replication_task_message.ModifyReplicationTaskMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.modify_replication_task_response.ModifyReplicationTaskResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_task

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.modify_replication_task.async_modify_replication_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.modify_replication_task_message.ModifyReplicationTaskMessage = {
            "replication_task_arn": replication_task_arn
        }
        if replication_task_identifier is not None:
            input_["replication_task_identifier"] = replication_task_identifier
        if migration_type is not None:
            input_["migration_type"] = migration_type
        if table_mappings is not None:
            input_["table_mappings"] = table_mappings
        if replication_task_settings is not None:
            input_["replication_task_settings"] = replication_task_settings
        if cdc_start_time is not None:
            input_["cdc_start_time"] = cdc_start_time
        if cdc_start_position is not None:
            input_["cdc_start_position"] = cdc_start_position
        if cdc_stop_position is not None:
            input_["cdc_stop_position"] = cdc_stop_position
        if task_data is not None:
            input_["task_data"] = task_data

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def move_replication_task(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        target_replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.move_replication_task_response.MoveReplicationTaskResponse":
        """<p>Moves a replication task from its current replication instance to a different target replication instance using the specified parameters. The target replication instance must be created with the same or later DMS version as the current replication instance.</p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name (ARN) of the task that you want to move.</p>
            target_replication_instance_arn: <p>The ARN of the replication instance where you want to move the task to.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.move_replication_task_message.MoveReplicationTaskMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.move_replication_task_response.MoveReplicationTaskResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.move_replication_task

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.move_replication_task.async_move_replication_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.move_replication_task_message.MoveReplicationTaskMessage = {
            "replication_task_arn": replication_task_arn,
            "target_replication_instance_arn": target_replication_instance_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reboot_replication_instance(
        self,
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        force_failover: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
        force_planned_failover: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.reboot_replication_instance_response.RebootReplicationInstanceResponse":
        """<p>Reboots a replication instance. Rebooting results in a momentary outage, until the replication instance becomes available again.</p>

        Args:
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance.</p>
            force_failover: <p>If this parameter is <code>true</code>, the reboot is conducted through a Multi-AZ failover. If the instance isn't configured for Multi-AZ, then you can't specify <code>true</code>. ( <code>--force-planned-failover</code> and <code>--force-failover</code> can't both be set to <code>true</code>.)</p>
            force_planned_failover: <p>If this parameter is <code>true</code>, the reboot is conducted through a planned Multi-AZ failover where resources are released and cleaned up prior to conducting the failover. If the instance isn''t configured for Multi-AZ, then you can't specify <code>true</code>. ( <code>--force-planned-failover</code> and <code>--force-failover</code> can't both be set to <code>true</code>.)</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.reboot_replication_instance_message.RebootReplicationInstanceMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.reboot_replication_instance_response.RebootReplicationInstanceResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.reboot_replication_instance

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.reboot_replication_instance.async_reboot_replication_instance(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.reboot_replication_instance_message.RebootReplicationInstanceMessage = {
            "replication_instance_arn": replication_instance_arn
        }
        if force_failover is not None:
            input_["force_failover"] = force_failover
        if force_planned_failover is not None:
            input_["force_planned_failover"] = force_planned_failover

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def refresh_schemas(
        self,
        endpoint_arn: "capo_database_migration_service.types.string.String",
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.refresh_schemas_response.RefreshSchemasResponse":
        """<p>Populates the schema for the specified endpoint. This is an asynchronous operation and can take several minutes. You can check the status of this operation by calling the DescribeRefreshSchemasStatus operation.</p>

        Args:
            endpoint_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Refresh schema
            Populates the schema for the specified endpoint. This is an asynchronous operation and can take several minutes. You can check the status of this operation by calling the describe-refresh-schemas-status operation.

            >>> await client.refresh_schemas(endpoint_arn='', replication_instance_arn='')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.refresh_schemas_message.RefreshSchemasMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.refresh_schemas_response.RefreshSchemasResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.refresh_schemas

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.refresh_schemas.async_refresh_schemas(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.refresh_schemas_message.RefreshSchemasMessage = {
            "endpoint_arn": endpoint_arn,
            "replication_instance_arn": replication_instance_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reload_replication_tables(
        self,
        replication_config_arn: "capo_database_migration_service.types.string.String",
        tables_to_reload: "capo_database_migration_service.types.table_list_to_reload.TableListToReload",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        reload_option: Optional[
            "capo_database_migration_service.types.reload_option_value.ReloadOptionValue"
        ] = None,
    ) -> "capo_database_migration_service.types.reload_replication_tables_response.ReloadReplicationTablesResponse":
        """<p>Reloads the target database table with the source data for a given DMS Serverless replication configuration.</p> <p>You can only use this operation with a task in the RUNNING state, otherwise the service will throw an <code>InvalidResourceStateFault</code> exception.</p>

        Args:
            replication_config_arn: <p>The Amazon Resource Name of the replication config for which to reload tables.</p>
            tables_to_reload: <p>The list of tables to reload.</p>
            reload_option: <p>Options for reload. Specify <code>data-reload</code> to reload the data and re-validate it if validation is enabled. Specify <code>validate-only</code> to re-validate the table. This option applies only when validation is enabled for the replication. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.reload_replication_tables_message.ReloadReplicationTablesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.reload_replication_tables_response.ReloadReplicationTablesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.reload_replication_tables

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.reload_replication_tables.async_reload_replication_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.reload_replication_tables_message.ReloadReplicationTablesMessage = {
            "replication_config_arn": replication_config_arn,
            "tables_to_reload": tables_to_reload,
        }
        if reload_option is not None:
            input_["reload_option"] = reload_option

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def reload_tables(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        tables_to_reload: "capo_database_migration_service.types.table_list_to_reload.TableListToReload",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        reload_option: Optional[
            "capo_database_migration_service.types.reload_option_value.ReloadOptionValue"
        ] = None,
    ) -> "capo_database_migration_service.types.reload_tables_response.ReloadTablesResponse":
        """<p>Reloads the target database table with the source data. </p> <p>You can only use this operation with a task in the <code>RUNNING</code> state, otherwise the service will throw an <code>InvalidResourceStateFault</code> exception.</p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name (ARN) of the replication task. </p>
            tables_to_reload: <p>The name and schema of the table to be reloaded. </p>
            reload_option: <p>Options for reload. Specify <code>data-reload</code> to reload the data and re-validate it if validation is enabled. Specify <code>validate-only</code> to re-validate the table. This option applies only when validation is enabled for the task. </p> <p>Valid values: data-reload, validate-only</p> <p>Default value is data-reload.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.reload_tables_message.ReloadTablesMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.reload_tables_response.ReloadTablesResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.reload_tables

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.reload_tables.async_reload_tables(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.reload_tables_message.ReloadTablesMessage = {
            "replication_task_arn": replication_task_arn,
            "tables_to_reload": tables_to_reload,
        }
        if reload_option is not None:
            input_["reload_option"] = reload_option

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def remove_tags_from_resource(
        self,
        resource_arn: "capo_database_migration_service.types.string.String",
        tag_keys: "capo_database_migration_service.types.key_list.KeyList",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.remove_tags_from_resource_response.RemoveTagsFromResourceResponse":
        """<p>Removes metadata tags from an DMS resource, including replication instance, endpoint, subnet group, and migration task. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_Tag.html"> <code>Tag</code> </a> data type description.</p>

        Args:
            resource_arn: <p>An DMS resource from which you want to remove tag(s). The value for this parameter is an Amazon Resource Name (ARN).</p>
            tag_keys: <p>The tag key (name) of the tag to be removed.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Remove tags from resource
            Removes metadata tags from an AWS DMS resource.

            >>> await client.remove_tags_from_resource(resource_arn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E', tag_keys=[])
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.remove_tags_from_resource_response.RemoveTagsFromResourceResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.remove_tags_from_resource

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.remove_tags_from_resource.async_remove_tags_from_resource(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.remove_tags_from_resource_message.RemoveTagsFromResourceMessage = {
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

    async def run_fleet_advisor_lsa_analysis(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.run_fleet_advisor_lsa_analysis_response.RunFleetAdvisorLsaAnalysisResponse":
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Runs large-scale assessment (LSA) analysis on every Fleet Advisor collector in your account.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[None]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.run_fleet_advisor_lsa_analysis_response.RunFleetAdvisorLsaAnalysisResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.run_fleet_advisor_lsa_analysis

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.run_fleet_advisor_lsa_analysis.async_run_fleet_advisor_lsa_analysis(
                req.options
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_data_migration(
        self,
        data_migration_identifier: "capo_database_migration_service.types.string.String",
        start_type: "capo_database_migration_service.types.start_replication_migration_type_value.StartReplicationMigrationTypeValue",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.start_data_migration_response.StartDataMigrationResponse":
        """<p>Starts the specified data migration.</p>

        Args:
            data_migration_identifier: <p>The identifier (name or ARN) of the data migration to start.</p>
            start_type: <p>Specifies the start type for the data migration. Valid values include <code>start-replication</code>, <code>reload-target</code>, and <code>resume-processing</code>.</p>

        Raises:
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_operation_fault.InvalidOperationFault: <p>The action or operation requested isn't valid.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_data_migration_message.StartDataMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_data_migration_response.StartDataMigrationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_data_migration

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_data_migration.async_start_data_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_data_migration_message.StartDataMigrationMessage = {
            "data_migration_identifier": data_migration_identifier,
            "start_type": start_type,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_extension_pack_association(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.start_extension_pack_association_response.StartExtensionPackAssociationResponse":
        """<p>Queues the installation of the extension pack on your target database. If other requests created by <code>Start*</code> operations are already in the migration project's queue, the installation begins after they complete.</p> <p>This operation requires a non-virtual target data provider.</p> <p>If the extension pack already exists, the operation reinstalls it. To ensure compatibility, reconvert your database objects if the version has changed since your last conversion. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/extension-pack.html">Using extension packs in DMS Schema Conversion</a>.</p> <p>To check the status of the request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeExtensionPackAssociations.html">DescribeExtensionPackAssociations</a> using the returned <code>RequestIdentifier</code> as a filter.</p> <p> <b>Required permissions:</b> <code>dms:AssociateExtensionPack</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Install the extension pack on the target database
            The following example queues the installation of the extension pack on the target database.

            >>> await client.start_extension_pack_association(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_extension_pack_association_message.StartExtensionPackAssociationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_extension_pack_association_response.StartExtensionPackAssociationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_extension_pack_association

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_extension_pack_association.async_start_extension_pack_association(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_extension_pack_association_message.StartExtensionPackAssociationMessage = {
            "migration_project_identifier": migration_project_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_metadata_model_assessment(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.start_metadata_model_assessment_response.StartMetadataModelAssessmentResponse":
        """<p>Queues an assessment of the selected source metadata models (database objects such as tables, views, and procedures) to evaluate conversion complexity to the target database format. If other requests created by <code>Start*</code> operations are already in the migration project's queue, the assessment begins after they complete.</p> <p>The assessment request loads metadata models that are not yet in the metadata tree, but does not reload metadata models that are already present. If your source database has changed since the metadata was loaded, refresh the affected metadata models with <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html">StartMetadataModelImport</a> before calling this operation.</p> <p>To check the status of the assessment request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelAssessments.html">DescribeMetadataModelAssessments</a> using the returned <code>RequestIdentifier</code> as a filter.</p> <p>To export the conversion assessment report after the request completes successfully, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ExportMetadataModelAssessment.html">ExportMetadataModelAssessment</a>.</p> <p> <b>Required permissions:</b> <code>dms:StartMetadataModelAssessment</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that identifies the metadata models to assess. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Assess all objects in a schema
            The following example queues an assessment of the conversion complexity for all objects in the ExampleSchema schema.

            >>> await client.start_metadata_model_assessment(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_metadata_model_assessment_message.StartMetadataModelAssessmentMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_metadata_model_assessment_response.StartMetadataModelAssessmentResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_assessment

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_assessment.async_start_metadata_model_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_metadata_model_assessment_message.StartMetadataModelAssessmentMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_metadata_model_conversion(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.start_metadata_model_conversion_response.StartMetadataModelConversionResponse":
        """<p>Queues a conversion of the selected source metadata models (database objects such as tables, views, and procedures) to the target database format. If other requests created by <code>Start*</code> operations are already in the migration project's queue, the conversion begins after they complete.</p> <p>The conversion request loads metadata models that are not yet in the metadata tree, but does not reload metadata models that are already present. If your source database has changed since the metadata was loaded, refresh the affected metadata models with <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html">StartMetadataModelImport</a> before calling this operation.</p> <note> <p>If converted objects already exist in the target metadata tree, the conversion overwrites them, including any manual edits.</p> </note> <p>To check the status of the conversion request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelConversions.html">DescribeMetadataModelConversions</a> using the returned <code>RequestIdentifier</code> as a filter.</p> <p>To cancel a queued or in-progress request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelConversion.html">CancelMetadataModelConversion</a> with the returned <code>RequestIdentifier</code>.</p> <p>After the conversion completes successfully:</p> <ul> <li> <p>To export a post-conversion assessment report, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_ExportMetadataModelAssessment.html">ExportMetadataModelAssessment</a>.</p> </li> <li> <p>To retrieve converted code, use any of the following options:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModel.html">DescribeMetadataModel</a> and <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelChildren.html">DescribeMetadataModelChildren</a> – navigate the target metadata tree and retrieve converted definitions.</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportAsScript.html">StartMetadataModelExportAsScript</a> – export as data definition language (DDL) scripts to your Amazon S3 bucket.</p> </li> <li> <p> <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelExportToTarget.html">StartMetadataModelExportToTarget</a> – apply directly to your target database.</p> </li> </ul> </li> </ul> <p> <b>Required permissions:</b> <code>dms:StartMetadataModelConversion</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that identifies the metadata models to convert. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Convert all objects in a schema
            The following example queues a conversion of all objects in the ExampleSchema schema to the target database format.

            >>> await client.start_metadata_model_conversion(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_metadata_model_conversion_message.StartMetadataModelConversionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_metadata_model_conversion_response.StartMetadataModelConversionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_conversion

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_conversion.async_start_metadata_model_conversion(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_metadata_model_conversion_message.StartMetadataModelConversionMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_metadata_model_creation(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        metadata_model_name: "capo_database_migration_service.types.string.String",
        properties: "capo_database_migration_service.types.metadata_model_properties.MetadataModelProperties",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.start_metadata_model_creation_response.StartMetadataModelCreationResponse":
        """<p>Queues the creation of a metadata model in the source metadata tree. If other requests created by <code>Start*</code> operations are already in the migration project's queue, the creation begins after they complete.</p> <note> <p>This operation supports only Microsoft SQL Server to Aurora PostgreSQL and Microsoft SQL Server to Amazon RDS for PostgreSQL conversion paths.</p> </note> <p>To check the status of the creation request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelCreations.html">DescribeMetadataModelCreations</a> using the returned <code>RequestIdentifier</code> as a filter.</p> <p>To cancel a queued or in-progress request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelMetadataModelCreation.html">CancelMetadataModelCreation</a> with the returned <code>RequestIdentifier</code>.</p> <important> <p>Calling <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelImport.html">StartMetadataModelImport</a> with <code>Refresh</code> deletes metadata models created by this operation.</p> </important> <p>After the creation completes successfully:</p> <ul> <li> <p>To evaluate conversion complexity, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelAssessment.html">StartMetadataModelAssessment</a>.</p> </li> <li> <p>To convert to the target database format, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_StartMetadataModelConversion.html">StartMetadataModelConversion</a>.</p> </li> </ul> <p> <b>Required permissions:</b> <code>dms:StartMetadataModelCreation</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that identifies the source schema for the metadata model. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only source selection rules, where <code>server-name</code> in the object locator matches the source data provider.</p> </li> <li> <p>Supports only <code>explicit</code> rule actions.</p> </li> <li> <p>Exactly one rule is allowed.</p> </li> </ul>
            metadata_model_name: <p>The name for the metadata model to use in subsequent operations.</p>
            properties: <p>The properties of the metadata model.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Create a metadata model for a SQL statement
            The following example queues the creation of a metadata model for a SQL statement. The selection rule specifies the schema where the metadata model is placed, and MetadataModelName provides a unique identifier for use in subsequent operations.

            >>> await client.start_metadata_model_creation(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection", "rule-id": "1", "rule-name": "1", "object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "database-name": "ExampleDatabase", "schema-name": "ExampleSchema"}, "rule-action": "explicit"}]}', metadata_model_name='ExampleStatement', properties={'StatementProperties': {'Definition': 'SELECT * FROM ExampleTable;'}})
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_metadata_model_creation_message.StartMetadataModelCreationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_metadata_model_creation_response.StartMetadataModelCreationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_creation

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_creation.async_start_metadata_model_creation(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_metadata_model_creation_message.StartMetadataModelCreationMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
            "metadata_model_name": metadata_model_name,
            "properties": properties,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_metadata_model_export_as_script(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        file_name: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.start_metadata_model_export_as_script_response.StartMetadataModelExportAsScriptResponse":
        """<p>Queues an export of metadata models (database objects such as tables, views, and procedures) as a data definition language (DDL) script. The script is stored as a ZIP archive in the Amazon S3 bucket associated with the migration project. If other requests created by <code>Start*</code> operations are already in the migration project's queue, the export begins after they complete.</p> <p>When exporting from the target metadata tree, the export applies only to metadata models created by conversion. Metadata models imported from the database are skipped.</p> <p>To check the status of the export request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelExportsAsScript.html">DescribeMetadataModelExportsAsScript</a> using the returned <code>RequestIdentifier</code> as a filter.</p> <p> <b>Required permissions:</b> <code>dms:StartMetadataModelExportAsScripts</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that identifies the metadata models to export as a SQL script. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts source or target selection rules depending on the <code>Origin</code> parameter. The <code>server-name</code> in the object locator must match the corresponding data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>
            origin: <p>Specifies the metadata tree to export from.</p>
            file_name: <p>The name for the exported file. When you omit this parameter, the service generates a name from the data provider engine name and an export timestamp.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Export converted metadata models as DDL scripts
            The following example queues an export of converted metadata models for all objects in the ExampleSchema schema as data definition language (DDL) scripts to the S3 bucket associated with the migration project.

            >>> await client.start_metadata_model_export_as_script(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-target-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}', origin='TARGET', file_name='ExampleScript')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_metadata_model_export_as_script_message.StartMetadataModelExportAsScriptMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_metadata_model_export_as_script_response.StartMetadataModelExportAsScriptResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_export_as_script

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_export_as_script.async_start_metadata_model_export_as_script(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_metadata_model_export_as_script_message.StartMetadataModelExportAsScriptMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
            "origin": origin,
        }
        if file_name is not None:
            input_["file_name"] = file_name

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_metadata_model_export_to_target(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        overwrite_extension_pack: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.start_metadata_model_export_to_target_response.StartMetadataModelExportToTargetResponse":
        """<p>Queues an export of the selected converted metadata models (database objects such as tables, views, and procedures) to your target database. If other requests created by <code>Start*</code> operations are already in the migration project's queue, the export begins after they complete.</p> <p>This operation requires a non-virtual target data provider.</p> <p>The export applies only metadata models created by conversion. Metadata models imported from the database are skipped.</p> <note> <p>If objects with the same name already exist on the target database, the export overwrites them.</p> </note> <p>The operation installs the extension pack on the target database. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/extension-pack.html">Using extension packs in DMS Schema Conversion</a>.</p> <p>To check the status of the export request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelExportsToTarget.html">DescribeMetadataModelExportsToTarget</a> using the returned <code>RequestIdentifier</code> as a filter.</p> <p> <b>Required permissions:</b> <code>dms:StartMetadataModelExportToTarget</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that identifies the metadata models to export to the target database. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts only target selection rules, where <code>server-name</code> in the object locator matches the target data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>
            overwrite_extension_pack: <p>Specifies whether to overwrite the extension pack if one already exists on the target database. The default value is <code>true</code>.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Export converted metadata models to the target database
            The following example queues an export of converted metadata models for all objects in the ExampleSchema schema to the target database.

            >>> await client.start_metadata_model_export_to_target(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-target-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}', overwrite_extension_pack=True)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_metadata_model_export_to_target_message.StartMetadataModelExportToTargetMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_metadata_model_export_to_target_response.StartMetadataModelExportToTargetResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_export_to_target

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_export_to_target.async_start_metadata_model_export_to_target(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_metadata_model_export_to_target_message.StartMetadataModelExportToTargetMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
        }
        if overwrite_extension_pack is not None:
            input_["overwrite_extension_pack"] = overwrite_extension_pack

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_metadata_model_import(
        self,
        migration_project_identifier: "capo_database_migration_service.types.migration_project_identifier.MigrationProjectIdentifier",
        selection_rules: "capo_database_migration_service.types.string.String",
        origin: "capo_database_migration_service.types.origin_type_value.OriginTypeValue",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        refresh: Optional[
            "capo_database_migration_service.types.boolean.Boolean"
        ] = None,
    ) -> "capo_database_migration_service.types.start_metadata_model_import_response.StartMetadataModelImportResponse":
        """<p>Queues an import of metadata models (database objects such as tables, views, and procedures) from your data provider into the metadata tree. If other requests created by <code>Start*</code> operations are already in the migration project's queue, the import begins after they complete.</p> <p>To check the status of the import request, call <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeMetadataModelImports.html">DescribeMetadataModelImports</a> using the returned <code>RequestIdentifier</code> as a filter.</p> <p> <b>Required permissions:</b> <code>dms:StartMetadataModelImport</code>. For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsdatabasemigrationservice.html">Actions, resources, and condition keys for Database Migration Service</a>.</p>

        Args:
            migration_project_identifier: <p>The migration project name or Amazon Resource Name (ARN).</p>
            selection_rules: <p>A JSON string that identifies the metadata models to import from the data provider. For the selection rule format and examples, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/sc-selection-rules.html">Selection rules in DMS Schema Conversion</a>.</p> <p>Usage:</p> <ul> <li> <p>Accepts source or target selection rules depending on the <code>Origin</code> parameter. The <code>server-name</code> in the object locator must match the corresponding data provider.</p> </li> <li> <p>Supports <code>explicit</code>, <code>include</code>, and <code>exclude</code> rule actions.</p> </li> </ul>
            origin: <p>Specifies the metadata tree to import into.</p> <note> <p>You cannot import from a virtual target data provider.</p> </note>
            refresh: <p>Specifies whether to refresh the selected metadata models from the data provider.</p> <p>When <code>true</code>, the import reloads the selected metadata models with current definitions and removes their existing subtree.</p> <p>When <code>false</code> (default), the import loads the full subtree that has not yet been loaded into the metadata tree.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Import metadata from the source database
            The following example queues a metadata import for all objects in the ExampleSchema schema from the source database.

            >>> await client.start_metadata_model_import(migration_project_identifier='arn:aws:dms:us-east-1:111122223333:migration-project:EXAMPLEABCDEFGHIJKLMNOPQRS', selection_rules='{"rules": [{"rule-type": "selection","rule-id": "1","rule-name": "1","object-locator": {"server-name": "example-source-server.us-east-1.rds.amazonaws.com", "schema-name": "ExampleSchema"},"rule-action": "explicit"}]}', origin='SOURCE', refresh=False)
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_metadata_model_import_message.StartMetadataModelImportMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_metadata_model_import_response.StartMetadataModelImportResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_import

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_metadata_model_import.async_start_metadata_model_import(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_metadata_model_import_message.StartMetadataModelImportMessage = {
            "migration_project_identifier": migration_project_identifier,
            "selection_rules": selection_rules,
            "origin": origin,
        }
        if refresh is not None:
            input_["refresh"] = refresh

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_recommendations(
        self,
        database_id: "capo_database_migration_service.types.string.String",
        settings: "capo_database_migration_service.types.recommendation_settings.RecommendationSettings",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> None:
        """<important> <p> End of support notice: On May 20, 2026, Amazon Web Services will end support for Amazon Web Services DMS Fleet Advisor;. After May 20, 2026, you will no longer be able to access the Amazon Web Services DMS Fleet Advisor; console or Amazon Web Services DMS Fleet Advisor; resources. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/dms_fleet.advisor-end-of-support.html">Amazon Web Services DMS Fleet Advisor end of support</a>. </p> </important> <p>Starts the analysis of your source database to provide recommendations of target engines.</p> <p>You can create recommendations for multiple source databases using <a href="https://docs.aws.amazon.com/dms/latest/APIReference/API_BatchStartRecommendations.html">BatchStartRecommendations</a>.</p>

        Args:
            database_id: <p>The identifier of the source database to analyze and provide recommendations for.</p>
            settings: <p>The settings in JSON format that Fleet Advisor uses to determine target engine recommendations. These parameters include target instance sizing and availability and durability settings. For target instance sizing, Fleet Advisor supports the following two options: total capacity and resource utilization. For availability and durability, Fleet Advisor supports the following two options: production (Multi-AZ deployments) and Dev/Test (Single-AZ deployments).</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_recommendations_request.StartRecommendationsRequest]",
        ) -> AsyncOperationResponse[None]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_recommendations

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_recommendations.async_start_recommendations(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_recommendations_request.StartRecommendationsRequest = {
            "database_id": database_id,
            "settings": settings,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_replication(
        self,
        replication_config_arn: "capo_database_migration_service.types.string.String",
        start_replication_type: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        premigration_assessment_settings: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        cdc_start_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        cdc_start_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        cdc_stop_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.start_replication_response.StartReplicationResponse":
        """<p>For a given DMS Serverless replication configuration, DMS connects to the source endpoint and collects the metadata to analyze the replication workload. Using this metadata, DMS then computes and provisions the required capacity and starts replicating to the target endpoint using the server resources that DMS has provisioned for the DMS Serverless replication.</p>

        Args:
            replication_config_arn: <p>The Amazon Resource Name of the replication for which to start replication.</p>
            start_replication_type: <p>The replication type.</p> <p>When the replication type is <code>full-load</code> or <code>full-load-and-cdc</code>, the only valid value for the first run of the replication is <code>start-replication</code>. This option will start the replication.</p> <p>You can also use <a>ReloadTables</a> to reload specific tables that failed during replication instead of restarting the replication.</p> <p>The <code>resume-processing</code> option isn't applicable for a full-load replication, because you can't resume partially loaded tables during the full load phase.</p> <p>For a <code>full-load-and-cdc</code> replication, DMS migrates table data, and then applies data changes that occur on the source. To load all the tables again, and start capturing source changes, use <code>reload-target</code>. Otherwise use <code>resume-processing</code>, to replicate the changes from the last stop position.</p>
            premigration_assessment_settings: <p>User-defined settings for the premigration assessment. The possible values are:</p> <ul> <li> <p> <code>ResultLocationFolder</code>: The folder within an Amazon S3 bucket where you want DMS to store the results of this assessment run.</p> </li> <li> <p> <code>ResultEncryptionMode</code>: The supported values are <code>SSE_KMS</code> and <code>SSE_S3</code>. If these values are not provided, then the files are not encrypted at rest. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.KMSKeys">Creating Amazon Web Services KMS keys to encrypt Amazon S3 target objects</a>.</p> </li> <li> <p> <code>ResultKmsKeyArn</code>: The ARN of a customer KMS encryption key that you specify when you set <code>ResultEncryptionMode</code> to <code>SSE_KMS</code>.</p> </li> <li> <p> <code>IncludeOnly</code>: A space-separated list of names for specific individual assessments that you want to include. These names come from the default list of individual assessments that Database Migration Service supports for the associated migration.</p> </li> <li> <p> <code>Exclude</code>: A space-separated list of names for specific individual assessments that you want to exclude. These names come from the default list of individual assessments that Database Migration Service supports for the associated migration.</p> </li> <li> <p> <code>FailOnAssessmentFailure</code>: A configurable setting you can set to <code>true</code> (the default setting) or <code>false</code>. Use this setting to to stop the replication from starting automatically if the assessment fails. This can help you evaluate the issue that is preventing the replication from running successfully.</p> </li> </ul>
            cdc_start_time: <p>Indicates the start time for a change data capture (CDC) operation. Use either <code>CdcStartTime</code> or <code>CdcStartPosition</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p>
            cdc_start_position: <p>Indicates when you want a change data capture (CDC) operation to start. Use either <code>CdcStartPosition</code> or <code>CdcStartTime</code> to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p>The value can be in date, checkpoint, or LSN/SCN format.</p>
            cdc_stop_position: <p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_replication_message.StartReplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_replication_response.StartReplicationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication.async_start_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_replication_message.StartReplicationMessage = {
            "replication_config_arn": replication_config_arn,
            "start_replication_type": start_replication_type,
        }
        if premigration_assessment_settings is not None:
            input_["premigration_assessment_settings"] = (
                premigration_assessment_settings
            )
        if cdc_start_time is not None:
            input_["cdc_start_time"] = cdc_start_time
        if cdc_start_position is not None:
            input_["cdc_start_position"] = cdc_start_position
        if cdc_stop_position is not None:
            input_["cdc_stop_position"] = cdc_stop_position

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_replication_task(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        start_replication_task_type: "capo_database_migration_service.types.start_replication_task_type_value.StartReplicationTaskTypeValue",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        cdc_start_time: Optional[
            "capo_database_migration_service.types.t_stamp.TStamp"
        ] = None,
        cdc_start_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        cdc_stop_position: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
    ) -> "capo_database_migration_service.types.start_replication_task_response.StartReplicationTaskResponse":
        """<p>Starts the replication task.</p> <p>For more information about DMS tasks, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html">Working with Migration Tasks </a> in the <i>Database Migration Service User Guide.</i> </p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name (ARN) of the replication task to be started.</p>
            start_replication_task_type: <p>The type of replication task to start.</p> <p> <code>start-replication</code> is the only valid action that can be used for the first time a task with the migration type of <code>full-load</code>full-load, <code>full-load-and-cdc</code> or <code>cdc</code> is run. Any other action used for the first time on a given task, such as <code>resume-processing</code> and reload-target will result in data errors.</p> <p>You can also use <a>ReloadTables</a> to reload specific tables that failed during migration instead of restarting the task.</p> <p>For a <code>full-load</code> task, the resume-processing option will reload any tables that were partially loaded or not yet loaded during the full load phase.</p> <p>For a <code>full-load-and-cdc</code> task, DMS migrates table data, and then applies data changes that occur on the source. To load all the tables again, and start capturing source changes, use <code>reload-target</code>. Otherwise use <code>resume-processing</code>, to replicate the changes from the last stop position.</p> <p>For a <code>cdc</code> only task, to start from a specific position, you must use start-replication and also specify the start position. Check the source endpoint DMS documentation for any limitations. For example, not all sources support starting from a time.</p> <note> <p> <code>resume-processing</code> is only available for previously executed tasks.</p> </note>
            cdc_start_time: <p>Indicates the start time for a change data capture (CDC) operation. Use either CdcStartTime or CdcStartPosition to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p>Timestamp Example: --cdc-start-time “2018-03-08T12:12:12”</p>
            cdc_start_position: <p>Indicates when you want a change data capture (CDC) operation to start. Use either CdcStartPosition or CdcStartTime to specify when you want a CDC operation to start. Specifying both values results in an error.</p> <p> The value can be in date, checkpoint, or LSN/SCN format.</p> <p>Date Example: --cdc-start-position “2018-03-08T12:12:12”</p> <p>Checkpoint Example: --cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"</p> <p>LSN Example: --cdc-start-position “mysql-bin-changelog.000024:373”</p> <note> <p>When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the <code>slotName</code> extra connection attribute to the name of this logical replication slot. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib">Extra Connection Attributes When Using PostgreSQL as a Source for DMS</a>.</p> </note>
            cdc_stop_position: <p>Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time.</p> <p>Server time example: --cdc-stop-position “server_time:2018-02-09T12:12:12”</p> <p>Commit time example: --cdc-stop-position “commit_time:2018-02-09T12:12:12“</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Start replication task
            Starts the replication task.

            >>> await client.start_replication_task(replication_task_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ', start_replication_task_type='start-replication', cdc_start_time='2016-12-14T13:33:20Z')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_replication_task_message.StartReplicationTaskMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_replication_task_response.StartReplicationTaskResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication_task

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication_task.async_start_replication_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_replication_task_message.StartReplicationTaskMessage = {
            "replication_task_arn": replication_task_arn,
            "start_replication_task_type": start_replication_task_type,
        }
        if cdc_start_time is not None:
            input_["cdc_start_time"] = cdc_start_time
        if cdc_start_position is not None:
            input_["cdc_start_position"] = cdc_start_position
        if cdc_stop_position is not None:
            input_["cdc_stop_position"] = cdc_stop_position

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_replication_task_assessment(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.start_replication_task_assessment_response.StartReplicationTaskAssessmentResponse":
        """<p> Starts the replication task assessment for unsupported data types in the source database. </p> <p>You can only use this operation for a task if the following conditions are true:</p> <ul> <li> <p>The task must be in the <code>stopped</code> state.</p> </li> <li> <p>The task must have successful connections to the source and target.</p> </li> </ul> <p>If either of these conditions are not met, an <code>InvalidResourceStateFault</code> error will result. </p> <p>For information about DMS task assessments, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.AssessmentReport.html">Creating a task assessment report</a> in the <i>Database Migration Service User Guide</i>.</p>

        Args:
            replication_task_arn: <p> The Amazon Resource Name (ARN) of the replication task. </p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_replication_task_assessment_message.StartReplicationTaskAssessmentMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_replication_task_assessment_response.StartReplicationTaskAssessmentResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication_task_assessment

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication_task_assessment.async_start_replication_task_assessment(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_replication_task_assessment_message.StartReplicationTaskAssessmentMessage = {
            "replication_task_arn": replication_task_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def start_replication_task_assessment_run(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        service_access_role_arn: "capo_database_migration_service.types.string.String",
        result_location_bucket: "capo_database_migration_service.types.string.String",
        assessment_run_name: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        result_location_folder: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        result_encryption_mode: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        result_kms_key_arn: Optional[
            "capo_database_migration_service.types.string.String"
        ] = None,
        include_only: Optional[
            "capo_database_migration_service.types.include_test_list.IncludeTestList"
        ] = None,
        exclude: Optional[
            "capo_database_migration_service.types.exclude_test_list.ExcludeTestList"
        ] = None,
        tags: Optional["capo_database_migration_service.types.tag_list.TagList"] = None,
    ) -> "capo_database_migration_service.types.start_replication_task_assessment_run_response.StartReplicationTaskAssessmentRunResponse":
        """<p>Starts a new premigration assessment run for one or more individual assessments of a migration task.</p> <p>The assessments that you can specify depend on the source and target database engine and the migration type defined for the given task. To run this operation, your migration task must already be created. After you run this operation, you can review the status of each individual assessment. You can also run the migration task manually after the assessment run and its individual assessments complete.</p>

        Args:
            replication_task_arn: <p>Amazon Resource Name (ARN) of the migration task associated with the premigration assessment run that you want to start.</p>
            service_access_role_arn: <p>ARN of the service role needed to start the assessment run. The role must allow the <code>iam:PassRole</code> action.</p>
            result_location_bucket: <p>Amazon S3 bucket where you want DMS to store the results of this assessment run.</p>
            result_location_folder: <p>Folder within an Amazon S3 bucket where you want DMS to store the results of this assessment run.</p>
            result_encryption_mode: <p>Encryption mode that you can specify to encrypt the results of this assessment run. If you don't specify this request parameter, DMS stores the assessment run results without encryption. You can specify one of the options following:</p> <ul> <li> <p> <code>"SSE_S3"</code> – The server-side encryption provided as a default by Amazon S3.</p> </li> <li> <p> <code>"SSE_KMS"</code> – Key Management Service (KMS) encryption. This encryption can use either a custom KMS encryption key that you specify or the default KMS encryption key that DMS provides.</p> </li> </ul>
            result_kms_key_arn: <p>ARN of a custom KMS encryption key that you specify when you set <code>ResultEncryptionMode</code> to <code>"SSE_KMS</code>".</p>
            assessment_run_name: <p>Unique name to identify the assessment run.</p>
            include_only: <p>Space-separated list of names for specific individual assessments that you want to include. These names come from the default list of individual assessments that DMS supports for the associated migration task. This task is specified by <code>ReplicationTaskArn</code>.</p> <note> <p>You can't set a value for <code>IncludeOnly</code> if you also set a value for <code>Exclude</code> in the API operation. </p> <p>To identify the names of the default individual assessments that DMS supports for the associated migration task, run the <code>DescribeApplicableIndividualAssessments</code> operation using its own <code>ReplicationTaskArn</code> request parameter.</p> </note>
            exclude: <p>Space-separated list of names for specific individual assessments that you want to exclude. These names come from the default list of individual assessments that DMS supports for the associated migration task. This task is specified by <code>ReplicationTaskArn</code>.</p> <note> <p>You can't set a value for <code>Exclude</code> if you also set a value for <code>IncludeOnly</code> in the API operation.</p> <p>To identify the names of the default individual assessments that DMS supports for the associated migration task, run the <code>DescribeApplicableIndividualAssessments</code> operation using its own <code>ReplicationTaskArn</code> request parameter.</p> </note>
            tags: <p>One or more tags to be assigned to the premigration assessment run that you want to start.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_access_denied_fault.KMSAccessDeniedFault: <p>The ciphertext references a key that doesn't exist or that the DMS account doesn't have access to.</p>
            capo_database_migration_service.errors.kms_disabled_fault.KMSDisabledFault: <p>The specified KMS key isn't enabled.</p>
            capo_database_migration_service.errors.kms_fault.KMSFault: <p>An Key Management Service (KMS) error is preventing access to KMS.</p>
            capo_database_migration_service.errors.kms_invalid_state_fault.KMSInvalidStateFault: <p>The state of the specified KMS resource isn't valid for this request.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.kms_not_found_fault.KMSNotFoundFault: <p>The specified KMS entity or resource can't be found.</p>
            capo_database_migration_service.errors.resource_already_exists_fault.ResourceAlreadyExistsFault: <p>The resource you are attempting to create already exists.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.s3_access_denied_fault.S3AccessDeniedFault: <p>Insufficient privileges are preventing access to an Amazon S3 object.</p>
            capo_database_migration_service.errors.s3_resource_not_found_fault.S3ResourceNotFoundFault: <p>A specified Amazon S3 bucket, bucket folder, or other object can't be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.start_replication_task_assessment_run_message.StartReplicationTaskAssessmentRunMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.start_replication_task_assessment_run_response.StartReplicationTaskAssessmentRunResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication_task_assessment_run

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.start_replication_task_assessment_run.async_start_replication_task_assessment_run(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.start_replication_task_assessment_run_message.StartReplicationTaskAssessmentRunMessage = {
            "replication_task_arn": replication_task_arn,
            "service_access_role_arn": service_access_role_arn,
            "result_location_bucket": result_location_bucket,
            "assessment_run_name": assessment_run_name,
        }
        if result_location_folder is not None:
            input_["result_location_folder"] = result_location_folder
        if result_encryption_mode is not None:
            input_["result_encryption_mode"] = result_encryption_mode
        if result_kms_key_arn is not None:
            input_["result_kms_key_arn"] = result_kms_key_arn
        if include_only is not None:
            input_["include_only"] = include_only
        if exclude is not None:
            input_["exclude"] = exclude
        if tags is not None:
            input_["tags"] = tags

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_data_migration(
        self,
        data_migration_identifier: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.stop_data_migration_response.StopDataMigrationResponse":
        """<p>Stops the specified data migration.</p>

        Args:
            data_migration_identifier: <p>The identifier (name or ARN) of the data migration to stop.</p>

        Raises:
            capo_database_migration_service.errors.failed_dependency_fault.FailedDependencyFault: <p>A dependency threw an exception.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.stop_data_migration_message.StopDataMigrationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.stop_data_migration_response.StopDataMigrationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.stop_data_migration

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.stop_data_migration.async_stop_data_migration(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.stop_data_migration_message.StopDataMigrationMessage = {
            "data_migration_identifier": data_migration_identifier
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_replication(
        self,
        replication_config_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.stop_replication_response.StopReplicationResponse":
        """<p>For a given DMS Serverless replication configuration, DMS stops any and all ongoing DMS Serverless replications. This command doesn't deprovision the stopped replications.</p>

        Args:
            replication_config_arn: <p>The Amazon Resource Name of the replication to stop.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.stop_replication_message.StopReplicationMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.stop_replication_response.StopReplicationResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.stop_replication

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.stop_replication.async_stop_replication(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.stop_replication_message.StopReplicationMessage = {
            "replication_config_arn": replication_config_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def stop_replication_task(
        self,
        replication_task_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.stop_replication_task_response.StopReplicationTaskResponse":
        """<p>Stops the replication task.</p>

        Args:
            replication_task_arn: <p>The Amazon Resource Name(ARN) of the replication task to be stopped.</p>

        Raises:
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Stop replication task
            Stops the replication task.

            >>> await client.stop_replication_task(replication_task_arn='arn:aws:dms:us-east-1:123456789012:endpoint:ASXWXJZLNWNT5HTWCGV2BUJQ7E')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.stop_replication_task_message.StopReplicationTaskMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.stop_replication_task_response.StopReplicationTaskResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.stop_replication_task

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.stop_replication_task.async_stop_replication_task(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.stop_replication_task_message.StopReplicationTaskMessage = {
            "replication_task_arn": replication_task_arn
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def test_connection(
        self,
        replication_instance_arn: "capo_database_migration_service.types.string.String",
        endpoint_arn: "capo_database_migration_service.types.string.String",
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
    ) -> "capo_database_migration_service.types.test_connection_response.TestConnectionResponse":
        """<p>Tests the connection between the replication instance and the endpoint.</p>

        Args:
            replication_instance_arn: <p>The Amazon Resource Name (ARN) of the replication instance.</p>
            endpoint_arn: <p>The Amazon Resource Name (ARN) string that uniquely identifies the endpoint.</p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.kms_key_not_accessible_fault.KMSKeyNotAccessibleFault: <p>DMS cannot access the KMS key.</p>
            capo_database_migration_service.errors.resource_not_found_fault.ResourceNotFoundFault: <p>The resource could not be found.</p>
            capo_database_migration_service.errors.resource_quota_exceeded_fault.ResourceQuotaExceededFault: <p>The quota for this resource quota has been exceeded.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Test conection
            Tests the connection between the replication instance and the endpoint.

            >>> await client.test_connection(replication_instance_arn='arn:aws:dms:us-east-1:123456789012:rep:6UTDJGBOUS3VI3SUWA66XFJCJQ', endpoint_arn='arn:aws:dms:us-east-1:123456789012:endpoint:RAAR3R22XSH46S3PWLC3NJAWKM')
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.test_connection_message.TestConnectionMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.test_connection_response.TestConnectionResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.test_connection

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.test_connection.async_test_connection(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.test_connection_message.TestConnectionMessage = {
            "replication_instance_arn": replication_instance_arn,
            "endpoint_arn": endpoint_arn,
        }

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        await response.response.aclose()
        return response.output

    async def update_subscriptions_to_event_bridge(
        self,
        *,
        config_overrides: Optional[AsyncDatabaseMigrationServiceClientConfig] = None,
        force_move: Optional[
            "capo_database_migration_service.types.boolean_optional.BooleanOptional"
        ] = None,
    ) -> "capo_database_migration_service.types.update_subscriptions_to_event_bridge_response.UpdateSubscriptionsToEventBridgeResponse":
        """<p>Migrates 10 active and enabled Amazon SNS subscriptions at a time and converts them to corresponding Amazon EventBridge rules. By default, this operation migrates subscriptions only when all your replication instance versions are 3.4.5 or higher. If any replication instances are from versions earlier than 3.4.5, the operation raises an error and tells you to upgrade these instances to version 3.4.5 or higher. To enable migration regardless of version, set the <code>Force</code> option to true. However, if you don't upgrade instances earlier than version 3.4.5, some types of events might not be available when you use Amazon EventBridge.</p> <p>To call this operation, make sure that you have certain permissions added to your user account. For more information, see <a href="https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html#CHAP_Events-migrate-to-eventbridge">Migrating event subscriptions to Amazon EventBridge</a> in the <i>Amazon Web Services Database Migration Service User Guide</i>.</p>

        Args:
            force_move: <p>When set to true, this operation migrates DMS subscriptions for Amazon SNS notifications no matter what your replication instance version is. If not set or set to false, this operation runs only when all your replication instances are from DMS version 3.4.5 or higher. </p>

        Raises:
            capo_database_migration_service.errors.access_denied_fault.AccessDeniedFault: <p>DMS was denied access to the endpoint. Check that the role is correctly configured.</p>
            capo_database_migration_service.errors.invalid_resource_state_fault.InvalidResourceStateFault: <p>The resource is in a state that prevents it from being used for database migration.</p>
            capo_database_migration_service.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        async def _handler(
            req: "AsyncOperationRequest[capo_database_migration_service.types.update_subscriptions_to_event_bridge_message.UpdateSubscriptionsToEventBridgeMessage]",
        ) -> AsyncOperationResponse[
            "capo_database_migration_service.types.update_subscriptions_to_event_bridge_response.UpdateSubscriptionsToEventBridgeResponse"
        ]:
            import capo_database_migration_service._operations.amazon_dm_sv20160101.update_subscriptions_to_event_bridge

            (
                output,
                http_response,
            ) = await capo_database_migration_service._operations.amazon_dm_sv20160101.update_subscriptions_to_event_bridge.async_update_subscriptions_to_event_bridge(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_database_migration_service.types.update_subscriptions_to_event_bridge_message.UpdateSubscriptionsToEventBridgeMessage = {}
        if force_move is not None:
            input_["force_move"] = force_move

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
