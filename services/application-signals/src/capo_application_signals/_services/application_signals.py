"""Generated from Smithy shape ``com.amazonaws.applicationsignals#ApplicationSignals``."""

import datetime
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_application_signals._auth._signers
import capo_application_signals._auth._sigv4
from capo_application_signals._auth._identity import Credentials
from capo_application_signals._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_application_signals._auth._zapros_handler import AuthMiddleware
from capo_application_signals._pagination import resolve_path as _resolve_path
from capo_application_signals._resources.application_signals.service_level_objective_resource import (
    ServiceLevelObjectiveResource,
)
from capo_application_signals._services._aws_config import aws_config
from capo_application_signals._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_application_signals.types.amazon_resource_name
    import capo_application_signals.types.attribute_filters
    import capo_application_signals.types.attributes
    import capo_application_signals.types.audit_targets
    import capo_application_signals.types.auditors
    import capo_application_signals.types.aws_account_id
    import capo_application_signals.types.batch_delete_deletion_target
    import capo_application_signals.types.batch_delete_instrumentation_configurations_request
    import capo_application_signals.types.batch_delete_instrumentation_configurations_response
    import capo_application_signals.types.batch_get_service_level_objective_budget_report_input
    import capo_application_signals.types.batch_get_service_level_objective_budget_report_output
    import capo_application_signals.types.batch_update_exclusion_windows_input
    import capo_application_signals.types.batch_update_exclusion_windows_output
    import capo_application_signals.types.burn_rate_configurations
    import capo_application_signals.types.capture_configuration
    import capo_application_signals.types.change_event
    import capo_application_signals.types.create_instrumentation_configuration_request
    import capo_application_signals.types.create_instrumentation_configuration_response
    import capo_application_signals.types.create_service_level_objective_input
    import capo_application_signals.types.create_service_level_objective_output
    import capo_application_signals.types.delete_grouping_configuration_output
    import capo_application_signals.types.delete_instrumentation_configuration_request
    import capo_application_signals.types.delete_instrumentation_configuration_response
    import capo_application_signals.types.delete_service_level_objective_input
    import capo_application_signals.types.delete_service_level_objective_output
    import capo_application_signals.types.dependency_config
    import capo_application_signals.types.detail_level
    import capo_application_signals.types.dynamic_instrumentation_attribute_filters
    import capo_application_signals.types.dynamic_instrumentation_signal_type
    import capo_application_signals.types.exclusion_window
    import capo_application_signals.types.exclusion_windows
    import capo_application_signals.types.get_instrumentation_configuration_request
    import capo_application_signals.types.get_instrumentation_configuration_response
    import capo_application_signals.types.get_instrumentation_configuration_status_request
    import capo_application_signals.types.get_instrumentation_configuration_status_response
    import capo_application_signals.types.get_service_input
    import capo_application_signals.types.get_service_level_objective_input
    import capo_application_signals.types.get_service_level_objective_output
    import capo_application_signals.types.get_service_output
    import capo_application_signals.types.goal
    import capo_application_signals.types.grouping_attribute_definitions
    import capo_application_signals.types.instrumentation_configuration_status
    import capo_application_signals.types.instrumentation_configuration_status_list
    import capo_application_signals.types.instrumentation_configuration_without_service_env
    import capo_application_signals.types.instrumentation_configurations_page
    import capo_application_signals.types.instrumentation_status_event
    import capo_application_signals.types.instrumentation_type
    import capo_application_signals.types.list_audit_finding_max_results
    import capo_application_signals.types.list_audit_findings_input
    import capo_application_signals.types.list_audit_findings_output
    import capo_application_signals.types.list_entity_events_input
    import capo_application_signals.types.list_entity_events_max_results
    import capo_application_signals.types.list_entity_events_output
    import capo_application_signals.types.list_grouping_attribute_definitions_input
    import capo_application_signals.types.list_grouping_attribute_definitions_output
    import capo_application_signals.types.list_instrumentation_configurations_request
    import capo_application_signals.types.list_service_dependencies_input
    import capo_application_signals.types.list_service_dependencies_max_results
    import capo_application_signals.types.list_service_dependencies_output
    import capo_application_signals.types.list_service_dependents_input
    import capo_application_signals.types.list_service_dependents_max_results
    import capo_application_signals.types.list_service_dependents_output
    import capo_application_signals.types.list_service_level_objective_exclusion_windows_input
    import capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results
    import capo_application_signals.types.list_service_level_objective_exclusion_windows_output
    import capo_application_signals.types.list_service_level_objectives_input
    import capo_application_signals.types.list_service_level_objectives_max_results
    import capo_application_signals.types.list_service_level_objectives_output
    import capo_application_signals.types.list_service_operation_max_results
    import capo_application_signals.types.list_service_operations_input
    import capo_application_signals.types.list_service_operations_output
    import capo_application_signals.types.list_service_states_input
    import capo_application_signals.types.list_service_states_max_results
    import capo_application_signals.types.list_service_states_output
    import capo_application_signals.types.list_services_input
    import capo_application_signals.types.list_services_max_results
    import capo_application_signals.types.list_services_output
    import capo_application_signals.types.list_tags_for_resource_request
    import capo_application_signals.types.list_tags_for_resource_response
    import capo_application_signals.types.location
    import capo_application_signals.types.location_identifier
    import capo_application_signals.types.metric_source
    import capo_application_signals.types.metric_source_types
    import capo_application_signals.types.next_token
    import capo_application_signals.types.operation_name
    import capo_application_signals.types.put_grouping_configuration_input
    import capo_application_signals.types.put_grouping_configuration_output
    import capo_application_signals.types.report_instrumentation_configuration_status_request
    import capo_application_signals.types.report_instrumentation_configuration_status_response
    import capo_application_signals.types.request_based_service_level_indicator_config
    import capo_application_signals.types.service_dependency
    import capo_application_signals.types.service_dependent
    import capo_application_signals.types.service_level_indicator_config
    import capo_application_signals.types.service_level_objective_description
    import capo_application_signals.types.service_level_objective_id
    import capo_application_signals.types.service_level_objective_ids
    import capo_application_signals.types.service_level_objective_name
    import capo_application_signals.types.service_level_objective_summary
    import capo_application_signals.types.service_operation
    import capo_application_signals.types.service_state
    import capo_application_signals.types.service_summary
    import capo_application_signals.types.start_discovery_input
    import capo_application_signals.types.start_discovery_output
    import capo_application_signals.types.tag_key_list
    import capo_application_signals.types.tag_list
    import capo_application_signals.types.tag_resource_request
    import capo_application_signals.types.tag_resource_response
    import capo_application_signals.types.untag_resource_request
    import capo_application_signals.types.untag_resource_response
    import capo_application_signals.types.update_service_level_objective_input
    import capo_application_signals.types.update_service_level_objective_output


class ApplicationSignalsClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    use_fips: bool | None
    endpoint: str | None
    region: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class ApplicationSignalsClient:
    """A client for the ``ApplicationSignals`` service.

    Args:
        http_handler: HTTP handler for sending requests. If not provided, creates a default handler.
        operation_interceptors: Interceptors that wrap every operation call. If not provided, defaults to an empty list.
        retry_max_attempts: Maximum number of times to retry a failed operation. Defaults to 3.
        use_fips: The value of the ``AWS::UseFIPS`` endpoint parameter.
        endpoint: The value of the ``SDK::Endpoint`` endpoint parameter.
        region: The value of the ``AWS::Region`` endpoint parameter.
        credentials: AWS credentials for request signing.
        credentials_provider: Provider that resolves AWS credentials. Takes precedence over ``credentials``.
    """

    def __init__(
        self,
        http_handler: BaseHandler | None = None,
        operation_interceptors: Iterable[Interceptor[Any, Any]] | None = None,
        retry_max_attempts: int | None = None,
        use_fips: bool | None = None,
        endpoint: str | None = None,
        region: str | None = None,
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
        self._config = ApplicationSignalsClientConfig(
            {
                "operation_interceptors": operation_interceptors or [],
                "retry_max_attempts": retry_max_attempts,
                "use_fips": use_fips,
                "endpoint": endpoint,
                "region": region,
                "credentials_provider": resolved_credentials_provider,
            }
        )

        # resources
        self.service_level_objective_resource = ServiceLevelObjectiveResource(self)

    def operation_options(
        self, config_overrides: Optional[ApplicationSignalsClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: ApplicationSignalsClientConfig = config_overrides or {}
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
            use_fips=overrides.get("use_fips", self._config.get("use_fips")),
            endpoint=overrides.get("endpoint", self._config.get("endpoint")),
            region=overrides.get("region", self._config.get("region")),
            credentials_provider=overrides.get(
                "credentials_provider", self._config.get("credentials_provider")
            ),
        )
        return interceptors_, options_

    def batch_delete_instrumentation_configurations(
        self,
        deletion_target: "capo_application_signals.types.batch_delete_deletion_target.BatchDeleteDeletionTarget",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.batch_delete_instrumentation_configurations_response.BatchDeleteInstrumentationConfigurationsResponse":
        """Deletes multiple instrumentation configurations in a single request. Supports two mutually exclusive selection methods: - By scope: Delete all configurations matching a Service + Environment + InstrumentationType - By ARN list: Delete specific configurations by providing a list of resource ARNs

        Args:
            deletion_target: The deletion target - either bulk by scope or targeted by ARN list.

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.batch_delete_instrumentation_configurations_request.BatchDeleteInstrumentationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.batch_delete_instrumentation_configurations_response.BatchDeleteInstrumentationConfigurationsResponse"
        ]:
            import capo_application_signals._operations.application_signals.batch_delete_instrumentation_configurations

            output, http_response = (
                capo_application_signals._operations.application_signals.batch_delete_instrumentation_configurations.batch_delete_instrumentation_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.batch_delete_instrumentation_configurations_request.BatchDeleteInstrumentationConfigurationsRequest = {
            "deletion_target": deletion_target
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_get_service_level_objective_budget_report(
        self,
        timestamp: datetime.datetime,
        slo_ids: "capo_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.batch_get_service_level_objective_budget_report_output.BatchGetServiceLevelObjectiveBudgetReportOutput":
        """<p>Use this operation to retrieve one or more <i>service level objective (SLO) budget reports</i>.</p> <p>An <i>error budget</i> is the amount of time or requests in an unhealthy state that your service can accumulate during an interval before your overall SLO budget health is breached and the SLO is considered to be unmet. For example, an SLO with a threshold of 99.95% and a monthly interval translates to an error budget of 21.9 minutes of downtime in a 30-day month.</p> <p>Budget reports include a health indicator, the attainment value, and remaining budget.</p> <p>For more information about SLO error budgets, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html#CloudWatch-ServiceLevelObjectives-concepts"> SLO concepts</a>.</p>

        Args:
            timestamp: <p>The date and time that you want the report to be for. It is expressed as the number of milliseconds since Jan 1, 1970 00:00:00 UTC.</p>
            slo_ids: <p>An array containing the IDs of the service level objectives that you want to include in the report.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.batch_get_service_level_objective_budget_report_input.BatchGetServiceLevelObjectiveBudgetReportInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.batch_get_service_level_objective_budget_report_output.BatchGetServiceLevelObjectiveBudgetReportOutput"
        ]:
            import capo_application_signals._operations.application_signals.batch_get_service_level_objective_budget_report

            output, http_response = (
                capo_application_signals._operations.application_signals.batch_get_service_level_objective_budget_report.batch_get_service_level_objective_budget_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.batch_get_service_level_objective_budget_report_input.BatchGetServiceLevelObjectiveBudgetReportInput = {
            "timestamp": timestamp,
            "slo_ids": slo_ids,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_update_exclusion_windows(
        self,
        slo_ids: "capo_application_signals.types.service_level_objective_ids.ServiceLevelObjectiveIds",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        add_exclusion_windows: Optional[
            "capo_application_signals.types.exclusion_windows.ExclusionWindows"
        ] = None,
        remove_exclusion_windows: Optional[
            "capo_application_signals.types.exclusion_windows.ExclusionWindows"
        ] = None,
    ) -> "capo_application_signals.types.batch_update_exclusion_windows_output.BatchUpdateExclusionWindowsOutput":
        """<p>Add or remove time window exclusions for one or more Service Level Objectives (SLOs).</p>

        Args:
            slo_ids: <p>The list of SLO IDs to add or remove exclusion windows from.</p>
            add_exclusion_windows: <p>A list of exclusion windows to add to the specified SLOs. You can add up to 10 exclusion windows per SLO.</p>
            remove_exclusion_windows: <p>A list of exclusion windows to remove from the specified SLOs. The window configuration must match an existing exclusion window.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.batch_update_exclusion_windows_input.BatchUpdateExclusionWindowsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.batch_update_exclusion_windows_output.BatchUpdateExclusionWindowsOutput"
        ]:
            import capo_application_signals._operations.application_signals.batch_update_exclusion_windows

            output, http_response = (
                capo_application_signals._operations.application_signals.batch_update_exclusion_windows.batch_update_exclusion_windows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.batch_update_exclusion_windows_input.BatchUpdateExclusionWindowsInput = {
            "slo_ids": slo_ids
        }
        if add_exclusion_windows is not None:
            input_["add_exclusion_windows"] = add_exclusion_windows
        if remove_exclusion_windows is not None:
            input_["remove_exclusion_windows"] = remove_exclusion_windows

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_instrumentation_configuration(
        self,
        instrumentation_type: "capo_application_signals.types.instrumentation_type.InstrumentationType",
        service: str,
        environment: str,
        signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType",
        location: "capo_application_signals.types.location.Location",
        capture_configuration: "capo_application_signals.types.capture_configuration.CaptureConfiguration",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        description: Optional[str] = None,
        expires_at: Optional[datetime.datetime] = None,
        attribute_filters: Optional[
            "capo_application_signals.types.dynamic_instrumentation_attribute_filters.DynamicInstrumentationAttributeFilters"
        ] = None,
        tags: Optional["capo_application_signals.types.tag_list.TagList"] = None,
    ) -> "capo_application_signals.types.create_instrumentation_configuration_response.CreateInstrumentationConfigurationResponse":
        """<p>Creates a dynamic instrumentation configuration for a specific code or endpoint location within a service and environment. Configurations are immutable after creation.</p> <p>For <code>BREAKPOINT</code> type configurations, they expire after 24 hours unless a shorter expiration is provided. For <code>PROBE</code> type configurations, they persist until explicitly deleted; an expiration cannot be set for <code>PROBE</code> configurations.</p> <p>If a configuration already exists for the same service, environment, signal type, and location, this operation returns a conflict instead of overwriting it. Use attribute filters and capture settings to control where the instrumentation runs and which data is collected.</p>

        Args:
            instrumentation_type: Type of instrumentation: BREAKPOINT (temporary) or PROBE (permanent)
            service: <p>The name of the service to instrument. This should match the <code>service.name</code> resource attribute reported by the application.</p>
            environment: <p>The environment that the service is running in, such as <code>eks:cluster-prod/namespace</code> or <code>ec2:production</code>.</p>
            signal_type: <p>The telemetry signal type to emit for this instrumentation. The supported value is <code>SNAPSHOT</code>.</p>
            location: <p>The location where instrumentation should be applied. Specify a <code>CodeLocation</code> for code-level instrumentation.</p>
            description: <p>An optional short description (up to 50 characters) that explains the purpose of this instrumentation.</p>
            expires_at: For BREAKPOINT: optional, defaults to 24 hours, must be between 5 min and 24 hours. For PROBE: not supported. PROBE configurations are permanent and persist until explicitly deleted.
            attribute_filters: <p>Client-side filters that target specific instances. Each object in the array is AND-matched on its keys, and multiple objects are OR-matched to decide where to apply the instrumentation.</p>
            capture_configuration: <p>Specifies what to capture when the instrumentation point is hit. Specify <code>CodeCapture</code> for code-level capture settings.</p>
            tags: <p>An optional list of key-value pairs to associate with the instrumentation configuration. Tags can help you organize and categorize your resources.</p>

        Raises:
            capo_application_signals.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_application_signals.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.create_instrumentation_configuration_request.CreateInstrumentationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.create_instrumentation_configuration_response.CreateInstrumentationConfigurationResponse"
        ]:
            import capo_application_signals._operations.application_signals.create_instrumentation_configuration

            output, http_response = (
                capo_application_signals._operations.application_signals.create_instrumentation_configuration.create_instrumentation_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.create_instrumentation_configuration_request.CreateInstrumentationConfigurationRequest = {
            "instrumentation_type": instrumentation_type,
            "service": service,
            "environment": environment,
            "signal_type": signal_type,
            "location": location,
            "capture_configuration": capture_configuration,
        }
        if description is not None:
            input_["description"] = description
        if expires_at is not None:
            input_["expires_at"] = expires_at
        if attribute_filters is not None:
            input_["attribute_filters"] = attribute_filters
        if tags is not None:
            input_["tags"] = tags

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_grouping_configuration(
        self, *, config_overrides: Optional[ApplicationSignalsClientConfig] = None
    ) -> "capo_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput":
        """<p>Deletes the grouping configuration for this account. This removes all custom grouping attribute definitions that were previously configured.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[None]",
        ) -> OperationResponse[
            "capo_application_signals.types.delete_grouping_configuration_output.DeleteGroupingConfigurationOutput"
        ]:
            import capo_application_signals._operations.application_signals.delete_grouping_configuration

            output, http_response = (
                capo_application_signals._operations.application_signals.delete_grouping_configuration.delete_grouping_configuration(
                    req.options
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)

        response = execute_pipeline(
            OperationRequest(input=None, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_instrumentation_configuration(
        self,
        instrumentation_type: "capo_application_signals.types.instrumentation_type.InstrumentationType",
        service: str,
        environment: str,
        signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType",
        location_identifier: "capo_application_signals.types.location_identifier.LocationIdentifier",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.delete_instrumentation_configuration_response.DeleteInstrumentationConfigurationResponse":
        """<p>Deletes the specified instrumentation configuration. SDKs remove the instrumentation during their next sync after the configuration is deleted or expires.</p>

        Args:
            instrumentation_type: Type of instrumentation configuration (BREAKPOINT or PROBE). Required to identify the configuration to delete.
            service: Service name for the instrumentation configuration.
            environment: Environment name for the instrumentation configuration.
            signal_type: Signal type for the instrumentation configuration.
            location_identifier: Location identifier - either full code location or a pre-computed hash.

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.delete_instrumentation_configuration_request.DeleteInstrumentationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.delete_instrumentation_configuration_response.DeleteInstrumentationConfigurationResponse"
        ]:
            import capo_application_signals._operations.application_signals.delete_instrumentation_configuration

            output, http_response = (
                capo_application_signals._operations.application_signals.delete_instrumentation_configuration.delete_instrumentation_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.delete_instrumentation_configuration_request.DeleteInstrumentationConfigurationRequest = {
            "instrumentation_type": instrumentation_type,
            "service": service,
            "environment": environment,
            "signal_type": signal_type,
            "location_identifier": location_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_instrumentation_configuration(
        self,
        instrumentation_type: "capo_application_signals.types.instrumentation_type.InstrumentationType",
        service: str,
        environment: str,
        signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType",
        location_identifier: "capo_application_signals.types.location_identifier.LocationIdentifier",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.get_instrumentation_configuration_response.GetInstrumentationConfigurationResponse":
        """<p>Returns the details of a single instrumentation configuration identified by service, environment, signal type, and location. Use this to audit or display configuration details.</p>

        Args:
            instrumentation_type: Type of instrumentation configuration (BREAKPOINT or PROBE). Required to identify the configuration to retrieve.
            service: Service name for the instrumentation configuration.
            environment: Environment name for the instrumentation configuration.
            signal_type: Signal type for the instrumentation configuration.
            location_identifier: Location identifier - either full code location or a pre-computed hash.

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.get_instrumentation_configuration_request.GetInstrumentationConfigurationRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.get_instrumentation_configuration_response.GetInstrumentationConfigurationResponse"
        ]:
            import capo_application_signals._operations.application_signals.get_instrumentation_configuration

            output, http_response = (
                capo_application_signals._operations.application_signals.get_instrumentation_configuration.get_instrumentation_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.get_instrumentation_configuration_request.GetInstrumentationConfigurationRequest = {
            "instrumentation_type": instrumentation_type,
            "service": service,
            "environment": environment,
            "signal_type": signal_type,
            "location_identifier": location_identifier,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_instrumentation_configuration_status(
        self,
        instrumentation_type: "capo_application_signals.types.instrumentation_type.InstrumentationType",
        service: str,
        environment: str,
        signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType",
        location_identifier: "capo_application_signals.types.location_identifier.LocationIdentifier",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        status: Optional[
            "capo_application_signals.types.instrumentation_configuration_status.InstrumentationConfigurationStatus"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.get_instrumentation_configuration_status_response.GetInstrumentationConfigurationStatusResponse":
        """<p>Retrieves the status history for a single instrumentation configuration during a specified time range. The response lists when the configuration was ACTIVE, READY, ERROR, or DISABLED.</p> <p>If no status or time window is provided, the operation defaults to ACTIVE events from the last hour.</p>

        Args:
            instrumentation_type: Type of instrumentation configuration (BREAKPOINT or PROBE). Required to identify the configuration to retrieve.
            service: Service name for the instrumentation configuration.
            environment: Environment name for the instrumentation configuration.
            signal_type: Signal type for the instrumentation configuration.
            location_identifier: Location identifier - either full code location or a pre-computed hash.
            status: <p>The single status to query for. If omitted, only <code>ACTIVE</code> status events are returned.</p>
            start_time: <p>The start of the time range to retrieve status events for. <code>StartTime</code> and <code>EndTime</code> must both be provided together or both be omitted. When both are omitted, the time range defaults to the last hour.</p>
            end_time: <p>The end of the time range to retrieve status events for. <code>StartTime</code> and <code>EndTime</code> must both be provided together or both be omitted. When both are omitted, the time range defaults to the last hour.</p>
            max_results: <p>The maximum number of status events to return in one call. The default is 60.</p>
            next_token: <p>Use the token returned by a previous call to retrieve the next page of status events.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.get_instrumentation_configuration_status_request.GetInstrumentationConfigurationStatusRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.get_instrumentation_configuration_status_response.GetInstrumentationConfigurationStatusResponse"
        ]:
            import capo_application_signals._operations.application_signals.get_instrumentation_configuration_status

            output, http_response = (
                capo_application_signals._operations.application_signals.get_instrumentation_configuration_status.get_instrumentation_configuration_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.get_instrumentation_configuration_status_request.GetInstrumentationConfigurationStatusRequest = {
            "instrumentation_type": instrumentation_type,
            "service": service,
            "environment": environment,
            "signal_type": signal_type,
            "location_identifier": location_identifier,
        }
        if status is not None:
            input_["status"] = status
        if start_time is not None:
            input_["start_time"] = start_time
        if end_time is not None:
            input_["end_time"] = end_time
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

    def iter_get_instrumentation_configuration_status(
        self,
        instrumentation_type: "capo_application_signals.types.instrumentation_type.InstrumentationType",
        service: str,
        environment: str,
        signal_type: "capo_application_signals.types.dynamic_instrumentation_signal_type.DynamicInstrumentationSignalType",
        location_identifier: "capo_application_signals.types.location_identifier.LocationIdentifier",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        status: Optional[
            "capo_application_signals.types.instrumentation_configuration_status.InstrumentationConfigurationStatus"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.instrumentation_status_event.InstrumentationStatusEvent]":
        _token = next_token
        while True:
            _response = self.get_instrumentation_configuration_status(
                instrumentation_type,
                service,
                environment,
                signal_type,
                location_identifier,
                config_overrides=config_overrides,
                status=status,
                start_time=start_time,
                end_time=end_time,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def get_service(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.get_service_output.GetServiceOutput":
        """<p>Returns information about a service discovered by Application Signals.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.get_service_input.GetServiceInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.get_service_output.GetServiceOutput"
        ]:
            import capo_application_signals._operations.application_signals.get_service

            output, http_response = (
                capo_application_signals._operations.application_signals.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.get_service_input.GetServiceInput = {
            "start_time": start_time,
            "end_time": end_time,
            "key_attributes": key_attributes,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_audit_findings(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        audit_targets: "capo_application_signals.types.audit_targets.AuditTargets",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        auditors: Optional["capo_application_signals.types.auditors.Auditors"] = None,
        detail_level: Optional[
            "capo_application_signals.types.detail_level.DetailLevel"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        max_results: Optional[
            "capo_application_signals.types.list_audit_finding_max_results.ListAuditFindingMaxResults"
        ] = None,
    ) -> "capo_application_signals.types.list_audit_findings_output.ListAuditFindingsOutput":
        """<p>Returns a list of audit findings that provide automated analysis of service behavior and root cause analysis. These findings help identify the most significant observations about your services, including performance issues, anomalies, and potential problems. The findings are generated using heuristic algorithms based on established troubleshooting patterns.</p>

        Args:
            start_time: <p>The start of the time period to retrieve audit findings for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>
            end_time: <p>The end of the time period to retrieve audit findings for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code> </p>
            auditors: <p>A list of auditor names to filter the findings by. Only findings generated by the specified auditors will be returned.</p> <p>The following auditors are available for configuration:</p> <ul> <li> <p> <code>slo</code> - SloAuditor: Identifies SLO violations and detects breached thresholds during the Assessment phase.</p> </li> <li> <p> <code>operation_metric</code> - OperationMetricAuditor: Detects anomalies in service operation metrics from Application Signals RED metrics during the Assessment phase</p> <note> <p>Anomaly detection is not supported for sparse metrics (those missing more than 80% of datapoints within the given time period).</p> </note> </li> <li> <p> <code>service_quota</code> - ServiceQuotaAuditor: Monitors resource utilization against service quotas during the Assessment phase</p> </li> <li> <p> <code>trace</code> - TraceAuditor: Performs deep-dive analysis of distributed traces, correlating traces with breached SLOs or abnormal RED metrics during the Analysis phase</p> </li> <li> <p> <code>dependency_metric</code> - CriticalPathAuditor: Analyzes service dependency impacts and maps dependency relationships from Application Signals RED metrics during the Analysis phase</p> </li> <li> <p> <code>top_contributor</code> - TopContributorAuditor: Identifies infrastructure-level contributors to issues by analyzing EMF logs of Application Signals RED metrics during the Analysis phase</p> </li> <li> <p> <code>log</code> - LogAuditor: Extracts insights from application logs, categorizing error types and ranking severity by frequency during the Analysis phase</p> </li> <li> <p> <code>change_indicator</code> - ChangeIndicatorAuditor: Detects change events (deployments, configuration changes) that occurred within 10 minutes before and during a detected anomaly, and surfaces them as findings with deployment timestamps in the Analysis phase. When changes are detected, the <code>top_contributor</code> auditor skips its analysis to avoid redundancy.</p> </li> </ul> <note> <p> <code>InitAuditor</code> and <code>Summarizer</code> auditors are not configurable as they are automatically triggered during the audit process.</p> </note>
            audit_targets: <p>A list of audit targets to filter the findings by. You can specify services, SLOs, or service operations to limit the audit findings to specific entities.</p>
            detail_level: <p>The level of details of the audit findings. Supported values: <code>BRIEF</code>, <code>DETAILED</code>.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of audit findings.</p>
            max_results: <p>The maximum number of audit findings to return in one operation. If you omit this parameter, the default of 10 is used.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_audit_findings_input.ListAuditFindingsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_audit_findings_output.ListAuditFindingsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_audit_findings

            output, http_response = (
                capo_application_signals._operations.application_signals.list_audit_findings.list_audit_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_audit_findings_input.ListAuditFindingsInput = {
            "start_time": start_time,
            "end_time": end_time,
            "audit_targets": audit_targets,
        }
        if auditors is not None:
            input_["auditors"] = auditors
        if detail_level is not None:
            input_["detail_level"] = detail_level
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

    def list_entity_events(
        self,
        entity: "capo_application_signals.types.attributes.Attributes",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_entity_events_max_results.ListEntityEventsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_entity_events_output.ListEntityEventsOutput":
        """<p>Returns a list of change events for a specific entity, such as deployments, configuration changes, or other state-changing activities. This operation helps track the history of changes that may have affected service performance.</p>

        Args:
            entity: <p>The entity for which to retrieve change events. This specifies the service, resource, or other entity whose event history you want to examine.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> <li> <p> <code>AwsAccountId</code> specifies the account where this object is in.</p> </li> </ul> <p>Below is an example of a service.</p> <p> <code>{ "Type": "Service", "Name": "visits-service", "Environment": "petclinic-test" }</code> </p> <p>Below is an example of a resource.</p> <p> <code>{ "Type": "AWS::Resource", "ResourceType": "AWS::DynamoDB::Table", "Identifier": "Customers" }</code> </p>
            start_time: <p>The start of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>
            end_time: <p>The end of the time period to retrieve change events for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example: <code>1698778057</code> </p>
            max_results: <p>The maximum number of change events to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of change events.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_entity_events_input.ListEntityEventsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_entity_events_output.ListEntityEventsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_entity_events

            output, http_response = (
                capo_application_signals._operations.application_signals.list_entity_events.list_entity_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_entity_events_input.ListEntityEventsInput = {
            "entity": entity,
            "start_time": start_time,
            "end_time": end_time,
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

    def iter_list_entity_events(
        self,
        entity: "capo_application_signals.types.attributes.Attributes",
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_entity_events_max_results.ListEntityEventsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.change_event.ChangeEvent]":
        _token = next_token
        while True:
            _response = self.list_entity_events(
                entity,
                start_time,
                end_time,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("change_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_grouping_attribute_definitions(
        self,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
    ) -> "capo_application_signals.types.list_grouping_attribute_definitions_output.ListGroupingAttributeDefinitionsOutput":
        """<p>Returns the current grouping configuration for this account, including all custom grouping attribute definitions that have been configured. These definitions determine how services are logically grouped based on telemetry attributes, Amazon Web Services tags, or predefined mappings.</p>

        Args:
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of grouping attribute definitions.</p>
            aws_account_id: <p>The Amazon Web Services account ID to retrieve grouping attribute definitions for. Use this when accessing grouping configurations from a different account in cross-account monitoring scenarios.</p>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include grouping attributes from source accounts in the returned data.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_grouping_attribute_definitions_input.ListGroupingAttributeDefinitionsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_grouping_attribute_definitions_output.ListGroupingAttributeDefinitionsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_grouping_attribute_definitions

            output, http_response = (
                capo_application_signals._operations.application_signals.list_grouping_attribute_definitions.list_grouping_attribute_definitions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_grouping_attribute_definitions_input.ListGroupingAttributeDefinitionsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_instrumentation_configurations(
        self,
        service: str,
        environment: str,
        instrumentation_type: "capo_application_signals.types.instrumentation_type.InstrumentationType",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        synced_at: Optional[datetime.datetime] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.instrumentation_configurations_page.InstrumentationConfigurationsPage":
        """<p>Returns all active instrumentation configurations for a service and environment. SDKs use this operation to sync configurations and apply client-side filters locally.</p> <p>Include the previous <code>SyncedAt</code> value to perform incremental syncs. When no changes are detected, the response sets <code>Changed</code> to <code>false</code> and omits configuration details.</p>

        Args:
            service: <p>The name of the service to retrieve instrumentation configurations for.</p>
            environment: <p>The environment that the service is running in.</p>
            instrumentation_type: Type of instrumentation configuration (BREAKPOINT or PROBE). Required to determine which backing store to query.
            synced_at: <p>The timestamp from the last successful sync. When provided, the response returns <code>Changed</code> as <code>false</code> if nothing is new since this time, or returns the latest configurations when changes exist.</p>
            max_results: <p>The maximum number of configurations to return in one call. The default is 50 and the maximum is 100.</p>
            next_token: <p>Use the token returned by a previous call to retrieve the next page of configurations.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_instrumentation_configurations_request.ListInstrumentationConfigurationsRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.instrumentation_configurations_page.InstrumentationConfigurationsPage"
        ]:
            import capo_application_signals._operations.application_signals.list_instrumentation_configurations

            output, http_response = (
                capo_application_signals._operations.application_signals.list_instrumentation_configurations.list_instrumentation_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_instrumentation_configurations_request.ListInstrumentationConfigurationsRequest = {
            "service": service,
            "environment": environment,
            "instrumentation_type": instrumentation_type,
        }
        if synced_at is not None:
            input_["synced_at"] = synced_at
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

    def iter_list_instrumentation_configurations(
        self,
        service: str,
        environment: str,
        instrumentation_type: "capo_application_signals.types.instrumentation_type.InstrumentationType",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        synced_at: Optional[datetime.datetime] = None,
        max_results: Optional[int] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.instrumentation_configuration_without_service_env.InstrumentationConfigurationWithoutServiceEnv]":
        _token = next_token
        while True:
            _response = self.list_instrumentation_configurations(
                service,
                environment,
                instrumentation_type,
                config_overrides=config_overrides,
                synced_at=synced_at,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("latest_configurations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_dependencies(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependencies_max_results.ListServiceDependenciesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_dependencies_output.ListServiceDependenciesOutput":
        """<p>Returns a list of service dependencies of the service that you specify. A dependency is an infrastructure component that an operation of this service connects with. Dependencies can include Amazon Web Services services, Amazon Web Services resources, and third-party services. </p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested end time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service dependencies.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_dependencies_input.ListServiceDependenciesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_dependencies_output.ListServiceDependenciesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_dependencies

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_dependencies.list_service_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_dependencies_input.ListServiceDependenciesInput = {
            "start_time": start_time,
            "end_time": end_time,
            "key_attributes": key_attributes,
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

    def iter_list_service_dependencies(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependencies_max_results.ListServiceDependenciesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> (
        "Iterator[capo_application_signals.types.service_dependency.ServiceDependency]"
    ):
        _token = next_token
        while True:
            _response = self.list_service_dependencies(
                start_time,
                end_time,
                key_attributes,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_dependencies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_dependents(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependents_max_results.ListServiceDependentsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_dependents_output.ListServiceDependentsOutput":
        """<p>Returns the list of dependents that invoked the specified service during the provided time range. Dependents include other services, CloudWatch Synthetics canaries, and clients that are instrumented with CloudWatch RUM app monitors.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service dependents.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_dependents_input.ListServiceDependentsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_dependents_output.ListServiceDependentsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_dependents

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_dependents.list_service_dependents(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_dependents_input.ListServiceDependentsInput = {
            "start_time": start_time,
            "end_time": end_time,
            "key_attributes": key_attributes,
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

    def iter_list_service_dependents(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_dependents_max_results.ListServiceDependentsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_dependent.ServiceDependent]":
        _token = next_token
        while True:
            _response = self.list_service_dependents(
                start_time,
                end_time,
                key_attributes,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_dependents",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_level_objective_exclusion_windows(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results.ListServiceLevelObjectiveExclusionWindowsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_level_objective_exclusion_windows_output.ListServiceLevelObjectiveExclusionWindowsOutput":
        """<p>Retrieves all exclusion windows configured for a specific SLO.</p>

        Args:
            id: <p>The ID of the SLO to list exclusion windows for.</p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used. </p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives. </p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_level_objective_exclusion_windows_input.ListServiceLevelObjectiveExclusionWindowsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_level_objective_exclusion_windows_output.ListServiceLevelObjectiveExclusionWindowsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_level_objective_exclusion_windows

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_level_objective_exclusion_windows.list_service_level_objective_exclusion_windows(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_level_objective_exclusion_windows_input.ListServiceLevelObjectiveExclusionWindowsInput = {
            "id": id
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

    def iter_list_service_level_objective_exclusion_windows(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objective_exclusion_windows_max_results.ListServiceLevelObjectiveExclusionWindowsMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.exclusion_window.ExclusionWindow]":
        _token = next_token
        while True:
            _response = self.list_service_level_objective_exclusion_windows(
                id,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exclusion_windows",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_operations(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_operation_max_results.ListServiceOperationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "capo_application_signals.types.list_service_operations_output.ListServiceOperationsOutput":
        """<p>Returns a list of the <i>operations</i> of this service that have been discovered by Application Signals. Only the operations that were invoked during the specified time range are returned.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested end time will be rounded to the nearest hour.</p>
            key_attributes: <p>Use this field to specify which service you want to retrieve information for. You must specify at least the <code>Type</code>, <code>Name</code>, and <code>Environment</code> attributes.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service operations.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_operations_input.ListServiceOperationsInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_operations_output.ListServiceOperationsOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_operations

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_operations.list_service_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_operations_input.ListServiceOperationsInput = {
            "start_time": start_time,
            "end_time": end_time,
            "key_attributes": key_attributes,
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

    def iter_list_service_operations(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        key_attributes: "capo_application_signals.types.attributes.Attributes",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_operation_max_results.ListServiceOperationMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_operation.ServiceOperation]":
        _token = next_token
        while True:
            _response = self.list_service_operations(
                start_time,
                end_time,
                key_attributes,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_operations",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_services_max_results.ListServicesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "capo_application_signals.types.list_services_output.ListServicesOutput":
        """<p>Returns a list of services that have been discovered by Application Signals. A service represents a minimum logical and transactional unit that completes a business function. Services are discovered through Application Signals instrumentation.</p>

        Args:
            start_time: <p>The start of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            end_time: <p>The end of the time period to retrieve information about. When used in a raw HTTP Query API, it is formatted as be epoch time in seconds. For example: <code>1698778057</code> </p> <p>Your requested start time will be rounded to the nearest hour.</p>
            max_results: <p> The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used. </p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of services.</p>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include services from source accounts in the returned data. </p>
            aws_account_id: <p>Amazon Web Services Account ID.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_services_input.ListServicesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_services_output.ListServicesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_services

            output, http_response = (
                capo_application_signals._operations.application_signals.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_services_input.ListServicesInput = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_services(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_services_max_results.ListServicesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_summary.ServiceSummary]":
        _token = next_token
        while True:
            _response = self.list_services(
                start_time,
                end_time,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include_linked_accounts=include_linked_accounts,
                aws_account_id=aws_account_id,
            )
            _page = _resolve_path(_response, ("service_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_states(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_states_max_results.ListServiceStatesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        attribute_filters: Optional[
            "capo_application_signals.types.attribute_filters.AttributeFilters"
        ] = None,
    ) -> "capo_application_signals.types.list_service_states_output.ListServiceStatesOutput":
        """<p>Returns information about the last deployment and other change states of services. This API provides visibility into recent changes that may have affected service performance, helping with troubleshooting and change correlation.</p>

        Args:
            start_time: <p>The start of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>
            end_time: <p>The end of the time period to retrieve service state information for. When used in a raw HTTP Query API, it is formatted as epoch time in seconds. For example, <code>1698778057</code>.</p>
            max_results: <p>The maximum number of service states to return in one operation. If you omit this parameter, the default of 20 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service states.</p>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include service states from source accounts in the returned data.</p>
            aws_account_id: <p>The Amazon Web Services account ID to filter service states by. Use this to limit results to services from a specific account.</p>
            attribute_filters: <p>A list of attribute filters to narrow down the services. You can filter by platform, environment, or other service attributes.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_states_input.ListServiceStatesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_states_output.ListServiceStatesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_states

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_states.list_service_states(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_states_input.ListServiceStatesInput = {
            "start_time": start_time,
            "end_time": end_time,
        }
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if aws_account_id is not None:
            input_["aws_account_id"] = aws_account_id
        if attribute_filters is not None:
            input_["attribute_filters"] = attribute_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_service_states(
        self,
        start_time: datetime.datetime,
        end_time: datetime.datetime,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_states_max_results.ListServiceStatesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        attribute_filters: Optional[
            "capo_application_signals.types.attribute_filters.AttributeFilters"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_state.ServiceState]":
        _token = next_token
        while True:
            _response = self.list_service_states(
                start_time,
                end_time,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
                include_linked_accounts=include_linked_accounts,
                aws_account_id=aws_account_id,
                attribute_filters=attribute_filters,
            )
            _page = _resolve_path(_response, ("service_states",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_application_signals.types.amazon_resource_name.AmazonResourceName",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Displays the tags associated with a CloudWatch resource. Tags can be assigned to service level objectives.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to view tags for.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_application_signals._operations.application_signals.list_tags_for_resource

            output, http_response = (
                capo_application_signals._operations.application_signals.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def put_grouping_configuration(
        self,
        grouping_attribute_definitions: "capo_application_signals.types.grouping_attribute_definitions.GroupingAttributeDefinitions",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.put_grouping_configuration_output.PutGroupingConfigurationOutput":
        """<p>Creates or updates the grouping configuration for this account. This operation allows you to define custom grouping attributes that determine how services are logically grouped based on telemetry attributes, Amazon Web Services tags, or predefined mappings. These grouping attributes can then be used to organize and filter services in the Application Signals console and APIs.</p>

        Args:
            grouping_attribute_definitions: <p>An array of grouping attribute definitions that specify how services should be grouped. Each definition includes a friendly name, source keys to derive the grouping value from, and an optional default value.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.put_grouping_configuration_input.PutGroupingConfigurationInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.put_grouping_configuration_output.PutGroupingConfigurationOutput"
        ]:
            import capo_application_signals._operations.application_signals.put_grouping_configuration

            output, http_response = (
                capo_application_signals._operations.application_signals.put_grouping_configuration.put_grouping_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.put_grouping_configuration_input.PutGroupingConfigurationInput = {
            "grouping_attribute_definitions": grouping_attribute_definitions
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def report_instrumentation_configuration_status(
        self,
        service: str,
        environment: str,
        configurations: "capo_application_signals.types.instrumentation_configuration_status_list.InstrumentationConfigurationStatusList",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.report_instrumentation_configuration_status_response.ReportInstrumentationConfigurationStatusResponse":
        """<p>Reports the status of one or more instrumentation configurations from SDK instances. Use this to record when configurations become ready, hit errors, become active, or are disabled by limits.</p> <p>Report <code>READY</code>, <code>ERROR</code>, and <code>DISABLED</code> when the status changes. Report <code>ACTIVE</code> periodically (for example, every minute) while instrumentation is running.</p>

        Args:
            service: <p>The service that the reported configurations belong to.</p>
            environment: <p>The environment that the service is running in.</p>
            configurations: <p>An array of configuration status reports (up to 100) that include the instrumentation type, signal type, location hash, status, timestamp, and optional error cause.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.report_instrumentation_configuration_status_request.ReportInstrumentationConfigurationStatusRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.report_instrumentation_configuration_status_response.ReportInstrumentationConfigurationStatusResponse"
        ]:
            import capo_application_signals._operations.application_signals.report_instrumentation_configuration_status

            output, http_response = (
                capo_application_signals._operations.application_signals.report_instrumentation_configuration_status.report_instrumentation_configuration_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.report_instrumentation_configuration_status_request.ReportInstrumentationConfigurationStatusRequest = {
            "service": service,
            "environment": environment,
            "configurations": configurations,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_discovery(
        self, *, config_overrides: Optional[ApplicationSignalsClientConfig] = None
    ) -> "capo_application_signals.types.start_discovery_output.StartDiscoveryOutput":
        """<p>Enables this Amazon Web Services account to be able to use CloudWatch Application Signals by creating the <i>AWSServiceRoleForCloudWatchApplicationSignals</i> service-linked role. This service- linked role has the following permissions:</p> <ul> <li> <p> <code>xray:GetServiceGraph</code> </p> </li> <li> <p> <code>logs:StartQuery</code> </p> </li> <li> <p> <code>logs:GetQueryResults</code> </p> </li> <li> <p> <code>cloudwatch:GetMetricData</code> </p> </li> <li> <p> <code>cloudwatch:ListMetrics</code> </p> </li> <li> <p> <code>tag:GetResources</code> </p> </li> <li> <p> <code>autoscaling:DescribeAutoScalingGroups</code> </p> </li> </ul> <p>A service-linked CloudTrail event channel is created to process CloudTrail events and return change event information. This includes last deployment time, userName, eventName, and other event metadata.</p> <p>After completing this step, you still need to instrument your Java and Python applications to send data to Application Signals. For more information, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Signals-Enable.html"> Enabling Application Signals</a>.</p>

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.start_discovery_input.StartDiscoveryInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.start_discovery_output.StartDiscoveryOutput"
        ]:
            import capo_application_signals._operations.application_signals.start_discovery

            output, http_response = (
                capo_application_signals._operations.application_signals.start_discovery.start_discovery(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.start_discovery_input.StartDiscoveryInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def tag_resource(
        self,
        resource_arn: "capo_application_signals.types.amazon_resource_name.AmazonResourceName",
        tags: "capo_application_signals.types.tag_list.TagList",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.tag_resource_response.TagResourceResponse":
        """<p>Assigns one or more tags (key-value pairs) to the specified CloudWatch resource, such as a service level objective.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p> <p>Tags don't have any semantic meaning to Amazon Web Services and are interpreted strictly as strings of characters.</p> <p>You can use the <code>TagResource</code> action with an alarm that already has tags. If you specify a new tag key for the alarm, this tag is appended to the list of tags associated with the alarm. If you specify a tag key that is already associated with the alarm, the new tag value that you specify replaces the previous value for that tag.</p> <p>You can associate as many as 50 tags with a CloudWatch resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to set tags for.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tags: <p>The list of key-value pairs to associate with the alarm.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_application_signals._operations.application_signals.tag_resource

            output, http_response = (
                capo_application_signals._operations.application_signals.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_application_signals.types.amazon_resource_name.AmazonResourceName",
        tag_keys: "capo_application_signals.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes one or more tags from the specified resource.</p>

        Args:
            resource_arn: <p>The Amazon Resource Name (ARN) of the CloudWatch resource that you want to delete tags from.</p> <p>The ARN format of an Application Signals SLO is <code>arn:aws:cloudwatch:<i>Region</i>:<i>account-id</i>:slo:<i>slo-name</i> </code> </p> <p>For more information about ARN format, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazoncloudwatch.html#amazoncloudwatch-resources-for-iam-policies"> Resource Types Defined by Amazon CloudWatch</a> in the <i>Amazon Web Services General Reference</i>.</p>
            tag_keys: <p>The list of tag keys to remove from the resource.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_application_signals.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_application_signals._operations.application_signals.untag_resource

            output, http_response = (
                capo_application_signals._operations.application_signals.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.untag_resource_request.UntagResourceRequest = {
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

    def create_service_level_objective(
        self,
        name: "capo_application_signals.types.service_level_objective_name.ServiceLevelObjectiveName",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        description: Optional[
            "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
        ] = None,
        sli_config: Optional[
            "capo_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
        ] = None,
        request_based_sli_config: Optional[
            "capo_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
        ] = None,
        goal: Optional["capo_application_signals.types.goal.Goal"] = None,
        tags: Optional["capo_application_signals.types.tag_list.TagList"] = None,
        burn_rate_configurations: Optional[
            "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
        ] = None,
        create_recommended_slo: Optional[bool] = None,
        auto_investigation_enabled: Optional[bool] = None,
    ) -> "capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput":
        """<p>Creates a service level objective (SLO), which can help you ensure that your critical business operations are meeting customer expectations. Use SLOs to set and track specific target levels for the reliability and availability of your applications and services. SLOs use service level indicators (SLIs) to calculate whether the application is performing at the level that you want.</p> <p>Create an SLO to set a target for a service or operation’s availability or latency. CloudWatch measures this target frequently you can find whether it has been breached. </p> <p>The target performance quality that is defined for an SLO is the <i>attainment goal</i>.</p> <p>You can set SLO targets for your applications that are discovered by Application Signals, using critical metrics such as latency and availability. You can also set SLOs against any CloudWatch metric or math expression that produces a time series.</p> <note> <p>You can't create an SLO for a service operation that was discovered by Application Signals until after that operation has reported standard metrics to Application Signals.</p> </note> <p>When you create an SLO, you specify whether it is a <i>period-based SLO</i> or a <i>request-based SLO</i>. Each type of SLO has a different way of evaluating your application's performance against its attainment goal.</p> <ul> <li> <p>A <i>period-based SLO</i> uses defined <i>periods</i> of time within a specified total time interval. For each period of time, Application Signals determines whether the application met its goal. The attainment rate is calculated as the <code>number of good periods/number of total periods</code>.</p> <p>For example, for a period-based SLO, meeting an attainment goal of 99.9% means that within your interval, your application must meet its performance goal during at least 99.9% of the time periods.</p> </li> <li> <p>A <i>request-based SLO</i> doesn't use pre-defined periods of time. Instead, the SLO measures <code>number of good requests/number of total requests</code> during the interval. At any time, you can find the ratio of good requests to total requests for the interval up to the time stamp that you specify, and measure that ratio against the goal set in your SLO.</p> </li> </ul> <p>After you have created an SLO, you can retrieve error budget reports for it. An <i>error budget</i> is the amount of time or amount of requests that your application can be non-compliant with the SLO's goal, and still have your application meet the goal.</p> <ul> <li> <p>For a period-based SLO, the error budget starts at a number defined by the highest number of periods that can fail to meet the threshold, while still meeting the overall goal. The <i>remaining error budget</i> decreases with every failed period that is recorded. The error budget within one interval can never increase.</p> <p>For example, an SLO with a threshold that 99.95% of requests must be completed under 2000ms every month translates to an error budget of 21.9 minutes of downtime per month.</p> </li> <li> <p>For a request-based SLO, the remaining error budget is dynamic and can increase or decrease, depending on the ratio of good requests to total requests.</p> </li> </ul> <p>For more information about SLOs, see <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-ServiceLevelObjectives.html"> Service level objectives (SLOs)</a>. </p> <p>When you perform a <code>CreateServiceLevelObjective</code> operation, Application Signals creates the <i>AWSServiceRoleForCloudWatchApplicationSignals</i> service-linked role, if it doesn't already exist in your account. This service- linked role has the following permissions:</p> <ul> <li> <p> <code>xray:GetServiceGraph</code> </p> </li> <li> <p> <code>logs:StartQuery</code> </p> </li> <li> <p> <code>logs:GetQueryResults</code> </p> </li> <li> <p> <code>cloudwatch:GetMetricData</code> </p> </li> <li> <p> <code>cloudwatch:ListMetrics</code> </p> </li> <li> <p> <code>tag:GetResources</code> </p> </li> <li> <p> <code>autoscaling:DescribeAutoScalingGroups</code> </p> </li> </ul>

        Args:
            name: <p>A name for this SLO.</p>
            description: <p>An optional description for this SLO.</p>
            sli_config: <p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>
            request_based_sli_config: <p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>RequestBasedSliConfig</code> and <code>SliConfig</code> in the same operation.</p>
            goal: <p>This structure contains the attributes that determine the goal of the SLO.</p>
            tags: <p>A list of key-value pairs to associate with the SLO. You can associate as many as 50 tags with an SLO. To be able to associate tags with the SLO when you create the SLO, you must have the <code>cloudwatch:TagResource</code> permission.</p> <p>Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.</p>
            burn_rate_configurations: <p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>
            create_recommended_slo: <p>Set this to <code>true</code> to create a recommended SLO out of the box. When set to <code>true</code>, you don't need to specify the <code>MetricThreshold</code> or <code>ComparisonOperator</code> in the <code>SliConfig</code> or <code>RequestBasedSliConfig</code>. The default value is <code>false</code>.</p> <p>This is supported for SLOs on a service, service operation, or a dependency.</p>
            auto_investigation_enabled: Indicates whether DevOps Agent will automatically investigate this SLO when it is breached

        Raises:
            capo_application_signals.errors.access_denied_exception.AccessDeniedException: <p>You don't have sufficient permissions to perform this action.</p>
            capo_application_signals.errors.conflict_exception.ConflictException: <p>This operation attempted to create a resource that already exists.</p>
            capo_application_signals.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>This request exceeds a service quota.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.create_service_level_objective_output.CreateServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.create_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.create_service_level_objective.create_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.create_service_level_objective_input.CreateServiceLevelObjectiveInput = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sli_config is not None:
            input_["sli_config"] = sli_config
        if request_based_sli_config is not None:
            input_["request_based_sli_config"] = request_based_sli_config
        if goal is not None:
            input_["goal"] = goal
        if tags is not None:
            input_["tags"] = tags
        if burn_rate_configurations is not None:
            input_["burn_rate_configurations"] = burn_rate_configurations
        if create_recommended_slo is not None:
            input_["create_recommended_slo"] = create_recommended_slo
        if auto_investigation_enabled is not None:
            input_["auto_investigation_enabled"] = auto_investigation_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service_level_objective(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.get_service_level_objective_output.GetServiceLevelObjectiveOutput":
        """<p>Returns information about one SLO created in the account. </p>

        Args:
            id: <p>The ARN or name of the SLO that you want to retrieve information about. You can find the ARNs of SLOs by using the <a href="https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_ListServiceLevelObjectives.html">ListServiceLevelObjectives</a> operation.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.get_service_level_objective_input.GetServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.get_service_level_objective_output.GetServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.get_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.get_service_level_objective.get_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.get_service_level_objective_input.GetServiceLevelObjectiveInput = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_level_objective(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        description: Optional[
            "capo_application_signals.types.service_level_objective_description.ServiceLevelObjectiveDescription"
        ] = None,
        sli_config: Optional[
            "capo_application_signals.types.service_level_indicator_config.ServiceLevelIndicatorConfig"
        ] = None,
        request_based_sli_config: Optional[
            "capo_application_signals.types.request_based_service_level_indicator_config.RequestBasedServiceLevelIndicatorConfig"
        ] = None,
        goal: Optional["capo_application_signals.types.goal.Goal"] = None,
        burn_rate_configurations: Optional[
            "capo_application_signals.types.burn_rate_configurations.BurnRateConfigurations"
        ] = None,
        auto_investigation_enabled: Optional[bool] = None,
    ) -> "capo_application_signals.types.update_service_level_objective_output.UpdateServiceLevelObjectiveOutput":
        """<p>Updates an existing service level objective (SLO). If you omit parameters, the previous values of those parameters are retained. </p> <p>You cannot change from a period-based SLO to a request-based SLO, or change from a request-based SLO to a period-based SLO.</p>

        Args:
            id: <p>The Amazon Resource Name (ARN) or name of the service level objective that you want to update.</p>
            description: <p>An optional description for the SLO.</p>
            sli_config: <p>If this SLO is a period-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p>
            request_based_sli_config: <p>If this SLO is a request-based SLO, this structure defines the information about what performance metric this SLO will monitor.</p> <p>You can't specify both <code>SliConfig</code> and <code>RequestBasedSliConfig</code> in the same operation.</p>
            goal: <p>A structure that contains the attributes that determine the goal of the SLO. This includes the time period for evaluation and the attainment threshold.</p>
            burn_rate_configurations: <p>Use this array to create <i>burn rates</i> for this SLO. Each burn rate is a metric that indicates how fast the service is consuming the error budget, relative to the attainment goal of the SLO.</p>
            auto_investigation_enabled: Indicates whether DevOps Agent will automatically investigate this SLO when it is breached

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.update_service_level_objective_input.UpdateServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.update_service_level_objective_output.UpdateServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.update_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.update_service_level_objective.update_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.update_service_level_objective_input.UpdateServiceLevelObjectiveInput = {
            "id": id
        }
        if description is not None:
            input_["description"] = description
        if sli_config is not None:
            input_["sli_config"] = sli_config
        if request_based_sli_config is not None:
            input_["request_based_sli_config"] = request_based_sli_config
        if goal is not None:
            input_["goal"] = goal
        if burn_rate_configurations is not None:
            input_["burn_rate_configurations"] = burn_rate_configurations
        if auto_investigation_enabled is not None:
            input_["auto_investigation_enabled"] = auto_investigation_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_level_objective(
        self,
        id: "capo_application_signals.types.service_level_objective_id.ServiceLevelObjectiveId",
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
    ) -> "capo_application_signals.types.delete_service_level_objective_output.DeleteServiceLevelObjectiveOutput":
        """<p>Deletes the specified service level objective.</p>

        Args:
            id: <p>The ARN or name of the service level objective to delete.</p>

        Raises:
            capo_application_signals.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.delete_service_level_objective_input.DeleteServiceLevelObjectiveInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.delete_service_level_objective_output.DeleteServiceLevelObjectiveOutput"
        ]:
            import capo_application_signals._operations.application_signals.delete_service_level_objective

            output, http_response = (
                capo_application_signals._operations.application_signals.delete_service_level_objective.delete_service_level_objective(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.delete_service_level_objective_input.DeleteServiceLevelObjectiveInput = {
            "id": id
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_service_level_objectives(
        self,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        key_attributes: Optional[
            "capo_application_signals.types.attributes.Attributes"
        ] = None,
        operation_name: Optional[
            "capo_application_signals.types.operation_name.OperationName"
        ] = None,
        dependency_config: Optional[
            "capo_application_signals.types.dependency_config.DependencyConfig"
        ] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objectives_max_results.ListServiceLevelObjectivesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        metric_source_types: Optional[
            "capo_application_signals.types.metric_source_types.MetricSourceTypes"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        slo_owner_aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        metric_source: Optional[
            "capo_application_signals.types.metric_source.MetricSource"
        ] = None,
    ) -> "capo_application_signals.types.list_service_level_objectives_output.ListServiceLevelObjectivesOutput":
        """<p>Returns a list of SLOs created in this account.</p>

        Args:
            key_attributes: <p>You can use this optional field to specify which services you want to retrieve SLO information for.</p> <p>This is a string-to-string map. It can include the following fields.</p> <ul> <li> <p> <code>Type</code> designates the type of object this is.</p> </li> <li> <p> <code>ResourceType</code> specifies the type of the resource. This field is used only when the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Name</code> specifies the name of the object. This is used only if the value of the <code>Type</code> field is <code>Service</code>, <code>RemoteService</code>, or <code>AWS::Service</code>.</p> </li> <li> <p> <code>Identifier</code> identifies the resource objects of this resource. This is used only if the value of the <code>Type</code> field is <code>Resource</code> or <code>AWS::Resource</code>.</p> </li> <li> <p> <code>Environment</code> specifies the location where this object is hosted, or what it belongs to.</p> </li> </ul>
            operation_name: <p>The name of the operation that this SLO is associated with.</p>
            dependency_config: <p>Identifies the dependency using the <code>DependencyKeyAttributes</code> and <code>DependencyOperationName</code>. </p>
            max_results: <p>The maximum number of results to return in one operation. If you omit this parameter, the default of 50 is used.</p>
            next_token: <p>Include this value, if it was returned by the previous operation, to get the next set of service level objectives.</p>
            metric_source_types: <p>Use this optional field to only include SLOs with the specified metric source types in the output. Supported types are:</p> <ul> <li> <p>Service operation</p> </li> <li> <p>Service dependency</p> </li> <li> <p>Service</p> </li> <li> <p>CloudWatch metric</p> </li> <li> <p>AppMonitor</p> </li> <li> <p>Canary</p> </li> </ul>
            include_linked_accounts: <p>If you are using this operation in a monitoring account, specify <code>true</code> to include SLO from source accounts in the returned data. </p> <p>When you are monitoring an account, you can use Amazon Web Services account ID in <code>KeyAttribute</code> filter for service source account and <code>SloOwnerawsaccountID</code> for SLO source account with <code>IncludeLinkedAccounts</code> to filter the returned data to only a single source account. </p>
            slo_owner_aws_account_id: <p>SLO's Amazon Web Services account ID.</p>
            metric_source: <p>Identifies the metric source to filter SLOs by.</p>

        Raises:
            capo_application_signals.errors.throttling_exception.ThrottlingException: <p>The request was throttled because of quota limits.</p>
            capo_application_signals.errors.validation_exception.ValidationException: <p>The resource is not valid.</p>
            capo_application_signals.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_application_signals.types.list_service_level_objectives_input.ListServiceLevelObjectivesInput]",
        ) -> OperationResponse[
            "capo_application_signals.types.list_service_level_objectives_output.ListServiceLevelObjectivesOutput"
        ]:
            import capo_application_signals._operations.application_signals.list_service_level_objectives

            output, http_response = (
                capo_application_signals._operations.application_signals.list_service_level_objectives.list_service_level_objectives(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_application_signals.types.list_service_level_objectives_input.ListServiceLevelObjectivesInput = {}
        if key_attributes is not None:
            input_["key_attributes"] = key_attributes
        if operation_name is not None:
            input_["operation_name"] = operation_name
        if dependency_config is not None:
            input_["dependency_config"] = dependency_config
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if metric_source_types is not None:
            input_["metric_source_types"] = metric_source_types
        if include_linked_accounts is not None:
            input_["include_linked_accounts"] = include_linked_accounts
        if slo_owner_aws_account_id is not None:
            input_["slo_owner_aws_account_id"] = slo_owner_aws_account_id
        if metric_source is not None:
            input_["metric_source"] = metric_source

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_service_level_objectives(
        self,
        *,
        config_overrides: Optional[ApplicationSignalsClientConfig] = None,
        key_attributes: Optional[
            "capo_application_signals.types.attributes.Attributes"
        ] = None,
        operation_name: Optional[
            "capo_application_signals.types.operation_name.OperationName"
        ] = None,
        dependency_config: Optional[
            "capo_application_signals.types.dependency_config.DependencyConfig"
        ] = None,
        max_results: Optional[
            "capo_application_signals.types.list_service_level_objectives_max_results.ListServiceLevelObjectivesMaxResults"
        ] = None,
        next_token: Optional[
            "capo_application_signals.types.next_token.NextToken"
        ] = None,
        metric_source_types: Optional[
            "capo_application_signals.types.metric_source_types.MetricSourceTypes"
        ] = None,
        include_linked_accounts: Optional[bool] = None,
        slo_owner_aws_account_id: Optional[
            "capo_application_signals.types.aws_account_id.AwsAccountId"
        ] = None,
        metric_source: Optional[
            "capo_application_signals.types.metric_source.MetricSource"
        ] = None,
    ) -> "Iterator[capo_application_signals.types.service_level_objective_summary.ServiceLevelObjectiveSummary]":
        _token = next_token
        while True:
            _response = self.list_service_level_objectives(
                config_overrides=config_overrides,
                key_attributes=key_attributes,
                operation_name=operation_name,
                dependency_config=dependency_config,
                max_results=max_results,
                next_token=_token,
                metric_source_types=metric_source_types,
                include_linked_accounts=include_linked_accounts,
                slo_owner_aws_account_id=slo_owner_aws_account_id,
                metric_source=metric_source,
            )
            _page = _resolve_path(_response, ("slo_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def __enter__(self) -> Self:
        return self

    def __exit__(self, exc_type: Any, exc: Any, tb: Any):
        self._client.close()
