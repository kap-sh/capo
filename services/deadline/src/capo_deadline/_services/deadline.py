"""Generated from Smithy shape ``com.amazonaws.deadline#Deadline``."""

import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_deadline._auth._signers
import capo_deadline._auth._sigv4
from capo_deadline._auth._identity import Credentials
from capo_deadline._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_deadline._auth._zapros_handler import AuthMiddleware
from capo_deadline._pagination import resolve_path as _resolve_path
from capo_deadline._resources.deadline.farm_resource import FarmResource
from capo_deadline._resources.deadline.license_endpoint_resource import (
    LicenseEndpointResource,
)
from capo_deadline._resources.deadline.monitor_resource import MonitorResource
from capo_deadline._services._aws_config import aws_config
from capo_deadline._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_deadline.types.aggregation_id
    import capo_deadline.types.allowed_storage_profile_ids
    import capo_deadline.types.amount_requirement_name
    import capo_deadline.types.associate_member_to_farm_request
    import capo_deadline.types.associate_member_to_farm_response
    import capo_deadline.types.associate_member_to_fleet_request
    import capo_deadline.types.associate_member_to_fleet_response
    import capo_deadline.types.associate_member_to_job_request
    import capo_deadline.types.associate_member_to_job_response
    import capo_deadline.types.associate_member_to_queue_request
    import capo_deadline.types.associate_member_to_queue_response
    import capo_deadline.types.assume_fleet_role_for_read_request
    import capo_deadline.types.assume_fleet_role_for_read_response
    import capo_deadline.types.assume_fleet_role_for_worker_request
    import capo_deadline.types.assume_fleet_role_for_worker_response
    import capo_deadline.types.assume_queue_role_for_read_request
    import capo_deadline.types.assume_queue_role_for_read_response
    import capo_deadline.types.assume_queue_role_for_user_request
    import capo_deadline.types.assume_queue_role_for_user_response
    import capo_deadline.types.assume_queue_role_for_worker_request
    import capo_deadline.types.assume_queue_role_for_worker_response
    import capo_deadline.types.attachments
    import capo_deadline.types.batch_get_job_entity_request
    import capo_deadline.types.batch_get_job_entity_response
    import capo_deadline.types.batch_get_job_identifiers
    import capo_deadline.types.batch_get_job_request
    import capo_deadline.types.batch_get_job_response
    import capo_deadline.types.batch_get_session_action_identifiers
    import capo_deadline.types.batch_get_session_action_request
    import capo_deadline.types.batch_get_session_action_response
    import capo_deadline.types.batch_get_session_identifiers
    import capo_deadline.types.batch_get_session_request
    import capo_deadline.types.batch_get_session_response
    import capo_deadline.types.batch_get_step_identifiers
    import capo_deadline.types.batch_get_step_request
    import capo_deadline.types.batch_get_step_response
    import capo_deadline.types.batch_get_task_identifiers
    import capo_deadline.types.batch_get_task_request
    import capo_deadline.types.batch_get_task_response
    import capo_deadline.types.batch_get_worker_identifiers
    import capo_deadline.types.batch_get_worker_request
    import capo_deadline.types.batch_get_worker_response
    import capo_deadline.types.batch_update_job_items
    import capo_deadline.types.batch_update_job_request
    import capo_deadline.types.batch_update_job_response
    import capo_deadline.types.batch_update_task_items
    import capo_deadline.types.batch_update_task_request
    import capo_deadline.types.batch_update_task_response
    import capo_deadline.types.budget_actions_to_add
    import capo_deadline.types.budget_actions_to_remove
    import capo_deadline.types.budget_id
    import capo_deadline.types.budget_schedule
    import capo_deadline.types.budget_status
    import capo_deadline.types.budget_summary
    import capo_deadline.types.client_token
    import capo_deadline.types.consumed_usage_limit
    import capo_deadline.types.copy_job_template_request
    import capo_deadline.types.copy_job_template_response
    import capo_deadline.types.cost_scale_factor
    import capo_deadline.types.create_budget_request
    import capo_deadline.types.create_budget_response
    import capo_deadline.types.create_farm_request
    import capo_deadline.types.create_farm_response
    import capo_deadline.types.create_fleet_request
    import capo_deadline.types.create_fleet_response
    import capo_deadline.types.create_job_request
    import capo_deadline.types.create_job_response
    import capo_deadline.types.create_job_target_task_run_status
    import capo_deadline.types.create_license_endpoint_request
    import capo_deadline.types.create_license_endpoint_response
    import capo_deadline.types.create_limit_request
    import capo_deadline.types.create_limit_response
    import capo_deadline.types.create_monitor_request
    import capo_deadline.types.create_monitor_response
    import capo_deadline.types.create_queue_environment_request
    import capo_deadline.types.create_queue_environment_response
    import capo_deadline.types.create_queue_fleet_association_request
    import capo_deadline.types.create_queue_fleet_association_response
    import capo_deadline.types.create_queue_limit_association_request
    import capo_deadline.types.create_queue_limit_association_response
    import capo_deadline.types.create_queue_request
    import capo_deadline.types.create_queue_response
    import capo_deadline.types.create_storage_profile_request
    import capo_deadline.types.create_storage_profile_response
    import capo_deadline.types.create_worker_request
    import capo_deadline.types.create_worker_response
    import capo_deadline.types.deadline_principal_type
    import capo_deadline.types.default_queue_budget_action
    import capo_deadline.types.delete_budget_request
    import capo_deadline.types.delete_budget_response
    import capo_deadline.types.delete_farm_request
    import capo_deadline.types.delete_farm_response
    import capo_deadline.types.delete_fleet_request
    import capo_deadline.types.delete_fleet_response
    import capo_deadline.types.delete_license_endpoint_request
    import capo_deadline.types.delete_license_endpoint_response
    import capo_deadline.types.delete_limit_request
    import capo_deadline.types.delete_limit_response
    import capo_deadline.types.delete_metered_product_request
    import capo_deadline.types.delete_metered_product_response
    import capo_deadline.types.delete_monitor_request
    import capo_deadline.types.delete_monitor_response
    import capo_deadline.types.delete_queue_environment_request
    import capo_deadline.types.delete_queue_environment_response
    import capo_deadline.types.delete_queue_fleet_association_request
    import capo_deadline.types.delete_queue_fleet_association_response
    import capo_deadline.types.delete_queue_limit_association_request
    import capo_deadline.types.delete_queue_limit_association_response
    import capo_deadline.types.delete_queue_request
    import capo_deadline.types.delete_queue_response
    import capo_deadline.types.delete_storage_profile_request
    import capo_deadline.types.delete_storage_profile_response
    import capo_deadline.types.delete_volume_request
    import capo_deadline.types.delete_volume_response
    import capo_deadline.types.delete_worker_request
    import capo_deadline.types.delete_worker_response
    import capo_deadline.types.description
    import capo_deadline.types.disassociate_member_from_farm_request
    import capo_deadline.types.disassociate_member_from_farm_response
    import capo_deadline.types.disassociate_member_from_fleet_request
    import capo_deadline.types.disassociate_member_from_fleet_response
    import capo_deadline.types.disassociate_member_from_job_request
    import capo_deadline.types.disassociate_member_from_job_response
    import capo_deadline.types.disassociate_member_from_queue_request
    import capo_deadline.types.disassociate_member_from_queue_response
    import capo_deadline.types.environment_template
    import capo_deadline.types.environment_template_type
    import capo_deadline.types.farm_id
    import capo_deadline.types.farm_member
    import capo_deadline.types.farm_summary
    import capo_deadline.types.file_system_locations_list
    import capo_deadline.types.fleet_configuration
    import capo_deadline.types.fleet_id
    import capo_deadline.types.fleet_ids
    import capo_deadline.types.fleet_member
    import capo_deadline.types.fleet_status
    import capo_deadline.types.fleet_summary
    import capo_deadline.types.get_budget_request
    import capo_deadline.types.get_budget_response
    import capo_deadline.types.get_farm_request
    import capo_deadline.types.get_farm_response
    import capo_deadline.types.get_fleet_request
    import capo_deadline.types.get_fleet_response
    import capo_deadline.types.get_job_request
    import capo_deadline.types.get_job_response
    import capo_deadline.types.get_license_endpoint_request
    import capo_deadline.types.get_license_endpoint_response
    import capo_deadline.types.get_limit_request
    import capo_deadline.types.get_limit_response
    import capo_deadline.types.get_monitor_request
    import capo_deadline.types.get_monitor_response
    import capo_deadline.types.get_monitor_settings_request
    import capo_deadline.types.get_monitor_settings_response
    import capo_deadline.types.get_queue_environment_request
    import capo_deadline.types.get_queue_environment_response
    import capo_deadline.types.get_queue_fleet_association_request
    import capo_deadline.types.get_queue_fleet_association_response
    import capo_deadline.types.get_queue_limit_association_request
    import capo_deadline.types.get_queue_limit_association_response
    import capo_deadline.types.get_queue_request
    import capo_deadline.types.get_queue_response
    import capo_deadline.types.get_session_action_request
    import capo_deadline.types.get_session_action_response
    import capo_deadline.types.get_session_request
    import capo_deadline.types.get_session_response
    import capo_deadline.types.get_sessions_statistics_aggregation_request
    import capo_deadline.types.get_sessions_statistics_aggregation_response
    import capo_deadline.types.get_step_request
    import capo_deadline.types.get_step_response
    import capo_deadline.types.get_storage_profile_for_queue_request
    import capo_deadline.types.get_storage_profile_for_queue_response
    import capo_deadline.types.get_storage_profile_request
    import capo_deadline.types.get_storage_profile_response
    import capo_deadline.types.get_task_request
    import capo_deadline.types.get_task_response
    import capo_deadline.types.get_volume_request
    import capo_deadline.types.get_volume_response
    import capo_deadline.types.get_worker_request
    import capo_deadline.types.get_worker_response
    import capo_deadline.types.host_configuration
    import capo_deadline.types.host_properties_request
    import capo_deadline.types.iam_role_arn
    import capo_deadline.types.identity_center_instance_arn
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.identity_store_id
    import capo_deadline.types.integer
    import capo_deadline.types.job_attachment_settings
    import capo_deadline.types.job_description_override
    import capo_deadline.types.job_entity_identifiers
    import capo_deadline.types.job_id
    import capo_deadline.types.job_member
    import capo_deadline.types.job_name
    import capo_deadline.types.job_parameter_definition
    import capo_deadline.types.job_parameters
    import capo_deadline.types.job_priority
    import capo_deadline.types.job_run_as_user
    import capo_deadline.types.job_summary
    import capo_deadline.types.job_target_task_run_status
    import capo_deadline.types.job_template
    import capo_deadline.types.job_template_type
    import capo_deadline.types.kms_key_arn
    import capo_deadline.types.license_endpoint_id
    import capo_deadline.types.license_endpoint_summary
    import capo_deadline.types.limit_id
    import capo_deadline.types.limit_summary
    import capo_deadline.types.list_available_metered_products_request
    import capo_deadline.types.list_available_metered_products_response
    import capo_deadline.types.list_budgets_request
    import capo_deadline.types.list_budgets_response
    import capo_deadline.types.list_farm_members_request
    import capo_deadline.types.list_farm_members_response
    import capo_deadline.types.list_farms_request
    import capo_deadline.types.list_farms_response
    import capo_deadline.types.list_fleet_members_request
    import capo_deadline.types.list_fleet_members_response
    import capo_deadline.types.list_fleets_request
    import capo_deadline.types.list_fleets_response
    import capo_deadline.types.list_job_members_request
    import capo_deadline.types.list_job_members_response
    import capo_deadline.types.list_job_parameter_definitions_request
    import capo_deadline.types.list_job_parameter_definitions_response
    import capo_deadline.types.list_jobs_request
    import capo_deadline.types.list_jobs_response
    import capo_deadline.types.list_license_endpoints_request
    import capo_deadline.types.list_license_endpoints_response
    import capo_deadline.types.list_limits_request
    import capo_deadline.types.list_limits_response
    import capo_deadline.types.list_metered_products_request
    import capo_deadline.types.list_metered_products_response
    import capo_deadline.types.list_monitors_request
    import capo_deadline.types.list_monitors_response
    import capo_deadline.types.list_queue_environments_request
    import capo_deadline.types.list_queue_environments_response
    import capo_deadline.types.list_queue_fleet_associations_request
    import capo_deadline.types.list_queue_fleet_associations_response
    import capo_deadline.types.list_queue_limit_associations_request
    import capo_deadline.types.list_queue_limit_associations_response
    import capo_deadline.types.list_queue_members_request
    import capo_deadline.types.list_queue_members_response
    import capo_deadline.types.list_queues_request
    import capo_deadline.types.list_queues_response
    import capo_deadline.types.list_session_actions_request
    import capo_deadline.types.list_session_actions_response
    import capo_deadline.types.list_sessions_for_worker_request
    import capo_deadline.types.list_sessions_for_worker_response
    import capo_deadline.types.list_sessions_request
    import capo_deadline.types.list_sessions_response
    import capo_deadline.types.list_step_consumers_request
    import capo_deadline.types.list_step_consumers_response
    import capo_deadline.types.list_step_dependencies_request
    import capo_deadline.types.list_step_dependencies_response
    import capo_deadline.types.list_steps_request
    import capo_deadline.types.list_steps_response
    import capo_deadline.types.list_storage_profiles_for_queue_request
    import capo_deadline.types.list_storage_profiles_for_queue_response
    import capo_deadline.types.list_storage_profiles_request
    import capo_deadline.types.list_storage_profiles_response
    import capo_deadline.types.list_tags_for_resource_request
    import capo_deadline.types.list_tags_for_resource_response
    import capo_deadline.types.list_tasks_request
    import capo_deadline.types.list_tasks_response
    import capo_deadline.types.list_volumes_request
    import capo_deadline.types.list_volumes_response
    import capo_deadline.types.list_workers_request
    import capo_deadline.types.list_workers_response
    import capo_deadline.types.max_count
    import capo_deadline.types.max_failed_tasks_count
    import capo_deadline.types.max_results
    import capo_deadline.types.max_retries_per_task
    import capo_deadline.types.max_worker_count
    import capo_deadline.types.membership_level
    import capo_deadline.types.metered_product_id
    import capo_deadline.types.metered_product_summary
    import capo_deadline.types.min_zero_max_integer
    import capo_deadline.types.monitor_id
    import capo_deadline.types.monitor_summary
    import capo_deadline.types.next_token
    import capo_deadline.types.period
    import capo_deadline.types.priority
    import capo_deadline.types.put_metered_product_request
    import capo_deadline.types.put_metered_product_response
    import capo_deadline.types.queue_environment_id
    import capo_deadline.types.queue_environment_summary
    import capo_deadline.types.queue_fleet_association_summary
    import capo_deadline.types.queue_id
    import capo_deadline.types.queue_ids
    import capo_deadline.types.queue_limit_association_summary
    import capo_deadline.types.queue_member
    import capo_deadline.types.queue_status
    import capo_deadline.types.queue_summary
    import capo_deadline.types.region
    import capo_deadline.types.required_file_system_location_names
    import capo_deadline.types.resource_name
    import capo_deadline.types.s3_location
    import capo_deadline.types.scheduling_configuration
    import capo_deadline.types.search_grouped_filter_expressions
    import capo_deadline.types.search_jobs_request
    import capo_deadline.types.search_jobs_response
    import capo_deadline.types.search_sort_expressions
    import capo_deadline.types.search_steps_request
    import capo_deadline.types.search_steps_response
    import capo_deadline.types.search_tasks_request
    import capo_deadline.types.search_tasks_response
    import capo_deadline.types.search_workers_request
    import capo_deadline.types.search_workers_response
    import capo_deadline.types.security_group_id_list
    import capo_deadline.types.session_action_id
    import capo_deadline.types.session_action_summary
    import capo_deadline.types.session_id
    import capo_deadline.types.session_lifecycle_target_status
    import capo_deadline.types.session_summary
    import capo_deadline.types.sessions_statistics_resources
    import capo_deadline.types.settings_map
    import capo_deadline.types.start_sessions_statistics_aggregation_request
    import capo_deadline.types.start_sessions_statistics_aggregation_response
    import capo_deadline.types.statistics
    import capo_deadline.types.step_consumer
    import capo_deadline.types.step_dependency
    import capo_deadline.types.step_id
    import capo_deadline.types.step_summary
    import capo_deadline.types.step_target_task_run_status
    import capo_deadline.types.storage_profile_id
    import capo_deadline.types.storage_profile_operating_system_family
    import capo_deadline.types.storage_profile_summary
    import capo_deadline.types.string
    import capo_deadline.types.string_list
    import capo_deadline.types.subdomain
    import capo_deadline.types.subnet_id_list
    import capo_deadline.types.tag_resource_request
    import capo_deadline.types.tag_resource_response
    import capo_deadline.types.tags
    import capo_deadline.types.task_id
    import capo_deadline.types.task_summary
    import capo_deadline.types.task_target_run_status
    import capo_deadline.types.timestamp
    import capo_deadline.types.timezone
    import capo_deadline.types.untag_resource_request
    import capo_deadline.types.untag_resource_response
    import capo_deadline.types.update_budget_request
    import capo_deadline.types.update_budget_response
    import capo_deadline.types.update_farm_request
    import capo_deadline.types.update_farm_response
    import capo_deadline.types.update_fleet_request
    import capo_deadline.types.update_fleet_response
    import capo_deadline.types.update_job_lifecycle_status
    import capo_deadline.types.update_job_request
    import capo_deadline.types.update_job_response
    import capo_deadline.types.update_limit_request
    import capo_deadline.types.update_limit_response
    import capo_deadline.types.update_monitor_request
    import capo_deadline.types.update_monitor_response
    import capo_deadline.types.update_monitor_settings_request
    import capo_deadline.types.update_monitor_settings_response
    import capo_deadline.types.update_queue_environment_request
    import capo_deadline.types.update_queue_environment_response
    import capo_deadline.types.update_queue_fleet_association_request
    import capo_deadline.types.update_queue_fleet_association_response
    import capo_deadline.types.update_queue_fleet_association_status
    import capo_deadline.types.update_queue_limit_association_request
    import capo_deadline.types.update_queue_limit_association_response
    import capo_deadline.types.update_queue_limit_association_status
    import capo_deadline.types.update_queue_request
    import capo_deadline.types.update_queue_response
    import capo_deadline.types.update_session_request
    import capo_deadline.types.update_session_response
    import capo_deadline.types.update_step_request
    import capo_deadline.types.update_step_response
    import capo_deadline.types.update_storage_profile_request
    import capo_deadline.types.update_storage_profile_response
    import capo_deadline.types.update_task_request
    import capo_deadline.types.update_task_response
    import capo_deadline.types.update_worker_request
    import capo_deadline.types.update_worker_response
    import capo_deadline.types.update_worker_schedule_request
    import capo_deadline.types.update_worker_schedule_response
    import capo_deadline.types.updated_session_actions
    import capo_deadline.types.updated_worker_status
    import capo_deadline.types.usage_group_by
    import capo_deadline.types.usage_statistics
    import capo_deadline.types.usage_tracking_resource
    import capo_deadline.types.volume_id
    import capo_deadline.types.volume_summary
    import capo_deadline.types.vpc_id
    import capo_deadline.types.worker_capabilities
    import capo_deadline.types.worker_id
    import capo_deadline.types.worker_session_summary
    import capo_deadline.types.worker_summary


class deadlineClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class deadlineClient:
    """A client for the ``deadline`` service.

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
        self._config = deadlineClientConfig(
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

        # resources
        self.farm_resource = FarmResource(self)
        self.license_endpoint_resource = LicenseEndpointResource(self)
        self.monitor_resource = MonitorResource(self)

    def operation_options(
        self, config_overrides: Optional[deadlineClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: deadlineClientConfig = config_overrides or {}
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

    def batch_get_job(
        self,
        identifiers: "capo_deadline.types.batch_get_job_identifiers.BatchGetJobIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.batch_get_job_response.BatchGetJobResponse":
        """<p>Retrieves multiple jobs in a single request. This is a batch version of the <code>GetJob</code> API.</p> <p>The result of getting each job is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of job identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get multiple jobs in a single request

            >>> client.batch_get_job(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_get_job_request.BatchGetJobRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_get_job_response.BatchGetJobResponse"
        ]:
            import capo_deadline._operations.deadline.batch_get_job

            output, http_response = (
                capo_deadline._operations.deadline.batch_get_job.batch_get_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_get_job_request.BatchGetJobRequest = {
            "identifiers": identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_session(
        self,
        identifiers: "capo_deadline.types.batch_get_session_identifiers.BatchGetSessionIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.batch_get_session_response.BatchGetSessionResponse":
        """<p>Retrieves multiple sessions in a single request. This is a batch version of the <code>GetSession</code> API.</p> <p>The result of getting each session is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of session identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get multiple sessions in a single request

            >>> client.batch_get_session(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionId': 'session-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionId': 'session-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_get_session_request.BatchGetSessionRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_get_session_response.BatchGetSessionResponse"
        ]:
            import capo_deadline._operations.deadline.batch_get_session

            output, http_response = (
                capo_deadline._operations.deadline.batch_get_session.batch_get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_get_session_request.BatchGetSessionRequest = {
            "identifiers": identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_session_action(
        self,
        identifiers: "capo_deadline.types.batch_get_session_action_identifiers.BatchGetSessionActionIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.batch_get_session_action_response.BatchGetSessionActionResponse":
        """<p>Retrieves multiple session actions in a single request. This is a batch version of the <code>GetSessionAction</code> API.</p> <p>The result of getting each session action is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of session action identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get multiple session actions in a single request

            >>> client.batch_get_session_action(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionActionId': 'sessionaction-1234567890abcdef1234567890abcdef-0'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'sessionActionId': 'sessionaction-1234567890abcdef1234567890abcdef-1'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_get_session_action_request.BatchGetSessionActionRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_get_session_action_response.BatchGetSessionActionResponse"
        ]:
            import capo_deadline._operations.deadline.batch_get_session_action

            output, http_response = (
                capo_deadline._operations.deadline.batch_get_session_action.batch_get_session_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_get_session_action_request.BatchGetSessionActionRequest = {
            "identifiers": identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_step(
        self,
        identifiers: "capo_deadline.types.batch_get_step_identifiers.BatchGetStepIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.batch_get_step_response.BatchGetStepResponse":
        """<p>Retrieves multiple steps in a single request. This is a batch version of the <code>GetStep</code> API.</p> <p>The result of getting each step is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of step identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get multiple steps in a single request

            >>> client.batch_get_step(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_get_step_request.BatchGetStepRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_get_step_response.BatchGetStepResponse"
        ]:
            import capo_deadline._operations.deadline.batch_get_step

            output, http_response = (
                capo_deadline._operations.deadline.batch_get_step.batch_get_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_get_step_request.BatchGetStepRequest = {
            "identifiers": identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_task(
        self,
        identifiers: "capo_deadline.types.batch_get_task_identifiers.BatchGetTaskIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.batch_get_task_response.BatchGetTaskResponse":
        """<p>Retrieves multiple tasks in a single request. This is a batch version of the <code>GetTask</code> API.</p> <p>The result of getting each task is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of task identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get multiple tasks in a single request

            >>> client.batch_get_task(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-0'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-1'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_get_task_request.BatchGetTaskRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_get_task_response.BatchGetTaskResponse"
        ]:
            import capo_deadline._operations.deadline.batch_get_task

            output, http_response = (
                capo_deadline._operations.deadline.batch_get_task.batch_get_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_get_task_request.BatchGetTaskRequest = {
            "identifiers": identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_worker(
        self,
        identifiers: "capo_deadline.types.batch_get_worker_identifiers.BatchGetWorkerIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.batch_get_worker_response.BatchGetWorkerResponse":
        """<p>Retrieves multiple workers in a single request. This is a batch version of the <code>GetWorker</code> API.</p> <p>The result of getting each worker is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            identifiers: <p>The list of worker identifiers to retrieve. You can specify up to 100 identifiers per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get multiple workers in a single request

            >>> client.batch_get_worker(identifiers=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'fleetId': 'fleet-1234567890abcdef1234567890abcdef', 'workerId': 'worker-1234567890abcdef1234567890abcdef'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'fleetId': 'fleet-1234567890abcdef1234567890abcdef', 'workerId': 'worker-234567890abcdef1234567890abcdef1'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_get_worker_request.BatchGetWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_get_worker_response.BatchGetWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.batch_get_worker

            output, http_response = (
                capo_deadline._operations.deadline.batch_get_worker.batch_get_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_get_worker_request.BatchGetWorkerRequest = {
            "identifiers": identifiers
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_job(
        self,
        jobs: "capo_deadline.types.batch_update_job_items.BatchUpdateJobItems",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
    ) -> "capo_deadline.types.batch_update_job_response.BatchUpdateJobResponse":
        """<p>Updates multiple jobs in a single request. This is a batch version of the <code>UpdateJob</code> API.</p> <p>The result of updating each job is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p> <p>When you change the status of a job to <code>ARCHIVED</code>, the job can't be scheduled or archived.</p> <important> <p>An archived job and its steps and tasks are deleted after 120 days. The job can't be recovered.</p> </important>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            jobs: <p>The list of jobs to update. You can specify up to 100 jobs per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update multiple jobs in a single request

            >>> client.batch_update_job(jobs=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'targetTaskRunStatus': 'FAILED'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-234567890abcdef1234567890abcdef1', 'targetTaskRunStatus': 'FAILED'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_update_job_request.BatchUpdateJobRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_update_job_response.BatchUpdateJobResponse"
        ]:
            import capo_deadline._operations.deadline.batch_update_job

            output, http_response = (
                capo_deadline._operations.deadline.batch_update_job.batch_update_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_update_job_request.BatchUpdateJobRequest = {
            "jobs": jobs
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

    def batch_update_task(
        self,
        tasks: "capo_deadline.types.batch_update_task_items.BatchUpdateTaskItems",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
    ) -> "capo_deadline.types.batch_update_task_response.BatchUpdateTaskResponse":
        """<p>Updates multiple tasks in a single request. This is a batch version of the <code>UpdateTask</code> API.</p> <p>The result of updating each task is reported individually in the response. Because the batch request can result in a combination of successful and unsuccessful actions, you should check for batch errors even when the call returns an HTTP status code of 200.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            tasks: <p>The list of tasks to update. You can specify up to 100 tasks per request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update multiple tasks in a single request

            >>> client.batch_update_task(tasks=[{'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-0', 'targetRunStatus': 'FAILED'}, {'farmId': 'farm-1234567890abcdef1234567890abcdef', 'queueId': 'queue-1234567890abcdef1234567890abcdef', 'jobId': 'job-1234567890abcdef1234567890abcdef', 'stepId': 'step-1234567890abcdef1234567890abcdef', 'taskId': 'task-1234567890abcdef1234567890abcdef-1', 'targetRunStatus': 'FAILED'}])
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_update_task_request.BatchUpdateTaskRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_update_task_response.BatchUpdateTaskResponse"
        ]:
            import capo_deadline._operations.deadline.batch_update_task

            output, http_response = (
                capo_deadline._operations.deadline.batch_update_task.batch_update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_update_task_request.BatchUpdateTaskRequest = {
            "tasks": tasks
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

    def create_queue_fleet_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.create_queue_fleet_association_response.CreateQueueFleetAssociationResponse":
        """<p>Creates an association between a queue and a fleet.</p>

        Args:
            farm_id: <p>The ID of the farm that the queue and fleet belong to.</p>
            queue_id: <p>The queue ID.</p>
            fleet_id: <p>The fleet ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_queue_fleet_association_request.CreateQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_queue_fleet_association_response.CreateQueueFleetAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.create_queue_fleet_association

            output, http_response = (
                capo_deadline._operations.deadline.create_queue_fleet_association.create_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_queue_fleet_association_request.CreateQueueFleetAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "fleet_id": fleet_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_queue_limit_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.create_queue_limit_association_response.CreateQueueLimitAssociationResponse":
        """<p>Associates a limit with a particular queue. After the limit is associated, all workers for jobs that specify the limit associated with the queue are subject to the limit. You can't associate two limits with the same <code>amountRequirementName</code> to the same queue.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the queue and limit to associate.</p>
            queue_id: <p>The unique identifier of the queue to associate with the limit.</p>
            limit_id: <p>The unique identifier of the limit to associate with the queue.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_queue_limit_association_request.CreateQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_queue_limit_association_response.CreateQueueLimitAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.create_queue_limit_association

            output, http_response = (
                capo_deadline._operations.deadline.create_queue_limit_association.create_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_queue_limit_association_request.CreateQueueLimitAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "limit_id": limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_queue_fleet_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_queue_fleet_association_response.DeleteQueueFleetAssociationResponse":
        """<p>Deletes a queue-fleet association.</p>

        Args:
            farm_id: <p>The farm ID of the farm that holds the queue-fleet association.</p>
            queue_id: <p>The queue ID of the queue-fleet association.</p>
            fleet_id: <p>The fleet ID of the queue-fleet association.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_queue_fleet_association_request.DeleteQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_queue_fleet_association_response.DeleteQueueFleetAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.delete_queue_fleet_association

            output, http_response = (
                capo_deadline._operations.deadline.delete_queue_fleet_association.delete_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_queue_fleet_association_request.DeleteQueueFleetAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "fleet_id": fleet_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_queue_limit_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_queue_limit_association_response.DeleteQueueLimitAssociationResponse":
        """<p>Removes the association between a queue and a limit. You must use the <code>UpdateQueueLimitAssociation</code> operation to set the status to <code>STOP_LIMIT_USAGE_AND_COMPLETE_TASKS</code> or <code>STOP_LIMIT_USAGE_AND_CANCEL_TASKS</code>. The status does not change immediately. Use the <code>GetQueueLimitAssociation</code> operation to see if the status changed to <code>STOPPED</code> before deleting the association.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the queue and limit to disassociate.</p>
            queue_id: <p>The unique identifier of the queue to disassociate.</p>
            limit_id: <p>The unique identifier of the limit to disassociate.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_queue_limit_association_request.DeleteQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_queue_limit_association_response.DeleteQueueLimitAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.delete_queue_limit_association

            output, http_response = (
                capo_deadline._operations.deadline.delete_queue_limit_association.delete_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_queue_limit_association_request.DeleteQueueLimitAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "limit_id": limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_queue_fleet_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_queue_fleet_association_response.GetQueueFleetAssociationResponse":
        """<p>Gets a queue-fleet association.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the queue-fleet association.</p>
            queue_id: <p>The queue ID for the queue-fleet association.</p>
            fleet_id: <p>The fleet ID for the queue-fleet association.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_queue_fleet_association_request.GetQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_queue_fleet_association_response.GetQueueFleetAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.get_queue_fleet_association

            output, http_response = (
                capo_deadline._operations.deadline.get_queue_fleet_association.get_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_queue_fleet_association_request.GetQueueFleetAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "fleet_id": fleet_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_queue_limit_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_queue_limit_association_response.GetQueueLimitAssociationResponse":
        """<p>Gets information about a specific association between a queue and a limit.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the associated queue and limit.</p>
            queue_id: <p>The unique identifier of the queue associated with the limit.</p>
            limit_id: <p>The unique identifier of the limit associated with the queue.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_queue_limit_association_request.GetQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_queue_limit_association_response.GetQueueLimitAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.get_queue_limit_association

            output, http_response = (
                capo_deadline._operations.deadline.get_queue_limit_association.get_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_queue_limit_association_request.GetQueueLimitAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "limit_id": limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_sessions_statistics_aggregation(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        aggregation_id: "capo_deadline.types.aggregation_id.AggregationId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.get_sessions_statistics_aggregation_response.GetSessionsStatisticsAggregationResponse":
        """<p>Gets a set of statistics for queues or farms. Before you can call the <code>GetSessionStatisticsAggregation</code> operation, you must first call the <code>StartSessionsStatisticsAggregation</code> operation. Statistics are available for 1 hour after you call the <code>StartSessionsStatisticsAggregation</code> operation.</p>

        Args:
            farm_id: <p>The identifier of the farm to include in the statistics. This should be the same as the farm ID used in the call to the <code>StartSessionsStatisticsAggregation</code> operation.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            aggregation_id: <p>The identifier returned by the <code>StartSessionsStatisticsAggregation</code> operation that identifies the aggregated statistics.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_sessions_statistics_aggregation_request.GetSessionsStatisticsAggregationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_sessions_statistics_aggregation_response.GetSessionsStatisticsAggregationResponse"
        ]:
            import capo_deadline._operations.deadline.get_sessions_statistics_aggregation

            output, http_response = (
                capo_deadline._operations.deadline.get_sessions_statistics_aggregation.get_sessions_statistics_aggregation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_sessions_statistics_aggregation_request.GetSessionsStatisticsAggregationRequest = {
            "farm_id": farm_id,
            "aggregation_id": aggregation_id,
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

    def iter_get_sessions_statistics_aggregation(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        aggregation_id: "capo_deadline.types.aggregation_id.AggregationId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.statistics.Statistics]":
        _token = next_token
        while True:
            _response = self.get_sessions_statistics_aggregation(
                farm_id,
                aggregation_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("statistics",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_available_metered_products(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_available_metered_products_response.ListAvailableMeteredProductsResponse":
        """<p>A list of the available metered products.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_available_metered_products_request.ListAvailableMeteredProductsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_available_metered_products_response.ListAvailableMeteredProductsResponse"
        ]:
            import capo_deadline._operations.deadline.list_available_metered_products

            output, http_response = (
                capo_deadline._operations.deadline.list_available_metered_products.list_available_metered_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_available_metered_products_request.ListAvailableMeteredProductsRequest = {}
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

    def iter_list_available_metered_products(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.metered_product_summary.MeteredProductSummary]":
        _token = next_token
        while True:
            _response = self.list_available_metered_products(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("metered_products",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_queue_fleet_associations(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["capo_deadline.types.queue_id.QueueId"] = None,
        fleet_id: Optional["capo_deadline.types.fleet_id.FleetId"] = None,
    ) -> "capo_deadline.types.list_queue_fleet_associations_response.ListQueueFleetAssociationsResponse":
        """<p>Lists queue-fleet associations.</p>

        Args:
            farm_id: <p>The farm ID for the queue-fleet association list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            queue_id: <p>The queue ID for the queue-fleet association list.</p>
            fleet_id: <p>The fleet ID for the queue-fleet association list.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_queue_fleet_associations_request.ListQueueFleetAssociationsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_queue_fleet_associations_response.ListQueueFleetAssociationsResponse"
        ]:
            import capo_deadline._operations.deadline.list_queue_fleet_associations

            output, http_response = (
                capo_deadline._operations.deadline.list_queue_fleet_associations.list_queue_fleet_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_queue_fleet_associations_request.ListQueueFleetAssociationsRequest = {
            "farm_id": farm_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if queue_id is not None:
            input_["queue_id"] = queue_id
        if fleet_id is not None:
            input_["fleet_id"] = fleet_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_queue_fleet_associations(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["capo_deadline.types.queue_id.QueueId"] = None,
        fleet_id: Optional["capo_deadline.types.fleet_id.FleetId"] = None,
    ) -> "Iterator[capo_deadline.types.queue_fleet_association_summary.QueueFleetAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_queue_fleet_associations(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                queue_id=queue_id,
                fleet_id=fleet_id,
            )
            _page = _resolve_path(_response, ("queue_fleet_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_queue_limit_associations(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["capo_deadline.types.queue_id.QueueId"] = None,
        limit_id: Optional["capo_deadline.types.limit_id.LimitId"] = None,
    ) -> "capo_deadline.types.list_queue_limit_associations_response.ListQueueLimitAssociationsResponse":
        """<p>Gets a list of the associations between queues and limits defined in a farm.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limits and associations.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of associations to return in each page of results.</p>
            queue_id: <p>Specifies that the operation should return only the queue limit associations for the specified queue. If you specify both the <code>queueId</code> and the <code>limitId</code>, only the specified limit is returned if it exists.</p>
            limit_id: <p>Specifies that the operation should return only the queue limit associations for the specified limit. If you specify both the <code>queueId</code> and the <code>limitId</code>, only the specified limit is returned if it exists.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_queue_limit_associations_request.ListQueueLimitAssociationsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_queue_limit_associations_response.ListQueueLimitAssociationsResponse"
        ]:
            import capo_deadline._operations.deadline.list_queue_limit_associations

            output, http_response = (
                capo_deadline._operations.deadline.list_queue_limit_associations.list_queue_limit_associations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_queue_limit_associations_request.ListQueueLimitAssociationsRequest = {
            "farm_id": farm_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if queue_id is not None:
            input_["queue_id"] = queue_id
        if limit_id is not None:
            input_["limit_id"] = limit_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_queue_limit_associations(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        queue_id: Optional["capo_deadline.types.queue_id.QueueId"] = None,
        limit_id: Optional["capo_deadline.types.limit_id.LimitId"] = None,
    ) -> "Iterator[capo_deadline.types.queue_limit_association_summary.QueueLimitAssociationSummary]":
        _token = next_token
        while True:
            _response = self.list_queue_limit_associations(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                queue_id=queue_id,
                limit_id=limit_id,
            )
            _page = _resolve_path(_response, ("queue_limit_associations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_deadline.types.string.String",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists tags for a resource.</p>

        Args:
            resource_arn: <p>The resource ARN to list tags for.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_deadline._operations.deadline.list_tags_for_resource

            output, http_response = (
                capo_deadline._operations.deadline.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_jobs(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        item_offset: "capo_deadline.types.integer.Integer",
        queue_ids: "capo_deadline.types.queue_ids.QueueIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "capo_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["capo_deadline.types.integer.Integer"] = None,
    ) -> "capo_deadline.types.search_jobs_response.SearchJobsResponse":
        """<p>Searches for jobs.</p>

        Args:
            farm_id: <p>The farm ID of the job.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            queue_ids: <p>The queue ID to use in the job search.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.search_jobs_request.SearchJobsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.search_jobs_response.SearchJobsResponse"
        ]:
            import capo_deadline._operations.deadline.search_jobs

            output, http_response = (
                capo_deadline._operations.deadline.search_jobs.search_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.search_jobs_request.SearchJobsRequest = {
            "farm_id": farm_id,
            "item_offset": item_offset,
            "queue_ids": queue_ids,
        }
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_steps(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        item_offset: "capo_deadline.types.integer.Integer",
        queue_ids: "capo_deadline.types.queue_ids.QueueIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "capo_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["capo_deadline.types.integer.Integer"] = None,
        job_id: Optional["capo_deadline.types.job_id.JobId"] = None,
    ) -> "capo_deadline.types.search_steps_response.SearchStepsResponse":
        """<p>Searches for steps.</p>

        Args:
            farm_id: <p>The farm ID to use for the step search.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            queue_ids: <p>The queue IDs in the step search.</p>
            job_id: <p>The job ID to use in the step search.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.search_steps_request.SearchStepsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.search_steps_response.SearchStepsResponse"
        ]:
            import capo_deadline._operations.deadline.search_steps

            output, http_response = (
                capo_deadline._operations.deadline.search_steps.search_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.search_steps_request.SearchStepsRequest = {
            "farm_id": farm_id,
            "item_offset": item_offset,
            "queue_ids": queue_ids,
        }
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        if page_size is not None:
            input_["page_size"] = page_size
        if job_id is not None:
            input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_tasks(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        item_offset: "capo_deadline.types.integer.Integer",
        queue_ids: "capo_deadline.types.queue_ids.QueueIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "capo_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["capo_deadline.types.integer.Integer"] = None,
        job_id: Optional["capo_deadline.types.job_id.JobId"] = None,
    ) -> "capo_deadline.types.search_tasks_response.SearchTasksResponse":
        """<p>Searches for tasks.</p>

        Args:
            farm_id: <p>The farm ID of the task.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            queue_ids: <p>The queue IDs to include in the search.</p>
            job_id: <p>The job ID for the task search.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.search_tasks_request.SearchTasksRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.search_tasks_response.SearchTasksResponse"
        ]:
            import capo_deadline._operations.deadline.search_tasks

            output, http_response = (
                capo_deadline._operations.deadline.search_tasks.search_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.search_tasks_request.SearchTasksRequest = {
            "farm_id": farm_id,
            "item_offset": item_offset,
            "queue_ids": queue_ids,
        }
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        if page_size is not None:
            input_["page_size"] = page_size
        if job_id is not None:
            input_["job_id"] = job_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def search_workers(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        item_offset: "capo_deadline.types.integer.Integer",
        fleet_ids: "capo_deadline.types.fleet_ids.FleetIds",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        filter_expressions: Optional[
            "capo_deadline.types.search_grouped_filter_expressions.SearchGroupedFilterExpressions"
        ] = None,
        sort_expressions: Optional[
            "capo_deadline.types.search_sort_expressions.SearchSortExpressions"
        ] = None,
        page_size: Optional["capo_deadline.types.integer.Integer"] = None,
    ) -> "capo_deadline.types.search_workers_response.SearchWorkersResponse":
        """<p>Searches for workers.</p>

        Args:
            farm_id: <p>The farm ID in the workers search.</p>
            filter_expressions: <p>The search terms for a resource.</p>
            sort_expressions: <p>The search terms for a resource.</p>
            item_offset: <p>The offset for the search results.</p>
            page_size: <p>Specifies the number of results to return.</p>
            fleet_ids: <p>The fleet ID of the workers to search for.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.search_workers_request.SearchWorkersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.search_workers_response.SearchWorkersResponse"
        ]:
            import capo_deadline._operations.deadline.search_workers

            output, http_response = (
                capo_deadline._operations.deadline.search_workers.search_workers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.search_workers_request.SearchWorkersRequest = {
            "farm_id": farm_id,
            "item_offset": item_offset,
            "fleet_ids": fleet_ids,
        }
        if filter_expressions is not None:
            input_["filter_expressions"] = filter_expressions
        if sort_expressions is not None:
            input_["sort_expressions"] = sort_expressions
        if page_size is not None:
            input_["page_size"] = page_size

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_sessions_statistics_aggregation(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        resource_ids: "capo_deadline.types.sessions_statistics_resources.SessionsStatisticsResources",
        start_time: "capo_deadline.types.timestamp.Timestamp",
        end_time: "capo_deadline.types.timestamp.Timestamp",
        group_by: "capo_deadline.types.usage_group_by.UsageGroupBy",
        statistics: "capo_deadline.types.usage_statistics.UsageStatistics",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        timezone: Optional["capo_deadline.types.timezone.Timezone"] = None,
        period: Optional["capo_deadline.types.period.Period"] = None,
    ) -> "capo_deadline.types.start_sessions_statistics_aggregation_response.StartSessionsStatisticsAggregationResponse":
        r"""<p>Starts an asynchronous request for getting aggregated statistics about queues and farms. Get the statistics using the <code>GetSessionsStatisticsAggregation</code> operation. You can only have one running aggregation for your Deadline Cloud farm. Call the <code>GetSessionsStatisticsAggregation</code> operation and check the <code>status</code> field to see if an aggregation is running. Statistics are available for 1 hour after you call the <code>StartSessionsStatisticsAggregation</code> operation.</p>

        Args:
            farm_id: <p>The identifier of the farm that contains queues or fleets to return statistics for.</p>
            resource_ids: <p>A list of fleet IDs or queue IDs to gather statistics for.</p>
            start_time: <p>The Linux timestamp of the date and time that the statistics start.</p>
            end_time: <p>The Linux timestamp of the date and time that the statistics end.</p>
            timezone: <p>The timezone to use for the statistics. Use UTC notation such as \"UTC+8.\"</p>
            period: <p>The period to aggregate the statistics.</p>
            group_by: <p>The field to use to group the statistics.</p>
            statistics: <p>One to four statistics to return.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.start_sessions_statistics_aggregation_request.StartSessionsStatisticsAggregationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.start_sessions_statistics_aggregation_response.StartSessionsStatisticsAggregationResponse"
        ]:
            import capo_deadline._operations.deadline.start_sessions_statistics_aggregation

            output, http_response = (
                capo_deadline._operations.deadline.start_sessions_statistics_aggregation.start_sessions_statistics_aggregation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.start_sessions_statistics_aggregation_request.StartSessionsStatisticsAggregationRequest = {
            "farm_id": farm_id,
            "resource_ids": resource_ids,
            "start_time": start_time,
            "end_time": end_time,
            "group_by": group_by,
            "statistics": statistics,
        }
        if timezone is not None:
            input_["timezone"] = timezone
        if period is not None:
            input_["period"] = period

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_deadline.types.string.String",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.tag_resource_response.TagResourceResponse":
        """<p>Tags a resource using the resource's ARN and desired tags.</p>

        Args:
            resource_arn: <p>The ARN of the resource to apply tags to.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_deadline._operations.deadline.tag_resource

            output, http_response = (
                capo_deadline._operations.deadline.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.tag_resource_request.TagResourceRequest = {
            "resource_arn": resource_arn
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

    def untag_resource(
        self,
        resource_arn: "capo_deadline.types.string.String",
        tag_keys: "capo_deadline.types.string_list.StringList",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes a tag from a resource using the resource's ARN and tag to remove.</p>

        Args:
            resource_arn: <p>The ARN of the resource to remove the tag from.</p>
            tag_keys: <p>They keys of the tag.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_deadline._operations.deadline.untag_resource

            output, http_response = (
                capo_deadline._operations.deadline.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.untag_resource_request.UntagResourceRequest = {
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

    def update_queue_fleet_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        status: "capo_deadline.types.update_queue_fleet_association_status.UpdateQueueFleetAssociationStatus",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.update_queue_fleet_association_response.UpdateQueueFleetAssociationResponse":
        """<p>Updates a queue-fleet association.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            queue_id: <p>The queue ID to update.</p>
            fleet_id: <p>The fleet ID to update.</p>
            status: <p>The status to update.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_queue_fleet_association_request.UpdateQueueFleetAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_queue_fleet_association_response.UpdateQueueFleetAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.update_queue_fleet_association

            output, http_response = (
                capo_deadline._operations.deadline.update_queue_fleet_association.update_queue_fleet_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_queue_fleet_association_request.UpdateQueueFleetAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "fleet_id": fleet_id,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_queue_limit_association(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        status: "capo_deadline.types.update_queue_limit_association_status.UpdateQueueLimitAssociationStatus",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.update_queue_limit_association_response.UpdateQueueLimitAssociationResponse":
        """<p>Updates the status of the queue. If you set the status to one of the <code>STOP_LIMIT_USAGE*</code> values, there will be a delay before the status transitions to the <code>STOPPED</code> state. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the associated queues and limits.</p>
            queue_id: <p>The unique identifier of the queue associated to the limit.</p>
            limit_id: <p>The unique identifier of the limit associated to the queue.</p>
            status: <p>Sets the status of the limit. You can mark the limit active, or you can stop usage of the limit and either complete existing tasks or cancel any existing tasks immediately. </p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_queue_limit_association_request.UpdateQueueLimitAssociationRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_queue_limit_association_response.UpdateQueueLimitAssociationResponse"
        ]:
            import capo_deadline._operations.deadline.update_queue_limit_association

            output, http_response = (
                capo_deadline._operations.deadline.update_queue_limit_association.update_queue_limit_association(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_queue_limit_association_request.UpdateQueueLimitAssociationRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "limit_id": limit_id,
            "status": status,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_farm(
        self,
        display_name: "capo_deadline.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        kms_key_arn: Optional["capo_deadline.types.kms_key_arn.KmsKeyArn"] = None,
        cost_scale_factor: Optional[
            "capo_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_farm_response.CreateFarmResponse":
        """<p>Creates a farm to allow space for queues and fleets. Farms are the space where the components of your renders gather and are pieced together in the cloud. Farms contain budgets and allow you to enforce permissions. Deadline Cloud farms are a useful container for large projects.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            kms_key_arn: <p>The ARN of the KMS key to use on the farm.</p>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment. The default value is 1.</p>
            tags: <p>The tags to add to your farm. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_farm_request.CreateFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_farm_response.CreateFarmResponse"
        ]:
            import capo_deadline._operations.deadline.create_farm

            output, http_response = (
                capo_deadline._operations.deadline.create_farm.create_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_farm_request.CreateFarmRequest = {
            "display_name": display_name
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if kms_key_arn is not None:
            input_["kms_key_arn"] = kms_key_arn
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_farm_response.GetFarmResponse":
        """<p>Get a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_farm_request.GetFarmRequest]",
        ) -> OperationResponse["capo_deadline.types.get_farm_response.GetFarmResponse"]:
            import capo_deadline._operations.deadline.get_farm

            output, http_response = (
                capo_deadline._operations.deadline.get_farm.get_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_farm_request.GetFarmRequest = {
            "farm_id": farm_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        cost_scale_factor: Optional[
            "capo_deadline.types.cost_scale_factor.CostScaleFactor"
        ] = None,
    ) -> "capo_deadline.types.update_farm_response.UpdateFarmResponse":
        """<p>Updates a farm.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            display_name: <p>The display name of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the farm to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            cost_scale_factor: <p>A multiplier applied to the farm's calculated costs for usage data and budget tracking. A value less than 1 represents a discount, a value greater than 1 represents a premium, and a value of 1 represents no adjustment.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_farm_request.UpdateFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_farm_response.UpdateFarmResponse"
        ]:
            import capo_deadline._operations.deadline.update_farm

            output, http_response = (
                capo_deadline._operations.deadline.update_farm.update_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_farm_request.UpdateFarmRequest = {
            "farm_id": farm_id
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if cost_scale_factor is not None:
            input_["cost_scale_factor"] = cost_scale_factor

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_farm_response.DeleteFarmResponse":
        """<p>Deletes a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_farm_request.DeleteFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_farm_response.DeleteFarmResponse"
        ]:
            import capo_deadline._operations.deadline.delete_farm

            output, http_response = (
                capo_deadline._operations.deadline.delete_farm.delete_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_farm_request.DeleteFarmRequest = {
            "farm_id": farm_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_farms(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "capo_deadline.types.list_farms_response.ListFarmsResponse":
        """<p>Lists farms.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal ID of the member to list on the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_farms_request.ListFarmsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_farms_response.ListFarmsResponse"
        ]:
            import capo_deadline._operations.deadline.list_farms

            output, http_response = (
                capo_deadline._operations.deadline.list_farms.list_farms(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_farms_request.ListFarmsRequest = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_farms(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "Iterator[capo_deadline.types.farm_summary.FarmSummary]":
        _token = next_token
        while True:
            _response = self.list_farms(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                principal_id=principal_id,
            )
            _page = _resolve_path(_response, ("farms",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_member_to_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "capo_deadline.types.membership_level.MembershipLevel",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
    ) -> "capo_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse":
        """<p>Assigns a farm membership level to a member.</p>

        Args:
            farm_id: <p>The ID of the farm to associate with the member.</p>
            principal_type: <p>The principal type of the member to associate with the farm.</p>
            identity_store_id: <p>The identity store ID of the member to associate with the farm.</p>
            membership_level: <p>The principal's membership level for the associated farm.</p>
            principal_id: <p>The member's principal ID to associate with the farm.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.associate_member_to_farm_response.AssociateMemberToFarmResponse"
        ]:
            import capo_deadline._operations.deadline.associate_member_to_farm

            output, http_response = (
                capo_deadline._operations.deadline.associate_member_to_farm.associate_member_to_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.associate_member_to_farm_request.AssociateMemberToFarmRequest = {
            "farm_id": farm_id,
            "principal_type": principal_type,
            "identity_store_id": identity_store_id,
            "membership_level": membership_level,
            "principal_id": principal_id,
        }
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        amount_requirement_name: "capo_deadline.types.amount_requirement_name.AmountRequirementName",
        max_count: "capo_deadline.types.max_count.MaxCount",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
    ) -> "capo_deadline.types.create_limit_response.CreateLimitResponse":
        """<p>Creates a limit that manages the distribution of shared resources, such as floating licenses. A limit can throttle work assignments, help manage workloads, and track current usage. Before you use a limit, you must associate the limit with one or more queues. </p> <p>You must add the <code>amountRequirementName</code> to a step in a job template to declare the limit requirement.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the limit.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            amount_requirement_name: <p>The value that you specify as the <code>name</code> in the <code>amounts</code> field of the <code>hostRequirements</code> in a step of a job template to declare the limit requirement.</p>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>
            description: <p>A description of the limit. A description helps you identify the purpose of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_limit_request.CreateLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_limit_response.CreateLimitResponse"
        ]:
            import capo_deadline._operations.deadline.create_limit

            output, http_response = (
                capo_deadline._operations.deadline.create_limit.create_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_limit_request.CreateLimitRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "amount_requirement_name": amount_requirement_name,
            "max_count": max_count,
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

    def create_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        os_family: "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        file_system_locations: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "capo_deadline.types.create_storage_profile_response.CreateStorageProfileResponse":
        """<p>Creates a storage profile that specifies the operating system, file type, and file location of resources used on a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the storage profile.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The type of operating system (OS) for the storage profile.</p>
            file_system_locations: <p>File system paths to include in the storage profile.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_storage_profile_response.CreateStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.create_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.create_storage_profile.create_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_storage_profile_request.CreateStorageProfileRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "os_family": os_family,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if file_system_locations is not None:
            input_["file_system_locations"] = file_system_locations

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_limit_response.DeleteLimitResponse":
        """<p>Removes a limit from the specified farm. Before you delete a limit you must use the <code>DeleteQueueLimitAssociation</code> operation to remove the association with any queues. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit to delete.</p>
            limit_id: <p>The unique identifier of the limit to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_limit_request.DeleteLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_limit_response.DeleteLimitResponse"
        ]:
            import capo_deadline._operations.deadline.delete_limit

            output, http_response = (
                capo_deadline._operations.deadline.delete_limit.delete_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_limit_request.DeleteLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse":
        """<p>Deletes a storage profile.</p>

        Args:
            farm_id: <p>The farm ID of the farm from which to remove the storage profile.</p>
            storage_profile_id: <p>The storage profile ID of the storage profile to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_storage_profile_response.DeleteStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.delete_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.delete_storage_profile.delete_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_storage_profile_request.DeleteStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_member_from_farm(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse":
        """<p>Disassociates a member from a farm.</p>

        Args:
            farm_id: <p>The farm ID of the farm to disassociate from the member.</p>
            principal_id: <p>A member's principal ID to disassociate from a farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.disassociate_member_from_farm_response.DisassociateMemberFromFarmResponse"
        ]:
            import capo_deadline._operations.deadline.disassociate_member_from_farm

            output, http_response = (
                capo_deadline._operations.deadline.disassociate_member_from_farm.disassociate_member_from_farm(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.disassociate_member_from_farm_request.DisassociateMemberFromFarmRequest = {
            "farm_id": farm_id,
            "principal_id": principal_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_limit_response.GetLimitResponse":
        """<p>Gets information about a specific limit.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to return.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_limit_request.GetLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_limit_response.GetLimitResponse"
        ]:
            import capo_deadline._operations.deadline.get_limit

            output, http_response = (
                capo_deadline._operations.deadline.get_limit.get_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_limit_request.GetLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse":
        """<p>Gets a storage profile.</p>

        Args:
            farm_id: <p>The farm ID for the storage profile.</p>
            storage_profile_id: <p>The storage profile ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_storage_profile_request.GetStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_storage_profile_response.GetStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.get_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.get_storage_profile.get_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_storage_profile_request.GetStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_farm_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_farm_members_response.ListFarmMembersResponse":
        """<p>Lists the members of a farm.</p>

        Args:
            farm_id: <p>The farm ID.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_farm_members_request.ListFarmMembersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_farm_members_response.ListFarmMembersResponse"
        ]:
            import capo_deadline._operations.deadline.list_farm_members

            output, http_response = (
                capo_deadline._operations.deadline.list_farm_members.list_farm_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_farm_members_request.ListFarmMembersRequest = {
            "farm_id": farm_id
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

    def iter_list_farm_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.farm_member.FarmMember]":
        _token = next_token
        while True:
            _response = self.list_farm_members(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_limits(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_limits_response.ListLimitsResponse":
        """<p>Gets a list of limits defined in the specified farm.</p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limits.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of limits to return in each page of results.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_limits_request.ListLimitsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_limits_response.ListLimitsResponse"
        ]:
            import capo_deadline._operations.deadline.list_limits

            output, http_response = (
                capo_deadline._operations.deadline.list_limits.list_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_limits_request.ListLimitsRequest = {
            "farm_id": farm_id
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

    def iter_list_limits(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.limit_summary.LimitSummary]":
        _token = next_token
        while True:
            _response = self.list_limits(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("limits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_storage_profiles(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
    ):
        """<p>Lists storage profiles.</p>

        Args:
            farm_id: <p>The farm ID of the storage profile.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_storage_profiles_response.ListStorageProfilesResponse"
        ]:
            import capo_deadline._operations.deadline.list_storage_profiles

            output, http_response = (
                capo_deadline._operations.deadline.list_storage_profiles.list_storage_profiles(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_storage_profiles_request.ListStorageProfilesRequest = {
            "farm_id": farm_id
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

    def iter_list_storage_profiles(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.storage_profile_summary.StorageProfileSummary]":
        _token = next_token
        while True:
            _response = self.list_storage_profiles(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("storage_profiles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_limit(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        limit_id: "capo_deadline.types.limit_id.LimitId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        max_count: Optional["capo_deadline.types.max_count.MaxCount"] = None,
    ) -> "capo_deadline.types.update_limit_response.UpdateLimitResponse":
        """<p>Updates the properties of the specified limit. </p>

        Args:
            farm_id: <p>The unique identifier of the farm that contains the limit.</p>
            limit_id: <p>The unique identifier of the limit to update.</p>
            display_name: <p>The new display name of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The new description of the limit.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            max_count: <p>The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit won't be scheduled until the resource is available.</p> <p>If more than the new maximum number is currently in use, running jobs finish but no new jobs are started until the number of resources in use is below the new maximum number.</p> <p>The <code>maxCount</code> must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_limit_request.UpdateLimitRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_limit_response.UpdateLimitResponse"
        ]:
            import capo_deadline._operations.deadline.update_limit

            output, http_response = (
                capo_deadline._operations.deadline.update_limit.update_limit(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_limit_request.UpdateLimitRequest = {
            "farm_id": farm_id,
            "limit_id": limit_id,
        }
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if max_count is not None:
            input_["max_count"] = max_count

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_storage_profile(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        os_family: Optional[
            "capo_deadline.types.storage_profile_operating_system_family.StorageProfileOperatingSystemFamily"
        ] = None,
        file_system_locations_to_add: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
        file_system_locations_to_remove: Optional[
            "capo_deadline.types.file_system_locations_list.FileSystemLocationsList"
        ] = None,
    ) -> "capo_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse":
        """<p>Updates a storage profile.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            storage_profile_id: <p>The storage profile ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the storage profile to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            os_family: <p>The OS system to update.</p>
            file_system_locations_to_add: <p>The file system location names to add.</p>
            file_system_locations_to_remove: <p>The file system location names to remove.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_storage_profile_response.UpdateStorageProfileResponse"
        ]:
            import capo_deadline._operations.deadline.update_storage_profile

            output, http_response = (
                capo_deadline._operations.deadline.update_storage_profile.update_storage_profile(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_storage_profile_request.UpdateStorageProfileRequest = {
            "farm_id": farm_id,
            "storage_profile_id": storage_profile_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if os_family is not None:
            input_["os_family"] = os_family
        if file_system_locations_to_add is not None:
            input_["file_system_locations_to_add"] = file_system_locations_to_add
        if file_system_locations_to_remove is not None:
            input_["file_system_locations_to_remove"] = file_system_locations_to_remove

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_budget(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        usage_tracking_resource: "capo_deadline.types.usage_tracking_resource.UsageTrackingResource",
        approximate_dollar_limit: "capo_deadline.types.consumed_usage_limit.ConsumedUsageLimit",
        actions: "capo_deadline.types.budget_actions_to_add.BudgetActionsToAdd",
        schedule: "capo_deadline.types.budget_schedule.BudgetSchedule",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_budget_response.CreateBudgetResponse":
        """<p>Creates a budget to set spending thresholds for your rendering activity.</p>

        Args:
            farm_id: <p>The farm ID to include in this budget.</p>
            display_name: <p>The display name of the budget.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the budget.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            usage_tracking_resource: <p>The queue ID provided to this budget to track usage.</p>
            approximate_dollar_limit: <p>The dollar limit based on consumed usage.</p>
            actions: <p>The budget actions to specify what happens when the budget runs out.</p>
            schedule: <p>The schedule to associate with this budget.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_budget_request.CreateBudgetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_budget_response.CreateBudgetResponse"
        ]:
            import capo_deadline._operations.deadline.create_budget

            output, http_response = (
                capo_deadline._operations.deadline.create_budget.create_budget(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_budget_request.CreateBudgetRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "usage_tracking_resource": usage_tracking_resource,
            "approximate_dollar_limit": approximate_dollar_limit,
            "actions": actions,
            "schedule": schedule,
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

    def get_budget(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        budget_id: "capo_deadline.types.budget_id.BudgetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_budget_response.GetBudgetResponse":
        """<p>Get a budget.</p>

        Args:
            farm_id: <p>The farm ID of the farm connected to the budget.</p>
            budget_id: <p>The budget ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_budget_request.GetBudgetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_budget_response.GetBudgetResponse"
        ]:
            import capo_deadline._operations.deadline.get_budget

            output, http_response = (
                capo_deadline._operations.deadline.get_budget.get_budget(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_budget_request.GetBudgetRequest = {
            "farm_id": farm_id,
            "budget_id": budget_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_budget(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        budget_id: "capo_deadline.types.budget_id.BudgetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        status: Optional["capo_deadline.types.budget_status.BudgetStatus"] = None,
        approximate_dollar_limit: Optional[
            "capo_deadline.types.consumed_usage_limit.ConsumedUsageLimit"
        ] = None,
        actions_to_add: Optional[
            "capo_deadline.types.budget_actions_to_add.BudgetActionsToAdd"
        ] = None,
        actions_to_remove: Optional[
            "capo_deadline.types.budget_actions_to_remove.BudgetActionsToRemove"
        ] = None,
        schedule: Optional["capo_deadline.types.budget_schedule.BudgetSchedule"] = None,
    ) -> "capo_deadline.types.update_budget_response.UpdateBudgetResponse":
        """<p>Updates a budget that sets spending thresholds for rendering activity.</p>

        Args:
            farm_id: <p>The farm ID of the budget to update.</p>
            budget_id: <p>The budget ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the budget to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the budget to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            status: <p>Updates the status of the budget.</p> <ul> <li> <p> <code>ACTIVE</code>–The budget is being evaluated.</p> </li> <li> <p> <code>INACTIVE</code>–The budget is inactive. This can include Expired, Canceled, or deleted Deleted statuses.</p> </li> </ul>
            approximate_dollar_limit: <p>The dollar limit to update on the budget. Based on consumed usage.</p>
            actions_to_add: <p>The budget actions to add. Budget actions specify what happens when the budget runs out.</p>
            actions_to_remove: <p>The budget actions to remove from the budget.</p>
            schedule: <p>The schedule to update.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_budget_request.UpdateBudgetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_budget_response.UpdateBudgetResponse"
        ]:
            import capo_deadline._operations.deadline.update_budget

            output, http_response = (
                capo_deadline._operations.deadline.update_budget.update_budget(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_budget_request.UpdateBudgetRequest = {
            "farm_id": farm_id,
            "budget_id": budget_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if status is not None:
            input_["status"] = status
        if approximate_dollar_limit is not None:
            input_["approximate_dollar_limit"] = approximate_dollar_limit
        if actions_to_add is not None:
            input_["actions_to_add"] = actions_to_add
        if actions_to_remove is not None:
            input_["actions_to_remove"] = actions_to_remove
        if schedule is not None:
            input_["schedule"] = schedule

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_budget(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        budget_id: "capo_deadline.types.budget_id.BudgetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_budget_response.DeleteBudgetResponse":
        """<p>Deletes a budget.</p>

        Args:
            farm_id: <p>The farm ID of the farm to remove from the budget.</p>
            budget_id: <p>The budget ID of the budget to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_budget_request.DeleteBudgetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_budget_response.DeleteBudgetResponse"
        ]:
            import capo_deadline._operations.deadline.delete_budget

            output, http_response = (
                capo_deadline._operations.deadline.delete_budget.delete_budget(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_budget_request.DeleteBudgetRequest = {
            "farm_id": farm_id,
            "budget_id": budget_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_budgets(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        status: Optional["capo_deadline.types.budget_status.BudgetStatus"] = None,
    ) -> "capo_deadline.types.list_budgets_response.ListBudgetsResponse":
        """<p>A list of budgets in a farm.</p>

        Args:
            farm_id: <p>The farm ID associated with the budgets.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            status: <p>The status to list for the budgets.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_budgets_request.ListBudgetsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_budgets_response.ListBudgetsResponse"
        ]:
            import capo_deadline._operations.deadline.list_budgets

            output, http_response = (
                capo_deadline._operations.deadline.list_budgets.list_budgets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_budgets_request.ListBudgetsRequest = {
            "farm_id": farm_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_budgets(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        status: Optional["capo_deadline.types.budget_status.BudgetStatus"] = None,
    ) -> "Iterator[capo_deadline.types.budget_summary.BudgetSummary]":
        _token = next_token
        while True:
            _response = self.list_budgets(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
            )
            _page = _resolve_path(_response, ("budgets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_fleet(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        role_arn: "capo_deadline.types.iam_role_arn.IamRoleArn",
        max_worker_count: "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger",
        configuration: "capo_deadline.types.fleet_configuration.FleetConfiguration",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        min_worker_count: Optional[
            "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
        ] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
        host_configuration: Optional[
            "capo_deadline.types.host_configuration.HostConfiguration"
        ] = None,
    ) -> "capo_deadline.types.create_fleet_response.CreateFleetResponse":
        """<p>Creates a fleet. Fleets gather information relating to compute, or capacity, for renders within your farms. You can choose to manage your own capacity or opt to have fleets fully managed by Deadline Cloud.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the fleet.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the fleet.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the fleet.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            role_arn: <p>The IAM role ARN for the role that the fleet's workers will use.</p>
            min_worker_count: <p>The minimum number of workers for the fleet.</p>
            max_worker_count: <p>The maximum number of workers for the fleet.</p> <p>Deadline Cloud limits the number of workers to less than or equal to the fleet's maximum worker count. The service maintains eventual consistency for the worker count. If you make multiple rapid calls to <code>CreateWorker</code> before the field updates, you might exceed your fleet's maximum worker count. For example, if your <code>maxWorkerCount</code> is 10 and you currently have 9 workers, making two quick <code>CreateWorker</code> calls might successfully create 2 workers instead of 1, resulting in 11 total workers.</p>
            configuration: <p>The configuration settings for the fleet. Customer managed fleets are self-managed. Service managed Amazon EC2 fleets are managed by Deadline Cloud.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>
            host_configuration: <p>Provides a script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_fleet_request.CreateFleetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_fleet_response.CreateFleetResponse"
        ]:
            import capo_deadline._operations.deadline.create_fleet

            output, http_response = (
                capo_deadline._operations.deadline.create_fleet.create_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_fleet_request.CreateFleetRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
            "role_arn": role_arn,
            "max_worker_count": max_worker_count,
            "configuration": configuration,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if min_worker_count is not None:
            input_["min_worker_count"] = min_worker_count
        if tags is not None:
            input_["tags"] = tags
        if host_configuration is not None:
            input_["host_configuration"] = host_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_fleet(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_fleet_response.GetFleetResponse":
        """<p>Get a fleet.</p>

        Args:
            farm_id: <p>The farm ID of the farm in the fleet.</p>
            fleet_id: <p>The fleet ID of the fleet to get.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_fleet_request.GetFleetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_fleet_response.GetFleetResponse"
        ]:
            import capo_deadline._operations.deadline.get_fleet

            output, http_response = (
                capo_deadline._operations.deadline.get_fleet.get_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_fleet_request.GetFleetRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_fleet(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        role_arn: Optional["capo_deadline.types.iam_role_arn.IamRoleArn"] = None,
        min_worker_count: Optional[
            "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
        ] = None,
        max_worker_count: Optional[
            "capo_deadline.types.min_zero_max_integer.MinZeroMaxInteger"
        ] = None,
        configuration: Optional[
            "capo_deadline.types.fleet_configuration.FleetConfiguration"
        ] = None,
        host_configuration: Optional[
            "capo_deadline.types.host_configuration.HostConfiguration"
        ] = None,
    ) -> "capo_deadline.types.update_fleet_response.UpdateFleetResponse":
        """<p>Updates a fleet.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            fleet_id: <p>The fleet ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the fleet to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the fleet to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            role_arn: <p>The IAM role ARN that the fleet's workers assume while running jobs.</p>
            min_worker_count: <p>The minimum number of workers in the fleet.</p>
            max_worker_count: <p>The maximum number of workers in the fleet.</p> <p>Deadline Cloud limits the number of workers to less than or equal to the fleet's maximum worker count. The service maintains eventual consistency for the worker count. If you make multiple rapid calls to <code>CreateWorker</code> before the field updates, you might exceed your fleet's maximum worker count. For example, if your <code>maxWorkerCount</code> is 10 and you currently have 9 workers, making two quick <code>CreateWorker</code> calls might successfully create 2 workers instead of 1, resulting in 11 total workers.</p>
            configuration: <p>The fleet configuration to update.</p>
            host_configuration: <p>Provides a script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_fleet_request.UpdateFleetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_fleet_response.UpdateFleetResponse"
        ]:
            import capo_deadline._operations.deadline.update_fleet

            output, http_response = (
                capo_deadline._operations.deadline.update_fleet.update_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_fleet_request.UpdateFleetRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if min_worker_count is not None:
            input_["min_worker_count"] = min_worker_count
        if max_worker_count is not None:
            input_["max_worker_count"] = max_worker_count
        if configuration is not None:
            input_["configuration"] = configuration
        if host_configuration is not None:
            input_["host_configuration"] = host_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_fleet(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
    ) -> "capo_deadline.types.delete_fleet_response.DeleteFleetResponse":
        """<p>Deletes a fleet.</p>

        Args:
            farm_id: <p>The farm ID of the farm to remove from the fleet.</p>
            fleet_id: <p>The fleet ID of the fleet to delete.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_fleet_request.DeleteFleetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_fleet_response.DeleteFleetResponse"
        ]:
            import capo_deadline._operations.deadline.delete_fleet

            output, http_response = (
                capo_deadline._operations.deadline.delete_fleet.delete_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_fleet_request.DeleteFleetRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
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

    def list_fleets(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        status: Optional["capo_deadline.types.fleet_status.FleetStatus"] = None,
    ) -> "capo_deadline.types.list_fleets_response.ListFleetsResponse":
        """<p>Lists fleets.</p>

        Args:
            farm_id: <p>The farm ID of the fleets.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal ID of the members to include in the fleet.</p>
            display_name: <p>The display names of a list of fleets.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            status: <p>The status of the fleet.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_fleets_request.ListFleetsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_fleets_response.ListFleetsResponse"
        ]:
            import capo_deadline._operations.deadline.list_fleets

            output, http_response = (
                capo_deadline._operations.deadline.list_fleets.list_fleets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_fleets_request.ListFleetsRequest = {
            "farm_id": farm_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id
        if display_name is not None:
            input_["display_name"] = display_name
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_fleets(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        status: Optional["capo_deadline.types.fleet_status.FleetStatus"] = None,
    ) -> "Iterator[capo_deadline.types.fleet_summary.FleetSummary]":
        _token = next_token
        while True:
            _response = self.list_fleets(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                principal_id=principal_id,
                display_name=display_name,
                status=status,
            )
            _page = _resolve_path(_response, ("fleets",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_member_to_fleet(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "capo_deadline.types.membership_level.MembershipLevel",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
    ) -> "capo_deadline.types.associate_member_to_fleet_response.AssociateMemberToFleetResponse":
        """<p>Assigns a fleet membership level to a member.</p>

        Args:
            farm_id: <p>The farm ID of the fleet to associate with the member.</p>
            fleet_id: <p>The ID of the fleet to associate with a member.</p>
            principal_type: <p>The member's principal type to associate with the fleet.</p>
            identity_store_id: <p>The member's identity store ID to associate with the fleet.</p>
            membership_level: <p>The principal's membership level for the associated fleet.</p>
            principal_id: <p>The member's principal ID to associate with a fleet.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.associate_member_to_fleet_request.AssociateMemberToFleetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.associate_member_to_fleet_response.AssociateMemberToFleetResponse"
        ]:
            import capo_deadline._operations.deadline.associate_member_to_fleet

            output, http_response = (
                capo_deadline._operations.deadline.associate_member_to_fleet.associate_member_to_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.associate_member_to_fleet_request.AssociateMemberToFleetRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "principal_type": principal_type,
            "identity_store_id": identity_store_id,
            "membership_level": membership_level,
            "principal_id": principal_id,
        }
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def assume_fleet_role_for_read(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.assume_fleet_role_for_read_response.AssumeFleetRoleForReadResponse":
        """<p>Get Amazon Web Services credentials from the fleet role. The IAM permissions of the credentials are scoped down to have read-only access.</p>

        Args:
            farm_id: <p>The farm ID for the fleet's farm.</p>
            fleet_id: <p>The fleet ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.assume_fleet_role_for_read_request.AssumeFleetRoleForReadRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.assume_fleet_role_for_read_response.AssumeFleetRoleForReadResponse"
        ]:
            import capo_deadline._operations.deadline.assume_fleet_role_for_read

            output, http_response = (
                capo_deadline._operations.deadline.assume_fleet_role_for_read.assume_fleet_role_for_read(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.assume_fleet_role_for_read_request.AssumeFleetRoleForReadRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_member_from_fleet(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.disassociate_member_from_fleet_response.DisassociateMemberFromFleetResponse":
        """<p>Disassociates a member from a fleet.</p>

        Args:
            farm_id: <p>The farm ID of the fleet to disassociate a member from.</p>
            fleet_id: <p>The fleet ID of the fleet to from which to disassociate a member.</p>
            principal_id: <p>A member's principal ID to disassociate from a fleet.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.disassociate_member_from_fleet_request.DisassociateMemberFromFleetRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.disassociate_member_from_fleet_response.DisassociateMemberFromFleetResponse"
        ]:
            import capo_deadline._operations.deadline.disassociate_member_from_fleet

            output, http_response = (
                capo_deadline._operations.deadline.disassociate_member_from_fleet.disassociate_member_from_fleet(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.disassociate_member_from_fleet_request.DisassociateMemberFromFleetRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "principal_id": principal_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_fleet_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_fleet_members_response.ListFleetMembersResponse":
        """<p>Lists fleet members.</p>

        Args:
            farm_id: <p>The farm ID of the fleet.</p>
            fleet_id: <p>The fleet ID to include on the list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_fleet_members_request.ListFleetMembersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_fleet_members_response.ListFleetMembersResponse"
        ]:
            import capo_deadline._operations.deadline.list_fleet_members

            output, http_response = (
                capo_deadline._operations.deadline.list_fleet_members.list_fleet_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_fleet_members_request.ListFleetMembersRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
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

    def iter_list_fleet_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.fleet_member.FleetMember]":
        _token = next_token
        while True:
            _response = self.list_fleet_members(
                farm_id,
                fleet_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_volume(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        volume_id: "capo_deadline.types.volume_id.VolumeId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_volume_response.GetVolumeResponse":
        """<p>Gets a persistent volume.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the fleet.</p>
            fleet_id: <p>The fleet ID of the fleet that contains the volume.</p>
            volume_id: <p>The volume ID of the volume to retrieve.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get a volume

            >>> client.get_volume(farm_id='farm-1234567890abcdef1234567890abcdef', fleet_id='fleet-1234567890abcdef1234567890abcdef', volume_id='volume-1234567890abcdef1234567890abcdef')
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_volume_request.GetVolumeRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_volume_response.GetVolumeResponse"
        ]:
            import capo_deadline._operations.deadline.get_volume

            output, http_response = (
                capo_deadline._operations.deadline.get_volume.get_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_volume_request.GetVolumeRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "volume_id": volume_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_volume(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        volume_id: "capo_deadline.types.volume_id.VolumeId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_volume_response.DeleteVolumeResponse":
        """<p>Deletes a persistent volume.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the fleet.</p>
            fleet_id: <p>The fleet ID of the fleet that contains the volume.</p>
            volume_id: <p>The volume ID of the volume to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Delete a volume

            >>> client.delete_volume(farm_id='farm-1234567890abcdef1234567890abcdef', fleet_id='fleet-1234567890abcdef1234567890abcdef', volume_id='volume-1234567890abcdef1234567890abcdef')
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_volume_request.DeleteVolumeRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_volume_response.DeleteVolumeResponse"
        ]:
            import capo_deadline._operations.deadline.delete_volume

            output, http_response = (
                capo_deadline._operations.deadline.delete_volume.delete_volume(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_volume_request.DeleteVolumeRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "volume_id": volume_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_volumes(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_volumes_response.ListVolumesResponse":
        """<p>Lists the persistent volumes in a fleet.</p>

        Args:
            farm_id: <p>The farm ID of the farm that contains the fleet.</p>
            fleet_id: <p>The fleet ID of the fleet that contains the volumes.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            List volumes for a fleet

            >>> client.list_volumes(farm_id='farm-1234567890abcdef1234567890abcdef', fleet_id='fleet-1234567890abcdef1234567890abcdef')
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_volumes_request.ListVolumesRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_volumes_response.ListVolumesResponse"
        ]:
            import capo_deadline._operations.deadline.list_volumes

            output, http_response = (
                capo_deadline._operations.deadline.list_volumes.list_volumes(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_volumes_request.ListVolumesRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
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

    def iter_list_volumes(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.volume_summary.VolumeSummary]":
        _token = next_token
        while True:
            _response = self.list_volumes(
                farm_id,
                fleet_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("volumes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def create_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        host_properties: Optional[
            "capo_deadline.types.host_properties_request.HostPropertiesRequest"
        ] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_worker_response.CreateWorkerResponse":
        """<p>Creates a worker. A worker tells your instance how much processing power (vCPU), and memory (GiB) you’ll need to assemble the digital assets held within a particular instance. You can specify certain instance types to use, or let the worker know which instances types to exclude.</p> <p>Deadline Cloud limits the number of workers to less than or equal to the fleet's maximum worker count. The service maintains eventual consistency for the worker count. If you make multiple rapid calls to <code>CreateWorker</code> before the field updates, you might exceed your fleet's maximum worker count. For example, if your <code>maxWorkerCount</code> is 10 and you currently have 9 workers, making two quick <code>CreateWorker</code> calls might successfully create 2 workers instead of 1, resulting in 11 total workers.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the worker.</p>
            fleet_id: <p>The fleet ID to connect to the worker.</p>
            host_properties: <p>The IP address and host name of the worker.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_worker_request.CreateWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_worker_response.CreateWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.create_worker

            output, http_response = (
                capo_deadline._operations.deadline.create_worker.create_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_worker_request.CreateWorkerRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
        }
        if host_properties is not None:
            input_["host_properties"] = host_properties
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

    def get_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_worker_response.GetWorkerResponse":
        """<p>Gets a worker.</p>

        Args:
            farm_id: <p>The farm ID for the worker.</p>
            fleet_id: <p>The fleet ID of the worker.</p>
            worker_id: <p>The worker ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_worker_request.GetWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_worker_response.GetWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.get_worker

            output, http_response = (
                capo_deadline._operations.deadline.get_worker.get_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_worker_request.GetWorkerRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        status: Optional[
            "capo_deadline.types.updated_worker_status.UpdatedWorkerStatus"
        ] = None,
        capabilities: Optional[
            "capo_deadline.types.worker_capabilities.WorkerCapabilities"
        ] = None,
        host_properties: Optional[
            "capo_deadline.types.host_properties_request.HostPropertiesRequest"
        ] = None,
    ) -> "capo_deadline.types.update_worker_response.UpdateWorkerResponse":
        """<p>Updates a worker.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            fleet_id: <p>The fleet ID to update.</p>
            worker_id: <p>The worker ID to update.</p>
            status: <p>The worker status to update.</p>
            capabilities: <p>The worker capabilities to update.</p>
            host_properties: <p>The host properties to update.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_worker_request.UpdateWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_worker_response.UpdateWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.update_worker

            output, http_response = (
                capo_deadline._operations.deadline.update_worker.update_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_worker_request.UpdateWorkerRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
        }
        if status is not None:
            input_["status"] = status
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if host_properties is not None:
            input_["host_properties"] = host_properties

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_worker_response.DeleteWorkerResponse":
        """<p>Deletes a worker.</p>

        Args:
            farm_id: <p>The farm ID of the worker to delete.</p>
            fleet_id: <p>The fleet ID of the worker to delete.</p>
            worker_id: <p>The worker ID of the worker to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_worker_request.DeleteWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_worker_response.DeleteWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.delete_worker

            output, http_response = (
                capo_deadline._operations.deadline.delete_worker.delete_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_worker_request.DeleteWorkerRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_workers(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_workers_response.ListWorkersResponse":
        """<p>Lists workers.</p>

        Args:
            farm_id: <p>The farm ID connected to the workers.</p>
            fleet_id: <p>The fleet ID of the workers.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_workers_request.ListWorkersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_workers_response.ListWorkersResponse"
        ]:
            import capo_deadline._operations.deadline.list_workers

            output, http_response = (
                capo_deadline._operations.deadline.list_workers.list_workers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_workers_request.ListWorkersRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
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

    def iter_list_workers(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.worker_summary.WorkerSummary]":
        _token = next_token
        while True:
            _response = self.list_workers(
                farm_id,
                fleet_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("workers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def assume_fleet_role_for_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.assume_fleet_role_for_worker_response.AssumeFleetRoleForWorkerResponse":
        """<p>Get credentials from the fleet role for a worker.</p>

        Args:
            farm_id: <p>The farm ID for the fleet's farm.</p>
            fleet_id: <p>The fleet ID that contains the worker.</p>
            worker_id: <p>The ID of the worker assuming the fleet role.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.assume_fleet_role_for_worker_request.AssumeFleetRoleForWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.assume_fleet_role_for_worker_response.AssumeFleetRoleForWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.assume_fleet_role_for_worker

            output, http_response = (
                capo_deadline._operations.deadline.assume_fleet_role_for_worker.assume_fleet_role_for_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.assume_fleet_role_for_worker_request.AssumeFleetRoleForWorkerRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def assume_queue_role_for_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.assume_queue_role_for_worker_response.AssumeQueueRoleForWorkerResponse":
        """<p>Allows a worker to assume a queue role.</p>

        Args:
            farm_id: <p>The farm ID of the worker assuming the queue role.</p>
            fleet_id: <p>The fleet ID of the worker assuming the queue role.</p>
            worker_id: <p>The worker ID of the worker assuming the queue role.</p>
            queue_id: <p>The queue ID of the worker assuming the queue role.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.assume_queue_role_for_worker_request.AssumeQueueRoleForWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.assume_queue_role_for_worker_response.AssumeQueueRoleForWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.assume_queue_role_for_worker

            output, http_response = (
                capo_deadline._operations.deadline.assume_queue_role_for_worker.assume_queue_role_for_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.assume_queue_role_for_worker_request.AssumeQueueRoleForWorkerRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
            "queue_id": queue_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_job_entity(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        identifiers: "capo_deadline.types.job_entity_identifiers.JobEntityIdentifiers",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.batch_get_job_entity_response.BatchGetJobEntityResponse":
        """<p>Get batched job details for a worker.</p>

        Args:
            farm_id: <p>The farm ID of the worker that's fetching job details. The worker must have an assignment on a job to fetch job details.</p>
            fleet_id: <p>The fleet ID of the worker that's fetching job details. The worker must have an assignment on a job to fetch job details.</p>
            worker_id: <p>The worker ID of the worker containing the job details to get.</p>
            identifiers: <p>The job identifiers to include within the job entity batch details.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.batch_get_job_entity_request.BatchGetJobEntityRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.batch_get_job_entity_response.BatchGetJobEntityResponse"
        ]:
            import capo_deadline._operations.deadline.batch_get_job_entity

            output, http_response = (
                capo_deadline._operations.deadline.batch_get_job_entity.batch_get_job_entity(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.batch_get_job_entity_request.BatchGetJobEntityRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
            "identifiers": identifiers,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_sessions_for_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_sessions_for_worker_response.ListSessionsForWorkerResponse":
        """<p>Lists sessions for a worker.</p>

        Args:
            farm_id: <p>The farm ID for the session.</p>
            fleet_id: <p>The fleet ID for the session.</p>
            worker_id: <p>The worker ID for the session.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_sessions_for_worker_request.ListSessionsForWorkerRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_sessions_for_worker_response.ListSessionsForWorkerResponse"
        ]:
            import capo_deadline._operations.deadline.list_sessions_for_worker

            output, http_response = (
                capo_deadline._operations.deadline.list_sessions_for_worker.list_sessions_for_worker(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_sessions_for_worker_request.ListSessionsForWorkerRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
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

    def iter_list_sessions_for_worker(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.worker_session_summary.WorkerSessionSummary]":
        _token = next_token
        while True:
            _response = self.list_sessions_for_worker(
                farm_id,
                fleet_id,
                worker_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_worker_schedule(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        fleet_id: "capo_deadline.types.fleet_id.FleetId",
        worker_id: "capo_deadline.types.worker_id.WorkerId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        updated_session_actions: Optional[
            "capo_deadline.types.updated_session_actions.UpdatedSessionActions"
        ] = None,
    ) -> "capo_deadline.types.update_worker_schedule_response.UpdateWorkerScheduleResponse":
        """<p>Updates the schedule for a worker.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            fleet_id: <p>The fleet ID to update.</p>
            worker_id: <p>The worker ID to update.</p>
            updated_session_actions: <p>The session actions associated with the worker schedule to update.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_worker_schedule_request.UpdateWorkerScheduleRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_worker_schedule_response.UpdateWorkerScheduleResponse"
        ]:
            import capo_deadline._operations.deadline.update_worker_schedule

            output, http_response = (
                capo_deadline._operations.deadline.update_worker_schedule.update_worker_schedule(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_worker_schedule_request.UpdateWorkerScheduleRequest = {
            "farm_id": farm_id,
            "fleet_id": fleet_id,
            "worker_id": worker_id,
        }
        if updated_session_actions is not None:
            input_["updated_session_actions"] = updated_session_actions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        display_name: "capo_deadline.types.resource_name.ResourceName",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        default_budget_action: Optional[
            "capo_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
        ] = None,
        job_attachment_settings: Optional[
            "capo_deadline.types.job_attachment_settings.JobAttachmentSettings"
        ] = None,
        role_arn: Optional["capo_deadline.types.iam_role_arn.IamRoleArn"] = None,
        job_run_as_user: Optional[
            "capo_deadline.types.job_run_as_user.JobRunAsUser"
        ] = None,
        required_file_system_location_names: Optional[
            "capo_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
        ] = None,
        allowed_storage_profile_ids: Optional[
            "capo_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
        ] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
        scheduling_configuration: Optional[
            "capo_deadline.types.scheduling_configuration.SchedulingConfiguration"
        ] = None,
    ) -> "capo_deadline.types.create_queue_response.CreateQueueResponse":
        """<p>Creates a queue to coordinate the order in which jobs run on a farm. A queue can also specify where to pull resources and indicate where to output completed jobs.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the queue.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The display name of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the queue.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            default_budget_action: <p>The default action to take on a queue if a budget isn't configured.</p>
            job_attachment_settings: <p>The job attachment settings for the queue. These are the Amazon S3 bucket name and the Amazon S3 prefix.</p>
            role_arn: <p>The IAM role ARN that workers will use while running jobs for this queue.</p>
            job_run_as_user: <p>The jobs in the queue run as the specified POSIX user.</p>
            required_file_system_location_names: <p>The file system location name to include in the queue.</p>
            allowed_storage_profile_ids: <p>The storage profile IDs to include in the queue.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>
            scheduling_configuration: <p>The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue.</p> <p>If not specified, the queue defaults to the <code>priorityFifo</code> scheduling configuration.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_queue_request.CreateQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_queue_response.CreateQueueResponse"
        ]:
            import capo_deadline._operations.deadline.create_queue

            output, http_response = (
                capo_deadline._operations.deadline.create_queue.create_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_queue_request.CreateQueueRequest = {
            "farm_id": farm_id,
            "display_name": display_name,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if default_budget_action is not None:
            input_["default_budget_action"] = default_budget_action
        if job_attachment_settings is not None:
            input_["job_attachment_settings"] = job_attachment_settings
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if job_run_as_user is not None:
            input_["job_run_as_user"] = job_run_as_user
        if required_file_system_location_names is not None:
            input_["required_file_system_location_names"] = (
                required_file_system_location_names
            )
        if allowed_storage_profile_ids is not None:
            input_["allowed_storage_profile_ids"] = allowed_storage_profile_ids
        if tags is not None:
            input_["tags"] = tags
        if scheduling_configuration is not None:
            input_["scheduling_configuration"] = scheduling_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_queue_response.GetQueueResponse":
        """<p>Gets a queue.</p>

        Args:
            farm_id: <p>The farm ID of the farm in the queue.</p>
            queue_id: <p>The queue ID for the queue to retrieve.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_queue_request.GetQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_queue_response.GetQueueResponse"
        ]:
            import capo_deadline._operations.deadline.get_queue

            output, http_response = (
                capo_deadline._operations.deadline.get_queue.get_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_queue_request.GetQueueRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        description: Optional["capo_deadline.types.description.Description"] = None,
        default_budget_action: Optional[
            "capo_deadline.types.default_queue_budget_action.DefaultQueueBudgetAction"
        ] = None,
        job_attachment_settings: Optional[
            "capo_deadline.types.job_attachment_settings.JobAttachmentSettings"
        ] = None,
        role_arn: Optional["capo_deadline.types.iam_role_arn.IamRoleArn"] = None,
        job_run_as_user: Optional[
            "capo_deadline.types.job_run_as_user.JobRunAsUser"
        ] = None,
        required_file_system_location_names_to_add: Optional[
            "capo_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
        ] = None,
        required_file_system_location_names_to_remove: Optional[
            "capo_deadline.types.required_file_system_location_names.RequiredFileSystemLocationNames"
        ] = None,
        allowed_storage_profile_ids_to_add: Optional[
            "capo_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
        ] = None,
        allowed_storage_profile_ids_to_remove: Optional[
            "capo_deadline.types.allowed_storage_profile_ids.AllowedStorageProfileIds"
        ] = None,
        scheduling_configuration: Optional[
            "capo_deadline.types.scheduling_configuration.SchedulingConfiguration"
        ] = None,
    ) -> "capo_deadline.types.update_queue_response.UpdateQueueResponse":
        """<p>Updates a queue.</p>

        Args:
            farm_id: <p>The farm ID to update in the queue.</p>
            queue_id: <p>The queue ID to update.</p>
            client_token: <p>The idempotency token to update in the queue.</p>
            display_name: <p>The display name of the queue to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            description: <p>The description of the queue to update.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            default_budget_action: <p>The default action to take for a queue update if a budget isn't configured.</p>
            job_attachment_settings: <p>The job attachment settings to update for the queue.</p>
            role_arn: <p>The IAM role ARN that's used to run jobs from this queue.</p>
            job_run_as_user: <p>Update the jobs in the queue to run as a specified POSIX user.</p>
            required_file_system_location_names_to_add: <p>The required file system location names to add to the queue.</p>
            required_file_system_location_names_to_remove: <p>The required file system location names to remove from the queue.</p>
            allowed_storage_profile_ids_to_add: <p>The storage profile IDs to add.</p>
            allowed_storage_profile_ids_to_remove: <p>The storage profile ID to remove.</p>
            scheduling_configuration: <p>The scheduling configuration for the queue. This configuration determines how workers are assigned to jobs in the queue.</p> <p>When updating the scheduling configuration, the entire configuration is replaced.</p> <p>In-progress tasks run to completion before the new scheduling configuration takes effect.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_queue_request.UpdateQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_queue_response.UpdateQueueResponse"
        ]:
            import capo_deadline._operations.deadline.update_queue

            output, http_response = (
                capo_deadline._operations.deadline.update_queue.update_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_queue_request.UpdateQueueRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if display_name is not None:
            input_["display_name"] = display_name
        if description is not None:
            input_["description"] = description
        if default_budget_action is not None:
            input_["default_budget_action"] = default_budget_action
        if job_attachment_settings is not None:
            input_["job_attachment_settings"] = job_attachment_settings
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if job_run_as_user is not None:
            input_["job_run_as_user"] = job_run_as_user
        if required_file_system_location_names_to_add is not None:
            input_["required_file_system_location_names_to_add"] = (
                required_file_system_location_names_to_add
            )
        if required_file_system_location_names_to_remove is not None:
            input_["required_file_system_location_names_to_remove"] = (
                required_file_system_location_names_to_remove
            )
        if allowed_storage_profile_ids_to_add is not None:
            input_["allowed_storage_profile_ids_to_add"] = (
                allowed_storage_profile_ids_to_add
            )
        if allowed_storage_profile_ids_to_remove is not None:
            input_["allowed_storage_profile_ids_to_remove"] = (
                allowed_storage_profile_ids_to_remove
            )
        if scheduling_configuration is not None:
            input_["scheduling_configuration"] = scheduling_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_queue_response.DeleteQueueResponse":
        """<p>Deletes a queue.</p> <important> <p>You can't recover the jobs in a queue if you delete the queue. Deleting the queue also deletes the jobs in that queue.</p> </important>

        Args:
            farm_id: <p>The ID of the farm from which to remove the queue.</p>
            queue_id: <p>The queue ID of the queue to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_queue_request.DeleteQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_queue_response.DeleteQueueResponse"
        ]:
            import capo_deadline._operations.deadline.delete_queue

            output, http_response = (
                capo_deadline._operations.deadline.delete_queue.delete_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_queue_request.DeleteQueueRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_queues(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
        status: Optional["capo_deadline.types.queue_status.QueueStatus"] = None,
    ) -> "capo_deadline.types.list_queues_response.ListQueuesResponse":
        """<p>Lists queues.</p>

        Args:
            farm_id: <p>The farm ID of the queue.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal IDs to include in the list of queues.</p>
            status: <p>The status of the queues listed.</p> <ul> <li> <p> <code>ACTIVE</code>–The queues are active.</p> </li> <li> <p> <code>SCHEDULING</code>–The queues are scheduling.</p> </li> <li> <p> <code>SCHEDULING_BLOCKED</code>–The queue scheduling is blocked for these queues.</p> </li> </ul>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_queues_request.ListQueuesRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_queues_response.ListQueuesResponse"
        ]:
            import capo_deadline._operations.deadline.list_queues

            output, http_response = (
                capo_deadline._operations.deadline.list_queues.list_queues(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_queues_request.ListQueuesRequest = {
            "farm_id": farm_id
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_queues(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
        status: Optional["capo_deadline.types.queue_status.QueueStatus"] = None,
    ) -> "Iterator[capo_deadline.types.queue_summary.QueueSummary]":
        _token = next_token
        while True:
            _response = self.list_queues(
                farm_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                principal_id=principal_id,
                status=status,
            )
            _page = _resolve_path(_response, ("queues",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_member_to_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "capo_deadline.types.membership_level.MembershipLevel",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
    ) -> "capo_deadline.types.associate_member_to_queue_response.AssociateMemberToQueueResponse":
        """<p>Assigns a queue membership level to a member</p>

        Args:
            farm_id: <p>The farm ID of the queue to associate with the member.</p>
            queue_id: <p>The ID of the queue to associate to the member.</p>
            principal_type: <p>The member's principal type to associate with the queue.</p>
            identity_store_id: <p>The member's identity store ID to associate with the queue.</p>
            membership_level: <p>The principal's membership level for the associated queue.</p>
            principal_id: <p>The member's principal ID to associate with the queue.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.associate_member_to_queue_request.AssociateMemberToQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.associate_member_to_queue_response.AssociateMemberToQueueResponse"
        ]:
            import capo_deadline._operations.deadline.associate_member_to_queue

            output, http_response = (
                capo_deadline._operations.deadline.associate_member_to_queue.associate_member_to_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.associate_member_to_queue_request.AssociateMemberToQueueRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "principal_type": principal_type,
            "identity_store_id": identity_store_id,
            "membership_level": membership_level,
            "principal_id": principal_id,
        }
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def assume_queue_role_for_read(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.assume_queue_role_for_read_response.AssumeQueueRoleForReadResponse":
        """<p>Gets Amazon Web Services credentials from the queue role. The IAM permissions of the credentials are scoped down to have read-only access.</p>

        Args:
            farm_id: <p>The farm ID of the farm containing the queue.</p>
            queue_id: <p>The queue ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.assume_queue_role_for_read_request.AssumeQueueRoleForReadRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.assume_queue_role_for_read_response.AssumeQueueRoleForReadResponse"
        ]:
            import capo_deadline._operations.deadline.assume_queue_role_for_read

            output, http_response = (
                capo_deadline._operations.deadline.assume_queue_role_for_read.assume_queue_role_for_read(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.assume_queue_role_for_read_request.AssumeQueueRoleForReadRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def assume_queue_role_for_user(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.assume_queue_role_for_user_response.AssumeQueueRoleForUserResponse":
        """<p>Allows a user to assume a role for a queue.</p>

        Args:
            farm_id: <p>The farm ID of the queue that the user assumes the role for.</p>
            queue_id: <p>The queue ID of the queue that the user assumes the role for.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.assume_queue_role_for_user_request.AssumeQueueRoleForUserRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.assume_queue_role_for_user_response.AssumeQueueRoleForUserResponse"
        ]:
            import capo_deadline._operations.deadline.assume_queue_role_for_user

            output, http_response = (
                capo_deadline._operations.deadline.assume_queue_role_for_user.assume_queue_role_for_user(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.assume_queue_role_for_user_request.AssumeQueueRoleForUserRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_queue_environment(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        priority: "capo_deadline.types.priority.Priority",
        template_type: "capo_deadline.types.environment_template_type.EnvironmentTemplateType",
        template: "capo_deadline.types.environment_template.EnvironmentTemplate",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
    ) -> "capo_deadline.types.create_queue_environment_response.CreateQueueEnvironmentResponse":
        """<p>Creates an environment for a queue that defines how jobs in the queue run.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the environment.</p>
            queue_id: <p>The queue ID to connect the queue and environment.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            priority: <p>Sets the priority of the environments in the queue from 0 to 10,000, where 0 is the highest priority (activated first and deactivated last). If two environments share the same priority value, the environment created first takes higher priority.</p>
            template_type: <p>The template's file type, <code>JSON</code> or <code>YAML</code>.</p>
            template: <p>The environment template to use in the queue.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_queue_environment_request.CreateQueueEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_queue_environment_response.CreateQueueEnvironmentResponse"
        ]:
            import capo_deadline._operations.deadline.create_queue_environment

            output, http_response = (
                capo_deadline._operations.deadline.create_queue_environment.create_queue_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_queue_environment_request.CreateQueueEnvironmentRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "priority": priority,
            "template_type": template_type,
            "template": template,
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

    def delete_queue_environment(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_queue_environment_response.DeleteQueueEnvironmentResponse":
        """<p>Deletes a queue environment.</p>

        Args:
            farm_id: <p>The farm ID of the farm from which to remove the queue environment.</p>
            queue_id: <p>The queue ID of the queue environment to delete.</p>
            queue_environment_id: <p>The queue environment ID of the queue environment to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_queue_environment_request.DeleteQueueEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_queue_environment_response.DeleteQueueEnvironmentResponse"
        ]:
            import capo_deadline._operations.deadline.delete_queue_environment

            output, http_response = (
                capo_deadline._operations.deadline.delete_queue_environment.delete_queue_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_queue_environment_request.DeleteQueueEnvironmentRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "queue_environment_id": queue_environment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_member_from_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.disassociate_member_from_queue_response.DisassociateMemberFromQueueResponse":
        """<p>Disassociates a member from a queue.</p>

        Args:
            farm_id: <p>The farm ID for the queue to disassociate from a member.</p>
            queue_id: <p>The queue ID of the queue in which you're disassociating from a member.</p>
            principal_id: <p>A member's principal ID to disassociate from a queue.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.disassociate_member_from_queue_request.DisassociateMemberFromQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.disassociate_member_from_queue_response.DisassociateMemberFromQueueResponse"
        ]:
            import capo_deadline._operations.deadline.disassociate_member_from_queue

            output, http_response = (
                capo_deadline._operations.deadline.disassociate_member_from_queue.disassociate_member_from_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.disassociate_member_from_queue_request.DisassociateMemberFromQueueRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "principal_id": principal_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_queue_environment(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> (
        "capo_deadline.types.get_queue_environment_response.GetQueueEnvironmentResponse"
    ):
        """<p>Gets a queue environment.</p>

        Args:
            farm_id: <p>The farm ID for the queue environment.</p>
            queue_id: <p>The queue ID for the queue environment.</p>
            queue_environment_id: <p>The queue environment ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_queue_environment_request.GetQueueEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_queue_environment_response.GetQueueEnvironmentResponse"
        ]:
            import capo_deadline._operations.deadline.get_queue_environment

            output, http_response = (
                capo_deadline._operations.deadline.get_queue_environment.get_queue_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_queue_environment_request.GetQueueEnvironmentRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "queue_environment_id": queue_environment_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_storage_profile_for_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        storage_profile_id: "capo_deadline.types.storage_profile_id.StorageProfileId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_storage_profile_for_queue_response.GetStorageProfileForQueueResponse":
        """<p>Gets a storage profile for a queue.</p>

        Args:
            farm_id: <p>The farm ID for the queue in storage profile.</p>
            queue_id: <p>The queue ID the queue in the storage profile.</p>
            storage_profile_id: <p>The storage profile ID for the storage profile in the queue.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_storage_profile_for_queue_request.GetStorageProfileForQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_storage_profile_for_queue_response.GetStorageProfileForQueueResponse"
        ]:
            import capo_deadline._operations.deadline.get_storage_profile_for_queue

            output, http_response = (
                capo_deadline._operations.deadline.get_storage_profile_for_queue.get_storage_profile_for_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_storage_profile_for_queue_request.GetStorageProfileForQueueRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "storage_profile_id": storage_profile_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_queue_environments(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_queue_environments_response.ListQueueEnvironmentsResponse":
        """<p>Lists queue environments.</p>

        Args:
            farm_id: <p>The farm ID for the queue environment list.</p>
            queue_id: <p>The queue ID for the queue environment list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_queue_environments_request.ListQueueEnvironmentsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_queue_environments_response.ListQueueEnvironmentsResponse"
        ]:
            import capo_deadline._operations.deadline.list_queue_environments

            output, http_response = (
                capo_deadline._operations.deadline.list_queue_environments.list_queue_environments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_queue_environments_request.ListQueueEnvironmentsRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
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

    def iter_list_queue_environments(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.queue_environment_summary.QueueEnvironmentSummary]":
        _token = next_token
        while True:
            _response = self.list_queue_environments(
                farm_id,
                queue_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("environments",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_queue_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_queue_members_response.ListQueueMembersResponse":
        """<p>Lists the members in a queue.</p>

        Args:
            farm_id: <p>The farm ID for the queue.</p>
            queue_id: <p>The queue ID to include on the list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_queue_members_request.ListQueueMembersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_queue_members_response.ListQueueMembersResponse"
        ]:
            import capo_deadline._operations.deadline.list_queue_members

            output, http_response = (
                capo_deadline._operations.deadline.list_queue_members.list_queue_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_queue_members_request.ListQueueMembersRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
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

    def iter_list_queue_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.queue_member.QueueMember]":
        _token = next_token
        while True:
            _response = self.list_queue_members(
                farm_id,
                queue_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_storage_profiles_for_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_storage_profiles_for_queue_response.ListStorageProfilesForQueueResponse":
        """<p>Lists storage profiles for a queue.</p>

        Args:
            farm_id: <p>The farm ID of the queue's storage profile.</p>
            queue_id: <p>The queue ID for the storage profile.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_storage_profiles_for_queue_request.ListStorageProfilesForQueueRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_storage_profiles_for_queue_response.ListStorageProfilesForQueueResponse"
        ]:
            import capo_deadline._operations.deadline.list_storage_profiles_for_queue

            output, http_response = (
                capo_deadline._operations.deadline.list_storage_profiles_for_queue.list_storage_profiles_for_queue(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_storage_profiles_for_queue_request.ListStorageProfilesForQueueRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
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

    def iter_list_storage_profiles_for_queue(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.storage_profile_summary.StorageProfileSummary]":
        _token = next_token
        while True:
            _response = self.list_storage_profiles_for_queue(
                farm_id,
                queue_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("storage_profiles",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_queue_environment(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        queue_environment_id: "capo_deadline.types.queue_environment_id.QueueEnvironmentId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        priority: Optional["capo_deadline.types.priority.Priority"] = None,
        template_type: Optional[
            "capo_deadline.types.environment_template_type.EnvironmentTemplateType"
        ] = None,
        template: Optional[
            "capo_deadline.types.environment_template.EnvironmentTemplate"
        ] = None,
    ) -> "capo_deadline.types.update_queue_environment_response.UpdateQueueEnvironmentResponse":
        """<p>Updates the queue environment.</p>

        Args:
            farm_id: <p>The farm ID of the queue environment to update.</p>
            queue_id: <p>The queue ID of the queue environment to update.</p>
            queue_environment_id: <p>The queue environment ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            priority: <p>The priority to update.</p>
            template_type: <p>The template type to update.</p>
            template: <p>The template to update.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_queue_environment_request.UpdateQueueEnvironmentRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_queue_environment_response.UpdateQueueEnvironmentResponse"
        ]:
            import capo_deadline._operations.deadline.update_queue_environment

            output, http_response = (
                capo_deadline._operations.deadline.update_queue_environment.update_queue_environment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_queue_environment_request.UpdateQueueEnvironmentRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "queue_environment_id": queue_environment_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if priority is not None:
            input_["priority"] = priority
        if template_type is not None:
            input_["template_type"] = template_type
        if template is not None:
            input_["template"] = template

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_job(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        priority: "capo_deadline.types.job_priority.JobPriority",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        template: Optional["capo_deadline.types.job_template.JobTemplate"] = None,
        template_type: Optional[
            "capo_deadline.types.job_template_type.JobTemplateType"
        ] = None,
        parameters: Optional["capo_deadline.types.job_parameters.JobParameters"] = None,
        attachments: Optional["capo_deadline.types.attachments.Attachments"] = None,
        storage_profile_id: Optional[
            "capo_deadline.types.storage_profile_id.StorageProfileId"
        ] = None,
        target_task_run_status: Optional[
            "capo_deadline.types.create_job_target_task_run_status.CreateJobTargetTaskRunStatus"
        ] = None,
        max_failed_tasks_count: Optional[
            "capo_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
        ] = None,
        max_retries_per_task: Optional[
            "capo_deadline.types.max_retries_per_task.MaxRetriesPerTask"
        ] = None,
        max_worker_count: Optional[
            "capo_deadline.types.max_worker_count.MaxWorkerCount"
        ] = None,
        source_job_id: Optional["capo_deadline.types.job_id.JobId"] = None,
        name_override: Optional["capo_deadline.types.job_name.JobName"] = None,
        description_override: Optional[
            "capo_deadline.types.job_description_override.JobDescriptionOverride"
        ] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_job_response.CreateJobResponse":
        r"""<p>Creates a job. A job is a set of instructions that Deadline Cloud uses to schedule and run work on available workers. For more information, see <a href=\"https://docs.aws.amazon.com/deadline-cloud/latest/userguide/deadline-cloud-jobs.html\">Deadline Cloud jobs</a>.</p>

        Args:
            farm_id: <p>The farm ID of the farm to connect to the job.</p>
            queue_id: <p>The ID of the queue that the job is submitted to.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            template: <p>The job template to use for this job.</p>
            template_type: <p>The file type for the job template.</p>
            priority: <p>The priority of the job. The highest priority (first scheduled) is 100. When two jobs have the same priority, the oldest job is scheduled first.</p>
            parameters: <p>The parameters for the job.</p>
            attachments: <p>The attachments for the job. Attach files required for the job to run to a render job.</p>
            storage_profile_id: <p>The storage profile ID for the storage profile to connect to the job.</p>
            target_task_run_status: <p>The initial job status when it is created. Jobs that are created with a <code>SUSPENDED</code> status will not run until manually requeued.</p>
            max_failed_tasks_count: <p>The number of task failures before the job stops running and is marked as <code>FAILED</code>.</p>
            max_retries_per_task: <p>The maximum number of retries for each task.</p>
            max_worker_count: <p>The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.</p> <p>You can't set the <code>maxWorkerCount</code> to 0. If you set it to -1, there is no maximum number of workers.</p> <p>If you don't specify the <code>maxWorkerCount</code>, Deadline Cloud won't throttle the number of workers used to process the job.</p>
            source_job_id: <p>The job ID for the source job.</p>
            name_override: <p>A custom name to override the job name derived from the job template.</p>
            description_override: <p>A custom description to override the job description derived from the job template.</p>
            tags: <p>The tags to add to your job. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_job_request.CreateJobRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_job_response.CreateJobResponse"
        ]:
            import capo_deadline._operations.deadline.create_job

            output, http_response = (
                capo_deadline._operations.deadline.create_job.create_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_job_request.CreateJobRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "priority": priority,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if template is not None:
            input_["template"] = template
        if template_type is not None:
            input_["template_type"] = template_type
        if parameters is not None:
            input_["parameters"] = parameters
        if attachments is not None:
            input_["attachments"] = attachments
        if storage_profile_id is not None:
            input_["storage_profile_id"] = storage_profile_id
        if target_task_run_status is not None:
            input_["target_task_run_status"] = target_task_run_status
        if max_failed_tasks_count is not None:
            input_["max_failed_tasks_count"] = max_failed_tasks_count
        if max_retries_per_task is not None:
            input_["max_retries_per_task"] = max_retries_per_task
        if max_worker_count is not None:
            input_["max_worker_count"] = max_worker_count
        if source_job_id is not None:
            input_["source_job_id"] = source_job_id
        if name_override is not None:
            input_["name_override"] = name_override
        if description_override is not None:
            input_["description_override"] = description_override
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_job(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_job_response.GetJobResponse":
        """<p>Gets a Deadline Cloud job.</p>

        Args:
            farm_id: <p>The farm ID of the farm in the job.</p>
            queue_id: <p>The queue ID associated with the job.</p>
            job_id: <p>The job ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_job_request.GetJobRequest]",
        ) -> OperationResponse["capo_deadline.types.get_job_response.GetJobResponse"]:
            import capo_deadline._operations.deadline.get_job

            output, http_response = capo_deadline._operations.deadline.get_job.get_job(
                req.options, req.input
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_job_request.GetJobRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_job(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        target_task_run_status: Optional[
            "capo_deadline.types.job_target_task_run_status.JobTargetTaskRunStatus"
        ] = None,
        priority: Optional["capo_deadline.types.job_priority.JobPriority"] = None,
        max_failed_tasks_count: Optional[
            "capo_deadline.types.max_failed_tasks_count.MaxFailedTasksCount"
        ] = None,
        max_retries_per_task: Optional[
            "capo_deadline.types.max_retries_per_task.MaxRetriesPerTask"
        ] = None,
        lifecycle_status: Optional[
            "capo_deadline.types.update_job_lifecycle_status.UpdateJobLifecycleStatus"
        ] = None,
        max_worker_count: Optional[
            "capo_deadline.types.max_worker_count.MaxWorkerCount"
        ] = None,
        name: Optional["capo_deadline.types.job_name.JobName"] = None,
        description: Optional[
            "capo_deadline.types.job_description_override.JobDescriptionOverride"
        ] = None,
    ) -> "capo_deadline.types.update_job_response.UpdateJobResponse":
        """<p>Updates a job. </p> <p>When you change the status of the job to <code>ARCHIVED</code>, the job can't be scheduled or archived.</p> <important> <p>An archived jobs and its steps and tasks are deleted after 120 days. The job can't be recovered.</p> </important>

        Args:
            farm_id: <p>The farm ID of the job to update.</p>
            queue_id: <p>The queue ID of the job to update.</p>
            job_id: <p>The job ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            target_task_run_status: <p>The task status to update the job's tasks to.</p>
            priority: <p>The updated job priority.</p>
            max_failed_tasks_count: <p>The number of task failures before the job stops running and is marked as <code>FAILED</code>.</p>
            max_retries_per_task: <p>The maximum number of retries for a job.</p>
            lifecycle_status: <p>The status of a job in its lifecycle. When you change the status of the job to <code>ARCHIVED</code>, the job can't be scheduled or archived.</p> <important> <p>An archived jobs and its steps and tasks are deleted after 120 days. The job can't be recovered.</p> </important>
            max_worker_count: <p>The maximum number of worker hosts that can concurrently process a job. When the <code>maxWorkerCount</code> is reached, no more workers will be assigned to process the job, even if the fleets assigned to the job's queue has available workers.</p> <p>You can't set the <code>maxWorkerCount</code> to 0. If you set it to -1, there is no maximum number of workers.</p> <p>If you don't specify the <code>maxWorkerCount</code>, the default is -1.</p> <p>The maximum number of workers that can process tasks in the job.</p>
            name: <p>The updated job name.</p>
            description: <p>The updated job description.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_job_request.UpdateJobRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_job_response.UpdateJobResponse"
        ]:
            import capo_deadline._operations.deadline.update_job

            output, http_response = (
                capo_deadline._operations.deadline.update_job.update_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_job_request.UpdateJobRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if target_task_run_status is not None:
            input_["target_task_run_status"] = target_task_run_status
        if priority is not None:
            input_["priority"] = priority
        if max_failed_tasks_count is not None:
            input_["max_failed_tasks_count"] = max_failed_tasks_count
        if max_retries_per_task is not None:
            input_["max_retries_per_task"] = max_retries_per_task
        if lifecycle_status is not None:
            input_["lifecycle_status"] = lifecycle_status
        if max_worker_count is not None:
            input_["max_worker_count"] = max_worker_count
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_jobs(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "capo_deadline.types.list_jobs_response.ListJobsResponse":
        """<p>Lists jobs.</p>

        Args:
            farm_id: <p>The farm ID for the jobs.</p>
            queue_id: <p>The queue ID for the job.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            principal_id: <p>The principal ID of the members on the jobs.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_jobs_request.ListJobsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_jobs_response.ListJobsResponse"
        ]:
            import capo_deadline._operations.deadline.list_jobs

            output, http_response = (
                capo_deadline._operations.deadline.list_jobs.list_jobs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_jobs_request.ListJobsRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if principal_id is not None:
            input_["principal_id"] = principal_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_jobs(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        principal_id: Optional[
            "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
        ] = None,
    ) -> "Iterator[capo_deadline.types.job_summary.JobSummary]":
        _token = next_token
        while True:
            _response = self.list_jobs(
                farm_id,
                queue_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                principal_id=principal_id,
            )
            _page = _resolve_path(_response, ("jobs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def associate_member_to_job(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        principal_type: "capo_deadline.types.deadline_principal_type.DeadlinePrincipalType",
        identity_store_id: "capo_deadline.types.identity_store_id.IdentityStoreId",
        membership_level: "capo_deadline.types.membership_level.MembershipLevel",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
    ) -> "capo_deadline.types.associate_member_to_job_response.AssociateMemberToJobResponse":
        """<p>Assigns a job membership level to a member</p>

        Args:
            farm_id: <p>The farm ID of the job to associate with the member.</p>
            queue_id: <p>The queue ID to associate to the member.</p>
            job_id: <p>The job ID to associate with the member.</p>
            principal_type: <p>The member's principal type to associate with the job.</p>
            identity_store_id: <p>The member's identity store ID to associate with the job.</p>
            membership_level: <p>The principal's membership level for the associated job.</p>
            principal_id: <p>The member's principal ID to associate with the job.</p>
            identity_center_region: <p>The Region of the IAM Identity Center instance. If not provided, the service defaults to the Region of the farm.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.associate_member_to_job_request.AssociateMemberToJobRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.associate_member_to_job_response.AssociateMemberToJobResponse"
        ]:
            import capo_deadline._operations.deadline.associate_member_to_job

            output, http_response = (
                capo_deadline._operations.deadline.associate_member_to_job.associate_member_to_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.associate_member_to_job_request.AssociateMemberToJobRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "principal_type": principal_type,
            "identity_store_id": identity_store_id,
            "membership_level": membership_level,
            "principal_id": principal_id,
        }
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def copy_job_template(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        target_s3_location: "capo_deadline.types.s3_location.S3Location",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.copy_job_template_response.CopyJobTemplateResponse":
        """<p>Copies a job template to an Amazon S3 bucket.</p>

        Args:
            farm_id: <p>The farm ID to copy.</p>
            queue_id: <p>The queue ID to copy.</p>
            job_id: <p>The job ID to copy.</p>
            target_s3_location: <p>The Amazon S3 bucket name and key where you would like to add a copy of the job template.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.copy_job_template_request.CopyJobTemplateRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.copy_job_template_response.CopyJobTemplateResponse"
        ]:
            import capo_deadline._operations.deadline.copy_job_template

            output, http_response = (
                capo_deadline._operations.deadline.copy_job_template.copy_job_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.copy_job_template_request.CopyJobTemplateRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "target_s3_location": target_s3_location,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def disassociate_member_from_job(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        principal_id: "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.disassociate_member_from_job_response.DisassociateMemberFromJobResponse":
        """<p>Disassociates a member from a job.</p>

        Args:
            farm_id: <p>The farm ID for the job to disassociate from the member.</p>
            queue_id: <p>The queue ID connected to a job for which you're disassociating a member.</p>
            job_id: <p>The job ID to disassociate from a member in a job.</p>
            principal_id: <p>A member's principal ID to disassociate from a job.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.disassociate_member_from_job_request.DisassociateMemberFromJobRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.disassociate_member_from_job_response.DisassociateMemberFromJobResponse"
        ]:
            import capo_deadline._operations.deadline.disassociate_member_from_job

            output, http_response = (
                capo_deadline._operations.deadline.disassociate_member_from_job.disassociate_member_from_job(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.disassociate_member_from_job_request.DisassociateMemberFromJobRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "principal_id": principal_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        session_id: "capo_deadline.types.session_id.SessionId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_session_response.GetSessionResponse":
        """<p>Gets a session.</p>

        Args:
            farm_id: <p>The farm ID for the session.</p>
            queue_id: <p>The queue ID for the session.</p>
            job_id: <p>The job ID for the session.</p>
            session_id: <p>The session ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_session_request.GetSessionRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_session_response.GetSessionResponse"
        ]:
            import capo_deadline._operations.deadline.get_session

            output, http_response = (
                capo_deadline._operations.deadline.get_session.get_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_session_request.GetSessionRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "session_id": session_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_session_action(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        session_action_id: "capo_deadline.types.session_action_id.SessionActionId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_session_action_response.GetSessionActionResponse":
        """<p>Gets a session action for the job.</p>

        Args:
            farm_id: <p>The farm ID for the session action.</p>
            queue_id: <p>The queue ID for the session action.</p>
            job_id: <p>The job ID for the session.</p>
            session_action_id: <p>The session action ID for the session.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_session_action_request.GetSessionActionRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_session_action_response.GetSessionActionResponse"
        ]:
            import capo_deadline._operations.deadline.get_session_action

            output, http_response = (
                capo_deadline._operations.deadline.get_session_action.get_session_action(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_session_action_request.GetSessionActionRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "session_action_id": session_action_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_step(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_step_response.GetStepResponse":
        """<p>Gets a step.</p>

        Args:
            farm_id: <p>The farm ID for the step.</p>
            queue_id: <p>The queue ID for the step.</p>
            job_id: <p>The job ID for the step.</p>
            step_id: <p>The step ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_step_request.GetStepRequest]",
        ) -> OperationResponse["capo_deadline.types.get_step_response.GetStepResponse"]:
            import capo_deadline._operations.deadline.get_step

            output, http_response = (
                capo_deadline._operations.deadline.get_step.get_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_step_request.GetStepRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "step_id": step_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_task(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        task_id: "capo_deadline.types.task_id.TaskId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_task_response.GetTaskResponse":
        """<p>Gets a task.</p>

        Args:
            farm_id: <p>The farm ID of the farm connected to the task.</p>
            queue_id: <p>The queue ID for the queue connected to the task.</p>
            job_id: <p>The job ID of the job connected to the task.</p>
            step_id: <p>The step ID for the step connected to the task.</p>
            task_id: <p>The task ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_task_request.GetTaskRequest]",
        ) -> OperationResponse["capo_deadline.types.get_task_response.GetTaskResponse"]:
            import capo_deadline._operations.deadline.get_task

            output, http_response = (
                capo_deadline._operations.deadline.get_task.get_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_task_request.GetTaskRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "step_id": step_id,
            "task_id": task_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_job_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_job_members_response.ListJobMembersResponse":
        """<p>Lists members on a job.</p>

        Args:
            farm_id: <p>The farm ID of the job to list.</p>
            queue_id: <p>The queue ID to include on the list.</p>
            job_id: <p>The job ID to include on the list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_job_members_request.ListJobMembersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_job_members_response.ListJobMembersResponse"
        ]:
            import capo_deadline._operations.deadline.list_job_members

            output, http_response = (
                capo_deadline._operations.deadline.list_job_members.list_job_members(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_job_members_request.ListJobMembersRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
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

    def iter_list_job_members(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.job_member.JobMember]":
        _token = next_token
        while True:
            _response = self.list_job_members(
                farm_id,
                queue_id,
                job_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("members",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_job_parameter_definitions(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_job_parameter_definitions_response.ListJobParameterDefinitionsResponse":
        """<p>Lists parameter definitions of a job.</p>

        Args:
            farm_id: <p>The farm ID of the job to list.</p>
            queue_id: <p>The queue ID to include on the list.</p>
            job_id: <p>The job ID to include on the list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_job_parameter_definitions_request.ListJobParameterDefinitionsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_job_parameter_definitions_response.ListJobParameterDefinitionsResponse"
        ]:
            import capo_deadline._operations.deadline.list_job_parameter_definitions

            output, http_response = (
                capo_deadline._operations.deadline.list_job_parameter_definitions.list_job_parameter_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_job_parameter_definitions_request.ListJobParameterDefinitionsRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
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

    def iter_list_job_parameter_definitions(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "Iterator[capo_deadline.types.job_parameter_definition.JobParameterDefinition]"
    ):
        _token = next_token
        while True:
            _response = self.list_job_parameter_definitions(
                farm_id,
                queue_id,
                job_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("job_parameter_definitions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_session_actions(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        session_id: Optional["capo_deadline.types.session_id.SessionId"] = None,
        task_id: Optional["capo_deadline.types.task_id.TaskId"] = None,
    ) -> "capo_deadline.types.list_session_actions_response.ListSessionActionsResponse":
        """<p>Lists session actions.</p>

        Args:
            farm_id: <p>The farm ID for the session actions list.</p>
            queue_id: <p>The queue ID for the session actions list.</p>
            job_id: <p>The job ID for the session actions list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>
            session_id: <p>The session ID to include on the sessions action list.</p>
            task_id: <p>The task ID for the session actions list.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_session_actions_request.ListSessionActionsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_session_actions_response.ListSessionActionsResponse"
        ]:
            import capo_deadline._operations.deadline.list_session_actions

            output, http_response = (
                capo_deadline._operations.deadline.list_session_actions.list_session_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_session_actions_request.ListSessionActionsRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
        }
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if session_id is not None:
            input_["session_id"] = session_id
        if task_id is not None:
            input_["task_id"] = task_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_session_actions(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
        session_id: Optional["capo_deadline.types.session_id.SessionId"] = None,
        task_id: Optional["capo_deadline.types.task_id.TaskId"] = None,
    ) -> "Iterator[capo_deadline.types.session_action_summary.SessionActionSummary]":
        _token = next_token
        while True:
            _response = self.list_session_actions(
                farm_id,
                queue_id,
                job_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                session_id=session_id,
                task_id=task_id,
            )
            _page = _resolve_path(_response, ("session_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_sessions(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_sessions_response.ListSessionsResponse":
        """<p>Lists sessions.</p>

        Args:
            farm_id: <p>The farm ID for the list of sessions.</p>
            queue_id: <p>The queue ID for the list of sessions</p>
            job_id: <p>The job ID for the list of sessions.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_sessions_request.ListSessionsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_sessions_response.ListSessionsResponse"
        ]:
            import capo_deadline._operations.deadline.list_sessions

            output, http_response = (
                capo_deadline._operations.deadline.list_sessions.list_sessions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_sessions_request.ListSessionsRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
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

    def iter_list_sessions(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.session_summary.SessionSummary]":
        _token = next_token
        while True:
            _response = self.list_sessions(
                farm_id,
                queue_id,
                job_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("sessions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_step_consumers(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.integer.Integer"] = None,
    ) -> "capo_deadline.types.list_step_consumers_response.ListStepConsumersResponse":
        """<p>Lists step consumers.</p>

        Args:
            farm_id: <p>The farm ID for the list of step consumers.</p>
            queue_id: <p>The queue ID for the step consumer.</p>
            job_id: <p>The job ID for the step consumer.</p>
            step_id: <p>The step ID to include on the list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_step_consumers_request.ListStepConsumersRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_step_consumers_response.ListStepConsumersResponse"
        ]:
            import capo_deadline._operations.deadline.list_step_consumers

            output, http_response = (
                capo_deadline._operations.deadline.list_step_consumers.list_step_consumers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_step_consumers_request.ListStepConsumersRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "step_id": step_id,
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

    def iter_list_step_consumers(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.integer.Integer"] = None,
    ) -> "Iterator[capo_deadline.types.step_consumer.StepConsumer]":
        _token = next_token
        while True:
            _response = self.list_step_consumers(
                farm_id,
                queue_id,
                job_id,
                step_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("consumers",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_step_dependencies(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.integer.Integer"] = None,
    ) -> "capo_deadline.types.list_step_dependencies_response.ListStepDependenciesResponse":
        """<p>Lists the dependencies for a step.</p>

        Args:
            farm_id: <p>The farm ID for the step dependencies list.</p>
            queue_id: <p>The queue ID for the step dependencies list.</p>
            job_id: <p>The job ID for the step dependencies list.</p>
            step_id: <p>The step ID to include on the list.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_step_dependencies_request.ListStepDependenciesRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_step_dependencies_response.ListStepDependenciesResponse"
        ]:
            import capo_deadline._operations.deadline.list_step_dependencies

            output, http_response = (
                capo_deadline._operations.deadline.list_step_dependencies.list_step_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_step_dependencies_request.ListStepDependenciesRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "step_id": step_id,
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

    def iter_list_step_dependencies(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.integer.Integer"] = None,
    ) -> "Iterator[capo_deadline.types.step_dependency.StepDependency]":
        _token = next_token
        while True:
            _response = self.list_step_dependencies(
                farm_id,
                queue_id,
                job_id,
                step_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("dependencies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_steps(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_steps_response.ListStepsResponse":
        """<p>Lists steps for a job.</p>

        Args:
            farm_id: <p>The farm ID to include on the list of steps.</p>
            queue_id: <p>The queue ID to include on the list of steps.</p>
            job_id: <p>The job ID to include on the list of steps.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_steps_request.ListStepsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_steps_response.ListStepsResponse"
        ]:
            import capo_deadline._operations.deadline.list_steps

            output, http_response = (
                capo_deadline._operations.deadline.list_steps.list_steps(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_steps_request.ListStepsRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
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

    def iter_list_steps(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.step_summary.StepSummary]":
        _token = next_token
        while True:
            _response = self.list_steps(
                farm_id,
                queue_id,
                job_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("steps",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tasks(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_tasks_response.ListTasksResponse":
        """<p>Lists tasks for a job.</p>

        Args:
            farm_id: <p>The farm ID connected to the tasks.</p>
            queue_id: <p>The queue ID connected to the tasks.</p>
            job_id: <p>The job ID for the tasks.</p>
            step_id: <p>The step ID for the tasks.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_tasks_request.ListTasksRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_tasks_response.ListTasksResponse"
        ]:
            import capo_deadline._operations.deadline.list_tasks

            output, http_response = (
                capo_deadline._operations.deadline.list_tasks.list_tasks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_tasks_request.ListTasksRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "step_id": step_id,
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

    def iter_list_tasks(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.task_summary.TaskSummary]":
        _token = next_token
        while True:
            _response = self.list_tasks(
                farm_id,
                queue_id,
                job_id,
                step_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("tasks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def update_session(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        session_id: "capo_deadline.types.session_id.SessionId",
        target_lifecycle_status: "capo_deadline.types.session_lifecycle_target_status.SessionLifecycleTargetStatus",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
    ) -> "capo_deadline.types.update_session_response.UpdateSessionResponse":
        """<p>Updates a session.</p>

        Args:
            farm_id: <p>The farm ID to update in the session.</p>
            queue_id: <p>The queue ID to update in the session.</p>
            job_id: <p>The job ID to update in the session.</p>
            session_id: <p>The session ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            target_lifecycle_status: <p>The life cycle status to update in the session.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_session_request.UpdateSessionRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_session_response.UpdateSessionResponse"
        ]:
            import capo_deadline._operations.deadline.update_session

            output, http_response = (
                capo_deadline._operations.deadline.update_session.update_session(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_session_request.UpdateSessionRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "session_id": session_id,
            "target_lifecycle_status": target_lifecycle_status,
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

    def update_step(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        target_task_run_status: "capo_deadline.types.step_target_task_run_status.StepTargetTaskRunStatus",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
    ) -> "capo_deadline.types.update_step_response.UpdateStepResponse":
        """<p>Updates a step.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            queue_id: <p>The queue ID to update.</p>
            job_id: <p>The job ID to update.</p>
            step_id: <p>The step ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            target_task_run_status: <p>The task status to update the step's tasks to.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_step_request.UpdateStepRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_step_response.UpdateStepResponse"
        ]:
            import capo_deadline._operations.deadline.update_step

            output, http_response = (
                capo_deadline._operations.deadline.update_step.update_step(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_step_request.UpdateStepRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "step_id": step_id,
            "target_task_run_status": target_task_run_status,
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

    def update_task(
        self,
        farm_id: "capo_deadline.types.farm_id.FarmId",
        queue_id: "capo_deadline.types.queue_id.QueueId",
        job_id: "capo_deadline.types.job_id.JobId",
        step_id: "capo_deadline.types.step_id.StepId",
        task_id: "capo_deadline.types.task_id.TaskId",
        target_run_status: "capo_deadline.types.task_target_run_status.TaskTargetRunStatus",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
    ) -> "capo_deadline.types.update_task_response.UpdateTaskResponse":
        """<p>Updates a task.</p>

        Args:
            farm_id: <p>The farm ID to update.</p>
            queue_id: <p>The queue ID to update.</p>
            job_id: <p>The job ID to update.</p>
            step_id: <p>The step ID to update.</p>
            task_id: <p>The task ID to update.</p>
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            target_run_status: <p>The run status with which to start the task.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_task_request.UpdateTaskRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_task_response.UpdateTaskResponse"
        ]:
            import capo_deadline._operations.deadline.update_task

            output, http_response = (
                capo_deadline._operations.deadline.update_task.update_task(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_task_request.UpdateTaskRequest = {
            "farm_id": farm_id,
            "queue_id": queue_id,
            "job_id": job_id,
            "step_id": step_id,
            "task_id": task_id,
            "target_run_status": target_run_status,
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

    def create_license_endpoint(
        self,
        vpc_id: "capo_deadline.types.vpc_id.VpcId",
        subnet_ids: "capo_deadline.types.subnet_id_list.SubnetIdList",
        security_group_ids: "capo_deadline.types.security_group_id_list.SecurityGroupIdList",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse":
        """<p>Creates a license endpoint to integrate your various licensed software used for rendering on Deadline Cloud.</p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            vpc_id: <p>The VPC (virtual private cloud) ID to use with the license endpoint.</p>
            subnet_ids: <p>The subnet IDs.</p>
            security_group_ids: <p>The security group IDs.</p>
            tags: <p>Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_license_endpoint_response.CreateLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.create_license_endpoint

            output, http_response = (
                capo_deadline._operations.deadline.create_license_endpoint.create_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_license_endpoint_request.CreateLicenseEndpointRequest = {
            "vpc_id": vpc_id,
            "subnet_ids": subnet_ids,
            "security_group_ids": security_group_ids,
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

    def get_license_endpoint(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse":
        """<p>Gets a licence endpoint.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_license_endpoint_response.GetLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.get_license_endpoint

            output, http_response = (
                capo_deadline._operations.deadline.get_license_endpoint.get_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_license_endpoint_request.GetLicenseEndpointRequest = {
            "license_endpoint_id": license_endpoint_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_license_endpoint(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse":
        """<p>Deletes a license endpoint.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID of the license endpoint to delete.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.conflict_exception.ConflictException: <p>Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_license_endpoint_response.DeleteLicenseEndpointResponse"
        ]:
            import capo_deadline._operations.deadline.delete_license_endpoint

            output, http_response = (
                capo_deadline._operations.deadline.delete_license_endpoint.delete_license_endpoint(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_license_endpoint_request.DeleteLicenseEndpointRequest = {
            "license_endpoint_id": license_endpoint_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_license_endpoints(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse":
        """<p>Lists license endpoints.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_license_endpoints_response.ListLicenseEndpointsResponse"
        ]:
            import capo_deadline._operations.deadline.list_license_endpoints

            output, http_response = (
                capo_deadline._operations.deadline.list_license_endpoints.list_license_endpoints(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_license_endpoints_request.ListLicenseEndpointsRequest = {}
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

    def iter_list_license_endpoints(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "Iterator[capo_deadline.types.license_endpoint_summary.LicenseEndpointSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_license_endpoints(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("license_endpoints",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def delete_metered_product(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "capo_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse":
        """<p>Deletes a metered product.</p>

        Args:
            license_endpoint_id: <p>The ID of the license endpoint from which to remove the metered product.</p>
            product_id: <p>The product ID to remove from the license endpoint.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_metered_product_response.DeleteMeteredProductResponse"
        ]:
            import capo_deadline._operations.deadline.delete_metered_product

            output, http_response = (
                capo_deadline._operations.deadline.delete_metered_product.delete_metered_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_metered_product_request.DeleteMeteredProductRequest = {
            "license_endpoint_id": license_endpoint_id,
            "product_id": product_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_metered_products(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> (
        "capo_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
    ):
        """<p>Lists metered products.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID to include on the list of metered products.</p>
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_metered_products_request.ListMeteredProductsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_metered_products_response.ListMeteredProductsResponse"
        ]:
            import capo_deadline._operations.deadline.list_metered_products

            output, http_response = (
                capo_deadline._operations.deadline.list_metered_products.list_metered_products(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_metered_products_request.ListMeteredProductsRequest = {
            "license_endpoint_id": license_endpoint_id
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

    def iter_list_metered_products(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.metered_product_summary.MeteredProductSummary]":
        _token = next_token
        while True:
            _response = self.list_metered_products(
                license_endpoint_id,
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("metered_products",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_metered_product(
        self,
        license_endpoint_id: "capo_deadline.types.license_endpoint_id.LicenseEndpointId",
        product_id: "capo_deadline.types.metered_product_id.MeteredProductId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.put_metered_product_response.PutMeteredProductResponse":
        """<p>Adds a metered product.</p>

        Args:
            license_endpoint_id: <p>The license endpoint ID to add to the metered product.</p>
            product_id: <p>The product ID to add to the metered product.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.put_metered_product_request.PutMeteredProductRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.put_metered_product_response.PutMeteredProductResponse"
        ]:
            import capo_deadline._operations.deadline.put_metered_product

            output, http_response = (
                capo_deadline._operations.deadline.put_metered_product.put_metered_product(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.put_metered_product_request.PutMeteredProductRequest = {
            "license_endpoint_id": license_endpoint_id,
            "product_id": product_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_monitor(
        self,
        display_name: "capo_deadline.types.resource_name.ResourceName",
        identity_center_instance_arn: "capo_deadline.types.identity_center_instance_arn.IdentityCenterInstanceArn",
        subdomain: "capo_deadline.types.subdomain.Subdomain",
        role_arn: "capo_deadline.types.iam_role_arn.IamRoleArn",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        client_token: Optional["capo_deadline.types.client_token.ClientToken"] = None,
        identity_center_region: Optional["capo_deadline.types.region.Region"] = None,
        tags: Optional["capo_deadline.types.tags.Tags"] = None,
    ) -> "capo_deadline.types.create_monitor_response.CreateMonitorResponse":
        """<p>Creates an Amazon Web Services Deadline Cloud monitor that you can use to view your farms, queues, and fleets. After you submit a job, you can track the progress of the tasks and steps that make up the job, and then download the job's results. </p>

        Args:
            client_token: <p>The unique token which the server uses to recognize retries of the same request.</p>
            display_name: <p>The name that you give the monitor that is displayed in the Deadline Cloud console.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            identity_center_instance_arn: <p>The Amazon Resource Name of the IAM Identity Center instance that authenticates monitor users.</p>
            identity_center_region: <p>The Region where IAM Identity Center is enabled. Required when IAM Identity Center is in a different Region than the monitor.</p>
            subdomain: <p>The subdomain to use when creating the monitor URL. The full URL of the monitor is subdomain.Region.deadlinecloud.amazonaws.com.</p>
            role_arn: <p>The Amazon Resource Name of the IAM role that the monitor uses to connect to Deadline Cloud. Every user that signs in to the monitor using IAM Identity Center uses this role to access Deadline Cloud resources.</p>
            tags: <p>The tags to add to your monitor. Each tag consists of a tag key and a tag value. Tag keys and values are both required, but tag values can be empty strings.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>You exceeded your service quota. Service quotas, also referred to as limits, are the maximum number of service resources or operations for your Amazon Web Services account.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.create_monitor_request.CreateMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.create_monitor_response.CreateMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.create_monitor

            output, http_response = (
                capo_deadline._operations.deadline.create_monitor.create_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.create_monitor_request.CreateMonitorRequest = {
            "display_name": display_name,
            "identity_center_instance_arn": identity_center_instance_arn,
            "subdomain": subdomain,
            "role_arn": role_arn,
        }
        if client_token is None:
            client_token = str(uuid.uuid4())
        input_["client_token"] = client_token
        if identity_center_region is not None:
            input_["identity_center_region"] = identity_center_region
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_monitor(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_monitor_response.GetMonitorResponse":
        """<p>Gets information about the specified monitor.</p>

        Args:
            monitor_id: <p>The unique identifier for the monitor. This ID is returned by the <code>CreateMonitor</code> operation.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_monitor_request.GetMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_monitor_response.GetMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.get_monitor

            output, http_response = (
                capo_deadline._operations.deadline.get_monitor.get_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_monitor_request.GetMonitorRequest = {
            "monitor_id": monitor_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_monitor(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        subdomain: Optional["capo_deadline.types.subdomain.Subdomain"] = None,
        display_name: Optional["capo_deadline.types.resource_name.ResourceName"] = None,
        role_arn: Optional["capo_deadline.types.iam_role_arn.IamRoleArn"] = None,
    ) -> "capo_deadline.types.update_monitor_response.UpdateMonitorResponse":
        """<p>Modifies the settings for a Deadline Cloud monitor. You can modify one or all of the settings when you call <code>UpdateMonitor</code>.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to update.</p>
            subdomain: <p>The new value of the subdomain to use when forming the monitor URL.</p>
            display_name: <p>The new value to use for the monitor's display name.</p> <important> <p>This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.</p> </important>
            role_arn: <p>The Amazon Resource Name of the new IAM role to use with the monitor.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_monitor_request.UpdateMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_monitor_response.UpdateMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.update_monitor

            output, http_response = (
                capo_deadline._operations.deadline.update_monitor.update_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_monitor_request.UpdateMonitorRequest = {
            "monitor_id": monitor_id
        }
        if subdomain is not None:
            input_["subdomain"] = subdomain
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

    def delete_monitor(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.delete_monitor_response.DeleteMonitorResponse":
        """<p>Removes a Deadline Cloud monitor. After you delete a monitor, you can create a new one and attach farms to the monitor.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to delete. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>GetMonitor</code> operation.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.delete_monitor_request.DeleteMonitorRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.delete_monitor_response.DeleteMonitorResponse"
        ]:
            import capo_deadline._operations.deadline.delete_monitor

            output, http_response = (
                capo_deadline._operations.deadline.delete_monitor.delete_monitor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.delete_monitor_request.DeleteMonitorRequest = {
            "monitor_id": monitor_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_monitors(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "capo_deadline.types.list_monitors_response.ListMonitorsResponse":
        """<p>Gets a list of your monitors in Deadline Cloud.</p>

        Args:
            next_token: <p>The token for the next set of results, or <code>null</code> to start from the beginning.</p>
            max_results: <p>The maximum number of results to return. Use this parameter with <code>NextToken</code> to get results as a set of sequential pages.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.list_monitors_request.ListMonitorsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.list_monitors_response.ListMonitorsResponse"
        ]:
            import capo_deadline._operations.deadline.list_monitors

            output, http_response = (
                capo_deadline._operations.deadline.list_monitors.list_monitors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.list_monitors_request.ListMonitorsRequest = {}
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

    def iter_list_monitors(
        self,
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
        next_token: Optional["capo_deadline.types.next_token.NextToken"] = None,
        max_results: Optional["capo_deadline.types.max_results.MaxResults"] = None,
    ) -> "Iterator[capo_deadline.types.monitor_summary.MonitorSummary]":
        _token = next_token
        while True:
            _response = self.list_monitors(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("monitors",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_monitor_settings(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse":
        """<p>Gets the settings for a Deadline Cloud monitor.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor. This ID is returned by the <code>CreateMonitor</code> operation, and is included in the response to the <code>ListMonitors</code> operation.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Get monitor settings

            >>> client.get_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef')
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.get_monitor_settings_response.GetMonitorSettingsResponse"
        ]:
            import capo_deadline._operations.deadline.get_monitor_settings

            output, http_response = (
                capo_deadline._operations.deadline.get_monitor_settings.get_monitor_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.get_monitor_settings_request.GetMonitorSettingsRequest = {
            "monitor_id": monitor_id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_monitor_settings(
        self,
        monitor_id: "capo_deadline.types.monitor_id.MonitorId",
        settings: "capo_deadline.types.settings_map.SettingsMap",
        *,
        config_overrides: Optional[deadlineClientConfig] = None,
    ) -> "capo_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse":
        """<p>Updates the settings for a Deadline Cloud monitor. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.</p>

        Args:
            monitor_id: <p>The unique identifier of the monitor to update settings for.</p>
            settings: <p>The monitor settings to update as key-value pairs. Keys present in the request are upserted; keys absent are left unchanged. Send an empty string value to delete a key.</p>

        Raises:
            capo_deadline.errors.access_denied_exception.AccessDeniedException: <p>You don't have permission to perform the action.</p>
            capo_deadline.errors.internal_server_error_exception.InternalServerErrorException: <p>Deadline Cloud can't process your request right now. Try again later.</p>
            capo_deadline.errors.resource_not_found_exception.ResourceNotFoundException: <p>The requested resource can't be found.</p>
            capo_deadline.errors.throttling_exception.ThrottlingException: <p>Your request exceeded a request rate quota.</p>
            capo_deadline.errors.validation_exception.ValidationException: <p>The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters.</p>
            capo_deadline.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            Update monitor settings

            >>> client.update_monitor_settings(monitor_id='monitor-1234567890abcdef1234567890abcdef', settings={'idcApplicationArn': 'arn:aws:sso::123456789012:application/ins-1234567890abcdef/apl-1234567890abcdef'})
        """

        def _handler(
            req: "OperationRequest[capo_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest]",
        ) -> OperationResponse[
            "capo_deadline.types.update_monitor_settings_response.UpdateMonitorSettingsResponse"
        ]:
            import capo_deadline._operations.deadline.update_monitor_settings

            output, http_response = (
                capo_deadline._operations.deadline.update_monitor_settings.update_monitor_settings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_deadline.types.update_monitor_settings_request.UpdateMonitorSettingsRequest = {
            "monitor_id": monitor_id,
            "settings": settings,
        }

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
