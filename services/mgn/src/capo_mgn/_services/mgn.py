"""Generated from Smithy shape ``com.amazonaws.mgn#ApplicationMigrationService``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_mgn._auth._signers
import capo_mgn._auth._sigv4
from capo_mgn._auth._identity import Credentials
from capo_mgn._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_mgn._auth._zapros_handler import AuthMiddleware
from capo_mgn._pagination import resolve_path as _resolve_path
from capo_mgn._resources.application_migration_service.account_resource import (
    AccountResource,
)
from capo_mgn._resources.application_migration_service.appliance_resource import (
    ApplianceResource,
)
from capo_mgn._resources.application_migration_service.application_resource import (
    ApplicationResource,
)
from capo_mgn._resources.application_migration_service.connector_resource import (
    ConnectorResource,
)
from capo_mgn._resources.application_migration_service.export_resource import (
    ExportResource,
)
from capo_mgn._resources.application_migration_service.import_resource import (
    ImportResource,
)
from capo_mgn._resources.application_migration_service.job_resource import JobResource
from capo_mgn._resources.application_migration_service.launch_configuration_template_resource import (
    LaunchConfigurationTemplateResource,
)
from capo_mgn._resources.application_migration_service.network_migration_definition_resource import (
    NetworkMigrationDefinitionResource,
)
from capo_mgn._resources.application_migration_service.replication_configuration_template_resource import (
    ReplicationConfigurationTemplateResource,
)
from capo_mgn._resources.application_migration_service.source_server_resource import (
    SourceServerResource,
)
from capo_mgn._resources.application_migration_service.vcenter_client_resource import (
    VcenterClientResource,
)
from capo_mgn._resources.application_migration_service.wave_resource import WaveResource
from capo_mgn._services._aws_config import aws_config
from capo_mgn._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_mgn.types.account_id
    import capo_mgn.types.action_category
    import capo_mgn.types.action_description
    import capo_mgn.types.action_id
    import capo_mgn.types.action_name
    import capo_mgn.types.application
    import capo_mgn.types.application_description
    import capo_mgn.types.application_i_ds
    import capo_mgn.types.application_id
    import capo_mgn.types.application_name
    import capo_mgn.types.archive_application_request
    import capo_mgn.types.archive_wave_request
    import capo_mgn.types.arn
    import capo_mgn.types.associate_applications_request
    import capo_mgn.types.associate_applications_response
    import capo_mgn.types.associate_source_servers_request
    import capo_mgn.types.associate_source_servers_request_source_server_i_ds
    import capo_mgn.types.associate_source_servers_response
    import capo_mgn.types.bandwidth_throttling
    import capo_mgn.types.boot_mode
    import capo_mgn.types.bounded_string
    import capo_mgn.types.change_server_life_cycle_state_request
    import capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle
    import capo_mgn.types.cidr_mappings_list
    import capo_mgn.types.client_idempotency_token
    import capo_mgn.types.code_generation_output_format_types
    import capo_mgn.types.connector
    import capo_mgn.types.connector_id
    import capo_mgn.types.connector_name
    import capo_mgn.types.connector_ssm_command_config
    import capo_mgn.types.construct_id
    import capo_mgn.types.create_application_request
    import capo_mgn.types.create_connector_request
    import capo_mgn.types.create_launch_configuration_template_request
    import capo_mgn.types.create_network_migration_definition_request
    import capo_mgn.types.create_replication_configuration_template_request
    import capo_mgn.types.create_wave_request
    import capo_mgn.types.delete_application_request
    import capo_mgn.types.delete_application_response
    import capo_mgn.types.delete_connector_request
    import capo_mgn.types.delete_job_request
    import capo_mgn.types.delete_job_response
    import capo_mgn.types.delete_launch_configuration_template_request
    import capo_mgn.types.delete_launch_configuration_template_response
    import capo_mgn.types.delete_network_migration_definition_request
    import capo_mgn.types.delete_network_migration_definition_response
    import capo_mgn.types.delete_replication_configuration_template_request
    import capo_mgn.types.delete_replication_configuration_template_response
    import capo_mgn.types.delete_source_server_request
    import capo_mgn.types.delete_source_server_response
    import capo_mgn.types.delete_vcenter_client_request
    import capo_mgn.types.delete_wave_request
    import capo_mgn.types.delete_wave_response
    import capo_mgn.types.describe_job_log_items_request
    import capo_mgn.types.describe_job_log_items_response
    import capo_mgn.types.describe_jobs_request
    import capo_mgn.types.describe_jobs_request_filters
    import capo_mgn.types.describe_jobs_response
    import capo_mgn.types.describe_launch_configuration_templates_request
    import capo_mgn.types.describe_launch_configuration_templates_response
    import capo_mgn.types.describe_replication_configuration_templates_request
    import capo_mgn.types.describe_replication_configuration_templates_response
    import capo_mgn.types.describe_source_servers_request
    import capo_mgn.types.describe_source_servers_request_filters
    import capo_mgn.types.describe_source_servers_response
    import capo_mgn.types.describe_vcenter_clients_request
    import capo_mgn.types.describe_vcenter_clients_response
    import capo_mgn.types.disassociate_applications_request
    import capo_mgn.types.disassociate_applications_response
    import capo_mgn.types.disassociate_source_servers_request
    import capo_mgn.types.disassociate_source_servers_request_source_server_i_ds
    import capo_mgn.types.disassociate_source_servers_response
    import capo_mgn.types.disconnect_from_service_request
    import capo_mgn.types.document_version
    import capo_mgn.types.ec2_instance_type
    import capo_mgn.types.enrichment_source_s3_configuration
    import capo_mgn.types.enrichment_target_s3_configuration
    import capo_mgn.types.export_id
    import capo_mgn.types.export_task
    import capo_mgn.types.export_task_error
    import capo_mgn.types.finalize_cutover_request
    import capo_mgn.types.fqdn_for_action_framework
    import capo_mgn.types.get_launch_configuration_request
    import capo_mgn.types.get_network_migration_definition_request
    import capo_mgn.types.get_network_migration_mapper_segment_construct_request
    import capo_mgn.types.get_network_migration_mapper_segment_construct_response
    import capo_mgn.types.get_replication_configuration_request
    import capo_mgn.types.import_file_enrichment
    import capo_mgn.types.import_id
    import capo_mgn.types.import_task
    import capo_mgn.types.import_task_error
    import capo_mgn.types.initialize_service_request
    import capo_mgn.types.initialize_service_response
    import capo_mgn.types.internet_protocol
    import capo_mgn.types.ip_assignment_strategy
    import capo_mgn.types.job
    import capo_mgn.types.job_id
    import capo_mgn.types.job_log
    import capo_mgn.types.kms_key_arn
    import capo_mgn.types.launch_configuration
    import capo_mgn.types.launch_configuration_template
    import capo_mgn.types.launch_configuration_template_i_ds
    import capo_mgn.types.launch_configuration_template_id
    import capo_mgn.types.launch_disposition
    import capo_mgn.types.launch_template_disk_conf
    import capo_mgn.types.licensing
    import capo_mgn.types.list_applications_request
    import capo_mgn.types.list_applications_request_filters
    import capo_mgn.types.list_applications_response
    import capo_mgn.types.list_connectors_request
    import capo_mgn.types.list_connectors_request_filters
    import capo_mgn.types.list_connectors_response
    import capo_mgn.types.list_export_errors_request
    import capo_mgn.types.list_export_errors_response
    import capo_mgn.types.list_exports_request
    import capo_mgn.types.list_exports_request_filters
    import capo_mgn.types.list_exports_response
    import capo_mgn.types.list_import_errors_request
    import capo_mgn.types.list_import_errors_response
    import capo_mgn.types.list_import_file_enrichments_filters
    import capo_mgn.types.list_import_file_enrichments_request
    import capo_mgn.types.list_import_file_enrichments_response
    import capo_mgn.types.list_imports_request
    import capo_mgn.types.list_imports_request_filters
    import capo_mgn.types.list_imports_response
    import capo_mgn.types.list_managed_accounts_request
    import capo_mgn.types.list_managed_accounts_response
    import capo_mgn.types.list_network_migration_analyses_filters
    import capo_mgn.types.list_network_migration_analyses_request
    import capo_mgn.types.list_network_migration_analyses_response
    import capo_mgn.types.list_network_migration_analysis_results_filters
    import capo_mgn.types.list_network_migration_analysis_results_request
    import capo_mgn.types.list_network_migration_analysis_results_response
    import capo_mgn.types.list_network_migration_code_generation_segments_filters
    import capo_mgn.types.list_network_migration_code_generation_segments_request
    import capo_mgn.types.list_network_migration_code_generation_segments_response
    import capo_mgn.types.list_network_migration_code_generations_filters
    import capo_mgn.types.list_network_migration_code_generations_request
    import capo_mgn.types.list_network_migration_code_generations_response
    import capo_mgn.types.list_network_migration_definitions_request
    import capo_mgn.types.list_network_migration_definitions_request_filters
    import capo_mgn.types.list_network_migration_definitions_response
    import capo_mgn.types.list_network_migration_deployed_stacks_request
    import capo_mgn.types.list_network_migration_deployed_stacks_response
    import capo_mgn.types.list_network_migration_deployer_job_filters
    import capo_mgn.types.list_network_migration_deployer_job_response
    import capo_mgn.types.list_network_migration_deployments_request
    import capo_mgn.types.list_network_migration_execution_request_filters
    import capo_mgn.types.list_network_migration_executions_request
    import capo_mgn.types.list_network_migration_executions_response
    import capo_mgn.types.list_network_migration_mapper_segment_constructs_filters
    import capo_mgn.types.list_network_migration_mapper_segment_constructs_request
    import capo_mgn.types.list_network_migration_mapper_segment_constructs_response
    import capo_mgn.types.list_network_migration_mapper_segments_filters
    import capo_mgn.types.list_network_migration_mapper_segments_request
    import capo_mgn.types.list_network_migration_mapper_segments_response
    import capo_mgn.types.list_network_migration_mapping_updates_filters
    import capo_mgn.types.list_network_migration_mapping_updates_request
    import capo_mgn.types.list_network_migration_mapping_updates_response
    import capo_mgn.types.list_network_migration_mappings_filters
    import capo_mgn.types.list_network_migration_mappings_request
    import capo_mgn.types.list_network_migration_mappings_response
    import capo_mgn.types.list_source_server_actions_request
    import capo_mgn.types.list_source_server_actions_response
    import capo_mgn.types.list_tags_for_resource_request
    import capo_mgn.types.list_tags_for_resource_response
    import capo_mgn.types.list_template_actions_request
    import capo_mgn.types.list_template_actions_response
    import capo_mgn.types.list_waves_request
    import capo_mgn.types.list_waves_request_filters
    import capo_mgn.types.list_waves_response
    import capo_mgn.types.managed_account
    import capo_mgn.types.mark_as_archived_request
    import capo_mgn.types.max_results_type
    import capo_mgn.types.network_migration_analysis_job_details
    import capo_mgn.types.network_migration_analysis_result
    import capo_mgn.types.network_migration_code_generation_job_details
    import capo_mgn.types.network_migration_code_generation_segment
    import capo_mgn.types.network_migration_definition
    import capo_mgn.types.network_migration_definition_description
    import capo_mgn.types.network_migration_definition_id
    import capo_mgn.types.network_migration_definition_name
    import capo_mgn.types.network_migration_definition_summary
    import capo_mgn.types.network_migration_deployed_stack_details
    import capo_mgn.types.network_migration_deployer_job_details
    import capo_mgn.types.network_migration_execution
    import capo_mgn.types.network_migration_execution_id
    import capo_mgn.types.network_migration_mapper_segment
    import capo_mgn.types.network_migration_mapper_segment_construct
    import capo_mgn.types.network_migration_mapping_job_details
    import capo_mgn.types.network_migration_mapping_update_job_details
    import capo_mgn.types.operating_system_string
    import capo_mgn.types.order_type
    import capo_mgn.types.pagination_token
    import capo_mgn.types.pause_replication_request
    import capo_mgn.types.positive_integer
    import capo_mgn.types.post_launch_actions
    import capo_mgn.types.put_source_server_action_request
    import capo_mgn.types.put_template_action_request
    import capo_mgn.types.remove_source_server_action_request
    import capo_mgn.types.remove_source_server_action_response
    import capo_mgn.types.remove_template_action_request
    import capo_mgn.types.remove_template_action_response
    import capo_mgn.types.replication_configuration
    import capo_mgn.types.replication_configuration_data_plane_routing
    import capo_mgn.types.replication_configuration_default_large_staging_disk_type
    import capo_mgn.types.replication_configuration_ebs_encryption
    import capo_mgn.types.replication_configuration_replicated_disks
    import capo_mgn.types.replication_configuration_template
    import capo_mgn.types.replication_configuration_template_i_ds
    import capo_mgn.types.replication_configuration_template_id
    import capo_mgn.types.replication_servers_security_groups_i_ds
    import capo_mgn.types.replication_type
    import capo_mgn.types.resume_replication_request
    import capo_mgn.types.retry_data_replication_request
    import capo_mgn.types.s3_bucket_name
    import capo_mgn.types.s3_bucket_source
    import capo_mgn.types.s3_key
    import capo_mgn.types.scope_tags_map
    import capo_mgn.types.security_group_mapping_strategy
    import capo_mgn.types.segment_id
    import capo_mgn.types.small_bounded_string
    import capo_mgn.types.source_configuration_list
    import capo_mgn.types.source_server
    import capo_mgn.types.source_server_action_document
    import capo_mgn.types.source_server_actions_request_filters
    import capo_mgn.types.source_server_connector_action
    import capo_mgn.types.source_server_id
    import capo_mgn.types.ssm_document_external_parameters
    import capo_mgn.types.ssm_document_parameters
    import capo_mgn.types.ssm_instance_id
    import capo_mgn.types.start_cutover_request
    import capo_mgn.types.start_cutover_request_source_server_i_ds
    import capo_mgn.types.start_cutover_response
    import capo_mgn.types.start_export_request
    import capo_mgn.types.start_export_response
    import capo_mgn.types.start_import_file_enrichment_request
    import capo_mgn.types.start_import_file_enrichment_response
    import capo_mgn.types.start_import_request
    import capo_mgn.types.start_import_response
    import capo_mgn.types.start_network_migration_analysis_request
    import capo_mgn.types.start_network_migration_analysis_response
    import capo_mgn.types.start_network_migration_code_generation_request
    import capo_mgn.types.start_network_migration_code_generation_response
    import capo_mgn.types.start_network_migration_deployer_job_response
    import capo_mgn.types.start_network_migration_deployment_request
    import capo_mgn.types.start_network_migration_mapping_request
    import capo_mgn.types.start_network_migration_mapping_response
    import capo_mgn.types.start_network_migration_mapping_update_constructs
    import capo_mgn.types.start_network_migration_mapping_update_request
    import capo_mgn.types.start_network_migration_mapping_update_response
    import capo_mgn.types.start_network_migration_mapping_update_segments
    import capo_mgn.types.start_replication_request
    import capo_mgn.types.start_test_request
    import capo_mgn.types.start_test_request_source_server_i_ds
    import capo_mgn.types.start_test_response
    import capo_mgn.types.stop_replication_request
    import capo_mgn.types.storage_configuration
    import capo_mgn.types.strictly_positive_integer
    import capo_mgn.types.subnet_id
    import capo_mgn.types.tag_keys
    import capo_mgn.types.tag_resource_request
    import capo_mgn.types.tag_value
    import capo_mgn.types.tags_map
    import capo_mgn.types.target_deployment
    import capo_mgn.types.target_instance_type_right_sizing_method
    import capo_mgn.types.target_network
    import capo_mgn.types.target_network_update
    import capo_mgn.types.target_s3_configuration
    import capo_mgn.types.target_s3_configuration_update
    import capo_mgn.types.template_action_document
    import capo_mgn.types.template_actions_request_filters
    import capo_mgn.types.terminate_target_instances_request
    import capo_mgn.types.terminate_target_instances_request_source_server_i_ds
    import capo_mgn.types.terminate_target_instances_response
    import capo_mgn.types.unarchive_application_request
    import capo_mgn.types.unarchive_wave_request
    import capo_mgn.types.untag_resource_request
    import capo_mgn.types.update_application_request
    import capo_mgn.types.update_connector_request
    import capo_mgn.types.update_launch_configuration_request
    import capo_mgn.types.update_launch_configuration_template_request
    import capo_mgn.types.update_network_migration_definition_request
    import capo_mgn.types.update_network_migration_mapper_segment_request
    import capo_mgn.types.update_replication_configuration_request
    import capo_mgn.types.update_replication_configuration_template_request
    import capo_mgn.types.update_source_server_replication_type_request
    import capo_mgn.types.update_source_server_request
    import capo_mgn.types.update_wave_request
    import capo_mgn.types.user_provided_id
    import capo_mgn.types.vcenter_client
    import capo_mgn.types.vcenter_client_id
    import capo_mgn.types.vpc_provisioning_strategy
    import capo_mgn.types.wave
    import capo_mgn.types.wave_description
    import capo_mgn.types.wave_id
    import capo_mgn.types.wave_name


class mgnClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class mgnClient:
    """A client for the ``mgn`` service.

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
        self._config = mgnClientConfig(
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
        self.account_resource = AccountResource(self)
        self.appliance_resource = ApplianceResource(self)
        self.application_resource = ApplicationResource(self)
        self.connector_resource = ConnectorResource(self)
        self.export_resource = ExportResource(self)
        self.import_resource = ImportResource(self)
        self.job_resource = JobResource(self)
        self.launch_configuration_template_resource = (
            LaunchConfigurationTemplateResource(self)
        )
        self.network_migration_definition_resource = NetworkMigrationDefinitionResource(
            self
        )
        self.replication_configuration_template_resource = (
            ReplicationConfigurationTemplateResource(self)
        )
        self.source_server_resource = SourceServerResource(self)
        self.vcenter_client_resource = VcenterClientResource(self)
        self.wave_resource = WaveResource(self)

    def operation_options(
        self, config_overrides: Optional[mgnClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: mgnClientConfig = config_overrides or {}
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

    def initialize_service(
        self, *, config_overrides: Optional[mgnClientConfig] = None
    ) -> "capo_mgn.types.initialize_service_response.InitializeServiceResponse":
        """<p>Initialize Application Migration Service.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.initialize_service_request.InitializeServiceRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.initialize_service_response.InitializeServiceResponse"
        ]:
            import capo_mgn._operations.application_migration_service.initialize_service

            output, http_response = (
                capo_mgn._operations.application_migration_service.initialize_service.initialize_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.initialize_service_request.InitializeServiceRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_import_file_enrichments(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_import_file_enrichments_filters.ListImportFileEnrichmentsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_import_file_enrichments_response.ListImportFileEnrichmentsResponse":
        """<p>Lists import file enrichment jobs with optional filtering by job IDs.</p>

        Args:
            filters: <p>Filters to apply when listing import file enrichment jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListImportFileEnrichments call

            >>> client.list_import_file_enrichments(filters={'jobIDs': ['01234567-abcd-abcd-efab-0123456789ab']}, max_results=10)
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_import_file_enrichments_request.ListImportFileEnrichmentsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_import_file_enrichments_response.ListImportFileEnrichmentsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_import_file_enrichments

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_import_file_enrichments.list_import_file_enrichments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_import_file_enrichments_request.ListImportFileEnrichmentsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_import_file_enrichments(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_import_file_enrichments_filters.ListImportFileEnrichmentsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.import_file_enrichment.ImportFileEnrichment]":
        _token = next_token
        while True:
            _response = self.list_import_file_enrichments(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_managed_accounts(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_managed_accounts_response.ListManagedAccountsResponse":
        """<p>List Managed Accounts.</p>

        Args:
            max_results: <p>List managed accounts request max results.</p>
            next_token: <p>List managed accounts request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_managed_accounts_request.ListManagedAccountsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_managed_accounts_response.ListManagedAccountsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_managed_accounts

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_managed_accounts.list_managed_accounts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_managed_accounts_request.ListManagedAccountsRequest = {}
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

    def iter_list_managed_accounts(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.managed_account.ManagedAccount]":
        _token = next_token
        while True:
            _response = self.list_managed_accounts(
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

    def list_tags_for_resource(
        self,
        resource_arn: "capo_mgn.types.arn.ARN",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>List all tags for your Application Migration Service resources.</p>

        Args:
            resource_arn: <p>List tags for resource request by ARN.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.internal_server_exception.InternalServerException: <p>The server encountered an unexpected condition that prevented it from fulfilling the request.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_tags_for_resource

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_import_file_enrichment(
        self,
        s3_bucket_source: "capo_mgn.types.enrichment_source_s3_configuration.EnrichmentSourceS3Configuration",
        s3_bucket_target: "capo_mgn.types.enrichment_target_s3_configuration.EnrichmentTargetS3Configuration",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        client_token: Optional[
            "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        ip_assignment_strategy: Optional[
            "capo_mgn.types.ip_assignment_strategy.IpAssignmentStrategy"
        ] = None,
    ) -> "capo_mgn.types.start_import_file_enrichment_response.StartImportFileEnrichmentResponse":
        """<p>Starts an import file enrichment job to process and enrich network migration import files with additional metadata and IP assignment strategies.</p>

        Args:
            client_token: <p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>
            s3_bucket_source: <p>The S3 configuration specifying the source location of the import file to be enriched.</p>
            s3_bucket_target: <p>The S3 configuration specifying the target location where the enriched import file will be stored.</p>
            ip_assignment_strategy: <p>The IP assignment strategy to use when enriching the import file. Can be STATIC or DYNAMIC.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartImportFileEnrichment call

            >>> client.start_import_file_enrichment(s3_bucket_source={'s3Bucket': 'my-source-bucket', 's3BucketOwner': '123456789012', 's3Key': 'imports/source-file.csv'}, s3_bucket_target={'s3Bucket': 'my-target-bucket', 's3BucketOwner': '123456789012', 's3Key': 'enriched/output.csv'}, ip_assignment_strategy='STATIC')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_import_file_enrichment_request.StartImportFileEnrichmentRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_import_file_enrichment_response.StartImportFileEnrichmentResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_import_file_enrichment

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_import_file_enrichment.start_import_file_enrichment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_import_file_enrichment_request.StartImportFileEnrichmentRequest = {
            "s3_bucket_source": s3_bucket_source,
            "s3_bucket_target": s3_bucket_target,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if ip_assignment_strategy is not None:
            input_["ip_assignment_strategy"] = ip_assignment_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_mgn.types.arn.ARN",
        tags: "capo_mgn.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Adds or overwrites only the specified tags for the specified Application Migration Service resource or resources. When you specify an existing tag key, the value is overwritten with the new value. Each resource can have a maximum of 50 tags. Each tag consists of a key and optional value.</p>

        Args:
            resource_arn: <p>Tag resource by ARN.</p>
            tags: <p>Tag resource by Tags.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.internal_server_exception.InternalServerException: <p>The server encountered an unexpected condition that prevented it from fulfilling the request.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mgn._operations.application_migration_service.tag_resource

            output, http_response = (
                capo_mgn._operations.application_migration_service.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_mgn.types.arn.ARN",
        tag_keys: "capo_mgn.types.tag_keys.TagKeys",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Deletes the specified set of tags from the specified set of Application Migration Service resources.</p>

        Args:
            resource_arn: <p>Untag resource by ARN.</p>
            tag_keys: <p>Untag resource by Keys.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.internal_server_exception.InternalServerException: <p>The server encountered an unexpected condition that prevented it from fulfilling the request.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[None]:
            import capo_mgn._operations.application_migration_service.untag_resource

            output, http_response = (
                capo_mgn._operations.application_migration_service.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.untag_resource_request.UntagResourceRequest = {
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

    def create_application(
        self,
        name: "capo_mgn.types.application_name.ApplicationName",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional[
            "capo_mgn.types.application_description.ApplicationDescription"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Create application.</p>

        Args:
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            tags: <p>Application tags.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_application_request.CreateApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.create_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_application.create_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.create_application_request.CreateApplicationRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_application_response.DeleteApplicationResponse":
        """<p>Delete application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_application_request.DeleteApplicationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_application_response.DeleteApplicationResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_application.delete_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_application_request.DeleteApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_applications_request_filters.ListApplicationsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_applications_response.ListApplicationsResponse":
        """<p>Retrieves all applications or multiple applications by ID.</p>

        Args:
            filters: <p>Applications list filters.</p>
            max_results: <p>Maximum results to return when listing applications.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Applications list Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_applications_request.ListApplicationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_applications_response.ListApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_applications

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_applications.list_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_applications_request.ListApplicationsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

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
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_applications_request_filters.ListApplicationsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "Iterator[capo_mgn.types.application.Application]":
        _token = next_token
        while True:
            _response = self.list_applications(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def archive_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Archive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.archive_application_request.ArchiveApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.archive_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.archive_application.archive_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.archive_application_request.ArchiveApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_source_servers(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "capo_mgn.types.associate_source_servers_request_source_server_i_ds.AssociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.associate_source_servers_response.AssociateSourceServersResponse":
        """<p>Associate source servers to application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.associate_source_servers_request.AssociateSourceServersRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.associate_source_servers_response.AssociateSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.associate_source_servers

            output, http_response = (
                capo_mgn._operations.application_migration_service.associate_source_servers.associate_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.associate_source_servers_request.AssociateSourceServersRequest = {
            "application_id": application_id,
            "source_server_i_ds": source_server_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_source_servers(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        source_server_i_ds: "capo_mgn.types.disassociate_source_servers_request_source_server_i_ds.DisassociateSourceServersRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse":
        """<p>Disassociate source servers from application.</p>

        Args:
            application_id: <p>Application ID.</p>
            source_server_i_ds: <p>Source server IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.disassociate_source_servers_response.DisassociateSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.disassociate_source_servers

            output, http_response = (
                capo_mgn._operations.application_migration_service.disassociate_source_servers.disassociate_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.disassociate_source_servers_request.DisassociateSourceServersRequest = {
            "application_id": application_id,
            "source_server_i_ds": source_server_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def unarchive_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Unarchive application.</p>

        Args:
            application_id: <p>Application ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.unarchive_application_request.UnarchiveApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.unarchive_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.unarchive_application.unarchive_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.unarchive_application_request.UnarchiveApplicationRequest = {
            "application_id": application_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_application(
        self,
        application_id: "capo_mgn.types.application_id.ApplicationID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.application_name.ApplicationName"] = None,
        description: Optional[
            "capo_mgn.types.application_description.ApplicationDescription"
        ] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.application.Application":
        """<p>Update application.</p>

        Args:
            application_id: <p>Application ID.</p>
            name: <p>Application name.</p>
            description: <p>Application description.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_application_request.UpdateApplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.application.Application"]:
            import capo_mgn._operations.application_migration_service.update_application

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_application.update_application(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_application_request.UpdateApplicationRequest = {
            "application_id": application_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_connector(
        self,
        name: "capo_mgn.types.connector_name.ConnectorName",
        ssm_instance_id: "capo_mgn.types.ssm_instance_id.SsmInstanceID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        ssm_command_config: Optional[
            "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
        ] = None,
    ) -> "capo_mgn.types.connector.Connector":
        """<p>Create Connector.</p>

        Args:
            name: <p>Create Connector request name.</p>
            ssm_instance_id: <p>Create Connector request SSM instance ID.</p>
            tags: <p>Create Connector request tags.</p>
            ssm_command_config: <p>Create Connector request SSM command config.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_connector_request.CreateConnectorRequest]",
        ) -> OperationResponse["capo_mgn.types.connector.Connector"]:
            import capo_mgn._operations.application_migration_service.create_connector

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_connector.create_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.create_connector_request.CreateConnectorRequest = {
            "name": name,
            "ssm_instance_id": ssm_instance_id,
        }
        if tags is not None:
            input_["tags"] = tags
        if ssm_command_config is not None:
            input_["ssm_command_config"] = ssm_command_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_connector(
        self,
        connector_id: "capo_mgn.types.connector_id.ConnectorID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.connector_name.ConnectorName"] = None,
        ssm_command_config: Optional[
            "capo_mgn.types.connector_ssm_command_config.ConnectorSsmCommandConfig"
        ] = None,
    ) -> "capo_mgn.types.connector.Connector":
        """<p>Update Connector.</p>

        Args:
            connector_id: <p>Update Connector request connector ID.</p>
            name: <p>Update Connector request name.</p>
            ssm_command_config: <p>Update Connector request SSM command config.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_connector_request.UpdateConnectorRequest]",
        ) -> OperationResponse["capo_mgn.types.connector.Connector"]:
            import capo_mgn._operations.application_migration_service.update_connector

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_connector.update_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_connector_request.UpdateConnectorRequest = {
            "connector_id": connector_id
        }
        if name is not None:
            input_["name"] = name
        if ssm_command_config is not None:
            input_["ssm_command_config"] = ssm_command_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_connector(
        self,
        connector_id: "capo_mgn.types.connector_id.ConnectorID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Delete Connector.</p>

        Args:
            connector_id: <p>Delete Connector request connector ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_connector_request.DeleteConnectorRequest]",
        ) -> OperationResponse[None]:
            import capo_mgn._operations.application_migration_service.delete_connector

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_connector.delete_connector(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_connector_request.DeleteConnectorRequest = {
            "connector_id": connector_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_connectors(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_connectors_request_filters.ListConnectorsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_connectors_response.ListConnectorsResponse":
        """<p>List Connectors.</p>

        Args:
            filters: <p>List Connectors Request filters.</p>
            max_results: <p>List Connectors Request max results.</p>
            next_token: <p>List Connectors Request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_connectors_request.ListConnectorsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_connectors_response.ListConnectorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_connectors

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_connectors.list_connectors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_connectors_request.ListConnectorsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_connectors(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_connectors_request_filters.ListConnectorsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.connector.Connector]":
        _token = next_token
        while True:
            _response = self.list_connectors(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_export(
        self,
        s3_bucket: "capo_mgn.types.s3_bucket_name.S3BucketName",
        s3_key: "capo_mgn.types.s3_key.S3Key",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        s3_bucket_owner: Optional["capo_mgn.types.account_id.AccountID"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
    ) -> "capo_mgn.types.start_export_response.StartExportResponse":
        """<p>Start export.</p>

        Args:
            s3_bucket: <p>Start export request s3 bucket.</p>
            s3_key: <p>Start export request s3key.</p>
            s3_bucket_owner: <p>Start export request s3 bucket owner.</p>
            tags: <p>Start export request tags.</p>

        Raises:
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_export_request.StartExportRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_export_response.StartExportResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_export

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_export.start_export(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_export_request.StartExportRequest = {
            "s3_bucket": s3_bucket,
            "s3_key": s3_key,
        }
        if s3_bucket_owner is not None:
            input_["s3_bucket_owner"] = s3_bucket_owner
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_exports(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_exports_request_filters.ListExportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_exports_response.ListExportsResponse":
        """<p>List exports.</p>

        Args:
            max_results: <p>List export request max results.</p>
            next_token: <p>List export request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_exports_request.ListExportsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_exports_response.ListExportsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_exports

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_exports.list_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_exports_request.ListExportsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_exports(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_exports_request_filters.ListExportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.export_task.ExportTask]":
        _token = next_token
        while True:
            _response = self.list_exports(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_export_errors(
        self,
        export_id: "capo_mgn.types.export_id.ExportID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_export_errors_response.ListExportErrorsResponse":
        """<p>List export errors.</p>

        Args:
            export_id: <p>List export errors request export id.</p>
            max_results: <p>List export errors request max results.</p>
            next_token: <p>List export errors request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_export_errors_request.ListExportErrorsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_export_errors_response.ListExportErrorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_export_errors

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_export_errors.list_export_errors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_export_errors_request.ListExportErrorsRequest = {
            "export_id": export_id
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

    def iter_list_export_errors(
        self,
        export_id: "capo_mgn.types.export_id.ExportID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.export_task_error.ExportTaskError]":
        _token = next_token
        while True:
            _response = self.list_export_errors(
                export_id,
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

    def start_import(
        self,
        s3_bucket_source: "capo_mgn.types.s3_bucket_source.S3BucketSource",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        client_token: Optional[
            "capo_mgn.types.client_idempotency_token.ClientIdempotencyToken"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
    ) -> "capo_mgn.types.start_import_response.StartImportResponse":
        """<p>Start import.</p>

        Args:
            client_token: <p>Start import request client token.</p>
            s3_bucket_source: <p>Start import request s3 bucket source.</p>
            tags: <p>Start import request tags.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_import_request.StartImportRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_import_response.StartImportResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_import

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_import.start_import(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_import_request.StartImportRequest = {
            "s3_bucket_source": s3_bucket_source
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

    def list_imports(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_imports_request_filters.ListImportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_imports_response.ListImportsResponse":
        """<p>List imports.</p>

        Args:
            filters: <p>List imports request filters.</p>
            max_results: <p>List imports request max results.</p>
            next_token: <p>List imports request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_imports_request.ListImportsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_imports_response.ListImportsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_imports

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_imports.list_imports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_imports_request.ListImportsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_imports(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_imports_request_filters.ListImportsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.import_task.ImportTask]":
        _token = next_token
        while True:
            _response = self.list_imports(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_import_errors(
        self,
        import_id: "capo_mgn.types.import_id.ImportID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_import_errors_response.ListImportErrorsResponse":
        """<p>List import errors.</p>

        Args:
            import_id: <p>List import errors request import id.</p>
            max_results: <p>List import errors request max results.</p>
            next_token: <p>List import errors request next token.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_import_errors_request.ListImportErrorsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_import_errors_response.ListImportErrorsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_import_errors

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_import_errors.list_import_errors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_import_errors_request.ListImportErrorsRequest = {
            "import_id": import_id
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

    def iter_list_import_errors(
        self,
        import_id: "capo_mgn.types.import_id.ImportID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.import_task_error.ImportTaskError]":
        _token = next_token
        while True:
            _response = self.list_import_errors(
                import_id,
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

    def delete_job(
        self,
        job_id: "capo_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_job_response.DeleteJobResponse":
        """<p>Deletes a single Job by ID.</p>

        Args:
            job_id: <p>Request to delete Job from service by Job ID.</p>
            account_id: <p>Request to delete Job from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_job_request.DeleteJobRequest]",
        ) -> OperationResponse["capo_mgn.types.delete_job_response.DeleteJobResponse"]:
            import capo_mgn._operations.application_migration_service.delete_job

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_job.delete_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_job_request.DeleteJobRequest = {"job_id": job_id}
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_jobs(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.describe_jobs_response.DescribeJobsResponse":
        """<p>Returns a list of Jobs. Use the jobIDs and fromDate and toDate filters to limit which jobs are returned. The response is sorted by creationDateTime - latest date first. Jobs are normally created by the StartTest, StartCutover, and TerminateTargetInstances APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.</p>

        Args:
            filters: <p>Request to describe Job log filters.</p>
            max_results: <p>Request to describe job log items by max results.</p>
            next_token: <p>Request to describe job log items by next token.</p>
            account_id: <p>Request to describe job log items by Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_jobs_request.DescribeJobsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_jobs_response.DescribeJobsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_jobs

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_jobs.describe_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.describe_jobs_request.DescribeJobsRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_jobs(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_jobs_request_filters.DescribeJobsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "Iterator[capo_mgn.types.job.Job]":
        _token = next_token
        while True:
            _response = self.describe_jobs(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_job_log_items(
        self,
        job_id: "capo_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse":
        """<p>Retrieves detailed job log items with paging.</p>

        Args:
            job_id: <p>Request to describe Job log job ID.</p>
            max_results: <p>Request to describe Job log item maximum results.</p>
            next_token: <p>Request to describe Job log next token.</p>
            account_id: <p>Request to describe Job log Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_job_log_items_response.DescribeJobLogItemsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_job_log_items

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_job_log_items.describe_job_log_items(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.describe_job_log_items_request.DescribeJobLogItemsRequest = {
            "job_id": job_id
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_job_log_items(
        self,
        job_id: "capo_mgn.types.job_id.JobID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "Iterator[capo_mgn.types.job_log.JobLog]":
        _token = next_token
        while True:
            _response = self.describe_job_log_items(
                job_id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_launch_configuration_template(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "capo_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional[
            "capo_mgn.types.kms_key_arn.KmsKeyArn"
        ] = None,
    ) -> "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Creates a new Launch Configuration Template.</p>

        Args:
            post_launch_actions: <p>Launch configuration template post launch actions.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            tags: <p>Request to associate tags during creation of a Launch Configuration Template.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.create_launch_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_launch_configuration_template.create_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.create_launch_configuration_template_request.CreateLaunchConfigurationTemplateRequest = {}
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if tags is not None:
            input_["tags"] = tags
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_launch_configuration_template(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        associate_public_ip_address: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        small_volume_max_size: Optional[
            "capo_mgn.types.positive_integer.PositiveInteger"
        ] = None,
        small_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        large_volume_conf: Optional[
            "capo_mgn.types.launch_template_disk_conf.LaunchTemplateDiskConf"
        ] = None,
        enable_parameters_encryption: Optional[bool] = None,
        parameters_encryption_key: Optional["capo_mgn.types.arn.ARN"] = None,
    ) -> "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate":
        """<p>Updates an existing Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>Launch Configuration Template ID.</p>
            post_launch_actions: <p>Post Launch Action to execute on the Test or Cutover instance.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration template map auto tagging MPE ID.</p>
            launch_disposition: <p>Launch disposition.</p>
            target_instance_type_right_sizing_method: <p>Target instance type right-sizing method.</p>
            copy_private_ip: <p>Copy private Ip.</p>
            associate_public_ip_address: <p>Associate public Ip address.</p>
            copy_tags: <p>Copy tags.</p>
            boot_mode: <p>Launch configuration template boot mode.</p>
            small_volume_max_size: <p>Small volume maximum size.</p>
            small_volume_conf: <p>Small volume config.</p>
            large_volume_conf: <p>Large volume config.</p>
            enable_parameters_encryption: <p>Enable parameters encryption.</p>
            parameters_encryption_key: <p>Parameters encryption key.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.update_launch_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_launch_configuration_template.update_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_launch_configuration_template_request.UpdateLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if associate_public_ip_address is not None:
            input_["associate_public_ip_address"] = associate_public_ip_address
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if small_volume_max_size is not None:
            input_["small_volume_max_size"] = small_volume_max_size
        if small_volume_conf is not None:
            input_["small_volume_conf"] = small_volume_conf
        if large_volume_conf is not None:
            input_["large_volume_conf"] = large_volume_conf
        if enable_parameters_encryption is not None:
            input_["enable_parameters_encryption"] = enable_parameters_encryption
        if parameters_encryption_key is not None:
            input_["parameters_encryption_key"] = parameters_encryption_key

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_launch_configuration_template(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse":
        """<p>Deletes a single Launch Configuration Template by ID.</p>

        Args:
            launch_configuration_template_id: <p>ID of resource to be deleted.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_launch_configuration_template_response.DeleteLaunchConfigurationTemplateResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_launch_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_launch_configuration_template.delete_launch_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_launch_configuration_template_request.DeleteLaunchConfigurationTemplateRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_launch_configuration_templates(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_mgn.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse":
        """<p>Lists all Launch Configuration Templates, filtered by Launch Configuration Template IDs</p>

        Args:
            launch_configuration_template_i_ds: <p>Request to filter Launch Configuration Templates list by Launch Configuration Template ID.</p>
            max_results: <p>Maximum results to be returned in DescribeLaunchConfigurationTemplates.</p>
            next_token: <p>Next pagination token returned from DescribeLaunchConfigurationTemplates.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_launch_configuration_templates_response.DescribeLaunchConfigurationTemplatesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_launch_configuration_templates

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_launch_configuration_templates.describe_launch_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.describe_launch_configuration_templates_request.DescribeLaunchConfigurationTemplatesRequest = {}
        if launch_configuration_template_i_ds is not None:
            input_["launch_configuration_template_i_ds"] = (
                launch_configuration_template_i_ds
            )
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

    def iter_describe_launch_configuration_templates(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        launch_configuration_template_i_ds: Optional[
            "capo_mgn.types.launch_configuration_template_i_ds.LaunchConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.launch_configuration_template.LaunchConfigurationTemplate]":
        _token = next_token
        while True:
            _response = self.describe_launch_configuration_templates(
                config_overrides=config_overrides,
                launch_configuration_template_i_ds=launch_configuration_template_i_ds,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_template_actions(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_template_actions_response.ListTemplateActionsResponse":
        """<p>List template post migration custom actions.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            filters: <p>Filters to apply when listing template post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing template post migration custom actions.</p>
            next_token: <p>Next token to use when listing template post migration custom actions.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_template_actions_request.ListTemplateActionsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_template_actions_response.ListTemplateActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_template_actions

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_template_actions.list_template_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_template_actions_request.ListTemplateActionsRequest = {
            "launch_configuration_template_id": launch_configuration_template_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_template_actions(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.template_actions_request_filters.TemplateActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.template_action_document.TemplateActionDocument]":
        _token = next_token
        while True:
            _response = self.list_template_actions(
                launch_configuration_template_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_template_action(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_name: "capo_mgn.types.bounded_string.BoundedString",
        document_identifier: "capo_mgn.types.bounded_string.BoundedString",
        order: "capo_mgn.types.order_type.OrderType",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        document_version: Optional[
            "capo_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        operating_system: Optional[
            "capo_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
        external_parameters: Optional[
            "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "capo_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["capo_mgn.types.action_category.ActionCategory"] = None,
    ) -> "capo_mgn.types.template_action_document.TemplateActionDocument":
        """<p>Put template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID.</p>
            action_name: <p>Template post migration custom action name.</p>
            document_identifier: <p>Template post migration custom action document identifier.</p>
            order: <p>Template post migration custom action order.</p>
            action_id: <p>Template post migration custom action ID.</p>
            document_version: <p>Template post migration custom action document version.</p>
            active: <p>Template post migration custom action active status.</p>
            timeout_seconds: <p>Template post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Template post migration custom action must succeed for cutover.</p>
            parameters: <p>Template post migration custom action parameters.</p>
            operating_system: <p>Operating system eligible for this template post migration custom action.</p>
            external_parameters: <p>Template post migration custom action external parameters.</p>
            description: <p>Template post migration custom action description.</p>
            category: <p>Template post migration custom action category.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.put_template_action_request.PutTemplateActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.template_action_document.TemplateActionDocument"
        ]:
            import capo_mgn._operations.application_migration_service.put_template_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.put_template_action.put_template_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.put_template_action_request.PutTemplateActionRequest = {
            "launch_configuration_template_id": launch_configuration_template_id,
            "action_name": action_name,
            "document_identifier": document_identifier,
            "order": order,
            "action_id": action_id,
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if operating_system is not None:
            input_["operating_system"] = operating_system
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_template_action(
        self,
        launch_configuration_template_id: "capo_mgn.types.launch_configuration_template_id.LaunchConfigurationTemplateID",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.remove_template_action_response.RemoveTemplateActionResponse":
        """<p>Remove template post migration custom action.</p>

        Args:
            launch_configuration_template_id: <p>Launch configuration template ID of the post migration custom action to remove.</p>
            action_id: <p>Template post migration custom action ID to remove.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.remove_template_action_request.RemoveTemplateActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.remove_template_action_response.RemoveTemplateActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.remove_template_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.remove_template_action.remove_template_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.remove_template_action_request.RemoveTemplateActionRequest = {
            "launch_configuration_template_id": launch_configuration_template_id,
            "action_id": action_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_network_migration_definition(
        self,
        name: "capo_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName",
        target_s3_configuration: "capo_mgn.types.target_s3_configuration.TargetS3Configuration",
        target_network: "capo_mgn.types.target_network.TargetNetwork",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional[
            "capo_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
        ] = None,
        source_configurations: Optional[
            "capo_mgn.types.source_configuration_list.SourceConfigurationList"
        ] = None,
        target_deployment: Optional[
            "capo_mgn.types.target_deployment.TargetDeployment"
        ] = None,
        vpc_provisioning_strategy: Optional[
            "capo_mgn.types.vpc_provisioning_strategy.VpcProvisioningStrategy"
        ] = None,
        cidr_mappings: Optional[
            "capo_mgn.types.cidr_mappings_list.CidrMappingsList"
        ] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        scope_tags: Optional["capo_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "capo_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Creates a new network migration definition that specifies the source and target network configuration for a migration.</p>

        Args:
            name: <p>The name of the network migration definition.</p>
            description: <p>A description of the network migration definition.</p>
            source_configurations: <p>A list of source configurations for the network migration.</p>
            target_s3_configuration: <p>The S3 configuration for storing the target network artifacts.</p>
            target_network: <p>The target network configuration including topology and CIDR ranges.</p>
            target_deployment: <p>The target deployment configuration for the migrated network.</p>
            vpc_provisioning_strategy: <p>Specifies whether to create new target VPCs or use existing ones. Set to <code>CREATE_NEW</code> to provision new target VPCs as part of the migration, or <code>USE_EXISTING</code> to migrate into existing VPCs in the target account.</p>
            cidr_mappings: <p>A list of CIDR mappings that map original source CIDR ranges to updated target CIDR ranges. CIDR mappings can be provided only when <code>vpcProvisioningStrategy</code> is set to <code>USE_EXISTING</code>.</p>
            tags: <p>Tags to assign to the network migration definition.</p>
            scope_tags: <p>Scope tags for the network migration definition to control access and organization.</p>

        Raises:
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample CreateNetworkMigrationDefinition call

            >>> client.create_network_migration_definition(name='network1', description='network 1 description', target_deployment='SINGLE_ACCOUNT', source_configurations=[{'sourceEnvironment': 'NSX', 'sourceS3Configuration': {'s3Bucket': 'source_bucket', 's3Key': 'source_key', 's3BucketOwner': '012345678901'}}], target_s3_configuration={'s3Bucket': 'target_bucket', 's3BucketOwner': '012345678901'}, target_network={'topology': 'ISOLATED_VPC', 'inboundCidr': '192.168.1.0/24'})
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_network_migration_definition_request.CreateNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import capo_mgn._operations.application_migration_service.create_network_migration_definition

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_network_migration_definition.create_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.create_network_migration_definition_request.CreateNetworkMigrationDefinitionRequest = {
            "name": name,
            "target_s3_configuration": target_s3_configuration,
            "target_network": target_network,
        }
        if description is not None:
            input_["description"] = description
        if source_configurations is not None:
            input_["source_configurations"] = source_configurations
        if target_deployment is not None:
            input_["target_deployment"] = target_deployment
        if vpc_provisioning_strategy is not None:
            input_["vpc_provisioning_strategy"] = vpc_provisioning_strategy
        if cidr_mappings is not None:
            input_["cidr_mappings"] = cidr_mappings
        if tags is not None:
            input_["tags"] = tags
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_network_migration_definition(
        self,
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional[
            "capo_mgn.types.network_migration_definition_name.NetworkMigrationDefinitionName"
        ] = None,
        description: Optional[
            "capo_mgn.types.network_migration_definition_description.NetworkMigrationDefinitionDescription"
        ] = None,
        source_configurations: Optional[
            "capo_mgn.types.source_configuration_list.SourceConfigurationList"
        ] = None,
        target_s3_configuration: Optional[
            "capo_mgn.types.target_s3_configuration_update.TargetS3ConfigurationUpdate"
        ] = None,
        target_network: Optional[
            "capo_mgn.types.target_network_update.TargetNetworkUpdate"
        ] = None,
        target_deployment: Optional[
            "capo_mgn.types.target_deployment.TargetDeployment"
        ] = None,
        vpc_provisioning_strategy: Optional[
            "capo_mgn.types.vpc_provisioning_strategy.VpcProvisioningStrategy"
        ] = None,
        cidr_mappings: Optional[
            "capo_mgn.types.cidr_mappings_list.CidrMappingsList"
        ] = None,
        scope_tags: Optional["capo_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> "capo_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Updates an existing network migration definition with new source or target configurations.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to update.</p>
            name: <p>The updated name of the network migration definition.</p>
            description: <p>The updated description of the network migration definition.</p>
            source_configurations: <p>The updated list of source configurations.</p>
            target_s3_configuration: <p>The updated S3 configuration for storing the target network artifacts.</p>
            target_network: <p>The updated target network configuration.</p>
            target_deployment: <p>The updated target deployment configuration.</p>
            vpc_provisioning_strategy: <p>Updates whether the migration creates new target VPCs or uses existing ones. Set to <code>USE_EXISTING</code> to migrate into existing VPCs in the target account, or to <code>CREATE_NEW</code> to provision new target VPCs.</p>
            cidr_mappings: <p>The updated list of CIDR mappings that map original source CIDR ranges to updated target CIDR ranges. CIDR mappings can be provided only when <code>vpcProvisioningStrategy</code> is set to <code>USE_EXISTING</code>.</p>
            scope_tags: <p>The updated scope tags for the network migration definition.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdateNetworkMigrationDefinition call

            >>> client.update_network_migration_definition(network_migration_definition_id='nmd-01234567891234567', name='network1', description='network 1 description', source_configurations=[{'sourceEnvironment': 'NSX', 'sourceS3Configuration': {'s3Bucket': 'source_bucket', 's3Key': 'source_key', 's3BucketOwner': '012345678901'}}], target_s3_configuration={'s3Bucket': 'target_bucket', 's3BucketOwner': '012345678901'}, target_network={'topology': 'ISOLATED_VPC', 'inboundCidr': '192.168.1.0/24'})
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_network_migration_definition_request.UpdateNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import capo_mgn._operations.application_migration_service.update_network_migration_definition

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_network_migration_definition.update_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_network_migration_definition_request.UpdateNetworkMigrationDefinitionRequest = {
            "network_migration_definition_id": network_migration_definition_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if source_configurations is not None:
            input_["source_configurations"] = source_configurations
        if target_s3_configuration is not None:
            input_["target_s3_configuration"] = target_s3_configuration
        if target_network is not None:
            input_["target_network"] = target_network
        if target_deployment is not None:
            input_["target_deployment"] = target_deployment
        if vpc_provisioning_strategy is not None:
            input_["vpc_provisioning_strategy"] = vpc_provisioning_strategy
        if cidr_mappings is not None:
            input_["cidr_mappings"] = cidr_mappings
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_network_migration_definition(
        self,
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.delete_network_migration_definition_response.DeleteNetworkMigrationDefinitionResponse":
        """<p>Deletes a network migration definition. This operation removes the migration definition and all associated metadata.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to delete.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample DeleteNetworkMigrationDefinition call

            >>> client.delete_network_migration_definition(network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_network_migration_definition_request.DeleteNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_network_migration_definition_response.DeleteNetworkMigrationDefinitionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_network_migration_definition

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_network_migration_definition.delete_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_network_migration_definition_request.DeleteNetworkMigrationDefinitionRequest = {
            "network_migration_definition_id": network_migration_definition_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_network_migration_definitions(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_definitions_request_filters.ListNetworkMigrationDefinitionsRequestFilters"
        ] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
    ) -> "capo_mgn.types.list_network_migration_definitions_response.ListNetworkMigrationDefinitionsResponse":
        """<p>Lists all network migration definitions in the account, with optional filtering.</p>

        Args:
            filters: <p>Filters to apply when listing network migration definitions.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationDefinitions call

            >>> client.list_network_migration_definitions(filters={'networkMigrationDefinitionIDs': ['nmd-01234567891234567']})
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_definitions_request.ListNetworkMigrationDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_definitions_response.ListNetworkMigrationDefinitionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_definitions

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_definitions.list_network_migration_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_definitions_request.ListNetworkMigrationDefinitionsRequest = {}
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_definitions(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_definitions_request_filters.ListNetworkMigrationDefinitionsRequestFilters"
        ] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_definition_summary.NetworkMigrationDefinitionSummary]":
        _token = next_token
        while True:
            _response = self.list_network_migration_definitions(
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_network_migration_definition(
        self,
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.network_migration_definition.NetworkMigrationDefinition":
        """<p>Retrieves the details of a network migration definition including source and target configurations.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to retrieve.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetNetworkMigrationDefinition call

            >>> client.get_network_migration_definition(network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.get_network_migration_definition_request.GetNetworkMigrationDefinitionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.network_migration_definition.NetworkMigrationDefinition"
        ]:
            import capo_mgn._operations.application_migration_service.get_network_migration_definition

            output, http_response = (
                capo_mgn._operations.application_migration_service.get_network_migration_definition.get_network_migration_definition(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.get_network_migration_definition_request.GetNetworkMigrationDefinitionRequest = {
            "network_migration_definition_id": network_migration_definition_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_network_migration_mapper_segment_construct(
        self,
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        segment_id: "capo_mgn.types.segment_id.SegmentID",
        construct_id: "capo_mgn.types.construct_id.ConstructID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.get_network_migration_mapper_segment_construct_response.GetNetworkMigrationMapperSegmentConstructResponse":
        """<p>Retrieves detailed information about a specific construct within a mapper segment, including its properties and configuration data.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            segment_id: <p>The unique identifier of the mapper segment.</p>
            construct_id: <p>The unique identifier of the construct within the segment.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample GetNetworkMigrationMapperSegmentConstruct call

            >>> client.get_network_migration_mapper_segment_construct(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab', construct_id='abc45678-abcd-abcd-efab-012345678abc')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.get_network_migration_mapper_segment_construct_request.GetNetworkMigrationMapperSegmentConstructRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.get_network_migration_mapper_segment_construct_response.GetNetworkMigrationMapperSegmentConstructResponse"
        ]:
            import capo_mgn._operations.application_migration_service.get_network_migration_mapper_segment_construct

            output, http_response = (
                capo_mgn._operations.application_migration_service.get_network_migration_mapper_segment_construct.get_network_migration_mapper_segment_construct(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.get_network_migration_mapper_segment_construct_request.GetNetworkMigrationMapperSegmentConstructRequest = {
            "network_migration_definition_id": network_migration_definition_id,
            "network_migration_execution_id": network_migration_execution_id,
            "segment_id": segment_id,
            "construct_id": construct_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_network_migration_analyses(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_analyses_filters.ListNetworkMigrationAnalysesFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_analyses_response.ListNetworkMigrationAnalysesResponse":
        """<p>Lists network migration analysis jobs for a specified execution. Returns information about analysis job status and results.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution to list analyses for.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing analysis jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationAnalyses call

            >>> client.list_network_migration_analyses(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_analyses_request.ListNetworkMigrationAnalysesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_analyses_response.ListNetworkMigrationAnalysesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_analyses

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_analyses.list_network_migration_analyses(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_analyses_request.ListNetworkMigrationAnalysesRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_analyses(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_analyses_filters.ListNetworkMigrationAnalysesFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_analysis_job_details.NetworkMigrationAnalysisJobDetails]":
        _token = next_token
        while True:
            _response = self.list_network_migration_analyses(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_analysis_results(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_analysis_results_filters.ListNetworkMigrationAnalysisResultsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_analysis_results_response.ListNetworkMigrationAnalysisResultsResponse":
        """<p>Lists the results of network migration analyses, showing connectivity and compatibility findings for migrated resources.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing analysis results, such as VPC IDs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationAnalysisResults call

            >>> client.list_network_migration_analysis_results(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_analysis_results_request.ListNetworkMigrationAnalysisResultsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_analysis_results_response.ListNetworkMigrationAnalysisResultsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_analysis_results

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_analysis_results.list_network_migration_analysis_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_analysis_results_request.ListNetworkMigrationAnalysisResultsRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_analysis_results(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_analysis_results_filters.ListNetworkMigrationAnalysisResultsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_analysis_result.NetworkMigrationAnalysisResult]":
        _token = next_token
        while True:
            _response = self.list_network_migration_analysis_results(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_code_generations(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_code_generations_filters.ListNetworkMigrationCodeGenerationsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_code_generations_response.ListNetworkMigrationCodeGenerationsResponse":
        """<p>Lists network migration code generation jobs, which convert network mappings into infrastructure-as-code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing code generation jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationCodeGenerations call

            >>> client.list_network_migration_code_generations(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_code_generations_request.ListNetworkMigrationCodeGenerationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_code_generations_response.ListNetworkMigrationCodeGenerationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_code_generations

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_code_generations.list_network_migration_code_generations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_code_generations_request.ListNetworkMigrationCodeGenerationsRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_code_generations(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_code_generations_filters.ListNetworkMigrationCodeGenerationsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_code_generation_job_details.NetworkMigrationCodeGenerationJobDetails]":
        _token = next_token
        while True:
            _response = self.list_network_migration_code_generations(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_code_generation_segments(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_code_generation_segments_filters.ListNetworkMigrationCodeGenerationSegmentsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_code_generation_segments_response.ListNetworkMigrationCodeGenerationSegmentsResponse":
        """<p>Lists code generation segments, which represent individual infrastructure components generated as code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing code generation segments.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationCodeGenerationSegments call

            >>> client.list_network_migration_code_generation_segments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_code_generation_segments_request.ListNetworkMigrationCodeGenerationSegmentsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_code_generation_segments_response.ListNetworkMigrationCodeGenerationSegmentsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_code_generation_segments

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_code_generation_segments.list_network_migration_code_generation_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_code_generation_segments_request.ListNetworkMigrationCodeGenerationSegmentsRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_code_generation_segments(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_code_generation_segments_filters.ListNetworkMigrationCodeGenerationSegmentsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_code_generation_segment.NetworkMigrationCodeGenerationSegment]":
        _token = next_token
        while True:
            _response = self.list_network_migration_code_generation_segments(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_deployed_stacks(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_deployed_stacks_response.ListNetworkMigrationDeployedStacksResponse":
        """<p>Lists CloudFormation stacks that have been deployed as part of the network migration.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationDeployedStacks call

            >>> client.list_network_migration_deployed_stacks(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_deployed_stacks_request.ListNetworkMigrationDeployedStacksRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_deployed_stacks_response.ListNetworkMigrationDeployedStacksResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_deployed_stacks

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_deployed_stacks.list_network_migration_deployed_stacks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_deployed_stacks_request.ListNetworkMigrationDeployedStacksRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
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

    def iter_list_network_migration_deployed_stacks(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_deployed_stack_details.NetworkMigrationDeployedStackDetails]":
        _token = next_token
        while True:
            _response = self.list_network_migration_deployed_stacks(
                network_migration_execution_id,
                network_migration_definition_id,
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

    def list_network_migration_deployments(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_deployer_job_filters.ListNetworkMigrationDeployerJobFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_deployer_job_response.ListNetworkMigrationDeployerJobResponse":
        """<p>Lists network migration deployment jobs and their current status.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing deployment jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationDeployments call

            >>> client.list_network_migration_deployments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_deployments_request.ListNetworkMigrationDeploymentsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_deployer_job_response.ListNetworkMigrationDeployerJobResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_deployments

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_deployments.list_network_migration_deployments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_deployments_request.ListNetworkMigrationDeploymentsRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_deployments(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_deployer_job_filters.ListNetworkMigrationDeployerJobFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_deployer_job_details.NetworkMigrationDeployerJobDetails]":
        _token = next_token
        while True:
            _response = self.list_network_migration_deployments(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_executions(
        self,
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_execution_request_filters.ListNetworkMigrationExecutionRequestFilters"
        ] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
    ) -> "capo_mgn.types.list_network_migration_executions_response.ListNetworkMigrationExecutionsResponse":
        """<p>Lists network migration execution instances for a given definition, showing the status and progress of each execution.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition to list executions for.</p>
            filters: <p>Filters to apply when listing executions, such as status or execution ID.</p>
            next_token: <p>The token for the next page of results.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationExecutions call

            >>> client.list_network_migration_executions(network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_executions_request.ListNetworkMigrationExecutionsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_executions_response.ListNetworkMigrationExecutionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_executions

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_executions.list_network_migration_executions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_executions_request.ListNetworkMigrationExecutionsRequest = {
            "network_migration_definition_id": network_migration_definition_id
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_executions(
        self,
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_execution_request_filters.ListNetworkMigrationExecutionRequestFilters"
        ] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
    ) -> (
        "Iterator[capo_mgn.types.network_migration_execution.NetworkMigrationExecution]"
    ):
        _token = next_token
        while True:
            _response = self.list_network_migration_executions(
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_mapper_segment_constructs(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        segment_id: "capo_mgn.types.segment_id.SegmentID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mapper_segment_constructs_filters.ListNetworkMigrationMapperSegmentConstructsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_mapper_segment_constructs_response.ListNetworkMigrationMapperSegmentConstructsResponse":
        """<p>Lists constructs within a mapper segment, representing individual infrastructure components like VPCs, subnets, or security groups.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            segment_id: <p>The unique identifier of the segment to list constructs for.</p>
            filters: <p>Filters to apply when listing constructs, such as construct type or ID.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationMapperSegmentConstructs call with properties enabled

            >>> client.list_network_migration_mapper_segment_constructs(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
            Sample ListNetworkMigrationMapperSegmentConstructs call with properties disabled (default)

            >>> client.list_network_migration_mapper_segment_constructs(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_mapper_segment_constructs_request.ListNetworkMigrationMapperSegmentConstructsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_mapper_segment_constructs_response.ListNetworkMigrationMapperSegmentConstructsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_mapper_segment_constructs

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_mapper_segment_constructs.list_network_migration_mapper_segment_constructs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_mapper_segment_constructs_request.ListNetworkMigrationMapperSegmentConstructsRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
            "segment_id": segment_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_mapper_segment_constructs(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        segment_id: "capo_mgn.types.segment_id.SegmentID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mapper_segment_constructs_filters.ListNetworkMigrationMapperSegmentConstructsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_mapper_segment_construct.NetworkMigrationMapperSegmentConstruct]":
        _token = next_token
        while True:
            _response = self.list_network_migration_mapper_segment_constructs(
                network_migration_execution_id,
                network_migration_definition_id,
                segment_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_mapper_segments(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mapper_segments_filters.ListNetworkMigrationMapperSegmentsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_mapper_segments_response.ListNetworkMigrationMapperSegmentsResponse":
        """<p>Lists mapper segments, which represent logical groupings of network resources to be migrated together.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing segments.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationMapperSegments call

            >>> client.list_network_migration_mapper_segments(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_mapper_segments_request.ListNetworkMigrationMapperSegmentsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_mapper_segments_response.ListNetworkMigrationMapperSegmentsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_mapper_segments

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_mapper_segments.list_network_migration_mapper_segments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_mapper_segments_request.ListNetworkMigrationMapperSegmentsRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_mapper_segments(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mapper_segments_filters.ListNetworkMigrationMapperSegmentsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment]":
        _token = next_token
        while True:
            _response = self.list_network_migration_mapper_segments(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_mappings(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mappings_filters.ListNetworkMigrationMappingsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_mappings_response.ListNetworkMigrationMappingsResponse":
        """<p>Lists network migration mapping jobs, which analyze and create relationships between source and target network resources.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing mapping jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationMappings call

            >>> client.list_network_migration_mappings(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_mappings_request.ListNetworkMigrationMappingsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_mappings_response.ListNetworkMigrationMappingsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_mappings

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_mappings.list_network_migration_mappings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_mappings_request.ListNetworkMigrationMappingsRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_mappings(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mappings_filters.ListNetworkMigrationMappingsFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_mapping_job_details.NetworkMigrationMappingJobDetails]":
        _token = next_token
        while True:
            _response = self.list_network_migration_mappings(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_network_migration_mapping_updates(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mapping_updates_filters.ListNetworkMigrationMappingUpdatesFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.list_network_migration_mapping_updates_response.ListNetworkMigrationMappingUpdatesResponse":
        """<p>Lists mapping update jobs, which apply customer modifications to the generated network mappings.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            filters: <p>Filters to apply when listing mapping update jobs.</p>
            max_results: <p>The maximum number of results to return in a single call.</p>
            next_token: <p>The token for the next page of results.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample ListNetworkMigrationMappingUpdates call

            >>> client.list_network_migration_mapping_updates(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_network_migration_mapping_updates_request.ListNetworkMigrationMappingUpdatesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_network_migration_mapping_updates_response.ListNetworkMigrationMappingUpdatesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_network_migration_mapping_updates

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_network_migration_mapping_updates.list_network_migration_mapping_updates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_network_migration_mapping_updates_request.ListNetworkMigrationMappingUpdatesRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if filters is not None:
            input_["filters"] = filters
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

    def iter_list_network_migration_mapping_updates(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_network_migration_mapping_updates_filters.ListNetworkMigrationMappingUpdatesFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.network_migration_mapping_update_job_details.NetworkMigrationMappingUpdateJobDetails]":
        _token = next_token
        while True:
            _response = self.list_network_migration_mapping_updates(
                network_migration_execution_id,
                network_migration_definition_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def start_network_migration_analysis(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.start_network_migration_analysis_response.StartNetworkMigrationAnalysisResponse":
        """<p>Starts a network migration analysis job to evaluate connectivity and compatibility of the migration mappings.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution to analyze.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartNetworkMigrationAnalysis call

            >>> client.start_network_migration_analysis(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_network_migration_analysis_request.StartNetworkMigrationAnalysisRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_network_migration_analysis_response.StartNetworkMigrationAnalysisResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_network_migration_analysis

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_network_migration_analysis.start_network_migration_analysis(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_network_migration_analysis_request.StartNetworkMigrationAnalysisRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_network_migration_code_generation(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        code_generation_output_format_types: Optional[
            "capo_mgn.types.code_generation_output_format_types.CodeGenerationOutputFormatTypes"
        ] = None,
    ) -> "capo_mgn.types.start_network_migration_code_generation_response.StartNetworkMigrationCodeGenerationResponse":
        """<p>Starts a code generation job to convert network migration mappings into infrastructure-as-code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            code_generation_output_format_types: <p>The output format types for code generation, such as CloudFormation or Terraform.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartNetworkMigrationCodeGeneration call

            >>> client.start_network_migration_code_generation(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_network_migration_code_generation_request.StartNetworkMigrationCodeGenerationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_network_migration_code_generation_response.StartNetworkMigrationCodeGenerationResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_network_migration_code_generation

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_network_migration_code_generation.start_network_migration_code_generation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_network_migration_code_generation_request.StartNetworkMigrationCodeGenerationRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if code_generation_output_format_types is not None:
            input_["code_generation_output_format_types"] = (
                code_generation_output_format_types
            )

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_network_migration_deployment(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.start_network_migration_deployer_job_response.StartNetworkMigrationDeployerJobResponse":
        """<p>Starts a deployment job to create the target network infrastructure based on the generated code templates.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartNetworkMigrationDeployment call

            >>> client.start_network_migration_deployment(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_network_migration_deployment_request.StartNetworkMigrationDeploymentRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_network_migration_deployer_job_response.StartNetworkMigrationDeployerJobResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_network_migration_deployment

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_network_migration_deployment.start_network_migration_deployment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_network_migration_deployment_request.StartNetworkMigrationDeploymentRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_network_migration_mapping(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        security_group_mapping_strategy: Optional[
            "capo_mgn.types.security_group_mapping_strategy.SecurityGroupMappingStrategy"
        ] = None,
    ) -> "capo_mgn.types.start_network_migration_mapping_response.StartNetworkMigrationMappingResponse":
        """<p>Starts the network migration mapping process for a given network migration execution.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            security_group_mapping_strategy: <p>The security group mapping strategy to use.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartNetworkMigrationMapping call

            >>> client.start_network_migration_mapping(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_network_migration_mapping_request.StartNetworkMigrationMappingRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_network_migration_mapping_response.StartNetworkMigrationMappingResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_network_migration_mapping

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_network_migration_mapping.start_network_migration_mapping(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_network_migration_mapping_request.StartNetworkMigrationMappingRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if security_group_mapping_strategy is not None:
            input_["security_group_mapping_strategy"] = security_group_mapping_strategy

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_network_migration_mapping_update(
        self,
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        constructs: Optional[
            "capo_mgn.types.start_network_migration_mapping_update_constructs.StartNetworkMigrationMappingUpdateConstructs"
        ] = None,
        segments: Optional[
            "capo_mgn.types.start_network_migration_mapping_update_segments.StartNetworkMigrationMappingUpdateSegments"
        ] = None,
    ) -> "capo_mgn.types.start_network_migration_mapping_update_response.StartNetworkMigrationMappingUpdateResponse":
        """<p>Starts a job to apply customer modifications to network migration mappings, such as changing properties.</p>

        Args:
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            constructs: <p>A list of construct updates to apply.</p>
            segments: <p>A list of segment updates to apply.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.throttling_exception.ThrottlingException: <p>Reached throttling quota exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample StartNetworkMigrationMappingUpdate call

            >>> client.start_network_migration_mapping_update(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', constructs=[{'segmentID': '12345678-abcd-abcd-efab-0123456789ab', 'constructID': 'abc45678-abcd-abcd-efab-012345678abc', 'constructType': 'AWS::EC2::VPC', 'operation': {'update': {'properties': {'CidrBlock': '10.31.0.0/22'}}}}], segments=[{'segmentID': '12345678-abcd-abcd-efab-0123456789ab', 'targetAccount': '234567890123', 'scopeTags': {'key1': 'val1', 'key2': 'val2'}}])
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_network_migration_mapping_update_request.StartNetworkMigrationMappingUpdateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_network_migration_mapping_update_response.StartNetworkMigrationMappingUpdateResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_network_migration_mapping_update

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_network_migration_mapping_update.start_network_migration_mapping_update(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_network_migration_mapping_update_request.StartNetworkMigrationMappingUpdateRequest = {
            "network_migration_execution_id": network_migration_execution_id,
            "network_migration_definition_id": network_migration_definition_id,
        }
        if constructs is not None:
            input_["constructs"] = constructs
        if segments is not None:
            input_["segments"] = segments

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_network_migration_mapper_segment(
        self,
        network_migration_definition_id: "capo_mgn.types.network_migration_definition_id.NetworkMigrationDefinitionID",
        network_migration_execution_id: "capo_mgn.types.network_migration_execution_id.NetworkMigrationExecutionID",
        segment_id: "capo_mgn.types.segment_id.SegmentID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        scope_tags: Optional["capo_mgn.types.scope_tags_map.ScopeTagsMap"] = None,
    ) -> (
        "capo_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment"
    ):
        """<p>Updates a mapper segment's configuration, such as changing its scope tags.</p>

        Args:
            network_migration_definition_id: <p>The unique identifier of the network migration definition.</p>
            network_migration_execution_id: <p>The unique identifier of the network migration execution.</p>
            segment_id: <p>The unique identifier of the segment to update.</p>
            scope_tags: <p>The updated scope tags for the segment.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Sample UpdateNetworkMigrationMapperSegment call

            >>> client.update_network_migration_mapper_segment(network_migration_execution_id='01234567-abcd-abcd-abcd-0123456789ab', network_migration_definition_id='nmd-01234567891234567', segment_id='12345678-abcd-abcd-efab-0123456789ab')
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_network_migration_mapper_segment_request.UpdateNetworkMigrationMapperSegmentRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.network_migration_mapper_segment.NetworkMigrationMapperSegment"
        ]:
            import capo_mgn._operations.application_migration_service.update_network_migration_mapper_segment

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_network_migration_mapper_segment.update_network_migration_mapper_segment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_network_migration_mapper_segment_request.UpdateNetworkMigrationMapperSegmentRequest = {
            "network_migration_definition_id": network_migration_definition_id,
            "network_migration_execution_id": network_migration_execution_id,
            "segment_id": segment_id,
        }
        if scope_tags is not None:
            input_["scope_tags"] = scope_tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_replication_configuration_template(
        self,
        staging_area_subnet_id: "capo_mgn.types.subnet_id.SubnetID",
        associate_default_security_group: bool,
        replication_servers_security_groups_i_ds: "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs",
        replication_server_instance_type: "capo_mgn.types.ec2_instance_type.EC2InstanceType",
        use_dedicated_replication_server: bool,
        default_large_staging_disk_type: "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType",
        ebs_encryption: "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption",
        bandwidth_throttling: "capo_mgn.types.bandwidth_throttling.BandwidthThrottling",
        data_plane_routing: "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting",
        create_public_ip: bool,
        staging_area_tags: "capo_mgn.types.tags_map.TagsMap",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        use_fips_endpoint: Optional[bool] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Creates a new ReplicationConfigurationTemplate.</p>

        Args:
            staging_area_subnet_id: <p>Request to configure the Staging Area subnet ID during Replication Settings template creation.</p>
            associate_default_security_group: <p>Request to associate the default Application Migration Service Security group with the Replication Settings template.</p>
            replication_servers_security_groups_i_ds: <p>Request to configure the Replication Server Security group ID during Replication Settings template creation.</p>
            replication_server_instance_type: <p>Request to configure the Replication Server instance type during Replication Settings template creation.</p>
            use_dedicated_replication_server: <p>Request to use Dedicated Replication Servers during Replication Settings template creation.</p>
            default_large_staging_disk_type: <p>Request to configure the default large staging disk EBS volume type during Replication Settings template creation.</p>
            ebs_encryption: <p>Request to configure EBS encryption during Replication Settings template creation.</p>
            ebs_encryption_key_arn: <p>Request to configure an EBS encryption key during Replication Settings template creation.</p>
            bandwidth_throttling: <p>Request to configure bandwidth throttling during Replication Settings template creation.</p>
            data_plane_routing: <p>Request to configure data plane routing during Replication Settings template creation.</p>
            create_public_ip: <p>Request to create Public IP during Replication Settings template creation.</p>
            staging_area_tags: <p>Request to configure Staging Area tags during Replication Settings template creation.</p>
            use_fips_endpoint: <p>Request to use Fips Endpoint during Replication Settings template creation.</p>
            tags: <p>Request to configure tags during Replication Settings template creation.</p>
            internet_protocol: <p>Request to configure the internet protocol to IPv4 or IPv6.</p>
            store_snapshot_on_local_zone: <p>Request to store snapshot on local zone during Replication Settings template creation.</p>
            storage_configuration: <p>Request to configure storage during Replication Settings template creation.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.create_replication_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_replication_configuration_template.create_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.create_replication_configuration_template_request.CreateReplicationConfigurationTemplateRequest = {
            "staging_area_subnet_id": staging_area_subnet_id,
            "associate_default_security_group": associate_default_security_group,
            "replication_servers_security_groups_i_ds": replication_servers_security_groups_i_ds,
            "replication_server_instance_type": replication_server_instance_type,
            "use_dedicated_replication_server": use_dedicated_replication_server,
            "default_large_staging_disk_type": default_large_staging_disk_type,
            "ebs_encryption": ebs_encryption,
            "bandwidth_throttling": bandwidth_throttling,
            "data_plane_routing": data_plane_routing,
            "create_public_ip": create_public_ip,
            "staging_area_tags": staging_area_tags,
        }
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if tags is not None:
            input_["tags"] = tags
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_replication_configuration_template(
        self,
        replication_configuration_template_id: "capo_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        arn: Optional["capo_mgn.types.arn.ARN"] = None,
        staging_area_subnet_id: Optional["capo_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        ebs_encryption: Optional[
            "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate":
        """<p>Updates a ReplicationConfigurationTemplate by ID.</p>

        Args:
            replication_configuration_template_id: <p>Update replication configuration template template ID request.</p>
            arn: <p>Update replication configuration template ARN request.</p>
            staging_area_subnet_id: <p>Update replication configuration template Staging Area subnet ID request.</p>
            associate_default_security_group: <p>Update replication configuration template associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration template Replication Server Security groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration template Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration template use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration template use default large Staging Disk type request.</p>
            ebs_encryption: <p>Update replication configuration template EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration template EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration template bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration template data plane routing request.</p>
            create_public_ip: <p>Update replication configuration template create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration template Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration template use Fips Endpoint request.</p>
            internet_protocol: <p>Update replication configuration template internet protocol request.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration template store snapshot on local zone request.</p>
            storage_configuration: <p>Update replication configuration template storage configuration request.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate"
        ]:
            import capo_mgn._operations.application_migration_service.update_replication_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_replication_configuration_template.update_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_replication_configuration_template_request.UpdateReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
        }
        if arn is not None:
            input_["arn"] = arn
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_replication_configuration_template(
        self,
        replication_configuration_template_id: "capo_mgn.types.replication_configuration_template_id.ReplicationConfigurationTemplateID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> "capo_mgn.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse":
        """<p>Deletes a single Replication Configuration Template by ID</p>

        Args:
            replication_configuration_template_id: <p>Request to delete Replication Configuration Template from service by Replication Configuration Template ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_replication_configuration_template_response.DeleteReplicationConfigurationTemplateResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_replication_configuration_template

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_replication_configuration_template.delete_replication_configuration_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_replication_configuration_template_request.DeleteReplicationConfigurationTemplateRequest = {
            "replication_configuration_template_id": replication_configuration_template_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_replication_configuration_templates(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_mgn.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse":
        """<p>Lists all ReplicationConfigurationTemplates, filtered by replication configuration template IDs.</p>

        Args:
            replication_configuration_template_i_ds: <p>Request to describe Replication Configuration template by template IDs.</p>
            max_results: <p>Request to describe Replication Configuration template by max results.</p>
            next_token: <p>Request to describe Replication Configuration template by next token.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_replication_configuration_templates_response.DescribeReplicationConfigurationTemplatesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_replication_configuration_templates

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_replication_configuration_templates.describe_replication_configuration_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.describe_replication_configuration_templates_request.DescribeReplicationConfigurationTemplatesRequest = {}
        if replication_configuration_template_i_ds is not None:
            input_["replication_configuration_template_i_ds"] = (
                replication_configuration_template_i_ds
            )
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

    def iter_describe_replication_configuration_templates(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        replication_configuration_template_i_ds: Optional[
            "capo_mgn.types.replication_configuration_template_i_ds.ReplicationConfigurationTemplateIDs"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.replication_configuration_template.ReplicationConfigurationTemplate]":
        _token = next_token
        while True:
            _response = self.describe_replication_configuration_templates(
                config_overrides=config_overrides,
                replication_configuration_template_i_ds=replication_configuration_template_i_ds,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_source_server(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
        connector_action: Optional[
            "capo_mgn.types.source_server_connector_action.SourceServerConnectorAction"
        ] = None,
        user_provided_id: Optional[
            "capo_mgn.types.user_provided_id.UserProvidedId"
        ] = None,
        fqdn_for_action_framework: Optional[
            "capo_mgn.types.fqdn_for_action_framework.FqdnForActionFramework"
        ] = None,
        platform: Optional[
            "capo_mgn.types.operating_system_string.OperatingSystemString"
        ] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Update Source Server.</p>

        Args:
            account_id: <p>Update Source Server request account ID.</p>
            source_server_id: <p>Update Source Server request source server ID.</p>
            connector_action: <p>Update Source Server request connector action.</p>
            user_provided_id: <p>Update Source Server request user provided ID.</p>
            fqdn_for_action_framework: <p>Update Source Server request FQDN for action framework.</p>
            platform: <p>Update Source Server request platform operating system.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_source_server_request.UpdateSourceServerRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.update_source_server

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_source_server.update_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_source_server_request.UpdateSourceServerRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id
        if connector_action is not None:
            input_["connector_action"] = connector_action
        if user_provided_id is not None:
            input_["user_provided_id"] = user_provided_id
        if fqdn_for_action_framework is not None:
            input_["fqdn_for_action_framework"] = fqdn_for_action_framework
        if platform is not None:
            input_["platform"] = platform

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_source_server(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_source_server_response.DeleteSourceServerResponse":
        """<p>Deletes a single source server by ID.</p>

        Args:
            source_server_id: <p>Request to delete Source Server from service by Server ID.</p>
            account_id: <p>Request to delete Source Server from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_source_server_request.DeleteSourceServerRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_source_server_response.DeleteSourceServerResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_source_server

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_source_server.delete_source_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_source_server_request.DeleteSourceServerRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_source_servers(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> (
        "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
    ):
        """<p>Retrieves all SourceServers or multiple SourceServers by ID.</p>

        Args:
            filters: <p>Request to filter Source Servers list.</p>
            max_results: <p>Request to filter Source Servers list by maximum results.</p>
            next_token: <p>Request to filter Source Servers list by next token.</p>
            account_id: <p>Request to filter Source Servers list by Account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_source_servers_request.DescribeSourceServersRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_source_servers_response.DescribeSourceServersResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_source_servers

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_source_servers.describe_source_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.describe_source_servers_request.DescribeSourceServersRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_source_servers(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.describe_source_servers_request_filters.DescribeSourceServersRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "Iterator[capo_mgn.types.source_server.SourceServer]":
        _token = next_token
        while True:
            _response = self.describe_source_servers(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def change_server_life_cycle_state(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        life_cycle: "capo_mgn.types.change_server_life_cycle_state_source_server_lifecycle.ChangeServerLifeCycleStateSourceServerLifecycle",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Allows the user to set the SourceServer.LifeCycle.state property for specific Source Server IDs to one of the following: READY_FOR_TEST or READY_FOR_CUTOVER. This command only works if the Source Server is already launchable (dataReplicationInfo.lagDuration is not null.)</p>

        Args:
            source_server_id: <p>The request to change the source server migration lifecycle state by source server ID.</p>
            life_cycle: <p>The request to change the source server migration lifecycle state.</p>
            account_id: <p>The request to change the source server migration account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.change_server_life_cycle_state

            output, http_response = (
                capo_mgn._operations.application_migration_service.change_server_life_cycle_state.change_server_life_cycle_state(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.change_server_life_cycle_state_request.ChangeServerLifeCycleStateRequest = {
            "source_server_id": source_server_id,
            "life_cycle": life_cycle,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disconnect_from_service(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Disconnects specific Source Servers from Application Migration Service. Data replication is stopped immediately. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. If the agent on the source server has not been prevented from communicating with Application Migration Service, then it will receive a command to uninstall itself (within approximately 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be set to DISCONNECTED; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to disconnect Source Server from service by Server ID.</p>
            account_id: <p>Request to disconnect Source Server from service by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.disconnect_from_service

            output, http_response = (
                capo_mgn._operations.application_migration_service.disconnect_from_service.disconnect_from_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.disconnect_from_service_request.DisconnectFromServiceRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def finalize_cutover(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Finalizes the cutover immediately for specific Source Servers. All AWS resources created by Application Migration Service for enabling the replication of these source servers will be terminated / deleted within 90 minutes. Launched Test or Cutover instances will NOT be terminated. The AWS Replication Agent will receive a command to uninstall itself (within 10 minutes). The following properties of the SourceServer will be changed immediately: dataReplicationInfo.dataReplicationState will be changed to DISCONNECTED; The SourceServer.lifeCycle.state will be changed to CUTOVER; The totalStorageBytes property for each of dataReplicationInfo.replicatedDisks will be set to zero; dataReplicationInfo.lagDuration and dataReplicationInfo.lagDuration will be nullified.</p>

        Args:
            source_server_id: <p>Request to finalize Cutover by Source Server ID.</p>
            account_id: <p>Request to finalize Cutover by Source Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.finalize_cutover_request.FinalizeCutoverRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.finalize_cutover

            output, http_response = (
                capo_mgn._operations.application_migration_service.finalize_cutover.finalize_cutover(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.finalize_cutover_request.FinalizeCutoverRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_launch_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Lists all LaunchConfigurations available, filtered by Source Server IDs.</p>

        Args:
            source_server_id: <p>Request to get Launch Configuration information by Source Server ID.</p>
            account_id: <p>Request to get Launch Configuration information by Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.get_launch_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.get_launch_configuration.get_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.get_launch_configuration_request.GetLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_replication_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Lists all ReplicationConfigurations, filtered by Source Server ID.</p>

        Args:
            source_server_id: <p>Request to get Replication Configuration by Source Server ID.</p>
            account_id: <p>Request to get Replication Configuration by Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.get_replication_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.get_replication_configuration.get_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.get_replication_configuration_request.GetReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_source_server_actions(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.source_server_actions_request_filters.SourceServerActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse":
        """<p>List source server post migration custom actions.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            filters: <p>Filters to apply when listing source server post migration custom actions.</p>
            max_results: <p>Maximum amount of items to return when listing source server post migration custom actions.</p>
            next_token: <p>Next token to use when listing source server post migration custom actions.</p>
            account_id: <p>Account ID to return when listing source server post migration custom actions.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.list_source_server_actions_response.ListSourceServerActionsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.list_source_server_actions

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_source_server_actions.list_source_server_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_source_server_actions_request.ListSourceServerActionsRequest = {
            "source_server_id": source_server_id
        }
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_source_server_actions(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.source_server_actions_request_filters.SourceServerActionsRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "Iterator[capo_mgn.types.source_server_action_document.SourceServerActionDocument]":
        _token = next_token
        while True:
            _response = self.list_source_server_actions(
                source_server_id,
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def mark_as_archived(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Archives specific Source Servers by setting the SourceServer.isArchived property to true for specified SourceServers by ID. This command only works for SourceServers with a lifecycle state that equals DISCONNECTED or CUTOVER.</p>

        Args:
            source_server_id: <p>Mark as archived by Source Server ID.</p>
            account_id: <p>Mark as archived by Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.mark_as_archived_request.MarkAsArchivedRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.mark_as_archived

            output, http_response = (
                capo_mgn._operations.application_migration_service.mark_as_archived.mark_as_archived(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.mark_as_archived_request.MarkAsArchivedRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def pause_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Pause Replication.</p>

        Args:
            source_server_id: <p>Pause Replication Request source server ID.</p>
            account_id: <p>Pause Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.pause_replication_request.PauseReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.pause_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.pause_replication.pause_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.pause_replication_request.PauseReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_source_server_action(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        action_name: "capo_mgn.types.action_name.ActionName",
        document_identifier: "capo_mgn.types.bounded_string.BoundedString",
        order: "capo_mgn.types.order_type.OrderType",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        document_version: Optional[
            "capo_mgn.types.document_version.DocumentVersion"
        ] = None,
        active: Optional[bool] = None,
        timeout_seconds: Optional[
            "capo_mgn.types.strictly_positive_integer.StrictlyPositiveInteger"
        ] = None,
        must_succeed_for_cutover: Optional[bool] = None,
        parameters: Optional[
            "capo_mgn.types.ssm_document_parameters.SsmDocumentParameters"
        ] = None,
        external_parameters: Optional[
            "capo_mgn.types.ssm_document_external_parameters.SsmDocumentExternalParameters"
        ] = None,
        description: Optional[
            "capo_mgn.types.action_description.ActionDescription"
        ] = None,
        category: Optional["capo_mgn.types.action_category.ActionCategory"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server_action_document.SourceServerActionDocument":
        """<p>Put source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID.</p>
            action_name: <p>Source server post migration custom action name.</p>
            document_identifier: <p>Source server post migration custom action document identifier.</p>
            order: <p>Source server post migration custom action order.</p>
            action_id: <p>Source server post migration custom action ID.</p>
            document_version: <p>Source server post migration custom action document version.</p>
            active: <p>Source server post migration custom action active status.</p>
            timeout_seconds: <p>Source server post migration custom action timeout in seconds.</p>
            must_succeed_for_cutover: <p>Source server post migration custom action must succeed for cutover.</p>
            parameters: <p>Source server post migration custom action parameters.</p>
            external_parameters: <p>Source server post migration custom action external parameters.</p>
            description: <p>Source server post migration custom action description.</p>
            category: <p>Source server post migration custom action category.</p>
            account_id: <p>Source server post migration custom account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.put_source_server_action_request.PutSourceServerActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.source_server_action_document.SourceServerActionDocument"
        ]:
            import capo_mgn._operations.application_migration_service.put_source_server_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.put_source_server_action.put_source_server_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.put_source_server_action_request.PutSourceServerActionRequest = {
            "source_server_id": source_server_id,
            "action_name": action_name,
            "document_identifier": document_identifier,
            "order": order,
            "action_id": action_id,
        }
        if document_version is not None:
            input_["document_version"] = document_version
        if active is not None:
            input_["active"] = active
        if timeout_seconds is not None:
            input_["timeout_seconds"] = timeout_seconds
        if must_succeed_for_cutover is not None:
            input_["must_succeed_for_cutover"] = must_succeed_for_cutover
        if parameters is not None:
            input_["parameters"] = parameters
        if external_parameters is not None:
            input_["external_parameters"] = external_parameters
        if description is not None:
            input_["description"] = description
        if category is not None:
            input_["category"] = category
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def remove_source_server_action(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        action_id: "capo_mgn.types.action_id.ActionID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse":
        """<p>Remove source server post migration custom action.</p>

        Args:
            source_server_id: <p>Source server ID of the post migration custom action to remove.</p>
            action_id: <p>Source server post migration custom action ID to remove.</p>
            account_id: <p>Source server post migration account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.remove_source_server_action_response.RemoveSourceServerActionResponse"
        ]:
            import capo_mgn._operations.application_migration_service.remove_source_server_action

            output, http_response = (
                capo_mgn._operations.application_migration_service.remove_source_server_action.remove_source_server_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.remove_source_server_action_request.RemoveSourceServerActionRequest = {
            "source_server_id": source_server_id,
            "action_id": action_id,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def resume_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Resume Replication.</p>

        Args:
            source_server_id: <p>Resume Replication Request source server ID.</p>
            account_id: <p>Resume Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.resume_replication_request.ResumeReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.resume_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.resume_replication.resume_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.resume_replication_request.ResumeReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def retry_data_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Causes the data replication initiation sequence to begin immediately upon next Handshake for specified SourceServer IDs, regardless of when the previous initiation started. This command will not work if the SourceServer is not stalled or is in a DISCONNECTED or STOPPED state.</p>

        Args:
            source_server_id: <p>Retry data replication for Source Server ID.</p>
            account_id: <p>Retry data replication for Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.retry_data_replication_request.RetryDataReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.retry_data_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.retry_data_replication.retry_data_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.retry_data_replication_request.RetryDataReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Start replication for source server irrespective of its replication type.</p>

        Args:
            source_server_id: <p>ID of source server on which to start replication.</p>
            account_id: <p>Account ID on which to start replication.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_replication_request.StartReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.start_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_replication.start_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_replication_request.StartReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_replication(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Stop Replication.</p>

        Args:
            source_server_id: <p>Stop Replication Request source server ID.</p>
            account_id: <p>Stop Replication Request account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.stop_replication_request.StopReplicationRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.stop_replication

            output, http_response = (
                capo_mgn._operations.application_migration_service.stop_replication.stop_replication(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.stop_replication_request.StopReplicationRequest = {
            "source_server_id": source_server_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_launch_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.small_bounded_string.SmallBoundedString"] = None,
        launch_disposition: Optional[
            "capo_mgn.types.launch_disposition.LaunchDisposition"
        ] = None,
        target_instance_type_right_sizing_method: Optional[
            "capo_mgn.types.target_instance_type_right_sizing_method.TargetInstanceTypeRightSizingMethod"
        ] = None,
        copy_private_ip: Optional[bool] = None,
        copy_tags: Optional[bool] = None,
        licensing: Optional["capo_mgn.types.licensing.Licensing"] = None,
        boot_mode: Optional["capo_mgn.types.boot_mode.BootMode"] = None,
        post_launch_actions: Optional[
            "capo_mgn.types.post_launch_actions.PostLaunchActions"
        ] = None,
        enable_map_auto_tagging: Optional[bool] = None,
        map_auto_tagging_mpe_id: Optional["capo_mgn.types.tag_value.TagValue"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.launch_configuration.LaunchConfiguration":
        """<p>Updates multiple LaunchConfigurations by Source Server ID.</p> <note> <p>bootMode valid values are <code>LEGACY_BIOS | UEFI | USE_SOURCE</code> </p> </note>

        Args:
            source_server_id: <p>Update Launch configuration by Source Server ID request.</p>
            name: <p>Update Launch configuration name request.</p>
            launch_disposition: <p>Update Launch configuration launch disposition request.</p>
            target_instance_type_right_sizing_method: <p>Update Launch configuration Target instance right sizing request.</p>
            copy_private_ip: <p>Update Launch configuration copy Private IP request.</p>
            copy_tags: <p>Update Launch configuration copy Tags request.</p>
            licensing: <p>Update Launch configuration licensing request.</p>
            boot_mode: <p>Update Launch configuration boot mode request.</p>
            enable_map_auto_tagging: <p>Enable map auto tagging.</p>
            map_auto_tagging_mpe_id: <p>Launch configuration map auto tagging MPE ID.</p>
            account_id: <p>Update Launch configuration Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.launch_configuration.LaunchConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.update_launch_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_launch_configuration.update_launch_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_launch_configuration_request.UpdateLaunchConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if launch_disposition is not None:
            input_["launch_disposition"] = launch_disposition
        if target_instance_type_right_sizing_method is not None:
            input_["target_instance_type_right_sizing_method"] = (
                target_instance_type_right_sizing_method
            )
        if copy_private_ip is not None:
            input_["copy_private_ip"] = copy_private_ip
        if copy_tags is not None:
            input_["copy_tags"] = copy_tags
        if licensing is not None:
            input_["licensing"] = licensing
        if boot_mode is not None:
            input_["boot_mode"] = boot_mode
        if post_launch_actions is not None:
            input_["post_launch_actions"] = post_launch_actions
        if enable_map_auto_tagging is not None:
            input_["enable_map_auto_tagging"] = enable_map_auto_tagging
        if map_auto_tagging_mpe_id is not None:
            input_["map_auto_tagging_mpe_id"] = map_auto_tagging_mpe_id
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_replication_configuration(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.small_bounded_string.SmallBoundedString"] = None,
        staging_area_subnet_id: Optional["capo_mgn.types.subnet_id.SubnetID"] = None,
        associate_default_security_group: Optional[bool] = None,
        replication_servers_security_groups_i_ds: Optional[
            "capo_mgn.types.replication_servers_security_groups_i_ds.ReplicationServersSecurityGroupsIDs"
        ] = None,
        replication_server_instance_type: Optional[
            "capo_mgn.types.ec2_instance_type.EC2InstanceType"
        ] = None,
        use_dedicated_replication_server: Optional[bool] = None,
        default_large_staging_disk_type: Optional[
            "capo_mgn.types.replication_configuration_default_large_staging_disk_type.ReplicationConfigurationDefaultLargeStagingDiskType"
        ] = None,
        replicated_disks: Optional[
            "capo_mgn.types.replication_configuration_replicated_disks.ReplicationConfigurationReplicatedDisks"
        ] = None,
        ebs_encryption: Optional[
            "capo_mgn.types.replication_configuration_ebs_encryption.ReplicationConfigurationEbsEncryption"
        ] = None,
        ebs_encryption_key_arn: Optional["capo_mgn.types.arn.ARN"] = None,
        bandwidth_throttling: Optional[
            "capo_mgn.types.bandwidth_throttling.BandwidthThrottling"
        ] = None,
        data_plane_routing: Optional[
            "capo_mgn.types.replication_configuration_data_plane_routing.ReplicationConfigurationDataPlaneRouting"
        ] = None,
        create_public_ip: Optional[bool] = None,
        staging_area_tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        use_fips_endpoint: Optional[bool] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
        internet_protocol: Optional[
            "capo_mgn.types.internet_protocol.InternetProtocol"
        ] = None,
        store_snapshot_on_local_zone: Optional[bool] = None,
        storage_configuration: Optional[
            "capo_mgn.types.storage_configuration.StorageConfiguration"
        ] = None,
    ) -> "capo_mgn.types.replication_configuration.ReplicationConfiguration":
        """<p>Allows you to update multiple ReplicationConfigurations by Source Server ID.</p>

        Args:
            source_server_id: <p>Update replication configuration Source Server ID request.</p>
            name: <p>Update replication configuration name request.</p>
            staging_area_subnet_id: <p>Update replication configuration Staging Area subnet request.</p>
            associate_default_security_group: <p>Update replication configuration associate default Application Migration Service Security group request.</p>
            replication_servers_security_groups_i_ds: <p>Update replication configuration Replication Server Security Groups IDs request.</p>
            replication_server_instance_type: <p>Update replication configuration Replication Server instance type request.</p>
            use_dedicated_replication_server: <p>Update replication configuration use dedicated Replication Server request.</p>
            default_large_staging_disk_type: <p>Update replication configuration use default large Staging Disk type request.</p>
            replicated_disks: <p>Update replication configuration replicated disks request.</p>
            ebs_encryption: <p>Update replication configuration EBS encryption request.</p>
            ebs_encryption_key_arn: <p>Update replication configuration EBS encryption key ARN request.</p>
            bandwidth_throttling: <p>Update replication configuration bandwidth throttling request.</p>
            data_plane_routing: <p>Update replication configuration data plane routing request.</p>
            create_public_ip: <p>Update replication configuration create Public IP request.</p>
            staging_area_tags: <p>Update replication configuration Staging Area Tags request.</p>
            use_fips_endpoint: <p>Update replication configuration use Fips Endpoint.</p>
            account_id: <p>Update replication configuration Account ID request.</p>
            internet_protocol: <p>Update replication configuration internet protocol.</p>
            store_snapshot_on_local_zone: <p>Update replication configuration store snapshot on local zone.</p>
            storage_configuration: <p>Update replication configuration storage configuration.</p>

        Raises:
            capo_mgn.errors.access_denied_exception.AccessDeniedException: <p>Operation denied due to a file permission or access check error.</p>
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.replication_configuration.ReplicationConfiguration"
        ]:
            import capo_mgn._operations.application_migration_service.update_replication_configuration

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_replication_configuration.update_replication_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_replication_configuration_request.UpdateReplicationConfigurationRequest = {
            "source_server_id": source_server_id
        }
        if name is not None:
            input_["name"] = name
        if staging_area_subnet_id is not None:
            input_["staging_area_subnet_id"] = staging_area_subnet_id
        if associate_default_security_group is not None:
            input_["associate_default_security_group"] = (
                associate_default_security_group
            )
        if replication_servers_security_groups_i_ds is not None:
            input_["replication_servers_security_groups_i_ds"] = (
                replication_servers_security_groups_i_ds
            )
        if replication_server_instance_type is not None:
            input_["replication_server_instance_type"] = (
                replication_server_instance_type
            )
        if use_dedicated_replication_server is not None:
            input_["use_dedicated_replication_server"] = (
                use_dedicated_replication_server
            )
        if default_large_staging_disk_type is not None:
            input_["default_large_staging_disk_type"] = default_large_staging_disk_type
        if replicated_disks is not None:
            input_["replicated_disks"] = replicated_disks
        if ebs_encryption is not None:
            input_["ebs_encryption"] = ebs_encryption
        if ebs_encryption_key_arn is not None:
            input_["ebs_encryption_key_arn"] = ebs_encryption_key_arn
        if bandwidth_throttling is not None:
            input_["bandwidth_throttling"] = bandwidth_throttling
        if data_plane_routing is not None:
            input_["data_plane_routing"] = data_plane_routing
        if create_public_ip is not None:
            input_["create_public_ip"] = create_public_ip
        if staging_area_tags is not None:
            input_["staging_area_tags"] = staging_area_tags
        if use_fips_endpoint is not None:
            input_["use_fips_endpoint"] = use_fips_endpoint
        if account_id is not None:
            input_["account_id"] = account_id
        if internet_protocol is not None:
            input_["internet_protocol"] = internet_protocol
        if store_snapshot_on_local_zone is not None:
            input_["store_snapshot_on_local_zone"] = store_snapshot_on_local_zone
        if storage_configuration is not None:
            input_["storage_configuration"] = storage_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_source_server_replication_type(
        self,
        source_server_id: "capo_mgn.types.source_server_id.SourceServerID",
        replication_type: "capo_mgn.types.replication_type.ReplicationType",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.source_server.SourceServer":
        """<p>Allows you to change between the AGENT_BASED replication type and the SNAPSHOT_SHIPPING replication type. </p> <p>SNAPSHOT_SHIPPING should be used for agentless replication.</p>

        Args:
            source_server_id: <p>ID of source server on which to update replication type.</p>
            replication_type: <p>Replication type to which to update source server.</p>
            account_id: <p>Account ID on which to update replication type.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest]",
        ) -> OperationResponse["capo_mgn.types.source_server.SourceServer"]:
            import capo_mgn._operations.application_migration_service.update_source_server_replication_type

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_source_server_replication_type.update_source_server_replication_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_source_server_replication_type_request.UpdateSourceServerReplicationTypeRequest = {
            "source_server_id": source_server_id,
            "replication_type": replication_type,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_cutover(
        self,
        source_server_i_ds: "capo_mgn.types.start_cutover_request_source_server_i_ds.StartCutoverRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_cutover_response.StartCutoverResponse":
        """<p>Launches a Cutover Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartCutover and changes the SourceServer.lifeCycle.state property to CUTTING_OVER.</p>

        Args:
            source_server_i_ds: <p>Start Cutover by Source Server IDs.</p>
            tags: <p>Start Cutover by Tags.</p>
            account_id: <p>Start Cutover by Account IDs</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_cutover_request.StartCutoverRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.start_cutover_response.StartCutoverResponse"
        ]:
            import capo_mgn._operations.application_migration_service.start_cutover

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_cutover.start_cutover(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_cutover_request.StartCutoverRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_test(
        self,
        source_server_i_ds: "capo_mgn.types.start_test_request_source_server_i_ds.StartTestRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.start_test_response.StartTestResponse":
        """<p>Launches a Test Instance for specific Source Servers. This command starts a LAUNCH job whose initiatedBy property is StartTest and changes the SourceServer.lifeCycle.state property to TESTING.</p>

        Args:
            source_server_i_ds: <p>Start Test for Source Server IDs.</p>
            tags: <p>Start Test by Tags.</p>
            account_id: <p>Start Test for Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.start_test_request.StartTestRequest]",
        ) -> OperationResponse["capo_mgn.types.start_test_response.StartTestResponse"]:
            import capo_mgn._operations.application_migration_service.start_test

            output, http_response = (
                capo_mgn._operations.application_migration_service.start_test.start_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.start_test_request.StartTestRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def terminate_target_instances(
        self,
        source_server_i_ds: "capo_mgn.types.terminate_target_instances_request_source_server_i_ds.TerminateTargetInstancesRequestSourceServerIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse":
        """<p>Starts a job that terminates specific launched EC2 Test and Cutover instances. This command will not work for any Source Server with a lifecycle.state of TESTING, CUTTING_OVER, or CUTOVER.</p>

        Args:
            source_server_i_ds: <p>Terminate Target instance by Source Server IDs.</p>
            tags: <p>Terminate Target instance by Tags.</p>
            account_id: <p>Terminate Target instance by Account ID</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.terminate_target_instances_response.TerminateTargetInstancesResponse"
        ]:
            import capo_mgn._operations.application_migration_service.terminate_target_instances

            output, http_response = (
                capo_mgn._operations.application_migration_service.terminate_target_instances.terminate_target_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.terminate_target_instances_request.TerminateTargetInstancesRequest = {
            "source_server_i_ds": source_server_i_ds
        }
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_vcenter_client(
        self,
        vcenter_client_id: "capo_mgn.types.vcenter_client_id.VcenterClientID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
    ) -> None:
        """<p>Deletes a given vCenter client by ID.</p>

        Args:
            vcenter_client_id: <p>ID of resource to be deleted.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest]",
        ) -> OperationResponse[None]:
            import capo_mgn._operations.application_migration_service.delete_vcenter_client

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_vcenter_client.delete_vcenter_client(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_vcenter_client_request.DeleteVcenterClientRequest = {
            "vcenter_client_id": vcenter_client_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_vcenter_clients(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse":
        """<p>Returns a list of the installed vCenter clients.</p>

        Args:
            max_results: <p>Maximum results to be returned in DescribeVcenterClients.</p>
            next_token: <p>Next pagination token to be provided for DescribeVcenterClients.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.validation_exception.ValidationException: <p>Validate exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.describe_vcenter_clients_response.DescribeVcenterClientsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.describe_vcenter_clients

            output, http_response = (
                capo_mgn._operations.application_migration_service.describe_vcenter_clients.describe_vcenter_clients(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.describe_vcenter_clients_request.DescribeVcenterClientsRequest = {}
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

    def iter_describe_vcenter_clients(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
    ) -> "Iterator[capo_mgn.types.vcenter_client.VcenterClient]":
        _token = next_token
        while True:
            _response = self.describe_vcenter_clients(
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

    def create_wave(
        self,
        name: "capo_mgn.types.wave_name.WaveName",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        description: Optional["capo_mgn.types.wave_description.WaveDescription"] = None,
        tags: Optional["capo_mgn.types.tags_map.TagsMap"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Create wave.</p>

        Args:
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            tags: <p>Wave tags.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.create_wave_request.CreateWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.create_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.create_wave.create_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.create_wave_request.CreateWaveRequest = {"name": name}
        if description is not None:
            input_["description"] = description
        if tags is not None:
            input_["tags"] = tags
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.delete_wave_response.DeleteWaveResponse":
        """<p>Delete wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.delete_wave_request.DeleteWaveRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.delete_wave_response.DeleteWaveResponse"
        ]:
            import capo_mgn._operations.application_migration_service.delete_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.delete_wave.delete_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.delete_wave_request.DeleteWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_waves(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_waves_request_filters.ListWavesRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.list_waves_response.ListWavesResponse":
        """<p>Retrieves all waves or multiple waves by ID.</p>

        Args:
            filters: <p>Waves list filters.</p>
            max_results: <p>Maximum results to return when listing waves.</p>
            next_token: <p>Request next token.</p>
            account_id: <p>Request account ID.</p>

        Raises:
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.list_waves_request.ListWavesRequest]",
        ) -> OperationResponse["capo_mgn.types.list_waves_response.ListWavesResponse"]:
            import capo_mgn._operations.application_migration_service.list_waves

            output, http_response = (
                capo_mgn._operations.application_migration_service.list_waves.list_waves(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.list_waves_request.ListWavesRequest = {}
        if filters is not None:
            input_["filters"] = filters
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_waves(
        self,
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        filters: Optional[
            "capo_mgn.types.list_waves_request_filters.ListWavesRequestFilters"
        ] = None,
        max_results: Optional["capo_mgn.types.max_results_type.MaxResultsType"] = None,
        next_token: Optional["capo_mgn.types.pagination_token.PaginationToken"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "Iterator[capo_mgn.types.wave.Wave]":
        _token = next_token
        while True:
            _response = self.list_waves(
                config_overrides=config_overrides,
                filters=filters,
                max_results=max_results,
                next_token=_token,
                account_id=account_id,
            )
            _page = _resolve_path(_response, ("items",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def archive_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Archive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.archive_wave_request.ArchiveWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.archive_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.archive_wave.archive_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.archive_wave_request.ArchiveWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def associate_applications(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        application_i_ds: "capo_mgn.types.application_i_ds.ApplicationIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.associate_applications_response.AssociateApplicationsResponse":
        """<p>Associate applications to wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.associate_applications_request.AssociateApplicationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.associate_applications_response.AssociateApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.associate_applications

            output, http_response = (
                capo_mgn._operations.application_migration_service.associate_applications.associate_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.associate_applications_request.AssociateApplicationsRequest = {
            "wave_id": wave_id,
            "application_i_ds": application_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_applications(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        application_i_ds: "capo_mgn.types.application_i_ds.ApplicationIDs",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse":
        """<p>Disassociate applications from wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            application_i_ds: <p>Application IDs list.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest]",
        ) -> OperationResponse[
            "capo_mgn.types.disassociate_applications_response.DisassociateApplicationsResponse"
        ]:
            import capo_mgn._operations.application_migration_service.disassociate_applications

            output, http_response = (
                capo_mgn._operations.application_migration_service.disassociate_applications.disassociate_applications(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.disassociate_applications_request.DisassociateApplicationsRequest = {
            "wave_id": wave_id,
            "application_i_ds": application_i_ds,
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def unarchive_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Unarchive wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>The request could not be completed because it exceeded the service quota.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.unarchive_wave_request.UnarchiveWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.unarchive_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.unarchive_wave.unarchive_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.unarchive_wave_request.UnarchiveWaveRequest = {
            "wave_id": wave_id
        }
        if account_id is not None:
            input_["account_id"] = account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_wave(
        self,
        wave_id: "capo_mgn.types.wave_id.WaveID",
        *,
        config_overrides: Optional[mgnClientConfig] = None,
        name: Optional["capo_mgn.types.wave_name.WaveName"] = None,
        description: Optional["capo_mgn.types.wave_description.WaveDescription"] = None,
        account_id: Optional["capo_mgn.types.account_id.AccountID"] = None,
    ) -> "capo_mgn.types.wave.Wave":
        """<p>Update wave.</p>

        Args:
            wave_id: <p>Wave ID.</p>
            name: <p>Wave name.</p>
            description: <p>Wave description.</p>
            account_id: <p>Account ID.</p>

        Raises:
            capo_mgn.errors.conflict_exception.ConflictException: <p>The request could not be completed due to a conflict with the current state of the target resource.</p>
            capo_mgn.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found exception.</p>
            capo_mgn.errors.uninitialized_account_exception.UninitializedAccountException: <p>Uninitialized account exception.</p>
            capo_mgn.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_mgn.types.update_wave_request.UpdateWaveRequest]",
        ) -> OperationResponse["capo_mgn.types.wave.Wave"]:
            import capo_mgn._operations.application_migration_service.update_wave

            output, http_response = (
                capo_mgn._operations.application_migration_service.update_wave.update_wave(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_mgn.types.update_wave_request.UpdateWaveRequest = {
            "wave_id": wave_id
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if account_id is not None:
            input_["account_id"] = account_id

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
