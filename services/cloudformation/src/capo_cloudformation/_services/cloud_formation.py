"""Generated from Smithy shape ``com.amazonaws.cloudformation#CloudFormation``."""

import time
import uuid
import warnings
from collections.abc import Iterator
from typing import TYPE_CHECKING, Any, Iterable, Optional

from typing_extensions import Self, TypedDict
from zapros import BaseHandler, Client

import capo_cloudformation._auth._signers
import capo_cloudformation._auth._sigv4
from capo_cloudformation._auth._identity import Credentials
from capo_cloudformation._auth._providers import (
    CredentialsProvider,
    IdentityProvider,
    StaticAwsCredentialsProvider,
    default_aws_credentials_chain,
)
from capo_cloudformation._auth._zapros_handler import AuthMiddleware
from capo_cloudformation._pagination import resolve_path as _resolve_path
from capo_cloudformation._services._aws_config import aws_config
from capo_cloudformation._services._pipeline import (
    Interceptor,
    OperationOptions,
    OperationRequest,
    OperationResponse,
    execute_pipeline,
    retry,
)
from capo_cloudformation.errors import (
    ServiceError,
    WaiterTimeoutError,
)

if TYPE_CHECKING:
    import capo_cloudformation.types.accept_terms_and_conditions
    import capo_cloudformation.types.account
    import capo_cloudformation.types.account_limit
    import capo_cloudformation.types.account_list
    import capo_cloudformation.types.activate_organizations_access_input
    import capo_cloudformation.types.activate_organizations_access_output
    import capo_cloudformation.types.activate_type_input
    import capo_cloudformation.types.activate_type_output
    import capo_cloudformation.types.auto_deployment
    import capo_cloudformation.types.auto_update
    import capo_cloudformation.types.batch_describe_type_configurations_input
    import capo_cloudformation.types.batch_describe_type_configurations_output
    import capo_cloudformation.types.boxed_max_results
    import capo_cloudformation.types.call_as
    import capo_cloudformation.types.cancel_update_stack_input
    import capo_cloudformation.types.capabilities
    import capo_cloudformation.types.change
    import capo_cloudformation.types.change_set_name
    import capo_cloudformation.types.change_set_name_or_id
    import capo_cloudformation.types.change_set_summary
    import capo_cloudformation.types.change_set_type
    import capo_cloudformation.types.client_request_token
    import capo_cloudformation.types.client_token
    import capo_cloudformation.types.connection_arn
    import capo_cloudformation.types.continue_update_rollback_input
    import capo_cloudformation.types.continue_update_rollback_output
    import capo_cloudformation.types.create_change_set_input
    import capo_cloudformation.types.create_change_set_output
    import capo_cloudformation.types.create_generated_template_input
    import capo_cloudformation.types.create_generated_template_output
    import capo_cloudformation.types.create_stack_input
    import capo_cloudformation.types.create_stack_instances_input
    import capo_cloudformation.types.create_stack_instances_output
    import capo_cloudformation.types.create_stack_output
    import capo_cloudformation.types.create_stack_refactor_input
    import capo_cloudformation.types.create_stack_refactor_output
    import capo_cloudformation.types.create_stack_set_input
    import capo_cloudformation.types.create_stack_set_output
    import capo_cloudformation.types.deactivate_organizations_access_input
    import capo_cloudformation.types.deactivate_organizations_access_output
    import capo_cloudformation.types.deactivate_type_input
    import capo_cloudformation.types.deactivate_type_output
    import capo_cloudformation.types.delete_change_set_input
    import capo_cloudformation.types.delete_change_set_output
    import capo_cloudformation.types.delete_generated_template_input
    import capo_cloudformation.types.delete_stack_input
    import capo_cloudformation.types.delete_stack_instances_input
    import capo_cloudformation.types.delete_stack_instances_output
    import capo_cloudformation.types.delete_stack_set_input
    import capo_cloudformation.types.delete_stack_set_output
    import capo_cloudformation.types.deletion_mode
    import capo_cloudformation.types.deployment_config
    import capo_cloudformation.types.deployment_mode
    import capo_cloudformation.types.deployment_targets
    import capo_cloudformation.types.deprecated_status
    import capo_cloudformation.types.deregister_type_input
    import capo_cloudformation.types.deregister_type_output
    import capo_cloudformation.types.describe_account_limits_input
    import capo_cloudformation.types.describe_account_limits_output
    import capo_cloudformation.types.describe_change_set_hooks_input
    import capo_cloudformation.types.describe_change_set_hooks_output
    import capo_cloudformation.types.describe_change_set_input
    import capo_cloudformation.types.describe_change_set_output
    import capo_cloudformation.types.describe_events_input
    import capo_cloudformation.types.describe_events_output
    import capo_cloudformation.types.describe_generated_template_input
    import capo_cloudformation.types.describe_generated_template_output
    import capo_cloudformation.types.describe_organizations_access_input
    import capo_cloudformation.types.describe_organizations_access_output
    import capo_cloudformation.types.describe_publisher_input
    import capo_cloudformation.types.describe_publisher_output
    import capo_cloudformation.types.describe_resource_scan_input
    import capo_cloudformation.types.describe_resource_scan_output
    import capo_cloudformation.types.describe_stack_drift_detection_status_input
    import capo_cloudformation.types.describe_stack_drift_detection_status_output
    import capo_cloudformation.types.describe_stack_events_input
    import capo_cloudformation.types.describe_stack_events_output
    import capo_cloudformation.types.describe_stack_instance_input
    import capo_cloudformation.types.describe_stack_instance_output
    import capo_cloudformation.types.describe_stack_refactor_input
    import capo_cloudformation.types.describe_stack_refactor_output
    import capo_cloudformation.types.describe_stack_resource_drifts_input
    import capo_cloudformation.types.describe_stack_resource_drifts_output
    import capo_cloudformation.types.describe_stack_resource_input
    import capo_cloudformation.types.describe_stack_resource_output
    import capo_cloudformation.types.describe_stack_resources_input
    import capo_cloudformation.types.describe_stack_resources_output
    import capo_cloudformation.types.describe_stack_set_input
    import capo_cloudformation.types.describe_stack_set_operation_input
    import capo_cloudformation.types.describe_stack_set_operation_output
    import capo_cloudformation.types.describe_stack_set_output
    import capo_cloudformation.types.describe_stacks_input
    import capo_cloudformation.types.describe_stacks_output
    import capo_cloudformation.types.describe_type_input
    import capo_cloudformation.types.describe_type_output
    import capo_cloudformation.types.describe_type_registration_input
    import capo_cloudformation.types.describe_type_registration_output
    import capo_cloudformation.types.description
    import capo_cloudformation.types.detect_stack_drift_input
    import capo_cloudformation.types.detect_stack_drift_output
    import capo_cloudformation.types.detect_stack_resource_drift_input
    import capo_cloudformation.types.detect_stack_resource_drift_output
    import capo_cloudformation.types.detect_stack_set_drift_input
    import capo_cloudformation.types.detect_stack_set_drift_output
    import capo_cloudformation.types.disable_rollback
    import capo_cloudformation.types.disable_validation
    import capo_cloudformation.types.enable_stack_creation
    import capo_cloudformation.types.enable_termination_protection
    import capo_cloudformation.types.estimate_template_cost_input
    import capo_cloudformation.types.estimate_template_cost_output
    import capo_cloudformation.types.event_filter
    import capo_cloudformation.types.execute_change_set_input
    import capo_cloudformation.types.execute_change_set_output
    import capo_cloudformation.types.execute_stack_refactor_input
    import capo_cloudformation.types.execution_role_name
    import capo_cloudformation.types.export
    import capo_cloudformation.types.export_name
    import capo_cloudformation.types.generated_template_name
    import capo_cloudformation.types.get_generated_template_input
    import capo_cloudformation.types.get_generated_template_output
    import capo_cloudformation.types.get_hook_result_input
    import capo_cloudformation.types.get_hook_result_output
    import capo_cloudformation.types.get_stack_policy_input
    import capo_cloudformation.types.get_stack_policy_output
    import capo_cloudformation.types.get_template_input
    import capo_cloudformation.types.get_template_output
    import capo_cloudformation.types.get_template_summary_input
    import capo_cloudformation.types.get_template_summary_output
    import capo_cloudformation.types.handler_error_code
    import capo_cloudformation.types.hook_invocation_id
    import capo_cloudformation.types.hook_result_id
    import capo_cloudformation.types.hook_status
    import capo_cloudformation.types.hook_type_arn
    import capo_cloudformation.types.import_existing_resources
    import capo_cloudformation.types.import_stacks_to_stack_set_input
    import capo_cloudformation.types.import_stacks_to_stack_set_output
    import capo_cloudformation.types.include_nested_stacks
    import capo_cloudformation.types.include_property_values
    import capo_cloudformation.types.jazz_logical_resource_ids
    import capo_cloudformation.types.list_change_sets_input
    import capo_cloudformation.types.list_change_sets_output
    import capo_cloudformation.types.list_exports_input
    import capo_cloudformation.types.list_exports_output
    import capo_cloudformation.types.list_generated_templates_input
    import capo_cloudformation.types.list_generated_templates_output
    import capo_cloudformation.types.list_hook_results_input
    import capo_cloudformation.types.list_hook_results_output
    import capo_cloudformation.types.list_hook_results_target_type
    import capo_cloudformation.types.list_imports_input
    import capo_cloudformation.types.list_imports_output
    import capo_cloudformation.types.list_resource_scan_related_resources_input
    import capo_cloudformation.types.list_resource_scan_related_resources_output
    import capo_cloudformation.types.list_resource_scan_resources_input
    import capo_cloudformation.types.list_resource_scan_resources_output
    import capo_cloudformation.types.list_resource_scans_input
    import capo_cloudformation.types.list_resource_scans_output
    import capo_cloudformation.types.list_stack_instance_resource_drifts_input
    import capo_cloudformation.types.list_stack_instance_resource_drifts_output
    import capo_cloudformation.types.list_stack_instances_input
    import capo_cloudformation.types.list_stack_instances_output
    import capo_cloudformation.types.list_stack_refactor_actions_input
    import capo_cloudformation.types.list_stack_refactor_actions_output
    import capo_cloudformation.types.list_stack_refactors_input
    import capo_cloudformation.types.list_stack_refactors_output
    import capo_cloudformation.types.list_stack_resources_input
    import capo_cloudformation.types.list_stack_resources_output
    import capo_cloudformation.types.list_stack_set_auto_deployment_targets_input
    import capo_cloudformation.types.list_stack_set_auto_deployment_targets_output
    import capo_cloudformation.types.list_stack_set_operation_results_input
    import capo_cloudformation.types.list_stack_set_operation_results_output
    import capo_cloudformation.types.list_stack_set_operations_input
    import capo_cloudformation.types.list_stack_set_operations_output
    import capo_cloudformation.types.list_stack_sets_input
    import capo_cloudformation.types.list_stack_sets_output
    import capo_cloudformation.types.list_stacks_input
    import capo_cloudformation.types.list_stacks_output
    import capo_cloudformation.types.list_type_registrations_input
    import capo_cloudformation.types.list_type_registrations_output
    import capo_cloudformation.types.list_type_versions_input
    import capo_cloudformation.types.list_type_versions_output
    import capo_cloudformation.types.list_types_input
    import capo_cloudformation.types.list_types_output
    import capo_cloudformation.types.logging_config
    import capo_cloudformation.types.logical_resource_id
    import capo_cloudformation.types.logical_resource_ids
    import capo_cloudformation.types.major_version
    import capo_cloudformation.types.managed_execution
    import capo_cloudformation.types.max_results
    import capo_cloudformation.types.next_token
    import capo_cloudformation.types.notification_ar_ns
    import capo_cloudformation.types.on_failure
    import capo_cloudformation.types.on_stack_failure
    import capo_cloudformation.types.operation_event
    import capo_cloudformation.types.operation_id
    import capo_cloudformation.types.operation_result_filters
    import capo_cloudformation.types.operation_status
    import capo_cloudformation.types.organizational_unit_id_list
    import capo_cloudformation.types.parameters
    import capo_cloudformation.types.permission_models
    import capo_cloudformation.types.physical_resource_id
    import capo_cloudformation.types.private_type_arn
    import capo_cloudformation.types.provisioning_type
    import capo_cloudformation.types.public_version_number
    import capo_cloudformation.types.publish_type_input
    import capo_cloudformation.types.publish_type_output
    import capo_cloudformation.types.publisher_id
    import capo_cloudformation.types.record_handler_progress_input
    import capo_cloudformation.types.record_handler_progress_output
    import capo_cloudformation.types.refresh_all_resources
    import capo_cloudformation.types.region
    import capo_cloudformation.types.region_list
    import capo_cloudformation.types.register_publisher_input
    import capo_cloudformation.types.register_publisher_output
    import capo_cloudformation.types.register_type_input
    import capo_cloudformation.types.register_type_output
    import capo_cloudformation.types.registration_status
    import capo_cloudformation.types.registration_token
    import capo_cloudformation.types.registry_type
    import capo_cloudformation.types.request_token
    import capo_cloudformation.types.resource_definitions
    import capo_cloudformation.types.resource_identifier
    import capo_cloudformation.types.resource_mappings
    import capo_cloudformation.types.resource_model
    import capo_cloudformation.types.resource_scan_id
    import capo_cloudformation.types.resource_scan_summary
    import capo_cloudformation.types.resource_scanner_max_results
    import capo_cloudformation.types.resource_signal_status
    import capo_cloudformation.types.resource_signal_unique_id
    import capo_cloudformation.types.resource_type_prefix
    import capo_cloudformation.types.resource_types
    import capo_cloudformation.types.resources_to_import
    import capo_cloudformation.types.resources_to_skip
    import capo_cloudformation.types.retain_except_on_create
    import capo_cloudformation.types.retain_resources
    import capo_cloudformation.types.retain_stacks
    import capo_cloudformation.types.role_arn
    import capo_cloudformation.types.role_arn2
    import capo_cloudformation.types.rollback_configuration
    import capo_cloudformation.types.rollback_stack_input
    import capo_cloudformation.types.rollback_stack_output
    import capo_cloudformation.types.s3_bucket
    import capo_cloudformation.types.s3_url
    import capo_cloudformation.types.scan_filters
    import capo_cloudformation.types.scan_type
    import capo_cloudformation.types.scanned_resource
    import capo_cloudformation.types.scanned_resource_identifiers
    import capo_cloudformation.types.set_stack_policy_input
    import capo_cloudformation.types.set_type_configuration_input
    import capo_cloudformation.types.set_type_configuration_output
    import capo_cloudformation.types.set_type_default_version_input
    import capo_cloudformation.types.set_type_default_version_output
    import capo_cloudformation.types.signal_resource_input
    import capo_cloudformation.types.stack
    import capo_cloudformation.types.stack_definitions
    import capo_cloudformation.types.stack_drift_detection_id
    import capo_cloudformation.types.stack_event
    import capo_cloudformation.types.stack_id
    import capo_cloudformation.types.stack_id_list
    import capo_cloudformation.types.stack_ids_url
    import capo_cloudformation.types.stack_instance_filters
    import capo_cloudformation.types.stack_instance_summary
    import capo_cloudformation.types.stack_name
    import capo_cloudformation.types.stack_name_or_id
    import capo_cloudformation.types.stack_policy_body
    import capo_cloudformation.types.stack_policy_during_update_body
    import capo_cloudformation.types.stack_policy_during_update_url
    import capo_cloudformation.types.stack_policy_url
    import capo_cloudformation.types.stack_refactor_action
    import capo_cloudformation.types.stack_refactor_execution_status_filter
    import capo_cloudformation.types.stack_refactor_id
    import capo_cloudformation.types.stack_refactor_summary
    import capo_cloudformation.types.stack_resource_drift_status_filters
    import capo_cloudformation.types.stack_resource_summary
    import capo_cloudformation.types.stack_set_name
    import capo_cloudformation.types.stack_set_name_or_id
    import capo_cloudformation.types.stack_set_operation_preferences
    import capo_cloudformation.types.stack_set_operation_result_summary
    import capo_cloudformation.types.stack_set_operation_summary
    import capo_cloudformation.types.stack_set_status
    import capo_cloudformation.types.stack_set_summary
    import capo_cloudformation.types.stack_status_filter
    import capo_cloudformation.types.stack_summary
    import capo_cloudformation.types.start_resource_scan_input
    import capo_cloudformation.types.start_resource_scan_output
    import capo_cloudformation.types.status_message
    import capo_cloudformation.types.stop_stack_set_operation_input
    import capo_cloudformation.types.stop_stack_set_operation_output
    import capo_cloudformation.types.tag_key
    import capo_cloudformation.types.tag_value
    import capo_cloudformation.types.tags
    import capo_cloudformation.types.template_body
    import capo_cloudformation.types.template_configuration
    import capo_cloudformation.types.template_format
    import capo_cloudformation.types.template_stage
    import capo_cloudformation.types.template_summary
    import capo_cloudformation.types.template_summary_config
    import capo_cloudformation.types.template_url
    import capo_cloudformation.types.test_type_input
    import capo_cloudformation.types.test_type_output
    import capo_cloudformation.types.third_party_type
    import capo_cloudformation.types.third_party_type_arn
    import capo_cloudformation.types.timeout_minutes
    import capo_cloudformation.types.type_arn
    import capo_cloudformation.types.type_configuration
    import capo_cloudformation.types.type_configuration_alias
    import capo_cloudformation.types.type_configuration_identifiers
    import capo_cloudformation.types.type_filters
    import capo_cloudformation.types.type_name
    import capo_cloudformation.types.type_summary
    import capo_cloudformation.types.type_version_id
    import capo_cloudformation.types.update_generated_template_input
    import capo_cloudformation.types.update_generated_template_output
    import capo_cloudformation.types.update_stack_input
    import capo_cloudformation.types.update_stack_instances_input
    import capo_cloudformation.types.update_stack_instances_output
    import capo_cloudformation.types.update_stack_output
    import capo_cloudformation.types.update_stack_set_input
    import capo_cloudformation.types.update_stack_set_output
    import capo_cloudformation.types.update_termination_protection_input
    import capo_cloudformation.types.update_termination_protection_output
    import capo_cloudformation.types.use_previous_template
    import capo_cloudformation.types.validate_template_input
    import capo_cloudformation.types.validate_template_output
    import capo_cloudformation.types.version_bump
    import capo_cloudformation.types.visibility


class CloudFormationClientConfig(TypedDict, total=False, closed=True):
    operation_interceptors: Iterable[Interceptor[Any, Any]]
    retry_max_attempts: int | None
    region: str | None
    use_dual_stack: bool | None
    use_fips: bool | None
    endpoint: str | None
    credentials_provider: IdentityProvider[Credentials] | None


class CloudFormationClient:
    """A client for the ``CloudFormation`` service.

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
        self._config = CloudFormationClientConfig(
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
        self, config_overrides: Optional[CloudFormationClientConfig] = None
    ) -> tuple[Iterable[Interceptor[Any, Any]], OperationOptions]:
        overrides: CloudFormationClientConfig = config_overrides or {}
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

    def activate_organizations_access(
        self, *, config_overrides: Optional[CloudFormationClientConfig] = None
    ) -> "capo_cloudformation.types.activate_organizations_access_output.ActivateOrganizationsAccessOutput":
        """<p>Activate trusted access with Organizations. With trusted access between StackSets and Organizations activated, the management account has permissions to create and manage StackSets for your organization.</p>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_not_found_exception.OperationNotFoundException: <p>The specified ID refers to an operation that doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.activate_organizations_access_input.ActivateOrganizationsAccessInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.activate_organizations_access_output.ActivateOrganizationsAccessOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.activate_organizations_access

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.activate_organizations_access.activate_organizations_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.activate_organizations_access_input.ActivateOrganizationsAccessInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def activate_type(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional[
            "capo_cloudformation.types.third_party_type.ThirdPartyType"
        ] = None,
        public_type_arn: Optional[
            "capo_cloudformation.types.third_party_type_arn.ThirdPartyTypeArn"
        ] = None,
        publisher_id: Optional[
            "capo_cloudformation.types.publisher_id.PublisherId"
        ] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        type_name_alias: Optional[
            "capo_cloudformation.types.type_name.TypeName"
        ] = None,
        auto_update: Optional[
            "capo_cloudformation.types.auto_update.AutoUpdate"
        ] = None,
        logging_config: Optional[
            "capo_cloudformation.types.logging_config.LoggingConfig"
        ] = None,
        execution_role_arn: Optional[
            "capo_cloudformation.types.role_arn2.RoleARN2"
        ] = None,
        version_bump: Optional[
            "capo_cloudformation.types.version_bump.VersionBump"
        ] = None,
        major_version: Optional[
            "capo_cloudformation.types.major_version.MajorVersion"
        ] = None,
    ) -> "capo_cloudformation.types.activate_type_output.ActivateTypeOutput":
        """<p>Activates a public third-party extension, such as a resource or module, to make it available for use in stack templates in your current account and Region. It can also create CloudFormation Hooks, which allow you to evaluate resource configurations before CloudFormation provisions them. Hooks integrate with both CloudFormation and Cloud Control API operations.</p> <p>After you activate an extension, you can use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to set specific properties for the extension.</p> <p>To see which extensions have been activated, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListTypes.html">ListTypes</a>. To see configuration details for an extension, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public-activate-extension.html">Activate a third-party public extension in your account</a> in the <i>CloudFormation User Guide</i>. For information about creating Hooks, see the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html">CloudFormation Hooks User Guide</a>.</p>

        Args:
            type: <p>The extension type.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
            public_type_arn: <p>The Amazon Resource Name (ARN) of the public extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
            publisher_id: <p>The ID of the extension publisher.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
            type_name: <p>The name of the extension.</p> <p>Conditional: You must specify <code>PublicTypeArn</code>, or <code>TypeName</code>, <code>Type</code>, and <code>PublisherId</code>.</p>
            type_name_alias: <p>An alias to assign to the public extension in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.</p> <p>An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.</p>
            auto_update: <p>Whether to automatically update the extension in this account and Region when a new <i>minor</i> version is published by the extension publisher. Major versions released by the publisher must be manually updated.</p> <p>The default is <code>true</code>.</p>
            logging_config: <p>Contains logging configuration information for an extension.</p>
            execution_role_arn: <p>The name of the IAM execution role to use to activate the extension.</p>
            version_bump: <p>Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of <code>AutoUpdate</code>.</p> <ul> <li> <p> <code>MAJOR</code>: CloudFormation updates the extension to the newest major version, if one is available.</p> </li> <li> <p> <code>MINOR</code>: CloudFormation updates the extension to the newest minor version, if one is available.</p> </li> </ul>
            major_version: <p>The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available <i>minor</i> version of the major version selected.</p> <p>You can specify <code>MajorVersion</code> or <code>VersionBump</code>, but not both.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.activate_type_input.ActivateTypeInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.activate_type_output.ActivateTypeOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.activate_type

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.activate_type.activate_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.activate_type_input.ActivateTypeInput = {}
        if type is not None:
            input_["type"] = type
        if public_type_arn is not None:
            input_["public_type_arn"] = public_type_arn
        if publisher_id is not None:
            input_["publisher_id"] = publisher_id
        if type_name is not None:
            input_["type_name"] = type_name
        if type_name_alias is not None:
            input_["type_name_alias"] = type_name_alias
        if auto_update is not None:
            input_["auto_update"] = auto_update
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if version_bump is not None:
            input_["version_bump"] = version_bump
        if major_version is not None:
            input_["major_version"] = major_version

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def batch_describe_type_configurations(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type_configuration_identifiers: Optional[
            "capo_cloudformation.types.type_configuration_identifiers.TypeConfigurationIdentifiers"
        ] = None,
    ) -> "capo_cloudformation.types.batch_describe_type_configurations_output.BatchDescribeTypeConfigurationsOutput":
        """<p>Returns configuration data for the specified CloudFormation extensions, from the CloudFormation registry in your current account and Region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html">Edit configuration data for extensions in your account</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            type_configuration_identifiers: <p>The list of identifiers for the desired extension configurations.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_configuration_not_found_exception.TypeConfigurationNotFoundException: <p>The specified extension configuration can't be found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.batch_describe_type_configurations_input.BatchDescribeTypeConfigurationsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.batch_describe_type_configurations_output.BatchDescribeTypeConfigurationsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.batch_describe_type_configurations

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.batch_describe_type_configurations.batch_describe_type_configurations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.batch_describe_type_configurations_input.BatchDescribeTypeConfigurationsInput = {}
        if type_configuration_identifiers is not None:
            input_["type_configuration_identifiers"] = type_configuration_identifiers

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def cancel_update_stack(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> None:
        """<p>Cancels an update on the specified stack. If the call completes successfully, the stack rolls back the update and reverts to the previous stack configuration.</p> <note> <p>You can cancel only stacks that are in the <code>UPDATE_IN_PROGRESS</code> state.</p> </note>

        Args:
            stack_name: <note> <p>If you don't pass a parameter to <code>StackName</code>, the API returns a response that describes all resources in the account.</p> <p>The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:</p> <p> <code>{ "Version": "2012-10-17", "Statement": [{ "Effect": "Deny", "Action": "cloudformation:DescribeStacks", "NotResource": "arn:aws:cloudformation:*:*:stack/*/*" }] }</code> </p> </note> <p>The name or the unique stack ID that's associated with the stack.</p>
            client_request_token: <p>A unique identifier for this <code>CancelUpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to cancel an update on a stack with the same name. You might retry <code>CancelUpdateStack</code> requests to ensure that CloudFormation successfully received them.</p>

        Raises:
            capo_cloudformation.errors.token_already_exists_exception.TokenAlreadyExistsException: <p>A client request token already exists.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.cancel_update_stack_input.CancelUpdateStackInput]",
        ) -> OperationResponse[None]:
            import capo_cloudformation._operations.cloud_formation.cancel_update_stack

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.cancel_update_stack.cancel_update_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.cancel_update_stack_input.CancelUpdateStackInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def continue_update_rollback(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        role_arn: Optional["capo_cloudformation.types.role_arn.RoleARN"] = None,
        resources_to_skip: Optional[
            "capo_cloudformation.types.resources_to_skip.ResourcesToSkip"
        ] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_cloudformation.types.continue_update_rollback_output.ContinueUpdateRollbackOutput":
        """<p>Continues rolling back a stack from <code>UPDATE_ROLLBACK_FAILED</code> to <code>UPDATE_ROLLBACK_COMPLETE</code> state. Depending on the cause of the failure, you can manually fix the error and continue the rollback. By continuing the rollback, you can return your stack to a working state (the <code>UPDATE_ROLLBACK_COMPLETE</code> state) and then try to update the stack again.</p> <p>A stack enters the <code>UPDATE_ROLLBACK_FAILED</code> state when CloudFormation can't roll back all changes after a failed stack update. For example, this might occur when a stack attempts to roll back to an old database that was deleted outside of CloudFormation. Because CloudFormation doesn't know the instance was deleted, it assumes the instance still exists and attempts to roll back to it, causing the update rollback to fail.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html">Continue rolling back an update</a> in the <i>CloudFormation User Guide</i>. For information for troubleshooting a failed update rollback, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed">Update rollback failed</a>.</p>

        Args:
            stack_name: <p>The name or the unique ID of the stack that you want to continue rolling back.</p> <note> <p>Don't specify the name of a nested stack (a stack that was created by using the <code>AWS::CloudFormation::Stack</code> resource). Instead, use this operation on the parent stack (the stack that contains the <code>AWS::CloudFormation::Stack</code> resource).</p> </note>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to roll back the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>
            resources_to_skip: <p>A list of the logical IDs of the resources that CloudFormation skips during the continue update rollback operation. You can specify only resources that are in the <code>UPDATE_FAILED</code> state because a rollback failed. You can't specify resources that are in the <code>UPDATE_FAILED</code> state for other reasons, for example, because an update was canceled. To check why a resource update failed, use the <a>DescribeStackResources</a> action, and view the resource status reason.</p> <important> <p>Specify this property to skip rolling back resources that CloudFormation can't successfully roll back. We recommend that you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/troubleshooting.html#troubleshooting-errors-update-rollback-failed"> troubleshoot</a> resources before skipping them. CloudFormation sets the status of the specified resources to <code>UPDATE_COMPLETE</code> and continues to roll back the stack. After the rollback is complete, the state of the skipped resources will be inconsistent with the state of the resources in the stack template. Before performing another stack update, you must update the stack or resources to be consistent with each other. If you don't, subsequent stack updates might fail, and the stack will become unrecoverable.</p> </important> <p>Specify the minimum number of resources required to successfully roll back your stack. For example, a failed resource update might cause dependent resources to fail. In this case, it might not be necessary to skip the dependent resources.</p> <p>To skip resources that are part of nested stacks, use the following format: <code>NestedStackName.ResourceLogicalID</code>. If you want to specify the logical ID of a stack resource (<code>Type: AWS::CloudFormation::Stack</code>) in the <code>ResourcesToSkip</code> list, then its corresponding embedded stack must be in one of the following states: <code>DELETE_IN_PROGRESS</code>, <code>DELETE_COMPLETE</code>, or <code>DELETE_FAILED</code>.</p> <note> <p>Don't confuse a child stack's name with its corresponding logical ID defined in the parent stack. For an example of a continue update rollback operation with nested stacks, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-continueupdaterollback.html#nested-stacks">Continue rolling back from failed nested stack updates</a>.</p> </note>
            client_request_token: <p>A unique identifier for this <code>ContinueUpdateRollback</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to continue the rollback to a stack with the same name. You might retry <code>ContinueUpdateRollback</code> requests to ensure that CloudFormation successfully received them.</p>

        Raises:
            capo_cloudformation.errors.token_already_exists_exception.TokenAlreadyExistsException: <p>A client request token already exists.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.continue_update_rollback_input.ContinueUpdateRollbackInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.continue_update_rollback_output.ContinueUpdateRollbackOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.continue_update_rollback

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.continue_update_rollback.continue_update_rollback(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.continue_update_rollback_input.ContinueUpdateRollbackInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if resources_to_skip is not None:
            input_["resources_to_skip"] = resources_to_skip
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_change_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
        use_previous_template: Optional[
            "capo_cloudformation.types.use_previous_template.UsePreviousTemplate"
        ] = None,
        parameters: Optional["capo_cloudformation.types.parameters.Parameters"] = None,
        capabilities: Optional[
            "capo_cloudformation.types.capabilities.Capabilities"
        ] = None,
        resource_types: Optional[
            "capo_cloudformation.types.resource_types.ResourceTypes"
        ] = None,
        role_arn: Optional["capo_cloudformation.types.role_arn.RoleARN"] = None,
        rollback_configuration: Optional[
            "capo_cloudformation.types.rollback_configuration.RollbackConfiguration"
        ] = None,
        notification_ar_ns: Optional[
            "capo_cloudformation.types.notification_ar_ns.NotificationARNs"
        ] = None,
        tags: Optional["capo_cloudformation.types.tags.Tags"] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name.ChangeSetName"
        ] = None,
        client_token: Optional[
            "capo_cloudformation.types.client_token.ClientToken"
        ] = None,
        description: Optional[
            "capo_cloudformation.types.description.Description"
        ] = None,
        change_set_type: Optional[
            "capo_cloudformation.types.change_set_type.ChangeSetType"
        ] = None,
        resources_to_import: Optional[
            "capo_cloudformation.types.resources_to_import.ResourcesToImport"
        ] = None,
        include_nested_stacks: Optional[
            "capo_cloudformation.types.include_nested_stacks.IncludeNestedStacks"
        ] = None,
        on_stack_failure: Optional[
            "capo_cloudformation.types.on_stack_failure.OnStackFailure"
        ] = None,
        import_existing_resources: Optional[
            "capo_cloudformation.types.import_existing_resources.ImportExistingResources"
        ] = None,
        deployment_mode: Optional[
            "capo_cloudformation.types.deployment_mode.DeploymentMode"
        ] = None,
        deployment_config: Optional[
            "capo_cloudformation.types.deployment_config.DeploymentConfig"
        ] = None,
        disable_validation: Optional[
            "capo_cloudformation.types.disable_validation.DisableValidation"
        ] = None,
    ) -> "capo_cloudformation.types.create_change_set_output.CreateChangeSetOutput":
        """<p>Creates a list of changes that will be applied to a stack so that you can review the changes before executing them. You can create a change set for a stack that doesn't exist or an existing stack. If you create a change set for a stack that doesn't exist, the change set shows all of the resources that CloudFormation will create. If you create a change set for an existing stack, CloudFormation compares the stack's information with the information that you submit in the change set and lists the differences. Use change sets to understand which resources CloudFormation will create or change, and how it will change resources in an existing stack, before you create or update a stack.</p> <p>To create a change set for a stack that doesn't exist, for the <code>ChangeSetType</code> parameter, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code> for the <code>ChangeSetType</code> parameter. To create a change set for an import operation, specify <code>IMPORT</code> for the <code>ChangeSetType</code> parameter. After the <code>CreateChangeSet</code> call successfully completes, CloudFormation starts creating the change set. To check the status of the change set or to review it, use the <a>DescribeChangeSet</a> action.</p> <p>When you are satisfied with the changes the change set will make, execute the change set by using the <a>ExecuteChangeSet</a> action. CloudFormation doesn't make changes until you execute the change set.</p> <p>To create a change set for the entire stack hierarchy, set <code>IncludeNestedStacks</code> to <code>True</code>.</p>

        Args:
            stack_name: <p>The name or the unique ID of the stack for which you are creating a change set. CloudFormation generates the change set by comparing this stack's information with the information that you submit, such as a modified template or different parameter input values.</p>
            template_body: <p>A structure that contains the body of the revised template, with a minimum length of 1 byte and a maximum length of 51,200 bytes. CloudFormation generates the change set by comparing this template with the template of the stack that you specified.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
            template_url: <p>The URL of the file that contains the revised template. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. CloudFormation generates the change set by comparing this template with the stack that you specified. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
            use_previous_template: <p>Whether to reuse the template that's associated with the stack to create the change set.</p> <p>When using templates with the <code>AWS::LanguageExtensions</code> transform, provide the template instead of using <code>UsePreviousTemplate</code> to ensure new parameter values and Systems Manager parameter updates are applied correctly. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-languageextensions.html">AWS::LanguageExtensions transform</a>.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
            parameters: <p>A list of <code>Parameter</code> structures that specify input parameters for the change set. For more information, see the <a>Parameter</a> data type.</p>
            capabilities: <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account, for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html"> AWS::IAM::ManagedPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html"> AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <note> <p>This capacity doesn't apply to creating change sets, and specifying it when creating change sets has no effect.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create or update the stack directly from the template using the <a>CreateStack</a> or <a>UpdateStack</a> action, and specifying this capability.</p> </note> <p>For more information about macros, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> </li> </ul> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>
            resource_types: <p>Specifies which resource types you can work with, such as <code>AWS::EC2::Instance</code> or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource type that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. IAM uses this parameter for condition keys in IAM policies for CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html">Control CloudFormation access with Identity and Access Management</a> in the <i>CloudFormation User Guide</i>.</p> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes when executing the change set. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least permission.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>
            rollback_configuration: <p>The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.</p>
            notification_ar_ns: <p>The Amazon Resource Names (ARNs) of Amazon SNS topics that CloudFormation associates with the stack. To remove all associated notification topics, specify an empty list.</p>
            tags: <p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to resources in the stack. You can specify a maximum of 50 tags.</p>
            change_set_name: <p>The name of the change set. The name must be unique among all change sets that are associated with the specified stack.</p> <p>A change set name can contain only alphanumeric, case sensitive characters, and hyphens. It must start with an alphabetical character and can't exceed 128 characters.</p>
            client_token: <p>A unique identifier for this <code>CreateChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another change set with the same name. You might retry <code>CreateChangeSet</code> requests to ensure that CloudFormation successfully received them.</p>
            description: <p>A description to help you identify this change set.</p>
            change_set_type: <p>The type of change set operation. To create a change set for a new stack, specify <code>CREATE</code>. To create a change set for an existing stack, specify <code>UPDATE</code>. To create a change set for an import operation, specify <code>IMPORT</code>.</p> <p>If you create a change set for a new stack, CloudFormation creates a stack with a unique stack ID, but no template or resources. The stack will be in the <code>REVIEW_IN_PROGRESS</code> state until you execute the change set.</p> <p>By default, CloudFormation specifies <code>UPDATE</code>. You can't use the <code>UPDATE</code> type to create a change set for a new stack or the <code>CREATE</code> type to create a change set for an existing stack.</p>
            resources_to_import: <p>The resources to import into your stack.</p>
            include_nested_stacks: <p>Creates a change set for the all nested stacks specified in the template. The default behavior of this action is set to <code>False</code>. To include nested sets in a change set, specify <code>True</code>.</p>
            on_stack_failure: <p>Determines what action will be taken if stack creation fails. If this parameter is specified, the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation must not be specified. This must be one of these values:</p> <ul> <li> <p> <code>DELETE</code> - Deletes the change set if the stack creation fails. This is only valid when the <code>ChangeSetType</code> parameter is set to <code>CREATE</code>. If the deletion of the stack fails, the status of the stack is <code>DELETE_FAILED</code>.</p> </li> <li> <p> <code>DO_NOTHING</code> - if the stack creation fails, do nothing. This is equivalent to specifying <code>true</code> for the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation.</p> </li> <li> <p> <code>ROLLBACK</code> - if the stack creation fails, roll back the stack. This is equivalent to specifying <code>false</code> for the <code>DisableRollback</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html">ExecuteChangeSet</a> API operation.</p> </li> </ul> <p>For nested stacks, when the <code>OnStackFailure</code> parameter is set to <code>DELETE</code> for the change set for the parent stack, any failure in a child stack will cause the parent stack creation to fail and all stacks to be deleted.</p>
            import_existing_resources: <p>Indicates if the change set auto-imports resources that already exist. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/import-resources-automatically.html">Import Amazon Web Services resources into a CloudFormation stack automatically</a> in the <i>CloudFormation User Guide</i>.</p> <note> <p>This parameter can only import resources that have custom names in templates. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-name.html">name type</a> in the <i>CloudFormation User Guide</i>. To import resources that do not accept custom names, such as EC2 instances, use the <code>ResourcesToImport</code> parameter instead.</p> </note>
            deployment_mode: <p>Determines how CloudFormation handles configuration drift during deployment.</p> <ul> <li> <p> <code>REVERT_DRIFT</code> – Creates a drift-aware change set that brings actual resource states in line with template definitions. Provides a three-way comparison between actual state, previous deployment state, and desired state.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/drift-aware-change-sets.html">Using drift-aware change sets</a> in the <i>CloudFormation User Guide</i>.</p>
            deployment_config: <p>The deployment configuration for this stack operation, including the deployment mode.</p>
            disable_validation: <p> Set to <code>true</code> to disable pre-deployment validations in changeset or stack operations. </p> <p> Default: <code>false</code> </p>

        Raises:
            capo_cloudformation.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudformation.errors.insufficient_capabilities_exception.InsufficientCapabilitiesException: <p>The template contains resources with capabilities that weren't specified in the Capabilities parameter.</p>
            capo_cloudformation.errors.limit_exceeded_exception.LimitExceededException: <p>The quota for the resource has already been reached.</p> <p>For information about resource and stack limitations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.create_change_set_input.CreateChangeSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.create_change_set_output.CreateChangeSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.create_change_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.create_change_set.create_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.create_change_set_input.CreateChangeSetInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url
        if use_previous_template is not None:
            input_["use_previous_template"] = use_previous_template
        if parameters is not None:
            input_["parameters"] = parameters
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if rollback_configuration is not None:
            input_["rollback_configuration"] = rollback_configuration
        if notification_ar_ns is not None:
            input_["notification_ar_ns"] = notification_ar_ns
        if tags is not None:
            input_["tags"] = tags
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if client_token is not None:
            input_["client_token"] = client_token
        if description is not None:
            input_["description"] = description
        if change_set_type is not None:
            input_["change_set_type"] = change_set_type
        if resources_to_import is not None:
            input_["resources_to_import"] = resources_to_import
        if include_nested_stacks is not None:
            input_["include_nested_stacks"] = include_nested_stacks
        if on_stack_failure is not None:
            input_["on_stack_failure"] = on_stack_failure
        if import_existing_resources is not None:
            input_["import_existing_resources"] = import_existing_resources
        if deployment_mode is not None:
            input_["deployment_mode"] = deployment_mode
        if deployment_config is not None:
            input_["deployment_config"] = deployment_config
        if disable_validation is not None:
            input_["disable_validation"] = disable_validation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_generated_template(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        resources: Optional[
            "capo_cloudformation.types.resource_definitions.ResourceDefinitions"
        ] = None,
        generated_template_name: Optional[
            "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
        ] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        template_configuration: Optional[
            "capo_cloudformation.types.template_configuration.TemplateConfiguration"
        ] = None,
    ) -> "capo_cloudformation.types.create_generated_template_output.CreateGeneratedTemplateOutput":
        """<p>Creates a template from existing resources that are not already managed with CloudFormation. You can check the status of the template generation using the <code>DescribeGeneratedTemplate</code> API action.</p>

        Args:
            resources: <p>An optional list of resources to be included in the generated template.</p> <p>If no resources are specified,the template will be created without any resources. Resources can be added to the template using the <code>UpdateGeneratedTemplate</code> API action.</p>
            generated_template_name: <p>The name assigned to the generated template.</p>
            stack_name: <p>An optional name or ARN of a stack to use as the base stack for the generated template.</p>
            template_configuration: <p>The configuration details of the generated template, including the <code>DeletionPolicy</code> and <code>UpdateReplacePolicy</code>.</p>

        Raises:
            capo_cloudformation.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudformation.errors.concurrent_resources_limit_exceeded_exception.ConcurrentResourcesLimitExceededException: <p>No more than 5 generated templates can be in an <code>InProgress</code> or <code>Pending</code> status at one time. This error is also returned if a generated template that is in an <code>InProgress</code> or <code>Pending</code> status is attempted to be updated or deleted.</p>
            capo_cloudformation.errors.limit_exceeded_exception.LimitExceededException: <p>The quota for the resource has already been reached.</p> <p>For information about resource and stack limitations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To create a generated template
            This example creates a generated template with a resources file.

            >>> client.create_generated_template(resources=[{'ResourceType': 'AWS::S3::Bucket', 'ResourceIdentifier': {'BucketName': 'jazz-bucket'}}, {'ResourceType': 'AWS::EC2::DHCPOptions', 'ResourceIdentifier': {'DhcpOptionsId': 'random-id123'}}], generated_template_name='JazzyTemplate')
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.create_generated_template_input.CreateGeneratedTemplateInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.create_generated_template_output.CreateGeneratedTemplateOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.create_generated_template

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.create_generated_template.create_generated_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.create_generated_template_input.CreateGeneratedTemplateInput = {}
        if resources is not None:
            input_["resources"] = resources
        if generated_template_name is not None:
            input_["generated_template_name"] = generated_template_name
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if template_configuration is not None:
            input_["template_configuration"] = template_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stack(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
        parameters: Optional["capo_cloudformation.types.parameters.Parameters"] = None,
        disable_rollback: Optional[
            "capo_cloudformation.types.disable_rollback.DisableRollback"
        ] = None,
        rollback_configuration: Optional[
            "capo_cloudformation.types.rollback_configuration.RollbackConfiguration"
        ] = None,
        timeout_in_minutes: Optional[
            "capo_cloudformation.types.timeout_minutes.TimeoutMinutes"
        ] = None,
        notification_ar_ns: Optional[
            "capo_cloudformation.types.notification_ar_ns.NotificationARNs"
        ] = None,
        capabilities: Optional[
            "capo_cloudformation.types.capabilities.Capabilities"
        ] = None,
        resource_types: Optional[
            "capo_cloudformation.types.resource_types.ResourceTypes"
        ] = None,
        role_arn: Optional["capo_cloudformation.types.role_arn.RoleARN"] = None,
        on_failure: Optional["capo_cloudformation.types.on_failure.OnFailure"] = None,
        stack_policy_body: Optional[
            "capo_cloudformation.types.stack_policy_body.StackPolicyBody"
        ] = None,
        stack_policy_url: Optional[
            "capo_cloudformation.types.stack_policy_url.StackPolicyURL"
        ] = None,
        tags: Optional["capo_cloudformation.types.tags.Tags"] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        enable_termination_protection: Optional[
            "capo_cloudformation.types.enable_termination_protection.EnableTerminationProtection"
        ] = None,
        retain_except_on_create: Optional[
            "capo_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
        ] = None,
        deployment_config: Optional[
            "capo_cloudformation.types.deployment_config.DeploymentConfig"
        ] = None,
        disable_validation: Optional[
            "capo_cloudformation.types.disable_validation.DisableValidation"
        ] = None,
    ) -> "capo_cloudformation.types.create_stack_output.CreateStackOutput":
        """<p>Creates a stack as specified in the template. After the call completes successfully, the stack creation starts. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>For more information about creating a stack and monitoring stack progress, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html">Managing Amazon Web Services resources as a single unit with CloudFormation stacks</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            stack_name: <p>The name that's associated with the stack. The name must be unique in the Region in which you are creating the stack.</p> <note> <p>A stack name can contain only alphanumeric characters (case sensitive) and hyphens. It must start with an alphabetical character and can't be longer than 128 characters.</p> </note>
            template_body: <p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify either <code>TemplateBody</code> or <code>TemplateURL</code>, but not both.</p>
            template_url: <p>The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>
            parameters: <p>A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.</p>
            disable_rollback: <p>Set to <code>true</code> to disable rollback of the stack if stack creation failed. You can specify either <code>DisableRollback</code> or <code>OnFailure</code>, but not both.</p> <p>Default: <code>false</code> </p>
            rollback_configuration: <p>The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.</p>
            timeout_in_minutes: <p>The amount of time that can pass before the stack status becomes <code>CREATE_FAILED</code>; if <code>DisableRollback</code> is not set or is set to <code>false</code>, the stack will be rolled back.</p>
            notification_ar_ns: <p>The Amazon SNS topic ARNs to publish stack related events. You can find your Amazon SNS topic ARNs using the Amazon SNS console or your Command Line Interface (CLI).</p>
            capabilities: <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to create the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html">AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html">AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html"> AWS::IAM::ManagedPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html">AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html">AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html">AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually creating the stack. If your stack template contains one or more macros, and you choose to create a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to create a stack from a stack template that contains macros <i>and</i> nested stacks, you must create the stack directly from the template using this capability.</p> <important> <p>You should only create stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> </li> </ul> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>
            resource_types: <p>Specifies which resource types you can work with, such as <code>AWS::EC2::Instance</code> or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource that you're creating, the stack creation fails. By default, CloudFormation grants permissions to all resource types. IAM uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html">Control CloudFormation access with Identity and Access Management</a>.</p> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to create the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>
            on_failure: <p>Determines what action will be taken if stack creation fails. This must be one of: <code>DO_NOTHING</code>, <code>ROLLBACK</code>, or <code>DELETE</code>. You can specify either <code>OnFailure</code> or <code>DisableRollback</code>, but not both.</p> <note> <p>Although the default setting is <code>ROLLBACK</code>, there is one exception. This exception occurs when a StackSet attempts to deploy a stack instance and the stack instance fails to create successfully. In this case, the <code>CreateStack</code> call overrides the default setting and sets the value of <code>OnFailure</code> to <code>DELETE</code>.</p> </note> <p>Default: <code>ROLLBACK</code> </p>
            stack_policy_body: <p>Structure that contains the stack policy body. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html">Prevent updates to stack resources</a> in the <i>CloudFormation User Guide</i>. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>
            stack_policy_url: <p>Location of a file that contains the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an S3 bucket in the same Region as the stack. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>
            tags: <p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to the resources created in the stack. A maximum number of 50 tags can be specified.</p>
            client_request_token: <p>A unique identifier for this <code>CreateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create a stack with the same name. You might retry <code>CreateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>
            enable_termination_protection: <p>Whether to enable termination protection on the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protect CloudFormation stacks from being deleted</a> in the <i>CloudFormation User Guide</i>. Termination protection is deactivated on stacks by default.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>
            retain_except_on_create: <p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>
            deployment_config: <p>The deployment configuration for this stack operation, including the deployment mode.</p>
            disable_validation: <p> Set to <code>true</code> to disable pre-deployment validations in changeset or stack operations. </p> <p> Default: <code>false</code> </p>

        Raises:
            capo_cloudformation.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudformation.errors.insufficient_capabilities_exception.InsufficientCapabilitiesException: <p>The template contains resources with capabilities that weren't specified in the Capabilities parameter.</p>
            capo_cloudformation.errors.limit_exceeded_exception.LimitExceededException: <p>The quota for the resource has already been reached.</p> <p>For information about resource and stack limitations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
            capo_cloudformation.errors.token_already_exists_exception.TokenAlreadyExistsException: <p>A client request token already exists.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.create_stack_input.CreateStackInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.create_stack_output.CreateStackOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.create_stack

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.create_stack.create_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.create_stack_input.CreateStackInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url
        if parameters is not None:
            input_["parameters"] = parameters
        if disable_rollback is not None:
            input_["disable_rollback"] = disable_rollback
        if rollback_configuration is not None:
            input_["rollback_configuration"] = rollback_configuration
        if timeout_in_minutes is not None:
            input_["timeout_in_minutes"] = timeout_in_minutes
        if notification_ar_ns is not None:
            input_["notification_ar_ns"] = notification_ar_ns
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if on_failure is not None:
            input_["on_failure"] = on_failure
        if stack_policy_body is not None:
            input_["stack_policy_body"] = stack_policy_body
        if stack_policy_url is not None:
            input_["stack_policy_url"] = stack_policy_url
        if tags is not None:
            input_["tags"] = tags
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if enable_termination_protection is not None:
            input_["enable_termination_protection"] = enable_termination_protection
        if retain_except_on_create is not None:
            input_["retain_except_on_create"] = retain_except_on_create
        if deployment_config is not None:
            input_["deployment_config"] = deployment_config
        if disable_validation is not None:
            input_["disable_validation"] = disable_validation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stack_instances(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        accounts: Optional["capo_cloudformation.types.account_list.AccountList"] = None,
        deployment_targets: Optional[
            "capo_cloudformation.types.deployment_targets.DeploymentTargets"
        ] = None,
        regions: Optional["capo_cloudformation.types.region_list.RegionList"] = None,
        parameter_overrides: Optional[
            "capo_cloudformation.types.parameters.Parameters"
        ] = None,
        operation_preferences: Optional[
            "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.create_stack_instances_output.CreateStackInstancesOutput":
        """<p>Creates stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region. You must specify at least one value for either <code>Accounts</code> or <code>DeploymentTargets</code>, and you must specify at least one value for <code>Regions</code>.</p> <note> <p>The maximum number of organizational unit (OUs) supported by a <code>CreateStackInstances</code> operation is 50.</p> <p>If you need more than 50, consider the following options:</p> <ul> <li> <p> <i>Batch processing:</i> If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each.</p> </li> <li> <p> <i>Parent OU strategy:</i> If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.</p> </li> </ul> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to create stack instances from.</p>
            accounts: <p>[Self-managed permissions] The account IDs of one or more Amazon Web Services accounts that you want to create stack instances in the specified Region(s) for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
            deployment_targets: <p>[Service-managed permissions] The Organizations accounts in which to create stack instances in the specified Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
            regions: <p>The names of one or more Amazon Web Services Regions where you want to create stack instances using the specified Amazon Web Services accounts.</p>
            parameter_overrides: <p>A list of StackSet parameters whose values you want to override in the selected stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the StackSet, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During StackSet updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the StackSet; to add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the StackSet template.</p>
            operation_preferences: <p>Preferences for how CloudFormation performs this StackSet operation.</p>
            operation_id: <p>The unique identifier for this StackSet operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the StackSet operation only once, even if you retry the request multiple times. You might retry StackSet operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>Repeating this StackSet operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.limit_exceeded_exception.LimitExceededException: <p>The quota for the resource has already been reached.</p> <p>For information about resource and stack limitations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
            capo_cloudformation.errors.operation_id_already_exists_exception.OperationIdAlreadyExistsException: <p>The specified operation ID already exists.</p>
            capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException: <p>Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.stale_request_exception.StaleRequestException: <p>Another operation has been performed on this StackSet since the specified operation was performed.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.create_stack_instances_input.CreateStackInstancesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.create_stack_instances_output.CreateStackInstancesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.create_stack_instances

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.create_stack_instances.create_stack_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.create_stack_instances_input.CreateStackInstancesInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if accounts is not None:
            input_["accounts"] = accounts
        if deployment_targets is not None:
            input_["deployment_targets"] = deployment_targets
        if regions is not None:
            input_["regions"] = regions
        if parameter_overrides is not None:
            input_["parameter_overrides"] = parameter_overrides
        if operation_preferences is not None:
            input_["operation_preferences"] = operation_preferences
        if operation_id is None:
            operation_id = str(uuid.uuid4())
        input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stack_refactor(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        description: Optional[
            "capo_cloudformation.types.description.Description"
        ] = None,
        enable_stack_creation: Optional[
            "capo_cloudformation.types.enable_stack_creation.EnableStackCreation"
        ] = None,
        resource_mappings: Optional[
            "capo_cloudformation.types.resource_mappings.ResourceMappings"
        ] = None,
        stack_definitions: Optional[
            "capo_cloudformation.types.stack_definitions.StackDefinitions"
        ] = None,
    ) -> "capo_cloudformation.types.create_stack_refactor_output.CreateStackRefactorOutput":
        """<p>Creates a refactor across multiple stacks, with the list of stacks and resources that are affected.</p>

        Args:
            description: <p>A description to help you identify the stack refactor.</p>
            enable_stack_creation: <p>Determines if a new stack is created with the refactor.</p>
            resource_mappings: <p>The mappings for the stack resource <code>Source</code> and stack resource <code>Destination</code>.</p>
            stack_definitions: <p>The stacks being refactored.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.create_stack_refactor_input.CreateStackRefactorInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.create_stack_refactor_output.CreateStackRefactorOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.create_stack_refactor

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.create_stack_refactor.create_stack_refactor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.create_stack_refactor_input.CreateStackRefactorInput = {}
        if description is not None:
            input_["description"] = description
        if enable_stack_creation is not None:
            input_["enable_stack_creation"] = enable_stack_creation
        if resource_mappings is not None:
            input_["resource_mappings"] = resource_mappings
        if stack_definitions is not None:
            input_["stack_definitions"] = stack_definitions

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def create_stack_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        description: Optional[
            "capo_cloudformation.types.description.Description"
        ] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
        stack_id: Optional["capo_cloudformation.types.stack_id.StackId"] = None,
        parameters: Optional["capo_cloudformation.types.parameters.Parameters"] = None,
        capabilities: Optional[
            "capo_cloudformation.types.capabilities.Capabilities"
        ] = None,
        tags: Optional["capo_cloudformation.types.tags.Tags"] = None,
        administration_role_arn: Optional[
            "capo_cloudformation.types.role_arn.RoleARN"
        ] = None,
        execution_role_name: Optional[
            "capo_cloudformation.types.execution_role_name.ExecutionRoleName"
        ] = None,
        permission_model: Optional[
            "capo_cloudformation.types.permission_models.PermissionModels"
        ] = None,
        auto_deployment: Optional[
            "capo_cloudformation.types.auto_deployment.AutoDeployment"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        managed_execution: Optional[
            "capo_cloudformation.types.managed_execution.ManagedExecution"
        ] = None,
    ) -> "capo_cloudformation.types.create_stack_set_output.CreateStackSetOutput":
        """<p>Creates a StackSet.</p>

        Args:
            stack_set_name: <p>The name to associate with the StackSet. The name must be unique in the Region where you create your StackSet.</p> <note> <p>A stack name can contain only alphanumeric characters (case-sensitive) and hyphens. It must start with an alphabetic character and can't be longer than 128 characters.</p> </note>
            description: <p>A description of the StackSet. You can use the description to identify the StackSet's purpose or other important information.</p>
            template_body: <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>
            template_url: <p>The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>. S3 static website URLs are not supported.</p> <p>Conditional: You must specify either the <code>TemplateBody</code> or the <code>TemplateURL</code> parameter, but not both.</p>
            stack_id: <p>The stack ID you are importing into a new StackSet. Specify the Amazon Resource Name (ARN) of the stack.</p>
            parameters: <p>The input parameters for the StackSet template.</p>
            capabilities: <p>In some cases, you must explicitly acknowledge that your StackSet template contains certain capabilities in order for CloudFormation to create the StackSet and related stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account; for example, by creating new IAM users. For those StackSets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html">AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html">AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html">AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html">AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html">AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your StackSet template references one or more macros, you must create the StackSet directly from the processed template, without first reviewing the resulting changes in a change set. To create the StackSet directly, you must acknowledge this capability. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> <important> <p>StackSets with service-managed permissions don't currently support the use of macros in templates. (This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a StackSet with service-managed permissions, if you reference a macro in your template the StackSet operation will fail.</p> </important> </li> </ul>
            tags: <p>The key-value pairs to associate with this StackSet and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. A maximum number of 50 tags can be specified.</p> <p>If you specify tags as part of a <code>CreateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you don't, the entire <code>CreateStackSet</code> action fails with an <code>access denied</code> error, and the StackSet is not created.</p>
            administration_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role to use to create this StackSet.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a> in the <i>CloudFormation User Guide</i>.</p> <p>Valid only if the permissions model is <code>SELF_MANAGED</code>.</p>
            execution_role_name: <p>The name of the IAM execution role to use to create the StackSet. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the StackSet operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their StackSets.</p> <p>Valid only if the permissions model is <code>SELF_MANAGED</code>.</p>
            permission_model: <p>Describes how the IAM roles required for StackSet operations are created. By default, <code>SELF-MANAGED</code> is specified.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html">Activate trusted access for StackSets with Organizations</a>.</p> </li> </ul>
            auto_deployment: <p>Describes whether StackSets automatically deploys to Organizations accounts that are added to the target organization or organizational unit (OU). For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html">Enable or disable automatic deployments for StackSets in Organizations</a> in the <i>CloudFormation User Guide</i>.</p> <p>Required if the permissions model is <code>SERVICE_MANAGED</code>. (Not used with self-managed permissions.)</p>
            call_as: <p>Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>To create a StackSet with service-managed permissions while signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>To create a StackSet with service-managed permissions while signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated admin in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul> <p>StackSets with service-managed permissions are created in the management account, including StackSets that are created by delegated administrators.</p> <p>Valid only if the permissions model is <code>SERVICE_MANAGED</code>.</p>
            client_request_token: <p>A unique identifier for this <code>CreateStackSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to create another StackSet with the same name. You might retry <code>CreateStackSet</code> requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>
            managed_execution: <p>Describes whether CloudFormation performs non-conflicting operations concurrently and queues conflicting operations.</p>

        Raises:
            capo_cloudformation.errors.created_but_modified_exception.CreatedButModifiedException: <p>The specified resource exists, but has been changed.</p>
            capo_cloudformation.errors.limit_exceeded_exception.LimitExceededException: <p>The quota for the resource has already been reached.</p> <p>For information about resource and stack limitations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
            capo_cloudformation.errors.name_already_exists_exception.NameAlreadyExistsException: <p>The specified name is already in use.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.create_stack_set_input.CreateStackSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.create_stack_set_output.CreateStackSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.create_stack_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.create_stack_set.create_stack_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.create_stack_set_input.CreateStackSetInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if description is not None:
            input_["description"] = description
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url
        if stack_id is not None:
            input_["stack_id"] = stack_id
        if parameters is not None:
            input_["parameters"] = parameters
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if tags is not None:
            input_["tags"] = tags
        if administration_role_arn is not None:
            input_["administration_role_arn"] = administration_role_arn
        if execution_role_name is not None:
            input_["execution_role_name"] = execution_role_name
        if permission_model is not None:
            input_["permission_model"] = permission_model
        if auto_deployment is not None:
            input_["auto_deployment"] = auto_deployment
        if call_as is not None:
            input_["call_as"] = call_as
        if client_request_token is None:
            client_request_token = str(uuid.uuid4())
        input_["client_request_token"] = client_request_token
        if managed_execution is not None:
            input_["managed_execution"] = managed_execution

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deactivate_organizations_access(
        self, *, config_overrides: Optional[CloudFormationClientConfig] = None
    ) -> "capo_cloudformation.types.deactivate_organizations_access_output.DeactivateOrganizationsAccessOutput":
        """<p>Deactivates trusted access with Organizations. If trusted access is deactivated, the management account does not have permissions to create and manage service-managed StackSets for your organization.</p>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_not_found_exception.OperationNotFoundException: <p>The specified ID refers to an operation that doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.deactivate_organizations_access_input.DeactivateOrganizationsAccessInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.deactivate_organizations_access_output.DeactivateOrganizationsAccessOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.deactivate_organizations_access

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.deactivate_organizations_access.deactivate_organizations_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.deactivate_organizations_access_input.DeactivateOrganizationsAccessInput = {}

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deactivate_type(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        type: Optional[
            "capo_cloudformation.types.third_party_type.ThirdPartyType"
        ] = None,
        arn: Optional[
            "capo_cloudformation.types.private_type_arn.PrivateTypeArn"
        ] = None,
    ) -> "capo_cloudformation.types.deactivate_type_output.DeactivateTypeOutput":
        """<p>Deactivates a public third-party extension, such as a resource or module, or a CloudFormation Hook when you no longer use it.</p> <p>Deactivating an extension deletes the configuration details that are associated with it. To temporarily disable a CloudFormation Hook instead, you can use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a>.</p> <p>Once deactivated, an extension can't be used in any CloudFormation operation. This includes stack update operations where the stack template includes the extension, even if no updates are being made to the extension. In addition, deactivated extensions aren't automatically updated if a new version of the extension is released.</p> <p>To see which extensions are currently activated, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListTypes.html">ListTypes</a>.</p>

        Args:
            type_name: <p>The type name of the extension in this account and Region. If you specified a type name alias when enabling the extension, use the type name alias.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            type: <p>The extension type.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            arn: <p>The Amazon Resource Name (ARN) for the extension in this account and Region.</p> <p>Conditional: You must specify either <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.deactivate_type_input.DeactivateTypeInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.deactivate_type_output.DeactivateTypeOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.deactivate_type

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.deactivate_type.deactivate_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.deactivate_type_input.DeactivateTypeInput = {}
        if type_name is not None:
            input_["type_name"] = type_name
        if type is not None:
            input_["type"] = type
        if arn is not None:
            input_["arn"] = arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_change_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
    ) -> "capo_cloudformation.types.delete_change_set_output.DeleteChangeSetOutput":
        """<p>Deletes the specified change set. Deleting change sets ensures that no one executes the wrong change set.</p> <p>If the call successfully completes, CloudFormation successfully deleted the change set.</p> <p>If <code>IncludeNestedStacks</code> specifies <code>True</code> during the creation of the nested change set, then <code>DeleteChangeSet</code> will delete all change sets that belong to the stacks hierarchy and will also delete all change sets for nested stacks with the status of <code>REVIEW_IN_PROGRESS</code>.</p>

        Args:
            change_set_name: <p>The name or Amazon Resource Name (ARN) of the change set that you want to delete.</p>
            stack_name: <p>If you specified the name of a change set to delete, specify the stack name or Amazon Resource Name (ARN) that's associated with it.</p>

        Raises:
            capo_cloudformation.errors.invalid_change_set_status_exception.InvalidChangeSetStatusException: <p>The specified change set can't be used to update the stack. For example, the change set status might be <code>CREATE_IN_PROGRESS</code>, or the stack status might be <code>UPDATE_IN_PROGRESS</code>.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.delete_change_set_input.DeleteChangeSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.delete_change_set_output.DeleteChangeSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.delete_change_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.delete_change_set.delete_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.delete_change_set_input.DeleteChangeSetInput = {}
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if stack_name is not None:
            input_["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_generated_template(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        generated_template_name: Optional[
            "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
        ] = None,
    ) -> None:
        """<p>Deleted a generated template.</p>

        Args:
            generated_template_name: <p>The name or Amazon Resource Name (ARN) of a generated template.</p>

        Raises:
            capo_cloudformation.errors.concurrent_resources_limit_exceeded_exception.ConcurrentResourcesLimitExceededException: <p>No more than 5 generated templates can be in an <code>InProgress</code> or <code>Pending</code> status at one time. This error is also returned if a generated template that is in an <code>InProgress</code> or <code>Pending</code> status is attempted to be updated or deleted.</p>
            capo_cloudformation.errors.generated_template_not_found_exception.GeneratedTemplateNotFoundException: <p>The generated template was not found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To delete a generated template
            This example deletes a generated template

            >>> client.delete_generated_template(generated_template_name='JazzyTemplate')
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.delete_generated_template_input.DeleteGeneratedTemplateInput]",
        ) -> OperationResponse[None]:
            import capo_cloudformation._operations.cloud_formation.delete_generated_template

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.delete_generated_template.delete_generated_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.delete_generated_template_input.DeleteGeneratedTemplateInput = {}
        if generated_template_name is not None:
            input_["generated_template_name"] = generated_template_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stack(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        retain_resources: Optional[
            "capo_cloudformation.types.retain_resources.RetainResources"
        ] = None,
        role_arn: Optional["capo_cloudformation.types.role_arn.RoleARN"] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        deletion_mode: Optional[
            "capo_cloudformation.types.deletion_mode.DeletionMode"
        ] = None,
        deployment_config: Optional[
            "capo_cloudformation.types.deployment_config.DeploymentConfig"
        ] = None,
    ) -> None:
        """<p>Deletes a specified stack. Once the call completes successfully, stack deletion starts. Deleted stacks don't show up in the <a>DescribeStacks</a> operation if the deletion has been completed successfully.</p> <p>For more information about deleting a stack, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-delete-stack.html">Delete a stack from the CloudFormation console</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            stack_name: <p>The name or the unique stack ID that's associated with the stack.</p>
            retain_resources: <p>For stacks in the <code>DELETE_FAILED</code> state, a list of resource logical IDs that are associated with the resources you want to retain. During deletion, CloudFormation deletes the stack but doesn't delete the retained resources.</p> <p>Retaining resources is useful when you can't delete a resource, such as a non-empty S3 bucket, but you want to delete the stack.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to delete the stack. CloudFormation uses the role's credentials to make calls on your behalf.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that's generated from your user credentials.</p>
            client_request_token: <p>A unique identifier for this <code>DeleteStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to delete a stack with the same name. You might retry <code>DeleteStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events initiated by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>
            deletion_mode: <p>Specifies the deletion mode for the stack. Possible values are:</p> <ul> <li> <p> <code>STANDARD</code> - Use the standard behavior. Specifying this value is the same as not specifying this parameter.</p> </li> <li> <p> <code>FORCE_DELETE_STACK</code> - Delete the stack if it's stuck in a <code>DELETE_FAILED</code> state due to resource deletion failure.</p> </li> </ul>
            deployment_config: <p>The deployment configuration for this stack operation, including the deployment mode.</p>

        Raises:
            capo_cloudformation.errors.token_already_exists_exception.TokenAlreadyExistsException: <p>A client request token already exists.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.delete_stack_input.DeleteStackInput]",
        ) -> OperationResponse[None]:
            import capo_cloudformation._operations.cloud_formation.delete_stack

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.delete_stack.delete_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.delete_stack_input.DeleteStackInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if retain_resources is not None:
            input_["retain_resources"] = retain_resources
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if deletion_mode is not None:
            input_["deletion_mode"] = deletion_mode
        if deployment_config is not None:
            input_["deployment_config"] = deployment_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stack_instances(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        accounts: Optional["capo_cloudformation.types.account_list.AccountList"] = None,
        deployment_targets: Optional[
            "capo_cloudformation.types.deployment_targets.DeploymentTargets"
        ] = None,
        regions: Optional["capo_cloudformation.types.region_list.RegionList"] = None,
        operation_preferences: Optional[
            "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
        ] = None,
        retain_stacks: Optional[
            "capo_cloudformation.types.retain_stacks.RetainStacks"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.delete_stack_instances_output.DeleteStackInstancesOutput":
        """<p>Deletes stack instances for the specified accounts, in the specified Amazon Web Services Regions.</p> <note> <p>The maximum number of organizational unit (OUs) supported by a <code>DeleteStackInstances</code> operation is 50.</p> <p>If you need more than 50, consider the following options:</p> <ul> <li> <p> <i>Batch processing:</i> If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each.</p> </li> <li> <p> <i>Parent OU strategy:</i> If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.</p> </li> </ul> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to delete stack instances for.</p>
            accounts: <p>[Self-managed permissions] The account IDs of the Amazon Web Services accounts that you want to delete stack instances for.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
            deployment_targets: <p>[Service-managed permissions] The Organizations accounts from which to delete stack instances.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
            regions: <p>The Amazon Web Services Regions where you want to delete StackSet instances.</p>
            operation_preferences: <p>Preferences for how CloudFormation performs this StackSet operation.</p>
            retain_stacks: <p>Removes the stack instances from the specified StackSet, but doesn't delete the stacks. You can't reassociate a retained stack or add an existing, saved stack to a new stack set.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">StackSet operation options</a>.</p>
            operation_id: <p>The unique identifier for this StackSet operation.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the StackSet operation only once, even if you retry the request multiple times. You can retry StackSet operation requests to ensure that CloudFormation successfully received them.</p> <p>Repeating this StackSet operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_id_already_exists_exception.OperationIdAlreadyExistsException: <p>The specified operation ID already exists.</p>
            capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException: <p>Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.stale_request_exception.StaleRequestException: <p>Another operation has been performed on this StackSet since the specified operation was performed.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.delete_stack_instances_input.DeleteStackInstancesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.delete_stack_instances_output.DeleteStackInstancesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.delete_stack_instances

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.delete_stack_instances.delete_stack_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.delete_stack_instances_input.DeleteStackInstancesInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if accounts is not None:
            input_["accounts"] = accounts
        if deployment_targets is not None:
            input_["deployment_targets"] = deployment_targets
        if regions is not None:
            input_["regions"] = regions
        if operation_preferences is not None:
            input_["operation_preferences"] = operation_preferences
        if retain_stacks is not None:
            input_["retain_stacks"] = retain_stacks
        if operation_id is None:
            operation_id = str(uuid.uuid4())
        input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def delete_stack_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.delete_stack_set_output.DeleteStackSetOutput":
        """<p>Deletes a StackSet. Before you can delete a StackSet, all its member stack instances must be deleted. For more information about how to complete this, see <a>DeleteStackInstances</a>.</p>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you're deleting. You can obtain this value by running <a>ListStackSets</a>.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException: <p>Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.</p>
            capo_cloudformation.errors.stack_set_not_empty_exception.StackSetNotEmptyException: <p>You can't yet delete this StackSet, because it still contains one or more stack instances. Delete all stack instances from the StackSet before deleting the StackSet.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.delete_stack_set_input.DeleteStackSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.delete_stack_set_output.DeleteStackSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.delete_stack_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.delete_stack_set.delete_stack_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.delete_stack_set_input.DeleteStackSetInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def deregister_type(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        arn: Optional[
            "capo_cloudformation.types.private_type_arn.PrivateTypeArn"
        ] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        version_id: Optional[
            "capo_cloudformation.types.type_version_id.TypeVersionId"
        ] = None,
    ) -> "capo_cloudformation.types.deregister_type_output.DeregisterTypeOutput":
        """<p>Marks an extension or extension version as <code>DEPRECATED</code> in the CloudFormation registry, removing it from active use. Deprecated extensions or extension versions cannot be used in CloudFormation operations.</p> <p>To deregister an entire extension, you must individually deregister all active versions of that extension. If an extension has only a single active version, deregistering that version results in the extension itself being deregistered and marked as deprecated in the registry.</p> <p>You can't deregister the default version of an extension if there are other active version of that extension. If you do deregister the default version of an extension, the extension type itself is deregistered as well and marked as deprecated.</p> <p>To view the deprecation status of an extension or extension version, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-private-deregister-extension.html">Remove third-party private extensions from your account</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type: <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type_name: <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            version_id: <p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.deregister_type_input.DeregisterTypeInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.deregister_type_output.DeregisterTypeOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.deregister_type

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.deregister_type.deregister_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.deregister_type_input.DeregisterTypeInput = {}
        if arn is not None:
            input_["arn"] = arn
        if type is not None:
            input_["type"] = type
        if type_name is not None:
            input_["type_name"] = type_name
        if version_id is not None:
            input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_account_limits(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.describe_account_limits_output.DescribeAccountLimitsOutput":
        """<p>Retrieves your account's CloudFormation limits, such as the maximum number of stacks that you can create in your account. For more information about account limits, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">Understand CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_account_limits_input.DescribeAccountLimitsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_account_limits_output.DescribeAccountLimitsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_account_limits

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_account_limits.describe_account_limits(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_account_limits_input.DescribeAccountLimitsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_account_limits(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.account_limit.AccountLimit]":
        _token = next_token
        while True:
            _response = self.describe_account_limits(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("account_limits",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_change_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        include_property_values: Optional[
            "capo_cloudformation.types.include_property_values.IncludePropertyValues"
        ] = None,
    ) -> "capo_cloudformation.types.describe_change_set_output.DescribeChangeSetOutput":
        """<p>Returns the inputs for the change set and a list of changes that CloudFormation will make if you execute the change set. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-changesets.html">Update CloudFormation stacks using change sets</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            change_set_name: <p>The name or Amazon Resource Name (ARN) of the change set that you want to describe.</p>
            stack_name: <p>If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            include_property_values: <p>If <code>true</code>, the returned changes include detailed changes in the property values.</p>

        Raises:
            capo_cloudformation.errors.change_set_not_found_exception.ChangeSetNotFoundException: <p>The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the <code>ListChangeSets</code> operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_change_set_input.DescribeChangeSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_change_set_output.DescribeChangeSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_change_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_change_set.describe_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_change_set_input.DescribeChangeSetInput = {}
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if next_token is not None:
            input_["next_token"] = next_token
        if include_property_values is not None:
            input_["include_property_values"] = include_property_values

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_change_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        include_property_values: Optional[
            "capo_cloudformation.types.include_property_values.IncludePropertyValues"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.change.Change]":
        _token = next_token
        while True:
            _response = self.describe_change_set(
                config_overrides=config_overrides,
                change_set_name=change_set_name,
                stack_name=stack_name,
                next_token=_token,
                include_property_values=include_property_values,
            )
            _page = _resolve_path(_response, ("changes",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_change_set_hooks(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        logical_resource_id: Optional[
            "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
        ] = None,
    ) -> "capo_cloudformation.types.describe_change_set_hooks_output.DescribeChangeSetHooksOutput":
        """<p>Returns Hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.</p>

        Args:
            change_set_name: <p>The name or Amazon Resource Name (ARN) of the change set that you want to describe.</p>
            stack_name: <p>If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            logical_resource_id: <p>If specified, lists only the Hooks related to the specified <code>LogicalResourceId</code>.</p>

        Raises:
            capo_cloudformation.errors.change_set_not_found_exception.ChangeSetNotFoundException: <p>The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the <code>ListChangeSets</code> operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_change_set_hooks_input.DescribeChangeSetHooksInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_change_set_hooks_output.DescribeChangeSetHooksOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_change_set_hooks

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_change_set_hooks.describe_change_set_hooks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_change_set_hooks_input.DescribeChangeSetHooksInput = {}
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if next_token is not None:
            input_["next_token"] = next_token
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_events(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.operation_id.OperationId"
        ] = None,
        filters: Optional["capo_cloudformation.types.event_filter.EventFilter"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.describe_events_output.DescribeEventsOutput":
        """<p>Returns CloudFormation events based on flexible query criteria. Groups events by operation ID, enabling you to focus on individual stack operations during deployment.</p> <p>An operation is any action performed on a stack, including stack lifecycle actions (Create, Update, Delete, Rollback), change set creation, nested stack creation, and automatic rollbacks triggered by failures. Each operation has a unique identifier (Operation ID) and represents a discrete change attempt on the stack.</p> <p>Returns different types of events including:</p> <ul> <li> <p> <b>Progress events</b> - Status updates during stack operation execution.</p> </li> <li> <p> <b>Validation errors</b> - Failures from CloudFormation Early Validations.</p> </li> <li> <p> <b>Provisioning errors</b> - Resource creation and update failures.</p> </li> <li> <p> <b>Hook invocation errors</b> - Failures from CloudFormation Hook during stack operations.</p> </li> </ul> <note> <p>One of <code>ChangeSetName</code>, <code>OperationId</code> or <code>StackName</code> must be specified as input.</p> </note>

        Args:
            stack_name: <p>The name or unique stack ID for which you want to retrieve events. If you specified the name of a change set, specify the stack name or ID (ARN) of the change set you want to describe.</p>
            change_set_name: <p>The name or Amazon Resource Name (ARN) of the change set for which you want to retrieve events.</p>
            operation_id: <p>The unique identifier of the operation for which you want to retrieve events.</p>
            filters: <p>Filters to apply when retrieving events.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_events_input.DescribeEventsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_events_output.DescribeEventsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_events

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_events.describe_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_events_input.DescribeEventsInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if operation_id is not None:
            input_["operation_id"] = operation_id
        if filters is not None:
            input_["filters"] = filters
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_events(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.operation_id.OperationId"
        ] = None,
        filters: Optional["capo_cloudformation.types.event_filter.EventFilter"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.operation_event.OperationEvent]":
        _token = next_token
        while True:
            _response = self.describe_events(
                config_overrides=config_overrides,
                stack_name=stack_name,
                change_set_name=change_set_name,
                operation_id=operation_id,
                filters=filters,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("operation_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_generated_template(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        generated_template_name: Optional[
            "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
        ] = None,
    ) -> "capo_cloudformation.types.describe_generated_template_output.DescribeGeneratedTemplateOutput":
        """<p>Describes a generated template. The output includes details about the progress of the creation of a generated template started by a <code>CreateGeneratedTemplate</code> API action or the update of a generated template started with an <code>UpdateGeneratedTemplate</code> API action.</p>

        Args:
            generated_template_name: <p>The name or Amazon Resource Name (ARN) of a generated template.</p>

        Raises:
            capo_cloudformation.errors.generated_template_not_found_exception.GeneratedTemplateNotFoundException: <p>The generated template was not found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_generated_template_input.DescribeGeneratedTemplateInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_generated_template_output.DescribeGeneratedTemplateOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_generated_template

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_generated_template.describe_generated_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_generated_template_input.DescribeGeneratedTemplateInput = {}
        if generated_template_name is not None:
            input_["generated_template_name"] = generated_template_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_organizations_access(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.describe_organizations_access_output.DescribeOrganizationsAccessOutput":
        """<p>Retrieves information about the account's <code>OrganizationAccess</code> status. This API can be called either by the management account or the delegated administrator by using the <code>CallAs</code> parameter. This API can also be called without the <code>CallAs</code> parameter by the management account.</p>

        Args:
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_not_found_exception.OperationNotFoundException: <p>The specified ID refers to an operation that doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_organizations_access_input.DescribeOrganizationsAccessInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_organizations_access_output.DescribeOrganizationsAccessOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_organizations_access

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_organizations_access.describe_organizations_access(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_organizations_access_input.DescribeOrganizationsAccessInput = {}
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_publisher(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        publisher_id: Optional[
            "capo_cloudformation.types.publisher_id.PublisherId"
        ] = None,
    ) -> "capo_cloudformation.types.describe_publisher_output.DescribePublisherOutput":
        """<p>Returns information about a CloudFormation extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p> <p>For more information about registering as a publisher, see:</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i> </p> </li> </ul>

        Args:
            publisher_id: <p>The ID of the extension publisher.</p> <p>If you don't supply a <code>PublisherId</code>, and you have registered as an extension publisher, <code>DescribePublisher</code> returns information about your own publisher account.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_publisher_input.DescribePublisherInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_publisher_output.DescribePublisherOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_publisher

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_publisher.describe_publisher(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_publisher_input.DescribePublisherInput = {}
        if publisher_id is not None:
            input_["publisher_id"] = publisher_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_resource_scan(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        resource_scan_id: Optional[
            "capo_cloudformation.types.resource_scan_id.ResourceScanId"
        ] = None,
    ) -> "capo_cloudformation.types.describe_resource_scan_output.DescribeResourceScanOutput":
        """<p>Describes details of a resource scan.</p>

        Args:
            resource_scan_id: <p>The Amazon Resource Name (ARN) of the resource scan.</p>

        Raises:
            capo_cloudformation.errors.resource_scan_not_found_exception.ResourceScanNotFoundException: <p>The resource scan was not found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_resource_scan_input.DescribeResourceScanInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_resource_scan_output.DescribeResourceScanOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_resource_scan

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_resource_scan.describe_resource_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_resource_scan_input.DescribeResourceScanInput = {}
        if resource_scan_id is not None:
            input_["resource_scan_id"] = resource_scan_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stack_drift_detection_status(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_drift_detection_id: Optional[
            "capo_cloudformation.types.stack_drift_detection_id.StackDriftDetectionId"
        ] = None,
    ) -> "capo_cloudformation.types.describe_stack_drift_detection_status_output.DescribeStackDriftDetectionStatusOutput":
        """<p>Returns information about a stack drift detection operation. A stack drift detection operation detects whether a stack's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. A stack is considered to have drifted if one or more of its resources have drifted. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detect unmanaged configuration changes to stacks and resources with drift detection</a>.</p> <p>Use <a>DetectStackDrift</a> to initiate a stack drift detection operation. <code>DetectStackDrift</code> returns a <code>StackDriftDetectionId</code> you can use to monitor the progress of the operation using <code>DescribeStackDriftDetectionStatus</code>. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p>

        Args:
            stack_drift_detection_id: <p>The ID of the drift detection results of this operation.</p> <p>CloudFormation generates new results, with a new drift detection ID, each time this operation is run. However, the number of drift results CloudFormation retains for any given stack, and for how long, may vary.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_drift_detection_status_input.DescribeStackDriftDetectionStatusInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_drift_detection_status_output.DescribeStackDriftDetectionStatusOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_drift_detection_status

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_drift_detection_status.describe_stack_drift_detection_status(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_drift_detection_status_input.DescribeStackDriftDetectionStatusInput = {}
        if stack_drift_detection_id is not None:
            input_["stack_drift_detection_id"] = stack_drift_detection_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stack_events(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.describe_stack_events_output.DescribeStackEventsOutput":
        """<p>Returns all stack related events for a specified stack in reverse chronological order. For more information about a stack's event history, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-resource-configuration-complete.html">Understand CloudFormation stack creation events</a> in the <i>CloudFormation User Guide</i>.</p> <note> <p>You can list events for stacks that have failed to create or have been deleted by specifying the unique stack identifier (stack ID).</p> </note>

        Args:
            stack_name: <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_events_input.DescribeStackEventsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_events_output.DescribeStackEventsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_events

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_events.describe_stack_events(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_events_input.DescribeStackEventsInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_stack_events(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_event.StackEvent]":
        _token = next_token
        while True:
            _response = self.describe_stack_events(
                config_overrides=config_overrides,
                stack_name=stack_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("stack_events",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_stack_instance(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        stack_instance_account: Optional[
            "capo_cloudformation.types.account.Account"
        ] = None,
        stack_instance_region: Optional[
            "capo_cloudformation.types.region.Region"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.describe_stack_instance_output.DescribeStackInstanceOutput":
        """<p>Returns the stack instance that's associated with the specified StackSet, Amazon Web Services account, and Amazon Web Services Region.</p> <p>For a list of stack instances that are associated with a specific StackSet, use <a>ListStackInstances</a>.</p>

        Args:
            stack_set_name: <p>The name or the unique stack ID of the StackSet that you want to get stack instance information for.</p>
            stack_instance_account: <p>The ID of an Amazon Web Services account that's associated with this stack instance.</p>
            stack_instance_region: <p>The name of a Region that's associated with this stack instance.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.stack_instance_not_found_exception.StackInstanceNotFoundException: <p>The specified stack instance doesn't exist.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_instance_input.DescribeStackInstanceInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_instance_output.DescribeStackInstanceOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_instance

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_instance.describe_stack_instance(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_instance_input.DescribeStackInstanceInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if stack_instance_account is not None:
            input_["stack_instance_account"] = stack_instance_account
        if stack_instance_region is not None:
            input_["stack_instance_region"] = stack_instance_region
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stack_refactor(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_refactor_id: Optional[
            "capo_cloudformation.types.stack_refactor_id.StackRefactorId"
        ] = None,
    ) -> "capo_cloudformation.types.describe_stack_refactor_output.DescribeStackRefactorOutput":
        """<p>Describes the stack refactor status.</p>

        Args:
            stack_refactor_id: <p>The ID associated with the stack refactor created from the <a>CreateStackRefactor</a> action.</p>

        Raises:
            capo_cloudformation.errors.stack_refactor_not_found_exception.StackRefactorNotFoundException: <p>The specified stack refactor can't be found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_refactor_input.DescribeStackRefactorInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_refactor_output.DescribeStackRefactorOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_refactor

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_refactor.describe_stack_refactor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_refactor_input.DescribeStackRefactorInput = {}
        if stack_refactor_id is not None:
            input_["stack_refactor_id"] = stack_refactor_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stack_resource(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        logical_resource_id: Optional[
            "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
        ] = None,
    ) -> "capo_cloudformation.types.describe_stack_resource_output.DescribeStackResourceOutput":
        """<p>Returns a description of the specified resource in the specified stack.</p> <p>For deleted stacks, DescribeStackResource returns resource information for up to 90 days after the stack has been deleted.</p>

        Args:
            stack_name: <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>
            logical_resource_id: <p>The logical name of the resource as specified in the template.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_resource_input.DescribeStackResourceInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_resource_output.DescribeStackResourceOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_resource

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_resource.describe_stack_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_resource_input.DescribeStackResourceInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stack_resource_drifts(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        stack_resource_drift_status_filters: Optional[
            "capo_cloudformation.types.stack_resource_drift_status_filters.StackResourceDriftStatusFilters"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.boxed_max_results.BoxedMaxResults"
        ] = None,
    ) -> "capo_cloudformation.types.describe_stack_resource_drifts_output.DescribeStackResourceDriftsOutput":
        """<p>Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.</p> <p>For a given stack, there will be one <code>StackResourceDrift</code> for each stack resource that has been checked for drift. Resources that haven't yet been checked for drift aren't included. Resources that don't currently support drift detection aren't checked, and so not included. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a>.</p> <p>Use <a>DetectStackResourceDrift</a> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all supported resources for a given stack.</p>

        Args:
            stack_name: <p>The name of the stack for which you want drift information.</p>
            stack_resource_drift_status_filters: <p>The resource drift status values to use as filters for the resource drift results returned.</p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> <li> <p> <code>UNKNOWN</code>: CloudFormation could not run drift detection for the resource.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_resource_drifts_input.DescribeStackResourceDriftsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_resource_drifts_output.DescribeStackResourceDriftsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_resource_drifts

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_resource_drifts.describe_stack_resource_drifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_resource_drifts_input.DescribeStackResourceDriftsInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if stack_resource_drift_status_filters is not None:
            input_["stack_resource_drift_status_filters"] = (
                stack_resource_drift_status_filters
            )
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

    def iter_describe_stack_resource_drifts(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        stack_resource_drift_status_filters: Optional[
            "capo_cloudformation.types.stack_resource_drift_status_filters.StackResourceDriftStatusFilters"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.boxed_max_results.BoxedMaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.describe_stack_resource_drifts_output.DescribeStackResourceDriftsOutput]":
        _token = next_token
        while True:
            _response = self.describe_stack_resource_drifts(
                config_overrides=config_overrides,
                stack_name=stack_name,
                stack_resource_drift_status_filters=stack_resource_drift_status_filters,
                next_token=_token,
                max_results=max_results,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def describe_stack_resources(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        logical_resource_id: Optional[
            "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
        ] = None,
        physical_resource_id: Optional[
            "capo_cloudformation.types.physical_resource_id.PhysicalResourceId"
        ] = None,
    ) -> "capo_cloudformation.types.describe_stack_resources_output.DescribeStackResourcesOutput":
        """<p>Returns Amazon Web Services resource descriptions for running and deleted stacks. If <code>StackName</code> is specified, all the associated resources that are part of the stack are returned. If <code>PhysicalResourceId</code> is specified, the associated resources of the stack that the resource belongs to are returned.</p> <note> <p>Only the first 100 resources will be returned. If your stack has more resources than this, you should use <code>ListStackResources</code> instead.</p> </note> <p>For deleted stacks, <code>DescribeStackResources</code> returns resource information for up to 90 days after the stack has been deleted.</p> <p>You must specify either <code>StackName</code> or <code>PhysicalResourceId</code>, but not both. In addition, you can specify <code>LogicalResourceId</code> to filter the returned result. For more information about resources, the <code>LogicalResourceId</code> and <code>PhysicalResourceId</code>, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/">CloudFormation User Guide</a>.</p> <note> <p>A <code>ValidationError</code> is returned if you specify both <code>StackName</code> and <code>PhysicalResourceId</code> in the same request.</p> </note>

        Args:
            stack_name: <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul> <p>Required: Conditional. If you don't specify <code>StackName</code>, you must specify <code>PhysicalResourceId</code>.</p>
            logical_resource_id: <p>The logical name of the resource as specified in the template.</p>
            physical_resource_id: <p>The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.</p> <p>For example, for an Amazon Elastic Compute Cloud (EC2) instance, <code>PhysicalResourceId</code> corresponds to the <code>InstanceId</code>. You can pass the EC2 <code>InstanceId</code> to <code>DescribeStackResources</code> to find which stack the instance belongs to and what other resources are part of the stack.</p> <p>Required: Conditional. If you don't specify <code>PhysicalResourceId</code>, you must specify <code>StackName</code>.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_resources_input.DescribeStackResourcesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_resources_output.DescribeStackResourcesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_resources

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_resources.describe_stack_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_resources_input.DescribeStackResourcesInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id
        if physical_resource_id is not None:
            input_["physical_resource_id"] = physical_resource_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stacks(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.describe_stacks_output.DescribeStacksOutput":
        """<p>Returns the description for the specified stack; if no stack name was specified, then it returns the description for all the stacks created. For more information about a stack's event history, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stack-resource-configuration-complete.html">Understand CloudFormation stack creation events</a> in the <i>CloudFormation User Guide</i>.</p> <note> <p>If the stack doesn't exist, a <code>ValidationError</code> is returned.</p> </note>

        Args:
            stack_name: <note> <p>If you don't pass a parameter to <code>StackName</code>, the API returns a response that describes all resources in the account, which can impact performance. This requires <code>ListStacks</code> and <code>DescribeStacks</code> permissions.</p> <p>Consider using the <a>ListStacks</a> API if you're not passing a parameter to <code>StackName</code>.</p> <p>The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:</p> <p>{ "Version": "2012-10-17", "Statement": [{ "Effect": "Deny", "Action": "cloudformation:DescribeStacks", "NotResource": "arn:aws:cloudformation:*:*:stack/*/*" }] }</p> </note> <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stacks_input.DescribeStacksInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stacks_output.DescribeStacksOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stacks

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stacks.describe_stacks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stacks_input.DescribeStacksInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_describe_stacks(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.stack.Stack]":
        _token = next_token
        while True:
            _response = self.describe_stacks(
                config_overrides=config_overrides,
                stack_name=stack_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("stacks",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def wait_until_stack_exists(
        self,
        *,
        max_wait_time: float,
        min_delay: float = 5,
        max_delay: float = 120,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.describe_stacks_output.DescribeStacksOutput":
        """Wait for stack_exists.

        Args:
            max_wait_time: Maximum total seconds to wait before raising WaiterTimeoutError.
            min_delay: Minimum seconds between operation attempts (spec default 2).
            max_delay: Maximum seconds between operation attempts (spec default 120).
            stack_name: <note> <p>If you don't pass a parameter to <code>StackName</code>, the API returns a response that describes all resources in the account, which can impact performance. This requires <code>ListStacks</code> and <code>DescribeStacks</code> permissions.</p> <p>Consider using the <a>ListStacks</a> API if you're not passing a parameter to <code>StackName</code>.</p> <p>The IAM policy below can be added to IAM policies when you want to limit resource-level permissions and avoid returning a response when no parameter is sent in the request:</p> <p>{ "Version": "2012-10-17", "Statement": [{ "Effect": "Deny", "Action": "cloudformation:DescribeStacks", "NotResource": "arn:aws:cloudformation:*:*:stack/*/*" }] }</p> </note> <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
        """
        start = time.monotonic()
        attempt = 0
        while True:
            op_output: "capo_cloudformation.types.describe_stacks_output.DescribeStacksOutput | None" = None
            op_error: ServiceError | None = None
            try:
                op_output = self.describe_stacks(  # noqa: F841
                    config_overrides=config_overrides,
                    stack_name=stack_name,
                    next_token=next_token,
                )
            except ServiceError as e:
                op_error = e
            if op_output is not None:
                return op_output
            elif op_error is not None and op_error.code == "ValidationError":
                pass

            elapsed = time.monotonic() - start
            remaining = max_wait_time - elapsed
            if remaining <= 0:
                raise WaiterTimeoutError("stack_exists", max_wait_time)
            delay = min(max_delay, min_delay * (2**attempt))
            delay = min(delay, remaining)
            time.sleep(delay)
            attempt += 1

    def describe_stack_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.describe_stack_set_output.DescribeStackSetOutput":
        """<p>Returns the description of the specified StackSet.</p> <note> <p>This API provides <i>strongly consistent</i> reads meaning it will always return the most up-to-date data.</p> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet whose description you want.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_set_input.DescribeStackSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_set_output.DescribeStackSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_set.describe_stack_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_set_input.DescribeStackSetInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_stack_set_operation(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.describe_stack_set_operation_output.DescribeStackSetOperationOutput":
        """<p>Returns the description of the specified StackSet operation.</p> <note> <p>This API provides <i>strongly consistent</i> reads meaning it will always return the most up-to-date data.</p> </note>

        Args:
            stack_set_name: <p>The name or the unique stack ID of the StackSet for the stack operation.</p>
            operation_id: <p>The unique ID of the StackSet operation.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.operation_not_found_exception.OperationNotFoundException: <p>The specified ID refers to an operation that doesn't exist.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_stack_set_operation_input.DescribeStackSetOperationInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_stack_set_operation_output.DescribeStackSetOperationOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_stack_set_operation

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_stack_set_operation.describe_stack_set_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_stack_set_operation_input.DescribeStackSetOperationInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if operation_id is not None:
            input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_type(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        arn: Optional["capo_cloudformation.types.type_arn.TypeArn"] = None,
        version_id: Optional[
            "capo_cloudformation.types.type_version_id.TypeVersionId"
        ] = None,
        publisher_id: Optional[
            "capo_cloudformation.types.publisher_id.PublisherId"
        ] = None,
        public_version_number: Optional[
            "capo_cloudformation.types.public_version_number.PublicVersionNumber"
        ] = None,
    ) -> "capo_cloudformation.types.describe_type_output.DescribeTypeOutput":
        """<p>Returns detailed information about an extension from the CloudFormation registry in your current account and Region.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html">Edit configuration data for extensions in your account</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            type: <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type_name: <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            arn: <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            version_id: <p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p> <p>If you specify a <code>VersionId</code>, <code>DescribeType</code> returns information about that specific extension version. Otherwise, it returns information about the default extension version.</p>
            publisher_id: <p>The publisher ID of the extension publisher.</p> <p>Extensions provided by Amazon Web Services are not assigned a publisher ID.</p>
            public_version_number: <p>The version number of a public third-party extension.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_type_input.DescribeTypeInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_type_output.DescribeTypeOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_type

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_type.describe_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_type_input.DescribeTypeInput = {}
        if type is not None:
            input_["type"] = type
        if type_name is not None:
            input_["type_name"] = type_name
        if arn is not None:
            input_["arn"] = arn
        if version_id is not None:
            input_["version_id"] = version_id
        if publisher_id is not None:
            input_["publisher_id"] = publisher_id
        if public_version_number is not None:
            input_["public_version_number"] = public_version_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def describe_type_registration(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        registration_token: Optional[
            "capo_cloudformation.types.registration_token.RegistrationToken"
        ] = None,
    ) -> "capo_cloudformation.types.describe_type_registration_output.DescribeTypeRegistrationOutput":
        """<p>Returns information about an extension's registration, including its current status and type and version identifiers.</p> <p>When you initiate a registration request using <a>RegisterType</a>, you can then use <a>DescribeTypeRegistration</a> to monitor the progress of that registration request.</p> <p>Once the registration request has completed, use <a>DescribeType</a> to return detailed information about an extension.</p>

        Args:
            registration_token: <p>The identifier for this registration request.</p> <p>This registration token is generated by CloudFormation when you initiate a registration request using <a>RegisterType</a>.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.describe_type_registration_input.DescribeTypeRegistrationInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.describe_type_registration_output.DescribeTypeRegistrationOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.describe_type_registration

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.describe_type_registration.describe_type_registration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.describe_type_registration_input.DescribeTypeRegistrationInput = {}
        if registration_token is not None:
            input_["registration_token"] = registration_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_stack_drift(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        logical_resource_ids: Optional[
            "capo_cloudformation.types.logical_resource_ids.LogicalResourceIds"
        ] = None,
    ) -> "capo_cloudformation.types.detect_stack_drift_output.DetectStackDriftOutput":
        """<p>Detects whether a stack's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. For each resource in the stack that supports drift detection, CloudFormation compares the actual configuration of the resource with its expected template configuration. Only resource properties explicitly defined in the stack template are checked for drift. A stack is considered to have drifted if one or more of its resources differ from their expected template configurations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detect unmanaged configuration changes to stacks and resources with drift detection</a>.</p> <p>Use <code>DetectStackDrift</code> to detect drift on all supported resources for a given stack, or <a>DetectStackResourceDrift</a> to detect drift on individual resources.</p> <p>For a list of stack resources that currently support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a>.</p> <p> <code>DetectStackDrift</code> can take up to several minutes, depending on the number of resources contained within the stack. Use <a>DescribeStackDriftDetectionStatus</a> to monitor the progress of a detect stack drift operation. Once the drift detection operation has completed, use <a>DescribeStackResourceDrifts</a> to return drift information about the stack and its resources.</p> <p>When detecting drift on a stack, CloudFormation doesn't detect drift on any nested stacks belonging to that stack. Perform <code>DetectStackDrift</code> directly on the nested stack itself.</p>

        Args:
            stack_name: <p>The name of the stack for which you want to detect drift.</p>
            logical_resource_ids: <p>The logical names of any resources you want to use as filters.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.detect_stack_drift_input.DetectStackDriftInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.detect_stack_drift_output.DetectStackDriftOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.detect_stack_drift

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.detect_stack_drift.detect_stack_drift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.detect_stack_drift_input.DetectStackDriftInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if logical_resource_ids is not None:
            input_["logical_resource_ids"] = logical_resource_ids

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_stack_resource_drift(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        logical_resource_id: Optional[
            "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
        ] = None,
    ) -> "capo_cloudformation.types.detect_stack_resource_drift_output.DetectStackResourceDriftOutput":
        """<p>Returns information about whether a resource's actual configuration differs, or has <i>drifted</i>, from its expected configuration, as defined in the stack template and any values specified as template parameters. This information includes actual and expected property values for resources in which CloudFormation detects drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information about stack and resource drift, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html">Detect unmanaged configuration changes to stacks and resources with drift detection</a>.</p> <p>Use <code>DetectStackResourceDrift</code> to detect drift on individual resources, or <a>DetectStackDrift</a> to detect drift on all resources in a given stack that support drift detection.</p> <p>Resources that don't currently support drift detection can't be checked. For a list of resources that support drift detection, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resource type support for imports and drift detection</a>.</p>

        Args:
            stack_name: <p>The name of the stack to which the resource belongs.</p>
            logical_resource_id: <p>The logical name of the resource for which to return drift information.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.detect_stack_resource_drift_input.DetectStackResourceDriftInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.detect_stack_resource_drift_output.DetectStackResourceDriftOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.detect_stack_resource_drift

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.detect_stack_resource_drift.detect_stack_resource_drift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.detect_stack_resource_drift_input.DetectStackResourceDriftInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def detect_stack_set_drift(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
        ] = None,
        operation_preferences: Optional[
            "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.detect_stack_set_drift_output.DetectStackSetDriftOutput":
        """<p>Detect drift on a StackSet. When CloudFormation performs drift detection on a StackSet, it performs drift detection on the stack associated with each stack instance in the StackSet. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-drift.html">Performing drift detection on CloudFormation StackSets</a>.</p> <p> <code>DetectStackSetDrift</code> returns the <code>OperationId</code> of the StackSet drift detection operation. Use this operation id with <a>DescribeStackSetOperation</a> to monitor the progress of the drift detection operation. The drift detection operation may take some time, depending on the number of stack instances included in the StackSet, in addition to the number of resources included in each stack.</p> <p>Once the operation has completed, use the following actions to return drift information:</p> <ul> <li> <p>Use <a>DescribeStackSet</a> to return detailed information about the stack set, including detailed information about the last <i>completed</i> drift operation performed on the StackSet. (Information about drift operations that are in progress isn't included.)</p> </li> <li> <p>Use <a>ListStackInstances</a> to return a list of stack instances belonging to the StackSet, including the drift status and last drift time checked of each instance.</p> </li> <li> <p>Use <a>DescribeStackInstance</a> to return detailed information about a specific stack instance, including its drift status and last drift time checked.</p> </li> </ul> <p>You can only run a single drift detection operation on a given StackSet at one time.</p> <p>To stop a drift detection StackSet operation, use <a>StopStackSetOperation</a>.</p>

        Args:
            stack_set_name: <p>The name of the StackSet on which to perform the drift detection operation.</p>
            operation_preferences: <p>The user-specified preferences for how CloudFormation performs a StackSet operation.</p> <p>For more information about maximum concurrent accounts and failure tolerance, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">StackSet operation options</a>.</p>
            operation_id: <p> <i>The ID of the StackSet operation.</i> </p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException: <p>Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.detect_stack_set_drift_input.DetectStackSetDriftInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.detect_stack_set_drift_output.DetectStackSetDriftOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.detect_stack_set_drift

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.detect_stack_set_drift.detect_stack_set_drift(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.detect_stack_set_drift_input.DetectStackSetDriftInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if operation_preferences is not None:
            input_["operation_preferences"] = operation_preferences
        if operation_id is None:
            operation_id = str(uuid.uuid4())
        input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def estimate_template_cost(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
        parameters: Optional["capo_cloudformation.types.parameters.Parameters"] = None,
    ) -> "capo_cloudformation.types.estimate_template_cost_output.EstimateTemplateCostOutput":
        """<p>Returns the estimated monthly cost of a template. The return value is an Amazon Web Services Simple Monthly Calculator URL with a query string that describes the resources required to run the template.</p>

        Args:
            template_body: <p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must pass <code>TemplateBody</code> or <code>TemplateURL</code>. If both are passed, only <code>TemplateBody</code> is used.</p>
            template_url: <p>The URL of a file that contains the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>
            parameters: <p>A list of <code>Parameter</code> structures that specify input parameters.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.estimate_template_cost_input.EstimateTemplateCostInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.estimate_template_cost_output.EstimateTemplateCostOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.estimate_template_cost

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.estimate_template_cost.estimate_template_cost(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.estimate_template_cost_input.EstimateTemplateCostInput = {}
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url
        if parameters is not None:
            input_["parameters"] = parameters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_change_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        disable_rollback: Optional[
            "capo_cloudformation.types.disable_rollback.DisableRollback"
        ] = None,
        retain_except_on_create: Optional[
            "capo_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
        ] = None,
    ) -> "capo_cloudformation.types.execute_change_set_output.ExecuteChangeSetOutput":
        """<p>Updates a stack using the input information that was provided when the specified change set was created. After the call successfully completes, CloudFormation starts updating the stack. Use the <a>DescribeStacks</a> action to view the status of the update.</p> <p>When you execute a change set, CloudFormation deletes all other change sets associated with the stack because they aren't valid for the updated stack.</p> <p>If a stack policy is associated with the stack, CloudFormation enforces the policy during the update. You can't specify a temporary stack policy that overrides the current policy.</p> <p>To create a change set for the entire stack hierarchy, <code>IncludeNestedStacks</code> must have been set to <code>True</code>.</p>

        Args:
            change_set_name: <p>The name or Amazon Resource Name (ARN) of the change set that you want use to update the specified stack.</p>
            stack_name: <p>If you specified the name of a change set, specify the stack name or Amazon Resource Name (ARN) that's associated with the change set you want to execute.</p>
            client_request_token: <p>A unique identifier for this <code>ExecuteChangeSet</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to execute a change set to update a stack with the same name. You might retry <code>ExecuteChangeSet</code> requests to ensure that CloudFormation successfully received them.</p>
            disable_rollback: <p>Preserves the state of previously provisioned resources when an operation fails. This parameter can't be specified when the <code>OnStackFailure</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html">CreateChangeSet</a> API operation was specified.</p> <ul> <li> <p> <code>True</code> - if the stack creation fails, do nothing. This is equivalent to specifying <code>DO_NOTHING</code> for the <code>OnStackFailure</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html">CreateChangeSet</a> API operation.</p> </li> <li> <p> <code>False</code> - if the stack creation fails, roll back the stack. This is equivalent to specifying <code>ROLLBACK</code> for the <code>OnStackFailure</code> parameter to the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html">CreateChangeSet</a> API operation.</p> </li> </ul> <p>Default: <code>True</code> </p>
            retain_except_on_create: <p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>

        Raises:
            capo_cloudformation.errors.change_set_not_found_exception.ChangeSetNotFoundException: <p>The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the <code>ListChangeSets</code> operation.</p>
            capo_cloudformation.errors.insufficient_capabilities_exception.InsufficientCapabilitiesException: <p>The template contains resources with capabilities that weren't specified in the Capabilities parameter.</p>
            capo_cloudformation.errors.invalid_change_set_status_exception.InvalidChangeSetStatusException: <p>The specified change set can't be used to update the stack. For example, the change set status might be <code>CREATE_IN_PROGRESS</code>, or the stack status might be <code>UPDATE_IN_PROGRESS</code>.</p>
            capo_cloudformation.errors.token_already_exists_exception.TokenAlreadyExistsException: <p>A client request token already exists.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.execute_change_set_input.ExecuteChangeSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.execute_change_set_output.ExecuteChangeSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.execute_change_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.execute_change_set.execute_change_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.execute_change_set_input.ExecuteChangeSetInput = {}
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if disable_rollback is not None:
            input_["disable_rollback"] = disable_rollback
        if retain_except_on_create is not None:
            input_["retain_except_on_create"] = retain_except_on_create

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def execute_stack_refactor(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_refactor_id: Optional[
            "capo_cloudformation.types.stack_refactor_id.StackRefactorId"
        ] = None,
    ) -> None:
        """<p>Executes the stack refactor operation.</p>

        Args:
            stack_refactor_id: <p>The ID associated with the stack refactor created from the <a>CreateStackRefactor</a> action.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.execute_stack_refactor_input.ExecuteStackRefactorInput]",
        ) -> OperationResponse[None]:
            import capo_cloudformation._operations.cloud_formation.execute_stack_refactor

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.execute_stack_refactor.execute_stack_refactor(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.execute_stack_refactor_input.ExecuteStackRefactorInput = {}
        if stack_refactor_id is not None:
            input_["stack_refactor_id"] = stack_refactor_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_generated_template(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        format: Optional[
            "capo_cloudformation.types.template_format.TemplateFormat"
        ] = None,
        generated_template_name: Optional[
            "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
        ] = None,
    ) -> "capo_cloudformation.types.get_generated_template_output.GetGeneratedTemplateOutput":
        """<p>Retrieves a generated template. If the template is in an <code>InProgress</code> or <code>Pending</code> status then the template returned will be the template when the template was last in a <code>Complete</code> status. If the template has not yet been in a <code>Complete</code> status then an empty template will be returned.</p>

        Args:
            format: <p>The language to use to retrieve for the generated template. Supported values are:</p> <ul> <li> <p> <code>JSON</code> </p> </li> <li> <p> <code>YAML</code> </p> </li> </ul>
            generated_template_name: <p>The name or Amazon Resource Name (ARN) of the generated template. The format is <code>arn:${Partition}:cloudformation:${Region}:${Account}:generatedtemplate/${Id}</code>. For example, <code>arn:aws:cloudformation:<i>us-east-1</i>:<i>123456789012</i>:generatedtemplate/<i>2e8465c1-9a80-43ea-a3a3-4f2d692fe6dc</i> </code>.</p>

        Raises:
            capo_cloudformation.errors.generated_template_not_found_exception.GeneratedTemplateNotFoundException: <p>The generated template was not found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To get a generated template in JSON format
            This example gets a generated template ins JSON format.

            >>> client.get_generated_template(generated_template_name='JazzyTemplate')
            To get a generated template in YAML format
            This example gets a generated template in YAML format.

            >>> client.get_generated_template(generated_template_name='JazzyTemplate', format='YAML')
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.get_generated_template_input.GetGeneratedTemplateInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.get_generated_template_output.GetGeneratedTemplateOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.get_generated_template

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.get_generated_template.get_generated_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.get_generated_template_input.GetGeneratedTemplateInput = {}
        if format is not None:
            input_["format"] = format
        if generated_template_name is not None:
            input_["generated_template_name"] = generated_template_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_hook_result(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        hook_result_id: Optional[
            "capo_cloudformation.types.hook_invocation_id.HookInvocationId"
        ] = None,
    ) -> "capo_cloudformation.types.get_hook_result_output.GetHookResultOutput":
        """<p>Retrieves detailed information and remediation guidance for a Hook invocation result.</p> <p>If the Hook uses a KMS key to encrypt annotations, callers of the <code>GetHookResult</code> operation must have <code>kms:Decrypt</code> permissions. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-kms-key-policy.html">KMS key policy and permissions for encrypting CloudFormation Hooks results at rest</a> in the <i>CloudFormation Hooks User Guide</i>.</p>

        Args:
            hook_result_id: <p>The unique identifier (ID) of the Hook invocation result that you want details about. You can get the ID from the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ListHookResults.html">ListHookResults</a> operation.</p>

        Raises:
            capo_cloudformation.errors.hook_result_not_found_exception.HookResultNotFoundException: <p>The specified target doesn't have any requested Hook invocations.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.get_hook_result_input.GetHookResultInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.get_hook_result_output.GetHookResultOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.get_hook_result

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.get_hook_result.get_hook_result(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.get_hook_result_input.GetHookResultInput = {}
        if hook_result_id is not None:
            input_["hook_result_id"] = hook_result_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_stack_policy(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
    ) -> "capo_cloudformation.types.get_stack_policy_output.GetStackPolicyOutput":
        """<p>Returns the stack policy for a specified stack. If a stack doesn't have a policy, a null value is returned.</p>

        Args:
            stack_name: <p>The name or unique stack ID that's associated with the stack whose policy you want to get.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.get_stack_policy_input.GetStackPolicyInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.get_stack_policy_output.GetStackPolicyOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.get_stack_policy

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.get_stack_policy.get_stack_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.get_stack_policy_input.GetStackPolicyInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_template(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        change_set_name: Optional[
            "capo_cloudformation.types.change_set_name_or_id.ChangeSetNameOrId"
        ] = None,
        template_stage: Optional[
            "capo_cloudformation.types.template_stage.TemplateStage"
        ] = None,
    ) -> "capo_cloudformation.types.get_template_output.GetTemplateOutput":
        """<p>Returns the template body for a specified stack. You can get the template for running or deleted stacks.</p> <p>For deleted stacks, <code>GetTemplate</code> returns the template for up to 90 days after the stack has been deleted.</p> <note> <p>If the template doesn't exist, a <code>ValidationError</code> is returned.</p> </note>

        Args:
            stack_name: <p>The name or the unique stack ID that's associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>
            change_set_name: <p>The name or Amazon Resource Name (ARN) of a change set for which CloudFormation returns the associated template. If you specify a name, you must also specify the <code>StackName</code>.</p>
            template_stage: <p>For templates that include transforms, the stage of the template that CloudFormation returns. To get the user-submitted template, specify <code>Original</code>. To get the template after CloudFormation has processed all transforms, specify <code>Processed</code>.</p> <p>If the template doesn't include transforms, <code>Original</code> and <code>Processed</code> return the same template. By default, CloudFormation specifies <code>Processed</code>.</p>

        Raises:
            capo_cloudformation.errors.change_set_not_found_exception.ChangeSetNotFoundException: <p>The specified change set name or ID doesn't exit. To view valid change sets for a stack, use the <code>ListChangeSets</code> operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.get_template_input.GetTemplateInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.get_template_output.GetTemplateOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.get_template

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.get_template.get_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.get_template_input.GetTemplateInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if change_set_name is not None:
            input_["change_set_name"] = change_set_name
        if template_stage is not None:
            input_["template_stage"] = template_stage

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def get_template_summary(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
        template_summary_config: Optional[
            "capo_cloudformation.types.template_summary_config.TemplateSummaryConfig"
        ] = None,
    ) -> (
        "capo_cloudformation.types.get_template_summary_output.GetTemplateSummaryOutput"
    ):
        """<p>Returns information about a new or existing template. The <code>GetTemplateSummary</code> action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or StackSet.</p> <p>You can use the <code>GetTemplateSummary</code> action when you submit a template, or you can get template information for a StackSet, or a running or deleted stack.</p> <p>For deleted stacks, <code>GetTemplateSummary</code> returns the template information for up to 90 days after the stack has been deleted. If the template doesn't exist, a <code>ValidationError</code> is returned.</p>

        Args:
            template_body: <p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
            template_url: <p>The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
            stack_name: <p>The name or the stack ID that's associated with the stack, which aren't always interchangeable. For running stacks, you can specify either the stack's name or its unique stack ID. For deleted stack, you must specify the unique stack ID.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
            stack_set_name: <p>The name or unique ID of the StackSet from which the stack was created.</p> <p>Conditional: You must specify only one of the following parameters: <code>StackName</code>, <code>StackSetName</code>, <code>TemplateBody</code>, or <code>TemplateURL</code>.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
            template_summary_config: <p>Specifies options for the <code>GetTemplateSummary</code> API action.</p>

        Raises:
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.get_template_summary_input.GetTemplateSummaryInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.get_template_summary_output.GetTemplateSummaryOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.get_template_summary

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.get_template_summary.get_template_summary(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.get_template_summary_input.GetTemplateSummaryInput = {}
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if call_as is not None:
            input_["call_as"] = call_as
        if template_summary_config is not None:
            input_["template_summary_config"] = template_summary_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def import_stacks_to_stack_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
        ] = None,
        stack_ids: Optional[
            "capo_cloudformation.types.stack_id_list.StackIdList"
        ] = None,
        stack_ids_url: Optional[
            "capo_cloudformation.types.stack_ids_url.StackIdsUrl"
        ] = None,
        organizational_unit_ids: Optional[
            "capo_cloudformation.types.organizational_unit_id_list.OrganizationalUnitIdList"
        ] = None,
        operation_preferences: Optional[
            "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput":
        """<p>Import existing stacks into a new StackSets. Use the stack import operation to import up to 10 stacks into a new StackSet in the same account as the source stack or in a different administrator account and Region, by specifying the stack ID of the stack you intend to import.</p>

        Args:
            stack_set_name: <p>The name of the StackSet. The name must be unique in the Region where you create your StackSet.</p>
            stack_ids: <p>The IDs of the stacks you are importing into a StackSet. You import up to 10 stacks per StackSet at a time.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>
            stack_ids_url: <p>The Amazon S3 URL which contains list of stack ids to be inputted.</p> <p>Specify either <code>StackIds</code> or <code>StackIdsUrl</code>.</p>
            organizational_unit_ids: <p>The list of OU ID's to which the imported stacks must be mapped as deployment targets.</p>
            operation_preferences: <p>The user-specified preferences for how CloudFormation performs a StackSet operation.</p> <p>For more information about maximum concurrent accounts and failure tolerance, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-concepts.html#stackset-ops-options">StackSet operation options</a>.</p>
            operation_id: <p>A unique, user defined, identifier for the StackSet operation.</p>
            call_as: <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>For service managed StackSets, specify <code>DELEGATED_ADMIN</code>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.limit_exceeded_exception.LimitExceededException: <p>The quota for the resource has already been reached.</p> <p>For information about resource and stack limitations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
            capo_cloudformation.errors.operation_id_already_exists_exception.OperationIdAlreadyExistsException: <p>The specified operation ID already exists.</p>
            capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException: <p>Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.</p>
            capo_cloudformation.errors.stack_not_found_exception.StackNotFoundException: <p>The specified stack ARN doesn't exist or stack doesn't exist corresponding to the ARN in input.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.stale_request_exception.StaleRequestException: <p>Another operation has been performed on this StackSet since the specified operation was performed.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.import_stacks_to_stack_set_input.ImportStacksToStackSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.import_stacks_to_stack_set_output.ImportStacksToStackSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.import_stacks_to_stack_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.import_stacks_to_stack_set.import_stacks_to_stack_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.import_stacks_to_stack_set_input.ImportStacksToStackSetInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if stack_ids is not None:
            input_["stack_ids"] = stack_ids
        if stack_ids_url is not None:
            input_["stack_ids_url"] = stack_ids_url
        if organizational_unit_ids is not None:
            input_["organizational_unit_ids"] = organizational_unit_ids
        if operation_preferences is not None:
            input_["operation_preferences"] = operation_preferences
        if operation_id is None:
            operation_id = str(uuid.uuid4())
        input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_change_sets(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.list_change_sets_output.ListChangeSetsOutput":
        """<p>Returns the ID and status of each active change set for a stack. For example, CloudFormation lists change sets that are in the <code>CREATE_IN_PROGRESS</code> or <code>CREATE_PENDING</code> state.</p>

        Args:
            stack_name: <p>The name or the Amazon Resource Name (ARN) of the stack for which you want to list change sets.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_change_sets_input.ListChangeSetsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_change_sets_output.ListChangeSetsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_change_sets

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_change_sets.list_change_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_change_sets_input.ListChangeSetsInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_change_sets(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.change_set_summary.ChangeSetSummary]":
        _token = next_token
        while True:
            _response = self.list_change_sets(
                config_overrides=config_overrides,
                stack_name=stack_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_exports(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.list_exports_output.ListExportsOutput":
        """<p>Lists all exported output values in the account and Region in which you call this action. Use this action to see the exported output values that you can import into other stacks. To import values, use the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html"> Fn::ImportValue</a> function.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-exports.html">Get exported outputs from a deployed CloudFormation stack</a>.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_exports_input.ListExportsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_exports_output.ListExportsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_exports

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_exports.list_exports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_exports_input.ListExportsInput = {}
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
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.export.Export]":
        _token = next_token
        while True:
            _response = self.list_exports(
                config_overrides=config_overrides,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("exports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_generated_templates(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_cloudformation.types.list_generated_templates_output.ListGeneratedTemplatesOutput":
        """<p>Lists your generated templates in this Region.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. By default the <code>ListGeneratedTemplates</code> API action will return at most 50 results in each response. The maximum value is 100.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_generated_templates_input.ListGeneratedTemplatesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_generated_templates_output.ListGeneratedTemplatesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_generated_templates

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_generated_templates.list_generated_templates(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_generated_templates_input.ListGeneratedTemplatesInput = {}
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

    def iter_list_generated_templates(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.template_summary.TemplateSummary]":
        _token = next_token
        while True:
            _response = self.list_generated_templates(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_hook_results(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        target_type: Optional[
            "capo_cloudformation.types.list_hook_results_target_type.ListHookResultsTargetType"
        ] = None,
        target_id: Optional[
            "capo_cloudformation.types.hook_result_id.HookResultId"
        ] = None,
        type_arn: Optional[
            "capo_cloudformation.types.hook_type_arn.HookTypeArn"
        ] = None,
        status: Optional["capo_cloudformation.types.hook_status.HookStatus"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.list_hook_results_output.ListHookResultsOutput":
        """<p>Returns summaries of invoked Hooks. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-view-invocations.html">View invocation summaries for CloudFormation Hooks</a> in the <i>CloudFormation Hooks User Guide</i>.</p> <p>This operation supports the following parameter combinations:</p> <ul> <li> <p>No parameters: Returns all Hook invocation summaries.</p> </li> <li> <p> <code>TypeArn</code> only: Returns summaries for a specific Hook.</p> </li> <li> <p> <code>TypeArn</code> and <code>Status</code>: Returns summaries for a specific Hook filtered by status.</p> </li> <li> <p> <code>TargetId</code> and <code>TargetType</code>: Returns summaries for a specific Hook invocation target.</p> </li> </ul>

        Args:
            target_type: <p>Filters results by target type. Currently, only <code>CHANGE_SET</code> and <code>CLOUD_CONTROL</code> are supported filter options.</p> <p>Required when <code>TargetId</code> is specified and cannot be used otherwise.</p>
            target_id: <p>Filters results by the unique identifier of the target the Hook was invoked against.</p> <p>For change sets, this is the change set ARN. When the target is a Cloud Control API operation, this value must be the <code>HookRequestToken</code> returned by the Cloud Control API request. For more information on the <code>HookRequestToken</code>, see <a href="https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ProgressEvent.html">ProgressEvent</a>.</p> <p>Required when <code>TargetType</code> is specified and cannot be used otherwise.</p>
            type_arn: <p>Filters results by the ARN of the Hook. Can be used alone or in combination with <code>Status</code>.</p>
            status: <p>Filters results by the status of Hook invocations. Can only be used in combination with <code>TypeArn</code>. Valid values are:</p> <ul> <li> <p> <code>HOOK_IN_PROGRESS</code>: The Hook is currently running.</p> </li> <li> <p> <code>HOOK_COMPLETE_SUCCEEDED</code>: The Hook completed successfully.</p> </li> <li> <p> <code>HOOK_COMPLETE_FAILED</code>: The Hook completed but failed validation.</p> </li> <li> <p> <code>HOOK_FAILED</code>: The Hook encountered an error during execution.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.hook_result_not_found_exception.HookResultNotFoundException: <p>The specified target doesn't have any requested Hook invocations.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_hook_results_input.ListHookResultsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_hook_results_output.ListHookResultsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_hook_results

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_hook_results.list_hook_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_hook_results_input.ListHookResultsInput = {}
        if target_type is not None:
            input_["target_type"] = target_type
        if target_id is not None:
            input_["target_id"] = target_id
        if type_arn is not None:
            input_["type_arn"] = type_arn
        if status is not None:
            input_["status"] = status
        if next_token is not None:
            input_["next_token"] = next_token

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
        config_overrides: Optional[CloudFormationClientConfig] = None,
        export_name: Optional[
            "capo_cloudformation.types.export_name.ExportName"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.list_imports_output.ListImportsOutput":
        """<p>Lists all stacks that are importing an exported output value. To modify or remove an exported output value, first use this action to see which stacks are using it. To see the exported output values in your account, see <a>ListExports</a>.</p> <p>For more information about importing an exported output value, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-importvalue.html">Fn::ImportValue</a> function.</p>

        Args:
            export_name: <p>The name of the exported output value. CloudFormation returns the stack names that are importing this value.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_imports_input.ListImportsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_imports_output.ListImportsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_imports

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_imports.list_imports(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_imports_input.ListImportsInput = {}
        if export_name is not None:
            input_["export_name"] = export_name
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
        config_overrides: Optional[CloudFormationClientConfig] = None,
        export_name: Optional[
            "capo_cloudformation.types.export_name.ExportName"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_name.StackName]":
        _token = next_token
        while True:
            _response = self.list_imports(
                config_overrides=config_overrides,
                export_name=export_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("imports",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_scan_related_resources(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        resource_scan_id: Optional[
            "capo_cloudformation.types.resource_scan_id.ResourceScanId"
        ] = None,
        resources: Optional[
            "capo_cloudformation.types.scanned_resource_identifiers.ScannedResourceIdentifiers"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.boxed_max_results.BoxedMaxResults"
        ] = None,
    ) -> "capo_cloudformation.types.list_resource_scan_related_resources_output.ListResourceScanRelatedResourcesOutput":
        """<p>Lists the related resources for a list of resources from a resource scan. The response indicates whether each returned resource is already managed by CloudFormation.</p>

        Args:
            resource_scan_id: <p>The Amazon Resource Name (ARN) of the resource scan.</p>
            resources: <p>The list of resources for which you want to get the related resources. Up to 100 resources can be provided.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. By default the <code>ListResourceScanRelatedResources</code> API action will return up to 100 results in each response. The maximum value is 100.</p>

        Raises:
            capo_cloudformation.errors.resource_scan_in_progress_exception.ResourceScanInProgressException: <p>A resource scan is currently in progress. Only one can be run at a time for an account in a Region.</p>
            capo_cloudformation.errors.resource_scan_not_found_exception.ResourceScanNotFoundException: <p>The resource scan was not found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list resource scan related resources
            This example lists the resources related to the passed in resources

            >>> client.list_resource_scan_related_resources(resource_scan_id='arn:aws:cloudformation:us-east-1:123456789012:resourceScan/c19304f6-c4f1-4ff8-8e1f-35162e41d7e1', resources=[{'ResourceType': 'AWS::S3::Bucket', 'ResourceIdentifier': {'BucketName': 'jazz-bucket'}}, {'ResourceType': 'AWS::EC2::DHCPOptions', 'ResourceIdentifier': {'DhcpOptionsId': 'random-id123'}}])
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_resource_scan_related_resources_input.ListResourceScanRelatedResourcesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_resource_scan_related_resources_output.ListResourceScanRelatedResourcesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_resource_scan_related_resources

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_resource_scan_related_resources.list_resource_scan_related_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_resource_scan_related_resources_input.ListResourceScanRelatedResourcesInput = {}
        if resource_scan_id is not None:
            input_["resource_scan_id"] = resource_scan_id
        if resources is not None:
            input_["resources"] = resources
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

    def iter_list_resource_scan_related_resources(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        resource_scan_id: Optional[
            "capo_cloudformation.types.resource_scan_id.ResourceScanId"
        ] = None,
        resources: Optional[
            "capo_cloudformation.types.scanned_resource_identifiers.ScannedResourceIdentifiers"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.boxed_max_results.BoxedMaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.scanned_resource.ScannedResource]":
        _token = next_token
        while True:
            _response = self.list_resource_scan_related_resources(
                config_overrides=config_overrides,
                resource_scan_id=resource_scan_id,
                resources=resources,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("related_resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_scan_resources(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        resource_scan_id: Optional[
            "capo_cloudformation.types.resource_scan_id.ResourceScanId"
        ] = None,
        resource_identifier: Optional[
            "capo_cloudformation.types.resource_identifier.ResourceIdentifier"
        ] = None,
        resource_type_prefix: Optional[
            "capo_cloudformation.types.resource_type_prefix.ResourceTypePrefix"
        ] = None,
        tag_key: Optional["capo_cloudformation.types.tag_key.TagKey"] = None,
        tag_value: Optional["capo_cloudformation.types.tag_value.TagValue"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.resource_scanner_max_results.ResourceScannerMaxResults"
        ] = None,
    ) -> "capo_cloudformation.types.list_resource_scan_resources_output.ListResourceScanResourcesOutput":
        """<p>Lists the resources from a resource scan. The results can be filtered by resource identifier, resource type prefix, tag key, and tag value. Only resources that match all specified filters are returned. The response indicates whether each returned resource is already managed by CloudFormation.</p>

        Args:
            resource_scan_id: <p>The Amazon Resource Name (ARN) of the resource scan.</p>
            resource_identifier: <p>If specified, the returned resources will have the specified resource identifier (or one of them in the case where the resource has multiple identifiers).</p>
            resource_type_prefix: <p>If specified, the returned resources will be of any of the resource types with the specified prefix.</p>
            tag_key: <p>If specified, the returned resources will have a matching tag key.</p>
            tag_value: <p>If specified, the returned resources will have a matching tag value.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. By default the <code>ListResourceScanResources</code> API action will return at most 100 results in each response. The maximum value is 100.</p>

        Raises:
            capo_cloudformation.errors.resource_scan_in_progress_exception.ResourceScanInProgressException: <p>A resource scan is currently in progress. Only one can be run at a time for an account in a Region.</p>
            capo_cloudformation.errors.resource_scan_not_found_exception.ResourceScanNotFoundException: <p>The resource scan was not found.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To list the resources in your resource scan
            This example lists the resources in your resource scan

            >>> client.list_resource_scan_resources(resource_scan_id='arn:aws:cloudformation:us-east-1:123456789012:resourceScan/c19304f6-c4f1-4ff8-8e1f-35162e41d7e1')
            To list the resources in your resource scan for specific resource type
            This example lists the resources in your resource scan filtering only the resources that start with the passed in prefix

            >>> client.list_resource_scan_resources(resource_scan_id='arn:aws:cloudformation:us-east-1:123456789012:resourceScan/c19304f6-c4f1-4ff8-8e1f-35162e41d7e1', resource_type_prefix='AWS::S3')
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_resource_scan_resources_input.ListResourceScanResourcesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_resource_scan_resources_output.ListResourceScanResourcesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_resource_scan_resources

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_resource_scan_resources.list_resource_scan_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_resource_scan_resources_input.ListResourceScanResourcesInput = {}
        if resource_scan_id is not None:
            input_["resource_scan_id"] = resource_scan_id
        if resource_identifier is not None:
            input_["resource_identifier"] = resource_identifier
        if resource_type_prefix is not None:
            input_["resource_type_prefix"] = resource_type_prefix
        if tag_key is not None:
            input_["tag_key"] = tag_key
        if tag_value is not None:
            input_["tag_value"] = tag_value
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

    def iter_list_resource_scan_resources(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        resource_scan_id: Optional[
            "capo_cloudformation.types.resource_scan_id.ResourceScanId"
        ] = None,
        resource_identifier: Optional[
            "capo_cloudformation.types.resource_identifier.ResourceIdentifier"
        ] = None,
        resource_type_prefix: Optional[
            "capo_cloudformation.types.resource_type_prefix.ResourceTypePrefix"
        ] = None,
        tag_key: Optional["capo_cloudformation.types.tag_key.TagKey"] = None,
        tag_value: Optional["capo_cloudformation.types.tag_value.TagValue"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.resource_scanner_max_results.ResourceScannerMaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.scanned_resource.ScannedResource]":
        _token = next_token
        while True:
            _response = self.list_resource_scan_resources(
                config_overrides=config_overrides,
                resource_scan_id=resource_scan_id,
                resource_identifier=resource_identifier,
                resource_type_prefix=resource_type_prefix,
                tag_key=tag_key,
                tag_value=tag_value,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("resources",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_resource_scans(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.resource_scanner_max_results.ResourceScannerMaxResults"
        ] = None,
        scan_type_filter: Optional[
            "capo_cloudformation.types.scan_type.ScanType"
        ] = None,
    ) -> "capo_cloudformation.types.list_resource_scans_output.ListResourceScansOutput":
        """<p>List the resource scans from newest to oldest. By default it will return up to 10 resource scans.</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can use for the <code>NextToken</code> parameter to get the next set of results. The default value is 10. The maximum value is 100.</p>
            scan_type_filter: <p>The scan type that you want to get summary information about. The default is <code>FULL</code>.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_resource_scans_input.ListResourceScansInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_resource_scans_output.ListResourceScansOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_resource_scans

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_resource_scans.list_resource_scans(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_resource_scans_input.ListResourceScansInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if scan_type_filter is not None:
            input_["scan_type_filter"] = scan_type_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_resource_scans(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.resource_scanner_max_results.ResourceScannerMaxResults"
        ] = None,
        scan_type_filter: Optional[
            "capo_cloudformation.types.scan_type.ScanType"
        ] = None,
    ) -> (
        "Iterator[capo_cloudformation.types.resource_scan_summary.ResourceScanSummary]"
    ):
        _token = next_token
        while True:
            _response = self.list_resource_scans(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                scan_type_filter=scan_type_filter,
            )
            _page = _resolve_path(_response, ("resource_scan_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stack_instance_resource_drifts(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        stack_instance_resource_drift_statuses: Optional[
            "capo_cloudformation.types.stack_resource_drift_status_filters.StackResourceDriftStatusFilters"
        ] = None,
        stack_instance_account: Optional[
            "capo_cloudformation.types.account.Account"
        ] = None,
        stack_instance_region: Optional[
            "capo_cloudformation.types.region.Region"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.list_stack_instance_resource_drifts_output.ListStackInstanceResourceDriftsOutput":
        """<p>Returns drift information for resources in a stack instance.</p> <note> <p> <code>ListStackInstanceResourceDrifts</code> returns drift information for the most recent drift detection operation. If an operation is in progress, it may only return partial results.</p> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to list drifted resources for.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            stack_instance_resource_drift_statuses: <p>The resource drift status of the stack instance. </p> <ul> <li> <p> <code>DELETED</code>: The resource differs from its expected template configuration in that the resource has been deleted.</p> </li> <li> <p> <code>MODIFIED</code>: One or more resource properties differ from their expected template values.</p> </li> <li> <p> <code>IN_SYNC</code>: The resource's actual configuration matches its expected template configuration.</p> </li> <li> <p> <code>NOT_CHECKED</code>: CloudFormation doesn't currently return this value.</p> </li> </ul>
            stack_instance_account: <p>The name of the Amazon Web Services account that you want to list resource drifts for.</p>
            stack_instance_region: <p>The name of the Region where you want to list resource drifts.</p>
            operation_id: <p>The unique ID of the drift operation.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.operation_not_found_exception.OperationNotFoundException: <p>The specified ID refers to an operation that doesn't exist.</p>
            capo_cloudformation.errors.stack_instance_not_found_exception.StackInstanceNotFoundException: <p>The specified stack instance doesn't exist.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_instance_resource_drifts_input.ListStackInstanceResourceDriftsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_instance_resource_drifts_output.ListStackInstanceResourceDriftsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_instance_resource_drifts

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_instance_resource_drifts.list_stack_instance_resource_drifts(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_instance_resource_drifts_input.ListStackInstanceResourceDriftsInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if stack_instance_resource_drift_statuses is not None:
            input_["stack_instance_resource_drift_statuses"] = (
                stack_instance_resource_drift_statuses
            )
        if stack_instance_account is not None:
            input_["stack_instance_account"] = stack_instance_account
        if stack_instance_region is not None:
            input_["stack_instance_region"] = stack_instance_region
        if operation_id is not None:
            input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_stack_instances(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_cloudformation.types.stack_instance_filters.StackInstanceFilters"
        ] = None,
        stack_instance_account: Optional[
            "capo_cloudformation.types.account.Account"
        ] = None,
        stack_instance_region: Optional[
            "capo_cloudformation.types.region.Region"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> (
        "capo_cloudformation.types.list_stack_instances_output.ListStackInstancesOutput"
    ):
        """<p>Returns summary information about stack instances that are associated with the specified StackSet. You can filter for stack instances that are associated with a specific Amazon Web Services account name or Region, or that have a specific status.</p>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to list stack instances for.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            filters: <p>The filter to apply to stack instances</p>
            stack_instance_account: <p>The name of the Amazon Web Services account that you want to list stack instances for.</p>
            stack_instance_region: <p>The name of the Region where you want to list stack instances.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_instances_input.ListStackInstancesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_instances_output.ListStackInstancesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_instances

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_instances.list_stack_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_instances_input.ListStackInstancesInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if filters is not None:
            input_["filters"] = filters
        if stack_instance_account is not None:
            input_["stack_instance_account"] = stack_instance_account
        if stack_instance_region is not None:
            input_["stack_instance_region"] = stack_instance_region
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stack_instances(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        filters: Optional[
            "capo_cloudformation.types.stack_instance_filters.StackInstanceFilters"
        ] = None,
        stack_instance_account: Optional[
            "capo_cloudformation.types.account.Account"
        ] = None,
        stack_instance_region: Optional[
            "capo_cloudformation.types.region.Region"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_instance_summary.StackInstanceSummary]":
        _token = next_token
        while True:
            _response = self.list_stack_instances(
                config_overrides=config_overrides,
                stack_set_name=stack_set_name,
                next_token=_token,
                max_results=max_results,
                filters=filters,
                stack_instance_account=stack_instance_account,
                stack_instance_region=stack_instance_region,
                call_as=call_as,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stack_refactor_actions(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_refactor_id: Optional[
            "capo_cloudformation.types.stack_refactor_id.StackRefactorId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
    ) -> "capo_cloudformation.types.list_stack_refactor_actions_output.ListStackRefactorActionsOutput":
        """<p>Lists the stack refactor actions that will be taken after calling the <a>ExecuteStackRefactor</a> action.</p>

        Args:
            stack_refactor_id: <p>The ID associated with the stack refactor created from the <a>CreateStackRefactor</a> action.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_refactor_actions_input.ListStackRefactorActionsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_refactor_actions_output.ListStackRefactorActionsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_refactor_actions

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_refactor_actions.list_stack_refactor_actions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_refactor_actions_input.ListStackRefactorActionsInput = {}
        if stack_refactor_id is not None:
            input_["stack_refactor_id"] = stack_refactor_id
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

    def iter_list_stack_refactor_actions(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_refactor_id: Optional[
            "capo_cloudformation.types.stack_refactor_id.StackRefactorId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "Iterator[capo_cloudformation.types.stack_refactor_action.StackRefactorAction]"
    ):
        _token = next_token
        while True:
            _response = self.list_stack_refactor_actions(
                config_overrides=config_overrides,
                stack_refactor_id=stack_refactor_id,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("stack_refactor_actions",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stack_refactors(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        execution_status_filter: Optional[
            "capo_cloudformation.types.stack_refactor_execution_status_filter.StackRefactorExecutionStatusFilter"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
    ) -> (
        "capo_cloudformation.types.list_stack_refactors_output.ListStackRefactorsOutput"
    ):
        """<p>Lists all account stack refactor operations and their statuses.</p>

        Args:
            execution_status_filter: <p>Execution status to use as a filter. Specify one or more execution status codes to list only stack refactors with the specified execution status codes.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_refactors_input.ListStackRefactorsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_refactors_output.ListStackRefactorsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_refactors

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_refactors.list_stack_refactors(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_refactors_input.ListStackRefactorsInput = {}
        if execution_status_filter is not None:
            input_["execution_status_filter"] = execution_status_filter
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

    def iter_list_stack_refactors(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        execution_status_filter: Optional[
            "capo_cloudformation.types.stack_refactor_execution_status_filter.StackRefactorExecutionStatusFilter"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_refactor_summary.StackRefactorSummary]":
        _token = next_token
        while True:
            _response = self.list_stack_refactors(
                config_overrides=config_overrides,
                execution_status_filter=execution_status_filter,
                next_token=_token,
                max_results=max_results,
            )
            _page = _resolve_path(_response, ("stack_refactor_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stack_resources(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> (
        "capo_cloudformation.types.list_stack_resources_output.ListStackResourcesOutput"
    ):
        """<p>Returns descriptions of all resources of the specified stack.</p> <p>For deleted stacks, ListStackResources returns resource information for up to 90 days after the stack has been deleted.</p>

        Args:
            stack_name: <p>The name or the unique stack ID that is associated with the stack, which aren't always interchangeable:</p> <ul> <li> <p>Running stacks: You can specify either the stack's name or its unique stack ID.</p> </li> <li> <p>Deleted stacks: You must specify the unique stack ID.</p> </li> </ul>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_resources_input.ListStackResourcesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_resources_output.ListStackResourcesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_resources

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_resources.list_stack_resources(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_resources_input.ListStackResourcesInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stack_resources(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_resource_summary.StackResourceSummary]":
        _token = next_token
        while True:
            _response = self.list_stack_resources(
                config_overrides=config_overrides,
                stack_name=stack_name,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("stack_resource_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stacks(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        stack_status_filter: Optional[
            "capo_cloudformation.types.stack_status_filter.StackStatusFilter"
        ] = None,
    ) -> "capo_cloudformation.types.list_stacks_output.ListStacksOutput":
        """<p>Returns the summary information for stacks whose status matches the specified <code>StackStatusFilter</code>. Summary information for stacks that have been deleted is kept for 90 days after the stack is deleted. If no <code>StackStatusFilter</code> is specified, summary information for all stacks is returned (including existing stacks and stacks that have been deleted).</p>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            stack_status_filter: <p>Stack status to use as a filter. Specify one or more stack status codes to list only stacks with the specified status codes. For a complete list of stack status codes, see the <code>StackStatus</code> parameter of the <a>Stack</a> data type.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stacks_input.ListStacksInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stacks_output.ListStacksOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stacks

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stacks.list_stacks(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stacks_input.ListStacksInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if stack_status_filter is not None:
            input_["stack_status_filter"] = stack_status_filter

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stacks(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        stack_status_filter: Optional[
            "capo_cloudformation.types.stack_status_filter.StackStatusFilter"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_summary.StackSummary]":
        _token = next_token
        while True:
            _response = self.list_stacks(
                config_overrides=config_overrides,
                next_token=_token,
                stack_status_filter=stack_status_filter,
            )
            _page = _resolve_path(_response, ("stack_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stack_set_auto_deployment_targets(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.list_stack_set_auto_deployment_targets_output.ListStackSetAutoDeploymentTargetsOutput":
        """<p>Returns summary information about deployment targets for a StackSet.</p>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to get automatic deployment targets for.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            call_as: <p>Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_set_auto_deployment_targets_input.ListStackSetAutoDeploymentTargetsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_set_auto_deployment_targets_output.ListStackSetAutoDeploymentTargetsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_set_auto_deployment_targets

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_set_auto_deployment_targets.list_stack_set_auto_deployment_targets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_set_auto_deployment_targets_input.ListStackSetAutoDeploymentTargetsInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def list_stack_set_operation_results(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
        filters: Optional[
            "capo_cloudformation.types.operation_result_filters.OperationResultFilters"
        ] = None,
    ) -> "capo_cloudformation.types.list_stack_set_operation_results_output.ListStackSetOperationResultsOutput":
        """<p>Returns summary information about the results of a StackSet operation.</p> <note> <p>This API provides <i>eventually consistent</i> reads meaning it may take some time but will eventually return the most up-to-date data.</p> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to get operation results for.</p>
            operation_id: <p>The ID of the StackSet operation.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
            filters: <p>The filter to apply to operation results.</p>

        Raises:
            capo_cloudformation.errors.operation_not_found_exception.OperationNotFoundException: <p>The specified ID refers to an operation that doesn't exist.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_set_operation_results_input.ListStackSetOperationResultsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_set_operation_results_output.ListStackSetOperationResultsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_set_operation_results

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_set_operation_results.list_stack_set_operation_results(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_set_operation_results_input.ListStackSetOperationResultsInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if operation_id is not None:
            input_["operation_id"] = operation_id
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if call_as is not None:
            input_["call_as"] = call_as
        if filters is not None:
            input_["filters"] = filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stack_set_operation_results(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
        filters: Optional[
            "capo_cloudformation.types.operation_result_filters.OperationResultFilters"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_set_operation_result_summary.StackSetOperationResultSummary]":
        _token = next_token
        while True:
            _response = self.list_stack_set_operation_results(
                config_overrides=config_overrides,
                stack_set_name=stack_set_name,
                operation_id=operation_id,
                next_token=_token,
                max_results=max_results,
                call_as=call_as,
                filters=filters,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stack_set_operations(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.list_stack_set_operations_output.ListStackSetOperationsOutput":
        """<p>Returns summary information about operations performed on a StackSet.</p> <note> <p>This API provides <i>eventually consistent</i> reads meaning it may take some time but will eventually return the most up-to-date data.</p> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to get operation summaries for.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_set_operations_input.ListStackSetOperationsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_set_operations_output.ListStackSetOperationsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_set_operations

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_set_operations.list_stack_set_operations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_set_operations_input.ListStackSetOperationsInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stack_set_operations(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_set_operation_summary.StackSetOperationSummary]":
        _token = next_token
        while True:
            _response = self.list_stack_set_operations(
                config_overrides=config_overrides,
                stack_set_name=stack_set_name,
                next_token=_token,
                max_results=max_results,
                call_as=call_as,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_stack_sets(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "capo_cloudformation.types.stack_set_status.StackSetStatus"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.list_stack_sets_output.ListStackSetsOutput":
        """<p>Returns summary information about StackSets that are associated with the user.</p> <note> <p>This API provides <i>strongly consistent</i> reads meaning it will always return the most up-to-date data.</p> </note> <ul> <li> <p>[Self-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to your Amazon Web Services account, <code>ListStackSets</code> returns all self-managed StackSets in your Amazon Web Services account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>SELF</code> while signed in to the organization's management account, <code>ListStackSets</code> returns all StackSets in the management account.</p> </li> <li> <p>[Service-managed permissions] If you set the <code>CallAs</code> parameter to <code>DELEGATED_ADMIN</code> while signed in to your member account, <code>ListStackSets</code> returns all StackSets with service-managed permissions in the management account.</p> </li> </ul>

        Args:
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            status: <p>The status of the StackSets that you want to get summary information about.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_stack_sets_input.ListStackSetsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_stack_sets_output.ListStackSetsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_stack_sets

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_stack_sets.list_stack_sets(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_stack_sets_input.ListStackSetsInput = {}
        if next_token is not None:
            input_["next_token"] = next_token
        if max_results is not None:
            input_["max_results"] = max_results
        if status is not None:
            input_["status"] = status
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_stack_sets(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        status: Optional[
            "capo_cloudformation.types.stack_set_status.StackSetStatus"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "Iterator[capo_cloudformation.types.stack_set_summary.StackSetSummary]":
        _token = next_token
        while True:
            _response = self.list_stack_sets(
                config_overrides=config_overrides,
                next_token=_token,
                max_results=max_results,
                status=status,
                call_as=call_as,
            )
            _page = _resolve_path(_response, ("summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_type_registrations(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        type_arn: Optional["capo_cloudformation.types.type_arn.TypeArn"] = None,
        registration_status_filter: Optional[
            "capo_cloudformation.types.registration_status.RegistrationStatus"
        ] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.list_type_registrations_output.ListTypeRegistrationsOutput":
        """<p>Returns a list of registration tokens for the specified extension(s).</p>

        Args:
            type: <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type_name: <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type_arn: <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            registration_status_filter: <p>The current status of the extension registration request.</p> <p>The default is <code>IN_PROGRESS</code>.</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_type_registrations_input.ListTypeRegistrationsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_type_registrations_output.ListTypeRegistrationsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_type_registrations

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_type_registrations.list_type_registrations(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_type_registrations_input.ListTypeRegistrationsInput = {}
        if type is not None:
            input_["type"] = type
        if type_name is not None:
            input_["type_name"] = type_name
        if type_arn is not None:
            input_["type_arn"] = type_arn
        if registration_status_filter is not None:
            input_["registration_status_filter"] = registration_status_filter
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

    def iter_list_type_registrations(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        type_arn: Optional["capo_cloudformation.types.type_arn.TypeArn"] = None,
        registration_status_filter: Optional[
            "capo_cloudformation.types.registration_status.RegistrationStatus"
        ] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.list_type_registrations_output.ListTypeRegistrationsOutput]":
        _token = next_token
        while True:
            _response = self.list_type_registrations(
                config_overrides=config_overrides,
                type=type,
                type_name=type_name,
                type_arn=type_arn,
                registration_status_filter=registration_status_filter,
                max_results=max_results,
                next_token=_token,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_types(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        visibility: Optional["capo_cloudformation.types.visibility.Visibility"] = None,
        provisioning_type: Optional[
            "capo_cloudformation.types.provisioning_type.ProvisioningType"
        ] = None,
        deprecated_status: Optional[
            "capo_cloudformation.types.deprecated_status.DeprecatedStatus"
        ] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        filters: Optional["capo_cloudformation.types.type_filters.TypeFilters"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "capo_cloudformation.types.list_types_output.ListTypesOutput":
        """<p>Returns summary information about all extensions, including your private resource types, modules, and Hooks as well as all public extensions from Amazon Web Services and third-party publishers.</p>

        Args:
            visibility: <p>The scope at which the extensions are visible and usable in CloudFormation operations.</p> <p>Valid values include:</p> <ul> <li> <p> <code>PRIVATE</code>: Extensions that are visible and usable within this account and Region. This includes:</p> <ul> <li> <p>Private extensions you have registered in this account and Region.</p> </li> <li> <p>Public extensions that you have activated in this account and Region.</p> </li> </ul> </li> <li> <p> <code>PUBLIC</code>: Extensions that are publicly visible and available to be activated within any Amazon Web Services account. This includes extensions from Amazon Web Services and third-party publishers.</p> </li> </ul> <p>The default is <code>PRIVATE</code>.</p>
            provisioning_type: <p>For resource types, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.</p> <p>Valid values include:</p> <ul> <li> <p> <code>FULLY_MUTABLE</code>: The resource type includes an update handler to process updates to the type during stack update operations.</p> </li> <li> <p> <code>IMMUTABLE</code>: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.</p> </li> <li> <p> <code>NON_PROVISIONABLE</code>: The resource type doesn't include create, read, and delete handlers, and therefore can't actually be provisioned.</p> </li> </ul> <p>The default is <code>FULLY_MUTABLE</code>.</p>
            deprecated_status: <p>The deprecation status of the extension that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension is registered for use in CloudFormation operations.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul>
            type: <p>The type of extension.</p>
            filters: <p>Filter criteria to use in determining which extensions to return.</p> <p>Filters must be compatible with <code>Visibility</code> to return valid results. For example, specifying <code>AWS_TYPES</code> for <code>Category</code> and <code>PRIVATE</code> for <code>Visibility</code> returns an empty list of types, but specifying <code>PUBLIC</code> for <code>Visibility</code> returns the desired list.</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_types_input.ListTypesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_types_output.ListTypesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_types

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_types.list_types(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_types_input.ListTypesInput = {}
        if visibility is not None:
            input_["visibility"] = visibility
        if provisioning_type is not None:
            input_["provisioning_type"] = provisioning_type
        if deprecated_status is not None:
            input_["deprecated_status"] = deprecated_status
        if type is not None:
            input_["type"] = type
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

    def iter_list_types(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        visibility: Optional["capo_cloudformation.types.visibility.Visibility"] = None,
        provisioning_type: Optional[
            "capo_cloudformation.types.provisioning_type.ProvisioningType"
        ] = None,
        deprecated_status: Optional[
            "capo_cloudformation.types.deprecated_status.DeprecatedStatus"
        ] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        filters: Optional["capo_cloudformation.types.type_filters.TypeFilters"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
    ) -> "Iterator[capo_cloudformation.types.type_summary.TypeSummary]":
        _token = next_token
        while True:
            _response = self.list_types(
                config_overrides=config_overrides,
                visibility=visibility,
                provisioning_type=provisioning_type,
                deprecated_status=deprecated_status,
                type=type,
                filters=filters,
                max_results=max_results,
                next_token=_token,
            )
            _page = _resolve_path(_response, ("type_summaries",))
            for _item in _page or []:
                yield _item
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def list_type_versions(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        arn: Optional["capo_cloudformation.types.type_arn.TypeArn"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        deprecated_status: Optional[
            "capo_cloudformation.types.deprecated_status.DeprecatedStatus"
        ] = None,
        publisher_id: Optional[
            "capo_cloudformation.types.publisher_id.PublisherId"
        ] = None,
    ) -> "capo_cloudformation.types.list_type_versions_output.ListTypeVersionsOutput":
        """<p>Returns summary information about the versions of an extension.</p>

        Args:
            type: <p>The kind of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type_name: <p>The name of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            arn: <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            max_results: <p>The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a <code>NextToken</code> value that you can assign to the <code>NextToken</code> request parameter to get the next set of results.</p>
            next_token: <p>The token for the next set of items to return. (You received this token from a previous call.)</p>
            deprecated_status: <p>The deprecation status of the extension versions that you want to get summary information about.</p> <p>Valid values include:</p> <ul> <li> <p> <code>LIVE</code>: The extension version is registered and can be used in CloudFormation operations, dependent on its provisioning behavior and visibility scope.</p> </li> <li> <p> <code>DEPRECATED</code>: The extension version has been deregistered and can no longer be used in CloudFormation operations.</p> </li> </ul> <p>The default is <code>LIVE</code>.</p>
            publisher_id: <p>The publisher ID of the extension publisher.</p> <p>Extensions published by Amazon aren't assigned a publisher ID.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.list_type_versions_input.ListTypeVersionsInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.list_type_versions_output.ListTypeVersionsOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.list_type_versions

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.list_type_versions.list_type_versions(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.list_type_versions_input.ListTypeVersionsInput = {}
        if type is not None:
            input_["type"] = type
        if type_name is not None:
            input_["type_name"] = type_name
        if arn is not None:
            input_["arn"] = arn
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token
        if deprecated_status is not None:
            input_["deprecated_status"] = deprecated_status
        if publisher_id is not None:
            input_["publisher_id"] = publisher_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def iter_list_type_versions(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        arn: Optional["capo_cloudformation.types.type_arn.TypeArn"] = None,
        max_results: Optional[
            "capo_cloudformation.types.max_results.MaxResults"
        ] = None,
        next_token: Optional["capo_cloudformation.types.next_token.NextToken"] = None,
        deprecated_status: Optional[
            "capo_cloudformation.types.deprecated_status.DeprecatedStatus"
        ] = None,
        publisher_id: Optional[
            "capo_cloudformation.types.publisher_id.PublisherId"
        ] = None,
    ) -> "Iterator[capo_cloudformation.types.list_type_versions_output.ListTypeVersionsOutput]":
        _token = next_token
        while True:
            _response = self.list_type_versions(
                config_overrides=config_overrides,
                type=type,
                type_name=type_name,
                arn=arn,
                max_results=max_results,
                next_token=_token,
                deprecated_status=deprecated_status,
                publisher_id=publisher_id,
            )
            yield _response
            _token = _resolve_path(_response, ("next_token",))
            if not _token:
                break

    def publish_type(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional[
            "capo_cloudformation.types.third_party_type.ThirdPartyType"
        ] = None,
        arn: Optional[
            "capo_cloudformation.types.private_type_arn.PrivateTypeArn"
        ] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        public_version_number: Optional[
            "capo_cloudformation.types.public_version_number.PublicVersionNumber"
        ] = None,
    ) -> "capo_cloudformation.types.publish_type_output.PublishTypeOutput":
        """<p>Publishes the specified extension to the CloudFormation registry as a public extension in this Region. Public extensions are available for use by all CloudFormation users. For more information about publishing extensions, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p> <p>To publish an extension, you must be registered as a publisher with CloudFormation. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterPublisher.html">RegisterPublisher</a>.</p>

        Args:
            type: <p>The type of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            arn: <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            type_name: <p>The name of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            public_version_number: <p>The version number to assign to this version of the extension.</p> <p>Use the following format, and adhere to semantic versioning when assigning a version number to your extension:</p> <p> <code>MAJOR.MINOR.PATCH</code> </p> <p>For more information, see <a href="https://semver.org/">Semantic Versioning 2.0.0</a>.</p> <p>If you don't specify a version number, CloudFormation increments the version number by one minor version release.</p> <p>You cannot specify a version number the first time you publish a type. CloudFormation automatically sets the first version number to be <code>1.0.0</code>.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.publish_type_input.PublishTypeInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.publish_type_output.PublishTypeOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.publish_type

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.publish_type.publish_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.publish_type_input.PublishTypeInput = {}
        if type is not None:
            input_["type"] = type
        if arn is not None:
            input_["arn"] = arn
        if type_name is not None:
            input_["type_name"] = type_name
        if public_version_number is not None:
            input_["public_version_number"] = public_version_number

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def record_handler_progress(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        bearer_token: Optional[
            "capo_cloudformation.types.client_token.ClientToken"
        ] = None,
        operation_status: Optional[
            "capo_cloudformation.types.operation_status.OperationStatus"
        ] = None,
        current_operation_status: Optional[
            "capo_cloudformation.types.operation_status.OperationStatus"
        ] = None,
        status_message: Optional[
            "capo_cloudformation.types.status_message.StatusMessage"
        ] = None,
        error_code: Optional[
            "capo_cloudformation.types.handler_error_code.HandlerErrorCode"
        ] = None,
        resource_model: Optional[
            "capo_cloudformation.types.resource_model.ResourceModel"
        ] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
    ) -> "capo_cloudformation.types.record_handler_progress_output.RecordHandlerProgressOutput":
        """<p>Reports progress of a resource handler to CloudFormation.</p> <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. Don't use this API in your code.</p>

        Args:
            bearer_token: <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>
            operation_status: <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>
            current_operation_status: <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>
            status_message: <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>
            error_code: <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>
            resource_model: <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>
            client_request_token: <p>Reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>.</p>

        Raises:
            capo_cloudformation.errors.invalid_state_transition_exception.InvalidStateTransitionException: <p>Error reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. CloudFormation doesn't return this error to users.</p>
            capo_cloudformation.errors.operation_status_check_failed_exception.OperationStatusCheckFailedException: <p>Error reserved for use by the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/what-is-cloudformation-cli.html">CloudFormation CLI</a>. CloudFormation doesn't return this error to users.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.record_handler_progress_input.RecordHandlerProgressInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.record_handler_progress_output.RecordHandlerProgressOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.record_handler_progress

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.record_handler_progress.record_handler_progress(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.record_handler_progress_input.RecordHandlerProgressInput = {}
        if bearer_token is not None:
            input_["bearer_token"] = bearer_token
        if operation_status is not None:
            input_["operation_status"] = operation_status
        if current_operation_status is not None:
            input_["current_operation_status"] = current_operation_status
        if status_message is not None:
            input_["status_message"] = status_message
        if error_code is not None:
            input_["error_code"] = error_code
        if resource_model is not None:
            input_["resource_model"] = resource_model
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_publisher(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        accept_terms_and_conditions: Optional[
            "capo_cloudformation.types.accept_terms_and_conditions.AcceptTermsAndConditions"
        ] = None,
        connection_arn: Optional[
            "capo_cloudformation.types.connection_arn.ConnectionArn"
        ] = None,
    ) -> "capo_cloudformation.types.register_publisher_output.RegisterPublisherOutput":
        """<p>Registers your account as a publisher of public extensions in the CloudFormation registry. Public extensions are available for use by all CloudFormation users. This publisher ID applies to your account in all Amazon Web Services Regions.</p> <p>For information about requirements for registering as a public extension publisher, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Prerequisite: Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p> <p></p>

        Args:
            accept_terms_and_conditions: <p>Whether you accept the <a href="https://cloudformation-registry-documents.s3.amazonaws.com/Terms_and_Conditions_for_AWS_CloudFormation_Registry_Publishers.pdf">Terms and Conditions</a> for publishing extensions in the CloudFormation registry. You must accept the terms and conditions in order to register to publish public extensions to the CloudFormation registry.</p> <p>The default is <code>false</code>.</p>
            connection_arn: <p>If you are using a Bitbucket or GitHub account for identity verification, the Amazon Resource Name (ARN) for your connection to that account.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-prereqs">Prerequisite: Registering your account to publish CloudFormation extensions</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.register_publisher_input.RegisterPublisherInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.register_publisher_output.RegisterPublisherOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.register_publisher

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.register_publisher.register_publisher(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.register_publisher_input.RegisterPublisherInput = {}
        if accept_terms_and_conditions is not None:
            input_["accept_terms_and_conditions"] = accept_terms_and_conditions
        if connection_arn is not None:
            input_["connection_arn"] = connection_arn

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def register_type(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        schema_handler_package: Optional[
            "capo_cloudformation.types.s3_url.S3Url"
        ] = None,
        logging_config: Optional[
            "capo_cloudformation.types.logging_config.LoggingConfig"
        ] = None,
        execution_role_arn: Optional[
            "capo_cloudformation.types.role_arn2.RoleARN2"
        ] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.request_token.RequestToken"
        ] = None,
    ) -> "capo_cloudformation.types.register_type_output.RegisterTypeOutput":
        """<p>Registers an extension with the CloudFormation service. Registering an extension makes it available for use in CloudFormation templates in your Amazon Web Services account, and includes:</p> <ul> <li> <p>Validating the extension schema.</p> </li> <li> <p>Determining which handlers, if any, have been specified for the extension.</p> </li> <li> <p>Making the extension available for use in your account.</p> </li> </ul> <p>For more information about how to develop extensions and ready them for registration, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-types.html">Creating resource types using the CloudFormation CLI</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p> <p>You can have a maximum of 50 resource extension versions registered at a time. This maximum is per account and per Region. Use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html">DeregisterType</a> to deregister specific extension versions if necessary.</p> <p>Once you have initiated a registration request using <a>RegisterType</a>, you can use <a>DescribeTypeRegistration</a> to monitor the progress of the registration request.</p> <p>Once you have registered a private extension in your account and Region, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_SetTypeConfiguration.html">SetTypeConfiguration</a> to specify configuration properties for the extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html">Edit configuration data for extensions in your account</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            type: <p>The kind of extension.</p>
            type_name: <p>The name of the extension being registered.</p> <p>We suggest that extension names adhere to the following patterns:</p> <ul> <li> <p>For resource types, <code>company_or_organization::service::type</code>.</p> </li> <li> <p>For modules, <code>company_or_organization::service::type::MODULE</code>.</p> </li> <li> <p>For Hooks, <code>MyCompany::Testing::MyTestHook</code>.</p> </li> </ul> <note> <p>The following organization namespaces are reserved and can't be used in your extension names:</p> <ul> <li> <p> <code>Alexa</code> </p> </li> <li> <p> <code>AMZN</code> </p> </li> <li> <p> <code>Amazon</code> </p> </li> <li> <p> <code>AWS</code> </p> </li> <li> <p> <code>Custom</code> </p> </li> <li> <p> <code>Dev</code> </p> </li> </ul> </note>
            schema_handler_package: <p>A URL to the S3 bucket that contains the extension project package that contains the necessary files for the extension you want to register.</p> <p>For information about generating a schema handler package for the extension you want to register, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-cli-submit.html">submit</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p> <note> <p>The user registering the extension must be able to access the package in the S3 bucket. That's, the user needs to have <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_GetObject.html">GetObject</a> permissions for the schema handler package. For more information, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p> </note>
            logging_config: <p>Specifies logging configuration information for an extension.</p>
            execution_role_arn: <p>The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the extension.</p> <p>For CloudFormation to assume the specified execution role, the role must contain a trust relationship with the CloudFormation service principal (<code>resources.cloudformation.amazonaws.com</code>). For more information about adding trust relationships, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy">Modifying a role trust policy</a> in the <i>Identity and Access Management User Guide</i>.</p> <p>If your extension calls Amazon Web Services APIs in any of its handlers, you must create an <i> <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html">IAM execution role</a> </i> that includes the necessary permissions to call those Amazon Web Services APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.</p>
            client_request_token: <p>A unique identifier that acts as an idempotency key for this registration request. Specifying a client request token prevents CloudFormation from generating more than one version of an extension from the same registration request, even if the request is submitted multiple times.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.register_type_input.RegisterTypeInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.register_type_output.RegisterTypeOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.register_type

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.register_type.register_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.register_type_input.RegisterTypeInput = {}
        if type is not None:
            input_["type"] = type
        if type_name is not None:
            input_["type_name"] = type_name
        if schema_handler_package is not None:
            input_["schema_handler_package"] = schema_handler_package
        if logging_config is not None:
            input_["logging_config"] = logging_config
        if execution_role_arn is not None:
            input_["execution_role_arn"] = execution_role_arn
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def rollback_stack(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        role_arn: Optional["capo_cloudformation.types.role_arn.RoleARN"] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        retain_except_on_create: Optional[
            "capo_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
        ] = None,
        deployment_config: Optional[
            "capo_cloudformation.types.deployment_config.DeploymentConfig"
        ] = None,
    ) -> "capo_cloudformation.types.rollback_stack_output.RollbackStackOutput":
        """<p>When specifying <code>RollbackStack</code>, you preserve the state of previously provisioned resources when an operation fails. You can check the status of the stack through the <a>DescribeStacks</a> operation.</p> <p>Rolls back the specified stack to the last known stable state from <code>CREATE_FAILED</code> or <code>UPDATE_FAILED</code> stack statuses.</p> <p>This operation will delete a stack if it doesn't contain a last known stable state. A last known stable state includes any status in a <code>*_COMPLETE</code>. This includes the following stack statuses.</p> <ul> <li> <p> <code>CREATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_COMPLETE</code> </p> </li> <li> <p> <code>UPDATE_ROLLBACK_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_COMPLETE</code> </p> </li> <li> <p> <code>IMPORT_ROLLBACK_COMPLETE</code> </p> </li> </ul>

        Args:
            stack_name: <p>The name that's associated with the stack.</p>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to rollback the stack.</p>
            client_request_token: <p>A unique identifier for this <code>RollbackStack</code> request.</p>
            retain_except_on_create: <p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>
            deployment_config: <p>The deployment configuration for this stack operation, including the deployment mode.</p>

        Raises:
            capo_cloudformation.errors.token_already_exists_exception.TokenAlreadyExistsException: <p>A client request token already exists.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.rollback_stack_input.RollbackStackInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.rollback_stack_output.RollbackStackOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.rollback_stack

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.rollback_stack.rollback_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.rollback_stack_input.RollbackStackInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if retain_except_on_create is not None:
            input_["retain_except_on_create"] = retain_except_on_create
        if deployment_config is not None:
            input_["deployment_config"] = deployment_config

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_stack_policy(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        stack_policy_body: Optional[
            "capo_cloudformation.types.stack_policy_body.StackPolicyBody"
        ] = None,
        stack_policy_url: Optional[
            "capo_cloudformation.types.stack_policy_url.StackPolicyURL"
        ] = None,
    ) -> None:
        """<p>Sets a stack policy for a specified stack.</p>

        Args:
            stack_name: <p>The name or unique stack ID that you want to associate a policy with.</p>
            stack_policy_body: <p>Structure that contains the stack policy body. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/protect-stack-resources.html">Prevent updates to stack resources</a> in the <i>CloudFormation User Guide</i>. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>
            stack_policy_url: <p>Location of a file that contains the stack policy. The URL must point to a policy (maximum size: 16 KB) located in an Amazon S3 bucket in the same Amazon Web Services Region as the stack. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.set_stack_policy_input.SetStackPolicyInput]",
        ) -> OperationResponse[None]:
            import capo_cloudformation._operations.cloud_formation.set_stack_policy

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.set_stack_policy.set_stack_policy(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.set_stack_policy_input.SetStackPolicyInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if stack_policy_body is not None:
            input_["stack_policy_body"] = stack_policy_body
        if stack_policy_url is not None:
            input_["stack_policy_url"] = stack_policy_url

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_type_configuration(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        type_arn: Optional["capo_cloudformation.types.type_arn.TypeArn"] = None,
        configuration: Optional[
            "capo_cloudformation.types.type_configuration.TypeConfiguration"
        ] = None,
        configuration_alias: Optional[
            "capo_cloudformation.types.type_configuration_alias.TypeConfigurationAlias"
        ] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        type: Optional[
            "capo_cloudformation.types.third_party_type.ThirdPartyType"
        ] = None,
    ) -> "capo_cloudformation.types.set_type_configuration_output.SetTypeConfigurationOutput":
        """<p>Specifies the configuration data for a CloudFormation extension, such as a resource or Hook, in the given account and Region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-set-configuration.html">Edit configuration data for extensions in your account</a> in the <i>CloudFormation User Guide</i>.</p> <p>To view the current configuration data for an extension, refer to the <code>ConfigurationSchema</code> element of <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p> <important> <p>It's strongly recommended that you use dynamic references to restrict sensitive configuration definitions, such as third-party credentials. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/dynamic-references.html">Specify values stored in other services using dynamic references</a> in the <i>CloudFormation User Guide</i>.</p> </important> <p>For more information about setting the configuration data for resource types, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html#resource-type-howto-configuration">Defining the account-level configuration of an extension</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>. For more information about setting the configuration data for Hooks, see the <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/what-is-cloudformation-hooks.html">CloudFormation Hooks User Guide</a>.</p>

        Args:
            type_arn: <p>The Amazon Resource Name (ARN) for the extension in this account and Region.</p> <p>For public extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">ActivateType</a> API operation in this account and Region. For private extensions, this will be the ARN assigned when you call the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a> API operation in this account and Region.</p> <p>Do not include the extension versions suffix at the end of the ARN. You can set the configuration for an extension, but not for a specific extension version.</p>
            configuration: <p>The configuration data for the extension in this account and Region.</p> <p>The configuration data must be formatted as JSON and validate against the extension's schema returned in the <code>Schema</code> response element of <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a>.</p>
            configuration_alias: <p>An alias by which to refer to this extension configuration data.</p> <p>Conditional: Specifying a configuration alias is required when setting a configuration for a resource type extension.</p>
            type_name: <p>The name of the extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>
            type: <p>The type of extension.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.set_type_configuration_input.SetTypeConfigurationInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.set_type_configuration_output.SetTypeConfigurationOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.set_type_configuration

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.set_type_configuration.set_type_configuration(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.set_type_configuration_input.SetTypeConfigurationInput = {}
        if type_arn is not None:
            input_["type_arn"] = type_arn
        if configuration is not None:
            input_["configuration"] = configuration
        if configuration_alias is not None:
            input_["configuration_alias"] = configuration_alias
        if type_name is not None:
            input_["type_name"] = type_name
        if type is not None:
            input_["type"] = type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def set_type_default_version(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        arn: Optional[
            "capo_cloudformation.types.private_type_arn.PrivateTypeArn"
        ] = None,
        type: Optional["capo_cloudformation.types.registry_type.RegistryType"] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        version_id: Optional[
            "capo_cloudformation.types.type_version_id.TypeVersionId"
        ] = None,
    ) -> "capo_cloudformation.types.set_type_default_version_output.SetTypeDefaultVersionOutput":
        """<p>Specify the default version of an extension. The default version of an extension will be used in CloudFormation operations.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the extension for which you want version summary information.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type: <p>The kind of extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            type_name: <p>The name of the extension.</p> <p>Conditional: You must specify either <code>TypeName</code> and <code>Type</code>, or <code>Arn</code>.</p>
            version_id: <p>The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it is registered.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.set_type_default_version_input.SetTypeDefaultVersionInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.set_type_default_version_output.SetTypeDefaultVersionOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.set_type_default_version

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.set_type_default_version.set_type_default_version(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.set_type_default_version_input.SetTypeDefaultVersionInput = {}
        if arn is not None:
            input_["arn"] = arn
        if type is not None:
            input_["type"] = type
        if type_name is not None:
            input_["type_name"] = type_name
        if version_id is not None:
            input_["version_id"] = version_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def signal_resource(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
        logical_resource_id: Optional[
            "capo_cloudformation.types.logical_resource_id.LogicalResourceId"
        ] = None,
        unique_id: Optional[
            "capo_cloudformation.types.resource_signal_unique_id.ResourceSignalUniqueId"
        ] = None,
        status: Optional[
            "capo_cloudformation.types.resource_signal_status.ResourceSignalStatus"
        ] = None,
    ) -> None:
        """<p>Sends a signal to the specified resource with a success or failure status. You can use the <code>SignalResource</code> operation in conjunction with a creation policy or update policy. CloudFormation doesn't proceed with a stack creation or update until resources receive the required number of signals or the timeout period is exceeded. The <code>SignalResource</code> operation is useful in cases where you want to send signals from anywhere other than an Amazon EC2 instance.</p>

        Args:
            stack_name: <p>The stack name or unique stack ID that includes the resource that you want to signal.</p>
            logical_resource_id: <p>The logical ID of the resource that you want to signal. The logical ID is the name of the resource that given in the template.</p>
            unique_id: <p>A unique ID of the signal. When you signal Amazon EC2 instances or Auto Scaling groups, specify the instance ID that you are signaling as the unique ID. If you send multiple signals to a single resource (such as signaling a wait condition), each signal requires a different unique ID.</p>
            status: <p>The status of the signal, which is either success or failure. A failure signal causes CloudFormation to immediately fail the stack creation or update.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.signal_resource_input.SignalResourceInput]",
        ) -> OperationResponse[None]:
            import capo_cloudformation._operations.cloud_formation.signal_resource

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.signal_resource.signal_resource(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.signal_resource_input.SignalResourceInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if logical_resource_id is not None:
            input_["logical_resource_id"] = logical_resource_id
        if unique_id is not None:
            input_["unique_id"] = unique_id
        if status is not None:
            input_["status"] = status

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def start_resource_scan(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        scan_filters: Optional[
            "capo_cloudformation.types.scan_filters.ScanFilters"
        ] = None,
    ) -> "capo_cloudformation.types.start_resource_scan_output.StartResourceScanOutput":
        """<p>Starts a scan of the resources in this account in this Region. You can the status of a scan using the <code>ListResourceScans</code> API action.</p>

        Args:
            client_request_token: <p>A unique identifier for this <code>StartResourceScan</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to start a new resource scan.</p>
            scan_filters: <p>The scan filters to use.</p>

        Raises:
            capo_cloudformation.errors.resource_scan_in_progress_exception.ResourceScanInProgressException: <p>A resource scan is currently in progress. Only one can be run at a time for an account in a Region.</p>
            capo_cloudformation.errors.resource_scan_limit_exceeded_exception.ResourceScanLimitExceededException: <p>The limit on resource scans has been exceeded. Reasons include:</p> <ul> <li> <p>Exceeded the daily quota for resource scans.</p> </li> <li> <p>A resource scan recently failed. You must wait 10 minutes before starting a new resource scan.</p> </li> <li> <p>The last resource scan failed after exceeding 100,000 resources. When this happens, you must wait 24 hours before starting a new resource scan.</p> </li> </ul>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To start a resource scan
            This example shows how to start a new resource scan

            >>> client.start_resource_scan()
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.start_resource_scan_input.StartResourceScanInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.start_resource_scan_output.StartResourceScanOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.start_resource_scan

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.start_resource_scan.start_resource_scan(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.start_resource_scan_input.StartResourceScanInput = {}
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if scan_filters is not None:
            input_["scan_filters"] = scan_filters

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def stop_stack_set_operation(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.stop_stack_set_operation_output.StopStackSetOperationOutput":
        """<p>Stops an in-progress operation on a StackSet and its associated stack instances. StackSets will cancel all the unstarted stack instance deployments and wait for those are in-progress to complete.</p>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to stop the operation for.</p>
            operation_id: <p>The ID of the stack operation.</p>
            call_as: <p>Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account. Valid only if the StackSet uses service-managed permissions.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_not_found_exception.OperationNotFoundException: <p>The specified ID refers to an operation that doesn't exist.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.stop_stack_set_operation_input.StopStackSetOperationInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.stop_stack_set_operation_output.StopStackSetOperationOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.stop_stack_set_operation

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.stop_stack_set_operation.stop_stack_set_operation(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.stop_stack_set_operation_input.StopStackSetOperationInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if operation_id is not None:
            input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def test_type(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        arn: Optional["capo_cloudformation.types.type_arn.TypeArn"] = None,
        type: Optional[
            "capo_cloudformation.types.third_party_type.ThirdPartyType"
        ] = None,
        type_name: Optional["capo_cloudformation.types.type_name.TypeName"] = None,
        version_id: Optional[
            "capo_cloudformation.types.type_version_id.TypeVersionId"
        ] = None,
        log_delivery_bucket: Optional[
            "capo_cloudformation.types.s3_bucket.S3Bucket"
        ] = None,
    ) -> "capo_cloudformation.types.test_type_output.TestTypeOutput":
        """<p>Tests a registered extension to make sure it meets all necessary requirements for being published in the CloudFormation registry.</p> <ul> <li> <p>For resource types, this includes passing all contracts tests defined for the type.</p> </li> <li> <p>For modules, this includes determining if the module's model meets all necessary requirements.</p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/publish-extension.html#publish-extension-testing">Testing your public extension before publishing</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in your account and Region for testing.</p> <p>To perform testing, CloudFormation assumes the execution role specified when the type was registered. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">RegisterType</a>.</p> <p>Once you've initiated testing on an extension using <code>TestType</code>, you can pass the returned <code>TypeVersionArn</code> into <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DescribeType.html">DescribeType</a> to monitor the current test status and test status description for the extension.</p> <p>An extension must have a test status of <code>PASSED</code> before it can be published. For more information, see <a href="https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-publish.html">Publishing extensions to make them available for public use</a> in the <i>CloudFormation Command Line Interface (CLI) User Guide</i>.</p>

        Args:
            arn: <p>The Amazon Resource Name (ARN) of the extension.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            type: <p>The type of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            type_name: <p>The name of the extension to test.</p> <p>Conditional: You must specify <code>Arn</code>, or <code>TypeName</code> and <code>Type</code>.</p>
            version_id: <p>The version of the extension to test.</p> <p>You can specify the version id with either <code>Arn</code>, or with <code>TypeName</code> and <code>Type</code>.</p> <p>If you don't specify a version, CloudFormation uses the default version of the extension in this account and Region for testing.</p>
            log_delivery_bucket: <p>The S3 bucket to which CloudFormation delivers the contract test execution logs.</p> <p>CloudFormation delivers the logs by the time contract testing has completed and the extension has been assigned a test type status of <code>PASSED</code> or <code>FAILED</code>.</p> <p>The user calling <code>TestType</code> must be able to access items in the specified S3 bucket. Specifically, the user needs the following permissions:</p> <ul> <li> <p> <code>GetObject</code> </p> </li> <li> <p> <code>PutObject</code> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazons3.html">Actions, Resources, and Condition Keys for Amazon S3</a> in the <i>Identity and Access Management User Guide</i>.</p>

        Raises:
            capo_cloudformation.errors.cfn_registry_exception.CFNRegistryException: <p>An error occurred during a CloudFormation registry operation.</p>
            capo_cloudformation.errors.type_not_found_exception.TypeNotFoundException: <p>The specified extension doesn't exist in the CloudFormation registry.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.test_type_input.TestTypeInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.test_type_output.TestTypeOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.test_type

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.test_type.test_type(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.test_type_input.TestTypeInput = {}
        if arn is not None:
            input_["arn"] = arn
        if type is not None:
            input_["type"] = type
        if type_name is not None:
            input_["type_name"] = type_name
        if version_id is not None:
            input_["version_id"] = version_id
        if log_delivery_bucket is not None:
            input_["log_delivery_bucket"] = log_delivery_bucket

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_generated_template(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        generated_template_name: Optional[
            "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
        ] = None,
        new_generated_template_name: Optional[
            "capo_cloudformation.types.generated_template_name.GeneratedTemplateName"
        ] = None,
        add_resources: Optional[
            "capo_cloudformation.types.resource_definitions.ResourceDefinitions"
        ] = None,
        remove_resources: Optional[
            "capo_cloudformation.types.jazz_logical_resource_ids.JazzLogicalResourceIds"
        ] = None,
        refresh_all_resources: Optional[
            "capo_cloudformation.types.refresh_all_resources.RefreshAllResources"
        ] = None,
        template_configuration: Optional[
            "capo_cloudformation.types.template_configuration.TemplateConfiguration"
        ] = None,
    ) -> "capo_cloudformation.types.update_generated_template_output.UpdateGeneratedTemplateOutput":
        """<p>Updates a generated template. This can be used to change the name, add and remove resources, refresh resources, and change the <code>DeletionPolicy</code> and <code>UpdateReplacePolicy</code> settings. You can check the status of the update to the generated template using the <code>DescribeGeneratedTemplate</code> API action.</p>

        Args:
            generated_template_name: <p>The name or Amazon Resource Name (ARN) of a generated template.</p>
            new_generated_template_name: <p>An optional new name to assign to the generated template.</p>
            add_resources: <p>An optional list of resources to be added to the generated template.</p>
            remove_resources: <p>A list of logical ids for resources to remove from the generated template.</p>
            refresh_all_resources: <p>If <code>true</code>, update the resource properties in the generated template with their current live state. This feature is useful when the resource properties in your generated a template does not reflect the live state of the resource properties. This happens when a user update the resource properties after generating a template.</p>
            template_configuration: <p>The configuration details of the generated template, including the <code>DeletionPolicy</code> and <code>UpdateReplacePolicy</code>.</p>

        Raises:
            capo_cloudformation.errors.already_exists_exception.AlreadyExistsException: <p>The resource with the name requested already exists.</p>
            capo_cloudformation.errors.generated_template_not_found_exception.GeneratedTemplateNotFoundException: <p>The generated template was not found.</p>
            capo_cloudformation.errors.limit_exceeded_exception.LimitExceededException: <p>The quota for the resource has already been reached.</p> <p>For information about resource and stack limitations, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cloudformation-limits.html">CloudFormation quotas</a> in the <i>CloudFormation User Guide</i>.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.

        Examples:
            To add resources to a generated template
            This example adds resources to a generated template

            >>> client.update_generated_template(generated_template_name='JazzyTemplate', add_resources=[{'ResourceType': 'AWS::S3::Bucket', 'ResourceIdentifier': {'BucketName': 'jazz-bucket'}}, {'ResourceType': 'AWS::EC2::DHCPOptions', 'ResourceIdentifier': {'DhcpOptionsId': 'random-id123'}}])
            To update a generated template's name
            This example updates a generated template with a new name.

            >>> client.update_generated_template(generated_template_name='JazzyTemplate', new_generated_template_name='JazzierTemplate')
            To remove resources from a generated template
            This example removes resources from a generated template

            >>> client.update_generated_template(generated_template_name='JazzyTemplate', remove_resources=['LogicalResourceId1', 'LogicalResourceId2'])
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.update_generated_template_input.UpdateGeneratedTemplateInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.update_generated_template_output.UpdateGeneratedTemplateOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.update_generated_template

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.update_generated_template.update_generated_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.update_generated_template_input.UpdateGeneratedTemplateInput = {}
        if generated_template_name is not None:
            input_["generated_template_name"] = generated_template_name
        if new_generated_template_name is not None:
            input_["new_generated_template_name"] = new_generated_template_name
        if add_resources is not None:
            input_["add_resources"] = add_resources
        if remove_resources is not None:
            input_["remove_resources"] = remove_resources
        if refresh_all_resources is not None:
            input_["refresh_all_resources"] = refresh_all_resources
        if template_configuration is not None:
            input_["template_configuration"] = template_configuration

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stack(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_name: Optional["capo_cloudformation.types.stack_name.StackName"] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
        use_previous_template: Optional[
            "capo_cloudformation.types.use_previous_template.UsePreviousTemplate"
        ] = None,
        stack_policy_during_update_body: Optional[
            "capo_cloudformation.types.stack_policy_during_update_body.StackPolicyDuringUpdateBody"
        ] = None,
        stack_policy_during_update_url: Optional[
            "capo_cloudformation.types.stack_policy_during_update_url.StackPolicyDuringUpdateURL"
        ] = None,
        parameters: Optional["capo_cloudformation.types.parameters.Parameters"] = None,
        capabilities: Optional[
            "capo_cloudformation.types.capabilities.Capabilities"
        ] = None,
        resource_types: Optional[
            "capo_cloudformation.types.resource_types.ResourceTypes"
        ] = None,
        role_arn: Optional["capo_cloudformation.types.role_arn.RoleARN"] = None,
        rollback_configuration: Optional[
            "capo_cloudformation.types.rollback_configuration.RollbackConfiguration"
        ] = None,
        stack_policy_body: Optional[
            "capo_cloudformation.types.stack_policy_body.StackPolicyBody"
        ] = None,
        stack_policy_url: Optional[
            "capo_cloudformation.types.stack_policy_url.StackPolicyURL"
        ] = None,
        notification_ar_ns: Optional[
            "capo_cloudformation.types.notification_ar_ns.NotificationARNs"
        ] = None,
        tags: Optional["capo_cloudformation.types.tags.Tags"] = None,
        disable_rollback: Optional[
            "capo_cloudformation.types.disable_rollback.DisableRollback"
        ] = None,
        client_request_token: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        retain_except_on_create: Optional[
            "capo_cloudformation.types.retain_except_on_create.RetainExceptOnCreate"
        ] = None,
        deployment_config: Optional[
            "capo_cloudformation.types.deployment_config.DeploymentConfig"
        ] = None,
        disable_validation: Optional[
            "capo_cloudformation.types.disable_validation.DisableValidation"
        ] = None,
    ) -> "capo_cloudformation.types.update_stack_output.UpdateStackOutput":
        """<p>Updates a stack as specified in the template. After the call completes successfully, the stack update starts. You can check the status of the stack through the <a>DescribeStacks</a> action.</p> <p>To get a copy of the template for an existing stack, you can use the <a>GetTemplate</a> action.</p> <p>For more information about updating a stack and monitoring the progress of the update, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html">Managing Amazon Web Services resources as a single unit with CloudFormation stacks</a> in the <i>CloudFormation User Guide</i>.</p>

        Args:
            stack_name: <p>The name or unique stack ID of the stack to update.</p>
            template_body: <p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
            template_url: <p>The URL of a file that contains the template body. The URL must point to a template that's located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
            use_previous_template: <p>Reuse the existing template that is associated with the stack that you are updating.</p> <p>When using templates with the <code>AWS::LanguageExtensions</code> transform, provide the template instead of using <code>UsePreviousTemplate</code> to ensure new parameter values and Systems Manager parameter updates are applied correctly. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/transform-aws-languageextensions.html">AWS::LanguageExtensions transform</a>.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code>, <code>TemplateURL</code>, or set the <code>UsePreviousTemplate</code> to <code>true</code>.</p>
            stack_policy_during_update_body: <p>Structure that contains the temporary overriding stack policy body. You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>
            stack_policy_during_update_url: <p>Location of a file that contains the temporary overriding stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>You can specify either the <code>StackPolicyDuringUpdateBody</code> or the <code>StackPolicyDuringUpdateURL</code> parameter, but not both.</p> <p>If you want to update protected resources, specify a temporary overriding stack policy during this update. If you don't specify a stack policy, the current policy that is associated with the stack will be used.</p>
            parameters: <p>A list of <code>Parameter</code> structures that specify input parameters for the stack. For more information, see the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_Parameter.html">Parameter</a> data type.</p>
            capabilities: <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the stack.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account, for example, by creating new IAM users. For those stacks, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we suggest that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html"> AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html"> AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-managedpolicy.html"> AWS::IAM::ManagedPolicy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html">AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html"> AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html"> AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some template contain macros. Macros perform custom processing on templates; this can include simple actions like find-and-replace operations, all the way to extensive transformations of entire templates. Because of this, users typically create a change set from the processed template, so that they can review the changes resulting from the macros before actually updating the stack. If your stack template contains one or more macros, and you choose to update a stack directly from the processed template, without first reviewing the resulting changes in a change set, you must acknowledge this capability. This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.</p> <p>If you want to update a stack from a stack template that contains macros <i>and</i> nested stacks, you must update the stack directly from the template using this capability.</p> <important> <p>You should only update stacks directly from a stack template that contains macros if you know what processing the macro performs.</p> <p>Each macro relies on an underlying Lambda service function for processing stack templates. Be aware that the Lambda function owner can update the function operation without CloudFormation being notified.</p> </important> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> </li> </ul> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>
            resource_types: <p>Specifies which resource types you can work with, such as <code>AWS::EC2::Instance</code> or <code>Custom::MyCustomInstance</code>.</p> <p>If the list of resource types doesn't include a resource that you're updating, the stack update fails. By default, CloudFormation grants permissions to all resource types. IAM uses this parameter for CloudFormation-specific condition keys in IAM policies. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html">Control CloudFormation access with Identity and Access Management</a>.</p> <note> <p>Only one of the <code>Capabilities</code> and <code>ResourceType</code> parameters can be specified.</p> </note>
            role_arn: <p>The Amazon Resource Name (ARN) of an IAM role that CloudFormation assumes to update the stack. CloudFormation uses the role's credentials to make calls on your behalf. CloudFormation always uses this role for all future operations on the stack. Provided that users have permission to operate on the stack, CloudFormation uses this role even if the users don't have permission to pass it. Ensure that the role grants least privilege.</p> <p>If you don't specify a value, CloudFormation uses the role that was previously associated with the stack. If no role is available, CloudFormation uses a temporary session that is generated from your user credentials.</p>
            rollback_configuration: <p>The rollback triggers for CloudFormation to monitor during stack creation and updating operations, and for the specified monitoring period afterwards.</p>
            stack_policy_body: <p>Structure that contains a new stack policy body. You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>
            stack_policy_url: <p>Location of a file that contains the updated stack policy. The URL must point to a policy (max size: 16KB) located in an S3 bucket in the same Region as the stack. The location for an Amazon S3 bucket must start with <code>https://</code>. URLs from S3 static websites are not supported.</p> <p>You can specify either the <code>StackPolicyBody</code> or the <code>StackPolicyURL</code> parameter, but not both.</p> <p>You might update the stack policy, for example, in order to protect a new resource that you created during a stack update. If you don't specify a stack policy, the current policy that is associated with the stack is unchanged.</p>
            notification_ar_ns: <p>Amazon Simple Notification Service topic Amazon Resource Names (ARNs) that CloudFormation associates with the stack. Specify an empty list to remove all notification topics.</p>
            tags: <p>Key-value pairs to associate with this stack. CloudFormation also propagates these tags to supported resources in the stack. You can specify a maximum number of 50 tags.</p> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags. If you specify an empty value, CloudFormation removes all associated tags.</p>
            disable_rollback: <p>Preserve the state of previously provisioned resources when an operation fails.</p> <p>Default: <code>False</code> </p>
            client_request_token: <p>A unique identifier for this <code>UpdateStack</code> request. Specify this token if you plan to retry requests so that CloudFormation knows that you're not attempting to update a stack with the same name. You might retry <code>UpdateStack</code> requests to ensure that CloudFormation successfully received them.</p> <p>All events triggered by a given stack operation are assigned the same client request token, which you can use to track operations. For example, if you execute a <code>CreateStack</code> operation with the token <code>token1</code>, then all the <code>StackEvents</code> generated by that operation will have <code>ClientRequestToken</code> set as <code>token1</code>.</p> <p>In the console, stack operations display the client request token on the Events tab. Stack operations that are initiated from the console use the token format <i>Console-StackOperation-ID</i>, which helps you easily identify the stack operation . For example, if you create a stack using the console, each stack event would be assigned the same token in the following format: <code>Console-CreateStack-7f59c3cf-00d2-40c7-b2ff-e75db0987002</code>.</p>
            retain_except_on_create: <p>When set to <code>true</code>, newly created resources are deleted when the operation rolls back. This includes newly created resources marked with a deletion policy of <code>Retain</code>.</p> <p>Default: <code>false</code> </p>
            deployment_config: <p>The deployment configuration for this stack operation, including the deployment mode.</p>
            disable_validation: <p> Set to <code>true</code> to disable pre-deployment validations in changeset or stack operations. </p> <p> Default: <code>false</code> </p>

        Raises:
            capo_cloudformation.errors.insufficient_capabilities_exception.InsufficientCapabilitiesException: <p>The template contains resources with capabilities that weren't specified in the Capabilities parameter.</p>
            capo_cloudformation.errors.token_already_exists_exception.TokenAlreadyExistsException: <p>A client request token already exists.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.update_stack_input.UpdateStackInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.update_stack_output.UpdateStackOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.update_stack

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.update_stack.update_stack(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.update_stack_input.UpdateStackInput = {}
        if stack_name is not None:
            input_["stack_name"] = stack_name
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url
        if use_previous_template is not None:
            input_["use_previous_template"] = use_previous_template
        if stack_policy_during_update_body is not None:
            input_["stack_policy_during_update_body"] = stack_policy_during_update_body
        if stack_policy_during_update_url is not None:
            input_["stack_policy_during_update_url"] = stack_policy_during_update_url
        if parameters is not None:
            input_["parameters"] = parameters
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if resource_types is not None:
            input_["resource_types"] = resource_types
        if role_arn is not None:
            input_["role_arn"] = role_arn
        if rollback_configuration is not None:
            input_["rollback_configuration"] = rollback_configuration
        if stack_policy_body is not None:
            input_["stack_policy_body"] = stack_policy_body
        if stack_policy_url is not None:
            input_["stack_policy_url"] = stack_policy_url
        if notification_ar_ns is not None:
            input_["notification_ar_ns"] = notification_ar_ns
        if tags is not None:
            input_["tags"] = tags
        if disable_rollback is not None:
            input_["disable_rollback"] = disable_rollback
        if client_request_token is not None:
            input_["client_request_token"] = client_request_token
        if retain_except_on_create is not None:
            input_["retain_except_on_create"] = retain_except_on_create
        if deployment_config is not None:
            input_["deployment_config"] = deployment_config
        if disable_validation is not None:
            input_["disable_validation"] = disable_validation

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stack_instances(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name_or_id.StackSetNameOrId"
        ] = None,
        accounts: Optional["capo_cloudformation.types.account_list.AccountList"] = None,
        deployment_targets: Optional[
            "capo_cloudformation.types.deployment_targets.DeploymentTargets"
        ] = None,
        regions: Optional["capo_cloudformation.types.region_list.RegionList"] = None,
        parameter_overrides: Optional[
            "capo_cloudformation.types.parameters.Parameters"
        ] = None,
        operation_preferences: Optional[
            "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
    ) -> "capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput":
        """<p>Updates the parameter values for stack instances for the specified accounts, within the specified Amazon Web Services Regions. A stack instance refers to a stack in a specific account and Region.</p> <p>You can only update stack instances in Amazon Web Services Regions and accounts where they already exist; to create additional stack instances, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateStackInstances.html">CreateStackInstances</a>.</p> <p>During StackSet updates, any parameters overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only update the parameter <i>values</i> that are specified in the StackSet. To add or delete a parameter itself, use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update the StackSet template. If you add a parameter to a template, before you can override the parameter value specified in the StackSet you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the StackSet. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p> <note> <p>The maximum number of organizational unit (OUs) supported by a <code>UpdateStackInstances</code> operation is 50.</p> <p>If you need more than 50, consider the following options:</p> <ul> <li> <p> <i>Batch processing:</i> If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each.</p> </li> <li> <p> <i>Parent OU strategy:</i> If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.</p> </li> </ul> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet associated with the stack instances.</p>
            accounts: <p>[Self-managed permissions] The account IDs of one or more Amazon Web Services accounts in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
            deployment_targets: <p>[Service-managed permissions] The Organizations accounts in which you want to update parameter values for stack instances. If your update targets OUs, the overridden parameter values only apply to the accounts that are currently in the target OUs and their child OUs. Accounts added to the target OUs and their child OUs in the future won't use the overridden values.</p> <p>You can specify <code>Accounts</code> or <code>DeploymentTargets</code>, but not both.</p>
            regions: <p>The names of one or more Amazon Web Services Regions in which you want to update parameter values for stack instances. The overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions.</p>
            parameter_overrides: <p>A list of input parameters whose values you want to update for the specified stack instances.</p> <p>Any overridden parameter values will be applied to all stack instances in the specified accounts and Amazon Web Services Regions. When specifying parameters and their values, be aware of how CloudFormation sets parameter values during stack instance update operations:</p> <ul> <li> <p>To override the current value for a parameter, include the parameter and specify its value.</p> </li> <li> <p>To leave an overridden parameter set to its present value, include the parameter and specify <code>UsePreviousValue</code> as <code>true</code>. (You can't specify both a value and set <code>UsePreviousValue</code> to <code>true</code>.)</p> </li> <li> <p>To set an overridden parameter back to the value specified in the StackSet, specify a parameter list but don't include the parameter in the list.</p> </li> <li> <p>To leave all parameters set to their present values, don't specify this property at all.</p> </li> </ul> <p>During StackSet updates, any parameter values overridden for a stack instance aren't updated, but retain their overridden value.</p> <p>You can only override the parameter <i>values</i> that are specified in the StackSet. To add or delete a parameter itself, use <code>UpdateStackSet</code> to update the StackSet template. If you add a parameter to a template, before you can override the parameter value specified in the StackSet you must first use <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_UpdateStackSet.html">UpdateStackSet</a> to update all stack instances with the updated template and parameter value specified in the StackSet. Once a stack instance has been updated with the new parameter, you can then override the parameter value using <code>UpdateStackInstances</code>.</p>
            operation_preferences: <p>Preferences for how CloudFormation performs this StackSet operation.</p>
            operation_id: <p>The unique identifier for this StackSet operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the StackSet operation only once, even if you retry the request multiple times. You might retry StackSet operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, the SDK generates one automatically.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_id_already_exists_exception.OperationIdAlreadyExistsException: <p>The specified operation ID already exists.</p>
            capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException: <p>Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.</p>
            capo_cloudformation.errors.stack_instance_not_found_exception.StackInstanceNotFoundException: <p>The specified stack instance doesn't exist.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.stale_request_exception.StaleRequestException: <p>Another operation has been performed on this StackSet since the specified operation was performed.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.update_stack_instances_input.UpdateStackInstancesInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.update_stack_instances_output.UpdateStackInstancesOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.update_stack_instances

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.update_stack_instances.update_stack_instances(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.update_stack_instances_input.UpdateStackInstancesInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if accounts is not None:
            input_["accounts"] = accounts
        if deployment_targets is not None:
            input_["deployment_targets"] = deployment_targets
        if regions is not None:
            input_["regions"] = regions
        if parameter_overrides is not None:
            input_["parameter_overrides"] = parameter_overrides
        if operation_preferences is not None:
            input_["operation_preferences"] = operation_preferences
        if operation_id is None:
            operation_id = str(uuid.uuid4())
        input_["operation_id"] = operation_id
        if call_as is not None:
            input_["call_as"] = call_as

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_stack_set(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        stack_set_name: Optional[
            "capo_cloudformation.types.stack_set_name.StackSetName"
        ] = None,
        description: Optional[
            "capo_cloudformation.types.description.Description"
        ] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
        use_previous_template: Optional[
            "capo_cloudformation.types.use_previous_template.UsePreviousTemplate"
        ] = None,
        parameters: Optional["capo_cloudformation.types.parameters.Parameters"] = None,
        capabilities: Optional[
            "capo_cloudformation.types.capabilities.Capabilities"
        ] = None,
        tags: Optional["capo_cloudformation.types.tags.Tags"] = None,
        operation_preferences: Optional[
            "capo_cloudformation.types.stack_set_operation_preferences.StackSetOperationPreferences"
        ] = None,
        administration_role_arn: Optional[
            "capo_cloudformation.types.role_arn.RoleARN"
        ] = None,
        execution_role_name: Optional[
            "capo_cloudformation.types.execution_role_name.ExecutionRoleName"
        ] = None,
        deployment_targets: Optional[
            "capo_cloudformation.types.deployment_targets.DeploymentTargets"
        ] = None,
        permission_model: Optional[
            "capo_cloudformation.types.permission_models.PermissionModels"
        ] = None,
        auto_deployment: Optional[
            "capo_cloudformation.types.auto_deployment.AutoDeployment"
        ] = None,
        operation_id: Optional[
            "capo_cloudformation.types.client_request_token.ClientRequestToken"
        ] = None,
        accounts: Optional["capo_cloudformation.types.account_list.AccountList"] = None,
        regions: Optional["capo_cloudformation.types.region_list.RegionList"] = None,
        call_as: Optional["capo_cloudformation.types.call_as.CallAs"] = None,
        managed_execution: Optional[
            "capo_cloudformation.types.managed_execution.ManagedExecution"
        ] = None,
    ) -> "capo_cloudformation.types.update_stack_set_output.UpdateStackSetOutput":
        """<p>Updates the StackSet and associated stack instances in the specified accounts and Amazon Web Services Regions.</p> <p>Even if the StackSet operation created by updating the StackSet fails (completely or partially, below or above a specified failure tolerance), the StackSet is updated with your changes. Subsequent <a>CreateStackInstances</a> calls on the specified StackSet use the updated StackSet.</p> <note> <p>The maximum number of organizational unit (OUs) supported by a <code>UpdateStackSet</code> operation is 50.</p> <p>If you need more than 50, consider the following options:</p> <ul> <li> <p> <i>Batch processing:</i> If you don't want to expose your OU hierarchy, split up the operations into multiple calls with less than 50 OUs each.</p> </li> <li> <p> <i>Parent OU strategy:</i> If you don't mind exposing the OU hierarchy, target a parent OU that contains all desired child OUs.</p> </li> </ul> </note>

        Args:
            stack_set_name: <p>The name or unique ID of the StackSet that you want to update.</p>
            description: <p>A brief description of updates that you are making.</p>
            template_body: <p>The structure that contains the template body, with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>
            template_url: <p>The URL of a file that contains the template body. The URL must point to a template (maximum size: 1 MB) that is located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>. S3 static website URLs are not supported.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>
            use_previous_template: <p>Use the existing template that's associated with the StackSet that you're updating.</p> <p>Conditional: You must specify only one of the following parameters: <code>TemplateBody</code> or <code>TemplateURL</code>—or set <code>UsePreviousTemplate</code> to true.</p>
            parameters: <p>A list of input parameters for the StackSet template.</p>
            capabilities: <p>In some cases, you must explicitly acknowledge that your stack template contains certain capabilities in order for CloudFormation to update the StackSet and its associated stack instances.</p> <ul> <li> <p> <code>CAPABILITY_IAM</code> and <code>CAPABILITY_NAMED_IAM</code> </p> <p>Some stack templates might include resources that can affect permissions in your Amazon Web Services account, for example, by creating new IAM users. For those stacks sets, you must explicitly acknowledge this by specifying one of these capabilities.</p> <p>The following IAM resources require you to specify either the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> capability.</p> <ul> <li> <p>If you have IAM resources, you can specify either capability.</p> </li> <li> <p>If you have IAM resources with custom names, you <i>must</i> specify <code>CAPABILITY_NAMED_IAM</code>.</p> </li> <li> <p>If you don't specify either of these capabilities, CloudFormation returns an <code>InsufficientCapabilities</code> error.</p> </li> </ul> <p>If your stack template contains these resources, we recommend that you review all permissions associated with them and edit their permissions if necessary.</p> <ul> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-accesskey.html">AWS::IAM::AccessKey</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-group.html">AWS::IAM::Group</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-instanceprofile.html">AWS::IAM::InstanceProfile</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-policy.html">AWS::IAM::Policy</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-role.html">AWS::IAM::Role</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-user.html">AWS::IAM::User</a> </p> </li> <li> <p> <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iam-usertogroupaddition.html">AWS::IAM::UserToGroupAddition</a> </p> </li> </ul> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities">Acknowledging IAM resources in CloudFormation templates</a>.</p> </li> <li> <p> <code>CAPABILITY_AUTO_EXPAND</code> </p> <p>Some templates reference macros. If your StackSet template references one or more macros, you must update the StackSet directly from the processed template, without first reviewing the resulting changes in a change set. To update the StackSet directly, you must acknowledge this capability. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-macros.html">Perform custom processing on CloudFormation templates with template macros</a>.</p> <important> <p>StackSets with service-managed permissions do not currently support the use of macros in templates. (This includes the <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-include.html">AWS::Include</a> and <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/transform-aws-serverless.html">AWS::Serverless</a> transforms, which are macros hosted by CloudFormation.) Even if you specify this capability for a StackSet with service-managed permissions, if you reference a macro in your template the StackSet operation will fail.</p> </important> </li> </ul>
            tags: <p>The key-value pairs to associate with this StackSet and the stacks created from it. CloudFormation also propagates these tags to supported resources that are created in the stacks. You can specify a maximum number of 50 tags.</p> <p>If you specify tags for this parameter, those tags replace any list of tags that are currently associated with this StackSet. This means:</p> <ul> <li> <p>If you don't specify this parameter, CloudFormation doesn't modify the stack's tags.</p> </li> <li> <p>If you specify <i>any</i> tags using this parameter, you must specify <i>all</i> the tags that you want associated with this StackSet, even tags you've specified before (for example, when creating the StackSet or during a previous update of the StackSet.). Any tags that you don't include in the updated list of tags are removed from the StackSet, and therefore from the stacks and resources as well.</p> </li> <li> <p>If you specify an empty value, CloudFormation removes all currently associated tags.</p> </li> </ul> <p>If you specify new tags as part of an <code>UpdateStackSet</code> action, CloudFormation checks to see if you have the required IAM permission to tag resources. If you omit tags that are currently associated with the StackSet from the list of tags you specify, CloudFormation assumes that you want to remove those tags from the StackSet, and checks to see if you have permission to untag resources. If you don't have the necessary permission(s), the entire <code>UpdateStackSet</code> action fails with an <code>access denied</code> error, and the StackSet is not updated.</p>
            operation_preferences: <p>Preferences for how CloudFormation performs this StackSet operation.</p>
            administration_role_arn: <p>[Self-managed permissions] The Amazon Resource Name (ARN) of the IAM role to use to update this StackSet.</p> <p>Specify an IAM role only if you are using customized administrator roles to control which users or groups can manage specific StackSets within the same administrator account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a> in the <i>CloudFormation User Guide</i>.</p> <p>If you specified a customized administrator role when you created the StackSet, you must specify a customized administrator role, even if it is the same customized administrator role used with this StackSet previously.</p>
            execution_role_name: <p>[Self-managed permissions] The name of the IAM execution role to use to update the stack set. If you do not specify an execution role, CloudFormation uses the <code>AWSCloudFormationStackSetExecutionRole</code> role for the StackSet operation.</p> <p>Specify an IAM role only if you are using customized execution roles to control which stack resources users and groups can include in their StackSets.</p> <p>If you specify a customized execution role, CloudFormation uses that role to update the stack. If you do not specify a customized execution role, CloudFormation performs the update using the role previously associated with the StackSet, so long as you have permissions to perform operations on the StackSet.</p>
            deployment_targets: <p>[Service-managed permissions] The Organizations accounts in which to update associated stack instances.</p> <p>To update all the stack instances associated with this StackSet, do not specify <code>DeploymentTargets</code> or <code>Regions</code>.</p> <p>If the StackSet update includes changes to the template (that is, if <code>TemplateBody</code> or <code>TemplateURL</code> is specified), or the <code>Parameters</code>, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the StackSet update doesn't include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>
            permission_model: <p>Describes how the IAM roles required for StackSet operations are created. You cannot modify <code>PermissionModel</code> if there are stack instances associated with your stack set.</p> <ul> <li> <p>With <code>self-managed</code> permissions, you must create the administrator and execution roles required to deploy to target accounts. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-prereqs-self-managed.html">Grant self-managed permissions</a>.</p> </li> <li> <p>With <code>service-managed</code> permissions, StackSets automatically creates the IAM roles required to deploy to accounts managed by Organizations. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-activate-trusted-access.html">Activate trusted access for StackSets with Organizations</a>.</p> </li> </ul>
            auto_deployment: <p>[Service-managed permissions] Describes whether StackSets automatically deploys to Organizations accounts that are added to a target organization or organizational unit (OU). For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-manage-auto-deployment.html">Enable or disable automatic deployments for StackSets in Organizations</a> in the <i>CloudFormation User Guide</i>.</p> <p>If you specify <code>AutoDeployment</code>, don't specify <code>DeploymentTargets</code> or <code>Regions</code>.</p>
            operation_id: <p>The unique ID for this StackSet operation.</p> <p>The operation ID also functions as an idempotency token, to ensure that CloudFormation performs the StackSet operation only once, even if you retry the request multiple times. You might retry StackSet operation requests to ensure that CloudFormation successfully received them.</p> <p>If you don't specify an operation ID, CloudFormation generates one automatically.</p> <p>Repeating this StackSet operation with a new operation ID retries all stack instances whose status is <code>OUTDATED</code>.</p>
            accounts: <p>[Self-managed permissions] The accounts in which to update associated stack instances. If you specify accounts, you must also specify the Amazon Web Services Regions in which to update StackSet instances.</p> <p>To update <i>all</i> the stack instances associated with this StackSet, don't specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the StackSet update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Amazon Web Services Regions. If the StackSet update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Amazon Web Services Regions, while leaving all other stack instances with their existing stack instance status.</p>
            regions: <p>The Amazon Web Services Regions in which to update associated stack instances. If you specify Regions, you must also specify accounts in which to update StackSet instances.</p> <p>To update <i>all</i> the stack instances associated with this StackSet, do not specify the <code>Accounts</code> or <code>Regions</code> properties.</p> <p>If the StackSet update includes changes to the template (that is, if the <code>TemplateBody</code> or <code>TemplateURL</code> properties are specified), or the <code>Parameters</code> property, CloudFormation marks all stack instances with a status of <code>OUTDATED</code> prior to updating the stack instances in the specified accounts and Regions. If the StackSet update does not include changes to the template or parameters, CloudFormation updates the stack instances in the specified accounts and Regions, while leaving all other stack instances with their existing stack instance status.</p>
            call_as: <p>[Service-managed permissions] Specifies whether you are acting as an account administrator in the organization's management account or as a delegated administrator in a member account.</p> <p>By default, <code>SELF</code> is specified. Use <code>SELF</code> for StackSets with self-managed permissions.</p> <ul> <li> <p>If you are signed in to the management account, specify <code>SELF</code>.</p> </li> <li> <p>If you are signed in to a delegated administrator account, specify <code>DELEGATED_ADMIN</code>.</p> <p>Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html">Register a delegated administrator</a> in the <i>CloudFormation User Guide</i>.</p> </li> </ul>
            managed_execution: <p>Describes whether CloudFormation performs non-conflicting operations concurrently and queues conflicting operations.</p>

        Raises:
            capo_cloudformation.errors.invalid_operation_exception.InvalidOperationException: <p>The specified operation isn't valid.</p>
            capo_cloudformation.errors.operation_id_already_exists_exception.OperationIdAlreadyExistsException: <p>The specified operation ID already exists.</p>
            capo_cloudformation.errors.operation_in_progress_exception.OperationInProgressException: <p>Another operation is currently in progress for this StackSet. Only one operation can be performed for a stack set at a given time.</p>
            capo_cloudformation.errors.stack_instance_not_found_exception.StackInstanceNotFoundException: <p>The specified stack instance doesn't exist.</p>
            capo_cloudformation.errors.stack_set_not_found_exception.StackSetNotFoundException: <p>The specified StackSet doesn't exist.</p>
            capo_cloudformation.errors.stale_request_exception.StaleRequestException: <p>Another operation has been performed on this StackSet since the specified operation was performed.</p>
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.update_stack_set_input.UpdateStackSetInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.update_stack_set_output.UpdateStackSetOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.update_stack_set

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.update_stack_set.update_stack_set(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.update_stack_set_input.UpdateStackSetInput = {}
        if stack_set_name is not None:
            input_["stack_set_name"] = stack_set_name
        if description is not None:
            input_["description"] = description
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url
        if use_previous_template is not None:
            input_["use_previous_template"] = use_previous_template
        if parameters is not None:
            input_["parameters"] = parameters
        if capabilities is not None:
            input_["capabilities"] = capabilities
        if tags is not None:
            input_["tags"] = tags
        if operation_preferences is not None:
            input_["operation_preferences"] = operation_preferences
        if administration_role_arn is not None:
            input_["administration_role_arn"] = administration_role_arn
        if execution_role_name is not None:
            input_["execution_role_name"] = execution_role_name
        if deployment_targets is not None:
            input_["deployment_targets"] = deployment_targets
        if permission_model is not None:
            input_["permission_model"] = permission_model
        if auto_deployment is not None:
            input_["auto_deployment"] = auto_deployment
        if operation_id is None:
            operation_id = str(uuid.uuid4())
        input_["operation_id"] = operation_id
        if accounts is not None:
            input_["accounts"] = accounts
        if regions is not None:
            input_["regions"] = regions
        if call_as is not None:
            input_["call_as"] = call_as
        if managed_execution is not None:
            input_["managed_execution"] = managed_execution

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def update_termination_protection(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        enable_termination_protection: Optional[
            "capo_cloudformation.types.enable_termination_protection.EnableTerminationProtection"
        ] = None,
        stack_name: Optional[
            "capo_cloudformation.types.stack_name_or_id.StackNameOrId"
        ] = None,
    ) -> "capo_cloudformation.types.update_termination_protection_output.UpdateTerminationProtectionOutput":
        """<p>Updates termination protection for the specified stack. If a user attempts to delete a stack with termination protection enabled, the operation fails and the stack remains unchanged. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-protect-stacks.html">Protect a CloudFormation stack from being deleted</a> in the <i>CloudFormation User Guide</i>.</p> <p>For <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-nested-stacks.html">nested stacks</a>, termination protection is set on the root stack and can't be changed directly on the nested stack.</p>

        Args:
            enable_termination_protection: <p>Whether to enable termination protection on the specified stack.</p>
            stack_name: <p>The name or unique ID of the stack for which you want to set termination protection.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.update_termination_protection_input.UpdateTerminationProtectionInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.update_termination_protection_output.UpdateTerminationProtectionOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.update_termination_protection

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.update_termination_protection.update_termination_protection(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.update_termination_protection_input.UpdateTerminationProtectionInput = {}
        if enable_termination_protection is not None:
            input_["enable_termination_protection"] = enable_termination_protection
        if stack_name is not None:
            input_["stack_name"] = stack_name

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        response.response.close()
        return response.output

    def validate_template(
        self,
        *,
        config_overrides: Optional[CloudFormationClientConfig] = None,
        template_body: Optional[
            "capo_cloudformation.types.template_body.TemplateBody"
        ] = None,
        template_url: Optional[
            "capo_cloudformation.types.template_url.TemplateURL"
        ] = None,
    ) -> "capo_cloudformation.types.validate_template_output.ValidateTemplateOutput":
        """<p>Validates a specified template. CloudFormation first checks if the template is valid JSON. If it isn't, CloudFormation checks if the template is valid YAML. If both these checks fail, CloudFormation returns a template validation error.</p>

        Args:
            template_body: <p>Structure that contains the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>
            template_url: <p>The URL of a file that contains the template body. The URL must point to a template (max size: 1 MB) that is located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with <code>https://</code>.</p> <p>Conditional: You must pass <code>TemplateURL</code> or <code>TemplateBody</code>. If both are passed, only <code>TemplateBody</code> is used.</p>

        Raises:
            capo_cloudformation.errors.UnknownServiceError: The service returned an error code this client does not model.
        """

        def _handler(
            req: "OperationRequest[capo_cloudformation.types.validate_template_input.ValidateTemplateInput]",
        ) -> OperationResponse[
            "capo_cloudformation.types.validate_template_output.ValidateTemplateOutput"
        ]:
            import capo_cloudformation._operations.cloud_formation.validate_template

            output, http_response = (
                capo_cloudformation._operations.cloud_formation.validate_template.validate_template(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self.operation_options(config_overrides)
        input_: capo_cloudformation.types.validate_template_input.ValidateTemplateInput = {}
        if template_body is not None:
            input_["template_body"] = template_body
        if template_url is not None:
            input_["template_url"] = template_url

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
