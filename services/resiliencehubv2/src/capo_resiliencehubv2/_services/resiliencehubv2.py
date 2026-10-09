"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#NGRHServiceCore``."""

import datetime
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_resiliencehubv2._auth._signers
import capo_resiliencehubv2._auth._sigv4
from capo_resiliencehubv2._auth._identity import Credentials
from capo_resiliencehubv2._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_resiliencehubv2._auth._zapros_handler import AuthMiddleware
from capo_resiliencehubv2._pagination import resolve_path as _resolve_path
from capo_resiliencehubv2._resources.ngrh_service_core.iam_app_resource import (
    IamAppResource,
)
from capo_resiliencehubv2._resources.ngrh_service_core.iam_policy_resource import (
    IamPolicyResource,
)
from capo_resiliencehubv2._resources.ngrh_service_core.iam_resiliency_policy_resource import (
    IamResiliencyPolicyResource,
)
from capo_resiliencehubv2._resources.ngrh_service_core.iam_service_resource import (
    IamServiceResource,
)
from capo_resiliencehubv2._resources.ngrh_service_core.iam_system_resource import (
    IamSystemResource,
)
from capo_resiliencehubv2._services._aws_config import aws_config
from capo_resiliencehubv2._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.account_id
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.assertion
    import capo_resiliencehubv2.types.assertion_source
    import capo_resiliencehubv2.types.assertion_text
    import capo_resiliencehubv2.types.assessment_sort_field
    import capo_resiliencehubv2.types.assessment_status
    import capo_resiliencehubv2.types.assessment_status_list
    import capo_resiliencehubv2.types.assessment_summary
    import capo_resiliencehubv2.types.associated_system_list
    import capo_resiliencehubv2.types.availability_slo
    import capo_resiliencehubv2.types.aws_region
    import capo_resiliencehubv2.types.client_token
    import capo_resiliencehubv2.types.create_assertion_request
    import capo_resiliencehubv2.types.create_assertion_response
    import capo_resiliencehubv2.types.create_input_source_request
    import capo_resiliencehubv2.types.create_input_source_response
    import capo_resiliencehubv2.types.create_policy_request
    import capo_resiliencehubv2.types.create_policy_response
    import capo_resiliencehubv2.types.create_report_request
    import capo_resiliencehubv2.types.create_report_response
    import capo_resiliencehubv2.types.create_service_function_request
    import capo_resiliencehubv2.types.create_service_function_resources_request
    import capo_resiliencehubv2.types.create_service_function_resources_response
    import capo_resiliencehubv2.types.create_service_function_response
    import capo_resiliencehubv2.types.create_service_request
    import capo_resiliencehubv2.types.create_service_response
    import capo_resiliencehubv2.types.create_system_request
    import capo_resiliencehubv2.types.create_system_response
    import capo_resiliencehubv2.types.create_test_request
    import capo_resiliencehubv2.types.create_test_response
    import capo_resiliencehubv2.types.create_user_journey_request
    import capo_resiliencehubv2.types.create_user_journey_response
    import capo_resiliencehubv2.types.data_recovery_targets
    import capo_resiliencehubv2.types.delete_assertion_request
    import capo_resiliencehubv2.types.delete_assertion_response
    import capo_resiliencehubv2.types.delete_input_source_request
    import capo_resiliencehubv2.types.delete_input_source_response
    import capo_resiliencehubv2.types.delete_policy_request
    import capo_resiliencehubv2.types.delete_policy_response
    import capo_resiliencehubv2.types.delete_service_function_request
    import capo_resiliencehubv2.types.delete_service_function_resources_request
    import capo_resiliencehubv2.types.delete_service_function_resources_response
    import capo_resiliencehubv2.types.delete_service_function_response
    import capo_resiliencehubv2.types.delete_service_request
    import capo_resiliencehubv2.types.delete_service_response
    import capo_resiliencehubv2.types.delete_system_request
    import capo_resiliencehubv2.types.delete_system_response
    import capo_resiliencehubv2.types.delete_test_request
    import capo_resiliencehubv2.types.delete_test_response
    import capo_resiliencehubv2.types.delete_test_sources_request
    import capo_resiliencehubv2.types.delete_test_sources_response
    import capo_resiliencehubv2.types.delete_user_journey_request
    import capo_resiliencehubv2.types.delete_user_journey_response
    import capo_resiliencehubv2.types.dependency_criticality
    import capo_resiliencehubv2.types.dependency_discovery_input
    import capo_resiliencehubv2.types.dependency_summary
    import capo_resiliencehubv2.types.entity_description
    import capo_resiliencehubv2.types.entity_id
    import capo_resiliencehubv2.types.entity_label
    import capo_resiliencehubv2.types.entity_name
    import capo_resiliencehubv2.types.failure_category
    import capo_resiliencehubv2.types.finding_severity
    import capo_resiliencehubv2.types.finding_status
    import capo_resiliencehubv2.types.finding_summary
    import capo_resiliencehubv2.types.get_dependency_insights_request
    import capo_resiliencehubv2.types.get_dependency_insights_response
    import capo_resiliencehubv2.types.get_failure_mode_finding_request
    import capo_resiliencehubv2.types.get_failure_mode_finding_response
    import capo_resiliencehubv2.types.get_policy_request
    import capo_resiliencehubv2.types.get_policy_response
    import capo_resiliencehubv2.types.get_service_request
    import capo_resiliencehubv2.types.get_service_response
    import capo_resiliencehubv2.types.get_system_request
    import capo_resiliencehubv2.types.get_system_response
    import capo_resiliencehubv2.types.get_test_request
    import capo_resiliencehubv2.types.get_test_response
    import capo_resiliencehubv2.types.get_test_run_request
    import capo_resiliencehubv2.types.get_test_run_response
    import capo_resiliencehubv2.types.get_test_template_request
    import capo_resiliencehubv2.types.get_test_template_response
    import capo_resiliencehubv2.types.get_user_journey_request
    import capo_resiliencehubv2.types.get_user_journey_response
    import capo_resiliencehubv2.types.iam_role_name
    import capo_resiliencehubv2.types.import_app_request
    import capo_resiliencehubv2.types.import_app_response
    import capo_resiliencehubv2.types.import_policy_request
    import capo_resiliencehubv2.types.import_policy_response
    import capo_resiliencehubv2.types.input_source_id
    import capo_resiliencehubv2.types.input_source_summary
    import capo_resiliencehubv2.types.input_source_type
    import capo_resiliencehubv2.types.kms_key_id
    import capo_resiliencehubv2.types.list_assertions_request
    import capo_resiliencehubv2.types.list_assertions_response
    import capo_resiliencehubv2.types.list_dependencies_request
    import capo_resiliencehubv2.types.list_dependencies_response
    import capo_resiliencehubv2.types.list_failure_mode_assessments_request
    import capo_resiliencehubv2.types.list_failure_mode_assessments_response
    import capo_resiliencehubv2.types.list_failure_mode_findings_request
    import capo_resiliencehubv2.types.list_failure_mode_findings_response
    import capo_resiliencehubv2.types.list_input_sources_request
    import capo_resiliencehubv2.types.list_input_sources_response
    import capo_resiliencehubv2.types.list_policies_request
    import capo_resiliencehubv2.types.list_policies_response
    import capo_resiliencehubv2.types.list_policy_events_request
    import capo_resiliencehubv2.types.list_policy_events_response
    import capo_resiliencehubv2.types.list_reports_request
    import capo_resiliencehubv2.types.list_reports_response
    import capo_resiliencehubv2.types.list_resolved_test_run_target_resources_request
    import capo_resiliencehubv2.types.list_resolved_test_run_target_resources_response
    import capo_resiliencehubv2.types.list_resources_request
    import capo_resiliencehubv2.types.list_resources_response
    import capo_resiliencehubv2.types.list_service_events_request
    import capo_resiliencehubv2.types.list_service_events_response
    import capo_resiliencehubv2.types.list_service_functions_request
    import capo_resiliencehubv2.types.list_service_functions_response
    import capo_resiliencehubv2.types.list_service_topology_edges_request
    import capo_resiliencehubv2.types.list_service_topology_edges_response
    import capo_resiliencehubv2.types.list_services_request
    import capo_resiliencehubv2.types.list_services_response
    import capo_resiliencehubv2.types.list_system_events_request
    import capo_resiliencehubv2.types.list_system_events_response
    import capo_resiliencehubv2.types.list_systems_request
    import capo_resiliencehubv2.types.list_systems_response
    import capo_resiliencehubv2.types.list_tags_for_resource_request
    import capo_resiliencehubv2.types.list_tags_for_resource_response
    import capo_resiliencehubv2.types.list_test_run_dependencies_request
    import capo_resiliencehubv2.types.list_test_run_dependencies_response
    import capo_resiliencehubv2.types.list_test_run_events_request
    import capo_resiliencehubv2.types.list_test_run_events_response
    import capo_resiliencehubv2.types.list_test_run_source_events_request
    import capo_resiliencehubv2.types.list_test_run_source_events_response
    import capo_resiliencehubv2.types.list_test_run_sources_request
    import capo_resiliencehubv2.types.list_test_run_sources_response
    import capo_resiliencehubv2.types.list_test_runs_request
    import capo_resiliencehubv2.types.list_test_runs_response
    import capo_resiliencehubv2.types.list_test_sources_request
    import capo_resiliencehubv2.types.list_test_sources_response
    import capo_resiliencehubv2.types.list_test_templates_request
    import capo_resiliencehubv2.types.list_test_templates_response
    import capo_resiliencehubv2.types.list_tests_request
    import capo_resiliencehubv2.types.list_tests_response
    import capo_resiliencehubv2.types.list_user_journeys_request
    import capo_resiliencehubv2.types.list_user_journeys_response
    import capo_resiliencehubv2.types.logging_configuration
    import capo_resiliencehubv2.types.long_description
    import capo_resiliencehubv2.types.max_results
    import capo_resiliencehubv2.types.multi_az_disaster_recovery_approach
    import capo_resiliencehubv2.types.multi_az_targets
    import capo_resiliencehubv2.types.multi_region_disaster_recovery_approach
    import capo_resiliencehubv2.types.multi_region_targets
    import capo_resiliencehubv2.types.next_token
    import capo_resiliencehubv2.types.ou_id
    import capo_resiliencehubv2.types.permission_model
    import capo_resiliencehubv2.types.policy_event
    import capo_resiliencehubv2.types.policy_event_type_list
    import capo_resiliencehubv2.types.policy_summary
    import capo_resiliencehubv2.types.put_test_sources_request
    import capo_resiliencehubv2.types.put_test_sources_response
    import capo_resiliencehubv2.types.query_granularity
    import capo_resiliencehubv2.types.region_list
    import capo_resiliencehubv2.types.report_generation_result
    import capo_resiliencehubv2.types.report_type
    import capo_resiliencehubv2.types.resolved_target_resource
    import capo_resiliencehubv2.types.resource_configuration
    import capo_resiliencehubv2.types.resource_list
    import capo_resiliencehubv2.types.resource_type_filter_list
    import capo_resiliencehubv2.types.service_event
    import capo_resiliencehubv2.types.service_event_type_list
    import capo_resiliencehubv2.types.service_function
    import capo_resiliencehubv2.types.service_function_criticality
    import capo_resiliencehubv2.types.service_owned_arn
    import capo_resiliencehubv2.types.service_report_configuration
    import capo_resiliencehubv2.types.service_resource
    import capo_resiliencehubv2.types.service_summary
    import capo_resiliencehubv2.types.service_topology_edge_summary
    import capo_resiliencehubv2.types.sort_order
    import capo_resiliencehubv2.types.start_dependency_insights_request
    import capo_resiliencehubv2.types.start_dependency_insights_response
    import capo_resiliencehubv2.types.start_failure_mode_assessment_request
    import capo_resiliencehubv2.types.start_failure_mode_assessment_response
    import capo_resiliencehubv2.types.start_test_run_request
    import capo_resiliencehubv2.types.start_test_run_response
    import capo_resiliencehubv2.types.stop_condition_list
    import capo_resiliencehubv2.types.stop_test_run_request
    import capo_resiliencehubv2.types.stop_test_run_response
    import capo_resiliencehubv2.types.system_event
    import capo_resiliencehubv2.types.system_event_type_list
    import capo_resiliencehubv2.types.system_summary
    import capo_resiliencehubv2.types.tag_key_list
    import capo_resiliencehubv2.types.tag_map
    import capo_resiliencehubv2.types.tag_resource_request
    import capo_resiliencehubv2.types.tag_resource_response
    import capo_resiliencehubv2.types.test_id
    import capo_resiliencehubv2.types.test_parameters
    import capo_resiliencehubv2.types.test_run_dependency_summary
    import capo_resiliencehubv2.types.test_run_event
    import capo_resiliencehubv2.types.test_run_id
    import capo_resiliencehubv2.types.test_run_source_arn
    import capo_resiliencehubv2.types.test_run_source_event
    import capo_resiliencehubv2.types.test_run_source_summary
    import capo_resiliencehubv2.types.test_run_source_type
    import capo_resiliencehubv2.types.test_run_summary
    import capo_resiliencehubv2.types.test_source_input_list
    import capo_resiliencehubv2.types.test_source_summary
    import capo_resiliencehubv2.types.test_source_type
    import capo_resiliencehubv2.types.test_summary
    import capo_resiliencehubv2.types.untag_resource_request
    import capo_resiliencehubv2.types.untag_resource_response
    import capo_resiliencehubv2.types.update_assertion_request
    import capo_resiliencehubv2.types.update_assertion_response
    import capo_resiliencehubv2.types.update_dependency_request
    import capo_resiliencehubv2.types.update_dependency_response
    import capo_resiliencehubv2.types.update_failure_mode_finding_request
    import capo_resiliencehubv2.types.update_failure_mode_finding_response
    import capo_resiliencehubv2.types.update_policy_request
    import capo_resiliencehubv2.types.update_policy_response
    import capo_resiliencehubv2.types.update_service_function_request
    import capo_resiliencehubv2.types.update_service_function_response
    import capo_resiliencehubv2.types.update_service_request
    import capo_resiliencehubv2.types.update_service_response
    import capo_resiliencehubv2.types.update_system_request
    import capo_resiliencehubv2.types.update_system_response
    import capo_resiliencehubv2.types.update_test_request
    import capo_resiliencehubv2.types.update_test_response
    import capo_resiliencehubv2.types.update_user_journey_request
    import capo_resiliencehubv2.types.update_user_journey_response
    import capo_resiliencehubv2.types.user_journey_id
    import capo_resiliencehubv2.types.user_journey_summary
    import capo_resiliencehubv2.types.uuid


class resiliencehubv2ClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None
    anonymous: bool | None


class resiliencehubv2Client:
    """A client for the ``resiliencehubv2`` service.

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
        self._config = resiliencehubv2ClientConfig(
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
        self.iam_app_resource = IamAppResource(self)
        self.iam_policy_resource = IamPolicyResource(self)
        self.iam_resiliency_policy_resource = IamResiliencyPolicyResource(self)
        self.iam_service_resource = IamServiceResource(self)
        self.iam_system_resource = IamSystemResource(self)

    def operation_options(
        self, config_overrides: Optional[resiliencehubv2ClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: resiliencehubv2ClientConfig = config_overrides or {}
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

    def create_assertion(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        text: "capo_resiliencehubv2.types.assertion_text.AssertionText",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_assertion_response.CreateAssertionResponse":
        """<p>Creates a resilience assertion for a service.</p>

        Args:
            text: <p>The text content of the assertion.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_assertion_request.CreateAssertionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_assertion_response.CreateAssertionResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_assertion

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_assertion.create_assertion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_assertion_request.CreateAssertionRequest = {
            "service_arn": service_arn,
            "text": text,
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

    def create_input_source(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        resource_configuration: "capo_resiliencehubv2.types.resource_configuration.ResourceConfiguration",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_input_source_response.CreateInputSourceResponse":
        """<p>Creates an input source for a service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_input_source_request.CreateInputSourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_input_source_response.CreateInputSourceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_input_source

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_input_source.create_input_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_input_source_request.CreateInputSourceRequest = {
            "service_arn": service_arn,
            "resource_configuration": resource_configuration,
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

    def create_policy(
        self,
        name: "capo_resiliencehubv2.types.entity_name.EntityName",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        availability_slo: Optional[
            "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
        ] = None,
        multi_az: Optional[
            "capo_resiliencehubv2.types.multi_az_targets.MultiAzTargets"
        ] = None,
        multi_region: Optional[
            "capo_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
        ] = None,
        data_recovery: Optional[
            "capo_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
        ] = None,
        sharing_enabled: Optional[bool] = None,
        kms_key_id: Optional["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_policy_response.CreatePolicyResponse":
        """<p>Creates a resilience policy that defines availability and disaster recovery requirements.</p>

        Args:
            availability_slo: <p>The availability SLO for the resilience policy.</p>
            multi_az: <p>The multi-AZ disaster recovery targets for the resilience policy.</p>
            multi_region: <p>The multi-Region disaster recovery targets for the resilience policy.</p>
            data_recovery: <p>The data recovery targets for the resilience policy.</p>
            sharing_enabled: <p>Specifies whether cross-account sharing is enabled for the policy. Only a delegated administrator or the management account can enable sharing.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_policy_request.CreatePolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_policy_response.CreatePolicyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_policy

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_policy.create_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_policy_request.CreatePolicyRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if availability_slo is not None:
            input_["availability_slo"] = availability_slo
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if multi_region is not None:
            input_["multi_region"] = multi_region
        if data_recovery is not None:
            input_["data_recovery"] = data_recovery
        if sharing_enabled is not None:
            input_["sharing_enabled"] = sharing_enabled
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
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

    def create_report(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        report_type: "capo_resiliencehubv2.types.report_type.ReportType",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_report_response.CreateReportResponse":
        """<p>On-demand report creation. Idempotent — duplicate requests with same clientToken return existing result.</p>

        Args:
            report_type: <p>The type of report to generate.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_report_request.CreateReportRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_report_response.CreateReportResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_report

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_report.create_report(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_report_request.CreateReportRequest = {
            "service_arn": service_arn,
            "report_type": report_type,
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

    def create_service(
        self,
        name: "capo_resiliencehubv2.types.entity_name.EntityName",
        regions: "capo_resiliencehubv2.types.region_list.RegionList",
        permission_model: "capo_resiliencehubv2.types.permission_model.PermissionModel",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        associated_systems: Optional[
            "capo_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
        ] = None,
        policy_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        dependency_discovery: Optional[
            "capo_resiliencehubv2.types.dependency_discovery_input.DependencyDiscoveryInput"
        ] = None,
        report_configuration: Optional[
            "capo_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
        ] = None,
        kms_key_id: Optional["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_service_response.CreateServiceResponse":
        """<p>Creates a service.</p>

        Args:
            associated_systems: <p>The systems to associate with the service.</p>
            regions: <p>The Regions where the service operates.</p>
            permission_model: <p>The permission model for the service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_service_request.CreateServiceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_service_response.CreateServiceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_service

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_service.create_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_service_request.CreateServiceRequest = {
            "name": name,
            "regions": regions,
            "permission_model": permission_model,
        }
        if description is not None:
            input_["description"] = description
        if associated_systems is not None:
            input_["associated_systems"] = associated_systems
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
        if dependency_discovery is not None:
            input_["dependency_discovery"] = dependency_discovery
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
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

    def create_service_function(
        self,
        name: "capo_resiliencehubv2.types.entity_label.EntityLabel",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        criticality: "capo_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_service_function_response.CreateServiceFunctionResponse":
        """<p>Creates a service function within a service.</p>

        Args:
            criticality: <p>The criticality level of the service function.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_service_function_request.CreateServiceFunctionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_service_function_response.CreateServiceFunctionResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_service_function

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_service_function.create_service_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_service_function_request.CreateServiceFunctionRequest = {
            "name": name,
            "service_arn": service_arn,
            "criticality": criticality,
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

    def create_service_function_resources(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId",
        resources: "capo_resiliencehubv2.types.resource_list.ResourceList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.create_service_function_resources_response.CreateServiceFunctionResourcesResponse":
        """<p>Associates resources with a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to associate resources with.</p>
            resources: <p>The list of resources to associate with the service function.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_service_function_resources_request.CreateServiceFunctionResourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_service_function_resources_response.CreateServiceFunctionResourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_service_function_resources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_service_function_resources.create_service_function_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_service_function_resources_request.CreateServiceFunctionResourcesRequest = {
            "service_arn": service_arn,
            "service_function_id": service_function_id,
            "resources": resources,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_system(
        self,
        name: "capo_resiliencehubv2.types.entity_name.EntityName",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        sharing_enabled: Optional[bool] = None,
        kms_key_id: Optional["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"] = None,
        tags: Optional["capo_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_system_response.CreateSystemResponse":
        """<p>Creates a system that represents a logical grouping of services.</p>

        Args:
            sharing_enabled: <p>Indicates whether cross-account sharing is enabled for the system.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_system_request.CreateSystemRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_system_response.CreateSystemResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_system

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_system.create_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_system_request.CreateSystemRequest = {
            "name": name
        }
        if description is not None:
            input_["description"] = description
        if sharing_enabled is not None:
            input_["sharing_enabled"] = sharing_enabled
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if tags is not None:
            input_["tags"] = tags
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

    def create_test(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        logging_configuration: Optional[
            "capo_resiliencehubv2.types.logging_configuration.LoggingConfiguration"
        ] = None,
        stop_conditions: Optional[
            "capo_resiliencehubv2.types.stop_condition_list.StopConditionList"
        ] = None,
        role_name: Optional[
            "capo_resiliencehubv2.types.iam_role_name.IamRoleName"
        ] = None,
        parameters: Optional[
            "capo_resiliencehubv2.types.test_parameters.TestParameters"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_test_response.CreateTestResponse":
        """<p>Creates a test for a service by configuring a test template. Each service has one test per template.</p>

        Args:
            service_arn: <p>The ARN of the service to create the test for.</p>
            test_template_arn: <p>The ARN of the test template to configure.</p>
            logging_configuration: <p>The logging configuration for the test.</p>
            stop_conditions: <p>The stop conditions for the test.</p>
            role_name: <p>The name of the IAM execution role to use when running the test.</p>
            parameters: <p>The parameter values for the test.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_test_request.CreateTestRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_test_response.CreateTestResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_test

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_test.create_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_test_request.CreateTestRequest = {
            "service_arn": service_arn,
            "test_template_arn": test_template_arn,
        }
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if stop_conditions is not None:
            input_["stop_conditions"] = stop_conditions
        if role_name is not None:
            input_["role_name"] = role_name
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_user_journey(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        name: "capo_resiliencehubv2.types.entity_label.EntityLabel",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        policy_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.create_user_journey_response.CreateUserJourneyResponse":
        """<p>Creates a user journey within a system.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.create_user_journey_request.CreateUserJourneyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.create_user_journey_response.CreateUserJourneyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.create_user_journey

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.create_user_journey.create_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.create_user_journey_request.CreateUserJourneyRequest = {
            "system_arn": system_arn,
            "name": name,
        }
        if description is not None:
            input_["description"] = description
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
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

    def delete_assertion(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        assertion_id: "capo_resiliencehubv2.types.uuid.Uuid",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_assertion_response.DeleteAssertionResponse":
        """<p>Deletes a resilience assertion from a service.</p>

        Args:
            assertion_id: <p>The unique identifier of the assertion to delete.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_assertion_request.DeleteAssertionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_assertion_response.DeleteAssertionResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_assertion

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_assertion.delete_assertion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_assertion_request.DeleteAssertionRequest = {
            "service_arn": service_arn,
            "assertion_id": assertion_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_input_source(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        input_source_id: "capo_resiliencehubv2.types.input_source_id.InputSourceId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_input_source_response.DeleteInputSourceResponse":
        """<p>Deletes an input source.</p>

        Args:
            input_source_id: <p>The identifier of the input source to delete.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_input_source_request.DeleteInputSourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_input_source_response.DeleteInputSourceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_input_source

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_input_source.delete_input_source(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_input_source_request.DeleteInputSourceRequest = {
            "service_arn": service_arn,
            "input_source_id": input_source_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_policy(
        self,
        policy_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_policy_response.DeletePolicyResponse":
        """<p>Deletes a resilience policy.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_policy_request.DeletePolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_policy_response.DeletePolicyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_policy

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_policy.delete_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_policy_request.DeletePolicyRequest = {
            "policy_arn": policy_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_service_response.DeleteServiceResponse":
        """<p>Deletes a service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_service_request.DeleteServiceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_service_response.DeleteServiceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_service

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_service.delete_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_service_request.DeleteServiceRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_function(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_service_function_response.DeleteServiceFunctionResponse":
        """<p>Deletes a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to delete.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_service_function_request.DeleteServiceFunctionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_service_function_response.DeleteServiceFunctionResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_service_function

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_service_function.delete_service_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_service_function_request.DeleteServiceFunctionRequest = {
            "service_arn": service_arn,
            "service_function_id": service_function_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_service_function_resources(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId",
        resources: "capo_resiliencehubv2.types.resource_list.ResourceList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_service_function_resources_response.DeleteServiceFunctionResourcesResponse":
        """<p>Removes resources from a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to remove resources from.</p>
            resources: <p>The list of resources to remove from the service function.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_service_function_resources_request.DeleteServiceFunctionResourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_service_function_resources_response.DeleteServiceFunctionResourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_service_function_resources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_service_function_resources.delete_service_function_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_service_function_resources_request.DeleteServiceFunctionResourcesRequest = {
            "service_arn": service_arn,
            "service_function_id": service_function_id,
            "resources": resources,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_system(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_system_response.DeleteSystemResponse":
        """<p>Deletes a system.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_system_request.DeleteSystemRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_system_response.DeleteSystemResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_system

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_system.delete_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_system_request.DeleteSystemRequest = {
            "system_arn": system_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_test(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_test_response.DeleteTestResponse":
        """<p>Deletes a test.</p>

        Args:
            test_id: <p>The identifier of the test to delete.</p>
            service_arn: <p>The ARN of the service the test belongs to.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_test_request.DeleteTestRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_test_response.DeleteTestResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_test

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_test.delete_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_test_request.DeleteTestRequest = {
            "test_id": test_id,
            "service_arn": service_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_test_sources(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        test_sources: "capo_resiliencehubv2.types.test_source_input_list.TestSourceInputList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_test_sources_response.DeleteTestSourcesResponse":
        """<p>Removes monitoring sources from a test. The operation is transactional and idempotent — removing a source that is not attached is a no-op.</p>

        Args:
            test_id: <p>The identifier of the test to remove sources from.</p>
            service_arn: <p>The ARN of the service the test belongs to.</p>
            test_sources: <p>The monitoring sources to remove.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_test_sources_request.DeleteTestSourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_test_sources_response.DeleteTestSourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_test_sources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_test_sources.delete_test_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_test_sources_request.DeleteTestSourcesRequest = {
            "test_id": test_id,
            "service_arn": service_arn,
            "test_sources": test_sources,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_user_journey(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.delete_user_journey_response.DeleteUserJourneyResponse":
        """<p>Deletes a user journey.</p>

        Args:
            user_journey_id: <p>The identifier of the user journey to delete.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.delete_user_journey_request.DeleteUserJourneyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.delete_user_journey_response.DeleteUserJourneyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.delete_user_journey

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.delete_user_journey.delete_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.delete_user_journey_request.DeleteUserJourneyRequest = {
            "system_arn": system_arn,
            "user_journey_id": user_journey_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_dependency_insights(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_dependency_insights_response.GetDependencyInsightsResponse":
        """<p>Retrieves the dependency insights generated for a service. The response reports the current generation status; insights are populated once generation has completed. If generation failed, the response includes an error code, whose possible values are listed under the response's errorCode field, and a message describing the cause. To use this operation, you must have the <code>resiliencehub:GetDependencyInsights</code> permission on the service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_dependency_insights_request.GetDependencyInsightsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_dependency_insights_response.GetDependencyInsightsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_dependency_insights

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_dependency_insights.get_dependency_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_dependency_insights_request.GetDependencyInsightsRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_failure_mode_finding(
        self,
        finding_id: "capo_resiliencehubv2.types.uuid.Uuid",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_failure_mode_finding_response.GetFailureModeFindingResponse":
        """<p>Retrieves a finding by findingId.</p>

        Args:
            finding_id: <p>The unique identifier of the finding to retrieve.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_failure_mode_finding_request.GetFailureModeFindingRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_failure_mode_finding_response.GetFailureModeFindingResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_failure_mode_finding

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_failure_mode_finding.get_failure_mode_finding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_failure_mode_finding_request.GetFailureModeFindingRequest = {
            "finding_id": finding_id,
            "service_arn": service_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_policy(
        self,
        policy_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_policy_response.GetPolicyResponse":
        """<p>Retrieves a resilience policy by ARN.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_policy_request.GetPolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_policy_response.GetPolicyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_policy

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_policy.get_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_policy_request.GetPolicyRequest = {
            "policy_arn": policy_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_service(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_service_response.GetServiceResponse":
        """<p>Retrieves a service by ARN.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_service_request.GetServiceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_service_response.GetServiceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_service

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_service.get_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_service_request.GetServiceRequest = {
            "service_arn": service_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_system(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_system_response.GetSystemResponse":
        """<p>Retrieves a system by ARN.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_system_request.GetSystemRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_system_response.GetSystemResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_system

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_system.get_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_system_request.GetSystemRequest = {
            "system_arn": system_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_test(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_test_response.GetTestResponse":
        """<p>Retrieves a test by ID.</p>

        Args:
            test_id: <p>The identifier of the test to retrieve.</p>
            service_arn: <p>The ARN of the service the test belongs to.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_test_request.GetTestRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_test_response.GetTestResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_test

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_test.get_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_test_request.GetTestRequest = {
            "test_id": test_id,
            "service_arn": service_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_test_run(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_test_run_response.GetTestRunResponse":
        """<p>Retrieves a test run by ID, including its status, results, and the configuration snapshotted when the run started.</p>

        Args:
            test_run_id: <p>The identifier of the test run to retrieve.</p>
            service_arn: <p>The ARN of the service the test run belongs to.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_test_run_request.GetTestRunRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_test_run_response.GetTestRunResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_test_run

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_test_run.get_test_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_test_run_request.GetTestRunRequest = {
            "test_run_id": test_run_id,
            "service_arn": service_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_test_template(
        self,
        test_template_arn: "capo_resiliencehubv2.types.service_owned_arn.ServiceOwnedArn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> (
        "capo_resiliencehubv2.types.get_test_template_response.GetTestTemplateResponse"
    ):
        """<p>Retrieves a resilience test template by ARN, including the parameters it accepts and the fault actions it runs.</p>

        Args:
            test_template_arn: <p>The ARN of the test template to retrieve.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_test_template_request.GetTestTemplateRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_test_template_response.GetTestTemplateResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_test_template

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_test_template.get_test_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_test_template_request.GetTestTemplateRequest = {
            "test_template_arn": test_template_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_user_journey(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.get_user_journey_response.GetUserJourneyResponse":
        """<p>Retrieves a user journey.</p>

        Args:
            user_journey_id: <p>The identifier of the user journey to retrieve.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.get_user_journey_request.GetUserJourneyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.get_user_journey_response.GetUserJourneyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.get_user_journey

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.get_user_journey.get_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.get_user_journey_request.GetUserJourneyRequest = {
            "system_arn": system_arn,
            "user_journey_id": user_journey_id,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_app(
        self,
        v1_app_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        policy_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        kms_key_id: Optional["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"] = None,
        skip_manually_added_resources: Optional[bool] = None,
        associated_systems: Optional[
            "capo_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
        ] = None,
        tags: Optional["capo_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.import_app_response.ImportAppResponse":
        """<p>Imports a V1 app into the V2 resource model, creating a service with the same name.</p>

        Args:
            skip_manually_added_resources: <p>Whether to skip manually added resources during import.</p>
            associated_systems: <p>The systems to associate with the imported service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.import_app_request.ImportAppRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.import_app_response.ImportAppResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.import_app

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.import_app.import_app(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.import_app_request.ImportAppRequest = {
            "v1_app_arn": v1_app_arn
        }
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if skip_manually_added_resources is not None:
            input_["skip_manually_added_resources"] = skip_manually_added_resources
        if associated_systems is not None:
            input_["associated_systems"] = associated_systems
        if tags is not None:
            input_["tags"] = tags
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

    def import_policy(
        self,
        v1_policy_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        kms_key_id: Optional["capo_resiliencehubv2.types.kms_key_id.KmsKeyId"] = None,
        availability_slo: Optional[
            "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
        ] = None,
        multi_az_disaster_recovery_approach: Optional[
            "capo_resiliencehubv2.types.multi_az_disaster_recovery_approach.MultiAzDisasterRecoveryApproach"
        ] = None,
        multi_region_disaster_recovery_approach: Optional[
            "capo_resiliencehubv2.types.multi_region_disaster_recovery_approach.MultiRegionDisasterRecoveryApproach"
        ] = None,
        tags: Optional["capo_resiliencehubv2.types.tag_map.TagMap"] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.import_policy_response.ImportPolicyResponse":
        """<p>Imports a V1 policy into V2, mapping RTO/RPO values from V1 scenarios.</p>

        Args:
            availability_slo: <p>The availability SLO to set on the imported policy.</p>
            multi_az_disaster_recovery_approach: <p>The multi-AZ disaster recovery approach for the imported policy.</p>
            multi_region_disaster_recovery_approach: <p>The multi-Region disaster recovery approach for the imported policy.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.import_policy_request.ImportPolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.import_policy_response.ImportPolicyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.import_policy

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.import_policy.import_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.import_policy_request.ImportPolicyRequest = {
            "v1_policy_arn": v1_policy_arn
        }
        if kms_key_id is not None:
            input_["kms_key_id"] = kms_key_id
        if availability_slo is not None:
            input_["availability_slo"] = availability_slo
        if multi_az_disaster_recovery_approach is not None:
            input_["multi_az_disaster_recovery_approach"] = (
                multi_az_disaster_recovery_approach
            )
        if multi_region_disaster_recovery_approach is not None:
            input_["multi_region_disaster_recovery_approach"] = (
                multi_region_disaster_recovery_approach
            )
        if tags is not None:
            input_["tags"] = tags
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

    def list_assertions(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        source: Optional[
            "capo_resiliencehubv2.types.assertion_source.AssertionSource"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_assertions_response.ListAssertionsResponse":
        """<p>Lists resilience assertions for a service.</p>

        Args:
            source: <p>Filter assertions by source type.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_assertions_request.ListAssertionsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_assertions_response.ListAssertionsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_assertions

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_assertions.list_assertions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_assertions_request.ListAssertionsRequest = {
            "service_arn": service_arn
        }
        if source is not None:
            input_["source"] = source
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

    def iter_list_assertions(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        source: Optional[
            "capo_resiliencehubv2.types.assertion_source.AssertionSource"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.assertion.Assertion]":
        _token = next_token
        while True:
            _response = self.list_assertions(
                service_arn,
                config_overrides=config_overrides,
                source=source,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assertions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_dependencies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        query_range_start_time: Optional[datetime.datetime] = None,
        query_range_end_time: Optional[datetime.datetime] = None,
        query_range_granularity: Optional[
            "capo_resiliencehubv2.types.query_granularity.QueryGranularity"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> (
        "capo_resiliencehubv2.types.list_dependencies_response.ListDependenciesResponse"
    ):
        """<p>Lists dependencies discovered for services.</p>

        Args:
            query_range_start_time: <p>The start time for the dependency query range.</p>
            query_range_end_time: <p>The end time for the dependency query range.</p>
            query_range_granularity: <p>The granularity for the dependency query range.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_dependencies_request.ListDependenciesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_dependencies_response.ListDependenciesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_dependencies

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_dependencies.list_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_dependencies_request.ListDependenciesRequest = {}
        if service_arn is not None:
            input_["service_arn"] = service_arn
        if query_range_start_time is not None:
            input_["query_range_start_time"] = query_range_start_time
        if query_range_end_time is not None:
            input_["query_range_end_time"] = query_range_end_time
        if query_range_granularity is not None:
            input_["query_range_granularity"] = query_range_granularity
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

    def iter_list_dependencies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        query_range_start_time: Optional[datetime.datetime] = None,
        query_range_end_time: Optional[datetime.datetime] = None,
        query_range_granularity: Optional[
            "capo_resiliencehubv2.types.query_granularity.QueryGranularity"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.dependency_summary.DependencySummary]":
        _token = next_token
        while True:
            _response = self.list_dependencies(
                config_overrides=config_overrides,
                service_arn=service_arn,
                query_range_start_time=query_range_start_time,
                query_range_end_time=query_range_end_time,
                query_range_granularity=query_range_granularity,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dependency_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_failure_mode_assessments(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        assessment_statuses: Optional[
            "capo_resiliencehubv2.types.assessment_status_list.AssessmentStatusList"
        ] = None,
        started_after: Optional[datetime.datetime] = None,
        ended_before: Optional[datetime.datetime] = None,
        sort_by: Optional[
            "capo_resiliencehubv2.types.assessment_sort_field.AssessmentSortField"
        ] = None,
        sort_order: Optional["capo_resiliencehubv2.types.sort_order.SortOrder"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_failure_mode_assessments_response.ListFailureModeAssessmentsResponse":
        """<p>Lists failure mode assessments.</p>

        Args:
            assessment_statuses: <p>Specifies the assessment statuses to include in the results.</p>
            started_after: <p>Specifies that only assessments that started at or after this timestamp appear in the results.</p>
            ended_before: <p>Specifies that only assessments that ended at or before this timestamp appear in the results.</p>
            sort_by: <p>The field to use for sorting failure mode assessments.</p>
            sort_order: <p>The sort order for results.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_failure_mode_assessments_request.ListFailureModeAssessmentsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_failure_mode_assessments_response.ListFailureModeAssessmentsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_assessments

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_assessments.list_failure_mode_assessments(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_failure_mode_assessments_request.ListFailureModeAssessmentsRequest = {
            "service_arn": service_arn
        }
        if assessment_statuses is not None:
            input_["assessment_statuses"] = assessment_statuses
        if started_after is not None:
            input_["started_after"] = started_after
        if ended_before is not None:
            input_["ended_before"] = ended_before
        if sort_by is not None:
            input_["sort_by"] = sort_by
        if sort_order is not None:
            input_["sort_order"] = sort_order
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

    def iter_list_failure_mode_assessments(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        assessment_statuses: Optional[
            "capo_resiliencehubv2.types.assessment_status_list.AssessmentStatusList"
        ] = None,
        started_after: Optional[datetime.datetime] = None,
        ended_before: Optional[datetime.datetime] = None,
        sort_by: Optional[
            "capo_resiliencehubv2.types.assessment_sort_field.AssessmentSortField"
        ] = None,
        sort_order: Optional["capo_resiliencehubv2.types.sort_order.SortOrder"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.assessment_summary.AssessmentSummary]":
        _token = next_token
        while True:
            _response = self.list_failure_mode_assessments(
                service_arn,
                config_overrides=config_overrides,
                assessment_statuses=assessment_statuses,
                started_after=started_after,
                ended_before=ended_before,
                sort_by=sort_by,
                sort_order=sort_order,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("assessment_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_failure_mode_findings(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        severity: Optional[
            "capo_resiliencehubv2.types.finding_severity.FindingSeverity"
        ] = None,
        failure_category: Optional[
            "capo_resiliencehubv2.types.failure_category.FailureCategory"
        ] = None,
        status: Optional[
            "capo_resiliencehubv2.types.finding_status.FindingStatus"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_failure_mode_findings_response.ListFailureModeFindingsResponse":
        """<p>List findings.</p>

        Args:
            severity: <p>Filter findings by severity.</p>
            failure_category: <p>Filter findings by failure category.</p>
            status: <p>Filter findings by status.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_failure_mode_findings_request.ListFailureModeFindingsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_failure_mode_findings_response.ListFailureModeFindingsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_findings

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_failure_mode_findings.list_failure_mode_findings(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_failure_mode_findings_request.ListFailureModeFindingsRequest = {
            "service_arn": service_arn
        }
        if severity is not None:
            input_["severity"] = severity
        if failure_category is not None:
            input_["failure_category"] = failure_category
        if status is not None:
            input_["status"] = status
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

    def iter_list_failure_mode_findings(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        severity: Optional[
            "capo_resiliencehubv2.types.finding_severity.FindingSeverity"
        ] = None,
        failure_category: Optional[
            "capo_resiliencehubv2.types.failure_category.FailureCategory"
        ] = None,
        status: Optional[
            "capo_resiliencehubv2.types.finding_status.FindingStatus"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.finding_summary.FindingSummary]":
        _token = next_token
        while True:
            _response = self.list_failure_mode_findings(
                service_arn,
                config_overrides=config_overrides,
                severity=severity,
                failure_category=failure_category,
                status=status,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("findings_summary",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_input_sources(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "capo_resiliencehubv2.types.input_source_type.InputSourceType"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_input_sources_response.ListInputSourcesResponse":
        """<p>Lists input sources for a service.</p>

        Args:
            type: <p>Filter input sources by type.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_input_sources_request.ListInputSourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_input_sources_response.ListInputSourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_input_sources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_input_sources.list_input_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_input_sources_request.ListInputSourcesRequest = {
            "service_arn": service_arn
        }
        if type is not None:
            input_["type"] = type
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

    def iter_list_input_sources(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "capo_resiliencehubv2.types.input_source_type.InputSourceType"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.input_source_summary.InputSourceSummary]":
        _token = next_token
        while True:
            _response = self.list_input_sources(
                service_arn,
                config_overrides=config_overrides,
                type=type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("input_source_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        account_id: Optional["capo_resiliencehubv2.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_policies_response.ListPoliciesResponse":
        """<p>Lists resilience policies.</p>

        Args:
            account_id: <p>The identifier of the account that owns the policies to include in the results.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_policies_request.ListPoliciesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_policies_response.ListPoliciesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_policies

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_policies.list_policies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_policies_request.ListPoliciesRequest = {}
        if account_id is not None:
            input_["account_id"] = account_id
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

    def iter_list_policies(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        account_id: Optional["capo_resiliencehubv2.types.account_id.AccountId"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.policy_summary.PolicySummary]":
        _token = next_token
        while True:
            _response = self.list_policies(
                config_overrides=config_overrides,
                account_id=account_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("policy_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_policy_events(
        self,
        policy_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "capo_resiliencehubv2.types.policy_event_type_list.PolicyEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_policy_events_response.ListPolicyEventsResponse":
        """<p>Lists events for a resilience policy, including services that started or stopped using it, changes to cross-account sharing, and deletion of the policy.</p>

        Args:
            event_types: <p>The type of events to include in the results.</p>
            start_time: <p>The start time for filtering events.</p>
            end_time: <p>The end time for filtering events.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_policy_events_request.ListPolicyEventsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_policy_events_response.ListPolicyEventsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_policy_events

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_policy_events.list_policy_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_policy_events_request.ListPolicyEventsRequest = {
            "policy_arn": policy_arn
        }
        if event_types is not None:
            input_["event_types"] = event_types
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

    def iter_list_policy_events(
        self,
        policy_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "capo_resiliencehubv2.types.policy_event_type_list.PolicyEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.policy_event.PolicyEvent]":
        _token = next_token
        while True:
            _response = self.list_policy_events(
                policy_arn,
                config_overrides=config_overrides,
                event_types=event_types,
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

    def list_reports(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        report_type: Optional[
            "capo_resiliencehubv2.types.report_type.ReportType"
        ] = None,
        test_run_id: Optional[
            "capo_resiliencehubv2.types.test_run_id.TestRunId"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_reports_response.ListReportsResponse":
        """<p>List reports for a service, or all reports owned by the account if serviceArn is not provided.</p>

        Args:
            service_arn: <p>Optional. If not provided, lists all reports owned by the account.</p>
            report_type: <p>Filter reports by type.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_reports_request.ListReportsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_reports_response.ListReportsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_reports

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_reports.list_reports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_reports_request.ListReportsRequest = {}
        if service_arn is not None:
            input_["service_arn"] = service_arn
        if report_type is not None:
            input_["report_type"] = report_type
        if test_run_id is not None:
            input_["test_run_id"] = test_run_id
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

    def iter_list_reports(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        report_type: Optional[
            "capo_resiliencehubv2.types.report_type.ReportType"
        ] = None,
        test_run_id: Optional[
            "capo_resiliencehubv2.types.test_run_id.TestRunId"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.report_generation_result.ReportGenerationResult]":
        _token = next_token
        while True:
            _response = self.list_reports(
                config_overrides=config_overrides,
                service_arn=service_arn,
                report_type=report_type,
                test_run_id=test_run_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("report_generation_results",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resolved_test_run_target_resources(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_resolved_test_run_target_resources_response.ListResolvedTestRunTargetResourcesResponse":
        """<p>Lists the AWS resources that AWS Fault Injection Service (AWS FIS) resolved as targets for a test run.</p>

        Args:
            test_run_id: <p>The identifier of the test run to list resolved target resources for.</p>
            service_arn: <p>The ARN of the service the test run belongs to.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_resolved_test_run_target_resources_request.ListResolvedTestRunTargetResourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_resolved_test_run_target_resources_response.ListResolvedTestRunTargetResourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_resolved_test_run_target_resources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_resolved_test_run_target_resources.list_resolved_test_run_target_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_resolved_test_run_target_resources_request.ListResolvedTestRunTargetResourcesRequest = {
            "test_run_id": test_run_id,
            "service_arn": service_arn,
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

    def iter_list_resolved_test_run_target_resources(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.resolved_target_resource.ResolvedTargetResource]":
        _token = next_token
        while True:
            _response = self.list_resolved_test_run_target_resources(
                test_run_id,
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("resolved_target_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resources(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_function_id: Optional[
            "capo_resiliencehubv2.types.entity_id.EntityId"
        ] = None,
        aws_region: Optional["capo_resiliencehubv2.types.aws_region.AwsRegion"] = None,
        resource_types: Optional[
            "capo_resiliencehubv2.types.resource_type_filter_list.ResourceTypeFilterList"
        ] = None,
        billable: Optional[bool] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_resources_response.ListResourcesResponse":
        """<p>List resources.</p>

        Args:
            service_function_id: <p>Filter resources by service function identifier.</p>
            aws_region: <p>Filter resources by AWS Region.</p>
            resource_types: <p>The CloudFormation resource types to include in the response.</p>
            billable: <p>Specifies whether to filter non-billable resources. When true (the default), the operation returns only billable resources.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_resources_request.ListResourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_resources_response.ListResourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_resources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_resources.list_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_resources_request.ListResourcesRequest = {
            "service_arn": service_arn
        }
        if service_function_id is not None:
            input_["service_function_id"] = service_function_id
        if aws_region is not None:
            input_["aws_region"] = aws_region
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if billable is not None:
            input_["billable"] = billable
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

    def iter_list_resources(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        service_function_id: Optional[
            "capo_resiliencehubv2.types.entity_id.EntityId"
        ] = None,
        aws_region: Optional["capo_resiliencehubv2.types.aws_region.AwsRegion"] = None,
        resource_types: Optional[
            "capo_resiliencehubv2.types.resource_type_filter_list.ResourceTypeFilterList"
        ] = None,
        billable: Optional[bool] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.service_resource.ServiceResource]":
        _token = next_token
        while True:
            _response = self.list_resources(
                service_arn,
                config_overrides=config_overrides,
                service_function_id=service_function_id,
                aws_region=aws_region,
                resource_types=resource_types,
                billable=billable,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_events(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "capo_resiliencehubv2.types.service_event_type_list.ServiceEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_service_events_response.ListServiceEventsResponse":
        """<p>Lists events for a service.</p>

        Args:
            event_types: <p>The type of events to include in the results.</p>
            start_time: <p>The start time for filtering events.</p>
            end_time: <p>The end time for filtering events.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_service_events_request.ListServiceEventsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_service_events_response.ListServiceEventsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_service_events

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_service_events.list_service_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_service_events_request.ListServiceEventsRequest = {
            "service_arn": service_arn
        }
        if event_types is not None:
            input_["event_types"] = event_types
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

    def iter_list_service_events(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "capo_resiliencehubv2.types.service_event_type_list.ServiceEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.service_event.ServiceEvent]":
        _token = next_token
        while True:
            _response = self.list_service_events(
                service_arn,
                config_overrides=config_overrides,
                event_types=event_types,
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

    def list_service_functions(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_service_functions_response.ListServiceFunctionsResponse":
        """<p>Lists service functions for a service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_service_functions_request.ListServiceFunctionsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_service_functions_response.ListServiceFunctionsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_service_functions

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_service_functions.list_service_functions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_service_functions_request.ListServiceFunctionsRequest = {
            "service_arn": service_arn
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

    def iter_list_service_functions(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.service_function.ServiceFunction]":
        _token = next_token
        while True:
            _response = self.list_service_functions(
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_functions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_services(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        system_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        user_journey_id: Optional[
            "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
        ] = None,
        ou_id: Optional["capo_resiliencehubv2.types.ou_id.OuId"] = None,
        account_id: Optional["capo_resiliencehubv2.types.account_id.AccountId"] = None,
        assessment_status: Optional[
            "capo_resiliencehubv2.types.assessment_status.AssessmentStatus"
        ] = None,
        policy_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_services_response.ListServicesResponse":
        """<p>Lists services.</p>

        Args:
            user_journey_id: <p>Filter services by user journey identifier.</p>
            ou_id: <p>Filter services by organizational unit (OU) identifier.</p>
            account_id: <p>Filter services by AWS account ID.</p>
            assessment_status: <p>Filter services by assessment status.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_services_request.ListServicesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_services_response.ListServicesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_services

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_services.list_services(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_services_request.ListServicesRequest = {}
        if system_arn is not None:
            input_["system_arn"] = system_arn
        if user_journey_id is not None:
            input_["user_journey_id"] = user_journey_id
        if ou_id is not None:
            input_["ou_id"] = ou_id
        if account_id is not None:
            input_["account_id"] = account_id
        if assessment_status is not None:
            input_["assessment_status"] = assessment_status
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
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

    def iter_list_services(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        system_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        user_journey_id: Optional[
            "capo_resiliencehubv2.types.user_journey_id.UserJourneyId"
        ] = None,
        ou_id: Optional["capo_resiliencehubv2.types.ou_id.OuId"] = None,
        account_id: Optional["capo_resiliencehubv2.types.account_id.AccountId"] = None,
        assessment_status: Optional[
            "capo_resiliencehubv2.types.assessment_status.AssessmentStatus"
        ] = None,
        policy_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.service_summary.ServiceSummary]":
        _token = next_token
        while True:
            _response = self.list_services(
                config_overrides=config_overrides,
                system_arn=system_arn,
                user_journey_id=user_journey_id,
                ou_id=ou_id,
                account_id=account_id,
                assessment_status=assessment_status,
                policy_arn=policy_arn,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_service_topology_edges(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_service_topology_edges_response.ListServiceTopologyEdgesResponse":
        """<p>Lists topology edges for a service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_service_topology_edges_request.ListServiceTopologyEdgesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_service_topology_edges_response.ListServiceTopologyEdgesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_service_topology_edges

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_service_topology_edges.list_service_topology_edges(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_service_topology_edges_request.ListServiceTopologyEdgesRequest = {
            "service_arn": service_arn
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

    def iter_list_service_topology_edges(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.service_topology_edge_summary.ServiceTopologyEdgeSummary]":
        _token = next_token
        while True:
            _response = self.list_service_topology_edges(
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("service_topology_edge_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_system_events(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "capo_resiliencehubv2.types.system_event_type_list.SystemEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_system_events_response.ListSystemEventsResponse":
        """<p>Lists events for a system.</p>

        Args:
            event_types: <p>The type of events to include in the results.</p>
            start_time: <p>The start time for filtering events.</p>
            end_time: <p>The end time for filtering events.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_system_events_request.ListSystemEventsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_system_events_response.ListSystemEventsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_system_events

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_system_events.list_system_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_system_events_request.ListSystemEventsRequest = {
            "system_arn": system_arn
        }
        if event_types is not None:
            input_["event_types"] = event_types
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

    def iter_list_system_events(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        event_types: Optional[
            "capo_resiliencehubv2.types.system_event_type_list.SystemEventTypeList"
        ] = None,
        start_time: Optional[datetime.datetime] = None,
        end_time: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.system_event.SystemEvent]":
        _token = next_token
        while True:
            _response = self.list_system_events(
                system_arn,
                config_overrides=config_overrides,
                event_types=event_types,
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

    def list_systems(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        ou_id: Optional["capo_resiliencehubv2.types.ou_id.OuId"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_systems_response.ListSystemsResponse":
        """<p>Lists systems.</p>

        Args:
            ou_id: <p>Filter systems by organizational unit (OU) identifier.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_systems_request.ListSystemsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_systems_response.ListSystemsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_systems

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_systems.list_systems(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_systems_request.ListSystemsRequest = {}
        if ou_id is not None:
            input_["ou_id"] = ou_id
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

    def iter_list_systems(
        self,
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        ou_id: Optional["capo_resiliencehubv2.types.ou_id.OuId"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.system_summary.SystemSummary]":
        _token = next_token
        while True:
            _response = self.list_systems(
                config_overrides=config_overrides,
                ou_id=ou_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("system_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tags_for_resource(
        self,
        resource_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.list_tags_for_resource_response.ListTagsForResourceResponse":
        """<p>Lists the tags for a resource.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_tags_for_resource_request.ListTagsForResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_tags_for_resource_response.ListTagsForResourceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_tags_for_resource

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_tags_for_resource.list_tags_for_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_tags_for_resource_request.ListTagsForResourceRequest = {
            "resource_arn": resource_arn
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_test_run_dependencies(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_test_run_dependencies_response.ListTestRunDependenciesResponse":
        """<p>Lists the dependencies that a test run blocked. Each dependency reflects the discovered classification captured when the run started, so results do not change if a dependency is reclassified after the run.</p>

        Args:
            test_run_id: <p>The identifier of the test run to list dependencies for.</p>
            service_arn: <p>The ARN of the service the test run belongs to.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_test_run_dependencies_request.ListTestRunDependenciesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_test_run_dependencies_response.ListTestRunDependenciesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_dependencies

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_dependencies.list_test_run_dependencies(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_test_run_dependencies_request.ListTestRunDependenciesRequest = {
            "test_run_id": test_run_id,
            "service_arn": service_arn,
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

    def iter_list_test_run_dependencies(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.test_run_dependency_summary.TestRunDependencySummary]":
        _token = next_token
        while True:
            _response = self.list_test_run_dependencies(
                test_run_id,
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("dependencies",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_test_run_events(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        started_at: Optional[datetime.datetime] = None,
        ended_at: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_test_run_events_response.ListTestRunEventsResponse":
        """<p>Lists the events in a test run's timeline.</p>

        Args:
            test_run_id: <p>The identifier of the test run to list events for.</p>
            service_arn: <p>The ARN of the service the test run belongs to.</p>
            started_at: <p>Return events at or after this timestamp.</p>
            ended_at: <p>Return events at or before this timestamp.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_test_run_events_request.ListTestRunEventsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_test_run_events_response.ListTestRunEventsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_events

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_events.list_test_run_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_test_run_events_request.ListTestRunEventsRequest = {
            "test_run_id": test_run_id,
            "service_arn": service_arn,
        }
        if started_at is not None:
            input_["started_at"] = started_at
        if ended_at is not None:
            input_["ended_at"] = ended_at
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

    def iter_list_test_run_events(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        started_at: Optional[datetime.datetime] = None,
        ended_at: Optional[datetime.datetime] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.test_run_event.TestRunEvent]":
        _token = next_token
        while True:
            _response = self.list_test_run_events(
                test_run_id,
                service_arn,
                config_overrides=config_overrides,
                started_at=started_at,
                ended_at=ended_at,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_test_runs(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        test_id: Optional["capo_resiliencehubv2.types.test_id.TestId"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_test_runs_response.ListTestRunsResponse":
        """<p>Lists the runs of a test, or all test runs for a service.</p>

        Args:
            service_arn: <p>The ARN of the service to list test runs for.</p>
            test_id: <p>Filter test runs by test identifier.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_test_runs_request.ListTestRunsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_test_runs_response.ListTestRunsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_test_runs

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_test_runs.list_test_runs(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_test_runs_request.ListTestRunsRequest = {
            "service_arn": service_arn
        }
        if test_id is not None:
            input_["test_id"] = test_id
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

    def iter_list_test_runs(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        test_id: Optional["capo_resiliencehubv2.types.test_id.TestId"] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.test_run_summary.TestRunSummary]":
        _token = next_token
        while True:
            _response = self.list_test_runs(
                service_arn,
                config_overrides=config_overrides,
                test_id=test_id,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("test_runs",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_test_run_source_events(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        source_arn: "capo_resiliencehubv2.types.test_run_source_arn.TestRunSourceArn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_test_run_source_events_response.ListTestRunSourceEventsResponse":
        """<p>Lists the state-change events observed for a test run monitoring source. Events are returned for one source per call, in chronological order.</p>

        Args:
            test_run_id: <p>The identifier of the test run to list source events for.</p>
            service_arn: <p>The ARN of the service the test run belongs to.</p>
            source_arn: <p>The ARN of the monitoring source to list events for, such as the ARN of a CloudWatch alarm. If the source was not monitored during the test run, the response is an empty list.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_test_run_source_events_request.ListTestRunSourceEventsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_test_run_source_events_response.ListTestRunSourceEventsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_source_events

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_source_events.list_test_run_source_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_test_run_source_events_request.ListTestRunSourceEventsRequest = {
            "test_run_id": test_run_id,
            "service_arn": service_arn,
            "source_arn": source_arn,
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

    def iter_list_test_run_source_events(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        source_arn: "capo_resiliencehubv2.types.test_run_source_arn.TestRunSourceArn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> (
        "Iterator[capo_resiliencehubv2.types.test_run_source_event.TestRunSourceEvent]"
    ):
        _token = next_token
        while True:
            _response = self.list_test_run_source_events(
                test_run_id,
                service_arn,
                source_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("test_run_source_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_test_run_sources(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "capo_resiliencehubv2.types.test_run_source_type.TestRunSourceType"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_test_run_sources_response.ListTestRunSourcesResponse":
        """<p>Lists the monitoring source snapshots captured for a test run, optionally filtered by type.</p>

        Args:
            test_run_id: <p>The identifier of the test run to list sources for.</p>
            service_arn: <p>The ARN of the service the test run belongs to.</p>
            type: <p>Filter sources by type.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_test_run_sources_request.ListTestRunSourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_test_run_sources_response.ListTestRunSourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_sources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_test_run_sources.list_test_run_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_test_run_sources_request.ListTestRunSourcesRequest = {
            "test_run_id": test_run_id,
            "service_arn": service_arn,
        }
        if type is not None:
            input_["type"] = type
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

    def iter_list_test_run_sources(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "capo_resiliencehubv2.types.test_run_source_type.TestRunSourceType"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.test_run_source_summary.TestRunSourceSummary]":
        _token = next_token
        while True:
            _response = self.list_test_run_sources(
                test_run_id,
                service_arn,
                config_overrides=config_overrides,
                type=type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("test_run_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_tests(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_tests_response.ListTestsResponse":
        """<p>Lists the tests configured for a service.</p>

        Args:
            service_arn: <p>The ARN of the service to list tests for.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_tests_request.ListTestsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_tests_response.ListTestsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_tests

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_tests.list_tests(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_tests_request.ListTestsRequest = {
            "service_arn": service_arn
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

    def iter_list_tests(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.test_summary.TestSummary]":
        _token = next_token
        while True:
            _response = self.list_tests(
                service_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("tests",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_test_sources(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "capo_resiliencehubv2.types.test_source_type.TestSourceType"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> (
        "capo_resiliencehubv2.types.list_test_sources_response.ListTestSourcesResponse"
    ):
        """<p>Lists the monitoring sources attached to a test, optionally filtered by type.</p>

        Args:
            test_id: <p>The identifier of the test to list sources for.</p>
            service_arn: <p>The ARN of the service the test belongs to.</p>
            type: <p>Filter sources by type.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_test_sources_request.ListTestSourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_test_sources_response.ListTestSourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_test_sources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_test_sources.list_test_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_test_sources_request.ListTestSourcesRequest = {
            "test_id": test_id,
            "service_arn": service_arn,
        }
        if type is not None:
            input_["type"] = type
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

    def iter_list_test_sources(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        type: Optional[
            "capo_resiliencehubv2.types.test_source_type.TestSourceType"
        ] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.test_source_summary.TestSourceSummary]":
        _token = next_token
        while True:
            _response = self.list_test_sources(
                test_id,
                service_arn,
                config_overrides=config_overrides,
                type=type,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("test_sources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_test_templates(
        self, *, config_overrides: Optional[resiliencehubv2ClientConfig] = None
    ) -> "capo_resiliencehubv2.types.list_test_templates_response.ListTestTemplatesResponse":
        """<p>Lists the available resilience test templates. A test template is a pre-configured, AWS recommended test that defines which resilience capability to validate.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_test_templates_request.ListTestTemplatesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_test_templates_response.ListTestTemplatesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_test_templates

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_test_templates.list_test_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_test_templates_request.ListTestTemplatesRequest = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_user_journeys(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "capo_resiliencehubv2.types.list_user_journeys_response.ListUserJourneysResponse":
        """<p>Lists user journeys for a system.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.list_user_journeys_request.ListUserJourneysRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.list_user_journeys_response.ListUserJourneysResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.list_user_journeys

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.list_user_journeys.list_user_journeys(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.list_user_journeys_request.ListUserJourneysRequest = {
            "system_arn": system_arn
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

    def iter_list_user_journeys(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        max_results: Optional[
            "capo_resiliencehubv2.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_resiliencehubv2.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_resiliencehubv2.types.user_journey_summary.UserJourneySummary]":
        _token = next_token
        while True:
            _response = self.list_user_journeys(
                system_arn,
                config_overrides=config_overrides,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("user_journey_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def put_test_sources(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        test_sources: "capo_resiliencehubv2.types.test_source_input_list.TestSourceInputList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.put_test_sources_response.PutTestSourcesResponse":
        """<p>Adds or updates the monitoring sources on a test. The operation is transactional — either every source is written or the call fails and nothing is written.</p>

        Args:
            test_id: <p>The identifier of the test to add sources to.</p>
            service_arn: <p>The ARN of the service the test belongs to.</p>
            test_sources: <p>The monitoring sources to add or update.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.put_test_sources_request.PutTestSourcesRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.put_test_sources_response.PutTestSourcesResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.put_test_sources

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.put_test_sources.put_test_sources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.put_test_sources_request.PutTestSourcesRequest = {
            "test_id": test_id,
            "service_arn": service_arn,
            "test_sources": test_sources,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_dependency_insights(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.start_dependency_insights_response.StartDependencyInsightsResponse":
        """<p>Starts generating dependency insights for a service. Generation runs asynchronously; the response returns the initial status, and you retrieve the results with GetDependencyInsights. To use this operation, you must have the <code>resiliencehub:StartDependencyInsights</code> permission on the service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.start_dependency_insights_request.StartDependencyInsightsRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.start_dependency_insights_response.StartDependencyInsightsResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.start_dependency_insights

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.start_dependency_insights.start_dependency_insights(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.start_dependency_insights_request.StartDependencyInsightsRequest = {
            "service_arn": service_arn
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

    def start_failure_mode_assessment(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        client_token: Optional[
            "capo_resiliencehubv2.types.client_token.ClientToken"
        ] = None,
    ) -> "capo_resiliencehubv2.types.start_failure_mode_assessment_response.StartFailureModeAssessmentResponse":
        """<p>Starts a failure mode assessment.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.start_failure_mode_assessment_request.StartFailureModeAssessmentRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.start_failure_mode_assessment_response.StartFailureModeAssessmentResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.start_failure_mode_assessment

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.start_failure_mode_assessment.start_failure_mode_assessment(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.start_failure_mode_assessment_request.StartFailureModeAssessmentRequest = {
            "service_arn": service_arn
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

    def start_test_run(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.start_test_run_response.StartTestRunResponse":
        """<p>Starts a run of a test. Each run scopes to the current resources in the service and produces a pass or fail outcome.</p>

        Args:
            test_id: <p>The identifier of the test to run.</p>
            service_arn: <p>The ARN of the service the test belongs to.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.start_test_run_request.StartTestRunRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.start_test_run_response.StartTestRunResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.start_test_run

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.start_test_run.start_test_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.start_test_run_request.StartTestRunRequest = {
            "test_id": test_id,
            "service_arn": service_arn,
        }

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_test_run(
        self,
        test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.stop_test_run_response.StopTestRunResponse":
        """<p>Stops an in-progress test run.</p>

        Args:
            test_run_id: <p>The identifier of the test run to stop.</p>
            service_arn: <p>The ARN of the service the test run belongs to.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.stop_test_run_request.StopTestRunRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.stop_test_run_response.StopTestRunResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.stop_test_run

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.stop_test_run.stop_test_run(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.stop_test_run_request.StopTestRunRequest = {
            "test_run_id": test_run_id,
            "service_arn": service_arn,
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
        resource_arn: "capo_resiliencehubv2.types.arn.Arn",
        tags: "capo_resiliencehubv2.types.tag_map.TagMap",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.tag_resource_response.TagResourceResponse":
        """<p>Adds tags to a resource.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.tag_resource_request.TagResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.tag_resource_response.TagResourceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.tag_resource

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.tag_resource.tag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.tag_resource_request.TagResourceRequest = {
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
        resource_arn: "capo_resiliencehubv2.types.arn.Arn",
        tag_keys: "capo_resiliencehubv2.types.tag_key_list.TagKeyList",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
    ) -> "capo_resiliencehubv2.types.untag_resource_response.UntagResourceResponse":
        """<p>Removes tags from a resource.</p>

        Args:
            tag_keys: <p>The tag keys to remove from the resource.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.throttling_exception.ThrottlingException: <p>Too many requests — rate limit exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.untag_resource_request.UntagResourceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.untag_resource_response.UntagResourceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.untag_resource

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.untag_resource.untag_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.untag_resource_request.UntagResourceRequest = {
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

    def update_assertion(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        assertion_id: "capo_resiliencehubv2.types.uuid.Uuid",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        text: Optional[
            "capo_resiliencehubv2.types.assertion_text.AssertionText"
        ] = None,
    ) -> "capo_resiliencehubv2.types.update_assertion_response.UpdateAssertionResponse":
        """<p>Updates a resilience assertion.</p>

        Args:
            assertion_id: <p>The unique identifier of the assertion to update.</p>
            text: <p>The updated text content of the assertion.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_assertion_request.UpdateAssertionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_assertion_response.UpdateAssertionResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_assertion

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_assertion.update_assertion(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_assertion_request.UpdateAssertionRequest = {
            "service_arn": service_arn,
            "assertion_id": assertion_id,
        }
        if text is not None:
            input_["text"] = text

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_dependency(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        dependency_id: "capo_resiliencehubv2.types.uuid.Uuid",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        criticality: Optional[
            "capo_resiliencehubv2.types.dependency_criticality.DependencyCriticality"
        ] = None,
        comment: Optional[str] = None,
    ) -> (
        "capo_resiliencehubv2.types.update_dependency_response.UpdateDependencyResponse"
    ):
        """<p>Updates a dependency classification.</p>

        Args:
            dependency_id: <p>The identifier of the dependency to update.</p>
            criticality: <p>The updated criticality level of the dependency.</p>
            comment: <p>A comment about the dependency.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_dependency_request.UpdateDependencyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_dependency_response.UpdateDependencyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_dependency

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_dependency.update_dependency(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_dependency_request.UpdateDependencyRequest = {
            "service_arn": service_arn,
            "dependency_id": dependency_id,
        }
        if criticality is not None:
            input_["criticality"] = criticality
        if comment is not None:
            input_["comment"] = comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_failure_mode_finding(
        self,
        finding_id: "capo_resiliencehubv2.types.uuid.Uuid",
        status: "capo_resiliencehubv2.types.finding_status.FindingStatus",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        comment: Optional[str] = None,
    ) -> "capo_resiliencehubv2.types.update_failure_mode_finding_response.UpdateFailureModeFindingResponse":
        """<p>Updates an existing finding.</p>

        Args:
            finding_id: <p>The identifier of the finding to update.</p>
            status: <p>The new status for the finding.</p>
            comment: <p>A comment about the finding update.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_failure_mode_finding_request.UpdateFailureModeFindingRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_failure_mode_finding_response.UpdateFailureModeFindingResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_failure_mode_finding

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_failure_mode_finding.update_failure_mode_finding(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_failure_mode_finding_request.UpdateFailureModeFindingRequest = {
            "finding_id": finding_id,
            "status": status,
            "service_arn": service_arn,
        }
        if comment is not None:
            input_["comment"] = comment

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_policy(
        self,
        policy_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        availability_slo: Optional[
            "capo_resiliencehubv2.types.availability_slo.AvailabilitySlo"
        ] = None,
        multi_az: Optional[
            "capo_resiliencehubv2.types.multi_az_targets.MultiAzTargets"
        ] = None,
        multi_region: Optional[
            "capo_resiliencehubv2.types.multi_region_targets.MultiRegionTargets"
        ] = None,
        data_recovery: Optional[
            "capo_resiliencehubv2.types.data_recovery_targets.DataRecoveryTargets"
        ] = None,
        sharing_enabled: Optional[bool] = None,
    ) -> "capo_resiliencehubv2.types.update_policy_response.UpdatePolicyResponse":
        """<p>Updates an existing resilience policy.</p>

        Args:
            availability_slo: <p>The updated availability SLO for the policy.</p>
            multi_az: <p>The updated multi-AZ disaster recovery targets for the policy.</p>
            multi_region: <p>The updated multi-Region disaster recovery targets for the policy.</p>
            data_recovery: <p>The updated data recovery targets for the policy.</p>
            sharing_enabled: <p>Specifies whether cross-account sharing is enabled for the policy. Disabling sharing stops member services from using the policy.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_policy_request.UpdatePolicyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_policy_response.UpdatePolicyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_policy

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_policy.update_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_policy_request.UpdatePolicyRequest = {
            "policy_arn": policy_arn
        }
        if description is not None:
            input_["description"] = description
        if availability_slo is not None:
            input_["availability_slo"] = availability_slo
        if multi_az is not None:
            input_["multi_az"] = multi_az
        if multi_region is not None:
            input_["multi_region"] = multi_region
        if data_recovery is not None:
            input_["data_recovery"] = data_recovery
        if sharing_enabled is not None:
            input_["sharing_enabled"] = sharing_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.long_description.LongDescription"
        ] = None,
        associated_systems: Optional[
            "capo_resiliencehubv2.types.associated_system_list.AssociatedSystemList"
        ] = None,
        policy_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
        regions: Optional["capo_resiliencehubv2.types.region_list.RegionList"] = None,
        permission_model: Optional[
            "capo_resiliencehubv2.types.permission_model.PermissionModel"
        ] = None,
        dependency_discovery: Optional[
            "capo_resiliencehubv2.types.dependency_discovery_input.DependencyDiscoveryInput"
        ] = None,
        report_configuration: Optional[
            "capo_resiliencehubv2.types.service_report_configuration.ServiceReportConfiguration"
        ] = None,
    ) -> "capo_resiliencehubv2.types.update_service_response.UpdateServiceResponse":
        """<p>Updates an existing service.</p>

        Args:
            associated_systems: <p>The updated systems to associate with the service.</p>
            regions: <p>The updated AWS Regions where the service operates.</p>
            permission_model: <p>The updated permission model for the service.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.service_quota_exceeded_exception.ServiceQuotaExceededException: <p>Service quota exceeded.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_service_request.UpdateServiceRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_service_response.UpdateServiceResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_service

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_service.update_service(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_service_request.UpdateServiceRequest = {
            "service_arn": service_arn
        }
        if description is not None:
            input_["description"] = description
        if associated_systems is not None:
            input_["associated_systems"] = associated_systems
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn
        if regions is not None:
            input_["regions"] = regions
        if permission_model is not None:
            input_["permission_model"] = permission_model
        if dependency_discovery is not None:
            input_["dependency_discovery"] = dependency_discovery
        if report_configuration is not None:
            input_["report_configuration"] = report_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_service_function(
        self,
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        service_function_id: "capo_resiliencehubv2.types.entity_id.EntityId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        name: Optional["capo_resiliencehubv2.types.entity_label.EntityLabel"] = None,
        description: Optional[
            "capo_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        criticality: Optional[
            "capo_resiliencehubv2.types.service_function_criticality.ServiceFunctionCriticality"
        ] = None,
    ) -> "capo_resiliencehubv2.types.update_service_function_response.UpdateServiceFunctionResponse":
        """<p>Updates a service function.</p>

        Args:
            service_function_id: <p>The identifier of the service function to update.</p>
            criticality: <p>The updated criticality level of the service function.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_service_function_request.UpdateServiceFunctionRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_service_function_response.UpdateServiceFunctionResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_service_function

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_service_function.update_service_function(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_service_function_request.UpdateServiceFunctionRequest = {
            "service_arn": service_arn,
            "service_function_id": service_function_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if criticality is not None:
            input_["criticality"] = criticality

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_system(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        description: Optional[
            "capo_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        sharing_enabled: Optional[bool] = None,
    ) -> "capo_resiliencehubv2.types.update_system_response.UpdateSystemResponse":
        """<p>Updates an existing system.</p>

        Args:
            sharing_enabled: <p>Whether cross-account sharing is enabled for the system.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_system_request.UpdateSystemRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_system_response.UpdateSystemResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_system

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_system.update_system(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_system_request.UpdateSystemRequest = {
            "system_arn": system_arn
        }
        if description is not None:
            input_["description"] = description
        if sharing_enabled is not None:
            input_["sharing_enabled"] = sharing_enabled

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_test(
        self,
        test_id: "capo_resiliencehubv2.types.test_id.TestId",
        service_arn: "capo_resiliencehubv2.types.arn.Arn",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        logging_configuration: Optional[
            "capo_resiliencehubv2.types.logging_configuration.LoggingConfiguration"
        ] = None,
        stop_conditions: Optional[
            "capo_resiliencehubv2.types.stop_condition_list.StopConditionList"
        ] = None,
        role_name: Optional[
            "capo_resiliencehubv2.types.iam_role_name.IamRoleName"
        ] = None,
        parameters: Optional[
            "capo_resiliencehubv2.types.test_parameters.TestParameters"
        ] = None,
    ) -> "capo_resiliencehubv2.types.update_test_response.UpdateTestResponse":
        """<p>Updates the configuration of an existing test.</p>

        Args:
            test_id: <p>The identifier of the test to update.</p>
            service_arn: <p>The ARN of the service the test belongs to.</p>
            logging_configuration: <p>The updated logging configuration for the test.</p>
            stop_conditions: <p>The updated stop conditions for the test.</p>
            role_name: <p>The updated IAM execution role name.</p>
            parameters: <p>The updated parameter values for the test.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_test_request.UpdateTestRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_test_response.UpdateTestResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_test

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_test.update_test(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_test_request.UpdateTestRequest = {
            "test_id": test_id,
            "service_arn": service_arn,
        }
        if logging_configuration is not None:
            input_["logging_configuration"] = logging_configuration
        if stop_conditions is not None:
            input_["stop_conditions"] = stop_conditions
        if role_name is not None:
            input_["role_name"] = role_name
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_user_journey(
        self,
        system_arn: "capo_resiliencehubv2.types.arn.Arn",
        user_journey_id: "capo_resiliencehubv2.types.user_journey_id.UserJourneyId",
        *,
        config_overrides: Optional[resiliencehubv2ClientConfig] = None,
        name: Optional["capo_resiliencehubv2.types.entity_label.EntityLabel"] = None,
        description: Optional[
            "capo_resiliencehubv2.types.entity_description.EntityDescription"
        ] = None,
        policy_arn: Optional["capo_resiliencehubv2.types.arn.Arn"] = None,
    ) -> "capo_resiliencehubv2.types.update_user_journey_response.UpdateUserJourneyResponse":
        """<p>Updates an existing user journey.</p>

        Args:
            user_journey_id: <p>The identifier of the user journey to update.</p>

        Raises:
            capo_resiliencehubv2.errors.access_denied_exception.AccessDeniedException: <p>Access denied — caller lacks required permissions.</p>
            capo_resiliencehubv2.errors.conflict_exception.ConflictException: <p>Conflict — resource already exists.</p>
            capo_resiliencehubv2.errors.internal_server_exception.InternalServerException: <p>Internal service error.</p>
            capo_resiliencehubv2.errors.resource_not_found_exception.ResourceNotFoundException: <p>Resource not found.</p>
            capo_resiliencehubv2.errors.validation_exception.ValidationException: <p>Validation error — invalid input parameters.</p>
            capo_resiliencehubv2.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_resiliencehubv2.types.update_user_journey_request.UpdateUserJourneyRequest]",
        ) -> OperationResponse[
            "capo_resiliencehubv2.types.update_user_journey_response.UpdateUserJourneyResponse"
        ]:
            import capo_resiliencehubv2._operations.ngrh_service_core.update_user_journey

            output, http_response = (
                capo_resiliencehubv2._operations.ngrh_service_core.update_user_journey.update_user_journey(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_resiliencehubv2.types.update_user_journey_request.UpdateUserJourneyRequest = {
            "system_arn": system_arn,
            "user_journey_id": user_journey_id,
        }
        if name is not None:
            input_["name"] = name
        if description is not None:
            input_["description"] = description
        if policy_arn is not None:
            input_["policy_arn"] = policy_arn

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
